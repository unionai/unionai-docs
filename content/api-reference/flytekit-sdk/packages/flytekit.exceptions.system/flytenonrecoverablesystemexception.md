---
title: FlyteNonRecoverableSystemException
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteNonRecoverableSystemException

**Package:** `flytekit.exceptions.system`

```python
class FlyteNonRecoverableSystemException(
    exc_value: Exception,
)
```
FlyteNonRecoverableSystemException is thrown when a system code raises an exception.



| Parameter | Type | Description |
|-|-|-|
| `exc_value` | `Exception` | The exception that was raised from system code. |

## Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `None` | The timestamp as fractional seconds since epoch |
| `value` | `None` |  |

