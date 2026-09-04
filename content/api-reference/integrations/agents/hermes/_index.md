---
title: Hermes
description: "Hermes agent adapter for Flyte."
icon: book
version: 2.7.1
variants: +flyte +union
layout: py_api
---

# Hermes



Hermes agent adapter for Flyte.

Bring your own Hermes agent (the `hermes-agent` package's `AIAgent`) and
run it durably on Flyte. The adapter provides:

- `flyteplugins.agents.hermes.tool` — turn a Flyte `@env.task` into a Hermes tool that executes as
  a durable child action (own container/GPU, retries, caching), registered in
  the Hermes tool registry under the `flyteplugins.agents.hermes.FLYTE_TOOLSET` toolset.
- `flyteplugins.agents.hermes.run_agent` — run the Hermes agent loop inside your task and return the
  final answer.

Each tool call runs as a durable Flyte child action, and the run timeline is
rendered into the Flyte task report.
## Directory

### Methods

| Method | Description |
|-|-|
| [`run_agent()`](#run_agent) | Run a Hermes agent with the given tools and prompt; return the final text. |
| [`run_agent_sync()`](#run_agent_sync) | Synchronous variant of run_agent for use in sync tasks; runs the async implementation on a dedicated event loop. |
| [`tool()`](#tool) | Convert a Flyte task (or plain callable) into a Hermes tool. |


### Variables

| Property | Type | Description |
|-|-|-|
| `FLYTE_TOOLSET` | `str` |  |

## Methods

#### run_agent()

```python
def run_agent(
    input: str,
    tools: typing.Sequence[typing.Any] = (),
    model: str | None = None,
    instructions: str | None = None,
    agent: typing.Any = None,
    name: str = 'hermes-agent',
    durable: bool = True,
    observability: bool = True,
    memory_key: str | None = None,
    **agent_kwargs: typing.Any,
) -> str
```
Run a Hermes agent with the given tools and prompt; return the final text.

Await this from an async task as `await run_agent(...)`; from a sync task
use `flyteplugins.agents.hermes.run_agent_sync` instead.

Call this from inside an `@env.task` — that task is the durable parent.
Within it, each tool call runs as a durable Flyte child action. Give the
enclosing task `retries=...` for self-healing and `report=True` to see
the agent timeline.

Provide either a pre-built `agent` (an `AIAgent` with its own
`enabled_toolsets`) or `tools` + `model` to have one built for you.



| Parameter | Type | Description |
|-|-|-|
| `input` | `str` | The user prompt. |
| `tools` | `typing.Sequence[typing.Any]` | `tool`-wrapped tools or bare `@env.task` templates. |
| `model` | `str \| None` | Model name for the built agent. Required when `agent` is not given (there is no default model). |
| `instructions` | `str \| None` | System prompt. On the builder path this becomes the agent's `ephemeral_system_prompt`; with a pre-built agent it is passed as this run's `system_message`. |
| `agent` | `typing.Any` | A pre-built Hermes `AIAgent`. Mutually exclusive with `tools`. |
| `name` | `str` | Agent name (used for the scoped toolset and observability). |
| `durable` | `bool` | Accepted for the shared adapter contract, but currently a no-op for Hermes: `hermes-agent` exposes no per-model-turn hook (the model client is buried inside `AIAgent`), so completed model turns cannot be recorded/replayed via `flyte.trace` the way the openai/langchain adapters do. Tool calls are durable regardless — each runs as a Flyte child action with retries and caching — so a retried task still self-heals at tool granularity. |
| `observability` | `bool` | Render the run timeline into the Flyte task report. |
| `memory_key` | `str \| None` | Stable id (e.g. a user/thread id) for cross-run memory. When set, conversation history is persisted to a keyed `MemoryStore` and resumed on a later run with the same key (passed to Hermes as `conversation_history`). |
| `**agent_kwargs` | `typing.Any` | |

**Returns:** The agent's final output as a string.

#### run_agent_sync()

```python
def run_agent_sync(
    input: str,
    tools: typing.Sequence[typing.Any] = (),
    model: str | None = None,
    instructions: str | None = None,
    agent: typing.Any = None,
    name: str = 'hermes-agent',
    durable: bool = True,
    observability: bool = True,
    memory_key: str | None = None,
    **agent_kwargs: typing.Any,
) -> str
```
Synchronous variant of run_agent for use in sync tasks; runs the async implementation on a dedicated event loop.

Run a Hermes agent with the given tools and prompt; return the final text.

Await this from an async task as `await run_agent(...)`; from a sync task
use `flyteplugins.agents.hermes.run_agent_sync` instead.

Call this from inside an `@env.task` — that task is the durable parent.
Within it, each tool call runs as a durable Flyte child action. Give the
enclosing task `retries=...` for self-healing and `report=True` to see
the agent timeline.

Provide either a pre-built `agent` (an `AIAgent` with its own
`enabled_toolsets`) or `tools` + `model` to have one built for you.



| Parameter | Type | Description |
|-|-|-|
| `input` | `str` | The user prompt. |
| `tools` | `typing.Sequence[typing.Any]` | `tool`-wrapped tools or bare `@env.task` templates. |
| `model` | `str \| None` | Model name for the built agent. Required when `agent` is not given (there is no default model). |
| `instructions` | `str \| None` | System prompt. On the builder path this becomes the agent's `ephemeral_system_prompt`; with a pre-built agent it is passed as this run's `system_message`. |
| `agent` | `typing.Any` | A pre-built Hermes `AIAgent`. Mutually exclusive with `tools`. |
| `name` | `str` | Agent name (used for the scoped toolset and observability). |
| `durable` | `bool` | Accepted for the shared adapter contract, but currently a no-op for Hermes: `hermes-agent` exposes no per-model-turn hook (the model client is buried inside `AIAgent`), so completed model turns cannot be recorded/replayed via `flyte.trace` the way the openai/langchain adapters do. Tool calls are durable regardless — each runs as a Flyte child action with retries and caching — so a retried task still self-heals at tool granularity. |
| `observability` | `bool` | Render the run timeline into the Flyte task report. |
| `memory_key` | `str \| None` | Stable id (e.g. a user/thread id) for cross-run memory. When set, conversation history is persisted to a keyed `MemoryStore` and resumed on a later run with the same key (passed to Hermes as `conversation_history`). |
| `**agent_kwargs` | `typing.Any` | |

**Returns**

The agent's final output as a string.


#### tool()

```python
def tool(
    func: AsyncFunctionTaskTemplate | typing.Callable | None = None,
    name: str | None = None,
    description: str | None = None,
) -> typing.Any
```
Convert a Flyte task (or plain callable) into a Hermes tool.

- For an `@env.task`: returns the shared core tool wrapper (a plain async
  function dispatching to the task as a durable Flyte child action, with
  `__wrapped_task__` and the resolver wired), *and* registers it in the
  Hermes tool registry under `flyteplugins.agents.hermes.FLYTE_TOOLSET` so an `AIAgent` can
  call it by name. The input schema is derived from the task via the Flyte
  type engine.
- For a plain (sync or async) callable: registers it as an inline Hermes
  tool, deriving the schema from its signature.

Usable bare, parametrized, or as a direct call:

```python
@tool
@env.task
async def get_weather(city: str) -> str: ...
```


| Parameter | Type | Description |
|-|-|-|
| `func` | `AsyncFunctionTaskTemplate \| typing.Callable \| None` | |
| `name` | `str \| None` | |
| `description` | `str \| None` | |

