---
title: FlytePickle
description: "This type is only used by Flyte internally."
icon: braces
version: 2.11.0
variants: +flyte +union
layout: py_api
---

# FlytePickle

**Package:** `flyte.types`

This type is only used by Flyte internally. Users should not use this type.
Any type that Flyte can't recognize becomes `FlytePickle`.


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

