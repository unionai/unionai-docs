---
title: LangGraph
version: 2.5.18
variants: +flyte +union
layout: py_api
---

# LangGraph



LangGraph adapter for Flyte.

Bring your own LangGraph ``StateGraph`` and run it durably on Flyte. You build the
graph; the adapter provides the durable, observable building blocks:

- :func:`tool` — turn a Flyte ``@env.task`` into a LangChain ``StructuredTool``
  (a first-class LangGraph tool) that executes as a durable child action (own
  container/GPU, retries, caching).
- :func:`ai_node` — the model-calling node: binds the tools to your chat model
  and records each model turn durably (replayed on retry).
- :func:`tool_node` — the tool-executing node: runs the model's tool calls as
  durable Flyte child actions.
- :func:`run_agent` — drive a compiled graph (or build a default one from tools)
  inside your task and return the final answer.

Each tool call runs as a durable Flyte child action, and the run timeline is
rendered into the Flyte task report.
## Directory

### Methods

| Method | Description |
|-|-|
| [`ai_node()`](#ai_node) | Build the model-calling node for a tool-calling graph. |
| [`run_agent()`](#run_agent) | Run a LangGraph graph and return the final text. |
| [`run_agent_sync()`](#run_agent_sync) | Synchronous variant of run_agent for use in sync tasks; runs the async implementation on a dedicated event loop. |
| [`tool()`](#tool) | Convert a Flyte task (or plain callable) into a LangChain ``StructuredTool``. |
| [`tool_node()`](#tool_node) | Build the tool-executing node for a tool-calling graph. |


## Methods

#### ai_node()

```python
def ai_node(
    model: 'BaseChatModel',
    tools: typing.Sequence[typing.Any],
    name: str = 'ai',
    durable: bool = True,
    observability: bool = True,
) -> Node
```
Build the model-calling node for a tool-calling graph.

The returned node binds ``tools`` to ``model`` and runs a single model turn
over ``state["messages"]``, appending the model's response. Pass
``@tool``-wrapped tasks (or any LangChain ``BaseTool``) as ``tools``.



| Parameter | Type | Description |
|-|-|-|
| `model` | `'BaseChatModel'` | A LangChain chat model (e.g. ``ChatOpenAI(model="gpt-4o")``). |
| `tools` | `typing.Sequence[typing.Any]` | The tools to expose to the model. |
| `name` | `str` | Node label (used for the graph node and the trace/report entry). |
| `durable` | `bool` | Record each model turn via ``flyte.trace`` so retries replay it. |
| `observability` | `bool` | Render each model turn into the Flyte task report. |

**Returns:** An async node ``state -> {"messages": [ai_message]}``.

#### run_agent()

```python
def run_agent(
    input: str | typing.Any,
    tools: typing.Sequence[typing.Any] = (),
    model: typing.Any = None,
    instructions: str | None = None,
    agent: typing.Any = None,
    name: str = 'langgraph-agent',
    durable: bool = True,
    observability: bool = True,
    memory_key: str | None = None,
    **run_kwargs: typing.Any,
) -> str
```
Run a LangGraph graph and return the final text.

Await this from an async task as ``await run_agent(...)``; from a sync task
use `run_agent_sync` instead.

Call this from inside an ``@env.task`` — that task is the durable parent.
Within it, each model turn is recorded via ``flyte.trace`` (replayed on
retry) and each tool call runs as a durable Flyte child action. Give the
enclosing task ``retries=...`` for self-healing and ``report=True`` to see
the agent timeline.

Provide either a pre-built ``agent`` (a compiled ``StateGraph`` you built
with `ai_node` / `tool_node`) or ``tools`` to have a default
tool-calling graph built for you. The two are mutually exclusive.



| Parameter | Type | Description |
|-|-|-|
| `input` | `str \| typing.Any` | The user prompt (a ``str``) or a full graph input state (a dict). |
| `tools` | `typing.Sequence[typing.Any]` | ``@tool``-wrapped tools or bare ``@env.task`` templates (used only when ``agent`` is not given). |
| `model` | `typing.Any` | A LangChain chat-model instance (e.g. ``ChatOpenAI(model="gpt-4o")``) or a ``provider:model`` string (resolved via ``init_chat_model``, which requires the ``langchain`` package). Required when building the graph (i.e. when ``agent`` is not given). |
| `instructions` | `str \| None` | System prompt prepended to a built graph's messages. |
| `agent` | `typing.Any` | A pre-built compiled LangGraph graph. Mutually exclusive with ``tools``. |
| `name` | `str` | Graph name (for debugging/observability). |
| `durable` | `bool` | Record each model turn via ``flyte.trace`` (built graphs only). |
| `observability` | `bool` | Render the run timeline into the Flyte task report. |
| `memory_key` | `str \| None` | Stable id (e.g. a user/thread id) for cross-run memory. When set, the conversation transcript is persisted to a keyed ``MemoryStore`` and resumed on a later run with the same key. |
| `**run_kwargs` | `typing.Any` | |

**Returns:** The graph's final assistant message as a string.

#### run_agent_sync()

```python
def run_agent_sync(
    input: str | typing.Any,
    tools: typing.Sequence[typing.Any] = (),
    model: typing.Any = None,
    instructions: str | None = None,
    agent: typing.Any = None,
    name: str = 'langgraph-agent',
    durable: bool = True,
    observability: bool = True,
    memory_key: str | None = None,
    **run_kwargs: typing.Any,
) -> str
```
Synchronous variant of run_agent for use in sync tasks; runs the async implementation on a dedicated event loop.

Run a LangGraph graph and return the final text.

Await this from an async task as ``await run_agent(...)``; from a sync task
use `run_agent_sync` instead.

Call this from inside an ``@env.task`` — that task is the durable parent.
Within it, each model turn is recorded via ``flyte.trace`` (replayed on
retry) and each tool call runs as a durable Flyte child action. Give the
enclosing task ``retries=...`` for self-healing and ``report=True`` to see
the agent timeline.

Provide either a pre-built ``agent`` (a compiled ``StateGraph`` you built
with `ai_node` / `tool_node`) or ``tools`` to have a default
tool-calling graph built for you. The two are mutually exclusive.



| Parameter | Type | Description |
|-|-|-|
| `input` | `str \| typing.Any` | The user prompt (a ``str``) or a full graph input state (a dict). |
| `tools` | `typing.Sequence[typing.Any]` | ``@tool``-wrapped tools or bare ``@env.task`` templates (used only when ``agent`` is not given). |
| `model` | `typing.Any` | A LangChain chat-model instance (e.g. ``ChatOpenAI(model="gpt-4o")``) or a ``provider:model`` string (resolved via ``init_chat_model``, which requires the ``langchain`` package). Required when building the graph (i.e. when ``agent`` is not given). |
| `instructions` | `str \| None` | System prompt prepended to a built graph's messages. |
| `agent` | `typing.Any` | A pre-built compiled LangGraph graph. Mutually exclusive with ``tools``. |
| `name` | `str` | Graph name (for debugging/observability). |
| `durable` | `bool` | Record each model turn via ``flyte.trace`` (built graphs only). |
| `observability` | `bool` | Render the run timeline into the Flyte task report. |
| `memory_key` | `str \| None` | Stable id (e.g. a user/thread id) for cross-run memory. When set, the conversation transcript is persisted to a keyed ``MemoryStore`` and resumed on a later run with the same key. |
| `**run_kwargs` | `typing.Any` | |

**Returns**

The graph's final assistant message as a string.


#### tool()

```python
def tool(
    func: AsyncFunctionTaskTemplate | typing.Callable | None = None,
    name: str | None = None,
    description: str | None = None,
) -> typing.Any
```
Convert a Flyte task (or plain callable) into a LangChain ``StructuredTool``.

- For an ``@env.task``: returns a ``StructuredTool`` whose async body runs the
  task as a durable Flyte child action when the graph invokes it. The input
  schema is inferred from the task's typed signature. The backing task is
  wired to `ToolTaskResolver` and exposed via
  ``__wrapped_task__`` so it resolves to itself on the worker (no recursion).
- For a plain (async) callable: returns a ``StructuredTool`` that runs it inline.

The result is a first-class LangGraph tool — bind it to a model or hand it to
`tool_node` /
`ai_node`.

Usable bare, parametrized, or as a direct call::

    @tool
    @env.task
    async def get_weather(city: str) -&gt; str: ...


| Parameter | Type | Description |
|-|-|-|
| `func` | `AsyncFunctionTaskTemplate \| typing.Callable \| None` | |
| `name` | `str \| None` | |
| `description` | `str \| None` | |

#### tool_node()

```python
def tool_node(
    tools: typing.Sequence[typing.Any],
    name: str = 'tools',
    observability: bool = True,
) -> Node
```
Build the tool-executing node for a tool-calling graph.

The returned node reads the tool calls from the last message and runs each
one, appending a ``ToolMessage`` per call. ``@tool``-wrapped tasks run as
durable Flyte child actions; anything else runs as the tool defines.



| Parameter | Type | Description |
|-|-|-|
| `tools` | `typing.Sequence[typing.Any]` | The tools available to execute (``@tool``-wrapped tasks or any LangChain ``BaseTool``). |
| `name` | `str` | Node label (used for the report entry). |
| `observability` | `bool` | Render each tool call/result into the Flyte task report. |

**Returns:** An async node ``state -> {"messages": [tool_message, ...]}``.

