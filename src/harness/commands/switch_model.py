from harness.commands.abstract import AbstractHarnessCommand
from markdown.display import display_text_as_markdown


class SwitchModelCommand(AbstractHarnessCommand):
    @property
    def command(self) -> str:
        return "switch-model"

    @property
    def usage(self) -> str:
        return f"{self.command} [model]"

    async def execute(self, model: str, think: bool, args: list[str]) -> bool:
        new_model: str = args[0]

        updated: bool = self.update_setting("model", new_model)
        if not updated:
            display_text_as_markdown(self.console, "error: **failed to switch model**")
            return False

        return True
