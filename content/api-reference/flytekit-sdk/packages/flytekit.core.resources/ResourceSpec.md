---
title: ResourceSpec
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ResourceSpec

**Package:** `flytekit.core.resources`

```python
class ResourceSpec(
    requests: flytekit.core.resources.Resources,
    limits: flytekit.core.resources.Resources,
)
```
| Parameter | Type | Description |
|-|-|-|
| `requests` | `flytekit.core.resources.Resources` | |
| `limits` | `flytekit.core.resources.Resources` | |

## Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`from_multiple_resource()`](#from_multiple_resource) | Convert Resources that represent both a requests and limits into a ResourceSpec. |
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

### from_multiple_resource()

```python
def from_multiple_resource(
    resource: flytekit.core.resources.Resources,
) -> ResourceSpec
```
Convert Resources that represent both a requests and limits into a ResourceSpec.


| Parameter | Type | Description |
|-|-|-|
| `resource` | `flytekit.core.resources.Resources` | |

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

