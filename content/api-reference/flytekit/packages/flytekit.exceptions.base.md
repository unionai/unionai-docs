---
title: flytekit.exceptions.base
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.exceptions.base

## Directory

### Classes

No classes in this package.

### Errors

* [`FlyteException`](.././flytekit.exceptions.base#flytekitexceptionsbaseflyteexception)
* [`FlyteRecoverableException`](.././flytekit.exceptions.base#flytekitexceptionsbaseflyterecoverableexception)

## flytekit.exceptions.base.FlyteException

Common base class for all non-exit exceptions.


```python
def FlyteException(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.exceptions.base.FlyteRecoverableException

Common base class for all non-exit exceptions.


```python
def FlyteRecoverableException(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

