---
title: Mistral
version: 2.6.10
variants: +flyte +union
layout: py_api
---

# Mistral



Mistral Agents adapter for Flyte (mistralai 2.x).

Bring your own Mistral agent and run it durably on Flyte. Tools you
expose are Flyte tasks (each call a durable child action), and each model turn is
recorded via `flyte.trace` (the turns are in-process HTTP calls, so we can trace
the seam below the SDK's loop) for per-turn replay on retry.

- `flyteplugins.agents.mistral.tool` — turn an `@env.task` into a Mistral run-framework tool.
- `flyteplugins.agents.mistral.run_agent` — run the SDK's agent loop inside your task; return the answer.
## Directory

### Methods

| Method | Description |
|-|-|
| [`run_agent()`](#run_agent) | Run a Mistral agent with the given tools and prompt; return the final text. |
| [`run_agent_sync()`](#run_agent_sync) | Synchronous variant of run_agent for use in sync tasks; runs the async implementation on a dedicated event loop. |
| [`tool()`](#tool) | Wrap a Flyte `@env.task` as a plain async tool function — the generic default. |


## Methods

#### run_agent()

```python
def run_agent(
    input: str,
    tools: typing.Sequence[typing.Any] = (),
    model: str | None = 'mistral-large-latest',
    instructions: str | None = None,
    timeout_ms: int | None = None,
    durable: bool = True,
    observability: bool = True,
    agent_id: str | None = None,
    api_key_env_var: str = 'MISTRAL_API_KEY',
    memory_key: str | None = None,
) -> str
```
Run a Mistral agent with the given tools and prompt; return the final text.

Await this from an async task as `await run_agent(...)`; from a sync task
use `flyteplugins.agents.mistral.run_agent_sync` instead.

Call this from inside an `@env.task` — that task is the durable parent.
The Mistral SDK runs the agent loop; each tool the agent calls runs as a
durable Flyte child action, and (with `durable=True`) each model turn is
recorded for replay. Pass `agent_id` to drive a pre-created server-side
agent instead of an inline `model`.



| Parameter | Type | Description |
|-|-|-|
| `input` | `str` | The user prompt. |
| `tools` | `typing.Sequence[typing.Any]` | `tool`-wrapped tools or bare `@env.task` templates. |
| `model` | `str \| None` | Model for an inline run (when `agent_id` is not given). |
| `instructions` | `str \| None` | System instructions. |
| `timeout_ms` | `int \| None` | Per-turn request timeout (ms), applied by the SDK to each model call inside its loop; `None` uses the SDK default. This bounds a single hung turn — it is not a whole-run cap (Mistral exposes no turn-count limit). To bound the entire agent run, set `timeout=` on the enclosing `@env.task` (the durable parent), which caps all turns + tool calls. |
| `durable` | `bool` | Record/replay each conversation turn via `flyte.trace`. |
| `observability` | `bool` | Render the run timeline into the Flyte task report. |
| `agent_id` | `str \| None` | Reuse an existing server-side agent (instead of `model`). |
| `api_key_env_var` | `str` | Env var holding the Mistral API key (wire as a secret). |
| `memory_key` | `str \| None` | Stable id (e.g. a user/thread id) for cross-run memory. When set, the thread's server-side `conversation_id` is persisted in a keyed `MemoryStore` and reused, so a later run with the same key continues the conversation. `None` disables memory. |

#### run_agent_sync()

```python
def run_agent_sync(
    input: str,
    tools: typing.Sequence[typing.Any] = (),
    model: str | None = 'mistral-large-latest',
    instructions: str | None = None,
    timeout_ms: int | None = None,
    durable: bool = True,
    observability: bool = True,
    agent_id: str | None = None,
    api_key_env_var: str = 'MISTRAL_API_KEY',
    memory_key: str | None = None,
) -> str
```
Synchronous variant of run_agent for use in sync tasks; runs the async implementation on a dedicated event loop.

Run a Mistral agent with the given tools and prompt; return the final text.

Await this from an async task as `await run_agent(...)`; from a sync task
use `flyteplugins.agents.mistral.run_agent_sync` instead.

Call this from inside an `@env.task` — that task is the durable parent.
The Mistral SDK runs the agent loop; each tool the agent calls runs as a
durable Flyte child action, and (with `durable=True`) each model turn is
recorded for replay. Pass `agent_id` to drive a pre-created server-side
agent instead of an inline `model`.



| Parameter | Type | Description |
|-|-|-|
| `input` | `str` | The user prompt. |
| `tools` | `typing.Sequence[typing.Any]` | `tool`-wrapped tools or bare `@env.task` templates. |
| `model` | `str \| None` | Model for an inline run (when `agent_id` is not given). |
| `instructions` | `str \| None` | System instructions. |
| `timeout_ms` | `int \| None` | Per-turn request timeout (ms), applied by the SDK to each model call inside its loop; `None` uses the SDK default. This bounds a single hung turn — it is not a whole-run cap (Mistral exposes no turn-count limit). To bound the entire agent run, set `timeout=` on the enclosing `@env.task` (the durable parent), which caps all turns + tool calls. |
| `durable` | `bool` | Record/replay each conversation turn via `flyte.trace`. |
| `observability` | `bool` | Render the run timeline into the Flyte task report. |
| `agent_id` | `str \| None` | Reuse an existing server-side agent (instead of `model`). |
| `api_key_env_var` | `str` | Env var holding the Mistral API key (wire as a secret). |
| `memory_key` | `str \| None` | Stable id (e.g. a user/thread id) for cross-run memory. When set, the thread's server-side `conversation_id` is persisted in a keyed `MemoryStore` and reused, so a later run with the same key continues the conversation. `None` disables memory. |

#### tool()

```python
def tool(
    func: AsyncFunctionTaskTemplate | typing.Callable | None = None,
    name: str | None = None,
    description: str | None = None,
) -> typing.Callable
```
Wrap a Flyte `@env.task` as a plain async tool function — the generic default.

For SDKs that accept plain Python callables as tools (deriving the schema from the
signature + docstring), this is the whole adapter `tool`: the returned
function carries the task's signature (`functools.wraps`), dispatches to
`task.aio()` (so each call is a durable Flyte child action), exposes
`__wrapped_task__`, and wires the backing task to `flyteplugins.agents.core.ToolTaskResolver`.
Adapters whose SDK needs a native tool type (e.g. OpenAI's
`FunctionTool`, Claude's MCP `SdkMcpTool`) provide their own instead.

Also accepts any other callable — a plain function or an instance of a callable
class defining `__call__` — and returns it usable as a tool as-is, since the
plain-callable SDKs derive the schema by inspecting the callable (a class instance
is inspected through its `__call__`). A `name` or `description` override is
applied to the callable best-effort.

Usable bare, parametrized or as a direct call:

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

