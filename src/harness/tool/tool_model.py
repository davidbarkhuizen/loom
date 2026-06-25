from dataclasses import dataclass
from enum import Enum
from typing import Callable


class ToolTag(Enum):
    TEMPORAL = "TEMPORAL"
    SEARCH = "SEARCH"
    MATHEMATICS = "MATHEMATICS"
    ARITHMETIC = "ARITHMETIC"
    INTERNET = "INTERNET"


@dataclass
class Tool:
    name: str
    function: Callable
    tags: list[ToolTag]
