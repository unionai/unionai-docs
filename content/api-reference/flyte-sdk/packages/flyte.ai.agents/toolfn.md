---
title: ToolFn
version: 2.5.9
variants: +flyte +union
layout: py_api
---

# ToolFn

**Package:** `flyte.ai.agents`

The tool under invocation, handed to a :data:`ToolCallHandler`.

Awaiting the instance runs the tool's *default* behavior::

    result = await tool_fn(**kwargs)

The attributes give a custom handler everything it needs to change that
behavior without re-deriving it. The most useful are:

- :attr:`target` — the underlying ``@env.task`` template, plain callable, or
  ``LazyEntity`` (``None`` for custom / MCP tools). Reach into it to, e.g.,
  ``tool_fn.target.override(resources=...).aio(**kwargs)``.
- :attr:`model` — the owning agent's model id, to pass to ``call_llm`` when
  the handler wants to consult the LLM.
- :attr:`name` / :attr:`description` / :attr:`parameters` — the tool's
  LLM-facing metadata.


## Parameters

```python
class ToolFn(
    name: str,
    description: str,
    parameters: dict[str, Any],
    model: str,
    target: Any,
    source: str,
    _execute: _ToolExecutor,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `description` | `str` | |
| `parameters` | `dict[str, Any]` | |
| `model` | `str` | |
| `target` | `Any` | |
| `source` | `str` | |
| `_execute` | `_ToolExecutor` | |

