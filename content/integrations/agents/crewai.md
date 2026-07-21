---
title: CrewAI
weight: 9
variants: +flyte +union
---

# CrewAI

Run [CrewAI](https://docs.crewai.com/) agents on Flyte. CrewAI drives the loop through `Agent.kickoff_async`. Flyte supplies the runtime: tools become durable child actions, model turns are recorded for replay, and the run renders into the task report.

## Installation

```bash
pip install flyteplugins-agents-crewai
```

Requires Python 3.10 or later.

## Quick start

```python{hl_lines=[2, 6, 11, "20-25"]}
import flyte
from flyteplugins.agents.crewai import run_agent, tool

env = flyte.TaskEnvironment(
    "crewai-agent",
    secrets=[flyte.Secret(key="openai_api_key", as_env_var="OPENAI_API_KEY")],
    image=flyte.Image.from_debian_base().with_pip_packages("flyteplugins-agents-crewai"),
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
        model="gpt-4o",
        instructions="You are a concise assistant. Use the tools to answer.",
    )
```

`model` is required on the builder path. The adapter is provider agnostic and assumes no default.

## How it maps to Flyte

**Tools:** CrewAI requires tools attached to `Agent(tools=[...])` to be `crewai.tools.BaseTool` instances; plain callables are rejected by pydantic validation. `tool` therefore produces a real `BaseTool` subclass whose execution dispatches to `task.aio()`. The input schema comes from the Flyte type engine.

CrewAI invokes tools synchronously, which is awkward inside an already-running event loop. The adapter handles this by making the synchronous `_run` path bridge to the task through a dedicated background-thread loop, and by awaiting the task directly on CrewAI's native async path. You do not have to think about it, but it explains why the tool object is a class rather than a function.

**Model turns:** On the builder path the agent is driven by a durable `LLM`, so each turn is recorded via `flyte.trace` and replayed on retry.

**Observability:** The run timeline renders into the task report.

## Bring your own agent

Pass a pre-built CrewAI `Agent` with its tools already attached.

```python{hl_lines=["6-12"]}
from crewai import Agent


@env.task(report=True, retries=3)
async def support(request: str) -> str:
    agent = Agent(
        role="Billing specialist",
        goal="Resolve billing questions accurately.",
        backstory="You have handled billing escalations for years.",
        tools=[lookup_account],
        llm="gpt-4o",
    )
    return await run_agent(request, agent=agent)
```

> [!WARNING] Pre-built agents keep their own model
> Model-turn durability is applied only when `run_agent` builds the agent, because the builder is what sets the durable `llm`. A pre-built agent keeps whatever `llm` you gave it and is not rewrapped, so its turns are not recorded. Tool calls remain durable either way.

`agent` and `tools` are mutually exclusive. A pre-built agent carries its own tools.

## Instructions and the built agent

On the builder path, `run_agent` constructs an agent with the role `Assistant` and a goal of answering accurately and concisely. `instructions` is folded into the backstory rather than replacing the whole persona. If you need full control over role, goal and backstory, build the agent yourself and pass it as `agent=`.

## Memory

```python
await run_agent(message, model="gpt-4o", memory_key="user-alice")
```

The conversation transcript is persisted to a durable, keyed `MemoryStore`. On the next run with the same key, the prior transcript is loaded and passed to `kickoff_async` as a message list so the agent continues the conversation.

## `run_agent` parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `input` | `str` | required | The user prompt |
| `tools` | `Sequence` | `()` | Tools to expose. Accepts `tool`-wrapped tools or bare `@env.task` templates |
| `model` | `str \| None` | `None` | Model name, for example `"gpt-4o"`. Required when `agent` is not given |
| `instructions` | `str \| None` | `None` | Extra guidance folded into the built agent's backstory |
| `agent` | `Any` | `None` | A pre-built CrewAI `Agent`. Mutually exclusive with `tools` |
| `name` | `str` | `"crewai-agent"` | Agent name, used for debugging and observability |
| `durable` | `bool` | `True` | Record and replay each model turn. Builder path only |
| `observability` | `bool` | `True` | Render the timeline into the task report |
| `memory_key` | `str \| None` | `None` | Stable user or thread ID for cross-run memory |
| `**run_kwargs` | | | Forwarded to `Agent.kickoff_async` |

Returns the final text, taken from the result's `raw` field. Use `run_agent_sync` with the same signature from a sync task.

## Examples

Full runnable examples live in the SDK repository under [`plugins/agents/crewai/examples`](https://github.com/flyteorg/flyte-sdk/tree/main/plugins/agents/crewai/examples):

- `crewai_durable_agent.py`: a single durable agent with traced model turns.
- `crewai_custom_agent.py`: building the `Agent` yourself and passing it as `agent=`.
- `crewai_sync_agent.py`: driving the same agent from a sync task with `run_agent_sync`.
- `crewai_multi_agent.py`: a planner, parallel researchers and an editor, each its own durable action.
- `crewai_crash_resume.py`: the task crashes on its first attempt and replays completed turns on retry.
- `crewai_memory.py`: two separate runs sharing a `memory_key`.
