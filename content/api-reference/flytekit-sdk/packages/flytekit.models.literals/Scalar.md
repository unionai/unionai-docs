---
title: Scalar
version: 1.16.10
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


## Properties

| Property | Type | Description |
|-|-|-|
| `binary` |  | {{< multiline >}}:rtype: Binary
{{< /multiline >}} |
| `blob` |  | {{< multiline >}}:rtype: Blob
{{< /multiline >}} |
| `error` |  | {{< multiline >}}:rtype: Error
{{< /multiline >}} |
| `generic` |  | {{< multiline >}}:rtype: google.protobuf.struct_pb2.Struct
{{< /multiline >}} |
| `is_empty` |  |  |
| `none_type` |  | {{< multiline >}}:rtype: Void
{{< /multiline >}} |
| `primitive` |  | {{< multiline >}}:rtype: Primitive
{{< /multiline >}} |
| `schema` |  | {{< multiline >}}:rtype: Schema
{{< /multiline >}} |
| `structured_dataset` |  |  |
| `union` |  | {{< multiline >}}:rtype: Union
{{< /multiline >}} |
| `value` |  | {{< multiline >}}Returns whichever value is set
:rtype: T
{{< /multiline >}} |

