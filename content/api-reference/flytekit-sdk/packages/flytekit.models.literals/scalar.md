---
title: Scalar
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Scalar

**Package:** `flytekit.models.literals`

```python
class Scalar(
    primitive: typing.Optional[flytekit.models.literals.Primitive],
    blob: typing.Optional[flytekit.models.literals.Blob],
    binary: typing.Optional[flytekit.models.literals.Binary],
    schema: typing.Optional[flytekit.models.literals.Schema],
    union: typing.Optional[flytekit.models.literals.Union],
    none_type: typing.Optional[flytekit.models.literals.Void],
    error: typing.Optional[flytekit.models.types.Error],
    generic: typing.Optional[google.protobuf.struct_pb2.Struct],
    structured_dataset: typing.Optional[flytekit.models.literals.StructuredDataset],
)
```
Scalar wrapper around Flyte types.  Only one can be specified.



| Parameter | Type | Description |
|-|-|-|
| `primitive` | `typing.Optional[flytekit.models.literals.Primitive]` | |
| `blob` | `typing.Optional[flytekit.models.literals.Blob]` | |
| `binary` | `typing.Optional[flytekit.models.literals.Binary]` | |
| `schema` | `typing.Optional[flytekit.models.literals.Schema]` | |
| `union` | `typing.Optional[flytekit.models.literals.Union]` | |
| `none_type` | `typing.Optional[flytekit.models.literals.Void]` | |
| `error` | `typing.Optional[flytekit.models.types.Error]` | |
| `generic` | `typing.Optional[google.protobuf.struct_pb2.Struct]` | |
| `structured_dataset` | `typing.Optional[flytekit.models.literals.StructuredDataset]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `binary` | `None` | :rtype: Binary |
| `blob` | `None` | :rtype: Blob |
| `error` | `None` | :rtype: Error |
| `generic` | `None` | :rtype: google.protobuf.struct_pb2.Struct |
| `is_empty` | `None` |  |
| `none_type` | `None` | :rtype: Void |
| `primitive` | `None` | :rtype: Primitive |
| `schema` | `None` | :rtype: Schema |
| `structured_dataset` | `None` |  |
| `union` | `None` | :rtype: Union |
| `value` | `None` | Returns whichever value is set :rtype: T |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

### serialize_to_string()

```python
def serialize_to_string()
```
### short_string()

```python
def short_string()
```
:rtype: Text


### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.literals_pb2.Scalar


