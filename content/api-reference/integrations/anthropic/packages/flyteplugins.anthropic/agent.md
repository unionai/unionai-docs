---
title: Agent
version: 2.0.10
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# Agent

**Package:** `flyteplugins.anthropic`

A Claude agent configuration.

    This class represents the configuration for a Claude agent, including
    the model to use, system instructions, and available tools.

    Attributes:
        name: A human-readable name for this agent. Used for logging and
            identification only; not sent to the API.
        instructions: The system prompt passed to Claude on every turn.
            Describes the agent's role, tone, and constraints.
        model: The Claude model ID to use, e.g. `"claude-sonnet-4-20250514"`.
        tools: List of `FunctionTool` instances the agent can invoke.
            Create tools with `function_tool()`.
        max_tokens: Maximum number of tokens in each Claude response.
        max_iterations: Maximum number of tool-call / response cycles before
            `run_agent` returns with a timeout message.
    


## Parameters

```python
class Agent(
    name: str,
    instructions: str,
    model: str,
    tools: list[flyteplugins.anthropic.agents._function_tools.FunctionTool],
    max_tokens: int,
    max_iterations: int,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `instructions` | `str` | |
| `model` | `str` | |
| `tools` | `list[flyteplugins.anthropic.agents._function_tools.FunctionTool]` | |
| `max_tokens` | `int` | |
| `max_iterations` | `int` | |

## Methods

| Method | Description |
|-|-|
| [`get_anthropic_tools()`](#get_anthropic_tools) | Get tool definitions in Anthropic format. |


### get_anthropic_tools()

```python
def get_anthropic_tools()
```
Get tool definitions in Anthropic format.


