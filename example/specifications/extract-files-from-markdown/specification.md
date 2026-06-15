### specification

#### inputs

- file path to a source markdown document
  * in the form of a string
- folder path to a destination folder to write the extracted code files to 
  * in the form of a string

### processing

- load the source markdown document from the local file system
- scan through the document, identifying all markdown code sections
- for each markdown code section identified
  * check if that section is immediately preceded (previous line) by a file path marker (format defined below)
    - in the positive case
      * write the contents of the code section to the local file system at the destination folder
        - use the file path in the associated file path marker as a relative path
        - ensure the path does not escape the destination folder
    - in the negative case
      * skip

### format of a text file for inclusion in a markdown document

- each text file is included as a separate fenced code block in a markdown document
- fenced code block for a text file with a given path is be immediately preceded in the markdown document (i.e. the previous line) by the file path marker in bold inline code format
  * e.g. **`xxx/yyy/zzz.py`**
  * the file path marker itself is not be preceded or followed by any whitespace
  * the fenced code block is not be indented
- the file path in the file path marker is a relative path, and not an absolute path
- the file path marker itself is immediately preceded by a blank line
- the fenced code block should be immediately followed by a blank line

Here is an example for a python code file `zzz.py` with relative file path `xxx/yyy/zzz.py`:

**`xxx/yyy/zzz.py`**
```python
def hello_world():
    print('hello world')
```

Here is an example for a python code file `dog.py` with relative file path `cat/fish/dog.py`:

**`cat/fish/dog.py`**
```python
def hello_world():
    print('hello world')
```

Here is an example for a sql code file `query.sql` with relative file path `cat/fish/query.sql`:

**`cat/fish/query.sql`**
```sql
select * 
from target_database.target_schema.target_table
where True
```

### outputs

a list of the destination paths of the successfully extracted files
