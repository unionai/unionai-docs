---
title: InitializationError
version: 2.0.0b43
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# InitializationError

**Package:** `flyte.errors`

This error is raised when the Union system is tried to access without being initialized.


```python
class InitializationError(
    code: str,
    kind: typing.Literal['system', 'unknown', 'user'],
    root_cause_message: str,
    worker: str | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `code` | `str` | |
| `kind` | `typing.Literal['system', 'unknown', 'user']` | |
| `root_cause_message` | `str` | |
| `worker` | `str \| None` | |

