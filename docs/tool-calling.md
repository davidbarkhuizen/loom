# tool-calling in ollama

## json schema

{
  "type": "function",
  "function": {
    "name": "function_name",
    "description": "Description of what the function does",
    "parameters": {
      "type": "object",
      "properties": {
        "param1": { "type": "string" }
      },
      "required": ["param1"]
    }
  }
}
