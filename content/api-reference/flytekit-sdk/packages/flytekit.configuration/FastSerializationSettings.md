---
title: FastSerializationSettings
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FastSerializationSettings

**Package:** `flytekit.configuration`

This object hold information about settings necessary to serialize an object so that it can be fast-registered.


```python
class FastSerializationSettings(
    enabled: bool,
    destination_dir: Optional[str],
    distribution_location: Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `enabled` | `bool` | |
| `destination_dir` | `Optional[str]` | |
| `distribution_location` | `Optional[str]` | |

## Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`schema()`](#schema) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
) -> ~A
```
| Parameter | Type | Description |
|-|-|-|
| `kvs` | `typing.Union[dict, list, str, int, float, bool, NoneType]` | |
| `infer_missing` |  | |

### from_json()

```python
def from_json(
    s: typing.Union[str, bytes, bytearray],
    parse_float,
    parse_int,
    parse_constant,
    infer_missing,
    kw,
) -> ~A
```
| Parameter | Type | Description |
|-|-|-|
| `s` | `typing.Union[str, bytes, bytearray]` | |
| `parse_float` |  | |
| `parse_int` |  | |
| `parse_constant` |  | |
| `infer_missing` |  | |
| `kw` |  | |

### schema()

```python
def schema(
    infer_missing: bool,
    only,
    exclude,
    many: bool,
    context,
    load_only,
    dump_only,
    partial: bool,
    unknown,
) -> SchemaType[A]
```
| Parameter | Type | Description |
|-|-|-|
| `infer_missing` | `bool` | |
| `only` |  | |
| `exclude` |  | |
| `many` | `bool` | |
| `context` |  | |
| `load_only` |  | |
| `dump_only` |  | |
| `partial` | `bool` | |
| `unknown` |  | |

### to_dict()

```python
def to_dict(
    encode_json,
) -> typing.Dict[str, typing.Union[dict, list, str, int, float, bool, NoneType]]
```
| Parameter | Type | Description |
|-|-|-|
| `encode_json` |  | |

### to_json()

```python
def to_json(
    skipkeys: bool,
    ensure_ascii: bool,
    check_circular: bool,
    allow_nan: bool,
    indent: typing.Union[int, str, NoneType],
    separators: typing.Tuple[str, str],
    default: typing.Callable,
    sort_keys: bool,
    kw,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `skipkeys` | `bool` | |
| `ensure_ascii` | `bool` | |
| `check_circular` | `bool` | |
| `allow_nan` | `bool` | |
| `indent` | `typing.Union[int, str, NoneType]` | |
| `separators` | `typing.Tuple[str, str]` | |
| `default` | `typing.Callable` | |
| `sort_keys` | `bool` | |
| `kw` |  | |

