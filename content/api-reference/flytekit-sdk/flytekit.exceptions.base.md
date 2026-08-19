---
title: flytekit.exceptions.base
version: 1.16.28
variants: +flyte +union
layout: py_api
---

# flytekit.exceptions.base

## Directory

### Errors

| Exception | Description |
|-|-|
| [`FlyteException`](.././flytekit.exceptions.base#flytekitexceptionsbaseflyteexception) |  |
| [`FlyteRecoverableException`](.././flytekit.exceptions.base#flytekitexceptionsbaseflyterecoverableexception) |  |

## flytekit.exceptions.base.FlyteException

### Parameters

```python
class FlyteException(
    *args,
    timestamp: typing.Optional[float] = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `*args` |  | |
| `timestamp` | `typing.Optional[float]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `typing.Optional[float]` | The timestamp as fractional seconds since epoch |

## flytekit.exceptions.base.FlyteRecoverableException

### Parameters

```python
class FlyteRecoverableException(
    *args,
    timestamp: typing.Optional[float] = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `*args` |  | |
| `timestamp` | `typing.Optional[float]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` | `typing.Optional[float]` | The timestamp as fractional seconds since epoch |

