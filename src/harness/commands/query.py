from harness.commands.abstract import AbstractHarnessCommand
from harness.tether import prompt
from model.model import RawPromptRequest, RawPromptResponse


class QueryCommand(AbstractHarnessCommand):
    @property
    def command(self) -> str:
        return "?"

    @property
    def usage(self) -> str:
        return "? [natural language query]"

    async def execute(self, model: str, args: list[str]) -> bool:

        text = " ".join(args)

        _: RawPromptResponse = await prompt(self.client, model, RawPromptRequest(system_prompt="", user_prompt=[text]))

        return True
