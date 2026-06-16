from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Sequence

from ollama import AsyncClient
from rich.console import Console

from config import YokeConfig


class AbstractHarnessCommand(ABC):
    def __init__(
        self,
        config: YokeConfig,
        async_client: AsyncClient,
        console: Console,
        commands: Sequence[AbstractHarnessCommand],
    ):
        self.config: YokeConfig = config
        self.client: AsyncClient = async_client
        self.console: Console = console
        self.commands: Sequence[AbstractHarnessCommand] = commands

    @property
    @abstractmethod
    def command(self) -> str:
        raise NotImplementedError()

    @property
    def usage(self) -> str:
        return self.command

    def get_command(self, name: str) -> AbstractHarnessCommand:
        matching_commands = [c for c in self.commands if c.command == name]
        if len(matching_commands) == 0:
            raise ValueError(f"no command harness command found for {name}")
        return matching_commands[0]

    @abstractmethod
    async def execute(self, model: str, args: list[str]) -> bool:
        raise NotImplementedError()
