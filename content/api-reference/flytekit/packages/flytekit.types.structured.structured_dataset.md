---
title: flytekit.types.structured.structured_dataset
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.types.structured.structured_dataset

## Directory

### Classes

| Class | Description |
|-|-|
| [`ABC`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetabc) | Helper class that provides a standard way to create an ABC using. |
| [`AsyncTypeTransformer`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetasynctypetransformer) | Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`Binary`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetbinary) |  |
| [`DataClassJSONMixin`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetdataclassjsonmixin) |  |
| [`FlyteContext`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetflytecontext) | This is an internal-facing context object, that most users will not have to deal with. |
| [`FlyteContextManager`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetflytecontextmanager) | FlyteContextManager manages the execution context within Flytekit. |
| [`Generic`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetgeneric) | Abstract base class for generic types. |
| [`Literal`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetliteral) |  |
| [`LiteralType`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetliteraltype) |  |
| [`Renderable`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetrenderable) | Base class for protocol classes. |
| [`Scalar`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetscalar) |  |
| [`SchemaType`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetschematype) |  |
| [`SerializableType`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetserializabletype) |  |
| [`Struct`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstruct) | A ProtocolMessage. |
| [`StructuredDataset`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstructureddataset) | This is the user facing StructuredDataset class. |
| [`StructuredDatasetDecoder`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstructureddatasetdecoder) | Helper class that provides a standard way to create an ABC using. |
| [`StructuredDatasetEncoder`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstructureddatasetencoder) | Helper class that provides a standard way to create an ABC using. |
| [`StructuredDatasetFormat`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstructureddatasetformat) | str(object='') -> str. |
| [`StructuredDatasetMetadata`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstructureddatasetmetadata) |  |
| [`StructuredDatasetTransformerEngine`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstructureddatasettransformerengine) | Think of this transformer as a higher-level meta transformer that is used for all the dataframe types. |
| [`StructuredDatasetType`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstructureddatasettype) |  |
| [`TypeEngine`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasettypeengine) | Core Extensible TypeEngine of Flytekit. |

### Errors

| Exception | Description |
|-|-|
| [`DuplicateHandlerError`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetduplicatehandlererror) | Inappropriate argument value (of correct type). |
| [`TypeTransformerFailedError`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasettypetransformerfailederror) | Inappropriate argument type. |

### Methods

| Method | Description |
|-|-|
| [`abstractmethod()`](#abstractmethod) | A decorator indicating abstract methods. |
| [`config()`](#config) |  |
| [`convert_schema_type_to_structured_dataset_type()`](#convert_schema_type_to_structured_dataset_type) |  |
| [`dataclass()`](#dataclass) | Add dunder methods based on the fields defined in the class. |
| [`extract_cols_and_format()`](#extract_cols_and_format) | Helper function, just used to iterate through Annotations and extract out the following information:. |
| [`field()`](#field) | Return an object to identify dataclass fields. |
| [`flatten_dict()`](#flatten_dict) |  |
| [`get_args()`](#get_args) | Get type arguments with all substitutions performed. |
| [`get_origin()`](#get_origin) | Get the unsubscripted version of a type. |
| [`get_protocol()`](#get_protocol) |  |
| [`get_supported_types()`](#get_supported_types) |  |
| [`is_dataclass()`](#is_dataclass) | Returns True if obj is a dataclass or an instance of a. |
| [`lazy_module()`](#lazy_module) | This function is used to lazily import modules. |
| [`model_serializer()`](#model_serializer) | Decorator that enables custom model serialization. |
| [`model_validator()`](#model_validator) | Usage docs: https://docs. |
| [`modify_literal_uris()`](#modify_literal_uris) | Modifies the literal object recursively to replace the URIs with the native paths in case they are of. |


### Variables

| Property | Type | Description |
|-|-|-|
| `CSV` | `str` |  |
| `DF` | `TypeVar` |  |
| `GENERIC_FORMAT` | `str` |  |
| `GENERIC_PROTOCOL` | `str` |  |
| `MESSAGEPACK` | `str` |  |
| `PARQUET` | `str` |  |
| `T` | `TypeVar` |  |
| `annotations` | `_Feature` |  |
| `developer_logger` | `Logger` |  |
| `flyte_dataset_transformer` | `StructuredDatasetTransformerEngine` |  |
| `logger` | `Logger` |  |
| `loop_manager` | `_AsyncLoopManager` |  |

## Methods

#### abstractmethod()

```python
def abstractmethod(
    funcobj,
)
```
A decorator indicating abstract methods.

Requires that the metaclass is ABCMeta or derived from it.  A
class that has a metaclass derived from ABCMeta cannot be
instantiated unless all of its abstract methods are overridden.
The abstract methods can be called using any of the normal
'super' call mechanisms.  abstractmethod() may be used to declare
abstract methods for properties and descriptors.

Usage:

class C(metaclass=ABCMeta):
@abstractmethod
def my_abstract_method(self, arg1, arg2, argN):
...


| Parameter | Type |
|-|-|
| `funcobj` |  |

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

#### convert_schema_type_to_structured_dataset_type()

```python
def convert_schema_type_to_structured_dataset_type(
    column_type: int,
) -> int
```
| Parameter | Type |
|-|-|
| `column_type` | `int` |

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

#### extract_cols_and_format()

```python
def extract_cols_and_format(
    t: typing.Any,
) -> typing.Tuple[Type[T], Optional[typing.OrderedDict[str, Type]], Optional[str], Optional['pa.lib.Schema']]
```
Helper function, just used to iterate through Annotations and extract out the following information:
- base type, if not Annotated, it will just be the type that was passed in.
- column information, as a collections.OrderedDict,
- the storage format, as a ``StructuredDatasetFormat`` (str),
- pa.lib.Schema

If more than one of any type of thing is found, an error will be raised.
If no instances of a given type are found, then None will be returned.

If we add more things, we should put all the returned items in a dataclass instead of just a tuple.



| Parameter | Type |
|-|-|
| `t` | `typing.Any` |

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

#### flatten_dict()

```python
def flatten_dict(
    sub_dict: dict,
    parent_key: str,
) -> typing.Dict
```
| Parameter | Type |
|-|-|
| `sub_dict` | `dict` |
| `parent_key` | `str` |

#### get_args()

```python
def get_args(
    tp,
)
```
Get type arguments with all substitutions performed.

For unions, basic simplifications used by Union constructor are performed.

Examples::

>>> T = TypeVar('T')
>>> assert get_args(Dict[str, int]) == (str, int)
>>> assert get_args(int) == ()
>>> assert get_args(Union[int, Union[T, int], str][int]) == (int, str)
>>> assert get_args(Union[int, Tuple[T, int]][str]) == (int, Tuple[str, int])
>>> assert get_args(Callable[[], T][int]) == ([], int)


| Parameter | Type |
|-|-|
| `tp` |  |

#### get_origin()

```python
def get_origin(
    tp,
)
```
Get the unsubscripted version of a type.

This supports generic types, Callable, Tuple, Union, Literal, Final, ClassVar,
Annotated, and others. Return None for unsupported types.

Examples::

>>> P = ParamSpec('P')
>>> assert get_origin(Literal[42]) is Literal
>>> assert get_origin(int) is None
>>> assert get_origin(ClassVar[int]) is ClassVar
>>> assert get_origin(Generic) is Generic
>>> assert get_origin(Generic[T]) is Generic
>>> assert get_origin(Union[T, int]) is Union
>>> assert get_origin(List[Tuple[T, T]][int]) is list
>>> assert get_origin(P.args) is P


| Parameter | Type |
|-|-|
| `tp` |  |

#### get_protocol()

```python
def get_protocol(
    url: str,
) -> str
```
| Parameter | Type |
|-|-|
| `url` | `str` |

#### get_supported_types()

```python
def get_supported_types()
```
#### is_dataclass()

```python
def is_dataclass(
    obj,
)
```
Returns True if obj is a dataclass or an instance of a
dataclass.


| Parameter | Type |
|-|-|
| `obj` |  |

#### lazy_module()

```python
def lazy_module(
    fullname,
)
```
This function is used to lazily import modules.  It is used in the following way:
.. code-block:: python
from flytekit.lazy_import import lazy_module
sklearn = lazy_module("sklearn")
sklearn.svm.SVC()


| Parameter | Type |
|-|-|
| `fullname` |  |

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

#### modify_literal_uris()

```python
def modify_literal_uris(
    lit: Literal,
)
```
Modifies the literal object recursively to replace the URIs with the native paths in case they are of
type "flyte://"


| Parameter | Type |
|-|-|
| `lit` | `Literal` |

## flytekit.types.structured.structured_dataset.ABC

Helper class that provides a standard way to create an ABC using
inheritance.


## flytekit.types.structured.structured_dataset.AsyncTypeTransformer

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

## flytekit.types.structured.structured_dataset.Binary

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

## flytekit.types.structured.structured_dataset.DataClassJSONMixin

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


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

## flytekit.types.structured.structured_dataset.DuplicateHandlerError

Inappropriate argument value (of correct type).


## flytekit.types.structured.structured_dataset.FlyteContext

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

## flytekit.types.structured.structured_dataset.FlyteContextManager

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

## flytekit.types.structured.structured_dataset.Generic

Abstract base class for generic types.

On Python 3.12 and newer, generic classes implicitly inherit from
Generic when they declare a parameter list after the class's name::

class Mapping[KT, VT]:
def __getitem__(self, key: KT) -> VT:
...
# Etc.

On older versions of Python, however, generic classes have to
explicitly inherit from Generic.

After a class has been declared to be generic, it can then be used as
follows::

def lookup_name[KT, VT](mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
try:
return mapping[key]
except KeyError:
return default


## flytekit.types.structured.structured_dataset.Literal

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

## flytekit.types.structured.structured_dataset.LiteralType

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

## flytekit.types.structured.structured_dataset.Renderable

Base class for protocol classes.

Protocol classes are defined as::

class Proto(Protocol):
def meth(self) -> int:
...

Such classes are primarily used with static type checkers that recognize
structural subtyping (static duck-typing).

For example::

class C:
def meth(self) -> int:
return 0

def func(x: Proto) -> int:
return x.meth()

func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with
@typing.runtime_checkable act as simple-minded runtime protocols that check
only the presence of given attributes, ignoring their type signatures.
Protocol classes can be generic, they are defined as::

class GenProto[T](Protocol):
def meth(self) -> T:
...


```python
class Renderable(
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
| [`to_html()`](#to_html) | Convert an object(markdown, pandas. |


#### to_html()

```python
def to_html(
    python_value: typing.Any,
) -> str
```
Convert an object(markdown, pandas.dataframe) to HTML and return HTML as a unicode string.
Returns: An HTML document as a string.


| Parameter | Type |
|-|-|
| `python_value` | `typing.Any` |

## flytekit.types.structured.structured_dataset.Scalar

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

## flytekit.types.structured.structured_dataset.SchemaType

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

## flytekit.types.structured.structured_dataset.SerializableType

## flytekit.types.structured.structured_dataset.Struct

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
## flytekit.types.structured.structured_dataset.StructuredDataset

This is the user facing StructuredDataset class. Please don't confuse it with the literals.StructuredDataset
class (that is just a model, a Python class representation of the protobuf).


```python
class StructuredDataset(
    dataframe: typing.Optional[typing.Any],
    uri: typing.Optional[str],
    metadata: typing.Optional[literals.StructuredDatasetMetadata],
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `dataframe` | `typing.Optional[typing.Any]` |
| `uri` | `typing.Optional[str]` |
| `metadata` | `typing.Optional[literals.StructuredDatasetMetadata]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`all()`](#all) |  |
| [`column_names()`](#column_names) |  |
| [`columns()`](#columns) |  |
| [`deserialize_structured_dataset()`](#deserialize_structured_dataset) |  |
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`iter()`](#iter) |  |
| [`open()`](#open) |  |
| [`serialize_structured_dataset()`](#serialize_structured_dataset) |  |
| [`set_literal()`](#set_literal) | A public wrapper method to set the StructuredDataset Literal. |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


#### all()

```python
def all()
```
#### column_names()

```python
def column_names()
```
#### columns()

```python
def columns()
```
#### deserialize_structured_dataset()

```python
def deserialize_structured_dataset(
    info,
) -> StructuredDataset
```
| Parameter | Type |
|-|-|
| `info` |  |

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

#### iter()

```python
def iter()
```
#### open()

```python
def open(
    dataframe_type: Type[DF],
)
```
| Parameter | Type |
|-|-|
| `dataframe_type` | `Type[DF]` |

#### serialize_structured_dataset()

```python
def serialize_structured_dataset()
```
#### set_literal()

```python
def set_literal(
    ctx: FlyteContext,
    expected: LiteralType,
)
```
A public wrapper method to set the StructuredDataset Literal.

This method provides external access to the internal _set_literal method.


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `expected` | `LiteralType` |

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
| `dataframe` |  |  |
| `literal` |  |  |
| `metadata` |  |  |

## flytekit.types.structured.structured_dataset.StructuredDatasetDecoder

Helper class that provides a standard way to create an ABC using
inheritance.


```python
class StructuredDatasetDecoder(
    python_type: Type[DF],
    protocol: Optional[str],
    supported_format: Optional[str],
    additional_protocols: Optional[List[str]],
)
```
Extend this abstract class, implement the decode function, and register your concrete class with the
StructuredDatasetTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the decoder interface, meaning it is used when there is a Flyte Literal value,
and we have to get a Python value out of it. For the other way, see the StructuredDatasetEncoder



| Parameter | Type |
|-|-|
| `python_type` | `Type[DF]` |
| `protocol` | `Optional[str]` |
| `supported_format` | `Optional[str]` |
| `additional_protocols` | `Optional[List[str]]` |

### Methods

| Method | Description |
|-|-|
| [`decode()`](#decode) | This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal. |


#### decode()

```python
def decode(
    ctx: FlyteContext,
    flyte_value: literals.StructuredDataset,
    current_task_metadata: StructuredDatasetMetadata,
) -> Union[DF, typing.Iterator[DF]]
```
This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal
value into a Python instance.



| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `flyte_value` | `literals.StructuredDataset` |
| `current_task_metadata` | `StructuredDatasetMetadata` |

### Properties

| Property | Type | Description |
|-|-|-|
| `protocol` |  |  |
| `python_type` |  |  |
| `supported_format` |  |  |

## flytekit.types.structured.structured_dataset.StructuredDatasetEncoder

Helper class that provides a standard way to create an ABC using
inheritance.


```python
class StructuredDatasetEncoder(
    python_type: Type[T],
    protocol: Optional[str],
    supported_format: Optional[str],
)
```
Extend this abstract class, implement the encode function, and register your concrete class with the
StructuredDatasetTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the encoding interface, meaning it is used when there is a Python value that the
flytekit type engine is trying to convert into a Flyte Literal. For the other way, see
the StructuredDatasetEncoder



| Parameter | Type |
|-|-|
| `python_type` | `Type[T]` |
| `protocol` | `Optional[str]` |
| `supported_format` | `Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`encode()`](#encode) | Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the. |


#### encode()

```python
def encode(
    ctx: FlyteContext,
    structured_dataset: StructuredDataset,
    structured_dataset_type: StructuredDatasetType,
) -> literals.StructuredDataset
```
Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the
incoming dataframe with defaults set for that dataframe
type. This simplifies this function's interface as a lot of data that could be specified by the user using
the
# TODO: Do we need to add a flag to indicate if it was wrapped by the transformer or by the user?



| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `structured_dataset` | `StructuredDataset` |
| `structured_dataset_type` | `StructuredDatasetType` |

### Properties

| Property | Type | Description |
|-|-|-|
| `protocol` |  |  |
| `python_type` |  |  |
| `supported_format` |  |  |

## flytekit.types.structured.structured_dataset.StructuredDatasetFormat

str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.


## flytekit.types.structured.structured_dataset.StructuredDatasetMetadata

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
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


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
| `structured_dataset_type` |  |  |

## flytekit.types.structured.structured_dataset.StructuredDatasetTransformerEngine

Think of this transformer as a higher-level meta transformer that is used for all the dataframe types.
If you are bringing a custom data frame type, or any data frame type, to flytekit, instead of
registering with the main type engine, you should register with this transformer instead.


```python
def StructuredDatasetTransformerEngine()
```
### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`async_to_literal()`](#async_to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`async_to_python_value()`](#async_to_python_value) | The only tricky thing with converting a Literal (say the output of an earlier task), to a Python value at. |
| [`dict_to_structured_dataset()`](#dict_to_structured_dataset) |  |
| [`encode()`](#encode) |  |
| [`from_binary_idl()`](#from_binary_idl) | If the input is from flytekit, the Life Cycle will be as follows:. |
| [`from_generic_idl()`](#from_generic_idl) | If the input is from Flyte Console, the Life Cycle will be as follows:. |
| [`get_decoder()`](#get_decoder) |  |
| [`get_encoder()`](#get_encoder) |  |
| [`get_literal_type()`](#get_literal_type) | Provide a concrete implementation so that writers of custom dataframe handlers since there's nothing that. |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type. |
| [`isinstance_generic()`](#isinstance_generic) |  |
| [`iter_as()`](#iter_as) |  |
| [`open_as()`](#open_as) | . |
| [`register()`](#register) | Call this with any Encoder or Decoder to register it with the flytekit type system. |
| [`register_for_protocol()`](#register_for_protocol) | See the main register function instead. |
| [`register_renderer()`](#register_renderer) |  |
| [`to_html()`](#to_html) | Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div. |
| [`to_literal()`](#to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`to_python_value()`](#to_python_value) | Converts the given Literal to a Python Type. |


#### assert_type()

```python
def assert_type(
    t: Type[StructuredDataset],
    v: typing.Any,
)
```
| Parameter | Type |
|-|-|
| `t` | `Type[StructuredDataset]` |
| `v` | `typing.Any` |

#### async_to_literal()

```python
def async_to_literal(
    ctx: FlyteContext,
    python_val: Union[StructuredDataset, typing.Any],
    python_type: Union[Type[StructuredDataset], Type],
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
| `python_val` | `Union[StructuredDataset, typing.Any]` |
| `python_type` | `Union[Type[StructuredDataset], Type]` |
| `expected` | `LiteralType` |

#### async_to_python_value()

```python
def async_to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T] | StructuredDataset,
) -> T | StructuredDataset
```
The only tricky thing with converting a Literal (say the output of an earlier task), to a Python value at
the start of a task execution, is the column subsetting behavior. For example, if you have,

def t1() -> Annotated[StructuredDataset, kwtypes(col_a=int, col_b=float)]: ...
def t2(in_a: Annotated[StructuredDataset, kwtypes(col_b=float)]): ...

where t2(in_a=t1()), when t2 does in_a.open(pd.DataFrame).all(), it should get a DataFrame
with only one column.

+-----------------------------+-----------------------------------------+--------------------------------------+
|                             |          StructuredDatasetType of the incoming Literal                         |
+-----------------------------+-----------------------------------------+--------------------------------------+
| StructuredDatasetType       | Has columns defined                     |  [] columns or None                  |
| of currently running task   |                                         |                                      |
+=============================+=========================================+======================================+
|    Has columns              | The StructuredDatasetType passed to the decoder will have the columns          |
|    defined                  | as defined by the type annotation of the currently running task.               |
|                             |                                                                                |
|                             | Decoders **should** then subset the incoming data to the columns requested.    |
|                             |                                                                                |
+-----------------------------+-----------------------------------------+--------------------------------------+
|   [] columns or None        | StructuredDatasetType passed to decoder | StructuredDatasetType passed to the  |
|                             | will have the columns from the incoming | decoder will have an empty list of   |
|                             | Literal. This is the scenario where     | columns.                             |
|                             | the Literal returned by the running     |                                      |
|                             | task will have more information than    |                                      |
|                             | the running task's signature.           |                                      |
+-----------------------------+-----------------------------------------+--------------------------------------+


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[T] \| StructuredDataset` |

#### dict_to_structured_dataset()

```python
def dict_to_structured_dataset(
    dict_obj: typing.Dict[str, str],
    expected_python_type: Type[T] | StructuredDataset,
) -> T | StructuredDataset
```
| Parameter | Type |
|-|-|
| `dict_obj` | `typing.Dict[str, str]` |
| `expected_python_type` | `Type[T] \| StructuredDataset` |

#### encode()

```python
def encode(
    ctx: FlyteContext,
    sd: StructuredDataset,
    df_type: Type,
    protocol: str,
    format: str,
    structured_literal_type: StructuredDatasetType,
) -> Literal
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `sd` | `StructuredDataset` |
| `df_type` | `Type` |
| `protocol` | `str` |
| `format` | `str` |
| `structured_literal_type` | `StructuredDatasetType` |

#### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: Binary,
    expected_python_type: Type[T] | StructuredDataset,
) -> T | StructuredDataset
```
If the input is from flytekit, the Life Cycle will be as follows:

Life Cycle:
binary IDL                 -> resolved binary         -> bytes                   -> expected Python object
(flytekit customized          (propeller processing)     (flytekit binary IDL)      (flytekit customized
serialization)                                                                       deserialization)

Example Code:
@dataclass
class DC:
sd: StructuredDataset

@workflow
def wf(dc: DC):
t_sd(dc.sd)

Note:
- The deserialization is the same as put a structured dataset in a dataclass, which will deserialize by the mashumaro's API.

Related PR:
- Title: Override Dataclass Serialization/Deserialization Behavior for FlyteTypes via Mashumaro
- Link: https://github.com/flyteorg/flytekit/pull/2554


| Parameter | Type |
|-|-|
| `binary_idl_object` | `Binary` |
| `expected_python_type` | `Type[T] \| StructuredDataset` |

#### from_generic_idl()

```python
def from_generic_idl(
    generic: Struct,
    expected_python_type: Type[T] | StructuredDataset,
) -> T | StructuredDataset
```
If the input is from Flyte Console, the Life Cycle will be as follows:

Life Cycle:
json str            -> protobuf struct         -> resolved protobuf struct   -> expected Python object
(console user input)   (console output)           (propeller)                   (flytekit customized deserialization)

Example Code:
@dataclass
class DC:
sd: StructuredDataset

@workflow
def wf(dc: DC):
t_sd(dc.sd)

Note:
- The deserialization is the same as put a structured dataset in a dataclass, which will deserialize by the mashumaro's API.

Related PR:
- Title: Override Dataclass Serialization/Deserialization Behavior for FlyteTypes via Mashumaro
- Link: https://github.com/flyteorg/flytekit/pull/2554


| Parameter | Type |
|-|-|
| `generic` | `Struct` |
| `expected_python_type` | `Type[T] \| StructuredDataset` |

#### get_decoder()

```python
def get_decoder(
    df_type: Type,
    protocol: str,
    format: str,
)
```
| Parameter | Type |
|-|-|
| `df_type` | `Type` |
| `protocol` | `str` |
| `format` | `str` |

#### get_encoder()

```python
def get_encoder(
    df_type: Type,
    protocol: str,
    format: str,
)
```
| Parameter | Type |
|-|-|
| `df_type` | `Type` |
| `protocol` | `str` |
| `format` | `str` |

#### get_literal_type()

```python
def get_literal_type(
    t: typing.Union[Type[StructuredDataset], typing.Any],
) -> LiteralType
```
Provide a concrete implementation so that writers of custom dataframe handlers since there's nothing that
special about the literal type. Any dataframe type will always be associated with the structured dataset type.
The other aspects of it - columns, external schema type, etc. can be read from associated metadata.



| Parameter | Type |
|-|-|
| `t` | `typing.Union[Type[StructuredDataset], typing.Any]` |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> Type[StructuredDataset]
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

#### iter_as()

```python
def iter_as(
    ctx: FlyteContext,
    sd: literals.StructuredDataset,
    df_type: Type[DF],
    updated_metadata: StructuredDatasetMetadata,
) -> typing.Iterator[DF]
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `sd` | `literals.StructuredDataset` |
| `df_type` | `Type[DF]` |
| `updated_metadata` | `StructuredDatasetMetadata` |

#### open_as()

```python
def open_as(
    ctx: FlyteContext,
    sd: literals.StructuredDataset,
    df_type: Type[DF],
    updated_metadata: StructuredDatasetMetadata,
) -> DF
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `sd` | `literals.StructuredDataset` |
| `df_type` | `Type[DF]` |
| `updated_metadata` | `StructuredDatasetMetadata` |

#### register()

```python
def register(
    h: Handlers,
    default_for_type: bool,
    override: bool,
    default_format_for_type: bool,
    default_storage_for_type: bool,
)
```
Call this with any Encoder or Decoder to register it with the flytekit type system. If your handler does not
specify a protocol (e.g. s3, gs, etc.) field, then



| Parameter | Type |
|-|-|
| `h` | `Handlers` |
| `default_for_type` | `bool` |
| `override` | `bool` |
| `default_format_for_type` | `bool` |
| `default_storage_for_type` | `bool` |

#### register_for_protocol()

```python
def register_for_protocol(
    h: Handlers,
    protocol: str,
    default_for_type: bool,
    override: bool,
    default_format_for_type: bool,
    default_storage_for_type: bool,
)
```
See the main register function instead.


| Parameter | Type |
|-|-|
| `h` | `Handlers` |
| `protocol` | `str` |
| `default_for_type` | `bool` |
| `override` | `bool` |
| `default_format_for_type` | `bool` |
| `default_storage_for_type` | `bool` |

#### register_renderer()

```python
def register_renderer(
    python_type: Type,
    renderer: Renderable,
)
```
| Parameter | Type |
|-|-|
| `python_type` | `Type` |
| `renderer` | `Renderable` |

#### to_html()

```python
def to_html(
    ctx: FlyteContext,
    python_val: typing.Any,
    expected_python_type: Type[T],
) -> str
```
Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `typing.Any` |
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

## flytekit.types.structured.structured_dataset.StructuredDatasetType

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

## flytekit.types.structured.structured_dataset.TypeEngine

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

## flytekit.types.structured.structured_dataset.TypeTransformerFailedError

Inappropriate argument type.


