---
title: FlyteUserException
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteUserException

**Package:** `flytekit.exceptions.user`

Common base class for all non-exit exceptions.


```python
class FlyteUserException(
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

