---
title: FlyteSchema
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteSchema

**Package:** `flytekit.types.schema.types`

```python
class FlyteSchema(
    local_path: typing.Optional[str],
    remote_path: typing.Optional[str],
    supported_mode: SchemaOpenMode,
    downloader: typing.Optional[typing.Callable],
)
```
| Parameter | Type | Description |
|-|-|-|
| `local_path` | `typing.Optional[str]` | |
| `remote_path` | `typing.Optional[str]` | |
| `supported_mode` | `SchemaOpenMode` | |
| `downloader` | `typing.Optional[typing.Callable]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `local_path` | `None` |  |
| `supported_mode` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`as_readonly()`](#as_readonly) |  |
| [`column_names()`](#column_names) |  |
| [`columns()`](#columns) |  |
| [`deserialize_flyte_schema()`](#deserialize_flyte_schema) |  |
| [`format()`](#format) |  |
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`open()`](#open) | Returns a reader or writer depending on the mode of the object when created. |
| [`serialize_flyte_schema()`](#serialize_flyte_schema) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


### as_readonly()

```python
def as_readonly()
```
### column_names()

```python
def column_names()
```
### columns()

```python
def columns()
```
### deserialize_flyte_schema()

```python
def deserialize_flyte_schema(
    info,
) -> FlyteSchema
```
| Parameter | Type | Description |
|-|-|-|
| `info` |  | |

### format()

```python
def format()
```
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

### open()

```python
def open(
    dataframe_fmt: typing.Optional[type],
    override_mode: typing.Optional[SchemaOpenMode],
) -> typing.Union[SchemaReader, SchemaWriter]
```
Returns a reader or writer depending on the mode of the object when created. This mode can be
overridden, but will depend on whether the override can be performed. For example, if the Object was
created in a read-mode a "write mode" override is not allowed.
if the object was created in write-mode, a read is allowed.



| Parameter | Type | Description |
|-|-|-|
| `dataframe_fmt` | `typing.Optional[type]` | Type of the dataframe for example pandas.DataFrame etc |
| `override_mode` | `typing.Optional[SchemaOpenMode]` | overrides the default mode (Read, Write) SchemaOpenMode.READ, SchemaOpenMode.Write So if you have written to a schema and want to re-open it for reading, you can use this mode. A ReadOnly Schema object cannot be opened in write mode. |

### serialize_flyte_schema()

```python
def serialize_flyte_schema()
```
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

