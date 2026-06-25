import asyncio

from config import YokeConfig, configure_from_json_file
from harness.tool.tool_registry import load_tools
from harness.yoke import yoke

if __name__ == "__main__":
    config: YokeConfig = configure_from_json_file()
    asyncio.run(yoke(config))
