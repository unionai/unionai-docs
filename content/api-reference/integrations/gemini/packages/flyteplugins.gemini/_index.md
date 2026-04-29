---
title: flyteplugins.gemini
version: 2.2.1
variants: +flyte +union
layout: py_api
---

# flyteplugins.gemini

Google Gemini plugin for Flyte.

This plugin provides integration between Flyte tasks and Google's Gemini API,
enabling you to use Flyte tasks as tools for Gemini agents. Tool calls run with
full Flyte observability, retries, and caching.

Key features:

- Use any Flyte task as a Gemini tool via `function_tool`
- Full agent loop with automatic tool dispatch via `run_agent`
- Configurable agent via `Agent` (model, system prompt, tools, iteration limits)

Basic usage example:

```python
import flyte
from flyteplugins.gemini import Agent, function_tool, run_agent

env = flyte.TaskEnvironment(
    name="agent_env",
    image=flyte.Image.from_debian_base(name="agent").with_pip_packages(
        "flyteplugins-gemini"
    ),
)

@env.task
async def get_weather(city: str) -> str:
    '''Get the current weather for a city.'''
    return f"Weather in {city}: sunny, 22°C"

weather_tool = function_tool(get_weather)

@env.task
async def run_weather_agent(question: str) -> str:
    return await run_agent(
        prompt=question,
        tools=[weather_tool],
        model="gemini-2.5-flash",
    )
```
## Directory

### Classes

| Class | Description |
|-|-|
| [`Agent`](../flyteplugins.gemini/agent) | A Gemini agent configuration. |

### Methods

| Method | Description |
|-|-|
| [`function_tool()`](#function_tool) | Convert a function or Flyte task to a Gemini-compatible tool. |
| [`run_agent()`](#run_agent) | Run a Gemini agent with the given tools and prompt. |


## Methods

#### function_tool()

```python
def function_tool(
    func: typing.Union[flyte._task.AsyncFunctionTaskTemplate, typing.Callable, NoneType],
    name: str | None,
    description: str | None,
) -> FunctionTool | partial[FunctionTool]
```
Convert a function or Flyte task to a Gemini-compatible tool.

This function converts a Python function, @flyte.trace decorated function,
or Flyte task into a FunctionTool that can be used with Gemini's function calling API.

The input_schema is derived via the Flyte type engine, producing JSON schema.
This ensures that Literal types, dataclasses, FlyteFile, and other Flyte-native
types are represented correctly.

For @flyte.trace decorated functions, the tracing context is preserved
automatically since functools.wraps maintains the original function's metadata.



| Parameter | Type | Description |
|-|-|-|
| `func` | `typing.Union[flyte._task.AsyncFunctionTaskTemplate, typing.Callable, NoneType]` | The function or Flyte task to convert. |
| `name` | `str \| None` | Optional custom name for the tool. Defaults to the function name. |
| `description` | `str \| None` | Optional custom description. Defaults to the function's docstring. |

**Returns**

A FunctionTool instance that can be used with run_agent().


#### run_agent()

```python
def run_agent(
    prompt: str,
    tools: list[flyteplugins.gemini.agents._function_tools.FunctionTool] | None,
    agent: flyteplugins.gemini.agents._function_tools.Agent | None,
    model: str,
    system: str | None,
    max_output_tokens: int,
    max_iterations: int,
    api_key: str | None,
) -> str
```
Run a Gemini agent with the given tools and prompt.

This function creates a Gemini conversation loop that can use tools
to accomplish tasks. It handles the back-and-forth of function calls
and responses until the agent produces a final text response.



| Parameter | Type | Description |
|-|-|-|
| `prompt` | `str` | The user prompt to send to the agent. |
| `tools` | `list[flyteplugins.gemini.agents._function_tools.FunctionTool] \| None` | List of FunctionTool instances to make available to the agent. |
| `agent` | `flyteplugins.gemini.agents._function_tools.Agent \| None` | Optional Agent configuration. If provided, overrides other params. |
| `model` | `str` | The Gemini model to use. |
| `system` | `str \| None` | Optional system prompt. |
| `max_output_tokens` | `int` | Maximum tokens in the response. |
| `max_iterations` | `int` | Maximum number of tool call iterations. |
| `api_key` | `str \| None` | Google API key. Defaults to GOOGLE_API_KEY env var. |

**Returns**

The final text response from the agent.


