---
title: FlyteUserRuntimeException
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteUserRuntimeException

**Package:** `flytekit.exceptions.user`

Common base class for all non-exit exceptions.


```python
class FlyteUserRuntimeException(
    exc_value: Exception,
    timestamp: typing.Optional[float],
)
```
FlyteUserRuntimeException is thrown when a user code raises an exception.



| Parameter | Type | Description |
|-|-|-|
| `exc_value` | `Exception` | The exception that was raised from user code. |
| `timestamp` | `typing.Optional[float]` | The timestamp as fractional seconds since epoch when the exception was raised. |

## Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |
| `value` |  |  |

