from abc import ABC, abstractmethod
from typing import Any, Callable

from ollama import AsyncClient

from config import LoomConfig


class AbstractHarnessCommand(ABC):
    def __init__(self, async_client: AsyncClient, config: LoomConfig, update_setting: Callable[[str, Any], bool]):
        self._async_client: AsyncClient = async_client
        self._config: LoomConfig = config
        self._update_setting: Callable[[str, Any], bool] = update_setting

    def client(self) -> AsyncClient:
        return self._async_client

    def update_setting(self, setting: str, value: Any) -> bool:
        return self._update_setting(setting, value)

    @property
    @abstractmethod
    def command(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    async def execute(self, model: str, think: bool, args: list[str]) -> None:
        raise NotImplementedError()
