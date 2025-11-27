---
title: StructuredDataset
version: 0.1.198
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# StructuredDataset

**Package:** `union`

This is the user facing StructuredDataset class. Please don't confuse it with the literals.StructuredDataset
class (that is just a model, a Python class representation of the protobuf).


```python
class StructuredDataset(
    dataframe: typing.Optional[typing.Any],
    uri: typing.Optional[str],
    metadata: typing.Optional[literals.StructuredDatasetMetadata],
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `dataframe` | `typing.Optional[typing.Any]` | |
| `uri` | `typing.Optional[str]` | |
| `metadata` | `typing.Optional[literals.StructuredDatasetMetadata]` | |
| `kwargs` | `**kwargs` | |

## Methods

| Method | Description |
|-|-|
| [`all()`](#all) |  |
| [`column_names()`](#column_names) |  |
| [`columns()`](#columns) |  |
| [`deserialize_structured_dataset()`](#deserialize_structured_dataset) |  |
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`iter()`](#iter) |  |
| [`open()`](#open) |  |
| [`serialize_structured_dataset()`](#serialize_structured_dataset) |  |
| [`set_literal()`](#set_literal) | A public wrapper method to set the StructuredDataset Literal. |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


### all()

```python
def all()
```
### column_names()

```python
def column_names()
```
### columns()

```python
def columns()
```
### deserialize_structured_dataset()

```python
def deserialize_structured_dataset(
    info,
) -> StructuredDataset
```
| Parameter | Type | Description |
|-|-|-|
| `info` |  | |

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

### iter()

```python
def iter()
```
### open()

```python
def open(
    dataframe_type: Type[DF],
)
```
| Parameter | Type | Description |
|-|-|-|
| `dataframe_type` | `Type[DF]` | |

### serialize_structured_dataset()

```python
def serialize_structured_dataset()
```
### set_literal()

```python
def set_literal(
    ctx: FlyteContext,
    expected: LiteralType,
)
```
A public wrapper method to set the StructuredDataset Literal.

This method provides external access to the internal _set_literal method.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `expected` | `LiteralType` | |

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

## Properties

| Property | Type | Description |
|-|-|-|
| `dataframe` |  |  |
| `literal` |  |  |
| `metadata` |  |  |

