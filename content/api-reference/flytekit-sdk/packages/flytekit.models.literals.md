---
title: flytekit.models.literals
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
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

```python
class Binary(
    value,
    tag,
)
```
| Parameter | Type |
|-|-|
| `value` |  |
| `tag` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: Binary
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.literals_pb2.Binary


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `tag` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `value` |  | {{< multiline >}}:rtype: bytes
{{< /multiline >}} |

## flytekit.models.literals.Binding

```python
class Binding(
    var,
    binding,
)
```
An input/output binding of a variable to either static value or a node output.



| Parameter | Type |
|-|-|
| `var` |  |
| `binding` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: flytekit.core.models.literals.Binding
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.literals_pb2.Binding


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `binding` |  | {{< multiline >}}Data to use to bind this variable.
:rtype: BindingData
{{< /multiline >}} |
| `is_empty` |  |  |
| `var` |  | {{< multiline >}}A variable name, must match an input or output variable of the node.
:rtype: Text
{{< /multiline >}} |

## flytekit.models.literals.BindingData

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



| Parameter | Type |
|-|-|
| `scalar` |  |
| `collection` |  |
| `promise` |  |
| `map` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`to_literal_model()`](#to_literal_model) | Converts current binding data into a Literal asserting that there are no promises in the bindings. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> n: BindingData
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.literals_pb2.BindingData


#### to_literal_model()

```python
def to_literal_model()
```
Converts current binding data into a Literal asserting that there are no promises in the bindings.
:rtype: Literal


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `collection` |  | {{< multiline >}}[Optional] A collection of binding data. This allows nesting of binding data to any number of levels.
:rtype: BindingDataCollection
{{< /multiline >}} |
| `is_empty` |  |  |
| `map` |  | {{< multiline >}}[Optional] A map of bindings. The key is always a string.
:rtype: BindingDataMap
{{< /multiline >}} |
| `promise` |  | {{< multiline >}}[Optional] References an output promised by another node.
:rtype: flytekit.models.types.OutputReference
{{< /multiline >}} |
| `scalar` |  | {{< multiline >}}A simple scalar value.
:rtype: Scalar
{{< /multiline >}} |
| `value` |  | {{< multiline >}}Returns whichever value is set
:rtype: T
{{< /multiline >}} |

## flytekit.models.literals.BindingDataCollection

```python
class BindingDataCollection(
    bindings,
)
```
A list of BindingData items.



| Parameter | Type |
|-|-|
| `bindings` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: flytekit.models.literals.BindingDataCollection
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.literals_pb2.BindingDataCollection


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `bindings` |  | {{< multiline >}}:rtype: list[BindingData]
{{< /multiline >}} |
| `is_empty` |  |  |

## flytekit.models.literals.BindingDataMap

```python
class BindingDataMap(
    bindings,
)
```
A map of BindingData items.  Can be a recursive structure



| Parameter | Type |
|-|-|
| `bindings` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: flytekit.models.literals.BindingDataMap
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.literals_pb2.BindingDataMap


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `bindings` |  | {{< multiline >}}Map of strings to Bindings
:rtype: dict[string, BindingData]
{{< /multiline >}} |
| `is_empty` |  |  |

## flytekit.models.literals.Blob

```python
class Blob(
    metadata,
    uri,
)
```
This literal model is used to represent binary data offloaded to some storage location which is
identifiable with a unique string. See {{< py_class_ref flytekit.FlyteFile >}} as an example.



| Parameter | Type |
|-|-|
| `metadata` |  |
| `uri` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> e: Blob
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.literals_pb2.Blob


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `metadata` |  | {{< multiline >}}:rtype: BlobMetadata
{{< /multiline >}} |
| `uri` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |

## flytekit.models.literals.BlobMetadata

This is metadata for the Blob literal.


```python
class BlobMetadata(
    type,
)
```
| Parameter | Type |
|-|-|
| `type` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> e: BlobMetadata
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.literals_pb2.BlobMetadata


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `type` |  | {{< multiline >}}:rtype: flytekit.models.core.types.BlobType
{{< /multiline >}} |

## flytekit.models.literals.Literal

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



| Parameter | Type |
|-|-|
| `scalar` | `typing.Optional[flytekit.models.literals.Scalar]` |
| `collection` | `typing.Optional[flytekit.models.literals.LiteralCollection]` |
| `map` | `typing.Optional[flytekit.models.literals.LiteralMap]` |
| `hash` | `typing.Optional[str]` |
| `metadata` | `typing.Optional[typing.Dict[str, str]]` |
| `offloaded_metadata` | `typing.Optional[flytekit.models.literals.LiteralOffloadedMetadata]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`set_metadata()`](#set_metadata) | Note: This is a mutation on the literal. |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.literals_pb2.Literal,
) -> e: Literal
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.literals_pb2.Literal` |

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


| Parameter | Type |
|-|-|
| `metadata` | `typing.Dict[str, str]` |

#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.literals_pb2.Literal


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `collection` |  | {{< multiline >}}If not None, this value holds a collection of Literal values which can be further unpacked.
:rtype: LiteralCollection
{{< /multiline >}} |
| `hash` |  | {{< multiline >}}If not None, this value holds a hash that represents the literal for caching purposes.
:rtype: str
{{< /multiline >}} |
| `is_empty` |  |  |
| `map` |  | {{< multiline >}}If not None, this value holds a map of Literal values which can be further unpacked.
:rtype: LiteralMap
{{< /multiline >}} |
| `metadata` |  | {{< multiline >}}This value holds metadata about the literal.
{{< /multiline >}} |
| `offloaded_metadata` |  | {{< multiline >}}This value holds metadata about the offloaded literal.
{{< /multiline >}} |
| `scalar` |  | {{< multiline >}}If not None, this value holds a scalar value which can be further unpacked.
:rtype: Scalar
{{< /multiline >}} |
| `value` |  | {{< multiline >}}Returns one of the scalar, collection, or map properties based on which one is set.
:rtype: T
{{< /multiline >}} |

## flytekit.models.literals.LiteralCollection

```python
class LiteralCollection(
    literals,
)
```
| Parameter | Type |
|-|-|
| `literals` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: LiteralCollection
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.literals_pb2.LiteralCollection


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `literals` |  | {{< multiline >}}:rtype: list[Literal]
{{< /multiline >}} |

## flytekit.models.literals.LiteralMap

```python
class LiteralMap(
    literals,
)
```
| Parameter | Type |
|-|-|
| `literals` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: LiteralMap
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.literals_pb2.LiteralMap


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `literals` |  | {{< multiline >}}A dictionary mapping Text key names to Literal objects.
:rtype: dict[Text, Literal]
{{< /multiline >}} |

## flytekit.models.literals.LiteralOffloadedMetadata

```python
class LiteralOffloadedMetadata(
    uri: typing.Optional[str],
    size_bytes: typing.Optional[int],
    inferred_type: typing.Optional[flytekit.models.types.LiteralType],
)
```
| Parameter | Type |
|-|-|
| `uri` | `typing.Optional[str]` |
| `size_bytes` | `typing.Optional[int]` |
| `inferred_type` | `typing.Optional[flytekit.models.types.LiteralType]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `inferred_type` |  |  |
| `is_empty` |  |  |
| `size_bytes` |  |  |
| `uri` |  |  |

## flytekit.models.literals.Primitive

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


| Parameter | Type |
|-|-|
| `integer` | `typing.Optional[int]` |
| `float_value` | `typing.Optional[float]` |
| `string_value` | `typing.Optional[str]` |
| `boolean` | `typing.Optional[bool]` |
| `datetime` | `typing.Optional[datetime.datetime]` |
| `duration` | `typing.Optional[datetime.timedelta]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> e: Primitive
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.literals_pb2.Primitive


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `boolean` |  | {{< multiline >}}:rtype: bool
{{< /multiline >}} |
| `datetime` |  | {{< multiline >}}:rtype: datetime.datetime
{{< /multiline >}} |
| `duration` |  | {{< multiline >}}:rtype: datetime.timedelta
{{< /multiline >}} |
| `float_value` |  | {{< multiline >}}:rtype: float
{{< /multiline >}} |
| `integer` |  | {{< multiline >}}:rtype: int
{{< /multiline >}} |
| `is_empty` |  |  |
| `string_value` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `value` |  | {{< multiline >}}This returns whichever field is set.
:rtype: T
{{< /multiline >}} |

## flytekit.models.literals.RetryStrategy

```python
class RetryStrategy(
    retries: int,
)
```
| Parameter | Type |
|-|-|
| `retries` | `int` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: RetryStrategy
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.literals_pb2.RetryStrategy


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `retries` |  | {{< multiline >}}Number of retries to attempt on recoverable failures.  If retries is 0, then only one attempt will be made.
:rtype: int
{{< /multiline >}} |

## flytekit.models.literals.Scalar

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



| Parameter | Type |
|-|-|
| `primitive` | `typing.Optional[flytekit.models.literals.Primitive]` |
| `blob` | `typing.Optional[flytekit.models.literals.Blob]` |
| `binary` | `typing.Optional[flytekit.models.literals.Binary]` |
| `schema` | `typing.Optional[flytekit.models.literals.Schema]` |
| `union` | `typing.Optional[flytekit.models.literals.Union]` |
| `none_type` | `typing.Optional[flytekit.models.literals.Void]` |
| `error` | `typing.Optional[flytekit.models.types.Error]` |
| `generic` | `typing.Optional[google.protobuf.struct_pb2.Struct]` |
| `structured_dataset` | `typing.Optional[flytekit.models.literals.StructuredDataset]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: flytekit.models.literals.Scalar
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.literals_pb2.Scalar


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

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

## flytekit.models.literals.Schema

```python
class Schema(
    uri,
    type,
)
```
A strongly typed schema that defines the interface of data retrieved from the underlying storage medium.



| Parameter | Type |
|-|-|
| `uri` |  |
| `type` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: Schema
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.literals_pb2.Schema


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `type` |  | {{< multiline >}}:rtype: flytekit.models.types.SchemaType
{{< /multiline >}} |
| `uri` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |

## flytekit.models.literals.StructuredDataset

```python
class StructuredDataset(
    uri: str,
    metadata: typing.Optional[flytekit.models.literals.StructuredDatasetMetadata],
)
```
A strongly typed schema that defines the interface of data retrieved from the underlying storage medium.


| Parameter | Type |
|-|-|
| `uri` | `str` |
| `metadata` | `typing.Optional[flytekit.models.literals.StructuredDatasetMetadata]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.literals_pb2.StructuredDataset,
) -> StructuredDataset
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.literals_pb2.StructuredDataset` |

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
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `metadata` |  |  |
| `uri` |  |  |

## flytekit.models.literals.StructuredDatasetMetadata

```python
class StructuredDatasetMetadata(
    structured_dataset_type: typing.Optional[flytekit.models.types.StructuredDatasetType],
)
```
| Parameter | Type |
|-|-|
| `structured_dataset_type` | `typing.Optional[flytekit.models.types.StructuredDatasetType]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.literals_pb2.StructuredDatasetMetadata,
) -> StructuredDatasetMetadata
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.literals_pb2.StructuredDatasetMetadata` |

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
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `structured_dataset_type` |  |  |

## flytekit.models.literals.Union

```python
class Union(
    value,
    stored_type,
)
```
The runtime representation of a tagged union value. See `UnionType` for more details.



| Parameter | Type |
|-|-|
| `value` |  |
| `stored_type` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: Schema
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.literals_pb2.Union


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `stored_type` |  | {{< multiline >}}:rtype: flytekit.models.types.LiteralType
{{< /multiline >}} |
| `value` |  | {{< multiline >}}:rtype: flytekit.models.literals.Literal
{{< /multiline >}} |

## flytekit.models.literals.Void

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> e: Void
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.literals_pb2.Void


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

