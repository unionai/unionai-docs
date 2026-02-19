---
title: LiteralType
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# LiteralType

**Package:** `flytekit.models.types`

```python
class LiteralType(
    simple,
    schema,
    collection_type,
    map_value_type,
    blob,
    enum_type,
    union_type,
    structured_dataset_type,
    metadata,
    structure,
    annotation,
)
```
This is a oneof message, only one of the kwargs may be set, representing one of the Flyte types.



| Parameter | Type | Description |
|-|-|-|
| `simple` |  | |
| `schema` |  | |
| `collection_type` |  | |
| `map_value_type` |  | |
| `blob` |  | |
| `enum_type` |  | |
| `union_type` |  | |
| `structured_dataset_type` |  | |
| `metadata` |  | |
| `structure` |  | |
| `annotation` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `annotation` | `None` | :rtype: flytekit.models.annotation.TypeAnnotation |
| `blob` | `None` |  |
| `collection_type` | `None` | The collection value type |
| `enum_type` | `None` |  |
| `is_empty` | `None` |  |
| `map_value_type` | `None` | The Value for a dictionary. Key is always string |
| `metadata` | `None` | :rtype: dict[Text, T] |
| `schema` | `None` |  |
| `simple` | `None` |  |
| `structure` | `None` |  |
| `structured_dataset_type` | `None` |  |
| `union_type` | `None` |  |

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
    proto,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` |  | |

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
:rtype: flyteidl.core.types_pb2.LiteralType


