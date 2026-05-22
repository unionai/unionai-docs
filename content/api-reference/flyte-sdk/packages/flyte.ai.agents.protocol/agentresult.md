---
title: AgentResult
version: 2.3.4
variants: +flyte +union
layout: py_api
---

# AgentResult

**Package:** `flyte.ai.agents.protocol`

Outcome of a single agent invocation.


## Parameters

```python
class AgentResult(
    code: str,
    charts: list[str],
    summary: str,
    error: str,
    attempts: int,
)
```
| Parameter | Type | Description |
|-|-|-|
| `code` | `str` | |
| `charts` | `list[str]` | |
| `summary` | `str` | |
| `error` | `str` | |
| `attempts` | `int` | |

