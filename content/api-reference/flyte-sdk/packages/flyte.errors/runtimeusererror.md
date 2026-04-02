---
title: RuntimeUserError
version: 2.1.2
variants: +flyte +union
layout: py_api
---

# RuntimeUserError

**Package:** `flyte.errors`

This error is raised when the underlying task execution fails because of an error in the user's code.


## Parameters

```python
class RuntimeUserError(
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

