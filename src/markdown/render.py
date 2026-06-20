from markdown.model import DEFAULT_LANGUAGE_MARKER, FileExtensionsForLanguageMarker, LanguageMarker
from model.model import TextFile


def dict_list_to_markdown_table(dict_list, alignment="center", column_order: list[str] | None = None) -> str:
    """
    Convert a list of dictionaries to a markdown table string.

    Args:
        dict_list (list[dict[str, str]]): List of dictionaries to convert
        alignment (str): Text alignment for table columns ('left', 'center', 'right')

    Returns:
        str: Markdown table as a string

    Raises:
        ValueError: If input validation fails
    """
    # Handle empty list case
    if not dict_list:
        return ""

    # Validate each dictionary in the list
    for i, d in enumerate(dict_list):
        if d is None:
            raise ValueError(f"Dictionary at index {i} is None")
        if not isinstance(d, dict):
            raise ValueError(f"Item at index {i} is not a dictionary")
        if None in d:
            raise ValueError(f"Dictionary at index {i} contains None as key")

    # Get all unique keys from all dictionaries
    all_keys = set()
    for d in dict_list:
        all_keys.update(d.keys())

    # Check that all dictionaries have the same keys
    for i, d in enumerate(dict_list):
        if set(d.keys()) != all_keys:
            raise ValueError(f"Dictionary at index {i} has different keys than others")

    # Sort keys for consistent column ordering
    sorted_keys = sorted(all_keys)

    if column_order is not None and len(column_order) > 0:
        for column in column_order:
            if column not in sorted_keys:
                raise ValueError(f"column_order contains an invalid column name: {column}")

    key_order = column_order + [k for k in sorted_keys if k not in column_order] if column_order else sorted_keys

    # Build header row
    header_row = "| " + " | ".join(key_order) + " |"

    # Build separator row with alignment
    separator_parts = []
    for key in key_order:
        if alignment == "left":
            separator_parts.append(":---")
        elif alignment == "center":
            separator_parts.append(":---:")
        elif alignment == "right":
            separator_parts.append("---:")
        else:
            raise ValueError("Alignment must be 'left', 'center', or 'right'")
    separator_row = "| " + " | ".join(separator_parts) + " |"

    # Build data rows
    data_rows = []
    for d in dict_list:
        row_parts = []
        for key in key_order:
            value = d.get(key)
            if value is None:
                row_parts.append("")
            elif isinstance(value, str):
                row_parts.append(value)
            else:
                row_parts.append(str(value))
        data_rows.append("| " + " | ".join(row_parts) + " |")

    # Combine all parts
    table_lines = [header_row, separator_row] + data_rows
    return "\n".join(table_lines)


def language_marker_from_file_extension(file_path: str) -> LanguageMarker:

    for lang_marker in LanguageMarker:
        for file_extension in FileExtensionsForLanguageMarker[lang_marker]:
            if file_path.endswith(file_extension):
                return lang_marker

    return DEFAULT_LANGUAGE_MARKER


def markdown_file_block_for_text_file(text_file: TextFile):

    language: str = language_marker_from_file_extension(text_file.path).value
    file_path: str = text_file.path
    contents: str = text_file.text

    return f"""

**`{file_path}`**
```{language}
{contents}
```

"""
