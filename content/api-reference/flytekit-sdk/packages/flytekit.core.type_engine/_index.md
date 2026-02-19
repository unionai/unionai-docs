---
title: flytekit.core.type_engine
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.type_engine

## Directory

### Classes

| Class | Description |
|-|-|
| [`AsyncTypeTransformer`](../flytekit.core.type_engine/asynctypetransformer) |  |
| [`BatchSize`](../flytekit.core.type_engine/batchsize) | This is used to annotate a FlyteDirectory when we want to download/upload the contents of the directory in batches. |
| [`BinaryIOTransformer`](../flytekit.core.type_engine/binaryiotransformer) | Handler for BinaryIO. |
| [`DataclassTransformer`](../flytekit.core.type_engine/dataclasstransformer) | The Dataclass Transformer provides a type transformer for dataclasses. |
| [`DictTransformer`](../flytekit.core.type_engine/dicttransformer) | Transformer that transforms an univariate dictionary Dict[str, T] to a Literal Map or. |
| [`EnumTransformer`](../flytekit.core.type_engine/enumtransformer) | Enables converting a python type enum. |
| [`ListTransformer`](../flytekit.core.type_engine/listtransformer) | Transformer that handles a univariate typing. |
| [`LiteralTypeTransformer`](../flytekit.core.type_engine/literaltypetransformer) |  |
| [`LiteralsResolver`](../flytekit.core.type_engine/literalsresolver) | LiteralsResolver is a helper class meant primarily for use with the FlyteRemote experience or any other situation. |
| [`ProtobufTransformer`](../flytekit.core.type_engine/protobuftransformer) |  |
| [`RestrictedTypeTransformer`](../flytekit.core.type_engine/restrictedtypetransformer) | Types registered with the RestrictedTypeTransformer are not allowed to be converted to and from literals. |
| [`SimpleTransformer`](../flytekit.core.type_engine/simpletransformer) | A Simple implementation of a type transformer that uses simple lambdas to transform and reduces boilerplate. |
| [`TextIOTransformer`](../flytekit.core.type_engine/textiotransformer) | Handler for TextIO. |
| [`TypeEngine`](../flytekit.core.type_engine/typeengine) | Core Extensible TypeEngine of Flytekit. |
| [`TypeTransformer`](../flytekit.core.type_engine/typetransformer) | Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`UnionTransformer`](../flytekit.core.type_engine/uniontransformer) | Transformer that handles a typing. |

### Errors

| Exception | Description |
|-|-|
| [`RestrictedTypeError`](../flytekit.core.type_engine/restrictedtypeerror) |  |
| [`TypeTransformerFailedError`](../flytekit.core.type_engine/typetransformerfailederror) |  |

### Methods

| Method | Description |
|-|-|
| [`convert_marshmallow_json_schema_to_python_class()`](#convert_marshmallow_json_schema_to_python_class) | Generate a model class based on the provided JSON Schema. |
| [`convert_mashumaro_json_schema_to_python_class()`](#convert_mashumaro_json_schema_to_python_class) | Generate a model class based on the provided JSON Schema. |
| [`dataclass_from_dict()`](#dataclass_from_dict) | Utility function to construct a dataclass object from dict. |
| [`generate_attribute_list_from_dataclass_json()`](#generate_attribute_list_from_dataclass_json) |  |
| [`generate_attribute_list_from_dataclass_json_mixin()`](#generate_attribute_list_from_dataclass_json_mixin) |  |
| [`get_batch_size()`](#get_batch_size) |  |
| [`get_underlying_type()`](#get_underlying_type) | Return the underlying type for annotated types or the type itself. |
| [`is_annotated()`](#is_annotated) |  |
| [`modify_literal_uris()`](#modify_literal_uris) | Modifies the literal object recursively to replace the URIs with the native paths in case they are of. |
| [`strict_type_hint_matching()`](#strict_type_hint_matching) | Try to be smarter about guessing the type of the input (and hence the transformer). |


### Variables

| Property | Type | Description |
|-|-|-|
| `BoolTransformer` | `SimpleTransformer` |  |
| `CACHE_KEY_METADATA` | `str` |  |
| `DEFINITIONS` | `str` |  |
| `DateTransformer` | `SimpleTransformer` |  |
| `DatetimeTransformer` | `SimpleTransformer` |  |
| `FLYTE_USE_OLD_DC_FORMAT` | `str` |  |
| `FloatTransformer` | `SimpleTransformer` |  |
| `IntTransformer` | `SimpleTransformer` |  |
| `MESSAGEPACK` | `str` |  |
| `NoneTransformer` | `SimpleTransformer` |  |
| `SERIALIZATION_FORMAT` | `str` |  |
| `StrTransformer` | `SimpleTransformer` |  |
| `T` | `TypeVar` |  |
| `TITLE` | `str` |  |
| `TimedeltaTransformer` | `SimpleTransformer` |  |

## Methods

#### convert_marshmallow_json_schema_to_python_class()

```python
def convert_marshmallow_json_schema_to_python_class(
    schema: dict,
    schema_name: typing.Any,
) -> type
```
Generate a model class based on the provided JSON Schema


| Parameter | Type | Description |
|-|-|-|
| `schema` | `dict` | dict representing valid JSON schema |
| `schema_name` | `typing.Any` | dataclass name of return type |

#### convert_mashumaro_json_schema_to_python_class()

```python
def convert_mashumaro_json_schema_to_python_class(
    schema: dict,
    schema_name: typing.Any,
) -> type
```
Generate a model class based on the provided JSON Schema


| Parameter | Type | Description |
|-|-|-|
| `schema` | `dict` | dict representing valid JSON schema |
| `schema_name` | `typing.Any` | dataclass name of return type |

#### dataclass_from_dict()

```python
def dataclass_from_dict(
    cls: type,
    src: typing.Dict[str, typing.Any],
) -> typing.Any
```
Utility function to construct a dataclass object from dict


| Parameter | Type | Description |
|-|-|-|
| `cls` | `type` | |
| `src` | `typing.Dict[str, typing.Any]` | |

#### generate_attribute_list_from_dataclass_json()

```python
def generate_attribute_list_from_dataclass_json(
    schema: dict,
    schema_name: typing.Any,
)
```
| Parameter | Type | Description |
|-|-|-|
| `schema` | `dict` | |
| `schema_name` | `typing.Any` | |

#### generate_attribute_list_from_dataclass_json_mixin()

```python
def generate_attribute_list_from_dataclass_json_mixin(
    schema: typing.Dict[str, typing.Any],
    schema_name: typing.Any,
)
```
| Parameter | Type | Description |
|-|-|-|
| `schema` | `typing.Dict[str, typing.Any]` | |
| `schema_name` | `typing.Any` | |

#### get_batch_size()

```python
def get_batch_size(
    t: Type,
) -> Optional[int]
```
| Parameter | Type | Description |
|-|-|-|
| `t` | `Type` | |

#### get_underlying_type()

```python
def get_underlying_type(
    t: Type,
) -> Type
```
Return the underlying type for annotated types or the type itself


| Parameter | Type | Description |
|-|-|-|
| `t` | `Type` | |

#### is_annotated()

```python
def is_annotated(
    t: Type,
) -> bool
```
| Parameter | Type | Description |
|-|-|-|
| `t` | `Type` | |

#### modify_literal_uris()

```python
def modify_literal_uris(
    lit: Literal,
)
```
Modifies the literal object recursively to replace the URIs with the native paths in case they are of
type "flyte://"


| Parameter | Type | Description |
|-|-|-|
| `lit` | `Literal` | |

#### strict_type_hint_matching()

```python
def strict_type_hint_matching(
    input_val: typing.Any,
    target_literal_type: LiteralType,
) -> typing.Type
```
Try to be smarter about guessing the type of the input (and hence the transformer).
If the literal type from the transformer for type(v), matches the literal type of the interface, then we
can use type(). Otherwise, fall back to guess python type from the literal type.
Raises ValueError, like in case of [1,2,3] type() will just give `list`, which won't work.
Raises ValueError also if the transformer found for the raw type doesn't have a literal type match.


| Parameter | Type | Description |
|-|-|-|
| `input_val` | `typing.Any` | |
| `target_literal_type` | `LiteralType` | |

