---
title: OOMError
version: 2.1.10.dev6+ga8f3f9bfa
variants: +flyte +union
layout: py_api
---

# OOMError

**Package:** `flyte.errors`

This error is raised when the underlying task execution fails because of an out-of-memory error.


## Parameters

```python
class OOMError(
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

