---
title: LangChain
weight: 6
variants: +flyte +union
---

# LangChain

Run [LangChain agents](https://docs.langchain.com/oss/python/langchain/agents) on Flyte. In LangChain 1.x an agent is built with `create_agent(model, tools, system_prompt=...)`, which returns a compiled graph. `run_agent` drives that graph inside your task, with tools running as durable child actions and model turns recorded for replay.

## Installation

```bash
pip install flyteplugins-agents-langchain
```

Requires Python 3.10 or later. Install the provider integration you need alongside it, for example `langchain-openai` or `langchain-anthropic`.

## Quick start

```python{hl_lines=[2, 6, 13, "24-29"]}
import flyte
from flyteplugins.agents.langchain import run_agent, tool

env = flyte.TaskEnvironment(
    "langchain-agent",
    secrets=[flyte.Secret(key="openai_api_key", as_env_var="OPENAI_API_KEY")],
    image=flyte.Image.from_debian_base().with_pip_packages(
        "flyteplugins-agents-langchain", "langchain-openai",
    ),
)


@tool
@env.task(cache="auto", retries=3)
async def get_weather(city: str) -> str:
    """Get the current weather for a city."""
    return f"The weather in {city} is sunny, 22C."


@env.task(report=True, retries=3)
async def city_agent(question: str) -> str:
    from langchain_openai import ChatOpenAI

    return await run_agent(
        question,
        tools=[get_weather],
        model=ChatOpenAI(model="gpt-4o"),
        instructions="You are a concise assistant. Use the tools to answer.",
    )
```

Build the chat model inside the task, where the provider API key is available.

## How it maps to Flyte

**Tools:** `tool` turns an `@env.task` into a LangChain `StructuredTool`, a real `BaseTool` that drops straight into `create_agent(model, tools=[...])`. The args schema is built as a pydantic model from the task's typed signature, with annotations and defaults preserved, rather than being inferred from the wrapper. When the agent calls the tool, the coroutine dispatches to `task.aio()` and the call becomes a durable child action.

**Model turns:** With `durable=True`, the chat model is wrapped in `DurableChatModel`, which records each turn via `flyte.trace`. On a retry, completed turns replay from their records and tool calls come back from cache.

**Observability:** The run timeline renders into the task report.

## Pass a model instance, not a string

Durability is applied by wrapping a `BaseChatModel` instance. `create_agent` also accepts a `provider:model` string, and that will run, but a string is passed straight through unwrapped, so you lose per-turn replay.

```python
model=ChatOpenAI(model="gpt-4o")   # wrapped, turns are durable
model="openai:gpt-4o"              # runs, but turns are not recorded
```

Tool calls stay durable either way. If you want the string form with durability, use the [LangGraph](./langgraph) or [Deep Agents](./deepagents) adapter, both of which resolve the string before wrapping.

## Bring your own agent

Pass a compiled `create_agent` graph as `agent=`.

```python{hl_lines=["9-14"]}
from langchain.agents import create_agent
from flyteplugins.agents.langchain import DurableChatModel


@env.task(report=True, retries=3)
async def support(request: str) -> str:
    from langchain_openai import ChatOpenAI

    graph = create_agent(
        DurableChatModel(inner=ChatOpenAI(model="gpt-4o")),
        [lookup_account],
        system_prompt="You are a billing support agent.",
    )
    return await run_agent(request, agent=graph)
```

A fully compiled graph owns its own model and cannot be rewrapped from outside, so wrap the model yourself with `DurableChatModel` when building it. Tool calls remain durable regardless.

`agent` and `tools` are mutually exclusive.

## Memory

```python
await run_agent(message, model=ChatOpenAI(model="gpt-4o"), memory_key="user-alice")
```

The conversation transcript is persisted to a durable, keyed `MemoryStore`. On the next run with the same key, prior messages are loaded and prepended to the new user turn, and the full transcript is saved back afterwards.

## `run_agent` parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `input` | `str` | required | The user prompt |
| `tools` | `Sequence` | `()` | Tools to expose. Accepts `tool`-wrapped tools or bare `@env.task` templates |
| `model` | `Any` | `None` | A LangChain chat model. Required when `agent` is not given |
| `instructions` | `str \| None` | `None` | System prompt for the built agent |
| `agent` | `Any` | `None` | A pre-built compiled `create_agent` graph. Mutually exclusive with `tools` |
| `name` | `str` | `"langchain-agent"` | Agent name, used for debugging and observability |
| `durable` | `bool` | `True` | Record and replay each model turn. Applies on the builder path |
| `observability` | `bool` | `True` | Render the timeline into the task report |
| `memory_key` | `str \| None` | `None` | Stable user or thread ID for cross-run memory |
| `**agent_kwargs` | | | Forwarded to `create_agent` |

Returns the final text, taken from the content of the last message. Use `run_agent_sync` with the same signature from a sync task.

## Examples

Full runnable examples live in the SDK repository under [`plugins/agents/langchain/examples`](https://github.com/flyteorg/flyte-sdk/tree/main/plugins/agents/langchain/examples):

- `langchain_durable_agent.py`: a single durable agent with traced model turns.
- `langchain_custom_agent.py`: building the agent yourself and passing it as `agent=`.
- `langchain_multi_agent.py`: a planner, parallel researchers and an editor, each its own durable action.
- `langchain_crash_resume.py`: the task crashes on its first attempt and replays completed turns on retry.
- `langchain_memory.py`: two separate runs sharing a `memory_key`.
