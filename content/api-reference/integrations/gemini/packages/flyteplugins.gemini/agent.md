---
title: Agent
version: 2.1.7
variants: +flyte +byoc +selfmanaged +union
layout: py_api
---

# Agent

**Package:** `flyteplugins.gemini`

A Gemini agent configuration.

This class represents the configuration for a Gemini agent, including
the model to use, system instructions, and available tools.



## Parameters

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
| `name` | `str` | A human-readable name for this agent. Used for logging and identification only; not sent to the API. |
| `instructions` | `str` | The system prompt passed to Gemini on every turn. Describes the agent's role, tone, and constraints. |
| `model` | `str` | The Gemini model ID to use, e.g. `"gemini-2.5-flash"`. |
| `tools` | `list[flyteplugins.gemini.agents._function_tools.FunctionTool]` | List of `FunctionTool` instances the agent can invoke. Create tools with `function_tool()`. |
| `max_output_tokens` | `int` | Maximum number of tokens in each Gemini response. |
| `max_iterations` | `int` | Maximum number of function-call / response cycles before `run_agent` returns with a timeout message. |

## Methods

| Method | Description |
|-|-|
| [`get_gemini_tools()`](#get_gemini_tools) | Get tool definitions in Gemini format. |


### get_gemini_tools()

```python
def get_gemini_tools()
```
Get tool definitions in Gemini format.


