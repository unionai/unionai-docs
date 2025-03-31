---
title: flytekit.types.error
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.types.error


Flytekit Error Type
==========================================================
.. currentmodule:: flytekit.types.error

.. autosummary::
   :nosignatures:
   :template: custom.rst
   :toctree: generated/

   FlyteError

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteError`](.././flytekit.types.error#flytekittypeserrorflyteerror) | Special Task type that will be used in the failure node. |

## flytekit.types.error.FlyteError

Special Task type that will be used in the failure node. Propeller will pass this error to failure task, so users
have to add an input with this type to the failure task.


```python
def FlyteError(
    message: str,
    failed_node_id: str,
):
```
| Parameter | Type |
|-|-|
| `message` | `str` |
| `failed_node_id` | `str` |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) | None |
| [`from_json()`](#from_json) | None |
| [`to_dict()`](#to_dict) | None |
| [`to_json()`](#to_json) | None |


#### from_dict()

```python
def from_dict(
    d,
    dialect,
):
```
| Parameter | Type |
|-|-|
| `d` |  |
| `dialect` |  |

#### from_json()

```python
def from_json(
    data: typing.Union[str, bytes, bytearray],
    decoder: collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]],
    from_dict_kwargs: typing.Any,
):
```
| Parameter | Type |
|-|-|
| `data` | `typing.Union[str, bytes, bytearray]` |
| `decoder` | `collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]]` |
| `from_dict_kwargs` | `typing.Any` |

#### to_dict()

```python
def to_dict()
```
#### to_json()

```python
def to_json(
    encoder: collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]],
    to_dict_kwargs: typing.Any,
):
```
| Parameter | Type |
|-|-|
| `encoder` | `collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]]` |
| `to_dict_kwargs` | `typing.Any` |

