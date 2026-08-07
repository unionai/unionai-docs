---
title: AgentTool
version: 2.5.19
variants: +flyte +union
layout: py_api
---

# AgentTool

**Package:** `flyte.ai.agents`

A normalized tool descriptor used by `flyte.ai.agents.Agent`.

Most users do not construct `flyte.ai.agents.AgentTool` directly — pass plain
callables, `@flyte.trace` helpers, or `@env.task` templates to
`flyte.ai.agents.Agent` and they will be wrapped automatically. Build one
explicitly when you need to:

- rename a tool for the LLM,
- override the description shown to the model,
- require human approval before execution (HITL),
- inject a fully custom JSON schema,
- intercept invocation with a `call_handler`.


## Parameters

```python
class AgentTool(
    name: str,
    description: str,
    parameters: dict[str, Any],
    execute: _ToolExecutor,
    requires_approval: bool = False,
    source: Literal['function', 'task', 'trace', 'remote_task', 'mcp', 'custom'] = 'function',
    target: Any = None,
    call_handler: ToolCallHandler | None = None,
    call_llm: LLMCallable | None = None,
    model: str | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `description` | `str` | |
| `parameters` | `dict[str, Any]` | |
| `execute` | `_ToolExecutor` | |
| `requires_approval` | `bool` | |
| `source` | `Literal['function', 'task', 'trace', 'remote_task', 'mcp', 'custom']` | |
| `target` | `Any` | |
| `call_handler` | `ToolCallHandler \| None` | |
| `call_llm` | `LLMCallable \| None` | |
| `model` | `str \| None` | |

## Methods

| Method | Description |
|-|-|
| [`aio()`](#aio) | Invoke the tool, routing through `call_handler` when one is registered. |
| [`to_openai_format()`](#to_openai_format) | Convert to the OpenAI / litellm tools schema. |


### aio()

```python
def aio(
    *args: Any,
    **kwargs: Any,
) -> Any
```
Invoke the tool, routing through `call_handler` when one is registered.

Mirrors `flyte._task.TaskTemplate.aio` enough for `flyte.map` and
in-task calls on `@tool`-wrapped tasks. When a `call_handler` is set,
it runs with `AgentTool.call_llm` and `AgentTool.model` (or their defaults).
Otherwise, durable `@env.task` / remote-task targets delegate to their
underlying `.aio`; everything else goes through `AgentTool.execute`.


| Parameter | Type | Description |
|-|-|-|
| `*args` | `Any` | |
| `**kwargs` | `Any` | |

### to_openai_format()

```python
def to_openai_format()
```
Convert to the OpenAI / litellm tools schema.


