import os
import re
from typing import List

from rich.console import Console
from rich.markdown import Markdown

console = Console()


def dicts_to_markdown_table(list_of_dicts: list[dict[str, str]]) -> Markdown:
    if not list_of_dicts:
        return Markdown("")

    # Extract headers from the first dictionary's keys
    headers = list_of_dicts[0].keys()

    # Create the header row
    header_row = "| " + " | ".join(headers) + " |"
    separator_row = "|-" + "-|-".join([""] * len(headers)) + "-|"

    # Create rows for each dictionary
    rows = []
    for d in list_of_dicts:
        row = "| " + " | ".join([str(d[key]) for key in headers]) + " |"
        rows.append(row)

    # Combine all parts into the final table string
    table = header_row + "\n" + separator_row + "\n" + "\n".join(rows)

    return Markdown(table)


def display_markdown(markdown: Markdown):
    global console
    console.print(markdown)


def display_text_as_markdown(text: str):
    global console
    console.print(Markdown(text))


def extract_embedded_files_from_markdown(markdown_str: str) -> List[tuple[str, str]]:
    """
    Extracts code blocks from a markdown document

    Args:
        markdown_str: multiline markdown document string

    Returns:
        List of tuples, where each tuple is
        [ file_contents, file_path ]
    """
    code_files = []

    # Regex patterns
    #
    # Marker: **`path**`
    marker_pattern = re.compile(r"^\*\*`(.+)`\*\*$")
    # Code block start: ``` (optionally followed by language identifier)
    code_start_pattern = re.compile(r"^`{3,}")
    # Code block end: ``` (with optional whitespace)
    code_end_pattern = re.compile(r"^\s*`{3,}\s*$")

    lines = markdown_str.split("\n")

    in_code_block = False
    code_content = []
    relative_file_path = None
    prev_line = None

    for line in lines:
        line_stripped = line.rstrip("\n\r")

        if not in_code_block:
            if code_start_pattern.match(line_stripped):
                # Check previous line for marker
                if prev_line is not None:
                    match = marker_pattern.match(prev_line.strip())
                    if match:
                        relative_file_path = match.group(1)
                        in_code_block = True
                        code_content = []
            # Update prev_line for next iteration
            prev_line = line_stripped
        else:
            if code_end_pattern.match(line_stripped):
                code_files.append(("\n".join(code_content), relative_file_path))
                in_code_block = False
                relative_file_path = None
                code_content = []
            else:
                code_content.append(line_stripped)

    return code_files
