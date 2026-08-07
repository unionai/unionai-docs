---
title: Core
version: 2.5.19
variants: +flyte +union
layout: py_api
---

# Core



flyteplugins-agents-core — the shared contract every agent-SDK adapter implements.

This package holds the SDK-agnostic machinery that makes Flyte the durable
runtime under any agent framework, so each `flyteplugins-agents-<sdk>` adapter
stays thin and consistent:

- `flyteplugins.agents.core.durable_step` — record a call as a durable, replayable `flyte.trace`
  leaf (the model-turn durability mechanism), keyed by a fingerprint.
- `flyteplugins.agents.core.fingerprint` — a deterministic memo key from a request payload.
- `flyteplugins.agents.core.ToolTaskResolver` / `flyteplugins.agents.core.attach_tool_resolver` — make a tool-backing
  task resolve to itself on the worker.
- `flyteplugins.agents.core.ReportTimeline` — render agent events into the Flyte task report.
- `flyteplugins.agents.core.testing` — `assert_adapter_conforms`, the
  CI-enforced conformance check every adapter runs.

The division of labor every adapter follows: the agent run is a Flyte
`@env.task` (durable parent), each model turn is a `flyte.trace` (a
memoized, replayable leaf), and each tool is a Flyte task invoked as a
durable child action.
## Directory

### Classes

| Class | Description |
|-|-|
| [`ReportTimeline`](./reporttimeline) | A `flyte.report.Timeline` that defaults to the `Agent` report tab. |
| [`ToolTaskResolver`](./tooltaskresolver) | Resolver for a task shadowed at module scope by a tool wrapper. |

### Methods

| Method | Description |
|-|-|
| [`abbrev()`](#abbrev) | HTML-escape `value` for a report row. |
| [`apply_call_wrapper()`](#apply_call_wrapper) | Offer a framework's call to its wrapper and return whatever should be called instead. |
| [`apply_instrumentation()`](#apply_instrumentation) | Offer a framework's run payload to its instrumentor and return the result. |
| [`attach_tool_resolver()`](#attach_tool_resolver) | Point a tool-backing `@env.task` at `flyteplugins.agents.core.ToolTaskResolver`. |
| [`coerce_tool_args()`](#coerce_tool_args) | Coerce LLM-supplied tool args to the task's declared parameter types. |
| [`durable_step()`](#durable_step) | Run `run()` once as a durable, replayable trace step keyed by `request_key`. |
| [`duration_ms()`](#duration_ms) | Format the gap between two ISO-8601 timestamps as `"<n> ms"` (best-effort). |
| [`fingerprint()`](#fingerprint) | A deterministic sha256 hex of a request `payload`. |
| [`flush_report()`](#flush_report) | Flush the active Flyte report — a best-effort no-op when there is none. |
| [`instrumented_frameworks()`](#instrumented_frameworks) | Frameworks with an instrumentor registered, for diagnostics and tests. |
| [`jsonable()`](#jsonable) | Best-effort conversion of an SDK object to something JSON-dumpable. |
| [`register_call_wrapper()`](#register_call_wrapper) | Register the call wrapper for a framework, replacing any previous one. |
| [`register_instrumentor()`](#register_instrumentor) | Register the instrumentor for a framework, replacing any previous one. |
| [`resolve_memory()`](#resolve_memory) | Open (or create) the keyed agent-memory store, or `None` if unavailable. |
| [`run_coro_sync()`](#run_coro_sync) | Run an async-adapter coroutine to completion from synchronous code. |
| [`sync_variant()`](#sync_variant) | Build the synchronous companion of an async adapter entry point. |
| [`task_json_schema()`](#task_json_schema) | The JSON schema of a Flyte task's inputs, via the Flyte type engine. |
| [`tool()`](#tool) | Wrap a Flyte `@env.task` as a plain async tool function — the generic default. |
| [`unregister_call_wrapper()`](#unregister_call_wrapper) | Remove a framework's call wrapper, if one is registered. |
| [`unregister_instrumentor()`](#unregister_instrumentor) | Remove a framework's instrumentor, if one is registered. |


## Methods

#### abbrev()

```python
def abbrev(
    value: typing.Any,
    limit: int = 300,
) -> str
```
HTML-escape `value` for a report row.

Short values render inline. Longer ones collapse into an expandable `<details>`:
the row shows a `limit`-character preview with a `+N` overflow marker, and
clicking it reveals the full content (up to a hard cap). Nothing is dropped on the
floor, so a value that trails off in the report can always be opened in place.


| Parameter | Type | Description |
|-|-|-|
| `value` | `typing.Any` | |
| `limit` | `int` | |

#### apply_call_wrapper()

```python
def apply_call_wrapper(
    framework: str,
    call: typing.Any,
) -> typing.Any
```
Offer a framework's call to its wrapper and return whatever should be called instead.

Returns the original callable when nothing is registered, and also when the wrapper fails:
a half-wrapped call is worse than an uninstrumented one, and observing an agent must never
be the reason it stops working.


| Parameter | Type | Description |
|-|-|-|
| `framework` | `str` | |
| `call` | `typing.Any` | |

#### apply_instrumentation()

```python
def apply_instrumentation(
    framework: str,
    payload: typing.Any,
) -> typing.Any
```
Offer a framework's run payload to its instrumentor and return the result.

Returns the payload untouched when nothing is registered for the framework, and also when
the instrumentor fails: instrumentation is never a reason to fail the agent it is
watching, and a half-modified payload is worse than an uninstrumented one.


| Parameter | Type | Description |
|-|-|-|
| `framework` | `str` | |
| `payload` | `typing.Any` | |

#### attach_tool_resolver()

```python
def attach_tool_resolver(
    task: typing.Any,
)
```
Point a tool-backing `@env.task` at `flyteplugins.agents.core.ToolTaskResolver`.

No-op for anything that isn't an async-function task or that already declares
a custom resolver, so the default resolver is left untouched elsewhere.


| Parameter | Type | Description |
|-|-|-|
| `task` | `typing.Any` | |

#### coerce_tool_args()

```python
def coerce_tool_args(
    task: AsyncFunctionTaskTemplate,
    kwargs: dict[str, typing.Any],
) -> dict[str, typing.Any]
```
Coerce LLM-supplied tool args to the task's declared parameter types.

LLMs emit JSON numbers without a fractional part as `int` (e.g. `42`), but
Flyte's type engine rejects an `int` where a `float` is declared — so the tool
call fails during input conversion, before the child action is even submitted (the
action never appears in the UI, and the task body never runs). This converts `int`
-&gt; `float` for float-annotated params (leaving `bool` alone). Best-effort: returns
the kwargs unchanged if the task's annotations can't be resolved.


| Parameter | Type | Description |
|-|-|-|
| `task` | `AsyncFunctionTaskTemplate` | |
| `kwargs` | `dict[str, typing.Any]` | |

#### durable_step()

```python
def durable_step(
    request_key: str,
    run: typing.Callable[[], typing.Awaitable[typing.Any]],
    name: str = 'durable_step',
    dumps: typing.Callable[[typing.Any], str] = ...,
    loads: typing.Callable[[str], typing.Any] = ...,
) -> typing.Any
```
Run `run()` once as a durable, replayable trace step keyed by `request_key`.

The real (possibly non-serializable) work is captured in the `run` closure,
so the traced function only ever sees the serializable `request_key`. The
result is serialized with `dumps` for the trace record (a `str` is stored
inline and is human-readable in the Flyte UI) and rebuilt with `loads` on
the way out and on replay.

Outside a task context `flyte.trace` is a transparent pass-through, so this
also works unchanged for local runs and unit tests.


| Parameter | Type | Description |
|-|-|-|
| `request_key` | `str` | A deterministic fingerprint of the call; the trace memo key. |
| `run` | `typing.Callable[[], typing.Awaitable[typing.Any]]` | Zero-arg async callable performing the real work. |
| `name` | `str` | Label for the trace action in the Flyte UI. |
| `dumps` | `typing.Callable[[typing.Any], str]` | Serialize the result to a `str` for the trace record. |
| `loads` | `typing.Callable[[str], typing.Any]` | Rebuild the result from the recorded `str`. |

#### duration_ms()

```python
def duration_ms(
    start_iso: typing.Any,
    end_iso: typing.Any,
) -> str
```
Format the gap between two ISO-8601 timestamps as `"<n> ms"` (best-effort).


| Parameter | Type | Description |
|-|-|-|
| `start_iso` | `typing.Any` | |
| `end_iso` | `typing.Any` | |

#### fingerprint()

```python
def fingerprint(
    payload: typing.Mapping[str, typing.Any],
) -> str
```
A deterministic sha256 hex of a request `payload`.

Must be a pure function of the semantic request so replays line up. Pass a
mapping of the request's identifying fields (e.g. system prompt, input
items, model, tool names) — not callables or live objects. Anything not
natively JSON-serializable is coerced with `str`.


| Parameter | Type | Description |
|-|-|-|
| `payload` | `typing.Mapping[str, typing.Any]` | |

#### flush_report()

```python
def flush_report()
```
Flush the active Flyte report — a best-effort no-op when there is none.

Adapters call this once after a run so the rendered timeline is published.


#### instrumented_frameworks()

```python
def instrumented_frameworks()
```
Frameworks with an instrumentor registered, for diagnostics and tests.


#### jsonable()

```python
def jsonable(
    obj: typing.Any,
) -> typing.Any
```
Best-effort conversion of an SDK object to something JSON-dumpable.


| Parameter | Type | Description |
|-|-|-|
| `obj` | `typing.Any` | |

#### register_call_wrapper()

```python
def register_call_wrapper(
    framework: str,
    wrapper: CallWrapper,
)
```
Register the call wrapper for a framework, replacing any previous one.


| Parameter | Type | Description |
|-|-|-|
| `framework` | `str` | |
| `wrapper` | `CallWrapper` | |

#### register_instrumentor()

```python
def register_instrumentor(
    framework: str,
    instrumentor: Instrumentor,
)
```
Register the instrumentor for a framework, replacing any previous one.



| Parameter | Type | Description |
|-|-|-|
| `framework` | `str` | Adapter name, matching the plugin directory: "langgraph", "langchain", "openai", "claude", "google", "pydantic_ai". |
| `instrumentor` | `Instrumentor` | Called with the framework's run payload, returns the modified payload. |

#### resolve_memory()

```python
def resolve_memory(
    memory_key: str | None,
    audit: bool = True,
) -> 'MemoryStore | None'
```
Open (or create) the keyed agent-memory store, or `None` if unavailable.

Best-effort: returns `None` (and logs) when `memory_key` is falsy or no
durable store can be resolved — e.g. no Flyte context/org, or an invalid key —
so memory never breaks a run. Call from inside an `@env.task`; the store's
remote path is derived from the run context and is stable across runs for the
same key.



| Parameter | Type | Description |
|-|-|-|
| `memory_key` | `str \| None` | A stable single-segment id (a user/thread id). `None` or empty disables memory. |
| `audit` | `bool` | Keep the store's append-only audit log (the `MemoryStore` default). |

#### run_coro_sync()

```python
def run_coro_sync(
    coro: typing.Coroutine[typing.Any, typing.Any, R],
) -> R
```
Run an async-adapter coroutine to completion from synchronous code.

Runs the coroutine on the calling thread's persistent background event
loop (via flyte._utils.asyn.loop_manager). Exceptions propagate to the
caller unchanged.


| Parameter | Type | Description |
|-|-|-|
| `coro` | `typing.Coroutine[typing.Any, typing.Any, R]` | |

#### sync_variant()

```python
def sync_variant(
    afunc: typing.Callable[..., typing.Coroutine[typing.Any, typing.Any, R]],
) -> typing.Callable[..., R]
```
Build the synchronous companion of an async adapter entry point.

Adapters use this to derive run_agent_sync from run_agent:

```python
run_agent_sync = sync_variant(run_agent)
```

The wrapper keeps run_agent's signature and docstring for introspection and
dispatches through `flyteplugins.agents.core.run_coro_sync`.


| Parameter | Type | Description |
|-|-|-|
| `afunc` | `typing.Callable[..., typing.Coroutine[typing.Any, typing.Any, R]]` | |

#### task_json_schema()

```python
def task_json_schema(
    task: AsyncFunctionTaskTemplate,
) -> dict[str, typing.Any]
```
The JSON schema of a Flyte task's inputs, via the Flyte type engine.

Useful for adapters whose SDK wants a JSON-schema tool definition and that
prefer Flyte's type-engine schema (correct `Literal` enums, `File`/`Dir`
/`DataFrame`, dataclasses) over the SDK's own signature inspection.


| Parameter | Type | Description |
|-|-|-|
| `task` | `AsyncFunctionTaskTemplate` | |

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

#### unregister_call_wrapper()

```python
def unregister_call_wrapper(
    framework: str,
)
```
Remove a framework's call wrapper, if one is registered.


| Parameter | Type | Description |
|-|-|-|
| `framework` | `str` | |

#### unregister_instrumentor()

```python
def unregister_instrumentor(
    framework: str,
)
```
Remove a framework's instrumentor, if one is registered.


| Parameter | Type | Description |
|-|-|-|
| `framework` | `str` | |

