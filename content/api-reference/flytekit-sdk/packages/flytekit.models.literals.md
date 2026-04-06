---
title: flytekit.models.literals
version: 1.16.16
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# flytekit.models.literals

## Directory

### Classes

| Class | Description |
|-|-|
| [`Binary`](.././flytekit.models.literals#flytekitmodelsliteralsbinary) |  |
| [`Binding`](.././flytekit.models.literals#flytekitmodelsliteralsbinding) |  |
| [`BindingData`](.././flytekit.models.literals#flytekitmodelsliteralsbindingdata) |  |
| [`BindingDataCollection`](.././flytekit.models.literals#flytekitmodelsliteralsbindingdatacollection) |  |
| [`BindingDataMap`](.././flytekit.models.literals#flytekitmodelsliteralsbindingdatamap) |  |
| [`Blob`](.././flytekit.models.literals#flytekitmodelsliteralsblob) |  |
| [`BlobMetadata`](.././flytekit.models.literals#flytekitmodelsliteralsblobmetadata) | This is metadata for the Blob literal. |
| [`Literal`](.././flytekit.models.literals#flytekitmodelsliteralsliteral) |  |
| [`LiteralCollection`](.././flytekit.models.literals#flytekitmodelsliteralsliteralcollection) |  |
| [`LiteralMap`](.././flytekit.models.literals#flytekitmodelsliteralsliteralmap) |  |
| [`LiteralOffloadedMetadata`](.././flytekit.models.literals#flytekitmodelsliteralsliteraloffloadedmetadata) |  |
| [`Primitive`](.././flytekit.models.literals#flytekitmodelsliteralsprimitive) |  |
| [`RetryStrategy`](.././flytekit.models.literals#flytekitmodelsliteralsretrystrategy) |  |
| [`Scalar`](.././flytekit.models.literals#flytekitmodelsliteralsscalar) |  |
| [`Schema`](.././flytekit.models.literals#flytekitmodelsliteralsschema) |  |
| [`StructuredDataset`](.././flytekit.models.literals#flytekitmodelsliteralsstructureddataset) |  |
| [`StructuredDatasetMetadata`](.././flytekit.models.literals#flytekitmodelsliteralsstructureddatasetmetadata) |  |
| [`Union`](.././flytekit.models.literals#flytekitmodelsliteralsunion) |  |
| [`Void`](.././flytekit.models.literals#flytekitmodelsliteralsvoid) |  |

## flytekit.models.literals.Binary

### Parameters

```python
class Binary(
    value,
    tag,
)
```
| Parameter | Type | Description |
|-|-|-|
| `value` |  | |
| `tag` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `tag` | `None` |  |
| `value` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** Binary

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.literals_pb2.Binary

## flytekit.models.literals.Binding

### Parameters

```python
class Binding(
    var,
    binding,
)
```
An input/output binding of a variable to either static value or a node output.



| Parameter | Type | Description |
|-|-|-|
| `var` |  | |
| `binding` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `binding` | `None` | Data to use to bind this variable. |
| `is_empty` | `None` |  |
| `var` | `None` | A variable name, must match an input or output variable of the node. |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** flytekit.core.models.literals.Binding

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.literals_pb2.Binding

## flytekit.models.literals.BindingData

### Parameters

```python
class BindingData(
    scalar,
    collection,
    promise,
    map,
)
```
Specifies either a simple value or a reference to another output. Only one of the input arguments may be
specified.



| Parameter | Type | Description |
|-|-|-|
| `scalar` |  | |
| `collection` |  | |
| `promise` |  | |
| `map` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `collection` | `None` | [Optional] A collection of binding data. This allows nesting of binding data to any number of levels. |
| `is_empty` | `None` |  |
| `map` | `None` | [Optional] A map of bindings. The key is always a string. |
| `promise` | `None` | [Optional] References an output promised by another node. |
| `scalar` | `None` | A simple scalar value. |
| `value` | `None` | Returns whichever value is set |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`to_literal_model()`](#to_literal_model) | Converts current binding data into a Literal asserting that there are no promises in the bindings. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** BindingData

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.literals_pb2.BindingData

#### to_literal_model()

```python
def to_literal_model()
```
Converts current binding data into a Literal asserting that there are no promises in the bindings.


**Returns:** Literal

## flytekit.models.literals.BindingDataCollection

### Parameters

```python
class BindingDataCollection(
    bindings,
)
```
A list of BindingData items.



| Parameter | Type | Description |
|-|-|-|
| `bindings` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `bindings` | `None` |  |
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** flytekit.models.literals.BindingDataCollection

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.literals_pb2.BindingDataCollection

## flytekit.models.literals.BindingDataMap

### Parameters

```python
class BindingDataMap(
    bindings,
)
```
A map of BindingData items.  Can be a recursive structure



| Parameter | Type | Description |
|-|-|-|
| `bindings` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `bindings` | `None` | Map of strings to Bindings |
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** flytekit.models.literals.BindingDataMap

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.literals_pb2.BindingDataMap

## flytekit.models.literals.Blob

### Parameters

```python
class Blob(
    metadata,
    uri,
)
```
This literal model is used to represent binary data offloaded to some storage location which is
identifiable with a unique string. See {{&lt; py_class_ref flytekit.FlyteFile &gt;}} as an example.



| Parameter | Type | Description |
|-|-|-|
| `metadata` |  | |
| `uri` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `metadata` | `None` |  |
| `uri` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` |  | |

**Returns:** Blob

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.literals_pb2.Blob

## flytekit.models.literals.BlobMetadata

This is metadata for the Blob literal.


### Parameters

```python
class BlobMetadata(
    type,
)
```
| Parameter | Type | Description |
|-|-|-|
| `type` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `type` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` |  | |

**Returns:** BlobMetadata

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.literals_pb2.BlobMetadata

## flytekit.models.literals.Literal

### Parameters

```python
class Literal(
    scalar: typing.Optional[flytekit.models.literals.Scalar],
    collection: typing.Optional[flytekit.models.literals.LiteralCollection],
    map: typing.Optional[flytekit.models.literals.LiteralMap],
    hash: typing.Optional[str],
    metadata: typing.Optional[typing.Dict[str, str]],
    offloaded_metadata: typing.Optional[flytekit.models.literals.LiteralOffloadedMetadata],
)
```
This IDL message represents a literal value in the Flyte ecosystem.



| Parameter | Type | Description |
|-|-|-|
| `scalar` | `typing.Optional[flytekit.models.literals.Scalar]` | |
| `collection` | `typing.Optional[flytekit.models.literals.LiteralCollection]` | |
| `map` | `typing.Optional[flytekit.models.literals.LiteralMap]` | |
| `hash` | `typing.Optional[str]` | |
| `metadata` | `typing.Optional[typing.Dict[str, str]]` | |
| `offloaded_metadata` | `typing.Optional[flytekit.models.literals.LiteralOffloadedMetadata]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `collection` | `None` | If not None, this value holds a collection of Literal values which can be further unpacked. |
| `hash` | `None` | If not None, this value holds a hash that represents the literal for caching purposes. |
| `is_empty` | `None` |  |
| `map` | `None` | If not None, this value holds a map of Literal values which can be further unpacked. |
| `metadata` | `None` | This value holds metadata about the literal. |
| `offloaded_metadata` | `None` | This value holds metadata about the offloaded literal. |
| `scalar` | `None` | If not None, this value holds a scalar value which can be further unpacked. |
| `value` | `None` | Returns one of the scalar, collection, or map properties based on which one is set. |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`set_metadata()`](#set_metadata) | Note: This is a mutation on the literal. |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.literals_pb2.Literal,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.literals_pb2.Literal` | |

**Returns:** Literal

#### serialize_to_string()

```python
def serialize_to_string()
```
#### set_metadata()

```python
def set_metadata(
    metadata: typing.Dict[str, str],
)
```
Note: This is a mutation on the literal


| Parameter | Type | Description |
|-|-|-|
| `metadata` | `typing.Dict[str, str]` | |

#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.literals_pb2.Literal

## flytekit.models.literals.LiteralCollection

### Parameters

```python
class LiteralCollection(
    literals,
)
```
| Parameter | Type | Description |
|-|-|-|
| `literals` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `literals` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** LiteralCollection

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.literals_pb2.LiteralCollection

## flytekit.models.literals.LiteralMap

### Parameters

```python
class LiteralMap(
    literals,
)
```
| Parameter | Type | Description |
|-|-|-|
| `literals` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `literals` | `None` | A dictionary mapping Text key names to Literal objects. |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** LiteralMap

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.literals_pb2.LiteralMap

## flytekit.models.literals.LiteralOffloadedMetadata

### Parameters

```python
class LiteralOffloadedMetadata(
    uri: typing.Optional[str],
    size_bytes: typing.Optional[int],
    inferred_type: typing.Optional[flytekit.models.types.LiteralType],
)
```
| Parameter | Type | Description |
|-|-|-|
| `uri` | `typing.Optional[str]` | |
| `size_bytes` | `typing.Optional[int]` | |
| `inferred_type` | `typing.Optional[flytekit.models.types.LiteralType]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `inferred_type` | `None` |  |
| `is_empty` | `None` |  |
| `size_bytes` | `None` |  |
| `uri` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


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
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.models.literals.Primitive

### Parameters

```python
class Primitive(
    integer: typing.Optional[int],
    float_value: typing.Optional[float],
    string_value: typing.Optional[str],
    boolean: typing.Optional[bool],
    datetime: typing.Optional[datetime.datetime],
    duration: typing.Optional[datetime.timedelta],
)
```
This object proxies the primitives supported by the Flyte IDL system.  Only one value can be set.


| Parameter | Type | Description |
|-|-|-|
| `integer` | `typing.Optional[int]` | |
| `float_value` | `typing.Optional[float]` | |
| `string_value` | `typing.Optional[str]` | |
| `boolean` | `typing.Optional[bool]` | |
| `datetime` | `typing.Optional[datetime.datetime]` | |
| `duration` | `typing.Optional[datetime.timedelta]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `boolean` | `None` |  |
| `datetime` | `None` |  |
| `duration` | `None` |  |
| `float_value` | `None` |  |
| `integer` | `None` |  |
| `is_empty` | `None` |  |
| `string_value` | `None` |  |
| `value` | `None` | This returns whichever field is set. |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` |  | |

**Returns:** Primitive

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.literals_pb2.Primitive

## flytekit.models.literals.RetryStrategy

### Parameters

```python
class RetryStrategy(
    retries: int,
)
```
| Parameter | Type | Description |
|-|-|-|
| `retries` | `int` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `retries` | `None` | Number of retries to attempt on recoverable failures.  If retries is 0, then only one attempt will be made. |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** RetryStrategy

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.literals_pb2.RetryStrategy

## flytekit.models.literals.Scalar

### Parameters

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

### Properties

| Property | Type | Description |
|-|-|-|
| `binary` | `None` |  |
| `blob` | `None` |  |
| `error` | `None` |  |
| `generic` | `None` |  |
| `is_empty` | `None` |  |
| `none_type` | `None` |  |
| `primitive` | `None` |  |
| `schema` | `None` |  |
| `structured_dataset` | `None` |  |
| `union` | `None` |  |
| `value` | `None` | Returns whichever value is set |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** flytekit.models.literals.Scalar

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.literals_pb2.Scalar

## flytekit.models.literals.Schema

### Parameters

```python
class Schema(
    uri,
    type,
)
```
A strongly typed schema that defines the interface of data retrieved from the underlying storage medium.



| Parameter | Type | Description |
|-|-|-|
| `uri` |  | |
| `type` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `type` | `None` |  |
| `uri` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** Schema

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.literals_pb2.Schema

## flytekit.models.literals.StructuredDataset

### Parameters

```python
class StructuredDataset(
    uri: str,
    metadata: typing.Optional[flytekit.models.literals.StructuredDatasetMetadata],
)
```
A strongly typed schema that defines the interface of data retrieved from the underlying storage medium.


| Parameter | Type | Description |
|-|-|-|
| `uri` | `str` | |
| `metadata` | `typing.Optional[flytekit.models.literals.StructuredDatasetMetadata]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `metadata` | `None` |  |
| `uri` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.literals_pb2.StructuredDataset,
) -> StructuredDataset
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.literals_pb2.StructuredDataset` | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.models.literals.StructuredDatasetMetadata

### Parameters

```python
class StructuredDatasetMetadata(
    structured_dataset_type: typing.Optional[flytekit.models.types.StructuredDatasetType],
)
```
| Parameter | Type | Description |
|-|-|-|
| `structured_dataset_type` | `typing.Optional[flytekit.models.types.StructuredDatasetType]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `structured_dataset_type` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.literals_pb2.StructuredDatasetMetadata,
) -> StructuredDatasetMetadata
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.literals_pb2.StructuredDatasetMetadata` | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.models.literals.Union

### Parameters

```python
class Union(
    value,
    stored_type,
)
```
The runtime representation of a tagged union value. See `UnionType` for more details.



| Parameter | Type | Description |
|-|-|-|
| `value` |  | |
| `stored_type` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `stored_type` | `None` |  |
| `value` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** Schema

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.literals_pb2.Union

## flytekit.models.literals.Void

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` |  | |

**Returns:** Void

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.literals_pb2.Void

