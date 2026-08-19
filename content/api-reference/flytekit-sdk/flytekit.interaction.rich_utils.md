---
title: flytekit.interaction.rich_utils
version: 1.16.28
variants: +flyte +union
layout: py_api
---

# flytekit.interaction.rich_utils

## Directory

### Classes

| Class | Description |
|-|-|
| [`RichCallback`](.././flytekit.interaction.rich_utils#flytekitinteractionrich_utilsrichcallback) |  |

## flytekit.interaction.rich_utils.RichCallback

### Parameters

```python
class RichCallback(
    rich_kwargs: typing.Optional[typing.Dict] = None,
    **kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `rich_kwargs` | `typing.Optional[typing.Dict]` | |
| `**kwargs` |  | |

### Methods

| Method | Description |
|-|-|
| [`relative_update()`](#relative_update) | Delta increment the internal counter. |
| [`set_size()`](#set_size) | Set the internal maximum size attribute. |


#### relative_update()

```python
def relative_update(
    inc = 1,
)
```
Delta increment the internal counter

Triggers ``call()``

Parameters
----------
inc: int


| Parameter | Type | Description |
|-|-|-|
| `inc` |  | |

#### set_size()

```python
def set_size(
    size,
)
```
Set the internal maximum size attribute

Usually called if not initially set at instantiation. Note that this
triggers a ``call()``.

Parameters
----------
size: int


| Parameter | Type | Description |
|-|-|-|
| `size` |  | |

