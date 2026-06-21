from typing import Optional

from pydantic import BaseModel, Field


class ToolCool(BaseModel):
    pass


{"function": {"name": "get_weather", "arguments": {"city": "Paris"}}}
