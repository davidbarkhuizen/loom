from dataclasses import dataclass
from enum import Enum
from model.model import TextFile

from markdown.parse import extract_embedded_text_files_from_markdown


class ChatMessageRole(Enum):
    user = "user"
    system = "system"
    assistant = "assistant"


@dataclass
class CommunicationStats:
    model: str
    done_reason: str | None
    total_duration_s: float
    load_duration_ms: float
    prompt_eval_count: int
    prompt_eval_duration_s: float
    eval_count: int
    eval_duration_s: float


@dataclass
class CommunicationResponse:
    content: str
    thinking: str
    stats: CommunicationStats | None

    def embedded_text_files(self) -> list[TextFile]
        return extract_embedded_text_files_from_markdown(self.content)


@dataclass
class OllamaModel:
    name: str | None
    size_MB: int | None
    family: str | None
    format: str | None
    parameters: str | None
    quantization: str | None


@dataclass
class TextFile:
    path: str
    contents: str
