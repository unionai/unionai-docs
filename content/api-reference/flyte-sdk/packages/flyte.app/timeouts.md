---
title: Timeouts
version: 2.1.2
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# Timeouts

**Package:** `flyte.app`

Timeout configuration for the application.



## Parameters

```python
class Timeouts(
    request: int | datetime.timedelta | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `request` | `int \| datetime.timedelta \| None` | Timeout for requests to the application. Can be an int (seconds) or timedelta. Must not exceed 1 hour. |

