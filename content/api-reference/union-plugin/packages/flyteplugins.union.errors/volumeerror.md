---
title: VolumeError
version: 0.4.3
variants: +flyte +union
layout: py_api
---

# VolumeError

**Package:** `flyteplugins.union.errors`

Base for Volume *system* failures — infra/runtime problems the caller
didn't cause (mount client died, command failed, …). A ``flyte.errors``
*system* error.


## Parameters

```python
class VolumeError(
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

