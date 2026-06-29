---
title: AgentTool
version: 2.5.6
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
    call_llm: LLMCallable | None,
    model: str | None,
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
| [`aio()`](#aio) | Invoke the tool, routing through ``call_handler`` when one is registered. |
| [`to_openai_format()`](#to_openai_format) | Convert to the OpenAI / litellm tools schema. |


### aio()

```python
def aio(
    args: *args,
    kwargs: **kwargs,
) -> Any
```
Invoke the tool, routing through ``call_handler`` when one is registered.

Mirrors :meth:`~flyte._task.TaskTemplate.aio` enough for ``flyte.map`` and
in-task calls on ``@tool``-wrapped tasks. When a ``call_handler`` is set,
it runs with :attr:`call_llm` and :attr:`model` (or their defaults).
Otherwise, durable ``@env.task`` / remote-task targets delegate to their
underlying ``.aio``; everything else goes through :meth:`execute`.


| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### to_openai_format()

```python
def to_openai_format()
```
Convert to the OpenAI / litellm tools schema.


