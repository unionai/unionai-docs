---
title: RetriesExhaustedError
version: 2.0.0b34.dev10+g162555e05
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# RetriesExhaustedError

**Package:** `flyte.errors`

This error is raised when the underlying task execution fails after all retries have been exhausted.


```python
class RetriesExhaustedError(
    code: str,
    message: str,
    worker: str | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `code` | `str` | |
| `message` | `str` | |
| `worker` | `str \| None` | |

