---
title: CrewAI
version: 2.5.18
variants: +flyte +union
layout: py_api
---

# CrewAI



CrewAI adapter for Flyte.

Bring your own CrewAI ``Agent`` and run it durably on Flyte. The adapter
provides:

- :func:`tool` — turn a Flyte ``@env.task`` into a CrewAI tool that executes as
  a durable child action (own container/GPU, retries, caching).
- :func:`run_agent` — run the CrewAI agent loop inside your task and return the
  final answer.

Each tool call runs as a durable Flyte child action, and the run timeline is
rendered into the Flyte task report.
## Directory

### Methods

| Method | Description |
|-|-|
| [`run_agent()`](#run_agent) | Run a CrewAI agent with the given tools and prompt; return the final text. |
| [`run_agent_sync()`](#run_agent_sync) | Synchronous variant of run_agent for use in sync tasks; runs the async implementation on a dedicated event loop. |
| [`tool()`](#tool) | Convert a Flyte task (or plain callable) into a CrewAI ``BaseTool``. |


## Methods

#### run_agent()

```python
def run_agent(
    input: str,
    tools: typing.Sequence[typing.Any],
    model: str | None,
    instructions: str | None,
    agent: typing.Any,
    name: str,
    durable: bool,
    observability: bool,
    memory_key: str | None,
    run_kwargs: typing.Any,
) -> str
```
Run a CrewAI agent with the given tools and prompt; return the final text.

Await this from an async task as ``await run_agent(...)``; from a sync task
use :func:`run_agent_sync` instead.

Call this from inside an ``@env.task`` — that task is the durable parent.
Within it, each tool call runs as a durable Flyte child action. Give the
enclosing task ``retries=...`` for self-healing and ``report=True`` to see
the agent timeline.

Provide either a pre-built ``agent`` (with its own tools already attached) or
``tools`` + ``model`` to have one built for you — not both.



| Parameter | Type | Description |
|-|-|-|
| `input` | `str` | The user prompt. |
| `tools` | `typing.Sequence[typing.Any]` | ``tool``-wrapped tools or bare ``@env.task`` templates. Attached natively to the built ``Agent(tools=...)``. Ignored when ``agent`` is given (a pre-built agent carries its own tools). |
| `model` | `str \| None` | Model name (e.g. ``"gpt-4o"``) for the built agent. Required on the builder path (no default is assumed — the adapter is provider agnostic); ignored when a pre-built ``agent`` is given. |
| `instructions` | `str \| None` | Extra guidance folded into the built agent's backstory. |
| `agent` | `typing.Any` | A pre-built CrewAI ``Agent``. Mutually exclusive with ``tools``. |
| `name` | `str` | Agent name (for debugging/observability). |
| `durable` | `bool` | Record/replay each model turn via ``flyte.trace``. Applied only when ``run_agent`` builds the agent (the builder sets a durable ``llm``); a pre-built ``agent`` keeps its own ``llm`` and is not rewrapped, so its turns are not durable. |
| `observability` | `bool` | Render the run timeline into the Flyte task report. |
| `memory_key` | `str \| None` | Stable id (e.g. a user/thread id) for cross-run memory. When set, conversation history is persisted to a keyed ``MemoryStore`` and resumed on a later run with the same key. |
| `run_kwargs` | `typing.Any` | |

**Returns:** The agent's final output as a string.

#### run_agent_sync()

```python
def run_agent_sync(
    input: str,
    tools: typing.Sequence[typing.Any],
    model: str | None,
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

Run a CrewAI agent with the given tools and prompt; return the final text.

    Await this from an async task as ``await run_agent(...)``; from a sync task
    use :func:`run_agent_sync` instead.

    Call this from inside an ``@env.task`` — that task is the durable parent.
    Within it, each tool call runs as a durable Flyte child action. Give the
    enclosing task ``retries=...`` for self-healing and ``report=True`` to see
    the agent timeline.

    Provide either a pre-built ``agent`` (with its own tools already attached) or
    ``tools`` + ``model`` to have one built for you — not both.

    Args:
        input: The user prompt.
        tools: ``tool``-wrapped tools or bare ``@env.task`` templates. Attached
            natively to the built ``Agent(tools=...)``. Ignored when ``agent`` is
            given (a pre-built agent carries its own tools).
        model: Model name (e.g. ``"gpt-4o"``) for the built agent. Required on
            the builder path (no default is assumed — the adapter is provider
            agnostic); ignored when a pre-built ``agent`` is given.
        instructions: Extra guidance folded into the built agent's backstory.
        agent: A pre-built CrewAI ``Agent``. Mutually exclusive with ``tools``.
        name: Agent name (for debugging/observability).
        durable: Record/replay each model turn via ``flyte.trace``. Applied only
            when ``run_agent`` builds the agent (the builder sets a durable
            ``llm``); a pre-built ``agent`` keeps its own ``llm`` and is not
            rewrapped, so its turns are not durable.
        observability: Render the run timeline into the Flyte task report.
        memory_key: Stable id (e.g. a user/thread id) for cross-run memory.
            When set, conversation history is persisted to a keyed ``MemoryStore``
            and resumed on a later run with the same key.
        **run_kwargs: Additional kwargs forwarded to ``Agent.kickoff_async``.

    Returns:
        The agent's final output as a string.
    


| Parameter | Type | Description |
|-|-|-|
| `input` | `str` | |
| `tools` | `typing.Sequence[typing.Any]` | |
| `model` | `str \| None` | |
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
) -> typing.Any
```
Convert a Flyte task (or plain callable) into a CrewAI ``BaseTool``.

- For an ``@env.task``: returns a ``BaseTool`` whose execution runs the task as
  a durable Flyte child action when the agent invokes it. The input schema is
  derived from the task via the Flyte type engine. The backing task is wired
  to :class:`~flyteplugins.agents.core.ToolTaskResolver` and exposed via
  ``__wrapped_task__`` so it resolves to itself on the worker (no recursion).
- For a plain (async) callable: returns a ``BaseTool`` that runs it inline.

The returned object is a native ``crewai.tools.BaseTool`` instance, so it can be
attached directly to ``Agent(tools=[...])``.

Usable bare, parametrized, or as a direct call::

    @tool
    @env.task
    async def get_weather(city: str) -&gt; str: ...


| Parameter | Type | Description |
|-|-|-|
| `func` | `AsyncFunctionTaskTemplate \| typing.Callable \| None` | |
| `name` | `str \| None` | |
| `description` | `str \| None` | |

