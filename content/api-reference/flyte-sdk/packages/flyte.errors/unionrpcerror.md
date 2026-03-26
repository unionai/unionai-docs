---
title: UnionRpcError
version: 2.0.11
variants: +flyte +byoc +selfmanaged
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
    worker: str | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `code` | `str` | |
| `message` | `str` | |
| `worker` | `str \| None` | |

