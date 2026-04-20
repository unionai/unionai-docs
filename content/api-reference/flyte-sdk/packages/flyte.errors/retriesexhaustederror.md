---
title: RetriesExhaustedError
<<<<<<< HEAD
version: 2.0.11
variants: +flyte +byoc +selfmanaged
=======
version: 2.1.7
variants: +flyte +union
>>>>>>> origin/main
layout: py_api
---

# RetriesExhaustedError

**Package:** `flyte.errors`

This error is raised when the underlying task execution fails after all retries have been exhausted.


## Parameters

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

