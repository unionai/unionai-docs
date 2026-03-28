---
title: InitializationError
version: 2.0.12.dev22+g879ad6de4
variants: +flyte +union
layout: py_api
---

# InitializationError

**Package:** `flyte.errors`

This error is raised when the Union system is tried to access without being initialized.


## Parameters

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

