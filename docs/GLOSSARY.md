# glossary

## ollama client

### chat method

    tools: Sequence[Mapping[str, Any] | Tool
    think: bool | Literal['low', 'medium', 'high']
    messages: Sequence[Mapping[str, Any] | Message]
    format: dict[str, Any] | Literal['', 'json']
    options: Mapping[str, Any] | Options

### role parameter

roles
- system [used to provide initial context]
- user [convey user invocation]
- assistant [last model response, used for continuity]
- tool [response to tool calls]
