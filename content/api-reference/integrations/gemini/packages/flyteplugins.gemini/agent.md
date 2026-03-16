---
title: Agent
version: 2.0.7
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# Agent

**Package:** `flyteplugins.gemini`

A Gemini agent configuration.

This class represents the configuration for a Gemini agent, including
the model to use, system instructions, and available tools.

Attributes:
    name: A human-readable name for this agent. Used for logging and
        identification only; not sent to the API.
    instructions: The system prompt passed to Gemini on every turn.
        Describes the agent's role, tone, and constraints.
    model: The Gemini model ID to use, e.g. ``"gemini-2.5-flash"``.
    tools: List of ``FunctionTool`` instances the agent can invoke.
        Create tools with ``function_tool()``.
    max_output_tokens: Maximum number of tokens in each Gemini response.
    max_iterations: Maximum number of function-call / response cycles before
        ``run_agent`` returns with a timeout message.



```python
class Agent(
    name: str,
    instructions: str,
    model: str,
    tools: list[flyteplugins.gemini.agents._function_tools.FunctionTool],
    max_output_tokens: int,
    max_iterations: int,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `instructions` | `str` | |
| `model` | `str` | |
| `tools` | `list[flyteplugins.gemini.agents._function_tools.FunctionTool]` | |
| `max_output_tokens` | `int` | |
| `max_iterations` | `int` | |

## Methods

| Method | Description |
|-|-|
| [`get_gemini_tools()`](#get_gemini_tools) | Get tool definitions in Gemini format. |


### get_gemini_tools()

```python
def get_gemini_tools()
```
Get tool definitions in Gemini format.


