## specification

convert list of python dictionaries to markdown table string

### inputs

- list of dictionaries to convert
  * `list[dict[str, str]]`
- alignment
  * str
  * allowed values: 'left', 'center', 'right'
  * default: 'center'

#### input validation

- in the case of being sent an empty list, then return an empty string
- if any of the dictionaries in the list are null, then raise a ValueError
- check that all the dictionaries in the list have the same keys
  * otherwise raise a ValueError() exception
- raise a ValueError exception if a dictionary item key of None is encountered

### outputs

return a single multiline string that corresponds to a table in markdown format

### processing

#### handling dictionary values

when retrieving a key value from a dictionary for conversion to a table row cell

- if the value, is None
  * convert to empty string
- if the value is a string
  * return the value
- all other cases
  * convert value to string using str function

### markdown table format specification

Markdown tables structure data using pipe character (|) to separate columns and a row of three hyphens (---) to define the header.  This syntax is part of GitHub-Flavored Markdown (GFM) and is widely supported in documentation, wikis, and README files.

Basic Syntax To create a simple table, place headers in the first row, followed by a separator line, and then the data rows. Pipes are required at the start and end of each line for clarity

### example of basic syntax for markdown tables

| Name    | Age | City       |
|---------|-----|------------|
| Alice   | 25  | New York   |
| Bob     | 30  | London     |


### text alignment in markdown tables

Text Alignment You can control column alignment using colons (:) in the separator row. A colon on the left aligns text left, on the right aligns right, and on both sides centers the text.

#### example of text alignment in markdown tables

| Left  | Center | Right |
|:------|:------:|------:|
| Data1 | Data2  | Data3 |
| Data4 | Data5  | Data6 |
