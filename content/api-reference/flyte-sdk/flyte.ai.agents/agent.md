---
title: Agent
version: 2.5.19
variants: +flyte +union
layout: py_api
---

# Agent

**Package:** `flyte.ai.agents`

A flyte-native tool-use agent harness.



## Parameters

```python
class Agent(
    name: str = 'flyte-agent',
    instructions: str = 'You are a helpful assistant.',
    model: str = 'claude-haiku-4-5',
    tools: Sequence[Any] | Mapping[str, Any] = <factory>,
    mcp_servers: Sequence[MCPServerSpec] = <factory>,
    skills: Sequence[str | pathlib.Path] = <factory>,
    max_turns: int = 25,
    call_llm: LLMCallable = _default_call_llm,
    approval_callback: ApprovalCallback = _condition_approval,
    parallel_tool_calls: bool = True,
    code_mode: bool = False,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Stable agent identifier (used for logs and event payloads). |
| `instructions` | `str` | Base system prompt. Skills and a tool catalog summary are appended automatically. |
| `model` | `str` | Model identifier passed to `call_llm`. Defaults to `"claude-haiku-4-5"`. |
| `tools` | `Sequence[Any] \| Mapping[str, Any]` | Sequence (or `{name: tool}` mapping) of tools the agent may call. Each entry can be a plain callable, a `@flyte.trace` helper, an `@env.task` `flyte.TaskTemplate`, a `flyte.remote._task.LazyEntity`, or a pre-built `flyte.ai.agents.AgentTool`. |
| `mcp_servers` | `Sequence[MCPServerSpec]` | Optional remote / stdio MCP servers whose tools should be loaded into the agent's tool registry on first use. See `flyte.ai.agents.MCPServerSpec`. |
| `skills` | `Sequence[str \| pathlib.Path]` | Extra context appended to the system prompt. Each entry is either a string or a `pathlib.Path` pointing to a local text file. |
| `max_turns` | `int` | Maximum number of LLM ↔ tool turns before the loop gives up. |
| `call_llm` | `LLMCallable` | Optional async callback `(model, system, messages, tools) -> LLMMessage`. Defaults to `_default_call_llm` (uses litellm). |
| `approval_callback` | `ApprovalCallback` | Optional async callback `(tool, args) -> bool` invoked when a tool with `requires_approval=True` is about to run. Defaults to a HITL prompt via a flyte-native condition (`flyte.new_condition`). |
| `parallel_tool_calls` | `bool` | When `True` (default) tool calls returned in a single assistant message are executed concurrently. Set to `False` to force strict sequential execution (useful when tool side-effects must be ordered). Ignored in code mode. |
| `code_mode` | `bool` | When `True` the agent runs in *code mode*: instead of emitting JSON tool calls, the LLM writes a small Python program each turn that is executed in the Monty sandbox (`flyte.sandbox.orchestrate_local`) with the tools exposed as plain functions. The value of the program's last expression becomes the observation for the next turn; the loop ends when the LLM replies with plain text (no code block). This unlocks generated control flow (loops, `flyte_map` fan-out, intermediate aggregation) while still dispatching `@env.task` tools durably on-cluster. Tools with a `call_handler` run through that handler in code mode as well. Requires `pydantic-monty` in the runtime image. Note: per-tool HITL approval is not enforced in code mode, since tools are invoked from inside the sandbox rather than as discrete approved calls. |

## Properties

| Property | Type | Description |
|-|-|-|
| `system_prompt` | `str` | The fully-rendered system prompt, including skills + tool catalog. |

## Methods

| Method | Description |
|-|-|
| [`add_tool()`](#add_tool) | Register an additional tool after construction. |
| [`approval_callback()`](#approval_callback) | Default HITL approval: pause the run on a flyte-native condition. |
| [`call_llm()`](#call_llm) | Default LLM callback that uses `litellm.acompletion` with tool calling. |
| [`run()`](#run) | Drive the LLM ↔ tool loop until the assistant returns a final reply. |
| [`tool_descriptions()`](#tool_descriptions) | Conform to `flyte.ai.agents.protocol.Agent`. |


### add_tool()

```python
def add_tool(
    obj: Any,
    name: str | None = None,
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
    args: dict[str, Any],
) -> bool
```
Default HITL approval: pause the run on a flyte-native condition.

Registers a condition via `flyte.new_condition` and blocks until a
human signals it — from the UI, `flyte signal condition`, or
`flyte.remote.Condition.signal`. Returns `True` if the user approves
the tool call. When the agent is running outside a Flyte task context
there is no backend to signal the condition, so this falls back to denying
the call so that the agent can recover by trying a different approach.


| Parameter | Type | Description |
|-|-|-|
| `tool` | `AgentTool` | |
| `args` | `dict[str, Any]` | |

### call_llm()

```python
def call_llm(
    model: str,
    system: str,
    messages: list[dict[str, Any]],
    tools: list[dict[str, Any]] | None,
) -> LLMMessage
```
Default LLM callback that uses `litellm.acompletion` with tool calling.

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
    memory: list[dict[str, Any]] | MemoryStore | None = None,
) -> AgentResult
```
Drive the LLM ↔ tool loop until the assistant returns a final reply.

Implements the `flyte.ai.agents.protocol.AgentProtocol` so
instances can be plugged directly into
`flyte.ai.chat.AgentChatAppEnvironment`.

The agent is decoupled from any persistent state: memory is passed in
per call rather than attached to the agent. `memory` may be:

- `None`: a stateless, single-shot conversation.
- a `list[dict]`: prior messages to prepend (e.g. a chat `history`).
  The returned `flyte.ai.agents.AgentResult` carries no memory in this case.
- a `flyte.ai.agents.MemoryStore`: its transcript is prepended, the in-flight
  transcript is appended back to it, and it is returned on
  `AgentResult.memory`. Persistence is the caller's
  responsibility: call `memory.save()` (or `.save.aio()`) after
  `run` to write the updated transcript back to its keyed remote path.

Call synchronously via `run(...)`; in async contexts use `run.aio(...)`.


| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `memory` | `list[dict[str, Any]] \| MemoryStore \| None` | |

### tool_descriptions()

```python
def tool_descriptions()
```
Conform to `flyte.ai.agents.protocol.Agent`.

MCP tools loaded lazily are only listed after the first
`Agent.run` call.


