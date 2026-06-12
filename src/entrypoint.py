import asyncio

from config import LoomConfig, configure_from_json_file
from loom import weave

if __name__ == "__main__":
    config: LoomConfig = configure_from_json_file()
    asyncio.run(weave(config))
