# Specification Distillation and Implementation for `dicts_to_table`

## specification

Create a Python function `dicts_to_table(data: list[dict[str, str]] | None) -> str | None` that:
1. Returns `None` when `data` is `None` or an empty list.
2. Validates that every dictionary in `data` contains identical keys in identical order; raises `ValueError` on mismatch.
3. Constructs and returns a Markdown table string where:
   - The first row lists dictionary keys as column headers.
   - The second row lists column separators.
   - Subsequent rows list dictionary values aligned to their respective keys.

## code

**`solution.py`**
```python
def dicts_to_table(data: list[dict[str, str]] | None) -> str | None:
    if not data:
        return None

    expected_keys = list(data[0].keys())

    for idx, row in enumerate(data):
        if list(row.keys()) != expected_keys:
            raise ValueError("Inconsistent dictionary keys across rows")

    headers = "| " + " | ".join(expected_keys) + " |"
    separators = "| " + " | ".join("---" for _ in expected_keys) + " |"

    rows = [
        "| " + " | ".join(row[key] for key in expected_keys) + " |"
        for row in data
    ]

    return "\n".join([headers, separators] + rows)
```

**`test_solution.py`**
```python
import unittest
from solution import dicts_to_table


class TestDictsToTable(unittest.TestCase):
    def test_null_input_returns_none(self):
        self.assertIsNone(dicts_to_table(None))

    def test_empty_list_returns_none(self):
        self.assertIsNone(dicts_to_table([]))

    def test_valid_dicts_returns_markdown_table(self):
        data = [
            {"name": "Alice", "age": "30"},
            {"name": "Bob", "age": "25"}
        ]
        result = dicts_to_table(data)
        self.assertIsNotNone(result)
        self.assertIn("| name | age |", result)
        self.assertIn("| --- | --- |", result)
        self.assertIn("| Alice | 30 |", result)
        self.assertIn("| Bob | 25 |", result)

    def test_mismatched_keys_raises_value_error(self):
        data = [{"a": "1"}, {"b": "2"}]
        with self.assertRaises(ValueError):
            dicts_to_table(data)

    def test_mismatched_key_order_raises_value_error(self):
        data = [{"a": "1", "b": "2"}, {"b": "2", "a": "1"}]
        with self.assertRaises(ValueError):
            dicts_to_table(data)


if __name__ == "__main__":
    unittest.main()
```