from harness.harness_commands.abstract import AbstractHarnessCommand
from harness.tether import communicate
from model.model import CommunicationResponse


class InvokeCommand(AbstractHarnessCommand):
    @property
    def command(self) -> str:
        return "!"

    async def execute(self, model: str, think: bool, args: list[str]) -> None:

        text = " ".join(args)

        _: CommunicationResponse = await communicate(
            client=self.client, model=model, system="", user=[text], think=think
        )
