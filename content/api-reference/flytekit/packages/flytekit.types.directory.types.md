---
title: flytekit.types.directory.types
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.types.directory.types

## Directory

### Classes

| Class | Description |
|-|-|
| [`Any`](.././flytekit.types.directory.types#flytekittypesdirectorytypesany) | Special type indicating an unconstrained type. |
| [`AsyncTypeTransformer`](.././flytekit.types.directory.types#flytekittypesdirectorytypesasynctypetransformer) | Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`Binary`](.././flytekit.types.directory.types#flytekittypesdirectorytypesbinary) |  |
| [`Blob`](.././flytekit.types.directory.types#flytekittypesdirectorytypesblob) |  |
| [`BlobMetadata`](.././flytekit.types.directory.types#flytekittypesdirectorytypesblobmetadata) | This is metadata for the Blob literal. |
| [`BlobType`](.././flytekit.types.directory.types#flytekittypesdirectorytypesblobtype) | This type represents offloaded data and is typically used for things like files. |
| [`DataClassJsonMixin`](.././flytekit.types.directory.types#flytekittypesdirectorytypesdataclassjsonmixin) | DataClassJsonMixin is an ABC that functions as a Mixin. |
| [`FileExt`](.././flytekit.types.directory.types#flytekittypesdirectorytypesfileext) | Used for annotating file extension types of FlyteFile. |
| [`FlyteContext`](.././flytekit.types.directory.types#flytekittypesdirectorytypesflytecontext) | This is an internal-facing context object, that most users will not have to deal with. |
| [`FlyteContextManager`](.././flytekit.types.directory.types#flytekittypesdirectorytypesflytecontextmanager) | FlyteContextManager manages the execution context within Flytekit. |
| [`FlyteDirToMultipartBlobTransformer`](.././flytekit.types.directory.types#flytekittypesdirectorytypesflytedirtomultipartblobtransformer) | This transformer handles conversion between the Python native FlyteDirectory class defined above, and the Flyte. |
| [`FlyteDirectory`](.././flytekit.types.directory.types#flytekittypesdirectorytypesflytedirectory) |  |
| [`FlyteFile`](.././flytekit.types.directory.types#flytekittypesdirectorytypesflytefile) |  |
| [`Literal`](.././flytekit.types.directory.types#flytekittypesdirectorytypesliteral) |  |
| [`LiteralType`](.././flytekit.types.directory.types#flytekittypesdirectorytypesliteraltype) |  |
| [`Path`](.././flytekit.types.directory.types#flytekittypesdirectorytypespath) | PurePath subclass that can make system calls. |
| [`Scalar`](.././flytekit.types.directory.types#flytekittypesdirectorytypesscalar) |  |
| [`SerializableType`](.././flytekit.types.directory.types#flytekittypesdirectorytypesserializabletype) |  |
| [`Struct`](.././flytekit.types.directory.types#flytekittypesdirectorytypesstruct) | A ProtocolMessage. |
| [`TypeEngine`](.././flytekit.types.directory.types#flytekittypesdirectorytypestypeengine) | Core Extensible TypeEngine of Flytekit. |
| [`UUID`](.././flytekit.types.directory.types#flytekittypesdirectorytypesuuid) | Instances of the UUID class represent UUIDs as specified in RFC 4122. |
| [`partial`](.././flytekit.types.directory.types#flytekittypesdirectorytypespartial) | Create a new function with partial application of the given arguments. |

### Errors

| Exception | Description |
|-|-|
| [`FlyteAssertion`](.././flytekit.types.directory.types#flytekittypesdirectorytypesflyteassertion) | Assertion failed. |
| [`TypeTransformerFailedError`](.././flytekit.types.directory.types#flytekittypesdirectorytypestypetransformerfailederror) | Inappropriate argument type. |

### Methods

| Method | Description |
|-|-|
| [`config()`](#config) |  |
| [`dataclass()`](#dataclass) | Add dunder methods based on the fields defined in the class. |
| [`field()`](#field) | Return an object to identify dataclass fields. |
| [`get_batch_size()`](#get_batch_size) |  |
| [`get_protocol()`](#get_protocol) |  |
| [`model_serializer()`](#model_serializer) | Decorator that enables custom model serialization. |
| [`model_validator()`](#model_validator) | Usage docs: https://docs. |
| [`noop()`](#noop) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `MESSAGEPACK` | `str` |  |
| `T` | `TypeVar` |  |
| `annotations` | `_Feature` |  |

## Methods

#### config()

```python
def config(
    metadata: dict,
    encoder: typing.Callable,
    decoder: typing.Callable,
    mm_field: marshmallow.fields.Field,
    letter_case: typing.Union[typing.Callable[[str], str], dataclasses_json.cfg.LetterCase, NoneType],
    undefined: typing.Union[str, dataclasses_json.undefined.Undefined, NoneType],
    field_name: str,
    exclude: typing.Union[typing.Callable[[str, ~T], bool], dataclasses_json.cfg.Exclude, NoneType],
) -> typing.Dict[str, dict]
```
| Parameter | Type |
|-|-|
| `metadata` | `dict` |
| `encoder` | `typing.Callable` |
| `decoder` | `typing.Callable` |
| `mm_field` | `marshmallow.fields.Field` |
| `letter_case` | `typing.Union[typing.Callable[[str], str], dataclasses_json.cfg.LetterCase, NoneType]` |
| `undefined` | `typing.Union[str, dataclasses_json.undefined.Undefined, NoneType]` |
| `field_name` | `str` |
| `exclude` | `typing.Union[typing.Callable[[str, ~T], bool], dataclasses_json.cfg.Exclude, NoneType]` |

#### dataclass()

```python
def dataclass(
    cls,
    init,
    repr,
    eq,
    order,
    unsafe_hash,
    frozen,
    match_args,
    kw_only,
    slots,
    weakref_slot,
)
```
Add dunder methods based on the fields defined in the class.

Examines PEP 526 __annotations__ to determine fields.

If init is true, an __init__() method is added to the class. If repr
is true, a __repr__() method is added. If order is true, rich
comparison dunder methods are added. If unsafe_hash is true, a
__hash__() method is added. If frozen is true, fields may not be
assigned to after instance creation. If match_args is true, the
__match_args__ tuple is added. If kw_only is true, then by default
all fields are keyword-only. If slots is true, a new class with a
__slots__ attribute is returned.


| Parameter | Type |
|-|-|
| `cls` |  |
| `init` |  |
| `repr` |  |
| `eq` |  |
| `order` |  |
| `unsafe_hash` |  |
| `frozen` |  |
| `match_args` |  |
| `kw_only` |  |
| `slots` |  |
| `weakref_slot` |  |

#### field()

```python
def field(
    default,
    default_factory,
    init,
    repr,
    hash,
    compare,
    metadata,
    kw_only,
)
```
Return an object to identify dataclass fields.

default is the default value of the field.  default_factory is a
0-argument function called to initialize a field's value.  If init
is true, the field will be a parameter to the class's __init__()
function.  If repr is true, the field will be included in the
object's repr().  If hash is true, the field will be included in the
object's hash().  If compare is true, the field will be used in
comparison functions.  metadata, if specified, must be a mapping
which is stored but not otherwise examined by dataclass.  If kw_only
is true, the field will become a keyword-only parameter to
__init__().

It is an error to specify both default and default_factory.


| Parameter | Type |
|-|-|
| `default` |  |
| `default_factory` |  |
| `init` |  |
| `repr` |  |
| `hash` |  |
| `compare` |  |
| `metadata` |  |
| `kw_only` |  |

#### get_batch_size()

```python
def get_batch_size(
    t: Type,
) -> Optional[int]
```
| Parameter | Type |
|-|-|
| `t` | `Type` |

#### get_protocol()

```python
def get_protocol(
    url: str,
) -> str
```
| Parameter | Type |
|-|-|
| `url` | `str` |

#### model_serializer()

```python
def model_serializer(
    f: _ModelPlainSerializerT | _ModelWrapSerializerT | None,
    mode: Literal['plain', 'wrap'],
    when_used: WhenUsed,
    return_type: Any,
) -> _ModelPlainSerializerT | Callable[[_ModelWrapSerializerT], _ModelWrapSerializerT] | Callable[[_ModelPlainSerializerT], _ModelPlainSerializerT]
```
Decorator that enables custom model serialization.

This is useful when a model need to be serialized in a customized manner, allowing for flexibility beyond just specific fields.

An example would be to serialize temperature to the same temperature scale, such as degrees Celsius.

```python
from typing import Literal

from pydantic import BaseModel, model_serializer

class TemperatureModel(BaseModel):
unit: Literal['C', 'F']
value: int

@model_serializer()
def serialize_model(self):
if self.unit == 'F':
return {'unit': 'C', 'value': int((self.value - 32) / 1.8)}
return {'unit': self.unit, 'value': self.value}

temperature = TemperatureModel(unit='F', value=212)
print(temperature.model_dump())
#> {'unit': 'C', 'value': 100}
```

Two signatures are supported for `mode='plain'`, which is the default:

- `(self)`
- `(self, info: SerializationInfo)`

And two other signatures for `mode='wrap'`:

- `(self, nxt: SerializerFunctionWrapHandler)`
- `(self, nxt: SerializerFunctionWrapHandler, info: SerializationInfo)`

See [Custom serializers](../concepts/serialization.md#custom-serializers) for more information.



| Parameter | Type |
|-|-|
| `f` | `_ModelPlainSerializerT \| _ModelWrapSerializerT \| None` |
| `mode` | `Literal['plain', 'wrap']` |
| `when_used` | `WhenUsed` |
| `return_type` | `Any` |

#### model_validator()

```python
def model_validator(
    mode: Literal['wrap', 'before', 'after'],
) -> Any
```
Usage docs: https://docs.pydantic.dev/2.10/concepts/validators/#model-validators

Decorate model methods for validation purposes.

Example usage:
```python
from typing_extensions import Self

from pydantic import BaseModel, ValidationError, model_validator

class Square(BaseModel):
width: float
height: float

@model_validator(mode='after')
def verify_square(self) -> Self:
if self.width != self.height:
raise ValueError('width and height do not match')
return self

s = Square(width=1, height=1)
print(repr(s))
#> Square(width=1.0, height=1.0)

try:
Square(width=1, height=2)
except ValidationError as e:
print(e)
'''
1 validation error for Square
Value error, width and height do not match [type=value_error, input_value={'width': 1, 'height': 2}, input_type=dict]
'''
```

For more in depth examples, see [Model Validators](../concepts/validators.md#model-validators).



| Parameter | Type |
|-|-|
| `mode` | `Literal['wrap', 'before', 'after']` |

#### noop()

```python
def noop()
```
## flytekit.types.directory.types.Any

Special type indicating an unconstrained type.

- Any is compatible with every type.
- Any assumed to have all methods.
- All values assumed to be instances of Any.

Note that all the above statements are true from the point of view of
static type checkers. At runtime, Any should not be used with instance
checks.


## flytekit.types.directory.types.AsyncTypeTransformer

Base transformer type that should be implemented for every python native type that can be handled by flytekit


```python
class AsyncTypeTransformer(
    name: str,
    t: Type[T],
    enable_type_assertions: bool,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `t` | `Type[T]` |
| `enable_type_assertions` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`async_to_literal()`](#async_to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`async_to_python_value()`](#async_to_python_value) | Converts the given Literal to a Python Type. |
| [`from_binary_idl()`](#from_binary_idl) | This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access. |
| [`from_generic_idl()`](#from_generic_idl) | TODO: Support all Flyte Types. |
| [`get_literal_type()`](#get_literal_type) | Converts the python type to a Flyte LiteralType. |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type. |
| [`isinstance_generic()`](#isinstance_generic) |  |
| [`to_html()`](#to_html) | Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div. |
| [`to_literal()`](#to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`to_python_value()`](#to_python_value) | Converts the given Literal to a Python Type. |


#### assert_type()

```python
def assert_type(
    t: Type[T],
    v: T,
)
```
| Parameter | Type |
|-|-|
| `t` | `Type[T]` |
| `v` | `T` |

#### async_to_literal()

```python
def async_to_literal(
    ctx: FlyteContext,
    python_val: T,
    python_type: Type[T],
    expected: LiteralType,
) -> Literal
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `T` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### async_to_python_value()

```python
def async_to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
) -> Optional[T]
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[T]` |

#### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: Binary,
    expected_python_type: Type[T],
) -> Optional[T]
```
This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access.｀

For untyped dict, dataclass, and pydantic basemodel:
Life Cycle (Untyped Dict as example):
python val -> msgpack bytes -> binary literal scalar -> msgpack bytes -> python val
(to_literal)                             (from_binary_idl)

For attribute access:
Life Cycle:
python val -> msgpack bytes -> binary literal scalar -> resolved golang value -> binary literal scalar -> msgpack bytes -> python val
(to_literal)                            (propeller attribute access)                       (from_binary_idl)


| Parameter | Type |
|-|-|
| `binary_idl_object` | `Binary` |
| `expected_python_type` | `Type[T]` |

#### from_generic_idl()

```python
def from_generic_idl(
    generic: Struct,
    expected_python_type: Type[T],
) -> Optional[T]
```
TODO: Support all Flyte Types.
This is for dataclass attribute access from input created from the Flyte Console.

Note:
- This can be removed in the future when the Flyte Console support generate Binary IDL Scalar as input.


| Parameter | Type |
|-|-|
| `generic` | `Struct` |
| `expected_python_type` | `Type[T]` |

#### get_literal_type()

```python
def get_literal_type(
    t: Type[T],
) -> LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type |
|-|-|
| `t` | `Type[T]` |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> Type[T]
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type |
|-|-|
| `literal_type` | `LiteralType` |

#### isinstance_generic()

```python
def isinstance_generic(
    obj,
    generic_alias,
)
```
| Parameter | Type |
|-|-|
| `obj` |  |
| `generic_alias` |  |

#### to_html()

```python
def to_html(
    ctx: FlyteContext,
    python_val: T,
    expected_python_type: Type[T],
) -> str
```
Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `T` |
| `expected_python_type` | `Type[T]` |

#### to_literal()

```python
def to_literal(
    ctx: FlyteContext,
    python_val: typing.Any,
    python_type: Type[T],
    expected: LiteralType,
) -> Literal
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `typing.Any` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
) -> Optional[T]
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[T]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_async` |  |  |
| `name` |  |  |
| `python_type` |  | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` |  | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

## flytekit.types.directory.types.Binary

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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> Binary
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
| `tag` |  |  |
| `value` |  |  |

## flytekit.types.directory.types.Blob

```python
class Blob(
    metadata,
    uri,
)
```
This literal model is used to represent binary data offloaded to some storage location which is
identifiable with a unique string. See :py:class:`flytekit.FlyteFile` as an example.



| Parameter | Type |
|-|-|
| `metadata` |  |
| `uri` |  |

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
) -> Blob
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
| `is_empty` |  |  |
| `metadata` |  |  |
| `uri` |  |  |

## flytekit.types.directory.types.BlobMetadata

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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> BlobMetadata
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
| `is_empty` |  |  |
| `type` |  |  |

## flytekit.types.directory.types.BlobType

This type represents offloaded data and is typically used for things like files.


```python
class BlobType(
    format,
    dimensionality,
)
```
| Parameter | Type |
|-|-|
| `format` |  |
| `dimensionality` |  |

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
) -> BlobType
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
| `dimensionality` |  | {{< multiline >}}An integer from BlobType.BlobDimensionality enum
{{< /multiline >}} |
| `format` |  | {{< multiline >}}A string describing the format of the underlying blob data.
{{< /multiline >}} |
| `is_empty` |  |  |

## flytekit.types.directory.types.DataClassJsonMixin

DataClassJsonMixin is an ABC that functions as a Mixin.

As with other ABCs, it should not be instantiated directly.


### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`schema()`](#schema) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


#### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
) -> ~A
```
| Parameter | Type |
|-|-|
| `kvs` | `typing.Union[dict, list, str, int, float, bool, NoneType]` |
| `infer_missing` |  |

#### from_json()

```python
def from_json(
    s: typing.Union[str, bytes, bytearray],
    parse_float,
    parse_int,
    parse_constant,
    infer_missing,
    kw,
) -> ~A
```
| Parameter | Type |
|-|-|
| `s` | `typing.Union[str, bytes, bytearray]` |
| `parse_float` |  |
| `parse_int` |  |
| `parse_constant` |  |
| `infer_missing` |  |
| `kw` |  |

#### schema()

```python
def schema(
    infer_missing: bool,
    only,
    exclude,
    many: bool,
    context,
    load_only,
    dump_only,
    partial: bool,
    unknown,
) -> SchemaType[A]
```
| Parameter | Type |
|-|-|
| `infer_missing` | `bool` |
| `only` |  |
| `exclude` |  |
| `many` | `bool` |
| `context` |  |
| `load_only` |  |
| `dump_only` |  |
| `partial` | `bool` |
| `unknown` |  |

#### to_dict()

```python
def to_dict(
    encode_json,
) -> typing.Dict[str, typing.Union[dict, list, str, int, float, bool, NoneType]]
```
| Parameter | Type |
|-|-|
| `encode_json` |  |

#### to_json()

```python
def to_json(
    skipkeys: bool,
    ensure_ascii: bool,
    check_circular: bool,
    allow_nan: bool,
    indent: typing.Union[int, str, NoneType],
    separators: typing.Tuple[str, str],
    default: typing.Callable,
    sort_keys: bool,
    kw,
) -> str
```
| Parameter | Type |
|-|-|
| `skipkeys` | `bool` |
| `ensure_ascii` | `bool` |
| `check_circular` | `bool` |
| `allow_nan` | `bool` |
| `indent` | `typing.Union[int, str, NoneType]` |
| `separators` | `typing.Tuple[str, str]` |
| `default` | `typing.Callable` |
| `sort_keys` | `bool` |
| `kw` |  |

## flytekit.types.directory.types.FileExt

Used for annotating file extension types of FlyteFile.
This is useful for extensions that have periods in them, e.g., "tar.gz".

Example:
TAR_GZ = Annotated[str, FileExt("tar.gz")]


```python
class FileExt(
    ext: str,
)
```
| Parameter | Type |
|-|-|
| `ext` | `str` |

### Methods

| Method | Description |
|-|-|
| [`check_and_convert_to_str()`](#check_and_convert_to_str) |  |


#### check_and_convert_to_str()

```python
def check_and_convert_to_str(
    item: typing.Union[typing.Type, str],
) -> str
```
| Parameter | Type |
|-|-|
| `item` | `typing.Union[typing.Type, str]` |

## flytekit.types.directory.types.FlyteAssertion

Assertion failed.


```python
class FlyteAssertion(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.types.directory.types.FlyteContext

This is an internal-facing context object, that most users will not have to deal with. It's essentially a globally
available grab bag of settings and objects that allows flytekit to do things like convert complex types, run and
compile workflows, serialize Flyte entities, etc.

Even though this object as a ``current_context`` function on it, it should not be called directly. Please use the
:py:class:`flytekit.FlyteContextManager` object instead.

Please do not confuse this object with the :py:class:`flytekit.ExecutionParameters` object.


```python
class FlyteContext(
    file_access: FileAccessProvider,
    level: int,
    flyte_client: Optional['friendly_client.SynchronousFlyteClient'],
    compilation_state: Optional[CompilationState],
    execution_state: Optional[ExecutionState],
    serialization_settings: Optional[SerializationSettings],
    in_a_condition: bool,
    origin_stackframe: Optional[traceback.FrameSummary],
    output_metadata_tracker: Optional[OutputMetadataTracker],
    worker_queue: Optional[Controller],
)
```
| Parameter | Type |
|-|-|
| `file_access` | `FileAccessProvider` |
| `level` | `int` |
| `flyte_client` | `Optional['friendly_client.SynchronousFlyteClient']` |
| `compilation_state` | `Optional[CompilationState]` |
| `execution_state` | `Optional[ExecutionState]` |
| `serialization_settings` | `Optional[SerializationSettings]` |
| `in_a_condition` | `bool` |
| `origin_stackframe` | `Optional[traceback.FrameSummary]` |
| `output_metadata_tracker` | `Optional[OutputMetadataTracker]` |
| `worker_queue` | `Optional[Controller]` |

### Methods

| Method | Description |
|-|-|
| [`current_context()`](#current_context) | This method exists only to maintain backwards compatibility. |
| [`enter_conditional_section()`](#enter_conditional_section) |  |
| [`get_deck()`](#get_deck) | Returns the deck that was created as part of the last execution. |
| [`get_origin_stackframe_repr()`](#get_origin_stackframe_repr) |  |
| [`new_builder()`](#new_builder) |  |
| [`new_compilation_state()`](#new_compilation_state) | Creates and returns a default compilation state. |
| [`new_execution_state()`](#new_execution_state) | Creates and returns a new default execution state. |
| [`set_stackframe()`](#set_stackframe) |  |
| [`with_client()`](#with_client) |  |
| [`with_compilation_state()`](#with_compilation_state) |  |
| [`with_execution_state()`](#with_execution_state) |  |
| [`with_file_access()`](#with_file_access) |  |
| [`with_new_compilation_state()`](#with_new_compilation_state) |  |
| [`with_output_metadata_tracker()`](#with_output_metadata_tracker) |  |
| [`with_serialization_settings()`](#with_serialization_settings) |  |
| [`with_worker_queue()`](#with_worker_queue) |  |


#### current_context()

```python
def current_context()
```
This method exists only to maintain backwards compatibility. Please use
``FlyteContextManager.current_context()`` instead.

Users of flytekit should be wary not to confuse the object returned from this function
with :py:func:`flytekit.current_context`


#### enter_conditional_section()

```python
def enter_conditional_section()
```
#### get_deck()

```python
def get_deck()
```
Returns the deck that was created as part of the last execution.

The return value depends on the execution environment. In a notebook, the return value is compatible with
IPython.display and should be rendered in the notebook.

.. code-block:: python

with flytekit.new_context() as ctx:
my_task(...)
ctx.get_deck()

OR if you wish to explicitly display

.. code-block:: python

from IPython import display
display(ctx.get_deck())


#### get_origin_stackframe_repr()

```python
def get_origin_stackframe_repr()
```
#### new_builder()

```python
def new_builder()
```
#### new_compilation_state()

```python
def new_compilation_state(
    prefix: str,
) -> CompilationState
```
Creates and returns a default compilation state. For most of the code this should be the entrypoint
of compilation, otherwise the code should always uses - with_compilation_state


| Parameter | Type |
|-|-|
| `prefix` | `str` |

#### new_execution_state()

```python
def new_execution_state(
    working_dir: Optional[os.PathLike],
) -> ExecutionState
```
Creates and returns a new default execution state. This should be used at the entrypoint of execution,
in all other cases it is preferable to use with_execution_state


| Parameter | Type |
|-|-|
| `working_dir` | `Optional[os.PathLike]` |

#### set_stackframe()

```python
def set_stackframe(
    s: traceback.FrameSummary,
)
```
| Parameter | Type |
|-|-|
| `s` | `traceback.FrameSummary` |

#### with_client()

```python
def with_client(
    c: SynchronousFlyteClient,
) -> Builder
```
| Parameter | Type |
|-|-|
| `c` | `SynchronousFlyteClient` |

#### with_compilation_state()

```python
def with_compilation_state(
    c: CompilationState,
) -> Builder
```
| Parameter | Type |
|-|-|
| `c` | `CompilationState` |

#### with_execution_state()

```python
def with_execution_state(
    es: ExecutionState,
) -> Builder
```
| Parameter | Type |
|-|-|
| `es` | `ExecutionState` |

#### with_file_access()

```python
def with_file_access(
    fa: FileAccessProvider,
) -> Builder
```
| Parameter | Type |
|-|-|
| `fa` | `FileAccessProvider` |

#### with_new_compilation_state()

```python
def with_new_compilation_state()
```
#### with_output_metadata_tracker()

```python
def with_output_metadata_tracker(
    t: OutputMetadataTracker,
) -> Builder
```
| Parameter | Type |
|-|-|
| `t` | `OutputMetadataTracker` |

#### with_serialization_settings()

```python
def with_serialization_settings(
    ss: SerializationSettings,
) -> Builder
```
| Parameter | Type |
|-|-|
| `ss` | `SerializationSettings` |

#### with_worker_queue()

```python
def with_worker_queue(
    wq: Controller,
) -> Builder
```
| Parameter | Type |
|-|-|
| `wq` | `Controller` |

### Properties

| Property | Type | Description |
|-|-|-|
| `user_space_params` |  |  |

## flytekit.types.directory.types.FlyteContextManager

FlyteContextManager manages the execution context within Flytekit. It holds global state of either compilation
or Execution. It is not thread-safe and can only be run as a single threaded application currently.
Context's within Flytekit is useful to manage compilation state and execution state. Refer to ``CompilationState``
and ``ExecutionState`` for more information. FlyteContextManager provides a singleton stack to manage these contexts.

Typical usage is

.. code-block:: python

FlyteContextManager.initialize()
with FlyteContextManager.with_context(o) as ctx:
pass

# If required - not recommended you can use
FlyteContextManager.push_context()
# but correspondingly a pop_context should be called
FlyteContextManager.pop_context()


### Methods

| Method | Description |
|-|-|
| [`add_signal_handler()`](#add_signal_handler) |  |
| [`current_context()`](#current_context) |  |
| [`get_origin_stackframe()`](#get_origin_stackframe) |  |
| [`initialize()`](#initialize) | Re-initializes the context and erases the entire context. |
| [`pop_context()`](#pop_context) |  |
| [`push_context()`](#push_context) |  |
| [`size()`](#size) |  |
| [`with_context()`](#with_context) |  |


#### add_signal_handler()

```python
def add_signal_handler(
    handler: typing.Callable[[int, FrameType], typing.Any],
)
```
| Parameter | Type |
|-|-|
| `handler` | `typing.Callable[[int, FrameType], typing.Any]` |

#### current_context()

```python
def current_context()
```
#### get_origin_stackframe()

```python
def get_origin_stackframe(
    limit,
) -> traceback.FrameSummary
```
| Parameter | Type |
|-|-|
| `limit` |  |

#### initialize()

```python
def initialize()
```
Re-initializes the context and erases the entire context


#### pop_context()

```python
def pop_context()
```
#### push_context()

```python
def push_context(
    ctx: FlyteContext,
    f: Optional[traceback.FrameSummary],
) -> FlyteContext
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `f` | `Optional[traceback.FrameSummary]` |

#### size()

```python
def size()
```
#### with_context()

```python
def with_context(
    b: FlyteContext.Builder,
) -> Generator[FlyteContext, None, None]
```
| Parameter | Type |
|-|-|
| `b` | `FlyteContext.Builder` |

## flytekit.types.directory.types.FlyteDirToMultipartBlobTransformer

This transformer handles conversion between the Python native FlyteDirectory class defined above, and the Flyte
IDL literal/type of Multipart Blob. Please see the FlyteDirectory comments for additional information.

.. caution:

The transformer will not check if the given path is actually a directory. This is because the path could be
a remote reference.


```python
def FlyteDirToMultipartBlobTransformer()
```
### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`async_to_literal()`](#async_to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`async_to_python_value()`](#async_to_python_value) | Converts the given Literal to a Python Type. |
| [`dict_to_flyte_directory()`](#dict_to_flyte_directory) |  |
| [`from_binary_idl()`](#from_binary_idl) | If the input is from flytekit, the Life Cycle will be as follows:. |
| [`from_generic_idl()`](#from_generic_idl) | If the input is from Flyte Console, the Life Cycle will be as follows:. |
| [`get_format()`](#get_format) |  |
| [`get_literal_type()`](#get_literal_type) | Converts the python type to a Flyte LiteralType. |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type. |
| [`isinstance_generic()`](#isinstance_generic) |  |
| [`to_html()`](#to_html) | Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div. |
| [`to_literal()`](#to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`to_python_value()`](#to_python_value) | Converts the given Literal to a Python Type. |


#### assert_type()

```python
def assert_type(
    t: typing.Type[FlyteDirectory],
    v: typing.Union[FlyteDirectory, os.PathLike, str],
)
```
| Parameter | Type |
|-|-|
| `t` | `typing.Type[FlyteDirectory]` |
| `v` | `typing.Union[FlyteDirectory, os.PathLike, str]` |

#### async_to_literal()

```python
def async_to_literal(
    ctx: FlyteContext,
    python_val: FlyteDirectory,
    python_type: typing.Type[FlyteDirectory],
    expected: LiteralType,
) -> Literal
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `FlyteDirectory` |
| `python_type` | `typing.Type[FlyteDirectory]` |
| `expected` | `LiteralType` |

#### async_to_python_value()

```python
def async_to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: typing.Type[FlyteDirectory],
) -> FlyteDirectory
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `typing.Type[FlyteDirectory]` |

#### dict_to_flyte_directory()

```python
def dict_to_flyte_directory(
    dict_obj: typing.Dict[str, str],
    expected_python_type: typing.Type[FlyteDirectory],
) -> FlyteDirectory
```
| Parameter | Type |
|-|-|
| `dict_obj` | `typing.Dict[str, str]` |
| `expected_python_type` | `typing.Type[FlyteDirectory]` |

#### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: Binary,
    expected_python_type: typing.Type[FlyteDirectory],
) -> FlyteDirectory
```
If the input is from flytekit, the Life Cycle will be as follows:

Life Cycle:
binary IDL                 -> resolved binary         -> bytes                   -> expected Python object
(flytekit customized          (propeller processing)     (flytekit binary IDL)      (flytekit customized
serialization)                                                                       deserialization)

Example Code:
@dataclass
class DC:
fd: FlyteDirectory

@workflow
def wf(dc: DC):
t_fd(dc.fd)

Note:
- The deserialization is the same as put a flyte directory in a dataclass, which will deserialize by the mashumaro's API.

Related PR:
- Title: Override Dataclass Serialization/Deserialization Behavior for FlyteTypes via Mashumaro
- Link: https://github.com/flyteorg/flytekit/pull/2554


| Parameter | Type |
|-|-|
| `binary_idl_object` | `Binary` |
| `expected_python_type` | `typing.Type[FlyteDirectory]` |

#### from_generic_idl()

```python
def from_generic_idl(
    generic: Struct,
    expected_python_type: typing.Type[FlyteDirectory],
) -> FlyteDirectory
```
If the input is from Flyte Console, the Life Cycle will be as follows:

Life Cycle:
json str            -> protobuf struct         -> resolved protobuf struct   -> expected Python object
(console user input)   (console output)           (propeller)                   (flytekit customized deserialization)

Example Code:
@dataclass
class DC:
fd: FlyteDirectory

@workflow
def wf(dc: DC):
t_fd(dc.fd)

Note:
- The deserialization is the same as put a flyte directory in a dataclass, which will deserialize by the mashumaro's API.

Related PR:
- Title: Override Dataclass Serialization/Deserialization Behavior for FlyteTypes via Mashumaro
- Link: https://github.com/flyteorg/flytekit/pull/2554


| Parameter | Type |
|-|-|
| `generic` | `Struct` |
| `expected_python_type` | `typing.Type[FlyteDirectory]` |

#### get_format()

```python
def get_format(
    t: typing.Type[FlyteDirectory],
) -> str
```
| Parameter | Type |
|-|-|
| `t` | `typing.Type[FlyteDirectory]` |

#### get_literal_type()

```python
def get_literal_type(
    t: typing.Type[FlyteDirectory],
) -> LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type |
|-|-|
| `t` | `typing.Type[FlyteDirectory]` |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> typing.Type[FlyteDirectory[typing.Any]]
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type |
|-|-|
| `literal_type` | `LiteralType` |

#### isinstance_generic()

```python
def isinstance_generic(
    obj,
    generic_alias,
)
```
| Parameter | Type |
|-|-|
| `obj` |  |
| `generic_alias` |  |

#### to_html()

```python
def to_html(
    ctx: FlyteContext,
    python_val: T,
    expected_python_type: Type[T],
) -> str
```
Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `T` |
| `expected_python_type` | `Type[T]` |

#### to_literal()

```python
def to_literal(
    ctx: FlyteContext,
    python_val: typing.Any,
    python_type: Type[T],
    expected: LiteralType,
) -> Literal
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `typing.Any` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
) -> Optional[T]
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[T]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_async` |  |  |
| `name` |  |  |
| `python_type` |  | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` |  | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

## flytekit.types.directory.types.FlyteDirectory

```python
class FlyteDirectory(
    path: typing.Union[str, os.PathLike],
    downloader: typing.Optional[typing.Callable],
    remote_directory: typing.Optional[typing.Union[os.PathLike, str, typing.Literal[False]]],
)
```
| Parameter | Type |
|-|-|
| `path` | `typing.Union[str, os.PathLike]` |
| `downloader` | `typing.Optional[typing.Callable]` |
| `remote_directory` | `typing.Optional[typing.Union[os.PathLike, str, typing.Literal[False]]]` |

### Methods

| Method | Description |
|-|-|
| [`crawl()`](#crawl) | Crawl returns a generator of all files prefixed by any sub-folders under the given "FlyteDirectory". |
| [`deserialize_flyte_dir()`](#deserialize_flyte_dir) |  |
| [`download()`](#download) |  |
| [`extension()`](#extension) |  |
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`from_source()`](#from_source) | Create a new FlyteDirectory object with the remote source set to the input. |
| [`listdir()`](#listdir) | This function will list all files and folders in the given directory, but without downloading the contents. |
| [`new()`](#new) | Create a new FlyteDirectory object in current Flyte working directory. |
| [`new_dir()`](#new_dir) | This will create a new folder under the current folder. |
| [`new_file()`](#new_file) | This will create a new file under the current folder. |
| [`new_remote()`](#new_remote) | Create a new FlyteDirectory object using the currently configured default remote in the context (i. |
| [`schema()`](#schema) |  |
| [`serialize_flyte_dir()`](#serialize_flyte_dir) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


#### crawl()

```python
def crawl(
    maxdepth: typing.Optional[int],
    topdown: bool,
    kwargs,
) -> Generator[Tuple[typing.Union[str, os.PathLike[Any]], typing.Dict[Any, Any]], None, None]
```
Crawl returns a generator of all files prefixed by any sub-folders under the given "FlyteDirectory".
if details=True is passed, then it will return a dictionary as specified by fsspec.

Example:

>>> list(fd.crawl())
[("/base", "file1"), ("/base", "dir1/file1"), ("/base", "dir2/file1"), ("/base", "dir1/dir/file1")]

>>> list(x.crawl(detail=True))
[('/tmp/test', {'my-dir/ab.py': {'name': '/tmp/test/my-dir/ab.py', 'size': 0, 'type': 'file',
'created': 1677720780.2318847, 'islink': False, 'mode': 33188, 'uid': 501, 'gid': 0,
'mtime': 1677720780.2317934, 'ino': 1694329, 'nlink': 1}})]


| Parameter | Type |
|-|-|
| `maxdepth` | `typing.Optional[int]` |
| `topdown` | `bool` |
| `kwargs` | ``**kwargs`` |

#### deserialize_flyte_dir()

```python
def deserialize_flyte_dir(
    info,
) -> FlyteDirectory
```
| Parameter | Type |
|-|-|
| `info` |  |

#### download()

```python
def download()
```
#### extension()

```python
def extension()
```
#### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
) -> ~A
```
| Parameter | Type |
|-|-|
| `kvs` | `typing.Union[dict, list, str, int, float, bool, NoneType]` |
| `infer_missing` |  |

#### from_json()

```python
def from_json(
    s: typing.Union[str, bytes, bytearray],
    parse_float,
    parse_int,
    parse_constant,
    infer_missing,
    kw,
) -> ~A
```
| Parameter | Type |
|-|-|
| `s` | `typing.Union[str, bytes, bytearray]` |
| `parse_float` |  |
| `parse_int` |  |
| `parse_constant` |  |
| `infer_missing` |  |
| `kw` |  |

#### from_source()

```python
def from_source(
    source: str | os.PathLike,
) -> FlyteDirectory
```
Create a new FlyteDirectory object with the remote source set to the input


| Parameter | Type |
|-|-|
| `source` | `str \| os.PathLike` |

#### listdir()

```python
def listdir(
    directory: FlyteDirectory,
) -> typing.List[typing.Union[FlyteDirectory, FlyteFile]]
```
This function will list all files and folders in the given directory, but without downloading the contents.
In addition, it will return a list of FlyteFile and FlyteDirectory objects that have ability to lazily download the
contents of the file/folder. For example:

.. code-block:: python

entity = FlyteDirectory.listdir(directory)
for e in entity:
print("s3 object:", e.remote_source)
# s3 object: s3://test-flytedir/file1.txt
# s3 object: s3://test-flytedir/file2.txt
# s3 object: s3://test-flytedir/sub_dir

open(entity[0], "r")  # This will download the file to the local disk.
open(entity[0], "r")  # flytekit will read data from the local disk if you open it again.


| Parameter | Type |
|-|-|
| `directory` | `FlyteDirectory` |

#### new()

```python
def new(
    dirname: str | os.PathLike,
) -> FlyteDirectory
```
Create a new FlyteDirectory object in current Flyte working directory.


| Parameter | Type |
|-|-|
| `dirname` | `str \| os.PathLike` |

#### new_dir()

```python
def new_dir(
    name: typing.Optional[str],
) -> FlyteDirectory
```
This will create a new folder under the current folder.
If given a name, it will use the name given, otherwise it'll pick a random string.
Collisions are not checked.


| Parameter | Type |
|-|-|
| `name` | `typing.Optional[str]` |

#### new_file()

```python
def new_file(
    name: typing.Optional[str],
) -> FlyteFile
```
This will create a new file under the current folder.
If given a name, it will use the name given, otherwise it'll pick a random string.
Collisions are not checked.


| Parameter | Type |
|-|-|
| `name` | `typing.Optional[str]` |

#### new_remote()

```python
def new_remote(
    stem: typing.Optional[str],
    alt: typing.Optional[str],
) -> FlyteDirectory
```
Create a new FlyteDirectory object using the currently configured default remote in the context (i.e.
the raw_output_prefix configured in the current FileAccessProvider object in the context).
This is used if you explicitly have a folder somewhere that you want to create files under.
If you want to write a whole folder, you can let your task return a FlyteDirectory object,
and let flytekit handle the uploading.



| Parameter | Type |
|-|-|
| `stem` | `typing.Optional[str]` |
| `alt` | `typing.Optional[str]` |

#### schema()

```python
def schema(
    infer_missing: bool,
    only,
    exclude,
    many: bool,
    context,
    load_only,
    dump_only,
    partial: bool,
    unknown,
) -> SchemaType[A]
```
| Parameter | Type |
|-|-|
| `infer_missing` | `bool` |
| `only` |  |
| `exclude` |  |
| `many` | `bool` |
| `context` |  |
| `load_only` |  |
| `dump_only` |  |
| `partial` | `bool` |
| `unknown` |  |

#### serialize_flyte_dir()

```python
def serialize_flyte_dir()
```
#### to_dict()

```python
def to_dict(
    encode_json,
) -> typing.Dict[str, typing.Union[dict, list, str, int, float, bool, NoneType]]
```
| Parameter | Type |
|-|-|
| `encode_json` |  |

#### to_json()

```python
def to_json(
    skipkeys: bool,
    ensure_ascii: bool,
    check_circular: bool,
    allow_nan: bool,
    indent: typing.Union[int, str, NoneType],
    separators: typing.Tuple[str, str],
    default: typing.Callable,
    sort_keys: bool,
    kw,
) -> str
```
| Parameter | Type |
|-|-|
| `skipkeys` | `bool` |
| `ensure_ascii` | `bool` |
| `check_circular` | `bool` |
| `allow_nan` | `bool` |
| `indent` | `typing.Union[int, str, NoneType]` |
| `separators` | `typing.Tuple[str, str]` |
| `default` | `typing.Callable` |
| `sort_keys` | `bool` |
| `kw` |  |

### Properties

| Property | Type | Description |
|-|-|-|
| `downloaded` |  |  |
| `remote_directory` |  |  |
| `remote_source` |  | {{< multiline >}}If this is an input to a task, and the original path is s3://something, flytekit will download the
directory for the user. In case the user wants access to the original path, it will be here.
{{< /multiline >}} |
| `sep` |  |  |

## flytekit.types.directory.types.FlyteFile

```python
class FlyteFile(
    path: typing.Union[str, os.PathLike],
    downloader: typing.Callable,
    remote_path: typing.Optional[typing.Union[os.PathLike, str, bool]],
    metadata: typing.Optional[dict[str, str]],
)
```
FlyteFile's init method.



| Parameter | Type |
|-|-|
| `path` | `typing.Union[str, os.PathLike]` |
| `downloader` | `typing.Callable` |
| `remote_path` | `typing.Optional[typing.Union[os.PathLike, str, bool]]` |
| `metadata` | `typing.Optional[dict[str, str]]` |

### Methods

| Method | Description |
|-|-|
| [`deserialize_flyte_file()`](#deserialize_flyte_file) |  |
| [`download()`](#download) |  |
| [`extension()`](#extension) |  |
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`from_source()`](#from_source) | Create a new FlyteFile object with the remote source set to the input. |
| [`new()`](#new) | Create a new FlyteFile object in the current Flyte working directory. |
| [`new_remote_file()`](#new_remote_file) | Create a new FlyteFile object with a remote path. |
| [`open()`](#open) | Returns a streaming File handle. |
| [`serialize_flyte_file()`](#serialize_flyte_file) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


#### deserialize_flyte_file()

```python
def deserialize_flyte_file(
    info,
) -> 'FlyteFile'
```
| Parameter | Type |
|-|-|
| `info` |  |

#### download()

```python
def download()
```
#### extension()

```python
def extension()
```
#### from_dict()

```python
def from_dict(
    d,
    dialect,
)
```
| Parameter | Type |
|-|-|
| `d` |  |
| `dialect` |  |

#### from_json()

```python
def from_json(
    data: typing.Union[str, bytes, bytearray],
    decoder: collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]],
    from_dict_kwargs: typing.Any,
) -> ~T
```
| Parameter | Type |
|-|-|
| `data` | `typing.Union[str, bytes, bytearray]` |
| `decoder` | `collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]]` |
| `from_dict_kwargs` | `typing.Any` |

#### from_source()

```python
def from_source(
    source: str | os.PathLike,
) -> FlyteFile
```
Create a new FlyteFile object with the remote source set to the input


| Parameter | Type |
|-|-|
| `source` | `str \| os.PathLike` |

#### new()

```python
def new(
    filename: str | os.PathLike,
) -> FlyteFile
```
Create a new FlyteFile object in the current Flyte working directory


| Parameter | Type |
|-|-|
| `filename` | `str \| os.PathLike` |

#### new_remote_file()

```python
def new_remote_file(
    name: typing.Optional[str],
    alt: typing.Optional[str],
) -> FlyteFile
```
Create a new FlyteFile object with a remote path.



| Parameter | Type |
|-|-|
| `name` | `typing.Optional[str]` |
| `alt` | `typing.Optional[str]` |

#### open()

```python
def open(
    mode: str,
    cache_type: typing.Optional[str],
    cache_options: typing.Optional[typing.Dict[str, typing.Any]],
)
```
Returns a streaming File handle

.. code-block:: python

@task
def copy_file(ff: FlyteFile) -> FlyteFile:
new_file = FlyteFile.new_remote_file()
with ff.open("rb", cache_type="readahead") as r:
with new_file.open("wb") as w:
w.write(r.read())
return new_file



| Parameter | Type |
|-|-|
| `mode` | `str` |
| `cache_type` | `typing.Optional[str]` |
| `cache_options` | `typing.Optional[typing.Dict[str, typing.Any]]` |

#### serialize_flyte_file()

```python
def serialize_flyte_file()
```
#### to_dict()

```python
def to_dict()
```
#### to_json()

```python
def to_json(
    encoder: collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]],
    to_dict_kwargs: typing.Any,
) -> typing.Union[str, bytes, bytearray]
```
| Parameter | Type |
|-|-|
| `encoder` | `collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]]` |
| `to_dict_kwargs` | `typing.Any` |

### Properties

| Property | Type | Description |
|-|-|-|
| `downloaded` |  |  |
| `remote_path` |  |  |
| `remote_source` |  | {{< multiline >}}If this is an input to a task, and the original path is an ``s3`` bucket, Flytekit downloads the
file for the user. In case the user wants access to the original path, it will be here.
{{< /multiline >}} |

## flytekit.types.directory.types.Literal

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

## flytekit.types.directory.types.LiteralType

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

## flytekit.types.directory.types.Path

PurePath subclass that can make system calls.

Path represents a filesystem path but unlike PurePath, also offers
methods to do system calls on path objects. Depending on your system,
instantiating a Path will return either a PosixPath or a WindowsPath
object. You can also instantiate a PosixPath or WindowsPath directly,
but cannot instantiate a WindowsPath on a POSIX system or vice versa.


```python
class Path(
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`absolute()`](#absolute) | Return an absolute version of this path. |
| [`as_posix()`](#as_posix) | Return the string representation of the path with forward (/). |
| [`as_uri()`](#as_uri) | Return the path as a URI. |
| [`chmod()`](#chmod) | Change the permissions of the path, like os. |
| [`cwd()`](#cwd) | Return a new path pointing to the current working directory. |
| [`exists()`](#exists) | Whether this path exists. |
| [`expanduser()`](#expanduser) | Return a new path with expanded ~ and ~user constructs. |
| [`from_uri()`](#from_uri) | Return a new path from the given 'file' URI. |
| [`full_match()`](#full_match) | Return True if this path matches the given glob-style pattern. |
| [`glob()`](#glob) | Iterate over this subtree and yield all existing files (of any. |
| [`group()`](#group) | Return the group name of the file gid. |
| [`hardlink_to()`](#hardlink_to) | Make this path a hard link pointing to the same file as *target*. |
| [`home()`](#home) | Return a new path pointing to expanduser('~'). |
| [`is_absolute()`](#is_absolute) | True if the path is absolute (has both a root and, if applicable,. |
| [`is_block_device()`](#is_block_device) | Whether this path is a block device. |
| [`is_char_device()`](#is_char_device) | Whether this path is a character device. |
| [`is_dir()`](#is_dir) | Whether this path is a directory. |
| [`is_fifo()`](#is_fifo) | Whether this path is a FIFO. |
| [`is_file()`](#is_file) | Whether this path is a regular file (also True for symlinks pointing. |
| [`is_junction()`](#is_junction) | Whether this path is a junction. |
| [`is_mount()`](#is_mount) | Check if this path is a mount point. |
| [`is_relative_to()`](#is_relative_to) | Return True if the path is relative to another path or False. |
| [`is_reserved()`](#is_reserved) | Return True if the path contains one of the special names reserved. |
| [`is_socket()`](#is_socket) | Whether this path is a socket. |
| [`is_symlink()`](#is_symlink) | Whether this path is a symbolic link. |
| [`iterdir()`](#iterdir) | Yield path objects of the directory contents. |
| [`joinpath()`](#joinpath) | Combine this path with one or several arguments, and return a. |
| [`lchmod()`](#lchmod) | Like chmod(), except if the path points to a symlink, the symlink's. |
| [`lstat()`](#lstat) | Like stat(), except if the path points to a symlink, the symlink's. |
| [`match()`](#match) | Return True if this path matches the given pattern. |
| [`mkdir()`](#mkdir) | Create a new directory at this given path. |
| [`open()`](#open) | Open the file pointed to by this path and return a file object, as. |
| [`owner()`](#owner) | Return the login name of the file owner. |
| [`read_bytes()`](#read_bytes) | Open the file in bytes mode, read it, and close the file. |
| [`read_text()`](#read_text) | Open the file in text mode, read it, and close the file. |
| [`readlink()`](#readlink) | Return the path to which the symbolic link points. |
| [`relative_to()`](#relative_to) | Return the relative path to another path identified by the passed. |
| [`rename()`](#rename) | Rename this path to the target path. |
| [`replace()`](#replace) | Rename this path to the target path, overwriting if that path exists. |
| [`resolve()`](#resolve) | Make the path absolute, resolving all symlinks on the way and also. |
| [`rglob()`](#rglob) | Recursively yield all existing files (of any kind, including. |
| [`rmdir()`](#rmdir) | Remove this directory. |
| [`samefile()`](#samefile) | Return whether other_path is the same or not as this file. |
| [`stat()`](#stat) | Return the result of the stat() system call on this path, like. |
| [`symlink_to()`](#symlink_to) | Make this path a symlink pointing to the target path. |
| [`touch()`](#touch) | Create this file with the given access mode, if it doesn't exist. |
| [`unlink()`](#unlink) | Remove this file or link. |
| [`walk()`](#walk) | Walk the directory tree from this directory, similar to os. |
| [`with_name()`](#with_name) | Return a new path with the file name changed. |
| [`with_segments()`](#with_segments) | Construct a new path object from any number of path-like objects. |
| [`with_stem()`](#with_stem) | Return a new path with the stem changed. |
| [`with_suffix()`](#with_suffix) | Return a new path with the file suffix changed. |
| [`write_bytes()`](#write_bytes) | Open the file in bytes mode, write to it, and close the file. |
| [`write_text()`](#write_text) | Open the file in text mode, write to it, and close the file. |


#### absolute()

```python
def absolute()
```
Return an absolute version of this path
No normalization or symlink resolution is performed.

Use resolve() to resolve symlinks and remove '..' segments.


#### as_posix()

```python
def as_posix()
```
Return the string representation of the path with forward (/)
slashes.


#### as_uri()

```python
def as_uri()
```
Return the path as a URI.


#### chmod()

```python
def chmod(
    mode,
    follow_symlinks,
)
```
Change the permissions of the path, like os.chmod().


| Parameter | Type |
|-|-|
| `mode` |  |
| `follow_symlinks` |  |

#### cwd()

```python
def cwd()
```
Return a new path pointing to the current working directory.


#### exists()

```python
def exists(
    follow_symlinks,
)
```
Whether this path exists.

This method normally follows symlinks; to check whether a symlink exists,
add the argument follow_symlinks=False.


| Parameter | Type |
|-|-|
| `follow_symlinks` |  |

#### expanduser()

```python
def expanduser()
```
Return a new path with expanded ~ and ~user constructs
(as returned by os.path.expanduser)


#### from_uri()

```python
def from_uri(
    uri,
)
```
Return a new path from the given 'file' URI.


| Parameter | Type |
|-|-|
| `uri` |  |

#### full_match()

```python
def full_match(
    pattern,
    case_sensitive,
)
```
Return True if this path matches the given glob-style pattern. The
pattern is matched against the entire path.


| Parameter | Type |
|-|-|
| `pattern` |  |
| `case_sensitive` |  |

#### glob()

```python
def glob(
    pattern,
    case_sensitive,
    recurse_symlinks,
)
```
Iterate over this subtree and yield all existing files (of any
kind, including directories) matching the given relative pattern.


| Parameter | Type |
|-|-|
| `pattern` |  |
| `case_sensitive` |  |
| `recurse_symlinks` |  |

#### group()

```python
def group(
    follow_symlinks,
)
```
Return the group name of the file gid.


| Parameter | Type |
|-|-|
| `follow_symlinks` |  |

#### hardlink_to()

```python
def hardlink_to(
    target,
)
```
Make this path a hard link pointing to the same file as *target*.

Note the order of arguments (self, target) is the reverse of os.link's.


| Parameter | Type |
|-|-|
| `target` |  |

#### home()

```python
def home()
```
Return a new path pointing to expanduser('~').



#### is_absolute()

```python
def is_absolute()
```
True if the path is absolute (has both a root and, if applicable,
a drive).


#### is_block_device()

```python
def is_block_device()
```
Whether this path is a block device.


#### is_char_device()

```python
def is_char_device()
```
Whether this path is a character device.


#### is_dir()

```python
def is_dir(
    follow_symlinks,
)
```
Whether this path is a directory.


| Parameter | Type |
|-|-|
| `follow_symlinks` |  |

#### is_fifo()

```python
def is_fifo()
```
Whether this path is a FIFO.


#### is_file()

```python
def is_file(
    follow_symlinks,
)
```
Whether this path is a regular file (also True for symlinks pointing
to regular files).


| Parameter | Type |
|-|-|
| `follow_symlinks` |  |

#### is_junction()

```python
def is_junction()
```
Whether this path is a junction.


#### is_mount()

```python
def is_mount()
```
Check if this path is a mount point


#### is_relative_to()

```python
def is_relative_to(
    other,
    _deprecated,
)
```
Return True if the path is relative to another path or False.



| Parameter | Type |
|-|-|
| `other` |  |
| `_deprecated` |  |

#### is_reserved()

```python
def is_reserved()
```
Return True if the path contains one of the special names reserved
by the system, if any.


#### is_socket()

```python
def is_socket()
```
Whether this path is a socket.


#### is_symlink()

```python
def is_symlink()
```
Whether this path is a symbolic link.


#### iterdir()

```python
def iterdir()
```
Yield path objects of the directory contents.

The children are yielded in arbitrary order, and the
special entries '.' and '..' are not included.


#### joinpath()

```python
def joinpath(
    pathsegments,
)
```
Combine this path with one or several arguments, and return a
new path representing either a subpath (if all arguments are relative
paths) or a totally different path (if one of the arguments is
anchored).


| Parameter | Type |
|-|-|
| `pathsegments` |  |

#### lchmod()

```python
def lchmod(
    mode,
)
```
Like chmod(), except if the path points to a symlink, the symlink's
permissions are changed, rather than its target's.


| Parameter | Type |
|-|-|
| `mode` |  |

#### lstat()

```python
def lstat()
```
Like stat(), except if the path points to a symlink, the symlink's
status information is returned, rather than its target's.


#### match()

```python
def match(
    path_pattern,
    case_sensitive,
)
```
Return True if this path matches the given pattern. If the pattern is
relative, matching is done from the right; otherwise, the entire path
is matched. The recursive wildcard '**' is *not* supported by this
method.


| Parameter | Type |
|-|-|
| `path_pattern` |  |
| `case_sensitive` |  |

#### mkdir()

```python
def mkdir(
    mode,
    parents,
    exist_ok,
)
```
Create a new directory at this given path.


| Parameter | Type |
|-|-|
| `mode` |  |
| `parents` |  |
| `exist_ok` |  |

#### open()

```python
def open(
    mode,
    buffering,
    encoding,
    errors,
    newline,
)
```
Open the file pointed to by this path and return a file object, as
the built-in open() function does.


| Parameter | Type |
|-|-|
| `mode` |  |
| `buffering` |  |
| `encoding` |  |
| `errors` |  |
| `newline` |  |

#### owner()

```python
def owner(
    follow_symlinks,
)
```
Return the login name of the file owner.


| Parameter | Type |
|-|-|
| `follow_symlinks` |  |

#### read_bytes()

```python
def read_bytes()
```
Open the file in bytes mode, read it, and close the file.


#### read_text()

```python
def read_text(
    encoding,
    errors,
    newline,
)
```
Open the file in text mode, read it, and close the file.


| Parameter | Type |
|-|-|
| `encoding` |  |
| `errors` |  |
| `newline` |  |

#### readlink()

```python
def readlink()
```
Return the path to which the symbolic link points.


#### relative_to()

```python
def relative_to(
    other,
    _deprecated,
    walk_up,
)
```
Return the relative path to another path identified by the passed
arguments.  If the operation is not possible (because this is not
related to the other path), raise ValueError.

The *walk_up* parameter controls whether `..` may be used to resolve
the path.


| Parameter | Type |
|-|-|
| `other` |  |
| `_deprecated` |  |
| `walk_up` |  |

#### rename()

```python
def rename(
    target,
)
```
Rename this path to the target path.

The target path may be absolute or relative. Relative paths are
interpreted relative to the current working directory, *not* the
directory of the Path object.

Returns the new Path instance pointing to the target path.


| Parameter | Type |
|-|-|
| `target` |  |

#### replace()

```python
def replace(
    target,
)
```
Rename this path to the target path, overwriting if that path exists.

The target path may be absolute or relative. Relative paths are
interpreted relative to the current working directory, *not* the
directory of the Path object.

Returns the new Path instance pointing to the target path.


| Parameter | Type |
|-|-|
| `target` |  |

#### resolve()

```python
def resolve(
    strict,
)
```
Make the path absolute, resolving all symlinks on the way and also
normalizing it.


| Parameter | Type |
|-|-|
| `strict` |  |

#### rglob()

```python
def rglob(
    pattern,
    case_sensitive,
    recurse_symlinks,
)
```
Recursively yield all existing files (of any kind, including
directories) matching the given relative pattern, anywhere in
this subtree.


| Parameter | Type |
|-|-|
| `pattern` |  |
| `case_sensitive` |  |
| `recurse_symlinks` |  |

#### rmdir()

```python
def rmdir()
```
Remove this directory.  The directory must be empty.


#### samefile()

```python
def samefile(
    other_path,
)
```
Return whether other_path is the same or not as this file
(as returned by os.path.samefile()).


| Parameter | Type |
|-|-|
| `other_path` |  |

#### stat()

```python
def stat(
    follow_symlinks,
)
```
Return the result of the stat() system call on this path, like
os.stat() does.


| Parameter | Type |
|-|-|
| `follow_symlinks` |  |

#### symlink_to()

```python
def symlink_to(
    target,
    target_is_directory,
)
```
Make this path a symlink pointing to the target path.
Note the order of arguments (link, target) is the reverse of os.symlink.


| Parameter | Type |
|-|-|
| `target` |  |
| `target_is_directory` |  |

#### touch()

```python
def touch(
    mode,
    exist_ok,
)
```
Create this file with the given access mode, if it doesn't exist.


| Parameter | Type |
|-|-|
| `mode` |  |
| `exist_ok` |  |

#### unlink()

```python
def unlink(
    missing_ok,
)
```
Remove this file or link.
If the path is a directory, use rmdir() instead.


| Parameter | Type |
|-|-|
| `missing_ok` |  |

#### walk()

```python
def walk(
    top_down,
    on_error,
    follow_symlinks,
)
```
Walk the directory tree from this directory, similar to os.walk().


| Parameter | Type |
|-|-|
| `top_down` |  |
| `on_error` |  |
| `follow_symlinks` |  |

#### with_name()

```python
def with_name(
    name,
)
```
Return a new path with the file name changed.


| Parameter | Type |
|-|-|
| `name` |  |

#### with_segments()

```python
def with_segments(
    pathsegments,
)
```
Construct a new path object from any number of path-like objects.
Subclasses may override this method to customize how new path objects
are created from methods like `iterdir()`.


| Parameter | Type |
|-|-|
| `pathsegments` |  |

#### with_stem()

```python
def with_stem(
    stem,
)
```
Return a new path with the stem changed.


| Parameter | Type |
|-|-|
| `stem` |  |

#### with_suffix()

```python
def with_suffix(
    suffix,
)
```
Return a new path with the file suffix changed.  If the path
has no suffix, add given suffix.  If the given suffix is an empty
string, remove the suffix from the path.


| Parameter | Type |
|-|-|
| `suffix` |  |

#### write_bytes()

```python
def write_bytes(
    data,
)
```
Open the file in bytes mode, write to it, and close the file.


| Parameter | Type |
|-|-|
| `data` |  |

#### write_text()

```python
def write_text(
    data,
    encoding,
    errors,
    newline,
)
```
Open the file in text mode, write to it, and close the file.


| Parameter | Type |
|-|-|
| `data` |  |
| `encoding` |  |
| `errors` |  |
| `newline` |  |

### Properties

| Property | Type | Description |
|-|-|-|
| `anchor` |  | {{< multiline >}}The concatenation of the drive and root, or ''.
{{< /multiline >}} |
| `drive` |  | {{< multiline >}}The drive prefix (letter or UNC path), if any.
{{< /multiline >}} |
| `name` |  | {{< multiline >}}The final path component, if any.
{{< /multiline >}} |
| `parent` |  | {{< multiline >}}The logical parent of the path.
{{< /multiline >}} |
| `parents` |  | {{< multiline >}}A sequence of this path's logical parents.
{{< /multiline >}} |
| `parts` |  | {{< multiline >}}An object providing sequence-like access to the
components in the filesystem path.
{{< /multiline >}} |
| `root` |  | {{< multiline >}}The root of the path, if any.
{{< /multiline >}} |
| `stem` |  | {{< multiline >}}The final path component, minus its last suffix.
{{< /multiline >}} |
| `suffix` |  | {{< multiline >}}The final component's last suffix, if any.

This includes the leading period. For example: '.txt'
{{< /multiline >}} |
| `suffixes` |  | {{< multiline >}}A list of the final component's suffixes, if any.

These include the leading periods. For example: ['.tar', '.gz']
{{< /multiline >}} |

## flytekit.types.directory.types.Scalar

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

## flytekit.types.directory.types.SerializableType

## flytekit.types.directory.types.Struct

A ProtocolMessage


### Methods

| Method | Description |
|-|-|
| [`get_or_create_list()`](#get_or_create_list) | Returns a list for this key, creating if it didn't exist already. |
| [`get_or_create_struct()`](#get_or_create_struct) | Returns a struct for this key, creating if it didn't exist already. |
| [`items()`](#items) |  |
| [`keys()`](#keys) |  |
| [`update()`](#update) |  |
| [`values()`](#values) |  |


#### get_or_create_list()

```python
def get_or_create_list(
    key,
)
```
Returns a list for this key, creating if it didn't exist already.


| Parameter | Type |
|-|-|
| `key` |  |

#### get_or_create_struct()

```python
def get_or_create_struct(
    key,
)
```
Returns a struct for this key, creating if it didn't exist already.


| Parameter | Type |
|-|-|
| `key` |  |

#### items()

```python
def items()
```
#### keys()

```python
def keys()
```
#### update()

```python
def update(
    dictionary,
)
```
| Parameter | Type |
|-|-|
| `dictionary` |  |

#### values()

```python
def values()
```
## flytekit.types.directory.types.TypeEngine

Core Extensible TypeEngine of Flytekit. This should be used to extend the capabilities of FlyteKits type system.
Users can implement their own TypeTransformers and register them with the TypeEngine. This will allow special handling
of user objects


### Methods

| Method | Description |
|-|-|
| [`async_to_literal()`](#async_to_literal) | Converts a python value of a given type and expected ``LiteralType`` into a resolved ``Literal`` value. |
| [`async_to_python_value()`](#async_to_python_value) |  |
| [`calculate_hash()`](#calculate_hash) |  |
| [`dict_to_literal_map()`](#dict_to_literal_map) |  |
| [`dict_to_literal_map_pb()`](#dict_to_literal_map_pb) |  |
| [`get_available_transformers()`](#get_available_transformers) | Returns all python types for which transformers are available. |
| [`get_transformer()`](#get_transformer) | Implements a recursive search for the transformer. |
| [`guess_python_type()`](#guess_python_type) | Transforms a flyte-specific ``LiteralType`` to a regular python value. |
| [`guess_python_types()`](#guess_python_types) | Transforms a dictionary of flyte-specific ``Variable`` objects to a dictionary of regular python values. |
| [`lazy_import_transformers()`](#lazy_import_transformers) | Only load the transformers if needed. |
| [`literal_map_to_kwargs()`](#literal_map_to_kwargs) |  |
| [`named_tuple_to_variable_map()`](#named_tuple_to_variable_map) | Converts a python-native ``NamedTuple`` to a flyte-specific VariableMap of named literals. |
| [`register()`](#register) | This should be used for all types that respond with the right type annotation when you use type(. |
| [`register_additional_type()`](#register_additional_type) |  |
| [`register_restricted_type()`](#register_restricted_type) |  |
| [`to_html()`](#to_html) |  |
| [`to_literal()`](#to_literal) | The current dance is because we are allowing users to call from an async function, this synchronous. |
| [`to_literal_checks()`](#to_literal_checks) |  |
| [`to_literal_type()`](#to_literal_type) | Converts a python type into a flyte specific ``LiteralType``. |
| [`to_python_value()`](#to_python_value) | Converts a Literal value with an expected python type into a python value. |
| [`unwrap_offloaded_literal()`](#unwrap_offloaded_literal) |  |


#### async_to_literal()

```python
def async_to_literal(
    ctx: FlyteContext,
    python_val: typing.Any,
    python_type: Type[T],
    expected: LiteralType,
) -> Literal
```
Converts a python value of a given type and expected ``LiteralType`` into a resolved ``Literal`` value.


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `typing.Any` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### async_to_python_value()

```python
def async_to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type,
) -> typing.Any
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type` |

#### calculate_hash()

```python
def calculate_hash(
    python_val: typing.Any,
    python_type: Type[T],
) -> Optional[str]
```
| Parameter | Type |
|-|-|
| `python_val` | `typing.Any` |
| `python_type` | `Type[T]` |

#### dict_to_literal_map()

```python
def dict_to_literal_map(
    ctx: FlyteContext,
    d: typing.Dict[str, typing.Any],
    type_hints: Optional[typing.Dict[str, type]],
) -> LiteralMap
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `d` | `typing.Dict[str, typing.Any]` |
| `type_hints` | `Optional[typing.Dict[str, type]]` |

#### dict_to_literal_map_pb()

```python
def dict_to_literal_map_pb(
    ctx: FlyteContext,
    d: typing.Dict[str, typing.Any],
    type_hints: Optional[typing.Dict[str, type]],
) -> Optional[literals_pb2.LiteralMap]
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `d` | `typing.Dict[str, typing.Any]` |
| `type_hints` | `Optional[typing.Dict[str, type]]` |

#### get_available_transformers()

```python
def get_available_transformers()
```
Returns all python types for which transformers are available


#### get_transformer()

```python
def get_transformer(
    python_type: Type,
) -> TypeTransformer[T]
```
Implements a recursive search for the transformer.


| Parameter | Type |
|-|-|
| `python_type` | `Type` |

#### guess_python_type()

```python
def guess_python_type(
    flyte_type: LiteralType,
) -> Type[T]
```
Transforms a flyte-specific ``LiteralType`` to a regular python value.


| Parameter | Type |
|-|-|
| `flyte_type` | `LiteralType` |

#### guess_python_types()

```python
def guess_python_types(
    flyte_variable_dict: typing.Dict[str, _interface_models.Variable],
) -> typing.Dict[str, type]
```
Transforms a dictionary of flyte-specific ``Variable`` objects to a dictionary of regular python values.


| Parameter | Type |
|-|-|
| `flyte_variable_dict` | `typing.Dict[str, _interface_models.Variable]` |

#### lazy_import_transformers()

```python
def lazy_import_transformers()
```
Only load the transformers if needed.


#### literal_map_to_kwargs()

```python
def literal_map_to_kwargs(
    ctx: FlyteContext,
    lm: LiteralMap,
    python_types: typing.Optional[typing.Dict[str, type]],
    literal_types: typing.Optional[typing.Dict[str, _interface_models.Variable]],
) -> typing.Dict[str, typing.Any]
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lm` | `LiteralMap` |
| `python_types` | `typing.Optional[typing.Dict[str, type]]` |
| `literal_types` | `typing.Optional[typing.Dict[str, _interface_models.Variable]]` |

#### named_tuple_to_variable_map()

```python
def named_tuple_to_variable_map(
    t: typing.NamedTuple,
) -> _interface_models.VariableMap
```
Converts a python-native ``NamedTuple`` to a flyte-specific VariableMap of named literals.


| Parameter | Type |
|-|-|
| `t` | `typing.NamedTuple` |

#### register()

```python
def register(
    transformer: TypeTransformer,
    additional_types: Optional[typing.List[Type]],
)
```
This should be used for all types that respond with the right type annotation when you use type(...) function


| Parameter | Type |
|-|-|
| `transformer` | `TypeTransformer` |
| `additional_types` | `Optional[typing.List[Type]]` |

#### register_additional_type()

```python
def register_additional_type(
    transformer: TypeTransformer[T],
    additional_type: Type[T],
    override,
)
```
| Parameter | Type |
|-|-|
| `transformer` | `TypeTransformer[T]` |
| `additional_type` | `Type[T]` |
| `override` |  |

#### register_restricted_type()

```python
def register_restricted_type(
    name: str,
    type: Type[T],
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `type` | `Type[T]` |

#### to_html()

```python
def to_html(
    ctx: FlyteContext,
    python_val: typing.Any,
    expected_python_type: Type[typing.Any],
) -> str
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `typing.Any` |
| `expected_python_type` | `Type[typing.Any]` |

#### to_literal()

```python
def to_literal(
    ctx: FlyteContext,
    python_val: typing.Any,
    python_type: Type[T],
    expected: LiteralType,
) -> Literal
```
The current dance is because we are allowing users to call from an async function, this synchronous
to_literal function, and allowing this to_literal function, to then invoke yet another async function,
namely an async transformer.


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `typing.Any` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### to_literal_checks()

```python
def to_literal_checks(
    python_val: typing.Any,
    python_type: Type[T],
    expected: LiteralType,
)
```
| Parameter | Type |
|-|-|
| `python_val` | `typing.Any` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### to_literal_type()

```python
def to_literal_type(
    python_type: Type[T],
) -> LiteralType
```
Converts a python type into a flyte specific ``LiteralType``


| Parameter | Type |
|-|-|
| `python_type` | `Type[T]` |

#### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type,
) -> typing.Any
```
Converts a Literal value with an expected python type into a python value.


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type` |

#### unwrap_offloaded_literal()

```python
def unwrap_offloaded_literal(
    ctx: FlyteContext,
    lv: Literal,
) -> Literal
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |

## flytekit.types.directory.types.TypeTransformerFailedError

Inappropriate argument type.


## flytekit.types.directory.types.UUID

Instances of the UUID class represent UUIDs as specified in RFC 4122.
UUID objects are immutable, hashable, and usable as dictionary keys.
Converting a UUID to a string with str() yields something in the form
'12345678-1234-1234-1234-123456789abc'.  The UUID constructor accepts
five possible forms: a similar string of hexadecimal digits, or a tuple
of six integer fields (with 32-bit, 16-bit, 16-bit, 8-bit, 8-bit, and
48-bit values respectively) as an argument named 'fields', or a string
of 16 bytes (with all the integer fields in big-endian order) as an
argument named 'bytes', or a string of 16 bytes (with the first three
fields in little-endian order) as an argument named 'bytes_le', or a
single 128-bit integer as an argument named 'int'.

UUIDs have these read-only attributes:

bytes       the UUID as a 16-byte string (containing the six
integer fields in big-endian byte order)

bytes_le    the UUID as a 16-byte string (with time_low, time_mid,
and time_hi_version in little-endian byte order)

fields      a tuple of the six integer fields of the UUID,
which are also available as six individual attributes
and two derived attributes:

time_low                the first 32 bits of the UUID
time_mid                the next 16 bits of the UUID
time_hi_version         the next 16 bits of the UUID
clock_seq_hi_variant    the next 8 bits of the UUID
clock_seq_low           the next 8 bits of the UUID
node                    the last 48 bits of the UUID

time                    the 60-bit timestamp
clock_seq               the 14-bit sequence number

hex         the UUID as a 32-character hexadecimal string

int         the UUID as a 128-bit integer

urn         the UUID as a URN as specified in RFC 4122

variant     the UUID variant (one of the constants RESERVED_NCS,
RFC_4122, RESERVED_MICROSOFT, or RESERVED_FUTURE)

version     the UUID version number (1 through 5, meaningful only
when the variant is RFC_4122)

is_safe     An enum indicating whether the UUID has been generated in
a way that is safe for multiprocessing applications, via
uuid_generate_time_safe(3).


```python
class UUID(
    hex,
    bytes,
    bytes_le,
    fields,
    int,
    version,
    is_safe,
)
```
Create a UUID from either a string of 32 hexadecimal digits,
a string of 16 bytes as the 'bytes' argument, a string of 16 bytes
in little-endian order as the 'bytes_le' argument, a tuple of six
integers (32-bit time_low, 16-bit time_mid, 16-bit time_hi_version,
8-bit clock_seq_hi_variant, 8-bit clock_seq_low, 48-bit node) as
the 'fields' argument, or a single 128-bit integer as the 'int'
argument.  When a string of hex digits is given, curly braces,
hyphens, and a URN prefix are all optional.  For example, these
expressions all yield the same UUID:

UUID('{12345678-1234-5678-1234-567812345678}')
UUID('12345678123456781234567812345678')
UUID('urn:uuid:12345678-1234-5678-1234-567812345678')
UUID(bytes='\x12\x34\x56\x78'*4)
UUID(bytes_le='\x78\x56\x34\x12\x34\x12\x78\x56' +
'\x12\x34\x56\x78\x12\x34\x56\x78')
UUID(fields=(0x12345678, 0x1234, 0x5678, 0x12, 0x34, 0x567812345678))
UUID(int=0x12345678123456781234567812345678)

Exactly one of 'hex', 'bytes', 'bytes_le', 'fields', or 'int' must
be given.  The 'version' argument is optional; if given, the resulting
UUID will have its variant and version set according to RFC 4122,
overriding the given 'hex', 'bytes', 'bytes_le', 'fields', or 'int'.

is_safe is an enum exposed as an attribute on the instance.  It
indicates whether the UUID has been generated in a way that is safe
for multiprocessing applications, via uuid_generate_time_safe(3).


| Parameter | Type |
|-|-|
| `hex` |  |
| `bytes` |  |
| `bytes_le` |  |
| `fields` |  |
| `int` |  |
| `version` |  |
| `is_safe` |  |

### Properties

| Property | Type | Description |
|-|-|-|
| `bytes` |  |  |
| `bytes_le` |  |  |
| `clock_seq` |  |  |
| `clock_seq_hi_variant` |  |  |
| `clock_seq_low` |  |  |
| `fields` |  |  |
| `hex` |  |  |
| `node` |  |  |
| `time` |  |  |
| `time_hi_version` |  |  |
| `time_low` |  |  |
| `time_mid` |  |  |
| `urn` |  |  |
| `variant` |  |  |
| `version` |  |  |

## flytekit.types.directory.types.partial

Create a new function with partial application of the given arguments
and keywords.


