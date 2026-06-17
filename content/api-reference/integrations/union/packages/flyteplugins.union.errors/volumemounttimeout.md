---
title: VolumeMountTimeout
version: 0.4.2
variants: +flyte +union
layout: py_api
---

# VolumeMountTimeout

**Package:** `flyteplugins.union.errors`

The mount did not become a FUSE mountpoint within the timeout. A kind of
:class:`VolumeMountError`, so ``except VolumeMountError`` catches it too.


## Parameters

```python
class VolumeMountTimeout(
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

