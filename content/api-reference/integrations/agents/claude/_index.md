---
title: Claude Agent SDK
version: 2.6.2
variants: +flyte +union
layout: py_api
---

# Claude Agent SDK



Claude Agent SDK adapter for Flyte.

Bring your own `claude-agent-sdk` agent and run it durably on Flyte. Tools you
expose are Flyte tasks (so each tool call is a durable child action with its own
container/resources, retries and caching); the agent loop itself runs in the
Claude Code runtime, and its timeline is rendered into the Flyte task report.

- `flyteplugins.agents.claude.tool` — turn an `@env.task` into a Claude in-process MCP tool.
- `flyteplugins.agents.claude.run_agent` — run the agent loop inside your task and return the answer.

The `claude-agent-sdk` wheel bundles the native `claude` CLI (no separate Node.js
install needed); set an Anthropic API key in the environment.
## Directory

### Methods

| Method | Description |
|-|-|
| [`run_agent()`](#run_agent) | Run a Claude agent with the given tools and prompt; return the final text. |
| [`run_agent_sync()`](#run_agent_sync) | Synchronous variant of run_agent for use in sync tasks; runs the async implementation on a dedicated event loop. |
| [`tool()`](#tool) | Convert a Flyte task (or plain callable) into a Claude Agent SDK tool. |


## Methods

#### run_agent()

```python
def run_agent(
    input: str,
    tools: typing.Sequence[typing.Any] = (),
    model: str | None = 'claude-sonnet-4-5',
    instructions: str | None = None,
    max_turns: int | None = None,
    durable: bool = True,
    observability: bool = True,
    options: ClaudeAgentOptions | None = None,
    server_name: str = 'flyte_tools',
    memory_key: str | None = None,
) -> str
```
Run a Claude agent with the given tools and prompt; return the final text.

Await this from an async task as `await run_agent(...)`; from a sync task
use `flyteplugins.agents.claude.run_agent_sync` instead.

Call this from inside an `@env.task` — that task is the durable parent,
and each tool the agent calls runs as a durable Flyte child action. Pass a
fully-built `ClaudeAgentOptions` via `options` to keep SDK-native config
(subagents, permissions, hooks, session resume); `tools`/`model`/
`instructions`/`max_turns` are layered on top.

With `durable=True` (and a checkpoint-capable task context) the SDK's session
mirror + resume is wired onto a `flyte.Checkpoint`, so a retry resumes the
conversation instead of restarting it. With `observability=True` the run
timeline — assistant turns plus per-tool outcomes (via hooks) — is rendered into
the task report.

Set `memory_key` (a user/thread id) for cross-run memory: the transcript is
persisted to a durable, keyed `MemoryStore` and resumed on a later run with the
same key (this also covers crash-resume, so it takes precedence over the per-run
`durable` checkpoint).

The `claude-agent-sdk` wheel bundles the native `claude` CLI, so the runtime
image needs no separate Node.js install — just an Anthropic API key.


| Parameter | Type | Description |
|-|-|-|
| `input` | `str` | |
| `tools` | `typing.Sequence[typing.Any]` | |
| `model` | `str \| None` | |
| `instructions` | `str \| None` | |
| `max_turns` | `int \| None` | |
| `durable` | `bool` | |
| `observability` | `bool` | |
| `options` | `ClaudeAgentOptions \| None` | |
| `server_name` | `str` | |
| `memory_key` | `str \| None` | |

#### run_agent_sync()

```python
def run_agent_sync(
    input: str,
    tools: typing.Sequence[typing.Any] = (),
    model: str | None = 'claude-sonnet-4-5',
    instructions: str | None = None,
    max_turns: int | None = None,
    durable: bool = True,
    observability: bool = True,
    options: ClaudeAgentOptions | None = None,
    server_name: str = 'flyte_tools',
    memory_key: str | None = None,
) -> str
```
Synchronous variant of run_agent for use in sync tasks; runs the async implementation on a dedicated event loop.

Run a Claude agent with the given tools and prompt; return the final text.

    Await this from an async task as `await run_agent(...)`; from a sync task
    use `flyteplugins.agents.claude.run_agent_sync` instead.

    Call this from inside an `@env.task` — that task is the durable parent,
    and each tool the agent calls runs as a durable Flyte child action. Pass a
    fully-built `ClaudeAgentOptions` via `options` to keep SDK-native config
    (subagents, permissions, hooks, session resume); `tools`/`model`/
    `instructions`/`max_turns` are layered on top.

    With `durable=True` (and a checkpoint-capable task context) the SDK's session
    mirror + resume is wired onto a `flyte.Checkpoint`, so a retry resumes the
    conversation instead of restarting it. With `observability=True` the run
    timeline — assistant turns plus per-tool outcomes (via hooks) — is rendered into
    the task report.

    Set `memory_key` (a user/thread id) for cross-run memory: the transcript is
    persisted to a durable, keyed `MemoryStore` and resumed on a later run with the
    same key (this also covers crash-resume, so it takes precedence over the per-run
    `durable` checkpoint).

    The `claude-agent-sdk` wheel bundles the native `claude` CLI, so the runtime
    image needs no separate Node.js install — just an Anthropic API key.
    


| Parameter | Type | Description |
|-|-|-|
| `input` | `str` | |
| `tools` | `typing.Sequence[typing.Any]` | |
| `model` | `str \| None` | |
| `instructions` | `str \| None` | |
| `max_turns` | `int \| None` | |
| `durable` | `bool` | |
| `observability` | `bool` | |
| `options` | `ClaudeAgentOptions \| None` | |
| `server_name` | `str` | |
| `memory_key` | `str \| None` | |

#### tool()

```python
def tool(
    func: AsyncFunctionTaskTemplate | typing.Callable | None = None,
    name: str | None = None,
    description: str | None = None,
) -> SdkMcpTool | typing.Callable
```
Convert a Flyte task (or plain callable) into a Claude Agent SDK tool.

- For an `@env.task`: returns an `SdkMcpTool` whose handler runs the task
  as a durable Flyte child action when Claude calls it. The input schema is
  derived from the task via the Flyte type engine. The backing task is wired
  to `flyteplugins.agents.core.ToolTaskResolver` and exposed via
  `__wrapped_task__` so it resolves to itself on the worker (no recursion).
- For a plain (async) callable: returns an `SdkMcpTool` that runs it inline.

Usable bare, parametrized, or as a direct call:

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

