---
title: Mistral
weight: 5
variants: +flyte +union
---

# Mistral Agents

Run [Mistral Agents](https://docs.mistral.ai/agents/agents_introduction/) on Flyte, built on the Conversations API in `mistralai` 2.x. Mistral's own runner drives the loop and executes tools. Flyte registers task-backed tools with it, records each conversation turn for replay, and renders the run into the task report.

Mistral is server-side, which changes two things relative to the other adapters: the transcript lives on Mistral's side, and you can drive a pre-created agent by ID instead of an inline model.

## Installation

```bash
pip install flyteplugins-agents-mistral
```

Requires Python 3.10 or later and `mistralai[agents]` 2.0 or later.

## Quick start

```python{hl_lines=[2, 6, 11, 20]}
import flyte
from flyteplugins.agents.mistral import run_agent, tool

env = flyte.TaskEnvironment(
    "mistral-agent",
    secrets=[flyte.Secret(key="mistral_api_key", as_env_var="MISTRAL_API_KEY")],
    image=flyte.Image.from_debian_base().with_pip_packages("flyteplugins-agents-mistral"),
)


@tool
@env.task(cache="auto", retries=3)
async def get_weather(city: str) -> str:
    """Get the current weather for a city."""
    return f"The weather in {city} is sunny, 22C."


@env.task(report=True, retries=3)
async def city_agent(question: str) -> str:
    return await run_agent(question, tools=[get_weather], model="mistral-large-latest")
```

`run_agent` raises with a clear message if the API key is missing, naming the environment variable it looked in.

## How it maps to Flyte

**Tools:** Mistral's `RunContext` takes plain Python functions and registers them with the runner. `tool` produces one whose body dispatches to `task.aio()`, so each call runs as a durable child action.

**Model turns:** The runner makes each turn by calling `conversations.start_async` or `conversations.append_async`, both in-process HTTP calls. With `durable=True` those two methods are wrapped, and each turn is recorded via `flyte.trace`. The `ConversationResponse` round-trips through pydantic JSON, including the polymorphic output entries.

That is the seam directly below the loop. The SDK still owns the loop; on a retry, completed turns replay from their records and completed tool calls come back from cache.

**Observability:** The turns, tool calls and final answer render into the report. The SDK's `RunResult` exposes no token usage, but each turn's `ConversationResponse` does, so the same wrapper tallies it and adds a usage row.

Replayed turns are counted as cached rather than fresh spend, so a retried run does not present a free replay as though it cost money.

## Driving a pre-created agent

Mistral agents can be created server-side and referenced by ID. Pass `agent_id` instead of `model` and the tool calls still run as durable Flyte actions.

```python{hl_lines=[6]}
@env.task(report=True, retries=3)
async def support(request: str) -> str:
    return await run_agent(
        request,
        tools=[lookup_account],
        agent_id="ag_01jd...",
    )
```

Native handoffs work on this path too. A triage agent can hand the conversation to a billing or technical agent by ID, with the whole multi-agent run durable on Flyte.

## Memory

```python
await run_agent(message, model="mistral-large-latest", memory_key="user-alice")
```

Mistral keeps the transcript server-side, so there is nothing to copy. Flyte persists the thread's `conversation_id` in a keyed `MemoryStore` and continues that conversation when the key recurs.

## Bounding a run

`timeout_ms` is a per-turn request timeout that the SDK applies to each model call inside its loop. It bounds a single hung turn. It is not a whole-run cap, and Mistral exposes no turn-count limit.

To bound the entire agent run, including every turn and tool call, set `timeout=` on the enclosing task.

## `run_agent` parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `input` | `str` | required | The user prompt |
| `tools` | `Sequence` | `()` | Tools to expose. Accepts `tool`-wrapped tools or bare `@env.task` templates |
| `model` | `str \| None` | `"mistral-large-latest"` | Model for an inline run, when `agent_id` is not given |
| `instructions` | `str \| None` | `None` | System instructions |
| `timeout_ms` | `int \| None` | `None` | Per-turn request timeout in milliseconds. `None` uses the SDK default |
| `durable` | `bool` | `True` | Record and replay each conversation turn |
| `observability` | `bool` | `True` | Render the timeline into the task report |
| `agent_id` | `str \| None` | `None` | Drive an existing server-side agent instead of `model` |
| `api_key_env_var` | `str` | `"MISTRAL_API_KEY"` | Environment variable holding the API key |
| `memory_key` | `str \| None` | `None` | Stable user or thread ID for cross-run memory |

Returns the final text. Use `run_agent_sync` with the same signature from a sync task.

## Examples

Full runnable examples live in the SDK repository under [`plugins/agents/mistral/examples`](https://github.com/flyteorg/flyte-sdk/tree/main/plugins/agents/mistral/examples):

- `mistral_durable_agent.py`: a single durable agent with per-turn tracing.
- `mistral_crash_resume.py`: the task crashes on its first attempt and replays completed turns on retry.
- `mistral_multi_agent.py`: a planner, parallel researchers and an editor, each its own durable action.
- `mistral_agent_id.py`: driving a pre-created server-side agent by ID.
- `mistral_memory.py`: two separate runs sharing a `memory_key`.
- `mistral_handoffs.py`: native handoffs to a specialist agent, which can pause on a Flyte condition for a human detail.
