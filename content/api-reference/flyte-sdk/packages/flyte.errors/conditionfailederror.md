---
title: ConditionFailedError
version: 2.5.14
variants: +flyte +union
layout: py_api
---

# ConditionFailedError

**Package:** `flyte.errors`

This error is raised when a condition fails during execution.

This can happen when the backend encounters an error while processing the condition,
or when the condition is explicitly marked as failed by the system.


## Parameters

```python
class ConditionFailedError(
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

