---
title: flytekit.core.type_engine
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.type_engine

## Directory

### Classes

| Class | Description |
|-|-|
| [`ABC`](.././flytekit.core.type_engine#flytekitcoretype_engineabc) | Helper class that provides a standard way to create an ABC using. |
| [`Any`](.././flytekit.core.type_engine#flytekitcoretype_engineany) | Special type indicating an unconstrained type. |
| [`AsyncTypeTransformer`](.././flytekit.core.type_engine#flytekitcoretype_engineasynctypetransformer) | Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`BatchSize`](.././flytekit.core.type_engine#flytekitcoretype_enginebatchsize) | This is used to annotate a FlyteDirectory when we want to download/upload the contents of the directory in batches. |
| [`Binary`](.././flytekit.core.type_engine#flytekitcoretype_enginebinary) |  |
| [`BinaryIOTransformer`](.././flytekit.core.type_engine#flytekitcoretype_enginebinaryiotransformer) | Handler for BinaryIO. |
| [`DataClassJSONMixin`](.././flytekit.core.type_engine#flytekitcoretype_enginedataclassjsonmixin) |  |
| [`DataClassJsonMixin`](.././flytekit.core.type_engine#flytekitcoretype_enginedataclassjsonmixin) | DataClassJsonMixin is an ABC that functions as a Mixin. |
| [`DataclassTransformer`](.././flytekit.core.type_engine#flytekitcoretype_enginedataclasstransformer) | The Dataclass Transformer provides a type transformer for dataclasses. |
| [`DictTransformer`](.././flytekit.core.type_engine#flytekitcoretype_enginedicttransformer) | Transformer that transforms an univariate dictionary Dict[str, T] to a Literal Map or. |
| [`EnumTransformer`](.././flytekit.core.type_engine#flytekitcoretype_engineenumtransformer) | Enables converting a python type enum. |
| [`FlyteAnnotation`](.././flytekit.core.type_engine#flytekitcoretype_engineflyteannotation) | A core object to add arbitrary annotations to flyte types. |
| [`FlyteContext`](.././flytekit.core.type_engine#flytekitcoretype_engineflytecontext) | This is an internal-facing context object, that most users will not have to deal with. |
| [`GenericAlias`](.././flytekit.core.type_engine#flytekitcoretype_enginegenericalias) | Represent a PEP 585 generic type. |
| [`HashMethod`](.././flytekit.core.type_engine#flytekitcoretype_enginehashmethod) | Flyte-specific object used to wrap the hash function for a specific type. |
| [`JSONDecoder`](.././flytekit.core.type_engine#flytekitcoretype_enginejsondecoder) | Abstract base class for generic types. |
| [`JSONEncoder`](.././flytekit.core.type_engine#flytekitcoretype_enginejsonencoder) | Abstract base class for generic types. |
| [`ListTransformer`](.././flytekit.core.type_engine#flytekitcoretype_enginelisttransformer) | Transformer that handles a univariate typing. |
| [`Literal`](.././flytekit.core.type_engine#flytekitcoretype_engineliteral) |  |
| [`LiteralCollection`](.././flytekit.core.type_engine#flytekitcoretype_engineliteralcollection) |  |
| [`LiteralMap`](.././flytekit.core.type_engine#flytekitcoretype_engineliteralmap) |  |
| [`LiteralType`](.././flytekit.core.type_engine#flytekitcoretype_engineliteraltype) |  |
| [`LiteralsResolver`](.././flytekit.core.type_engine#flytekitcoretype_engineliteralsresolver) | LiteralsResolver is a helper class meant primarily for use with the FlyteRemote experience or any other situation. |
| [`Message`](.././flytekit.core.type_engine#flytekitcoretype_enginemessage) | Abstract base class for protocol messages. |
| [`MessagePackDecoder`](.././flytekit.core.type_engine#flytekitcoretype_enginemessagepackdecoder) | Abstract base class for generic types. |
| [`MessagePackEncoder`](.././flytekit.core.type_engine#flytekitcoretype_enginemessagepackencoder) | Abstract base class for generic types. |
| [`OrderedDict`](.././flytekit.core.type_engine#flytekitcoretype_engineordereddict) | Dictionary that remembers insertion order. |
| [`Primitive`](.././flytekit.core.type_engine#flytekitcoretype_engineprimitive) |  |
| [`ProtobufTransformer`](.././flytekit.core.type_engine#flytekitcoretype_engineprotobuftransformer) | Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`RestrictedTypeTransformer`](.././flytekit.core.type_engine#flytekitcoretype_enginerestrictedtypetransformer) | Types registered with the RestrictedTypeTransformer are not allowed to be converted to and from literals. |
| [`Scalar`](.././flytekit.core.type_engine#flytekitcoretype_enginescalar) |  |
| [`SimpleTransformer`](.././flytekit.core.type_engine#flytekitcoretype_enginesimpletransformer) | A Simple implementation of a type transformer that uses simple lambdas to transform and reduces boilerplate. |
| [`SimpleType`](.././flytekit.core.type_engine#flytekitcoretype_enginesimpletype) |  |
| [`Struct`](.././flytekit.core.type_engine#flytekitcoretype_enginestruct) | A ProtocolMessage. |
| [`TextIOTransformer`](.././flytekit.core.type_engine#flytekitcoretype_enginetextiotransformer) | Handler for TextIO. |
| [`TypeAnnotationModel`](.././flytekit.core.type_engine#flytekitcoretype_enginetypeannotationmodel) | Python class representation of the flyteidl TypeAnnotation message. |
| [`TypeEngine`](.././flytekit.core.type_engine#flytekitcoretype_enginetypeengine) | Core Extensible TypeEngine of Flytekit. |
| [`TypeStructure`](.././flytekit.core.type_engine#flytekitcoretype_enginetypestructure) | Models _types_pb2. |
| [`TypeTransformer`](.././flytekit.core.type_engine#flytekitcoretype_enginetypetransformer) | Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`Union`](.././flytekit.core.type_engine#flytekitcoretype_engineunion) |  |
| [`UnionTransformer`](.././flytekit.core.type_engine#flytekitcoretype_engineuniontransformer) | Transformer that handles a typing. |
| [`UnionType`](.././flytekit.core.type_engine#flytekitcoretype_engineuniontype) | Models _types_pb2. |
| [`Void`](.././flytekit.core.type_engine#flytekitcoretype_enginevoid) |  |
| [`timeit`](.././flytekit.core.type_engine#flytekitcoretype_enginetimeit) | A context manager and a decorator that measures the execution time of the wrapped code block or functions. |

### Errors

| Exception | Description |
|-|-|
| [`RestrictedTypeError`](.././flytekit.core.type_engine#flytekitcoretype_enginerestrictedtypeerror) | Common base class for all non-exit exceptions. |
| [`TypeTransformerFailedError`](.././flytekit.core.type_engine#flytekitcoretype_enginetypetransformerfailederror) | Inappropriate argument type. |

### Methods

| Method | Description |
|-|-|
| [`NamedTuple()`](#namedtuple) | Typed version of namedtuple. |
| [`_MessageToDict()`](#_messagetodict) | Converts protobuf message to a dictionary. |
| [`_ParseDict()`](#_parsedict) | Parses a JSON dictionary representation into a message. |
| [`_add_tag_to_type()`](#_add_tag_to_type) |  |
| [`_are_types_castable()`](#_are_types_castable) |  |
| [`_check_and_convert_void()`](#_check_and_convert_void) |  |
| [`_check_and_covert_float()`](#_check_and_covert_float) |  |
| [`_default_msgpack_decoder()`](#_default_msgpack_decoder) |  |
| [`_get_element_type()`](#_get_element_type) |  |
| [`_handle_flyte_console_float_input_to_int()`](#_handle_flyte_console_float_input_to_int) | Flyte Console is written by JavaScript and JavaScript has only one number type which is Number. |
| [`_is_union_type()`](#_is_union_type) | Returns True if t is a Union type. |
| [`_register_default_type_transformers()`](#_register_default_type_transformers) |  |
| [`_run_coros_in_chunks()`](#_run_coros_in_chunks) | Run the given coroutines in  chunks. |
| [`_type_essence()`](#_type_essence) |  |
| [`abstractmethod()`](#abstractmethod) | A decorator indicating abstract methods. |
| [`cast()`](#cast) | Cast a value to a type. |
| [`convert_marshmallow_json_schema_to_python_class()`](#convert_marshmallow_json_schema_to_python_class) | Generate a model class based on the provided JSON Schema. |
| [`convert_mashumaro_json_schema_to_python_class()`](#convert_mashumaro_json_schema_to_python_class) | Generate a model class based on the provided JSON Schema. |
| [`dataclass_from_dict()`](#dataclass_from_dict) | Utility function to construct a dataclass object from dict. |
| [`dataclass_json()`](#dataclass_json) | Based on the code in the `dataclasses` module to handle optional-parens. |
| [`generate_attribute_list_from_dataclass_json()`](#generate_attribute_list_from_dataclass_json) |  |
| [`generate_attribute_list_from_dataclass_json_mixin()`](#generate_attribute_list_from_dataclass_json_mixin) |  |
| [`get_args()`](#get_args) | Get type arguments with all substitutions performed. |
| [`get_batch_size()`](#get_batch_size) |  |
| [`get_origin()`](#get_origin) | Get the unsubscripted version of a type. |
| [`get_underlying_type()`](#get_underlying_type) | Return the underlying type for annotated types or the type itself. |
| [`is_annotated()`](#is_annotated) |  |
| [`is_imported()`](#is_imported) | This function is used to check if a module has been imported by the regular import. |
| [`literal_map_string_repr()`](#literal_map_string_repr) | This method is used to convert a literal map to a string representation. |
| [`literal_types_match()`](#literal_types_match) | Returns if two LiteralTypes are the same. |
| [`load_proto_from_file()`](#load_proto_from_file) |  |
| [`load_type_from_tag()`](#load_type_from_tag) | Loads python type from tag. |
| [`lru_cache()`](#lru_cache) | Least-recently-used cache decorator. |
| [`modify_literal_uris()`](#modify_literal_uris) | Modifies the literal object recursively to replace the URIs with the native paths in case they are of. |
| [`str2bool()`](#str2bool) | Convert a string to a boolean. |
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
| `annotations` | `_Feature` |  |
| `logger` | `Logger` |  |
| `loop_manager` | `_AsyncLoopManager` |  |

## Methods

#### NamedTuple()

```python
def NamedTuple(
    typename,
    fields,
    kwargs,
)
```
Typed version of namedtuple.

Usage::

class Employee(NamedTuple):
name: str
id: int

This is equivalent to::

Employee = collections.namedtuple('Employee', ['name', 'id'])

The resulting class has an extra __annotations__ attribute, giving a
dict that maps field names to types.  (The field names are also in
the _fields attribute, which is part of the namedtuple API.)
An alternative equivalent functional syntax is also accepted::

Employee = NamedTuple('Employee', [('name', str), ('id', int)])


| Parameter | Type |
|-|-|
| `typename` |  |
| `fields` |  |
| `kwargs` | ``**kwargs`` |

#### _MessageToDict()

```python
def _MessageToDict(
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

#### _ParseDict()

```python
def _ParseDict(
    js_dict,
    message,
    ignore_unknown_fields,
    descriptor_pool,
    max_recursion_depth,
)
```
Parses a JSON dictionary representation into a message.



| Parameter | Type |
|-|-|
| `js_dict` |  |
| `message` |  |
| `ignore_unknown_fields` |  |
| `descriptor_pool` |  |
| `max_recursion_depth` |  |

#### _add_tag_to_type()

```python
def _add_tag_to_type(
    x: LiteralType,
    tag: str,
) -> LiteralType
```
| Parameter | Type |
|-|-|
| `x` | `LiteralType` |
| `tag` | `str` |

#### _are_types_castable()

```python
def _are_types_castable(
    upstream: LiteralType,
    downstream: LiteralType,
) -> bool
```
| Parameter | Type |
|-|-|
| `upstream` | `LiteralType` |
| `downstream` | `LiteralType` |

#### _check_and_convert_void()

```python
def _check_and_convert_void(
    lv: Literal,
)
```
| Parameter | Type |
|-|-|
| `lv` | `Literal` |

#### _check_and_covert_float()

```python
def _check_and_covert_float(
    lv: Literal,
) -> float
```
| Parameter | Type |
|-|-|
| `lv` | `Literal` |

#### _default_msgpack_decoder()

```python
def _default_msgpack_decoder(
    data: bytes,
) -> Any
```
| Parameter | Type |
|-|-|
| `data` | `bytes` |

#### _get_element_type()

```python
def _get_element_type(
    element_property: typing.Dict[str, str],
) -> Type
```
| Parameter | Type |
|-|-|
| `element_property` | `typing.Dict[str, str]` |

#### _handle_flyte_console_float_input_to_int()

```python
def _handle_flyte_console_float_input_to_int(
    lv: Literal,
) -> int
```
Flyte Console is written by JavaScript and JavaScript has only one number type which is Number.
Sometimes it keeps track of trailing 0s and sometimes it doesn't.
We have to convert float to int back in the following example.

Example Code:
@dataclass
class DC:
a: int

@workflow
def wf(dc: DC):
t_int(a=dc.a)

Life Cycle:
json str            -> protobuf struct         -> resolved float    -> float                          -> int
(console user input)   (console output)           (propeller)          (flytekit simple transformer)  (_handle_flyte_console_float_input_to_int)


| Parameter | Type |
|-|-|
| `lv` | `Literal` |

#### _is_union_type()

```python
def _is_union_type(
    t,
)
```
Returns True if t is a Union type.


| Parameter | Type |
|-|-|
| `t` |  |

#### _register_default_type_transformers()

```python
def _register_default_type_transformers()
```
#### _run_coros_in_chunks()

```python
def _run_coros_in_chunks(
    coros,
    batch_size,
    callback,
    timeout,
    return_exceptions,
    nofiles,
)
```
Run the given coroutines in  chunks.

Parameters
----------
coros: list of coroutines to run
batch_size: int or None
Number of coroutines to submit/wait on simultaneously.
If -1, then it will not be any throttling. If
None, it will be inferred from _get_batch_size()
callback: fsspec.callbacks.Callback instance
Gets a relative_update when each coroutine completes
timeout: number or None
If given, each coroutine times out after this time. Note that, since
there are multiple batches, the total run time of this function will in
general be longer
return_exceptions: bool
Same meaning as in asyncio.gather
nofiles: bool
If inferring the batch_size, does this operation involve local files?
If yes, you normally expect smaller batches.


| Parameter | Type |
|-|-|
| `coros` |  |
| `batch_size` |  |
| `callback` |  |
| `timeout` |  |
| `return_exceptions` |  |
| `nofiles` |  |

#### _type_essence()

```python
def _type_essence(
    x: LiteralType,
) -> LiteralType
```
| Parameter | Type |
|-|-|
| `x` | `LiteralType` |

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

#### cast()

```python
def cast(
    typ,
    val,
)
```
Cast a value to a type.

This returns the value unchanged.  To the type checker this
signals that the return value has the designated type, but at
runtime we intentionally don't check anything (we want this
to be as fast as possible).


| Parameter | Type |
|-|-|
| `typ` |  |
| `val` |  |

#### convert_marshmallow_json_schema_to_python_class()

```python
def convert_marshmallow_json_schema_to_python_class(
    schema: dict,
    schema_name: typing.Any,
) -> type
```
Generate a model class based on the provided JSON Schema


| Parameter | Type |
|-|-|
| `schema` | `dict` |
| `schema_name` | `typing.Any` |

#### convert_mashumaro_json_schema_to_python_class()

```python
def convert_mashumaro_json_schema_to_python_class(
    schema: dict,
    schema_name: typing.Any,
) -> type
```
Generate a model class based on the provided JSON Schema


| Parameter | Type |
|-|-|
| `schema` | `dict` |
| `schema_name` | `typing.Any` |

#### dataclass_from_dict()

```python
def dataclass_from_dict(
    cls: type,
    src: typing.Dict[str, typing.Any],
) -> typing.Any
```
Utility function to construct a dataclass object from dict


| Parameter | Type |
|-|-|
| `cls` | `type` |
| `src` | `typing.Dict[str, typing.Any]` |

#### dataclass_json()

```python
def dataclass_json(
    _cls,
    letter_case,
    undefined: typing.Union[str, dataclasses_json.undefined.Undefined, NoneType],
)
```
Based on the code in the `dataclasses` module to handle optional-parens
decorators. See example below:

@dataclass_json
@dataclass_json(letter_case=LetterCase.CAMEL)
class Example:
...


| Parameter | Type |
|-|-|
| `_cls` |  |
| `letter_case` |  |
| `undefined` | `typing.Union[str, dataclasses_json.undefined.Undefined, NoneType]` |

#### generate_attribute_list_from_dataclass_json()

```python
def generate_attribute_list_from_dataclass_json(
    schema: dict,
    schema_name: typing.Any,
)
```
| Parameter | Type |
|-|-|
| `schema` | `dict` |
| `schema_name` | `typing.Any` |

#### generate_attribute_list_from_dataclass_json_mixin()

```python
def generate_attribute_list_from_dataclass_json_mixin(
    schema: dict,
    schema_name: typing.Any,
)
```
| Parameter | Type |
|-|-|
| `schema` | `dict` |
| `schema_name` | `typing.Any` |

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

#### get_batch_size()

```python
def get_batch_size(
    t: Type,
) -> Optional[int]
```
| Parameter | Type |
|-|-|
| `t` | `Type` |

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

#### get_underlying_type()

```python
def get_underlying_type(
    t: Type,
) -> Type
```
Return the underlying type for annotated types or the type itself


| Parameter | Type |
|-|-|
| `t` | `Type` |

#### is_annotated()

```python
def is_annotated(
    t: Type,
) -> bool
```
| Parameter | Type |
|-|-|
| `t` | `Type` |

#### is_imported()

```python
def is_imported(
    module_name,
)
```
This function is used to check if a module has been imported by the regular import.
Return false if module is lazy imported and not used yet.


| Parameter | Type |
|-|-|
| `module_name` |  |

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

#### load_proto_from_file()

```python
def load_proto_from_file(
    pb2_type,
    path,
)
```
| Parameter | Type |
|-|-|
| `pb2_type` |  |
| `path` |  |

#### load_type_from_tag()

```python
def load_type_from_tag(
    tag: str,
) -> typing.Type[~T]
```
Loads python type from tag


| Parameter | Type |
|-|-|
| `tag` | `str` |

#### lru_cache()

```python
def lru_cache(
    maxsize,
    typed,
)
```
Least-recently-used cache decorator.

If *maxsize* is set to None, the LRU features are disabled and the cache
can grow without bound.

If *typed* is True, arguments of different types will be cached separately.
For example, f(decimal.Decimal("3.0")) and f(3.0) will be treated as
distinct calls with distinct results. Some types such as str and int may
be cached separately even when typed is false.

Arguments to the cached function must be hashable.

View the cache statistics named tuple (hits, misses, maxsize, currsize)
with f.cache_info().  Clear the cache and statistics with f.cache_clear().
Access the underlying function with f.__wrapped__.

See:  https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)


| Parameter | Type |
|-|-|
| `maxsize` |  |
| `typed` |  |

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

#### str2bool()

```python
def str2bool(
    value: typing.Optional[str],
) -> bool
```
Convert a string to a boolean. This is useful for parsing environment variables.


| Parameter | Type |
|-|-|
| `value` | `typing.Optional[str]` |

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


| Parameter | Type |
|-|-|
| `input_val` | `typing.Any` |
| `target_literal_type` | `LiteralType` |

## flytekit.core.type_engine.ABC

Helper class that provides a standard way to create an ABC using
inheritance.


## flytekit.core.type_engine.Any

Special type indicating an unconstrained type.

- Any is compatible with every type.
- Any assumed to have all methods.
- All values assumed to be instances of Any.

Note that all the above statements are true from the point of view of
static type checkers. At runtime, Any should not be used with instance
checks.


## flytekit.core.type_engine.AsyncTypeTransformer

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

## flytekit.core.type_engine.BatchSize

This is used to annotate a FlyteDirectory when we want to download/upload the contents of the directory in batches. For example,

```python
@task
def t1(directory: Annotated[FlyteDirectory, BatchSize(10)]) -> Annotated[FlyteDirectory, BatchSize(100)]:
...
return FlyteDirectory(...)
```

In the above example flytekit will download all files from the input `directory` in chunks of 10, i.e. first it
downloads 10 files, loads them to memory, then writes those 10 to local disk, then it loads the next 10, so on
and so forth. Similarly, for outputs, in this case flytekit is going to upload the resulting directory in chunks of
100.


```python
class BatchSize(
    val: int,
)
```
| Parameter | Type |
|-|-|
| `val` | `int` |

### Properties

| Property | Type | Description |
|-|-|-|
| `val` |  |  |

## flytekit.core.type_engine.Binary

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

## flytekit.core.type_engine.BinaryIOTransformer

Handler for BinaryIO


```python
def BinaryIOTransformer()
```
### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
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
    t: Type[typing.BinaryIO],
) -> LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type |
|-|-|
| `t` | `Type[typing.BinaryIO]` |

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
    python_val: typing.BinaryIO,
    python_type: Type[typing.BinaryIO],
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
| `python_val` | `typing.BinaryIO` |
| `python_type` | `Type[typing.BinaryIO]` |
| `expected` | `LiteralType` |

#### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[typing.BinaryIO],
) -> typing.BinaryIO
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[typing.BinaryIO]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_async` |  |  |
| `name` |  |  |
| `python_type` |  | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` |  | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

## flytekit.core.type_engine.DataClassJSONMixin

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

## flytekit.core.type_engine.DataClassJsonMixin

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

## flytekit.core.type_engine.DataclassTransformer

The Dataclass Transformer provides a type transformer for dataclasses.

The dataclass is converted to and from MessagePack Bytes by the mashumaro library
and is transported between tasks using the Binary IDL representation.
Also, the type declaration will try to extract the JSON Schema for the
object, if possible, and pass it with the definition.

The lifecycle of the dataclass in the Flyte type system is as follows:

1. Serialization: The dataclass transformer converts the dataclass to MessagePack Bytes.
(1) Handle dataclass attributes to make them serializable with mashumaro.
(2) Use the mashumaro API to serialize the dataclass to MessagePack Bytes.
(3) Use MessagePack Bytes to create a Flyte Literal.
(4) Serialize the Flyte Literal to a Binary IDL Object.

2. Deserialization: The dataclass transformer converts the MessagePack Bytes back to a dataclass.
(1) Convert MessagePack Bytes to a dataclass using mashumaro.
(2) Handle dataclass attributes to ensure they are of the correct types.

For Json Schema, we use https://github.com/fuhrysteve/marshmallow-jsonschema library.

Example

.. code-block:: python

@dataclass
class Test(DataClassJsonMixin):
a: int
b: str

from marshmallow_jsonschema import JSONSchema
t = Test(a=10,b="e")
JSONSchema().dump(t.schema())

Output will look like

.. code-block:: json

{'$schema': 'http://json-schema.org/draft-07/schema#',
'definitions': {'TestSchema': {'properties': {'a': {'title': 'a',
'type': 'number',
'format': 'integer'},
'b': {'title': 'b', 'type': 'string'}},
'type': 'object',
'additionalProperties': False}},
'$ref': '#/definitions/TestSchema'}

.. note::

The schema support is experimental and is useful for auto-completing in the UI/CLI


```python
def DataclassTransformer()
```
### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`from_binary_idl()`](#from_binary_idl) | This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access. |
| [`from_generic_idl()`](#from_generic_idl) | TODO: Support all Flyte Types. |
| [`get_literal_type()`](#get_literal_type) | Extracts the Literal type definition for a Dataclass and returns a type Struct. |
| [`isinstance_generic()`](#isinstance_generic) |  |
| [`to_generic_literal()`](#to_generic_literal) | Serializes a dataclass or dictionary to a Flyte literal, handling both JSON and MessagePack formats. |
| [`to_html()`](#to_html) | Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div. |
| [`to_literal()`](#to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`to_python_value()`](#to_python_value) | Converts the given Literal to a Python Type. |


#### assert_type()

```python
def assert_type(
    expected_type: Type[DataClassJsonMixin],
    v: T,
)
```
| Parameter | Type |
|-|-|
| `expected_type` | `Type[DataClassJsonMixin]` |
| `v` | `T` |

#### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: Binary,
    expected_python_type: Type[T],
) -> T
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
Extracts the Literal type definition for a Dataclass and returns a type Struct.
If possible also extracts the JSONSchema for the dataclass.


| Parameter | Type |
|-|-|
| `t` | `Type[T]` |

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

#### to_generic_literal()

```python
def to_generic_literal(
    ctx: FlyteContext,
    python_val: T,
    python_type: Type[T],
    expected: LiteralType,
) -> Literal
```
Serializes a dataclass or dictionary to a Flyte literal, handling both JSON and MessagePack formats.
Set `FLYTE_USE_OLD_DC_FORMAT=true` to use the old JSON-based format.
Note: This is deprecated and will be removed in the future.


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `T` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

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

#### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
) -> T
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

## flytekit.core.type_engine.DictTransformer

Transformer that transforms an univariate dictionary Dict[str, T] to a Literal Map or
transforms an untyped dictionary to a Binary Scalar Literal with a Struct Literal Type.


```python
def DictTransformer()
```
### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`async_to_literal()`](#async_to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`async_to_python_value()`](#async_to_python_value) | Converts the given Literal to a Python Type. |
| [`dict_to_binary_literal()`](#dict_to_binary_literal) | Converts a Python dictionary to a Flyte-specific ``Literal`` using MessagePack encoding. |
| [`dict_to_generic_literal()`](#dict_to_generic_literal) | This is deprecated from flytekit 1. |
| [`extract_types()`](#extract_types) |  |
| [`from_binary_idl()`](#from_binary_idl) | This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access. |
| [`from_generic_idl()`](#from_generic_idl) | TODO: Support all Flyte Types. |
| [`get_literal_type()`](#get_literal_type) | Transforms a native python dictionary to a flyte-specific ``LiteralType``. |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type. |
| [`is_pickle()`](#is_pickle) |  |
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
    python_val: typing.Any,
    python_type: Type[dict],
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
| `python_type` | `Type[dict]` |
| `expected` | `LiteralType` |

#### async_to_python_value()

```python
def async_to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[dict],
) -> dict
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[dict]` |

#### dict_to_binary_literal()

```python
def dict_to_binary_literal(
    ctx: FlyteContext,
    v: dict,
    python_type: Type[dict],
    allow_pickle: bool,
) -> Literal
```
Converts a Python dictionary to a Flyte-specific ``Literal`` using MessagePack encoding.
Falls back to Pickle if encoding fails and `allow_pickle` is True.


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `v` | `dict` |
| `python_type` | `Type[dict]` |
| `allow_pickle` | `bool` |

#### dict_to_generic_literal()

```python
def dict_to_generic_literal(
    ctx: FlyteContext,
    v: dict,
    python_type: Type[dict],
    allow_pickle: bool,
) -> Literal
```
This is deprecated from flytekit 1.14.0.
Creates a flyte-specific ``Literal`` value from a native python dictionary.
Note: This is deprecated and will be removed in the future.


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `v` | `dict` |
| `python_type` | `Type[dict]` |
| `allow_pickle` | `bool` |

#### extract_types()

```python
def extract_types(
    t: Optional[Type[dict]],
) -> typing.Tuple
```
| Parameter | Type |
|-|-|
| `t` | `Optional[Type[dict]]` |

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
    t: Type[dict],
) -> LiteralType
```
Transforms a native python dictionary to a flyte-specific ``LiteralType``


| Parameter | Type |
|-|-|
| `t` | `Type[dict]` |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> Union[Type[dict], typing.Dict[Type, Type]]
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type |
|-|-|
| `literal_type` | `LiteralType` |

#### is_pickle()

```python
def is_pickle(
    python_type: Type[dict],
) -> bool
```
| Parameter | Type |
|-|-|
| `python_type` | `Type[dict]` |

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

## flytekit.core.type_engine.EnumTransformer

Enables converting a python type enum.Enum to LiteralType.EnumType


```python
def EnumTransformer()
```
### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
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
    t: Type[enum.Enum],
    v: T,
)
```
| Parameter | Type |
|-|-|
| `t` | `Type[enum.Enum]` |
| `v` | `T` |

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
) -> Type[enum.Enum]
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
    python_val: enum.Enum,
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
| `python_val` | `enum.Enum` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
) -> T
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

## flytekit.core.type_engine.FlyteAnnotation

A core object to add arbitrary annotations to flyte types.

This metadata is ingested as a python dictionary and will be serialized
into fields on the flyteidl type literals. This data is not accessible at
runtime but rather can be retrieved from flyteadmin for custom presentation
of typed parameters.

Flytekit expects to receive a maximum of one `FlyteAnnotation` object
within each typehint.

For a task definition:

.. code-block:: python

@task
def x(a: typing.Annotated[int, FlyteAnnotation({"foo": {"bar": 1}})]):
return


```python
class FlyteAnnotation(
    data: typing.Dict[str, typing.Any],
)
```
| Parameter | Type |
|-|-|
| `data` | `typing.Dict[str, typing.Any]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `data` |  |  |

## flytekit.core.type_engine.FlyteContext

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

## flytekit.core.type_engine.GenericAlias

Represent a PEP 585 generic type

E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).


## flytekit.core.type_engine.HashMethod

Flyte-specific object used to wrap the hash function for a specific type


```python
class HashMethod(
    function: typing.Callable[[~T], str],
)
```
| Parameter | Type |
|-|-|
| `function` | `typing.Callable[[~T], str]` |

### Methods

| Method | Description |
|-|-|
| [`calculate()`](#calculate) | Calculate hash for `obj`. |


#### calculate()

```python
def calculate(
    obj: ~T,
) -> str
```
Calculate hash for `obj`.


| Parameter | Type |
|-|-|
| `obj` | `~T` |

## flytekit.core.type_engine.JSONDecoder

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


```python
class JSONDecoder(
    shape_type: typing.Union[typing.Type[~T], typing.Any],
    default_dialect: typing.Optional[typing.Type[mashumaro.dialect.Dialect]],
    pre_decoder_func: collections.abc.Callable[[typing.Union[str, bytes, bytearray]], typing.Any],
)
```
| Parameter | Type |
|-|-|
| `shape_type` | `typing.Union[typing.Type[~T], typing.Any]` |
| `default_dialect` | `typing.Optional[typing.Type[mashumaro.dialect.Dialect]]` |
| `pre_decoder_func` | `collections.abc.Callable[[typing.Union[str, bytes, bytearray]], typing.Any]` |

### Methods

| Method | Description |
|-|-|
| [`decode()`](#decode) |  |


#### decode()

```python
def decode(
    data: typing.Union[str, bytes, bytearray],
) -> ~T
```
| Parameter | Type |
|-|-|
| `data` | `typing.Union[str, bytes, bytearray]` |

## flytekit.core.type_engine.JSONEncoder

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


```python
class JSONEncoder(
    shape_type: typing.Union[typing.Type[~T], typing.Any],
    default_dialect: typing.Optional[typing.Type[mashumaro.dialect.Dialect]],
    post_encoder_func: collections.abc.Callable[[typing.Any], str],
)
```
| Parameter | Type |
|-|-|
| `shape_type` | `typing.Union[typing.Type[~T], typing.Any]` |
| `default_dialect` | `typing.Optional[typing.Type[mashumaro.dialect.Dialect]]` |
| `post_encoder_func` | `collections.abc.Callable[[typing.Any], str]` |

### Methods

| Method | Description |
|-|-|
| [`encode()`](#encode) |  |


#### encode()

```python
def encode(
    obj: ~T,
) -> str
```
| Parameter | Type |
|-|-|
| `obj` | `~T` |

## flytekit.core.type_engine.ListTransformer

Transformer that handles a univariate typing.List[T]


```python
def ListTransformer()
```
### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`async_to_literal()`](#async_to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`async_to_python_value()`](#async_to_python_value) | Converts the given Literal to a Python Type. |
| [`from_binary_idl()`](#from_binary_idl) | This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access. |
| [`from_generic_idl()`](#from_generic_idl) | TODO: Support all Flyte Types. |
| [`get_literal_type()`](#get_literal_type) | Only univariate Lists are supported in Flyte. |
| [`get_sub_type()`](#get_sub_type) | Return the generic Type T of the List. |
| [`get_sub_type_or_none()`](#get_sub_type_or_none) | Return the generic Type T of the List, or None if the generic type cannot be inferred. |
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
) -> typing.Optional[typing.List[T]]
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
) -> Optional[LiteralType]
```
Only univariate Lists are supported in Flyte


| Parameter | Type |
|-|-|
| `t` | `Type[T]` |

#### get_sub_type()

```python
def get_sub_type(
    t: Type[T],
) -> Type[T]
```
Return the generic Type T of the List


| Parameter | Type |
|-|-|
| `t` | `Type[T]` |

#### get_sub_type_or_none()

```python
def get_sub_type_or_none(
    t: Type[T],
) -> Optional[Type[T]]
```
Return the generic Type T of the List, or None if the generic type cannot be inferred


| Parameter | Type |
|-|-|
| `t` | `Type[T]` |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> list
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

## flytekit.core.type_engine.Literal

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

## flytekit.core.type_engine.LiteralCollection

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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> LiteralCollection
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
| `literals` |  |  |

## flytekit.core.type_engine.LiteralMap

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

## flytekit.core.type_engine.LiteralType

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

## flytekit.core.type_engine.LiteralsResolver

LiteralsResolver is a helper class meant primarily for use with the FlyteRemote experience or any other situation
where you might be working with LiteralMaps. This object allows the caller to specify the Python type that should
correspond to an element of the map.


```python
class LiteralsResolver(
    literals: typing.Dict[str, Literal],
    variable_map: Optional[Dict[str, _interface_models.Variable]],
    ctx: Optional[FlyteContext],
)
```
| Parameter | Type |
|-|-|
| `literals` | `typing.Dict[str, Literal]` |
| `variable_map` | `Optional[Dict[str, _interface_models.Variable]]` |
| `ctx` | `Optional[FlyteContext]` |

### Methods

| Method | Description |
|-|-|
| [`as_python_native()`](#as_python_native) | This should return the native Python representation, compatible with unpacking. |
| [`clear()`](#clear) | D. |
| [`copy()`](#copy) |  |
| [`fromkeys()`](#fromkeys) |  |
| [`get()`](#get) | This will get the ``attr`` value from the Literal map, and invoke the TypeEngine to convert it into a Python. |
| [`get_literal()`](#get_literal) |  |
| [`items()`](#items) | D. |
| [`keys()`](#keys) | D. |
| [`pop()`](#pop) | D. |
| [`popitem()`](#popitem) | D. |
| [`setdefault()`](#setdefault) | D. |
| [`update()`](#update) | D. |
| [`update_type_hints()`](#update_type_hints) |  |
| [`values()`](#values) | D. |


#### as_python_native()

```python
def as_python_native(
    python_interface: Interface,
) -> typing.Any
```
This should return the native Python representation, compatible with unpacking.
This function relies on Python interface outputs being ordered correctly.



| Parameter | Type |
|-|-|
| `python_interface` | `Interface` |

#### clear()

```python
def clear()
```
D.clear() -> None.  Remove all items from D.


#### copy()

```python
def copy()
```
#### fromkeys()

```python
def fromkeys(
    iterable,
    value,
)
```
| Parameter | Type |
|-|-|
| `iterable` |  |
| `value` |  |

#### get()

```python
def get(
    attr: str,
    as_type: Optional[typing.Type],
) -> typing.Any
```
This will get the ``attr`` value from the Literal map, and invoke the TypeEngine to convert it into a Python
native value. A Python type can optionally be supplied. If successful, the native value will be cached and
future calls will return the cached value instead.



| Parameter | Type |
|-|-|
| `attr` | `str` |
| `as_type` | `Optional[typing.Type]` |

#### get_literal()

```python
def get_literal(
    key: str,
) -> Literal
```
| Parameter | Type |
|-|-|
| `key` | `str` |

#### items()

```python
def items()
```
D.items() -> a set-like object providing a view on D's items


#### keys()

```python
def keys()
```
D.keys() -> a set-like object providing a view on D's keys


#### pop()

```python
def pop(
    key,
    default,
)
```
D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised.


| Parameter | Type |
|-|-|
| `key` |  |
| `default` |  |

#### popitem()

```python
def popitem()
```
D.popitem() -> (k, v), remove and return some (key, value) pair
as a 2-tuple; but raise KeyError if D is empty.


#### setdefault()

```python
def setdefault(
    key,
    default,
)
```
D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D


| Parameter | Type |
|-|-|
| `key` |  |
| `default` |  |

#### update()

```python
def update(
    other,
    kwds,
)
```
D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
If E present and has a .keys() method, does:     for k in E.keys(): D[k] = E[k]
If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k, v in F.items(): D[k] = v


| Parameter | Type |
|-|-|
| `other` |  |
| `kwds` |  |

#### update_type_hints()

```python
def update_type_hints(
    type_hints: typing.Dict[str, typing.Type],
)
```
| Parameter | Type |
|-|-|
| `type_hints` | `typing.Dict[str, typing.Type]` |

#### values()

```python
def values()
```
D.values() -> an object providing a view on D's values


### Properties

| Property | Type | Description |
|-|-|-|
| `literals` |  |  |
| `native_values` |  |  |
| `variable_map` |  |  |

## flytekit.core.type_engine.Message

Abstract base class for protocol messages.

Protocol message classes are almost always generated by the protocol
compiler.  These generated types subclass Message and implement the methods
shown below.


### Methods

| Method | Description |
|-|-|
| [`ByteSize()`](#bytesize) | Returns the serialized size of this message. |
| [`Clear()`](#clear) | Clears all data that was set in the message. |
| [`ClearExtension()`](#clearextension) | Clears the contents of a given extension. |
| [`ClearField()`](#clearfield) | Clears the contents of a given field. |
| [`CopyFrom()`](#copyfrom) | Copies the content of the specified message into the current message. |
| [`DiscardUnknownFields()`](#discardunknownfields) | Clears all fields in the :class:`UnknownFieldSet`. |
| [`FromString()`](#fromstring) |  |
| [`HasExtension()`](#hasextension) | Checks if a certain extension is present for this message. |
| [`HasField()`](#hasfield) | Checks if a certain field is set for the message. |
| [`IsInitialized()`](#isinitialized) | Checks if the message is initialized. |
| [`ListFields()`](#listfields) | Returns a list of (FieldDescriptor, value) tuples for present fields. |
| [`MergeFrom()`](#mergefrom) | Merges the contents of the specified message into current message. |
| [`MergeFromString()`](#mergefromstring) | Merges serialized protocol buffer data into this message. |
| [`ParseFromString()`](#parsefromstring) | Parse serialized protocol buffer data in binary form into this message. |
| [`SerializePartialToString()`](#serializepartialtostring) | Serializes the protocol message to a binary string. |
| [`SerializeToString()`](#serializetostring) | Serializes the protocol message to a binary string. |
| [`SetInParent()`](#setinparent) | Mark this as present in the parent. |
| [`UnknownFields()`](#unknownfields) | Returns the UnknownFieldSet. |
| [`WhichOneof()`](#whichoneof) | Returns the name of the field that is set inside a oneof group. |


#### ByteSize()

```python
def ByteSize()
```
Returns the serialized size of this message.

Recursively calls ByteSize() on all contained messages.

Returns:
int: The number of bytes required to serialize this message.


#### Clear()

```python
def Clear()
```
Clears all data that was set in the message.


#### ClearExtension()

```python
def ClearExtension(
    field_descriptor,
)
```
Clears the contents of a given extension.



| Parameter | Type |
|-|-|
| `field_descriptor` |  |

#### ClearField()

```python
def ClearField(
    field_name,
)
```
Clears the contents of a given field.

Inside a oneof group, clears the field set. If the name neither refers to a
defined field or oneof group, :exc:`ValueError` is raised.



| Parameter | Type |
|-|-|
| `field_name` |  |

#### CopyFrom()

```python
def CopyFrom(
    other_msg,
)
```
Copies the content of the specified message into the current message.

The method clears the current message and then merges the specified
message using MergeFrom.



| Parameter | Type |
|-|-|
| `other_msg` |  |

#### DiscardUnknownFields()

```python
def DiscardUnknownFields()
```
Clears all fields in the :class:`UnknownFieldSet`.

This operation is recursive for nested message.


#### FromString()

```python
def FromString(
    s,
)
```
| Parameter | Type |
|-|-|
| `s` |  |

#### HasExtension()

```python
def HasExtension(
    field_descriptor,
)
```
Checks if a certain extension is present for this message.

Extensions are retrieved using the :attr:`Extensions` mapping (if present).



| Parameter | Type |
|-|-|
| `field_descriptor` |  |

#### HasField()

```python
def HasField(
    field_name,
)
```
Checks if a certain field is set for the message.

For a oneof group, checks if any field inside is set. Note that if the
field_name is not defined in the message descriptor, :exc:`ValueError` will
be raised.



| Parameter | Type |
|-|-|
| `field_name` |  |

#### IsInitialized()

```python
def IsInitialized()
```
Checks if the message is initialized.

Returns:
bool: The method returns True if the message is initialized (i.e. all of
its required fields are set).


#### ListFields()

```python
def ListFields()
```
Returns a list of (FieldDescriptor, value) tuples for present fields.

A message field is non-empty if HasField() would return true. A singular
primitive field is non-empty if HasField() would return true in proto2 or it
is non zero in proto3. A repeated field is non-empty if it contains at least
one element. The fields are ordered by field number.

Returns:
list[tuple(FieldDescriptor, value)]: field descriptors and values
for all fields in the message which are not empty. The values vary by
field type.


#### MergeFrom()

```python
def MergeFrom(
    other_msg,
)
```
Merges the contents of the specified message into current message.

This method merges the contents of the specified message into the current
message. Singular fields that are set in the specified message overwrite
the corresponding fields in the current message. Repeated fields are
appended. Singular sub-messages and groups are recursively merged.



| Parameter | Type |
|-|-|
| `other_msg` |  |

#### MergeFromString()

```python
def MergeFromString(
    serialized,
)
```
Merges serialized protocol buffer data into this message.

When we find a field in `serialized` that is already present
in this message:

-   If it's a "repeated" field, we append to the end of our list.
-   Else, if it's a scalar, we overwrite our field.
-   Else, (it's a nonrepeated composite), we recursively merge
into the existing composite.



| Parameter | Type |
|-|-|
| `serialized` |  |

#### ParseFromString()

```python
def ParseFromString(
    serialized,
)
```
Parse serialized protocol buffer data in binary form into this message.

Like :func:`MergeFromString()`, except we clear the object first.

Raises:
message.DecodeError if the input cannot be parsed.


| Parameter | Type |
|-|-|
| `serialized` |  |

#### SerializePartialToString()

```python
def SerializePartialToString(
    kwargs,
)
```
Serializes the protocol message to a binary string.

This method is similar to SerializeToString but doesn't check if the
message is initialized.

Keyword Args:
deterministic (bool): If true, requests deterministic serialization
of the protobuf, with predictable ordering of map keys.

Returns:
bytes: A serialized representation of the partial message.


| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### SerializeToString()

```python
def SerializeToString(
    kwargs,
)
```
Serializes the protocol message to a binary string.

Keyword Args:
deterministic (bool): If true, requests deterministic serialization
of the protobuf, with predictable ordering of map keys.

Returns:
A binary string representation of the message if all of the required
fields in the message are set (i.e. the message is initialized).

Raises:
EncodeError: if the message isn't initialized (see :func:`IsInitialized`).


| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### SetInParent()

```python
def SetInParent()
```
Mark this as present in the parent.

This normally happens automatically when you assign a field of a
sub-message, but sometimes you want to make the sub-message
present while keeping it empty.  If you find yourself using this,
you may want to reconsider your design.


#### UnknownFields()

```python
def UnknownFields()
```
Returns the UnknownFieldSet.

Returns:
UnknownFieldSet: The unknown fields stored in this message.


#### WhichOneof()

```python
def WhichOneof(
    oneof_group,
)
```
Returns the name of the field that is set inside a oneof group.

If no field is set, returns None.



| Parameter | Type |
|-|-|
| `oneof_group` |  |

## flytekit.core.type_engine.MessagePackDecoder

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


```python
class MessagePackDecoder(
    shape_type: typing.Union[typing.Type[~T], typing.Any],
    default_dialect: typing.Optional[typing.Type[mashumaro.dialect.Dialect]],
    pre_decoder_func: typing.Optional[collections.abc.Callable[[bytes], typing.Any]],
)
```
| Parameter | Type |
|-|-|
| `shape_type` | `typing.Union[typing.Type[~T], typing.Any]` |
| `default_dialect` | `typing.Optional[typing.Type[mashumaro.dialect.Dialect]]` |
| `pre_decoder_func` | `typing.Optional[collections.abc.Callable[[bytes], typing.Any]]` |

### Methods

| Method | Description |
|-|-|
| [`decode()`](#decode) |  |


#### decode()

```python
def decode(
    data: bytes,
) -> ~T
```
| Parameter | Type |
|-|-|
| `data` | `bytes` |

## flytekit.core.type_engine.MessagePackEncoder

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


```python
class MessagePackEncoder(
    shape_type: typing.Union[typing.Type[~T], typing.Any],
    default_dialect: typing.Optional[typing.Type[mashumaro.dialect.Dialect]],
    post_encoder_func: typing.Optional[collections.abc.Callable[[typing.Any], bytes]],
)
```
| Parameter | Type |
|-|-|
| `shape_type` | `typing.Union[typing.Type[~T], typing.Any]` |
| `default_dialect` | `typing.Optional[typing.Type[mashumaro.dialect.Dialect]]` |
| `post_encoder_func` | `typing.Optional[collections.abc.Callable[[typing.Any], bytes]]` |

### Methods

| Method | Description |
|-|-|
| [`encode()`](#encode) |  |


#### encode()

```python
def encode(
    obj: ~T,
) -> bytes
```
| Parameter | Type |
|-|-|
| `obj` | `~T` |

## flytekit.core.type_engine.OrderedDict

Dictionary that remembers insertion order


## flytekit.core.type_engine.Primitive

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

## flytekit.core.type_engine.ProtobufTransformer

Base transformer type that should be implemented for every python native type that can be handled by flytekit


```python
def ProtobufTransformer()
```
### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`from_binary_idl()`](#from_binary_idl) | This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access. |
| [`from_generic_idl()`](#from_generic_idl) | TODO: Support all Flyte Types. |
| [`get_literal_type()`](#get_literal_type) | Converts the python type to a Flyte LiteralType. |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type. |
| [`isinstance_generic()`](#isinstance_generic) |  |
| [`tag()`](#tag) |  |
| [`to_html()`](#to_html) | Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div. |
| [`to_literal()`](#to_literal) | Convert the protobuf struct to literal. |
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

#### tag()

```python
def tag(
    expected_python_type: Type[T],
) -> str
```
| Parameter | Type |
|-|-|
| `expected_python_type` | `Type[T]` |

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
    python_val: T,
    python_type: Type[T],
    expected: LiteralType,
) -> Literal
```
Convert the protobuf struct to literal.

This conversion supports two types of python_val:
1. google.protobuf.struct_pb2.Struct: A dictionary-like message
2. google.protobuf.struct_pb2.ListValue: An ordered collection of values

For details, please refer to the following issue:
https://github.com/flyteorg/flyte/issues/5959

Because the remote handling works without errors, we implement conversion with the logic as below:
https://github.com/flyteorg/flyte/blob/a87585ab7cbb6a047c76d994b3f127c4210070fd/flytepropeller/pkg/controller/nodes/attr_path_resolver.go#L72-L106


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `T` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
) -> T
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

## flytekit.core.type_engine.RestrictedTypeError

Common base class for all non-exit exceptions.


## flytekit.core.type_engine.RestrictedTypeTransformer

Types registered with the RestrictedTypeTransformer are not allowed to be converted to and from literals. In other words,
Restricted types are not allowed to be used as inputs or outputs of tasks and workflows.


```python
class RestrictedTypeTransformer(
    name: str,
    t: Type[T],
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `t` | `Type[T]` |

### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
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
    t: Optional[Type[T]],
) -> LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type |
|-|-|
| `t` | `Optional[Type[T]]` |

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

#### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
) -> T
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

## flytekit.core.type_engine.Scalar

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

## flytekit.core.type_engine.SimpleTransformer

A Simple implementation of a type transformer that uses simple lambdas to transform and reduces boilerplate


```python
class SimpleTransformer(
    name: str,
    t: Type[T],
    lt: LiteralType,
    to_literal_transformer: typing.Callable[[T], Literal],
    from_literal_transformer: typing.Callable[[Literal], T],
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `t` | `Type[T]` |
| `lt` | `LiteralType` |
| `to_literal_transformer` | `typing.Callable[[T], Literal]` |
| `from_literal_transformer` | `typing.Callable[[Literal], T]` |

### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
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
    t: Optional[Type[T]],
) -> LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type |
|-|-|
| `t` | `Optional[Type[T]]` |

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

#### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
) -> T
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
| `base_type` |  |  |
| `is_async` |  |  |
| `name` |  |  |
| `python_type` |  | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` |  | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

## flytekit.core.type_engine.SimpleType

## flytekit.core.type_engine.Struct

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
## flytekit.core.type_engine.TextIOTransformer

Handler for TextIO


```python
def TextIOTransformer()
```
### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
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
    t: typing.TextIO,
) -> LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type |
|-|-|
| `t` | `typing.TextIO` |

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
    python_val: typing.TextIO,
    python_type: Type[typing.TextIO],
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
| `python_val` | `typing.TextIO` |
| `python_type` | `Type[typing.TextIO]` |
| `expected` | `LiteralType` |

#### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[typing.TextIO],
) -> typing.TextIO
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[typing.TextIO]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_async` |  |  |
| `name` |  |  |
| `python_type` |  | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` |  | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

## flytekit.core.type_engine.TypeAnnotationModel

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

## flytekit.core.type_engine.TypeEngine

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

## flytekit.core.type_engine.TypeStructure

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

## flytekit.core.type_engine.TypeTransformer

Base transformer type that should be implemented for every python native type that can be handled by flytekit


```python
class TypeTransformer(
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

## flytekit.core.type_engine.TypeTransformerFailedError

Inappropriate argument type.


## flytekit.core.type_engine.Union

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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> Schema
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
| `stored_type` |  |  |
| `value` |  |  |

## flytekit.core.type_engine.UnionTransformer

Transformer that handles a typing.Union[T1, T2, ...]


```python
def UnionTransformer()
```
### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`async_to_literal()`](#async_to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`async_to_python_value()`](#async_to_python_value) | Converts the given Literal to a Python Type. |
| [`from_binary_idl()`](#from_binary_idl) | This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access. |
| [`from_generic_idl()`](#from_generic_idl) | TODO: Support all Flyte Types. |
| [`get_literal_type()`](#get_literal_type) | Converts the python type to a Flyte LiteralType. |
| [`get_sub_type_in_optional()`](#get_sub_type_in_optional) | Return the generic Type T of the Optional type. |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type. |
| [`is_optional_type()`](#is_optional_type) |  |
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
) -> typing.Union[Literal, asyncio.Future]
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
) -> Optional[typing.Any]
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
) -> Optional[LiteralType]
```
Converts the python type to a Flyte LiteralType


| Parameter | Type |
|-|-|
| `t` | `Type[T]` |

#### get_sub_type_in_optional()

```python
def get_sub_type_in_optional(
    t: Type[T],
) -> Type[T]
```
Return the generic Type T of the Optional type


| Parameter | Type |
|-|-|
| `t` | `Type[T]` |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> type
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type |
|-|-|
| `literal_type` | `LiteralType` |

#### is_optional_type()

```python
def is_optional_type(
    t: Type,
) -> bool
```
| Parameter | Type |
|-|-|
| `t` | `Type` |

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

## flytekit.core.type_engine.UnionType

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

## flytekit.core.type_engine.Void

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
) -> Void
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

## flytekit.core.type_engine.timeit

A context manager and a decorator that measures the execution time of the wrapped code block or functions.
It will append a timing information to TimeLineDeck. For instance:

@timeit("Function description")
def function()

with timeit("Wrapped code block description"):
# your code


```python
class timeit(
    name: str,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |

