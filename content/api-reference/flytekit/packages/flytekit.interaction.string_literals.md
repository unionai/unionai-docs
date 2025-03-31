---
title: flytekit.interaction.string_literals
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.interaction.string_literals

## Directory

### Classes

| Class | Description |
|-|-|
| [`Literal`](.././flytekit.interaction.string_literals#flytekitinteractionstring_literalsliteral) |  |
| [`LiteralMap`](.././flytekit.interaction.string_literals#flytekitinteractionstring_literalsliteralmap) |  |
| [`Primitive`](.././flytekit.interaction.string_literals#flytekitinteractionstring_literalsprimitive) |  |
| [`Scalar`](.././flytekit.interaction.string_literals#flytekitinteractionstring_literalsscalar) |  |

### Methods

| Method | Description |
|-|-|
| [`MessageToDict()`](#messagetodict) | Converts protobuf message to a dictionary. |
| [`literal_map_string_repr()`](#literal_map_string_repr) | This method is used to convert a literal map to a string representation. |
| [`literal_string_repr()`](#literal_string_repr) | This method is used to convert a literal to a string representation. |
| [`primitive_to_string()`](#primitive_to_string) | This method is used to convert a primitive to a string representation. |
| [`scalar_to_string()`](#scalar_to_string) | This method is used to convert a scalar to a string representation. |


## Methods

#### MessageToDict()

```python
def MessageToDict(
    message,
    always_print_fields_with_no_presence,
    preserving_proto_field_name,
    use_integers_for_enums,
    descriptor_pool,
    float_precision,
)
```
Converts protobuf message to a dictionary.

When the dictionary is encoded to JSON, it conforms to proto3 JSON spec.



| Parameter | Type |
|-|-|
| `message` |  |
| `always_print_fields_with_no_presence` |  |
| `preserving_proto_field_name` |  |
| `use_integers_for_enums` |  |
| `descriptor_pool` |  |
| `float_precision` |  |

#### literal_map_string_repr()

```python
def literal_map_string_repr(
    lm: typing.Union[flytekit.models.literals.LiteralMap, typing.Dict[str, flytekit.models.literals.Literal]],
) -> typing.Dict[str, typing.Any]
```
This method is used to convert a literal map to a string representation.


| Parameter | Type |
|-|-|
| `lm` | `typing.Union[flytekit.models.literals.LiteralMap, typing.Dict[str, flytekit.models.literals.Literal]]` |

#### literal_string_repr()

```python
def literal_string_repr(
    lit: flytekit.models.literals.Literal,
) -> typing.Any
```
This method is used to convert a literal to a string representation. This is useful in places, where we need to
use a shortened string representation of a literal, especially a FlyteFile, FlyteDirectory, or StructuredDataset.


| Parameter | Type |
|-|-|
| `lit` | `flytekit.models.literals.Literal` |

#### primitive_to_string()

```python
def primitive_to_string(
    primitive: flytekit.models.literals.Primitive,
) -> typing.Any
```
This method is used to convert a primitive to a string representation.


| Parameter | Type |
|-|-|
| `primitive` | `flytekit.models.literals.Primitive` |

#### scalar_to_string()

```python
def scalar_to_string(
    scalar: flytekit.models.literals.Scalar,
) -> typing.Any
```
This method is used to convert a scalar to a string representation.


| Parameter | Type |
|-|-|
| `scalar` | `flytekit.models.literals.Scalar` |

## flytekit.interaction.string_literals.Literal

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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`set_metadata()`](#set_metadata) | Note: This is a mutation on the literal. |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.literals_pb2.Literal,
) -> Literal
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
| `collection` |  | {{< multiline >}}If not None, this value holds a collection of Literal values which can be further unpacked.
{{< /multiline >}} |
| `hash` |  | {{< multiline >}}If not None, this value holds a hash that represents the literal for caching purposes.
{{< /multiline >}} |
| `is_empty` |  |  |
| `map` |  | {{< multiline >}}If not None, this value holds a map of Literal values which can be further unpacked.
{{< /multiline >}} |
| `metadata` |  | {{< multiline >}}This value holds metadata about the literal.
{{< /multiline >}} |
| `offloaded_metadata` |  | {{< multiline >}}This value holds metadata about the offloaded literal.
{{< /multiline >}} |
| `scalar` |  | {{< multiline >}}If not None, this value holds a scalar value which can be further unpacked.
{{< /multiline >}} |
| `value` |  | {{< multiline >}}Returns one of the scalar, collection, or map properties based on which one is set.
{{< /multiline >}} |

## flytekit.interaction.string_literals.LiteralMap

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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> LiteralMap
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
| `is_empty` |  |  |
| `literals` |  | {{< multiline >}}A dictionary mapping Text key names to Literal objects.
{{< /multiline >}} |

## flytekit.interaction.string_literals.Primitive

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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> Primitive
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
| `boolean` |  |  |
| `datetime` |  |  |
| `duration` |  |  |
| `float_value` |  |  |
| `integer` |  |  |
| `is_empty` |  |  |
| `string_value` |  |  |
| `value` |  | {{< multiline >}}This returns whichever field is set.
{{< /multiline >}} |

## flytekit.interaction.string_literals.Scalar

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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> flytekit.models.literals.Scalar
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
| `binary` |  |  |
| `blob` |  |  |
| `error` |  |  |
| `generic` |  |  |
| `is_empty` |  |  |
| `none_type` |  |  |
| `primitive` |  |  |
| `schema` |  |  |
| `structured_dataset` |  |  |
| `union` |  |  |
| `value` |  | {{< multiline >}}Returns whichever value is set
{{< /multiline >}} |

