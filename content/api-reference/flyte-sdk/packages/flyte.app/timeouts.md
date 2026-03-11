---
title: Timeouts
version: 2.0.6
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# Timeouts

**Package:** `flyte.app`

Timeout configuration for the application.

Attributes:
    request: Timeout for requests to the application. Can be an int
        (seconds) or timedelta. Must not exceed 1 hour.



```python
class Timeouts(
    request: int | datetime.timedelta | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `request` | `int \| datetime.timedelta \| None` | |

