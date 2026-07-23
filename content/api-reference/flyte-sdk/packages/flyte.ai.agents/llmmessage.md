---
title: LLMMessage
version: 2.5.14
variants: +flyte +union
layout: py_api
---

# LLMMessage

**Package:** `flyte.ai.agents`

Provider-agnostic shape returned by :data:`LLMCallable`.

``tool_calls`` follows the OpenAI tool-calling convention; provider-specific
callers should normalize to this shape.


## Parameters

```python
class LLMMessage(
    content: str | None,
    tool_calls: list[dict[str, Any]],
    raw: Any,
)
```
| Parameter | Type | Description |
|-|-|-|
| `content` | `str \| None` | |
| `tool_calls` | `list[dict[str, Any]]` | |
| `raw` | `Any` | |

