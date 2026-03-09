---
title: Agent
version: 2.0.4
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# Agent

**Package:** `flyteplugins.anthropic`

A Claude agent configuration.

    This class represents the configuration for a Claude agent, including
    the model to use, system instructions, and available tools.
    


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


