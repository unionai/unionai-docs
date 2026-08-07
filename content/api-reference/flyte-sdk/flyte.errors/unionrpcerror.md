---
title: UnionRpcError
version: 2.5.18
variants: +flyte +union
layout: py_api
---

# UnionRpcError

**Package:** `flyte.errors`

This error is raised when communication with the Union server fails.


## Parameters

```python
class UnionRpcError(
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

