from pathlib import Path

from chat import communicate
from config import LoomConfig
from file_utils import read_text_file_async, write_text_file_async
from harness_commands.abstract import AbstractSystemCommand
from model import CommunicationResponse


class TaskCommand(AbstractSystemCommand):
    @property
    def command(self) -> str:
        return "task"

    async def execute(self, args: list[str]) -> list[str]:
        if len(args) == 0:
            return ["error, no task specified. usage is: task [task-name], e.g. task test"]

        task = args[0]

        config: LoomConfig = self.config()

        task_folder: Path = Path(config.task.folder) / Path(task)
        task_inputs_folder: Path = task_folder / "input"

        system_text: str = await read_text_file_async(task_inputs_folder / "system.txt")
        user_text: str = await read_text_file_async(task_inputs_folder / "user.txt")

        response: CommunicationResponse = await communicate(
            client=self.client(),
            model=config.model.model,
            system=system_text,
            user=[user_text],
            think=config.model.think,
        )

        task_outputs_folder: Path = task_folder / "output"

        await write_text_file_async(task_outputs_folder / "content.txt", response.content)

        if response.thinking:
            await write_text_file_async(task_outputs_folder / "thinking.txt", response.thinking)

        # TODO stats

        return []
