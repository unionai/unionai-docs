---
title: RuntimeSystemError
version: 2.1.10.dev6+ga8f3f9bfa
variants: +flyte +union
layout: py_api
---

# RuntimeSystemError

**Package:** `flyte.errors`

This error is raised when the underlying task execution fails because of a system error. This could be a bug in the
Union system or a bug in the user's code.


## Parameters

```python
class RuntimeSystemError(
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

