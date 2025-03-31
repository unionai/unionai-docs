---
title: flytekit.models.types
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.types

## Directory

### Classes

| Class | Description |
|-|-|
| [`Error`](.././flytekit.models.types#flytekitmodelstypeserror) |  |
| [`LiteralType`](.././flytekit.models.types#flytekitmodelstypesliteraltype) |  |
| [`OutputReference`](.././flytekit.models.types#flytekitmodelstypesoutputreference) |  |
| [`SchemaType`](.././flytekit.models.types#flytekitmodelstypesschematype) |  |
| [`SimpleType`](.././flytekit.models.types#flytekitmodelstypessimpletype) |  |
| [`StructuredDatasetType`](.././flytekit.models.types#flytekitmodelstypesstructureddatasettype) |  |
| [`TypeAnnotationModel`](.././flytekit.models.types#flytekitmodelstypestypeannotationmodel) | Python class representation of the flyteidl TypeAnnotation message. |
| [`TypeStructure`](.././flytekit.models.types#flytekitmodelstypestypestructure) | Models _types_pb2. |
| [`UnionType`](.././flytekit.models.types#flytekitmodelstypesuniontype) | Models _types_pb2. |

## flytekit.models.types.Error

```python
class Error(
    failed_node_id: str,
    message: str,
)
```
| Parameter | Type |
|-|-|
| `failed_node_id` | `str` |
| `message` | `str` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.types_pb2.Error,
) -> Error
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.types_pb2.Error` |

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
| `failed_node_id` |  |  |
| `is_empty` |  |  |
| `message` |  |  |

## flytekit.models.types.LiteralType

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

## flytekit.models.types.OutputReference

```python
class OutputReference(
    node_id,
    var,
    attr_path: typing.List[typing.Union[str, int]],
)
```
A reference to an output produced by a node. The type can be retrieved -and validated- from
the underlying interface of the node.



| Parameter | Type |
|-|-|
| `node_id` |  |
| `var` |  |
| `attr_path` | `typing.List[typing.Union[str, int]]` |

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
    pb2_object,
) -> OutputReference
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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
| `attr_path` |  | {{< multiline >}}The attribute path the promise will be resolved with.
{{< /multiline >}} |
| `is_empty` |  |  |
| `node_id` |  | {{< multiline >}}Node id must exist at the graph layer.
{{< /multiline >}} |
| `var` |  | {{< multiline >}}Variable name must refer to an output variable for the node.
{{< /multiline >}} |

## flytekit.models.types.SchemaType

```python
class SchemaType(
    columns,
)
```
| Parameter | Type |
|-|-|
| `columns` |  |

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
) -> SchemaType
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
| `columns` |  | {{< multiline >}}A list of columns defining the underlying data frame.
{{< /multiline >}} |
| `is_empty` |  |  |

## flytekit.models.types.SimpleType

## flytekit.models.types.StructuredDatasetType

```python
class StructuredDatasetType(
    columns: typing.List[flytekit.models.types.StructuredDatasetType.DatasetColumn],
    format: str,
    external_schema_type: str,
    external_schema_bytes: bytes,
)
```
| Parameter | Type |
|-|-|
| `columns` | `typing.List[flytekit.models.types.StructuredDatasetType.DatasetColumn]` |
| `format` | `str` |
| `external_schema_type` | `str` |
| `external_schema_bytes` | `bytes` |

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
    proto: flyteidl.core.types_pb2.StructuredDatasetType,
) -> flyteidl.core.types_pb2.StructuredDatasetType
```
| Parameter | Type |
|-|-|
| `proto` | `flyteidl.core.types_pb2.StructuredDatasetType` |

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
| `columns` |  |  |
| `external_schema_bytes` |  |  |
| `external_schema_type` |  |  |
| `format` |  |  |
| `is_empty` |  |  |

## flytekit.models.types.TypeAnnotationModel

Python class representation of the flyteidl TypeAnnotation message.


```python
class TypeAnnotationModel(
    annotations: typing.Dict[str, typing.Any],
)
```
| Parameter | Type |
|-|-|
| `annotations` | `typing.Dict[str, typing.Any]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`merge_annotations()`](#merge_annotations) | Merges two annotations together. |
| [`to_flyte_idl()`](#to_flyte_idl) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> TypeAnnotation
```
| Parameter | Type |
|-|-|
| `proto` |  |

#### merge_annotations()

```python
def merge_annotations(
    annotation: TypeAnnotation,
    other_annotation: TypeAnnotation,
) -> TypeAnnotation
```
Merges two annotations together. If the same key exists in both annotations, the value in the other annotation
will be used.


| Parameter | Type |
|-|-|
| `annotation` | `TypeAnnotation` |
| `other_annotation` | `TypeAnnotation` |

#### to_flyte_idl()

```python
def to_flyte_idl()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `annotations` |  |  |

## flytekit.models.types.TypeStructure

Models _types_pb2.TypeStructure


```python
class TypeStructure(
    tag: str,
    dataclass_type: typing.Dict[str, ForwardRef('LiteralType')],
)
```
| Parameter | Type |
|-|-|
| `tag` | `str` |
| `dataclass_type` | `typing.Dict[str, ForwardRef('LiteralType')]` |

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
    proto: flyteidl.core.types_pb2.TypeStructure,
)
```
| Parameter | Type |
|-|-|
| `proto` | `flyteidl.core.types_pb2.TypeStructure` |

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
| `dataclass_type` |  |  |
| `is_empty` |  |  |
| `tag` |  |  |

## flytekit.models.types.UnionType

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

