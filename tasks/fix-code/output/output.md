### Problems Identified

1. **`loom.py`**: `execute_harness_command` prints an unknown command message but fails to return, causing `next(iter(matching_command))` to raise `StopIteration`.
2. **`loom.py`**: Synchronous `input()` is called inside an `async def`, blocking the event loop.
3. **`loom.py`**: `case []:` in the `match` statement is unreachable dead code since `str.split()` on a non-empty string always returns at least one element.
4. **`chat.py`**: Incorrect attribute access (`part.model`, `message.thinking`) on dictionary objects returned by the `ollama` streaming API. Should use `.get()`.
5. **`chat.py`**: Synchronous `open()` inside an `async for` loop blocks the event loop on every iteration.
6. **`chat.py`**: `bool(part.get("done", "False"))` incorrectly evaluates the non-empty string `"False"` as `True`.

---

### Fixes

**`/home/david/code/loom/tasks/fix-code/input/files/loom.py`**
```python
import asyncio
import traceback
from typing import Any

from ollama import AsyncClient

from chat import new_async_ollama_client
from common.markdown_utils import display_text_as_markdown
from config import LoomConfig
from harness_commands.abstract import AbstractHarnessCommand
from harness_commands.active_model import ActiveModelCommand
from harness_commands.invoke import InvokeCommand
from harness_commands.list_models import ListModelsCommand
from harness_commands.ps import PSCommand
from harness_commands.switch_model import SwitchModelCommand
from harness_commands.switch_thinking_mode import SwitchThinkingModeCommand
from harness_commands.task import TaskCommand

HARNESS_COMMANDS = [
    ListModelsCommand,
    SwitchModelCommand,
    ActiveModelCommand,
    SwitchThinkingModeCommand,
    InvokeCommand,
    TaskCommand,
    PSCommand,
]


async def weave(client: AsyncClient, config: LoomConfig):

    _model: str = config.ollama.default_model
    _think: bool = False

    def update_setting(setting: str, value: Any) -> bool:
        nonlocal _model
        nonlocal _think

        match setting:
            case "model":
                _model = str(value)
            case "think":
                _think = value
            case _:
                return False

        return True

    def register_harness_commands(client: AsyncClient) -> list[AbstractHarnessCommand]:
        return [X(client, config, update_setting) for X in HARNESS_COMMANDS]

    registered_harness_commands = register_harness_commands(client)

    async def execute_harness_command(command: str, args: list[str]):
        matching_command = [cmd for cmd in registered_harness_commands if cmd.command == command]
        if len(matching_command) == 0:
            display_text_as_markdown(f"unknown system command: {command}")
            return

        system_command = next(iter(matching_command))
        await system_command.execute(_model, _think, args)

    while (invocation := await asyncio.to_thread(input, f"\n{_model} > ").strip().lower()) not in ["exit", "quit"]:
        if len(invocation) == 0:
            continue

        match invocation.split(" "):
            case [command, *args]:
                await execute_harness_command(command, args)
            case _:
                continue


async def loom(config: LoomConfig):

    host: str = config.ollama.host
    port: int = config.ollama.port

    client = new_async_ollama_client(host, port)
    try:
        await weave(client, config)
    except Exception:
        traceback.print_exc()
    finally:
        await client.close()
```

**`/home/david/code/loom/tasks/fix-code/input/files/chat.py`**
```python
from typing import Any

import aiofiles
from ollama import AsyncClient

from model import ChatMessageRole, CommunicationResponse


def new_async_ollama_client(host: str, port: int) -> AsyncClient:
    url: str = f"http://{host}:{port}"
    return AsyncClient(host=url)


def new_message(role: str, text: str, think: bool) -> dict[str, Any]:
    return {"content": text, "role": role}


async def communicate(
    client: AsyncClient, model: str, system: str, user: list[str], think: bool
) -> CommunicationResponse:

    system_message = new_message(ChatMessageRole.system.value, system, think)
    user_messages = [new_message(ChatMessageRole.user.value, text, think) for text in user]

    messages: list[dict[str, Any]] = [system_message, *user_messages]

    response_text: str = ""
    thinking_text: str = ""

    stream = await client.chat(model=model, messages=messages, stream=True)

    async with aiofiles.open("log.log", "a") as log_file:
        async for part in stream:
            await log_file.write(str(part) + "\n")

            responding_model: str | None = part.get("model")
            if responding_model and responding_model != model:
                raise ValueError(
                    f"response model mismatch. requested a response from {model}, but actually received one from {responding_model}"
                )

            message = part.get("message", None)
            if message is None:
                continue

            thinking: str | None = message.get("thinking")
            if thinking:
                if not thinking_text:
                    print("\nThinking")
                    print("=-" * 40)

                thinking_text += thinking
                print(thinking, end="", flush=True)

            content: str = message.get("content", None)
            if content:
                if not response_text:
                    print("\nContent")
                    print("=-" * 40)

                response_text += content
                print(content, end="", flush=True)

            done: bool = part.get("done", False)
            if done:
                pass

    print()

    return CommunicationResponse(content=response_text, thinking=thinking_text)
```