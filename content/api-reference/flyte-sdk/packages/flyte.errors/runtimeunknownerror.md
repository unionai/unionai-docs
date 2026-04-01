---
title: RuntimeUnknownError
version: 2.1.2.dev2+g62f55b516
variants: +flyte +union
layout: py_api
---

# RuntimeUnknownError

**Package:** `flyte.errors`

This error is raised when the underlying task execution fails because of an unknown error.


## Parameters

```python
class RuntimeUnknownError(
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

