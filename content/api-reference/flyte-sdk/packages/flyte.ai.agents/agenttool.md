---
title: AgentTool
version: 2.5.2
variants: +flyte +union
layout: py_api
---

# AgentTool

**Package:** `flyte.ai.agents`

A normalized tool descriptor used by :class:`Agent`.

Most users do not construct :class:`AgentTool` directly — pass plain
callables, ``@flyte.trace`` helpers, or ``@env.task`` templates to
:class:`Agent` and they will be wrapped automatically. Build one
explicitly when you need to:

- rename a tool for the LLM,
- override the description shown to the model,
- require human approval before execution (HITL),
- inject a fully custom JSON schema,
- intercept invocation with a ``call_handler``.


## Parameters

```python
class AgentTool(
    name: str,
    description: str,
    parameters: dict[str, Any],
    execute: _ToolExecutor,
    requires_approval: bool,
    source: Literal['function', 'task', 'trace', 'remote_task', 'mcp', 'custom'],
    target: Any,
    call_handler: ToolCallHandler | None,
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

## Methods

| Method | Description |
|-|-|
| [`to_openai_format()`](#to_openai_format) | Convert to the OpenAI / litellm tools schema. |


### to_openai_format()

```python
def to_openai_format()
```
Convert to the OpenAI / litellm tools schema.


