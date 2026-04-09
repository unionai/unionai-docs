---
title: Anthropic
weight: 1
variants: +flyte +union
sidebar_expanded: false
---

# Anthropic

The Anthropic plugin lets you build agentic workflows with [Claude](https://www.anthropic.com/) on Flyte. It provides a `function_tool` decorator that wraps Flyte tasks as tools that Claude can call, and a `run_agent` function that drives the agent conversation loop.

When Claude calls a tool, the call executes as a Flyte task with full observability, retries, and caching.

## Installation

```bash
pip install flyteplugins-anthropic
```

Requires `anthropic >= 0.40.0`.

## Quick start

```python
import flyte
from flyteplugins.anthropic import function_tool, run_agent

env = flyte.TaskEnvironment(
    name="claude-agent",
    resources=flyte.Resources(cpu=1, memory="250Mi"),
    image=flyte.Image.from_uv_script(__file__, name="anthropic_agent"),
    secrets=flyte.Secret("anthropic_api_key", as_env_var="ANTHROPIC_API_KEY"),
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

Converts a Flyte task, `@flyte.trace`-decorated function, or plain callable into a tool that Claude can invoke.

```python
@function_tool
@env.task
async def my_tool(param: str) -> str:
    """Tool description sent to Claude."""
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
> The docstring on each `@function_tool` task is sent to Claude as the tool description. Write clear, concise docstrings.

### `Agent`

A dataclass for bundling agent configuration:

```python
from flyteplugins.anthropic import Agent

agent = Agent(
    name="my-agent",
    instructions="You are a helpful assistant.",
    model="claude-sonnet-4-20250514",
    tools=[get_weather],
    max_tokens=4096,
    max_iterations=10,
)
```

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `name` | `str` | `"assistant"` | Agent name |
| `instructions` | `str` | `"You are a helpful assistant."` | System prompt |
| `model` | `str` | `"claude-sonnet-4-20250514"` | Claude model ID |
| `tools` | `list[FunctionTool]` | `[]` | Tools available to the agent |
| `max_tokens` | `int` | `4096` | Maximum tokens per response |
| `max_iterations` | `int` | `10` | Maximum tool-call loop iterations |

### `run_agent`

Runs a Claude conversation loop, dispatching tool calls to Flyte tasks until Claude returns a final response.

```python
result = await run_agent(
    prompt="What's the weather in Tokyo?",
    tools=[get_weather],
    model="claude-sonnet-4-20250514",
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
| `model` | `str` | `"claude-sonnet-4-20250514"` | Claude model ID |
| `system` | `str` | `None` | System prompt |
| `max_tokens` | `int` | `4096` | Maximum tokens per response |
| `max_iterations` | `int` | `10` | Maximum iterations (prevents infinite loops) |
| `api_key` | `str` | `None` | API key (falls back to `ANTHROPIC_API_KEY` env var) |

## Secrets

Store your Anthropic API key as a Flyte secret and expose it as an environment variable:

```python
secrets=flyte.Secret("anthropic_api_key", as_env_var="ANTHROPIC_API_KEY")
```

## API reference

See the [Anthropic API reference](../../api-reference/integrations/anthropic/_index) for full details.
