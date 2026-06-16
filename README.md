# Yoke System Specification

## Overview
Yoke is an intelligent task automation framework that leverages large language models to execute complex workflows through structured prompts and file-based inputs/outputs. The system provides a command-line interface for interacting with various AI capabilities while maintaining clean separation between system prompts, user specifications, and generated outputs.

## Core Architecture

### 1. Command Structure
The system operates through a series of commands accessible via the command-line interface:
- `list-models`: Display available language models
- `list-tasks`: Show all available task templates
- `task [task-name] [specification-name]`: Execute a specific task with user input
- `! [natural language query]`: Direct LLM interaction without task context

### 2. Folder Structure
The system maintains a hierarchical folder structure:
```
system/
├── task/
│   └── [task-name]/
│       ├── system.md          # System prompt for the task
│       └── [subfolders]       # Additional task-specific resources
user/
├── [specification-name]/
│   ├── specification.md       # User's problem description
│   └── files/                 # Supporting input files
generated/
└── [specification-name]/      # Output directory for results
    ├── output.md              # Main response from LLM
    ├── thinking.md            # LLM's reasoning process (if available)
    └── files/                 # Embedded files extracted from response
```

## Task Execution Workflow

### 1. Task Selection and Preparation
When executing a task:
1. System identifies the task template by name
2. Reads the system prompt from `system/task/[task-name]/system.md`
3. Locates user specification in `user/[specification-name]/`
4. Gathers all files from `user/[specification-name]/files/`

### 2. Prompt Construction
The system constructs a structured prompt combining:
- **System Prompt**: The task's base instructions
- **User Files Block**: All input files embedded into the context
- **User Specification**: The natural language problem description

### 3. LLM Interaction
The constructed prompt is sent to the specified language model through the `communicate()` function in `harness/tether.py`.

### 4. Response Processing
The system processes the LLM response by:
1. Extracting reasoning from `thinking.md` (if present)
2. Parsing embedded text files from the markdown output
3. Saving all outputs to the generated folder

## Key Components

### 1. Communication Layer (`harness/tether.py`)
- Handles asynchronous communication with language models
- Manages conversation flow between system and LLM
- Processes both thinking and content responses

### 2. File Handling Utilities (`common/file_utils.py`)
- Asynchronous file reading/writing operations
- Binary file detection
- Text file encoding/decoding for markdown contexts

### 3. Markdown Processing (`markdown/` folder)
- **Parsing**: Extract embedded files from markdown responses
- **Rendering**: Format text files as markdown code blocks
- **Display**: Present structured data in readable formats

### 4. Command Interface (`harness/commands/`)
Each command implements the `AbstractHarnessCommand` interface:
- **ListModelsCommand**: Displays available models with details
- **ListTasksCommand**: Shows all registered tasks
- **TaskCommand**: Executes tasks with user specifications
- **InvokeCommand**: Direct natural language queries

## Features and Capabilities

### 1. Task Templates
Tasks are defined as reusable templates that provide:
- System prompts that guide the LLM's behavior
- Context for problem-solving
- Expected output formats

### 2. File Context Management
- Automatic embedding of user input files into prompts
- Support for nested file structures
- Binary file detection and handling

### 3. Response Extraction
- Automatic parsing of embedded code blocks from markdown outputs
- Extraction of generated files from LLM responses
- Preservation of reasoning process in separate files

### 4. Modular Design
- Clear separation between system components
- Extensible command structure
- Reusable utility functions

## Usage Examples

### Execute a Task
```
task code-generation my-web-app
```

### Direct Query
```
! explain quantum computing in simple terms
```

### List Available Resources
```
list-models
list-tasks
```

## Output Structure
Generated outputs are systematically organized:
- `output.md`: Main response from the LLM
- `thinking.md`: Reasoning process (if enabled)
- `files/`: Extracted embedded files from the response

This specification provides a comprehensive framework for understanding and extending the Yoke system's functionality while maintaining its modular, file-based approach to AI task execution.
