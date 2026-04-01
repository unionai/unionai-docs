---
title: UnionRpcError
version: 2.1.2.dev2+g62f55b516
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
    worker: str | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `code` | `str` | |
| `message` | `str` | |
| `worker` | `str \| None` | |

