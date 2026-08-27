---
title: OpenAI Agents SDK
version: 2.6.10
variants: +flyte +union
layout: py_api
---

# OpenAI Agents SDK



OpenAI Agents SDK adapter for Flyte.

Bring your own `openai-agents` `Agent` (tools, handoffs, guardrails) and run
it durably on Flyte. The adapter provides three things, each independently
usable:

- `flyteplugins.agents.openai.tool` — turn a Flyte `@env.task` into an OpenAI Agents tool
  that executes as a durable child action (own container/GPU, retries,
  caching) when the agent calls it.
- `flyteplugins.agents.openai.FlyteModelProvider` — a `ModelProvider` wrapper that records each
  model turn through `flyte.trace` so a crashed/retried run replays
  completed turns instead of re-calling (and re-billing) the LLM.
- `flyteplugins.agents.openai.FlyteTracingProcessor` — forwards the OpenAI Agents trace (turns, tool
  calls, handoffs, token usage) into the Flyte task report for observability.

`flyteplugins.agents.openai.run_agent` wires all three together for the common case. For full control,
use them directly with `Runner.run` and a `RunConfig`.
## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteModel`](./flytemodel) | Wrap a `agents.models.interface.Model` so each turn is durable. |
| [`FlyteModelProvider`](./flytemodelprovider) | Wrap a `ModelProvider` so every model it returns produces durable turns. |
| [`FlyteSession`](./flytesession) | An `agents` `Session` whose items live in a keyed Flyte `MemoryStore`. |
| [`FlyteTracingProcessor`](./flytetracingprocessor) | Map OpenAI Agents spans onto the shared `flyteplugins.agents.core.ReportTimeline`. |
| [`FunctionTool`](./functiontool) | An OpenAI Agents `FunctionTool` backed by a Flyte task. |

### Methods

| Method | Description |
|-|-|
| [`install_flyte_tracing()`](#install_flyte_tracing) | Install a `flyteplugins.agents.openai.FlyteTracingProcessor` as a global trace processor. |
| [`run_agent()`](#run_agent) | Run an OpenAI Agents SDK agent with Flyte providing the runtime. |
| [`run_agent_sync()`](#run_agent_sync) | Synchronous variant of run_agent for use in sync tasks; runs the async implementation on a dedicated event loop. |
| [`tool()`](#tool) | Flyte-aware replacement for `agents.function_tool` — named `tool` for consistency. |


## Methods

#### install_flyte_tracing()

```python
def install_flyte_tracing(
    exclusive: bool = True,
    tab_name: str = 'Agent',
) -> FlyteTracingProcessor
```
Install a `flyteplugins.agents.openai.FlyteTracingProcessor` as a global trace processor.

With `exclusive=True` (default) it replaces all processors, so traces are
rendered only into the Flyte report and nothing is uploaded to OpenAI's
tracing backend. Set `exclusive=False` to keep the SDK's default processors
(e.g. to also export to the OpenAI dashboard) and add Flyte alongside.


| Parameter | Type | Description |
|-|-|-|
| `exclusive` | `bool` | |
| `tab_name` | `str` | |

#### run_agent()

```python
def run_agent(
    input: str | list[typing.Any],
    agent: Agent | None = None,
    tools: typing.Sequence[typing.Any] = (),
    model: str = 'gpt-4.1',
    instructions: str | None = None,
    name: str = 'flyte-agent',
    max_turns: int = 10,
    durable: bool = True,
    observability: bool = True,
    run_config: RunConfig | None = None,
    hooks: typing.Any = None,
    memory_key: str | None = None,
) -> str
```
Run an OpenAI Agents SDK agent with Flyte providing the runtime.

Await this from an async task as `await run_agent(...)`; from a sync task
use `flyteplugins.agents.openai.run_agent_sync` instead.

Call this from inside an `@env.task` — that task is the durable parent.
Within it, each model turn is recorded via `flyte.trace` (replayed on
retry) and each tool call runs as a durable Flyte child action. Give the
enclosing task `retries=...` for self-healing and `report=True` to see
the agent timeline.

Provide either a fully-built `agent` (keeping its handoffs/guardrails), or
`tools` + `instructions` + `model` to have one built for you. `tools`
may be `flyteplugins.agents.openai.tool`-wrapped tools or bare `@env.task` templates
(wrapped automatically).



| Parameter | Type | Description |
|-|-|-|
| `input` | `str \| list[typing.Any]` | The user prompt (or a list of input items). |
| `agent` | `Agent \| None` | A pre-built `agents.Agent`. Mutually exclusive with `tools`. |
| `tools` | `typing.Sequence[typing.Any]` | Tools to expose (when `agent` is not given). |
| `model` | `str` | Model name (when `agent` is not given). |
| `instructions` | `str \| None` | System instructions (when `agent` is not given). |
| `name` | `str` | Agent name (when `agent` is not given). |
| `max_turns` | `int` | Maximum model to tool turns and vice versa before the SDK raises. |
| `durable` | `bool` | Record/replay each model turn via `flyte.trace`. |
| `observability` | `bool` | Render the run timeline into the Flyte task report. |
| `run_config` | `RunConfig \| None` | A custom `RunConfig`; `model_provider` is wrapped for durability unless `durable=False`. |
| `hooks` | `typing.Any` | Your own `RunHooks`. Any registered instrumentor is offered these, so an observability handler chains onto yours rather than displacing them. |
| `memory_key` | `str \| None` | Stable id (e.g. a user/thread id) for cross-run memory. When set, conversation history is loaded from and saved to a durable, keyed `MemoryStore` (via the SDK's `Session`), so a later run with the same key continues the conversation. `None` disables memory. |

**Returns:** The agent's final output as a string.

#### run_agent_sync()

```python
def run_agent_sync(
    input: str | list[typing.Any],
    agent: Agent | None = None,
    tools: typing.Sequence[typing.Any] = (),
    model: str = 'gpt-4.1',
    instructions: str | None = None,
    name: str = 'flyte-agent',
    max_turns: int = 10,
    durable: bool = True,
    observability: bool = True,
    run_config: RunConfig | None = None,
    hooks: typing.Any = None,
    memory_key: str | None = None,
) -> str
```
Synchronous variant of run_agent for use in sync tasks; runs the async implementation on a dedicated event loop.

Run an OpenAI Agents SDK agent with Flyte providing the runtime.

Await this from an async task as `await run_agent(...)`; from a sync task
use `flyteplugins.agents.openai.run_agent_sync` instead.

Call this from inside an `@env.task` — that task is the durable parent.
Within it, each model turn is recorded via `flyte.trace` (replayed on
retry) and each tool call runs as a durable Flyte child action. Give the
enclosing task `retries=...` for self-healing and `report=True` to see
the agent timeline.

Provide either a fully-built `agent` (keeping its handoffs/guardrails), or
`tools` + `instructions` + `model` to have one built for you. `tools`
may be `flyteplugins.agents.openai.tool`-wrapped tools or bare `@env.task` templates
(wrapped automatically).



| Parameter | Type | Description |
|-|-|-|
| `input` | `str \| list[typing.Any]` | The user prompt (or a list of input items). |
| `agent` | `Agent \| None` | A pre-built `agents.Agent`. Mutually exclusive with `tools`. |
| `tools` | `typing.Sequence[typing.Any]` | Tools to expose (when `agent` is not given). |
| `model` | `str` | Model name (when `agent` is not given). |
| `instructions` | `str \| None` | System instructions (when `agent` is not given). |
| `name` | `str` | Agent name (when `agent` is not given). |
| `max_turns` | `int` | Maximum model to tool turns and vice versa before the SDK raises. |
| `durable` | `bool` | Record/replay each model turn via `flyte.trace`. |
| `observability` | `bool` | Render the run timeline into the Flyte task report. |
| `run_config` | `RunConfig \| None` | A custom `RunConfig`; `model_provider` is wrapped for durability unless `durable=False`. |
| `hooks` | `typing.Any` | Your own `RunHooks`. Any registered instrumentor is offered these, so an observability handler chains onto yours rather than displacing them. |
| `memory_key` | `str \| None` | Stable id (e.g. a user/thread id) for cross-run memory. When set, conversation history is loaded from and saved to a durable, keyed `MemoryStore` (via the SDK's `Session`), so a later run with the same key continues the conversation. `None` disables memory. |

**Returns**

The agent's final output as a string.


#### tool()

```python
def tool(
    func: AsyncFunctionTaskTemplate | typing.Callable | None = None,
    **kwargs: typing.Any,
) -> FunctionTool | OpenAIFunctionTool
```
Flyte-aware replacement for `agents.function_tool` — named `tool` for consistency.

- For an `@env.task` (an `AsyncFunctionTaskTemplate`): returns a
  `flyteplugins.agents.openai.FunctionTool` whose invocation runs the task as a durable Flyte
  action. The tool's JSON schema, name and description are derived by the
  OpenAI Agents SDK from the task's function signature, so strict-mode tool
  calling works unchanged.
- For a plain callable or a `@flyte.trace` helper: forwards to the native
  `agents.function_tool` (runs inline; `@flyte.trace` helpers are still
  recorded for observability when inside a task).

`**kwargs` (e.g. `name_override`, `description_override`) are forwarded
to `agents.function_tool` in both cases.

Usable as a bare decorator, a parametrized decorator, or a direct call:

```python
@tool
@env.task
async def get_weather(city: str) -> str: ...

weather = tool(get_weather, name_override="weather")
```


| Parameter | Type | Description |
|-|-|-|
| `func` | `AsyncFunctionTaskTemplate \| typing.Callable \| None` | |
| `**kwargs` | `typing.Any` | |

