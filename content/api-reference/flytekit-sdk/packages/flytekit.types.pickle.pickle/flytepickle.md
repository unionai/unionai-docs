---
title: FlytePickle
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlytePickle

**Package:** `flytekit.types.pickle.pickle`

This type is only used by flytekit internally. User should not use this type.
Any type that flyte can't recognize will become FlytePickle



## Methods

| Method | Description |
|-|-|
| [`from_pickle()`](#from_pickle) |  |
| [`python_type()`](#python_type) |  |
| [`to_pickle()`](#to_pickle) |  |


### from_pickle()

```python
def from_pickle(
    uri: str,
) -> typing.Any
```
| Parameter | Type | Description |
|-|-|-|
| `uri` | `str` | |

### python_type()

```python
def python_type()
```
### to_pickle()

```python
def to_pickle(
    ctx: flytekit.core.context_manager.FlyteContext,
    python_val: typing.Any,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `python_val` | `typing.Any` | |

