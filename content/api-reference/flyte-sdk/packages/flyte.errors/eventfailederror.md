---
title: EventFailedError
version: 2.4.4
variants: +flyte +union
layout: py_api
---

# EventFailedError

**Package:** `flyte.errors`

This error is raised when a condition event fails during execution.

This can happen when the backend encounters an error while processing the condition,
or when the event is explicitly marked as failed by the system.


## Parameters

```python
class EventFailedError(
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

