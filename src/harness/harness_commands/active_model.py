from rich.markdown import Markdown

from common.markdown import display_markdown
from harness.harness_commands.abstract import AbstractHarnessCommand


class ActiveModelCommand(AbstractHarnessCommand):
    @property
    def command(self) -> str:
        return "active-model"

    async def execute(self, model: str, think: bool, args: list[str]) -> None:
        display_markdown(Markdown(f"{model}"))
