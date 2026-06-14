# Markdown Table Generator from List of Dictionaries

## specification

Create a Python function `dicts_to_table` that accepts a `list[dict[str, str]]`. The function must:
- Return an empty string if the input list is empty.
- Validate that all dictionaries in the list contain exactly the same keys. If validation fails, raise a `ValueError`.
- Generate a markdown-formatted table string where:
  - The first row contains the dictionary keys as column headers.
  - The second row contains the standard markdown separator.
  - Each subsequent row contains the values from one dictionary, aligned with the corresponding keys.
  - The column order follows the key order of the first dictionary in the input list.
- Return the complete multiline string.

## code

**`src/dicts_to_table.py`**
```python
def dicts_to_table(dicts: list[dict[str, str]]) -> str:
    """Convert a list of dictionaries with identical keys into a markdown table string."""
    if not dicts:
        return ""

    keys = list(dicts[0].keys())
    expected_key_set = set(keys)

    for i, d in enumerate(dicts):
        if set(d.keys()) != expected_key_set:
            raise ValueError(
                f"All dictionaries must have the same keys. "
                f"Mismatch found at index {i}."
            )

    header = "| " + " | ".join(keys) + " |"
    separator = "| " + " | ".join(["---"] * len(keys)) + " |"
    rows = [header, separator]

    for d in dicts:
        row = "| " + " | ".join(str(d[k]) for k in keys) + " |"
        rows.append(row)

    return "\n".join(rows)
```

**`tests/test_dicts_to_table.py`**
```python
import pytest
from src.dicts_to_table import dicts_to_table


def test_basic_table_generation():
    data = [
        {"name": "Alice", "age": "30"},
        {"name": "Bob", "age": "25"},
    ]
    result = dicts_to_table(data)
    expected = (
        "| name | age |\n"
        "| --- | --- |\n"
        "| Alice | 30 |\n"
        "| Bob | 25 |"
    )
    assert result == expected


def test_single_dictionary():
    data = [{"id": "1", "value": "test"}]
    result = dicts_to_table(data)
    expected = "| id | value |\n| --- | --- |\n| 1 | test |"
    assert result == expected


def test_empty_list():
    assert dicts_to_table([]) == ""


def test_mismatched_keys_raises_error():
    data = [
        {"a": "1", "b": "2"},
        {"a": "3", "c": "4"},
    ]
    with pytest.raises(ValueError, match="All dictionaries must have the same keys"):
        dicts_to_table(data)


def test_different_key_order_same_keys():
    data = [
        {"x": "1", "y": "2"},
        {"y": "3", "x": "4"},
    ]
    result = dicts_to_table(data)
    # Column order should match the first dictionary
    expected = (
        "| x | y |\n"
        "| --- | --- |\n"
        "| 1 | 2 |\n"
        "| 4 | 3 |"
    )
    assert result == expected
```