---
title: Google ADK
version: 2.5.18
variants: +flyte +union
layout: py_api
---

# Google ADK



Google ADK (Agent Development Kit) adapter for Flyte.

Bring your own ``google-adk`` agent and run it durably on Flyte. ADK's ``Runner``
owns the loop; Flyte is the runtime underneath: the tools you expose are Flyte tasks
(durable child actions), each model turn is recorded for replay (``durable=True``),
the run timeline renders into the task report, and ``memory_key`` gives cross-run
conversation memory.

- :func:`tool` — turn an ``@env.task`` into a Google ADK tool.
- :func:`run_agent` — run the ADK agent loop inside your task and return the answer.
- :func:`durable_model` — wrap a model so its turns are durable, for hand-built agent
  trees (e.g. sub-agent transfers) passed to ``run_agent`` via ``agent=``.

Set the model provider's API key in the environment (e.g. ``GOOGLE_API_KEY`` for
Gemini) — wire it as a Flyte secret.
## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteLlm`](./flytellm) | A ``BaseLlm`` that records each model turn via ``durable_step`` for replay. |

### Methods

| Method | Description |
|-|-|
| [`durable_model()`](#durable_model) | Wrap ``model`` (a name string or ``BaseLlm``) so its turns are durable. |
| [`run_agent()`](#run_agent) | Run a Google ADK agent with the given tools and prompt; return the final text. |
| [`run_agent_sync()`](#run_agent_sync) | Synchronous variant of run_agent for use in sync tasks; runs the async implementation on a dedicated event loop. |
| [`tool()`](#tool) | Wrap a Flyte ``@env. |


## Methods

#### durable_model()

```python
def durable_model(
    model: typing.Any,
) -> typing.Any
```
Wrap ``model`` (a name string or ``BaseLlm``) so its turns are durable.

Returns a :class:`FlyteLlm` over the resolved inner model, or ``model`` unchanged
when it can't be wrapped (durability is best-effort, never fatal).


| Parameter | Type | Description |
|-|-|-|
| `model` | `typing.Any` | |

#### run_agent()

```python
def run_agent(
    input: str,
    agent: typing.Any,
    tools: typing.Sequence[typing.Any],
    model: str,
    instructions: str | None,
    name: str,
    max_llm_calls: int | None,
    durable: bool,
    observability: bool,
    memory_key: str | None,
    app_name: str,
    user_id: str,
) -> str
```
Run a Google ADK agent with the given tools and prompt; return the final text.

Await this from an async task as ``await run_agent(...)``; from a sync task
use :func:`run_agent_sync` instead.

Call this from inside an ``@env.task`` — that task is the durable parent, and each
tool the agent calls runs as a durable Flyte child action. Provide either a
pre-built ``agent`` (an ADK ``LlmAgent``/``BaseAgent``) or ``tools`` + ``model`` +
``instructions`` to have one built.



| Parameter | Type | Description |
|-|-|-|
| `input` | `str` | The user prompt. |
| `agent` | `typing.Any` | A pre-built ADK agent. Mutually exclusive with ``tools``. |
| `tools` | `typing.Sequence[typing.Any]` | ``tool``-wrapped tools or bare ``@env.task`` templates. |
| `model` | `str` | Model name for the built agent (e.g. ``gemini-2.0-flash``). |
| `instructions` | `str \| None` | System instruction for the built agent. |
| `name` | `str` | Agent name (a valid Python identifier). ADK injects this into the system prompt as the model's "internal name", so it can surface in replies — keep it natural (defaults to ``"assistant"``; avoid a brand-y/internal label). |
| `max_llm_calls` | `int \| None` | Cap on model (LLM) calls before ADK raises ``LlmCallsLimitExceededError`` (its runaway-loop guard, via ``RunConfig.max_llm_calls``); ``None`` uses ADK's default of 500. Counts LLM calls, not conversational turns (a tool round is ~2 calls). For a wall-clock bound on the whole run, set ``timeout=`` on the enclosing ``@env.task``. |
| `durable` | `bool` | Wrap the model so each turn is recorded/replayed via ``flyte.trace``. |
| `observability` | `bool` | Render the run timeline into the Flyte task report. |
| `memory_key` | `str \| None` | Stable id (user/thread) for cross-run memory. When set, the session transcript is persisted and restored so a later run continues the conversation. |
| `app_name` | `str` | ADK app name (namespacing). |
| `user_id` | `str` | ADK user id. |

#### run_agent_sync()

```python
def run_agent_sync(
    input: str,
    agent: typing.Any,
    tools: typing.Sequence[typing.Any],
    model: str,
    instructions: str | None,
    name: str,
    max_llm_calls: int | None,
    durable: bool,
    observability: bool,
    memory_key: str | None,
    app_name: str,
    user_id: str,
) -> str
```
Synchronous variant of run_agent for use in sync tasks; runs the async implementation on a dedicated event loop.

Run a Google ADK agent with the given tools and prompt; return the final text.

    Await this from an async task as ``await run_agent(...)``; from a sync task
    use :func:`run_agent_sync` instead.

    Call this from inside an ``@env.task`` — that task is the durable parent, and each
    tool the agent calls runs as a durable Flyte child action. Provide either a
    pre-built ``agent`` (an ADK ``LlmAgent``/``BaseAgent``) or ``tools`` + ``model`` +
    ``instructions`` to have one built.

    Args:
        input: The user prompt.
        agent: A pre-built ADK agent. Mutually exclusive with ``tools``.
        tools: ``tool``-wrapped tools or bare ``@env.task`` templates.
        model: Model name for the built agent (e.g. ``gemini-2.0-flash``).
        instructions: System instruction for the built agent.
        name: Agent name (a valid Python identifier). ADK injects this into the system
            prompt as the model's "internal name", so it can surface in replies — keep it
            natural (defaults to ``"assistant"``; avoid a brand-y/internal label).
        max_llm_calls: Cap on model (LLM) calls before ADK raises
            ``LlmCallsLimitExceededError`` (its runaway-loop guard, via
            ``RunConfig.max_llm_calls``); ``None`` uses ADK's default of 500. Counts LLM
            calls, not conversational turns (a tool round is ~2 calls). For a wall-clock
            bound on the whole run, set ``timeout=`` on the enclosing ``@env.task``.
        durable: Wrap the model so each turn is recorded/replayed via ``flyte.trace``.
        observability: Render the run timeline into the Flyte task report.
        memory_key: Stable id (user/thread) for cross-run memory. When set, the session
            transcript is persisted and restored so a later run continues the conversation.
        app_name: ADK app name (namespacing).
        user_id: ADK user id.
    


| Parameter | Type | Description |
|-|-|-|
| `input` | `str` | |
| `agent` | `typing.Any` | |
| `tools` | `typing.Sequence[typing.Any]` | |
| `model` | `str` | |
| `instructions` | `str \| None` | |
| `name` | `str` | |
| `max_llm_calls` | `int \| None` | |
| `durable` | `bool` | |
| `observability` | `bool` | |
| `memory_key` | `str \| None` | |
| `app_name` | `str` | |
| `user_id` | `str` | |

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

