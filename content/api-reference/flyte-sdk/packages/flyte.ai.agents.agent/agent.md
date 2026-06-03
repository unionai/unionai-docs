---
title: Agent
version: 2.4.0
variants: +flyte +union
layout: py_api
---

# Agent

**Package:** `flyte.ai.agents.agent`

A flyte-native tool-use agent harness.

Parameters
----------
name:
    Stable agent identifier (used for logs and event payloads).
instructions:
    Base system prompt. Skills and a tool catalog summary are appended
    automatically.
model:
    Model identifier passed to ``call_llm``. Defaults to
    ``"claude-haiku-4-5"`` to match :class:`CodeModeAgent`.
tools:
    Sequence (or ``{name: tool}`` mapping) of tools the agent may call.
    Each entry can be a plain callable, a ``@flyte.trace`` helper, an
    ``@env.task`` :class:`~flyte.TaskTemplate`, a
    :class:`~flyte.remote._task.LazyEntity`, or a pre-built
    :class:`AgentTool`.
mcp_servers:
    Optional remote / stdio MCP servers whose tools should be loaded into
    the agent's tool registry on first use. See :class:`MCPServerSpec`.
skills:
    Extra context appended to the system prompt. Each entry is either a
    string or a :class:`pathlib.Path` pointing to a local text file.
max_turns:
    Maximum number of LLM ↔ tool turns before the loop gives up.
call_llm:
    Optional async callback ``(model, system, messages, tools) -&gt; LLMMessage``.
    Defaults to :func:`_default_call_llm` (uses litellm).
memory:
    Optional :class:`MemoryStore` initialized from a previous session.
    When provided, the existing transcript is prepended to every
    conversation and the in-flight transcript is appended to it on each
    call. Tools may also use the same instance for path-addressed
    artifact reads / writes (with audit + optional concurrency).
approval_callback:
    Optional async callback ``(tool, args) -&gt; bool`` invoked when a tool
    with ``requires_approval=True`` is about to run. Defaults to a HITL
    prompt via ``flyteplugins-hitl``.
parallel_tool_calls:
    When ``True`` (default) tool calls returned in a single assistant
    message are executed concurrently. Set to ``False`` to force strict
    sequential execution (useful when tool side-effects must be ordered).


## Parameters

```python
class Agent(
    name: str,
    instructions: str,
    model: str,
    tools: Sequence[Any] | Mapping[str, Any],
    mcp_servers: Sequence[MCPServerSpec],
    skills: Sequence[str | pathlib.Path],
    max_turns: int,
    call_llm: LLMCallable,
    memory: MemoryStore | None,
    approval_callback: ApprovalCallback,
    parallel_tool_calls: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `instructions` | `str` | |
| `model` | `str` | |
| `tools` | `Sequence[Any] \| Mapping[str, Any]` | |
| `mcp_servers` | `Sequence[MCPServerSpec]` | |
| `skills` | `Sequence[str \| pathlib.Path]` | |
| `max_turns` | `int` | |
| `call_llm` | `LLMCallable` | |
| `memory` | `MemoryStore \| None` | |
| `approval_callback` | `ApprovalCallback` | |
| `parallel_tool_calls` | `bool` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `system_prompt` | `str` | The fully-rendered system prompt, including skills + tool catalog. |

## Methods

| Method | Description |
|-|-|
| [`add_tool()`](#add_tool) | Register an additional tool after construction. |
| [`approval_callback()`](#approval_callback) | Default HITL approval: ask the user via ``flyteplugins-hitl``. |
| [`call_llm()`](#call_llm) | Default LLM callback that uses ``litellm. |
| [`run()`](#run) | Drive the LLM ↔ tool loop until the assistant returns a final reply. |
| [`tool_descriptions()`](#tool_descriptions) | Conform to :class:`~flyte. |


### add_tool()

```python
def add_tool(
    obj: Any,
    name: str | None,
) -> AgentTool
```
Register an additional tool after construction.

Useful when tools need access to runtime objects (e.g. an HTTP client
created inside a task).


| Parameter | Type | Description |
|-|-|-|
| `obj` | `Any` | |
| `name` | `str \| None` | |

### approval_callback()

```python
def approval_callback(
    tool: AgentTool,
    args: *args,
) -> bool
```
Default HITL approval: ask the user via ``flyteplugins-hitl``.

Returns ``True`` if the user approves the tool call. When the plugin is not
installed (or the agent is running outside a Flyte task context), this
falls back to denying the call so that the agent can recover by trying a
different approach.


| Parameter | Type | Description |
|-|-|-|
| `tool` | `AgentTool` | |
| `args` | `*args` | |

### call_llm()

```python
def call_llm(
    model: str,
    system: str,
    messages: list[dict[str, Any]],
    tools: list[dict[str, Any]] | None,
) -> LLMMessage
```
Default LLM callback that uses ``litellm.acompletion`` with tool calling.

Compatible with any provider that litellm supports (OpenAI, Anthropic,
Gemini, Bedrock, local OpenAI-compatible servers, …).


| Parameter | Type | Description |
|-|-|-|
| `model` | `str` | |
| `system` | `str` | |
| `messages` | `list[dict[str, Any]]` | |
| `tools` | `list[dict[str, Any]] \| None` | |

### run()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <Agent instance>.run.aio()`.
```python
def run(
    message: str,
    history: list[dict[str, Any]] | None,
) -> AgentResult
```
Drive the LLM ↔ tool loop until the assistant returns a final reply.

Implements the :class:`~flyte.ai.agents.protocol.AgentProtocol` so
instances can be plugged directly into
:class:`~flyte.ai.chat.AgentChatAppEnvironment`.

Call synchronously via ``run(...)``; in async contexts use ``run.aio(...)``.


| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `history` | `list[dict[str, Any]] \| None` | |

### tool_descriptions()

```python
def tool_descriptions()
```
Conform to :class:`~flyte.ai.agents.protocol.Agent`.

MCP tools loaded lazily are only listed after the first
:meth:`run` call.


