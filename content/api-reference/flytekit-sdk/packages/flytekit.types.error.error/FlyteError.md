---
title: FlyteError
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteError

**Package:** `flytekit.types.error.error`

Special Task type that will be used in the failure node. Propeller will pass this error to failure task, so users
have to add an input with this type to the failure task.


```python
class FlyteError(
    message: str,
    failed_node_id: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `failed_node_id` | `str` | |

## Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


### from_dict()

```python
def from_dict(
    d,
    dialect,
)
```
| Parameter | Type | Description |
|-|-|-|
| `d` |  | |
| `dialect` |  | |

### from_json()

```python
def from_json(
    data: typing.Union[str, bytes, bytearray],
    decoder: collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]],
    from_dict_kwargs: typing.Any,
) -> ~T
```
| Parameter | Type | Description |
|-|-|-|
| `data` | `typing.Union[str, bytes, bytearray]` | |
| `decoder` | `collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]]` | |
| `from_dict_kwargs` | `typing.Any` | |

### to_dict()

```python
def to_dict()
```
### to_json()

```python
def to_json(
    encoder: collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]],
    to_dict_kwargs: typing.Any,
) -> typing.Union[str, bytes, bytearray]
```
| Parameter | Type | Description |
|-|-|-|
| `encoder` | `collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]]` | |
| `to_dict_kwargs` | `typing.Any` | |

