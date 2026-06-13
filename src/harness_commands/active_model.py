from harness_commands.abstract import AbstractHarnessCommand


class ActiveModelCommand(AbstractHarnessCommand):
    @property
    def command(self) -> str:
        return "active-model"

    async def execute(self, args: list[str]) -> list[str]:
        return [f"{self.config().model.model}"]
