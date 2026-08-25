---
title: flyte.ai.agents
version: 2.6.5
variants: +flyte +union
layout: py_api
---

# flyte.ai.agents

flyte.ai.agents — Agent abstractions for Flyte apps.
## Directory

### Classes

| Class | Description |
|-|-|
| [`Agent`](../flyte.ai.agents/agent) | A flyte-native tool-use agent harness. |
| [`AgentEvent`](../flyte.ai.agents/agentevent) | Lightweight event emitted by the agent loop. |
| [`AgentResult`](../flyte.ai.agents/agentresult) | Outcome of a single agent invocation. |
| [`AgentTool`](../flyte.ai.agents/agenttool) | A normalized tool descriptor used by `flyte.ai.agents.Agent`. |
| [`LLMMessage`](../flyte.ai.agents/llmmessage) | Provider-agnostic shape returned by `flyte.ai.agents.LLMCallable`. |
| [`MCPServerSpec`](../flyte.ai.agents/mcpserverspec) | Declarative spec for a remote MCP server that exposes tools. |
| [`MemoryMeta`](../flyte.ai.agents/memorymeta) | Per-file metadata sidecar (sha256, actor, timestamp, …) for a memory entry. |
| [`MemoryStore`](../flyte.ai.agents/memorystore) | Conversation transcript + path-addressed artifact memory backed by `flyte.io.Dir`. |
| [`ToolFn`](../flyte.ai.agents/toolfn) | The tool under invocation, handed to a `flyte.ai.agents.ToolCallHandler`. |

### Protocols

| Protocol | Description |
|-|-|
| [`AgentProtocol`](../flyte.ai.agents/agentprotocol) | Minimal protocol that any agent must satisfy to work with. |

### Errors

| Exception | Description |
|-|-|
| [`AccessDenied`](../flyte.ai.agents/accessdenied) | Raised when a write targets a read-only or reserved prefix. |
| [`ConcurrencyError`](../flyte.ai.agents/concurrencyerror) | Raised when an `expected_sha` precondition does not match the current state. |
| [`MemoryStoreError`](../flyte.ai.agents/memorystoreerror) | Base class for `flyte.ai.agents.MemoryStore` errors. |

### Methods

| Method | Description |
|-|-|
| [`tool()`](#tool) | Wrap a task, `@flyte.trace` helper, plain callable, or `LazyEntity` as a `flyte.ai.agents.AgentTool`. |


### Variables

| Property | Type | Description |
|-|-|-|
| `agent_progress_cb` | `ContextVar` |  |

## Methods

#### tool()

```python
def tool(
    obj: Any = None,
    name: str | None = None,
    description: str | None = None,
    requires_approval: bool = False,
    call_handler: ToolCallHandler | None = None,
) -> AgentTool | Callable[[Any], AgentTool]
```
Wrap a task, `@flyte.trace` helper, plain callable, or `LazyEntity` as a `flyte.ai.agents.AgentTool`.

This removes the boilerplate of building a `flyte.ai.agents.AgentTool` by hand
(manually pulling the docstring, JSON schema, and writing a dict-args
execution bridge) when you only need to tweak how a tool is presented to
the model or gate it behind human approval.

Use it as a direct call:

```python
refund_tool = tool(issue_refund, requires_approval=True)
```

or as a (parametrized) decorator stacked on top of `@env.task` /
`@flyte.trace` / a plain function:

```python
@tool(requires_approval=True)
@env.task
async def issue_refund(order_id: str, amount_usd: float) -> dict: ...

@tool
def search(query: str) -> str: ...
```

The wrapped task is still registered with its `flyte.TaskEnvironment`
and executes on-cluster via `task.aio` when the agent calls it.

Pass `call_handler` to intercept *how* the tool is invoked. The handler is
an async callback `(call_llm, tool_fn, **kwargs) -> result` that runs in
place of the default execution. `tool_fn` is a `flyte.ai.agents.ToolFn`: await it to
run the default behavior, or use `tool_fn.target` (the underlying task /
callable) and `call_llm` to do something custom — e.g. ask the LLM how to
size compute, then run the task with overridden resources and retry on OOM:

```python
async def right_size(call_llm, tool_fn, **kwargs):
    resources = await _ask_llm_for_resources(call_llm, tool_fn, kwargs)
    return await tool_fn.target.override(resources=resources).aio(**kwargs)

@tool(call_handler=right_size)
@env.task
async def train(...): ...
```



| Parameter | Type | Description |
|-|-|-|
| `obj` | `Any` | The object to wrap. Omit when using `tool` as a parametrized decorator (`@tool(...)`). |
| `name` | `str \| None` | Override the tool name shown to the model. Defaults to the function / task name. |
| `description` | `str \| None` | Override the description shown to the model. Defaults to the first paragraph of the object's docstring. |
| `requires_approval` | `bool` | Gate execution behind the agent's HITL approval callback. |
| `call_handler` | `ToolCallHandler \| None` | Optional async interceptor `(call_llm, tool_fn, **kwargs)` that customizes how the tool is invoked. See `flyte.ai.agents.ToolCallHandler` and `flyte.ai.agents.ToolFn`. |

**Returns:** An `flyte.ai.agents.AgentTool` (direct call) or a decorator returning one.

