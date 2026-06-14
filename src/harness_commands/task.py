import glob
import os
from pathlib import Path

from chat import communicate
from common.markdown import display_text_as_markdown, extract_embedded_files_from_markdown
from file_utils import read_text_file_async, write_text_file_async
from harness_commands.abstract import AbstractHarnessCommand
from model import CommunicationResponse


class TaskCommand(AbstractHarnessCommand):
    @property
    def command(self) -> str:
        return "task"

    async def execute(self, model: str, think: bool, args: list[str]) -> None:
        if len(args) == 0:
            display_text_as_markdown("error, no task specified. usage is: task [task-name], e.g. task test")

        task = args[0]

        task_folder: Path = Path(self._config.task.folder) / Path(task)
        task_inputs_folder: Path = task_folder / "input"

        system_text: str = await read_text_file_async(task_inputs_folder / "system.md")
        user_text: str = await read_text_file_async(task_inputs_folder / "user.md")

        async def context_file_block_for_files(file_paths: list[str]) -> str:
            context = []
            for path in file_paths:
                file_contents = await read_text_file_async(Path(path))
                context.append(
                    f"\n--- Begin File: {path} ---\n```python\n{file_contents}\n```\n--- End File: {path} ---\n"
                )
            return "\n".join(context)

        task_file_inputs_folder: Path = task_inputs_folder / "files"
        glob_expression = f"{task_file_inputs_folder.absolute()}/**/*.*"

        context_file_block = await context_file_block_for_files(glob.glob(glob_expression, recursive=True))

        structured_user_text: str = f"""
# user prompt

## files

{context_file_block}

## additional information

{user_text}
"""

        response: CommunicationResponse = await communicate(
            client=self.client(),
            model=model,
            system=system_text,
            user=[structured_user_text],
            think=think,
        )

        task_outputs_folder: Path = task_folder / "output"

        if response.thinking:
            await write_text_file_async(task_outputs_folder / "thinking.md", response.thinking)

        output_markdown_doc: str = response.content

        await write_text_file_async(task_outputs_folder / "output.md", output_markdown_doc)

        embedded_files: list[tuple[str, str]] = extract_embedded_files_from_markdown(output_markdown_doc)

        embedded_files_output_path: Path = task_outputs_folder / "files"
        os.makedirs(embedded_files_output_path, exist_ok=True)

        for file_contents, relative_file_path in embedded_files:
            await write_text_file_async(embedded_files_output_path / relative_file_path, file_contents)

        # TODO stats
