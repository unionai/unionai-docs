---
title: AgentResult
version: 2.5.2
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
    memory: 'MemoryStore | None',
)
```
| Parameter | Type | Description |
|-|-|-|
| `code` | `str` | |
| `charts` | `list[str]` | |
| `summary` | `str` | |
| `error` | `str` | |
| `attempts` | `int` | |
| `memory` | `'MemoryStore \| None'` | |

