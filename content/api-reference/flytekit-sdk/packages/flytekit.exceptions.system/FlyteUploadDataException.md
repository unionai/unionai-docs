---
title: FlyteUploadDataException
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteUploadDataException

**Package:** `flytekit.exceptions.system`

Common base class for all non-exit exceptions.


```python
class FlyteUploadDataException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `timestamp` | `typing.Optional[float]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

