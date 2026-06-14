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