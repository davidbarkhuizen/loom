from ollama import AsyncClient, ChatResponse


def new_client(url: str) -> AsyncClient:
    return AsyncClient(host=url)


async def connect_and_start_session(host: str, port: int, model: str):
    client: AsyncClient = new_client(f"http://{host}:{port}")

    async def communicate(text: str) -> str:

        message = {"content": text, "role": "user"}

        stream = await client.chat(model=model, messages=[message], stream=True)

        reply: list[str] = []

        async for part in stream:
            content: str | list[str] = part["message"]["content"]

            if isinstance(content, str):
                reply.append(content)
            if isinstance(content, list):
                reply.extend([str(x) for x in content])

            print(str(content), end="", flush=True)

        return reply

    while (utterance := input("> ")) != "exit":
        response = await communicate(utterance)
        print()
