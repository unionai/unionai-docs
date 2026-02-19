---
title: flytekit.models.core.types
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.models.core.types

## Directory

### Classes

| Class | Description |
|-|-|
| [`BlobType`](.././flytekit.models.core.types#flytekitmodelscoretypesblobtype) | This type represents offloaded data and is typically used for things like files. |
| [`EnumType`](.././flytekit.models.core.types#flytekitmodelscoretypesenumtype) | Models _types_pb2. |

## flytekit.models.core.types.BlobType

This type represents offloaded data and is typically used for things like files.



```python
class BlobType(
    format,
    dimensionality,
)
```
| Parameter | Type | Description |
|-|-|-|
| `format` |  | |
| `dimensionality` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `dimensionality` | `None` | An integer from BlobType.BlobDimensionality enum :rtype: int |
| `format` | `None` | A string describing the format of the underlying blob data. :rtype: Text |
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.types_pb2.BlobType


## flytekit.models.core.types.EnumType

Models _types_pb2.EnumType



```python
class EnumType(
    values: typing.List[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `values` | `typing.List[str]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `values` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto: _types_pb2.EnumType,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` | `_types_pb2.EnumType` | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
