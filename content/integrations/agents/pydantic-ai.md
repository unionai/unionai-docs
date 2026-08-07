---
title: Pydantic AI
weight: 10
variants: +flyte +union
---

# Pydantic AI

Run [Pydantic AI](https://ai.pydantic.dev/) agents on Flyte. Pydantic AI owns the loop through `Agent.run`. Flyte supplies the runtime: tools become durable child actions, model turns are recorded for replay, and the run renders into the task report.

This is the one adapter that applies model-turn durability on both the builder path and the pre-built path, because `Agent.override` gives it a clean way in.

## Installation

```bash
pip install flyteplugins-agents-pydantic-ai
```

Requires Python 3.10 or later and `pydantic-ai` 2.x.

## Quick start

```python{hl_lines=[2, 6, 11, "20-25"]}
import flyte
from flyteplugins.agents.pydantic_ai import run_agent, tool

env = flyte.TaskEnvironment(
    "pydantic-ai-agent",
    secrets=[flyte.Secret(key="openai_api_key", as_env_var="OPENAI_API_KEY")],
    image=flyte.Image.from_debian_base().with_pip_packages("flyteplugins-agents-pydantic-ai"),
)


@tool
@env.task(cache="auto", retries=3)
async def get_weather(city: str) -> str:
    """Get the current weather for a city."""
    return f"The weather in {city} is sunny, 22C."


@env.task(report=True, retries=3)
async def city_agent(question: str) -> str:
    return await run_agent(
        question,
        tools=[get_weather],
        model="openai:gpt-4o",
        instructions="You are a concise assistant. Use the tools to answer.",
    )
```

Note the import path uses an underscore, `flyteplugins.agents.pydantic_ai`, while the package on PyPI is `flyteplugins-agents-pydantic-ai`.

`model` is required on the builder path. The adapter is provider agnostic and assumes no default.

## How it maps to Flyte

**Tools:** Pydantic AI accepts plain async callables in `Agent(tools=[...])` and infers each tool's schema from the signature. `tool` here is the shared core wrapper, which preserves the signature through `functools.wraps` and dispatches to `task.aio()`, so schema inference works unchanged and every call is a durable child action.

**Model turns:** On the builder path the model is resolved through `infer_model` and wrapped in `FlyteModel`. On the pre-built path the wrapper is applied through `Agent.override(model=...)`, scoped to the run.

Both paths are best-effort. If the model cannot be inferred or the agent exposes no accessible `Model`, a warning is logged and the run proceeds without per-turn durability rather than failing. Tool calls stay durable regardless.

**Observability:** The run timeline renders into the task report.

## Bring your own agent

Tools are attached at construction in Pydantic AI. `Agent.run` takes no `tools` argument, so a pre-built agent carries its own.

```python{hl_lines=[1, "6-11"]}
from pydantic_ai import Agent


@env.task(report=True, retries=3)
async def support(request: str) -> str:
    agent = Agent(
        "openai:gpt-4o",
        system_prompt="You are a billing support agent.",
        tools=[lookup_account],
    )
    return await run_agent(request, agent=agent)
```

Durability is applied through `override` on this path, so you do not have to wrap the model yourself.

`agent` and `tools` are mutually exclusive.

## Memory

```python
await run_agent(message, model="openai:gpt-4o", memory_key="user-alice")
```

Prior conversation history is loaded from a durable, keyed `MemoryStore` and passed as `message_history=`. After the run, the full history is saved back, so a later run with the same key continues the conversation.

An explicit `message_history=` in `**run_kwargs` takes precedence over loaded memory.

## `run_agent` parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `input` | `str` | required | The user prompt |
| `tools` | `Sequence` | `()` | Tools to expose. Accepts `tool`-wrapped tools or bare `@env.task` templates |
| `model` | `Any` | `None` | Model name such as `"openai:gpt-4o"`, or a `Model` instance. Required when `agent` is not given |
| `instructions` | `str \| None` | `None` | System prompt for the built agent |
| `agent` | `Any` | `None` | A pre-built Pydantic AI `Agent` with tools attached. Mutually exclusive with `tools` |
| `name` | `str` | `"pydantic-ai-agent"` | Agent name, used for debugging and observability |
| `durable` | `bool` | `True` | Record and replay each model turn. Applies on both paths |
| `observability` | `bool` | `True` | Render the timeline into the task report |
| `memory_key` | `str \| None` | `None` | Stable user or thread ID for cross-run memory |
| `**run_kwargs` | | | Forwarded to `agent.run`, including an explicit `message_history=` |

Returns the final output as a string, taken from `result.output`. Use `run_agent_sync` with the same signature from a sync task.

## Examples

Full runnable examples live in the SDK repository under [`plugins/agents/pydantic_ai/examples`](https://github.com/flyteorg/flyte-sdk/tree/main/plugins/agents/pydantic_ai/examples):

- `pydantic_ai_durable_agent.py`: a single durable agent with traced model turns.
- `pydantic_ai_custom_agent.py`: building the `Agent` yourself and passing it as `agent=`.
- `pydantic_ai_multi_agent.py`: a planner, parallel researchers and an editor, each its own durable action.
- `pydantic_ai_crash_resume.py`: the task crashes on its first attempt and replays completed turns on retry.
- `pydantic_ai_memory.py`: two separate runs sharing a `memory_key`.
