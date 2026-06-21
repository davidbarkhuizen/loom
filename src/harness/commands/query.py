from typing_extensions import Any, Callable

from harness.commands.abstract import AbstractHarnessCommand
from harness.tether import prompt
from harness.tool.tools.time import get_current_date
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

        query_tools: list[Callable] = [get_current_date]

        initial_rq = RawPromptRequest(system_prompt="", user_prompt=[text], tools=query_tools, message_history=[])
        initial_rsp: RawPromptResponse = await prompt(self.client, model, initial_rq)

        message_history: list[dict[str, Any]] = initial_rsp.message_history

        for msg in message_history:
            print(msg)
        return False

        tool_calls = initial_rsp.tool_calls
        while len(tool_calls) > 0:
            # make each tool call
            # send the response

            rsp: RawPromptResponse = await prompt(
                self.client,
                model,
                RawPromptRequest(system_prompt="", user_prompt=[], tools=query_tools, message_history=message_history),
            )
            tool_calls = [*rsp.tool_calls]
            message_history = rsp.message_history

        return True
