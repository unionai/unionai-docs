---
title: flytekit.models.types
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
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
| [`TypeStructure`](.././flytekit.models.types#flytekitmodelstypestypestructure) | Models _types_pb2. |
| [`UnionType`](.././flytekit.models.types#flytekitmodelstypesuniontype) | Models _types_pb2. |

## flytekit.models.types.Error

```python
class Error(
    failed_node_id: str,
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `failed_node_id` | `str` | |
| `message` | `str` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `failed_node_id` | `None` |  |
| `is_empty` | `None` |  |
| `message` | `None` |  |

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
    pb2_object: flyteidl.core.types_pb2.Error,
) -> Error
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.types_pb2.Error` | |

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

### Properties

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
:rtype: flyteidl.core.types_pb2.LiteralType


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



| Parameter | Type | Description |
|-|-|-|
| `node_id` |  | |
| `var` |  | |
| `attr_path` | `typing.List[typing.Union[str, int]]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `attr_path` | `None` | The attribute path the promise will be resolved with. :rtype: list[union[str, int]] |
| `is_empty` | `None` |  |
| `node_id` | `None` | Node id must exist at the graph layer. :rtype: Text |
| `var` | `None` | Variable name must refer to an output variable for the node. :rtype: Text |

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
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

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
:rtype: flyteidl.core.types.OutputReference


## flytekit.models.types.SchemaType

```python
class SchemaType(
    columns,
)
```
| Parameter | Type | Description |
|-|-|-|
| `columns` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `columns` | `None` | A list of columns defining the underlying data frame. :rtype: list[SchemaType.SchemaColumn] |
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
:rtype: flyteidl.core.types_pb2.SchemaType


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
| Parameter | Type | Description |
|-|-|-|
| `columns` | `typing.List[flytekit.models.types.StructuredDatasetType.DatasetColumn]` | |
| `format` | `str` | |
| `external_schema_type` | `str` | |
| `external_schema_bytes` | `bytes` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `columns` | `None` |  |
| `external_schema_bytes` | `None` |  |
| `external_schema_type` | `None` |  |
| `format` | `None` |  |
| `is_empty` | `None` |  |

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
    proto: flyteidl.core.types_pb2.StructuredDatasetType,
) -> flyteidl.core.types_pb2.StructuredDatasetType
```
| Parameter | Type | Description |
|-|-|-|
| `proto` | `flyteidl.core.types_pb2.StructuredDatasetType` | |

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
## flytekit.models.types.TypeStructure

Models _types_pb2.TypeStructure



```python
class TypeStructure(
    tag: str,
    dataclass_type: typing.Dict[str, ForwardRef('LiteralType')],
)
```
| Parameter | Type | Description |
|-|-|-|
| `tag` | `str` | |
| `dataclass_type` | `typing.Dict[str, ForwardRef('LiteralType')]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `dataclass_type` | `None` |  |
| `is_empty` | `None` |  |
| `tag` | `None` |  |

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
    proto: flyteidl.core.types_pb2.TypeStructure,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` | `flyteidl.core.types_pb2.TypeStructure` | |

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
## flytekit.models.types.UnionType

Models _types_pb2.UnionType



```python
class UnionType(
    variants: typing.List[ForwardRef('LiteralType')],
)
```
| Parameter | Type | Description |
|-|-|-|
| `variants` | `typing.List[ForwardRef('LiteralType')]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `variants` | `None` |  |

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
    proto: flyteidl.core.types_pb2.UnionType,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` | `flyteidl.core.types_pb2.UnionType` | |

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
