---
title: FlytePickle
version: 2.0.0b38
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlytePickle

**Package:** `flyte.types`

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
    python_val: typing.Any,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `python_val` | `typing.Any` | |

