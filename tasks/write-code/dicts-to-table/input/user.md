## summary

return a python function called `dicts_to_table`, and any additional helper functions, classes, and modules as required

dicts_to_table function
- takes a `list[dict[str, str]] | None` as an argument
- in the case of being sent an empty list or null value, then return None
- check that all the dictionaries in the list have the same keys, in the same order, otherwise raise an exception
- returns a single multiline string that corresponds to a table in markdown format
  * each column should correspond to a dictionary key, and have the key as the column header
  * each row should correspond to the values of a specific dictionary in the list
