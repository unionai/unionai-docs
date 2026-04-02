---
title: BaseRuntimeError
version: 2.1.2
variants: +flyte +union
layout: py_api
---

# BaseRuntimeError

**Package:** `flyte.errors`

Base class for all Union runtime errors. These errors are raised when the underlying task execution fails, either
because of a user error, system error or an unknown error.


## Parameters

```python
class BaseRuntimeError(
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

