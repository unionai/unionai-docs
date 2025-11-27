---
title: FlyteNonRecoverableSystemException
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteNonRecoverableSystemException

**Package:** `flytekit.exceptions.system`

Common base class for all non-exit exceptions.


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
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |
| `value` |  |  |

