---
title: Gemini
weight: 1
variants: +flyte +union
sidebar_expanded: false
---

# Gemini

The Gemini plugin lets you build agentic workflows with [Gemini](https://ai.google.dev/) on Flyte. It provides a `function_tool` decorator that wraps Flyte tasks as tools that Gemini can call, and a `run_agent` function that drives the agent conversation loop.

When Gemini calls a tool, the call executes as a Flyte task with full observability, retries, and caching. Gemini's native parallel function calling is supported: multiple tool calls in a single turn are all dispatched and their results bundled into one response.

## Installation

```bash
pip install flyteplugins-gemini
```

Requires `google-genai >= 1.0.0`.

## Quick start

```python
import flyte
from flyteplugins.gemini import function_tool, run_agent

env = flyte.TaskEnvironment(
    name="gemini-agent",
    resources=flyte.Resources(cpu=1, memory="250Mi"),
    image=flyte.Image.from_uv_script(__file__, name="gemini_agent"),
    secrets=flyte.Secret("google_api_key", as_env_var="GOOGLE_API_KEY"),
)

@function_tool
@env.task
async def get_weather(city: str) -> str:
    """Get the current weather for a city."""
    return f"The weather in {city} is sunny, 72F"

@env.task
async def main(prompt: str) -> str:
    tools = [get_weather]
    return await run_agent(prompt=prompt, tools=tools)
```

## API

### `function_tool`

Converts a Flyte task, `@flyte.trace`-decorated function, or plain callable into a tool that Gemini can invoke.

```python
@function_tool
@env.task
async def my_tool(param: str) -> str:
    """Tool description sent to Gemini."""
    ...
```

Can also be called with optional overrides:

```python
@function_tool(name="custom_name", description="Custom description")
@env.task
async def my_tool(param: str) -> str:
    ...
```

Parameters:

| Parameter | Type | Description |
|-----------|------|-------------|
| `func` | callable | The function to wrap |
| `name` | `str` | Override the tool name (defaults to the function name) |
| `description` | `str` | Override the tool description (defaults to the docstring) |

> [!NOTE]
> The docstring on each `@function_tool` task is sent to Gemini as the tool description. Write clear, concise docstrings.

### `Agent`

A dataclass for bundling agent configuration:

```python
from flyteplugins.gemini import Agent

agent = Agent(
    name="my-agent",
    instructions="You are a helpful assistant.",
    model="gemini-2.5-flash",
    tools=[get_weather],
    max_output_tokens=8192,
    max_iterations=10,
)
```

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `name` | `str` | `"assistant"` | Agent name |
| `instructions` | `str` | `"You are a helpful assistant."` | System prompt |
| `model` | `str` | `"gemini-2.5-flash"` | Gemini model ID |
| `tools` | `list[FunctionTool]` | `[]` | Tools available to the agent |
| `max_output_tokens` | `int` | `8192` | Maximum tokens per response |
| `max_iterations` | `int` | `10` | Maximum tool-call loop iterations |

### `run_agent`

Runs a Gemini conversation loop, dispatching tool calls to Flyte tasks until Gemini returns a final response.

```python
result = await run_agent(
    prompt="What's the weather in Tokyo?",
    tools=[get_weather],
    model="gemini-2.5-flash",
)
```

You can also pass an `Agent` object:

```python
result = await run_agent(prompt="What's the weather?", agent=agent)
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `prompt` | `str` | required | User message |
| `tools` | `list[FunctionTool]` | `None` | Tools available to the agent |
| `agent` | `Agent` | `None` | Agent config (overrides individual params) |
| `model` | `str` | `"gemini-2.5-flash"` | Gemini model ID |
| `system` | `str` | `None` | System prompt |
| `max_output_tokens` | `int` | `8192` | Maximum tokens per response |
| `max_iterations` | `int` | `10` | Maximum iterations (prevents infinite loops) |
| `api_key` | `str` | `None` | API key (falls back to `GOOGLE_API_KEY` env var) |

## Secrets

Store your Google API key as a Flyte secret and expose it as an environment variable:

```python
secrets=flyte.Secret("google_api_key", as_env_var="GOOGLE_API_KEY")
```

## API reference

See the [Gemini API reference](../../api-reference/integrations/gemini/_index) for full details.
