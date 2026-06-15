from abc import ABC, abstractmethod
from typing import Any, Callable, Sequence

from ollama import AsyncClient

from config import LoomConfig


class AbstractHarnessCommand(ABC):
    def __init__(self, async_client: AsyncClient, config: LoomConfig, update_setting: Callable[[str, Any], bool]):
        self.client: AsyncClient = async_client
        self.config: LoomConfig = config
        self.update_setting: Callable[[str, Any], bool] = update_setting

    @property
    @abstractmethod
    def command(self) -> str:
        raise NotImplementedError()

    @property
    def usage(self) -> str:
        return self.command

    @abstractmethod
    async def execute(self, model: str, think: bool, args: list[str]) -> None:
        raise NotImplementedError()
