from ollama import AsyncClient, ChatResponse


def new_client(url: str) -> AsyncClient:
    return AsyncClient(host=url)


async def connect_and_start_session(host: str, port: int, model: str):
    client: AsyncClient = new_client(f"http://{host}:{port}")

    async def invoke(invocation: str) -> str:

        message = {"content": invocation, "role": "user"}

        stream = await client.chat(model=model, messages=[message], stream=True)

        reply: str = ""

        async for part in stream:
            content: str | list[str] = part["message"]["content"]

            text: str = str(content)
            reply += text
            print(text, end="", flush=True)

        return reply

    async def execute_harness_command(command: str, args: list[str]) -> list[str]:
        return list(["execute_harness_command"])

    while (invocation := input("> ")) != "exit":
        if invocation.startswith("!"):
            command_text = invocation.strip()[1:]
            command_response: list[str]
            match command_text.split(" "):
                case []:
                    command_response = list(["empty harness command"])
                case [command, *args]:
                    command_response = await execute_harness_command(command, args)
                case _:
                    command_response = list()
            for line in command_response:
                print(line)
        else:
            _ = await invoke(invocation)
            print()
