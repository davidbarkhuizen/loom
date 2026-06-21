from typing import Any, Callable, Mapping

from ollama import Message

from harness.tether import new_message
from harness.tools.tools.time import get_current_date


def call_tool(tool_call: Message.ToolCall) -> dict[str, str]:

    target_tool: str = tool_call.function.name
    tool_call_arguments: Mapping[str, Any] = tool_call.function.arguments

    # get target tool
    # validate arguments
    # call target tool, passing arguments
    tool: Callable = get_current_date

    tool_call_result: str = tool(**tool_call_arguments)

    return new_message(role="tool", tool_name=target_tool, text=tool_call_result)
