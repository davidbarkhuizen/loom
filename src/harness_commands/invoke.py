from chat import communicate
from harness_commands.abstract import AbstractHarnessCommand
from model import CommunicationResponse


class InvokeCommand(AbstractHarnessCommand):
    @property
    def command(self) -> str:
        return "!"

    async def execute(self, model: str, think: bool, args: list[str]) -> None:

        text = " ".join(args)

        _: CommunicationResponse = await communicate(
            client=self.client(), model=model, system="", user=[text], think=think
        )
