from ollama._types import ListResponse, ModelDetails

from common.markdown_utils import dicts_to_markdown_table, display_markdown
from harness_commands.abstract import AbstractHarnessCommand


class ListModelsCommand(AbstractHarnessCommand):
    @property
    def command(self) -> str:
        return "list-models"

    async def execute(self, args: list[str]) -> None:
        list_response: ListResponse = await self.client().list()

        FIELDS_TO_EXCLUDE = ["modified_at", "parent_model", "families"]

        model_dicts = [
            {k: v for k, v in model.__dict__.items() if k not in FIELDS_TO_EXCLUDE} for model in list_response.models
        ]

        for model_dict in model_dicts:
            model_dict["digest"] = model_dict["digest"][:8] + "..." + model_dict["digest"][-8:]
            details_object = model_dict.pop("details")
            details = {k: v for k, v in details_object.__dict__.items() if k not in FIELDS_TO_EXCLUDE}
            model_dict.update(details)

        model_dicts = sorted(model_dicts, key=lambda d: d["model"])

        display_markdown(dicts_to_markdown_table(model_dicts))
