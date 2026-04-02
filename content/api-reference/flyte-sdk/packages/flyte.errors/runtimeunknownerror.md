---
title: RuntimeUnknownError
version: 2.1.3.dev1+ge23e739d5
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

