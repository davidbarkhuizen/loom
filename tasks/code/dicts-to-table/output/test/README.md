# dicts_to_table

This module provides a function `dicts_to_table` that converts a list of dictionaries into a markdown formatted table.

## Usage

```python
from dicts_to_table import dicts_to_table

data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
]

table = dicts_to_table(data)
print(table)
```

## Testing

To run the tests, execute the `dicts_to_table.py` script directly:

```sh
python dicts_to_table.py
```
