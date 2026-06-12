# specification

## definitions

## functionality

## objectives

### 1 - improve basic flow handling

- inspect message data to determine when current response is complete
- set additional arguments - e.g. think - from config
- change to submitting chat content in json format

### 2 - minimum semantic information 

    class ContextItemType(Enum):
      TEXT = 'TEXT' # includes text file
      IMAGE = 'IMAGE'

    @dataclass
    class ContextItem:
      type: ContextItemType
      description: str
      value: str

    class GrammaticalMood(Enum):
      Interrogative = 'question'
      Imperative = 'instruction'

    @dataclass
    class InvocationContext:
      items: list[ContextItem]

    @dataclass
    class Invocation:
      text: str
      mood: GrammaticalMood
      context: InvocationContext

### 3 - file based output

- provide an input file
- obtain an output file

next obj
