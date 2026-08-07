---
title: Pydantic AI
version: 2.5.18
variants: +flyte +union
layout: py_api
---

# Pydantic AI



Pydantic AI adapter for Flyte.

Bring your own Pydantic AI ``Agent`` and run it durably on Flyte. The adapter
provides:

- :func:`tool` — turn a Flyte ``@env.task`` into a Pydantic AI tool that
  executes as a durable child action (own container/GPU, retries, caching).
  This is the shared :func:`flyteplugins.agents.core.tool`: Pydantic AI accepts
  plain (async) callables in ``Agent(tools=[...])`` and infers each tool's
  schema from the callable's signature, which the core wrapper preserves.
- :func:`run_agent` — run the Pydantic AI agent loop inside your task and return
  the final answer.

Each tool call runs as a durable Flyte child action, and the run timeline is
rendered into the Flyte task report.
## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteModel`](./flytemodel) | Wrap a :class:`~pydantic_ai. |

### Methods

| Method | Description |
|-|-|
| [`run_agent()`](#run_agent) | Run a Pydantic AI agent with the given tools and prompt; return the final text. |
| [`run_agent_sync()`](#run_agent_sync) | Synchronous variant of run_agent for use in sync tasks; runs the async implementation on a dedicated event loop. |
| [`tool()`](#tool) | Wrap a Flyte ``@env. |


## Methods

#### run_agent()

```python
def run_agent(
    input: str,
    tools: typing.Sequence[typing.Any],
    model: typing.Any,
    instructions: str | None,
    agent: typing.Any,
    name: str,
    durable: bool,
    observability: bool,
    memory_key: str | None,
    run_kwargs: typing.Any,
) -> str
```
Run a Pydantic AI agent with the given tools and prompt; return the final text.

Await this from an async task as ``await run_agent(...)``; from a sync task
use :func:`run_agent_sync` instead.

Call this from inside an ``@env.task`` — that task is the durable parent.
Within it, each tool call runs as a durable Flyte child action. Give the
enclosing task ``retries=...`` for self-healing and ``report=True`` to see
the agent timeline.

Provide either a pre-built ``agent`` (with its tools already attached) or
``tools`` + ``model`` to have one built for you — not both.



| Parameter | Type | Description |
|-|-|-|
| `input` | `str` | The user prompt. |
| `tools` | `typing.Sequence[typing.Any]` | ``tool``-wrapped tools or bare ``@env.task`` templates. Used only when no ``agent`` is passed; the built agent attaches them natively. |
| `model` | `typing.Any` | Model name (e.g. ``"openai:gpt-4o"``) or ``pydantic_ai`` ``Model`` instance for the built agent. Required on the builder path (no default is assumed — the adapter is provider agnostic); ignored when a pre-built ``agent`` is given. |
| `instructions` | `str \| None` | System prompt / instructions for the built agent. |
| `agent` | `typing.Any` | A pre-built Pydantic AI ``Agent`` (tools already attached). Mutually exclusive with ``tools``. |
| `name` | `str` | Agent name (for debugging/observability). |
| `durable` | `bool` | Record/replay each model turn via ``flyte.trace``. On the builder path the inferred model is wrapped in ``FlyteModel``; on the prebuilt- agent path durability is applied via ``agent.override(model=...)`` when the agent's model can be obtained (best-effort otherwise). |
| `observability` | `bool` | Render the run timeline into the Flyte task report. |
| `memory_key` | `str \| None` | Stable id (e.g. a user/thread id) for cross-run memory. When set, prior conversation history is loaded from a durable, keyed ``MemoryStore`` and passed as ``message_history=``; after the run the full history is saved back, so a later run with the same key continues the conversation. Best-effort — a memory failure never breaks a run. |
| `run_kwargs` | `typing.Any` | |

**Returns:** The agent's final output as a string.

#### run_agent_sync()

```python
def run_agent_sync(
    input: str,
    tools: typing.Sequence[typing.Any],
    model: typing.Any,
    instructions: str | None,
    agent: typing.Any,
    name: str,
    durable: bool,
    observability: bool,
    memory_key: str | None,
    run_kwargs: typing.Any,
) -> str
```
Synchronous variant of run_agent for use in sync tasks; runs the async implementation on a dedicated event loop.

Run a Pydantic AI agent with the given tools and prompt; return the final text.

    Await this from an async task as ``await run_agent(...)``; from a sync task
    use :func:`run_agent_sync` instead.

    Call this from inside an ``@env.task`` — that task is the durable parent.
    Within it, each tool call runs as a durable Flyte child action. Give the
    enclosing task ``retries=...`` for self-healing and ``report=True`` to see
    the agent timeline.

    Provide either a pre-built ``agent`` (with its tools already attached) or
    ``tools`` + ``model`` to have one built for you — not both.

    Args:
        input: The user prompt.
        tools: ``tool``-wrapped tools or bare ``@env.task`` templates. Used only
            when no ``agent`` is passed; the built agent attaches them natively.
        agent: A pre-built Pydantic AI ``Agent`` (tools already attached).
            Mutually exclusive with ``tools``.
        model: Model name (e.g. ``"openai:gpt-4o"``) or ``pydantic_ai`` ``Model``
            instance for the built agent. Required on the builder path (no default
            is assumed — the adapter is provider agnostic); ignored when a
            pre-built ``agent`` is given.
        instructions: System prompt / instructions for the built agent.
        name: Agent name (for debugging/observability).
        durable: Record/replay each model turn via ``flyte.trace``. On the builder
            path the inferred model is wrapped in ``FlyteModel``; on the prebuilt-
            agent path durability is applied via ``agent.override(model=...)`` when
            the agent's model can be obtained (best-effort otherwise).
        observability: Render the run timeline into the Flyte task report.
        memory_key: Stable id (e.g. a user/thread id) for cross-run memory. When
            set, prior conversation history is loaded from a durable, keyed
            ``MemoryStore`` and passed as ``message_history=``; after the run the
            full history is saved back, so a later run with the same key continues
            the conversation. Best-effort — a memory failure never breaks a run.
        **run_kwargs: Additional kwargs forwarded to ``agent.run`` (e.g. an explicit
            ``message_history=``, which takes precedence over loaded memory).

    Returns:
        The agent's final output as a string.
    


| Parameter | Type | Description |
|-|-|-|
| `input` | `str` | |
| `tools` | `typing.Sequence[typing.Any]` | |
| `model` | `typing.Any` | |
| `instructions` | `str \| None` | |
| `agent` | `typing.Any` | |
| `name` | `str` | |
| `durable` | `bool` | |
| `observability` | `bool` | |
| `memory_key` | `str \| None` | |
| `run_kwargs` | `typing.Any` | |

#### tool()

```python
def tool(
    func: AsyncFunctionTaskTemplate | typing.Callable | None,
    name: str | None,
    description: str | None,
) -> typing.Callable
```
Wrap a Flyte ``@env.task`` as a plain async tool function — the generic default.

For SDKs that accept plain Python callables as tools (deriving the schema from the
signature + docstring), this is the whole adapter ``tool``: the returned
function carries the task's signature (``functools.wraps``), dispatches to
``task.aio()`` (so each call is a durable Flyte child action), exposes
``__wrapped_task__``, and wires the backing task to :class:`ToolTaskResolver`.
Adapters whose SDK needs a native tool type (e.g. OpenAI's
``FunctionTool``, Claude's MCP ``SdkMcpTool``) provide their own instead.

Also accepts any other callable — a plain function or an instance of a callable
class defining ``__call__`` — and returns it usable as a tool as-is, since the
plain-callable SDKs derive the schema by inspecting the callable (a class instance
is inspected through its ``__call__``). A ``name`` or ``description`` override is
applied to the callable best-effort.

Usable bare, parametrized or as a direct call::

    @tool
    @env.task
    async def get_weather(city: str) -&gt; str: ...


| Parameter | Type | Description |
|-|-|-|
| `func` | `AsyncFunctionTaskTemplate \| typing.Callable \| None` | |
| `name` | `str \| None` | |
| `description` | `str \| None` | |

