from ollama import AsyncClient
from rich.console import Console
from typing_extensions import Sequence

from config import YokeConfig
from harness.commands.abstract import AbstractHarnessCommand
from harness.tool.tool_registry import load_tools
from markdown.display import display_text_as_markdown
from markdown.render import dict_list_to_markdown_table


class ListToolsCommand(AbstractHarnessCommand):
    def __init__(
        self,
        config: YokeConfig,
        async_client: AsyncClient,
        console: Console,
    ):
        super().__init__(config, async_client, console)

    @property
    def command(self) -> str:
        return "list-tools"

    async def execute(self, model: str, args: list[str]) -> bool:

        tool_dicts = [{"tool": tool.name} for tool in load_tools()]
        tool_dicts = sorted(tool_dicts, key=lambda d: d["tool"])

        display_text_as_markdown(self.console, dict_list_to_markdown_table(tool_dicts, alignment="left"))

        return True
