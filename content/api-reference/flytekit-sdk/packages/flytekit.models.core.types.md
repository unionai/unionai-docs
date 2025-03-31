---
title: flytekit.models.core.types
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
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
def BlobType(
    format,
    dimensionality,
):
```
| Parameter | Type |
|-|-|
| `format` |  |
| `dimensionality` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
):
```
| Parameter | Type |
|-|-|
| `proto` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| dimensionality |  |  |
| format |  |  |
| is_empty |  |  |

## flytekit.models.core.types.EnumType

Models _types_pb2.EnumType


```python
def EnumType(
    values: typing.List[str],
):
```
| Parameter | Type |
|-|-|
| `values` | `typing.List[str]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto: _types_pb2.EnumType,
):
```
| Parameter | Type |
|-|-|
| `proto` | `_types_pb2.EnumType` |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| is_empty |  |  |
| values |  |  |

