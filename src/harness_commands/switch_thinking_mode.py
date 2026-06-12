from harness_commands.abstract import AbstractSystemCommand


class SwitchThinkingModeCommand(AbstractSystemCommand):
    @property
    def command(self) -> str:
        return "switch-thinking-mode"

    async def execute(self, args: list[str]) -> list[str]:
        thinking_mode: str = args[0]
        reconfigured: bool = self.reconfigure("thinking_mode", thinking_mode)
        return [f"thinking_mode switched to {thinking_mode}" if reconfigured else "failed to switch thinking mode"]
