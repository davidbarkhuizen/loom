2026, david barkhuizen

# Yoke System Documentation

## Overview

Yoke is a command-line interface (CLI) tool that provides an interactive environment for working with large language models (LLMs). It allows users to switch between different models, execute tasks using predefined specifications, and interact directly with LLMs through a simple command interface.

The system consists of several key components:
1. A core CLI interface (`yoke`) for user interaction
2. Model management capabilities including listing, switching, and monitoring running processes
3. Task execution framework that supports structured prompts and file-based contexts
4. Integration with Ollama for LLM interactions

## Installation

To use Yoke, you need to have Python 3.8+ installed along with the required dependencies:

```bash
pip install ollama
```

## Core Commands

### List Models (`list-models`)
Displays all available models in your Ollama instance.

```bash
yoke list-models
```

This command shows:
- Model names and sizes
- Details about each model including architecture, parent model, and quantization
- Sorts results alphabetically by model name

### Switch Model (`switch-model`)
Changes the active model for subsequent commands.

```bash
yoke switch-model <model-name>
```

Example:
```bash
yoke switch-model llama3
```

### Process Status (`ps`)
Shows currently running processes and their details.

```bash
yoke ps
```

This displays information about running models including:
- Model name and size
- Memory usage and status
- Details like architecture, parent model, quantization, etc.

### Direct Invocation (`!`)
Allows direct interaction with the LLM without any specific task context.

```bash
yoke ! <your-prompt>
```

Example:
```bash
yoke ! What is the capital of France?
```

### Task Execution (`task`)
Executes predefined tasks using structured prompts and file contexts.

```bash
yoke task <task-name> <specification>
```

Example:
```bash
yoke task code-generation my-project
```

## File Structure

Yoke expects a specific directory structure for managing tasks:

```
system/
└── task/
    └── <task-name>/
        └── system.md

user/
└── <specification>/
    └── files/
        └── (all relevant source files)
    └── specification.md

generated/
└── <specification>/
    ├── thinking.md
    ├── output.md
    └── files/
        └── (generated code/output files)
```

## Configuration

The system uses configuration files to determine folder locations and other settings. The main configuration file should define:
- `folders.system`: Path to system task definitions
- `folders.user`: Path to user specification files
- `folders.generated`: Path where generated outputs are stored

## Usage Examples

### Basic Interaction
```bash
# List available models
yoke list-models

# Switch to a specific model
yoke switch-model llama3

# Ask a direct question
yoke ! Explain quantum computing in simple terms

# Execute a task
yoke task code-generation my-web-app
```

### Task Execution Workflow

1. Create the directory structure:
   ```
   system/task/code-generation/
   └── system.md

   user/my-web-app/files/
   └── (source files)

   user/my-web-app/specification.md
   ```

2. Define your task in `system.md`:
   ```markdown
   You are an expert software developer who helps create clean, well-documented code.
   ```

3. Define your specification in `specification.md`:
   ```markdown
   Create a React component for a user profile page with the following features:
   - Display user avatar
   - Show user name and email
   - Include edit profile button
   ```

4. Run the task:
   ```bash
   yoke task code-generation my-web-app
   ```

## Output Generation

When executing tasks, Yoke generates several outputs:
- `output.md`: The main response from the LLM
- `thinking.md`: If enabled, contains the reasoning process of the model
- Files in `files/` directory: Any embedded code snippets or files extracted from the response

## Advanced Features

### File Embedding
The system supports embedding file contents directly into prompts using a markdown-based syntax. This allows LLMs to reference and work with actual source code during task execution.

### Context Management
Tasks automatically include all relevant files in the specified user folder, providing comprehensive context for LLM responses.

## Limitations

- Requires Ollama to be running locally
- Currently only supports markdown-based file formats
- Output quality depends heavily on model selection and prompt engineering
- File paths must be properly configured in the system configuration

## Troubleshooting

### Common Issues

1. **Model not found**: Ensure the specified model exists in your Ollama installation
2. **Permission denied**: Check that Yoke has proper access to configured directories
3. **No response from LLM**: Verify Ollama service is running and models are downloaded

### Debugging Tips

- Use `ps` command to check if models are properly loaded
- Test basic commands like `yoke ! hello` to verify connectivity
- Check that task directories exist and contain required files
- Monitor system resources when running resource-intensive tasks

This documentation provides the core functionality of Yoke. For more detailed information about specific commands or implementation details, refer to the source code comments and inline documentation.
