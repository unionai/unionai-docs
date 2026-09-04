---
title: OOMError
description: "This error is raised when the underlying task execution fails because of an out-of-memory error."
icon: exclamation-triangle
version: 2.7.1
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
    worker: str | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `code` | `str` | |
| `message` | `str` | |
| `worker` | `str \| None` | |

