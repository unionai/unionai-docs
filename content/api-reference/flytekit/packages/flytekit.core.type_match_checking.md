---
title: flytekit.core.type_match_checking
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.type_match_checking

## Directory

### Classes

| Class | Description |
|-|-|
| [`EnumType`](.././flytekit.core.type_match_checking#flytekitcoretype_match_checkingenumtype) | Models _types_pb2. |
| [`LiteralType`](.././flytekit.core.type_match_checking#flytekitcoretype_match_checkingliteraltype) |  |
| [`UnionType`](.././flytekit.core.type_match_checking#flytekitcoretype_match_checkinguniontype) | Models _types_pb2. |

### Methods

| Method | Description |
|-|-|
| [`_enum_types_match()`](#_enum_types_match) |  |
| [`_union_types_match()`](#_union_types_match) |  |
| [`literal_types_match()`](#literal_types_match) | Returns if two LiteralTypes are the same. |


### Variables

| Property | Type | Description |
|-|-|-|
| `annotations` | `_Feature` |  |

## Methods

#### _enum_types_match()

```python
def _enum_types_match(
    downstream: EnumType,
    upstream: EnumType,
) -> bool
```
| Parameter | Type |
|-|-|
| `downstream` | `EnumType` |
| `upstream` | `EnumType` |

#### _union_types_match()

```python
def _union_types_match(
    downstream: UnionType,
    upstream: UnionType,
) -> bool
```
| Parameter | Type |
|-|-|
| `downstream` | `UnionType` |
| `upstream` | `UnionType` |

#### literal_types_match()

```python
def literal_types_match(
    downstream: LiteralType,
    upstream: LiteralType,
) -> bool
```
Returns if two LiteralTypes are the same.
Takes into account arbitrary ordering of enums and unions, otherwise just an equivalence check.


| Parameter | Type |
|-|-|
| `downstream` | `LiteralType` |
| `upstream` | `LiteralType` |

## flytekit.core.type_match_checking.EnumType

Models _types_pb2.EnumType


```python
class EnumType(
    values: typing.List[str],
)
```
| Parameter | Type |
|-|-|
| `values` | `typing.List[str]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto: _types_pb2.EnumType,
)
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
| `is_empty` |  |  |
| `values` |  |  |

## flytekit.core.type_match_checking.LiteralType

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



| Parameter | Type |
|-|-|
| `simple` |  |
| `schema` |  |
| `collection_type` |  |
| `map_value_type` |  |
| `blob` |  |
| `enum_type` |  |
| `union_type` |  |
| `structured_dataset_type` |  |
| `metadata` |  |
| `structure` |  |
| `annotation` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> LiteralType
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
| `annotation` |  |  |
| `blob` |  |  |
| `collection_type` |  | {{< multiline >}}The collection value type
{{< /multiline >}} |
| `enum_type` |  |  |
| `is_empty` |  |  |
| `map_value_type` |  | {{< multiline >}}The Value for a dictionary. Key is always string
{{< /multiline >}} |
| `metadata` |  |  |
| `schema` |  |  |
| `simple` |  |  |
| `structure` |  |  |
| `structured_dataset_type` |  |  |
| `union_type` |  |  |

## flytekit.core.type_match_checking.UnionType

Models _types_pb2.UnionType


```python
class UnionType(
    variants: typing.List[ForwardRef('LiteralType')],
)
```
| Parameter | Type |
|-|-|
| `variants` | `typing.List[ForwardRef('LiteralType')]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto: flyteidl.core.types_pb2.UnionType,
)
```
| Parameter | Type |
|-|-|
| `proto` | `flyteidl.core.types_pb2.UnionType` |

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
| `is_empty` |  |  |
| `variants` |  |  |

