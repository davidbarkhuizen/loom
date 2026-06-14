import asyncio

import loom
from config import LoomConfig, configure_from_json_file

if __name__ == "__main__":
    config: LoomConfig = configure_from_json_file()
    asyncio.run(loom.loom(config))
