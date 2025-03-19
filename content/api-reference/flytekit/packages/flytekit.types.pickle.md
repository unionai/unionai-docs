---
title: flytekit.types.pickle
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.types.pickle


Flytekit Pickle Type
==========================================================
.. currentmodule:: flytekit.types.pickle

.. autosummary::
   :template: custom.rst
   :toctree: generated/

   FlytePickle

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlytePickle`](.././flytekit.types.pickle#flytekittypespickleflytepickle) | This type is only used by flytekit internally. |

## flytekit.types.pickle.FlytePickle

This type is only used by flytekit internally. User should not use this type.
Any type that flyte can't recognize will become FlytePickle


### Methods

| Method | Description |
|-|-|
| [`from_pickle()`](#from_pickle) | None |
| [`python_type()`](#python_type) | None |
| [`to_pickle()`](#to_pickle) | None |


#### from_pickle()

```python
def from_pickle(
    uri: str,
):
```
| Parameter | Type |
|-|-|
| `uri` | `str` |

#### python_type()

```python
def python_type()
```
#### to_pickle()

```python
def to_pickle(
    ctx: flytekit.core.context_manager.FlyteContext,
    python_val: typing.Any,
):
```
| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `python_val` | `typing.Any` |

