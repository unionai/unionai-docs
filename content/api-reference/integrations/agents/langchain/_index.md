---
title: LangChain
version: 2.5.18
variants: +flyte +union
layout: py_api
---

# LangChain



LangChain adapter for Flyte.

Bring your own LangChain agent and run it durably on Flyte. The adapter provides:

- :func:`tool` — turn a Flyte ``@env.task`` into a LangChain ``StructuredTool``
  (a ``BaseTool``) that executes as a durable child action (own container/GPU,
  retries, caching).
- :func:`run_agent` — run the LangChain agent (a compiled ``create_agent`` graph)
  inside your task and return the final answer. Either pass a pre-built ``agent``
  or let it build one from ``tools`` + ``model`` + ``instructions``.

Each tool call runs as a durable Flyte child action, and the run timeline is
rendered into the Flyte task report.
## Directory

### Methods

| Method | Description |
|-|-|
| [`run_agent()`](#run_agent) | Run a LangChain agent with the given tools and prompt; return the final text. |
| [`run_agent_sync()`](#run_agent_sync) | Synchronous variant of run_agent for use in sync tasks; runs the async implementation on a dedicated event loop. |
| [`tool()`](#tool) | Convert a Flyte task (or plain callable) into a LangChain ``StructuredTool``. |


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
    agent_kwargs: typing.Any,
) -> str
```
Run a LangChain agent with the given tools and prompt; return the final text.

Await this from an async task as ``await run_agent(...)``; from a sync task
use :func:`run_agent_sync` instead.

Call this from inside an ``@env.task`` — that task is the durable parent.
Within it, each tool call runs as a durable Flyte child action. Give the
enclosing task ``retries=...`` for self-healing and ``report=True`` to see
the agent timeline.

Provide either a pre-built ``agent`` (a compiled graph from ``create_agent``)
or ``tools`` + ``model`` to have one built for you.



| Parameter | Type | Description |
|-|-|-|
| `input` | `str` | The user prompt. |
| `tools` | `typing.Sequence[typing.Any]` | ``tool``-wrapped tools or bare ``@env.task`` templates. |
| `model` | `typing.Any` | A LangChain-compatible chat model (e.g. ``ChatOpenAI(model="gpt-4o")``). Required when ``agent`` is not given — one is built using this model. |
| `instructions` | `str \| None` | System prompt for the built agent. |
| `agent` | `typing.Any` | A pre-built LangChain agent (a compiled ``create_agent`` graph). Mutually exclusive with ``tools``. |
| `name` | `str` | Agent name (for debugging/observability). |
| `durable` | `bool` | Record/replay each model turn via ``flyte.trace``. Applies when a model is being built (``tools`` + ``model``, or a caller-passed ``BaseChatModel``) — the model is wrapped in :class:`DurableChatModel`. A fully pre-built compiled ``agent`` cannot be rewrapped, so its model turns are not made durable (its tool calls remain durable regardless). |
| `observability` | `bool` | Render the run timeline into the Flyte task report. |
| `memory_key` | `str \| None` | Stable id (e.g. a user/thread id) for cross-run memory. When set, conversation history is persisted to a keyed ``MemoryStore`` and resumed on a later run with the same key. |
| `agent_kwargs` | `typing.Any` | |

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
    agent_kwargs: typing.Any,
) -> str
```
Synchronous variant of run_agent for use in sync tasks; runs the async implementation on a dedicated event loop.

Run a LangChain agent with the given tools and prompt; return the final text.

    Await this from an async task as ``await run_agent(...)``; from a sync task
    use :func:`run_agent_sync` instead.

    Call this from inside an ``@env.task`` — that task is the durable parent.
    Within it, each tool call runs as a durable Flyte child action. Give the
    enclosing task ``retries=...`` for self-healing and ``report=True`` to see
    the agent timeline.

    Provide either a pre-built ``agent`` (a compiled graph from ``create_agent``)
    or ``tools`` + ``model`` to have one built for you.

    Args:
        input: The user prompt.
        tools: ``tool``-wrapped tools or bare ``@env.task`` templates.
        model: A LangChain-compatible chat model (e.g.
            ``ChatOpenAI(model="gpt-4o")``). Required when ``agent`` is not
            given — one is built using this model.
        instructions: System prompt for the built agent.
        agent: A pre-built LangChain agent (a compiled ``create_agent`` graph).
            Mutually exclusive with ``tools``.
        name: Agent name (for debugging/observability).
        durable: Record/replay each model turn via ``flyte.trace``. Applies when
            a model is being built (``tools`` + ``model``, or a caller-passed
            ``BaseChatModel``) — the model is wrapped in :class:`DurableChatModel`.
            A fully pre-built compiled ``agent`` cannot be rewrapped, so its model
            turns are not made durable (its tool calls remain durable regardless).
        observability: Render the run timeline into the Flyte task report.
        memory_key: Stable id (e.g. a user/thread id) for cross-run memory.
            When set, conversation history is persisted to a keyed ``MemoryStore``
            and resumed on a later run with the same key.
        **agent_kwargs: Additional kwargs forwarded to ``create_agent``.

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
| `agent_kwargs` | `typing.Any` | |

#### tool()

```python
def tool(
    func: AsyncFunctionTaskTemplate | typing.Callable | None,
    name: str | None,
    description: str | None,
) -> typing.Any
```
Convert a Flyte task (or plain callable) into a LangChain ``StructuredTool``.

- For an ``@env.task``: returns a ``StructuredTool`` whose async coroutine runs
  the task as a durable Flyte child action when the agent invokes it. The input
  schema is derived from the task's typed signature. The backing task is wired to
  :class:`~flyteplugins.agents.core.ToolTaskResolver` and exposed via
  ``__wrapped_task__`` so it resolves to itself on the worker (no recursion).
- For a plain (async) callable: returns a ``StructuredTool`` that runs it inline.

Usable bare, parametrized, or as a direct call::

    @tool
    @env.task
    async def get_weather(city: str) -&gt; str: ...


| Parameter | Type | Description |
|-|-|-|
| `func` | `AsyncFunctionTaskTemplate \| typing.Callable \| None` | |
| `name` | `str \| None` | |
| `description` | `str \| None` | |

