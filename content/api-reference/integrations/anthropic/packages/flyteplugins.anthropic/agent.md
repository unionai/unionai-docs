---
title: Agent
version: 2.1.2.dev2+g62f55b516
variants: +flyte +byoc +selfmanaged +union
layout: py_api
---

# Agent

**Package:** `flyteplugins.anthropic`

A Claude agent configuration.

This class represents the configuration for a Claude agent, including
the model to use, system instructions, and available tools.



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
| `name` | `str` | A human-readable name for this agent. Used for logging and identification only; not sent to the API. |
| `instructions` | `str` | The system prompt passed to Claude on every turn. Describes the agent's role, tone, and constraints. |
| `model` | `str` | The Claude model ID to use, e.g. `"claude-sonnet-4-20250514"`. |
| `tools` | `list[flyteplugins.anthropic.agents._function_tools.FunctionTool]` | List of `FunctionTool` instances the agent can invoke. Create tools with `function_tool()`. |
| `max_tokens` | `int` | Maximum number of tokens in each Claude response. |
| `max_iterations` | `int` | Maximum number of tool-call / response cycles before `run_agent` returns with a timeout message. |

## Methods

| Method | Description |
|-|-|
| [`get_anthropic_tools()`](#get_anthropic_tools) | Get tool definitions in Anthropic format. |


### get_anthropic_tools()

```python
def get_anthropic_tools()
```
Get tool definitions in Anthropic format.


