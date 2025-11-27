---
title: flytekit.core.environment
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.environment

## Directory

### Classes

| Class | Description |
|-|-|
| [`Environment`](../flytekit.core.environment/environment) |  |

### Methods

| Method | Description |
|-|-|
| [`forge()`](#forge) |  |
| [`inherit()`](#inherit) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `P` | `ParamSpec` |  |
| `T` | `TypeVar` |  |

## Methods

#### forge()

```python
def forge(
    source: typing.Callable[typing.Concatenate[typing.Any, ~P], ~T],
) -> typing.Callable[[typing.Callable], typing.Callable[typing.Concatenate[typing.Any, ~P], ~T]]
```
| Parameter | Type | Description |
|-|-|-|
| `source` | `typing.Callable[typing.Concatenate[typing.Any, ~P], ~T]` | |

#### inherit()

```python
def inherit(
    old: dict[str, typing.Any],
    new: dict[str, typing.Any],
) -> dict[str, typing.Any]
```
| Parameter | Type | Description |
|-|-|-|
| `old` | `dict[str, typing.Any]` | |
| `new` | `dict[str, typing.Any]` | |

