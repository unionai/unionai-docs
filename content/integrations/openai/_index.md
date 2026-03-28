---
title: OpenAI
weight: 1
variants: +flyte +union
sidebar_expanded: false
---

# OpenAI

The OpenAI plugin provides a drop-in replacement for the [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) `function_tool` decorator. It lets you use Flyte tasks as tools in agentic workflows so that tool calls run as tracked, reproducible Flyte task executions.

## When to use this plugin

- Building agentic workflows with the OpenAI Agents SDK on Flyte
- You want tool calls to run as Flyte tasks with full observability, retries, and caching
- You want to combine LLM agents with existing Flyte pipelines

## Installation

```bash
pip install flyteplugins-openai
```

Requires `openai-agents >= 0.2.4`.

## Usage

The plugin provides a single decorator, `function_tool`, that wraps Flyte tasks as OpenAI agent tools.

### `function_tool`

When applied to a Flyte task (a function decorated with `@env.task`), `function_tool` makes that task available as an OpenAI `FunctionTool`. The agent can call it like any other tool, and the call executes as a Flyte task.

When applied to a regular function or a `@flyte.trace`-decorated function, it delegates directly to the OpenAI Agents SDK's built-in `function_tool`.

### Basic pattern

1. Define a `TaskEnvironment` with your image and secrets
2. Decorate your task functions with `@function_tool` and `@env.task`
3. Pass the tools to an `Agent`
4. Run the agent from another Flyte task

```python
from agents import Agent, Runner
from flyteplugins.openai.agents import function_tool

env = flyte.TaskEnvironment(
    name="openai_agents",
    resources=flyte.Resources(cpu=1, memory="250Mi"),
    image=flyte.Image.from_uv_script(__file__, name="openai_agents_image"),
    secrets=flyte.Secret("openai_api_key", as_env_var="OPENAI_API_KEY"),
)

@function_tool
@env.task
async def get_weather(city: str) -> Weather:
    """Get the weather for a given city."""
    return Weather(city=city, temperature_range="14-20C", conditions="Sunny")

agent = Agent(
    name="Weather Agent",
    instructions="You are a helpful agent.",
    tools=[get_weather],
)

@env.task
async def main() -> str:
    result = await Runner.run(agent, input="What's the weather in Tokyo?")
    return result.final_output
```

> [!NOTE]
> The docstring on each `@function_tool` task is sent to the LLM as the tool description. Write clear, concise docstrings that describe what the tool does and what its parameters mean.

### Secrets

Store your OpenAI API key as a Flyte secret and expose it as an environment variable:

```python
secrets=flyte.Secret("openai_api_key", as_env_var="OPENAI_API_KEY")
```

## Example

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/openai/openai/agents_tools.py" lang="python" >}}

## API reference

See the [OpenAI API reference](../../api-reference/integrations/openai/_index) for full details.
