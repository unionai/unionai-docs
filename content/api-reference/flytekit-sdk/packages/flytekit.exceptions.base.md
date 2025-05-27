---
title: flytekit.exceptions.base
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.exceptions.base

## Directory

### Errors

| Exception | Description |
|-|-|
| [`FlyteException`](.././flytekit.exceptions.base#flytekitexceptionsbaseflyteexception) | Common base class for all non-exit exceptions. |
| [`FlyteRecoverableException`](.././flytekit.exceptions.base#flytekitexceptionsbaseflyterecoverableexception) | Common base class for all non-exit exceptions. |

## flytekit.exceptions.base.FlyteException

Common base class for all non-exit exceptions.


```python
class FlyteException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.exceptions.base.FlyteRecoverableException

Common base class for all non-exit exceptions.


```python
class FlyteRecoverableException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

