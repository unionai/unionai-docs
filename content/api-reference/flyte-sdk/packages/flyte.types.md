---
title: flyte.types
version: 0.2.0b10.dev2+g9bf3bb9
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flyte.types


# Flyte Type System

The Flyte type system provides a way to define, transform, and manipulate types in Flyte workflows.
Since the data flowing through Flyte has to often cross process, container and langauge boundaries, the type system
is designed to be serializable to a universal format that can be understood across different environments. This
universal format is based on Protocol Buffers. The types are called LiteralTypes and the runtime
representation of data is called Literals.

The type system includes:
- **TypeEngine**: The core engine that manages type transformations and serialization. This is the main entry point for
  for all the internal type transformations and serialization logic.
- **TypeTransformer**: A class that defines how to transform one type to another. This is extensible
    allowing users to define custom types and transformations.
- **Renderable**: An interface for types that can be rendered as HTML, that can be outputted to a flyte.report.

It is always possible to bypass the type system and use the `FlytePickle` type to serialize any python object
 into a pickle format. The pickle format is not human-readable, but can be passed between flyte tasks that are
 written in python. The Pickled objects cannot be represented in the UI, and may be in-efficient for large datasets.

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlytePickle`](.././flyte.types#flytetypesflytepickle) | This type is only used by flytekit internally. |
| [`TypeEngine`](.././flyte.types#flytetypestypeengine) | Core Extensible TypeEngine of Flytekit. |
| [`TypeTransformer`](.././flyte.types#flytetypestypetransformer) | Base transformer type that should be implemented for every python native type that can be handled by flytekit. |

### Protocols

| Protocol | Description |
|-|-|
| [`Renderable`](.././flyte.types#flytetypesrenderable) | Base class for protocol classes. |

### Errors

| Exception | Description |
|-|-|
| [`TypeTransformerFailedError`](.././flyte.types#flytetypestypetransformerfailederror) | Inappropriate argument type. |

### Methods

| Method | Description |
|-|-|
| [`guess_interface()`](#guess_interface) | Returns the interface of the task with guessed types, as types may not be present in current env. |
| [`literal_string_repr()`](#literal_string_repr) | This method is used to convert a literal map to a string representation. |


## Methods

#### guess_interface()

```python
def guess_interface(
    interface: flyteidl.core.interface_pb2.TypedInterface,
) -> flyte.models.NativeInterface
```
Returns the interface of the task with guessed types, as types may not be present in current env.


| Parameter | Type |
|-|-|
| `interface` | `flyteidl.core.interface_pb2.TypedInterface` |

#### literal_string_repr()

```python
def literal_string_repr(
    lm: typing.Union[flyteidl.core.literals_pb2.Literal, workflow.run_definition_pb2.NamedLiteral, workflow.run_definition_pb2.Inputs, workflow.run_definition_pb2.Outputs, flyteidl.core.literals_pb2.LiteralMap, typing.Dict[str, flyteidl.core.literals_pb2.Literal]],
) -> typing.Dict[str, typing.Any]
```
This method is used to convert a literal map to a string representation.


| Parameter | Type |
|-|-|
| `lm` | `typing.Union[flyteidl.core.literals_pb2.Literal, workflow.run_definition_pb2.NamedLiteral, workflow.run_definition_pb2.Inputs, workflow.run_definition_pb2.Outputs, flyteidl.core.literals_pb2.LiteralMap, typing.Dict[str, flyteidl.core.literals_pb2.Literal]]` |

## flyte.types.FlytePickle

This type is only used by flytekit internally. User should not use this type.
Any type that flyte can't recognize will become FlytePickle


### Methods

| Method | Description |
|-|-|
| [`from_pickle()`](#from_pickle) |  |
| [`python_type()`](#python_type) |  |
| [`to_pickle()`](#to_pickle) |  |


#### from_pickle()

```python
def from_pickle(
    uri: str,
) -> typing.Any
```
| Parameter | Type |
|-|-|
| `uri` | `str` |

#### python_type()

```python
def python_type()
```
#### to_pickle()

```python
def to_pickle(
    python_val: typing.Any,
) -> str
```
| Parameter | Type |
|-|-|
| `python_val` | `typing.Any` |

## flyte.types.Renderable

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
protocol Renderable()
```
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

## flyte.types.TypeEngine

Core Extensible TypeEngine of Flytekit. This should be used to extend the capabilities of FlyteKits type system.
Users can implement their own TypeTransformers and register them with the TypeEngine. This will allow special
 handling
of user objects


### Methods

| Method | Description |
|-|-|
| [`calculate_hash()`](#calculate_hash) |  |
| [`dict_to_literal_map()`](#dict_to_literal_map) | Given a dictionary mapping string keys to python values and a dictionary containing guessed types for such. |
| [`get_available_transformers()`](#get_available_transformers) | Returns all python types for which transformers are available. |
| [`get_transformer()`](#get_transformer) | Implements a recursive search for the transformer. |
| [`guess_python_type()`](#guess_python_type) | Transforms a flyte-specific ``LiteralType`` to a regular python value. |
| [`guess_python_types()`](#guess_python_types) | Transforms a dictionary of flyte-specific ``Variable`` objects to a dictionary of regular python values. |
| [`lazy_import_transformers()`](#lazy_import_transformers) | Only load the transformers if needed. |
| [`literal_map_to_kwargs()`](#literal_map_to_kwargs) | Given a ``LiteralMap`` (usually an input into a task - intermediate), convert to kwargs for the task. |
| [`named_tuple_to_variable_map()`](#named_tuple_to_variable_map) | Converts a python-native ``NamedTuple`` to a flyte-specific VariableMap of named literals. |
| [`register()`](#register) | This should be used for all types that respond with the right type annotation when you use type(. |
| [`register_additional_type()`](#register_additional_type) |  |
| [`register_restricted_type()`](#register_restricted_type) |  |
| [`to_html()`](#to_html) |  |
| [`to_literal()`](#to_literal) |  |
| [`to_literal_checks()`](#to_literal_checks) |  |
| [`to_literal_type()`](#to_literal_type) | Converts a python type into a flyte specific ``LiteralType``. |
| [`to_python_value()`](#to_python_value) | Converts a Literal value with an expected python type into a python value. |
| [`unwrap_offloaded_literal()`](#unwrap_offloaded_literal) |  |


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
    d: typing.Dict[str, typing.Any],
    type_hints: Optional[typing.Dict[str, type]],
) -> LiteralMap
```
Given a dictionary mapping string keys to python values and a dictionary containing guessed types for such
string keys,
convert to a LiteralMap.


| Parameter | Type |
|-|-|
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
) -> TypeTransformer
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
    flyte_variable_dict: typing.Dict[str, interface_pb2.Variable],
) -> typing.Dict[str, Type[Any]]
```
Transforms a dictionary of flyte-specific ``Variable`` objects to a dictionary of regular python values.


| Parameter | Type |
|-|-|
| `flyte_variable_dict` | `typing.Dict[str, interface_pb2.Variable]` |

#### lazy_import_transformers()

```python
def lazy_import_transformers()
```
Only load the transformers if needed.


#### literal_map_to_kwargs()

```python
def literal_map_to_kwargs(
    lm: LiteralMap,
    python_types: typing.Optional[typing.Dict[str, type]],
    literal_types: typing.Optional[typing.Dict[str, interface_pb2.Variable]],
) -> typing.Dict[str, typing.Any]
```
Given a ``LiteralMap`` (usually an input into a task - intermediate), convert to kwargs for the task


| Parameter | Type |
|-|-|
| `lm` | `LiteralMap` |
| `python_types` | `typing.Optional[typing.Dict[str, type]]` |
| `literal_types` | `typing.Optional[typing.Dict[str, interface_pb2.Variable]]` |

#### named_tuple_to_variable_map()

```python
def named_tuple_to_variable_map(
    t: typing.NamedTuple,
) -> interface_pb2.VariableMap
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
    python_val: typing.Any,
    expected_python_type: Type[typing.Any],
) -> str
```
| Parameter | Type |
|-|-|
| `python_val` | `typing.Any` |
| `expected_python_type` | `Type[typing.Any]` |

#### to_literal()

```python
def to_literal(
    python_val: typing.Any,
    python_type: Type[T],
    expected: types_pb2.LiteralType,
) -> literals_pb2.Literal
```
| Parameter | Type |
|-|-|
| `python_val` | `typing.Any` |
| `python_type` | `Type[T]` |
| `expected` | `types_pb2.LiteralType` |

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
    lv: Literal,
    expected_python_type: Type,
) -> typing.Any
```
Converts a Literal value with an expected python type into a python value.


| Parameter | Type |
|-|-|
| `lv` | `Literal` |
| `expected_python_type` | `Type` |

#### unwrap_offloaded_literal()

```python
def unwrap_offloaded_literal(
    lv: literals_pb2.Literal,
) -> literals_pb2.Literal
```
| Parameter | Type |
|-|-|
| `lv` | `literals_pb2.Literal` |

## flyte.types.TypeTransformer

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
| [`from_binary_idl()`](#from_binary_idl) | This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and. |
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
This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and
 attribute access.

For untyped dict, dataclass, and pydantic basemodel:
Life Cycle (Untyped Dict as example):
    python val -> msgpack bytes -> binary literal scalar -> msgpack bytes -> python val
                  (to_literal)                             (from_binary_idl)

For attribute access:
Life Cycle:
    python val -> msgpack bytes -> binary literal scalar -> resolved golang value -> binary literal scalar
     -> msgpack bytes -> python val
                  (to_literal)      (propeller attribute access)     (from_binary_idl)


| Parameter | Type |
|-|-|
| `binary_idl_object` | `Binary` |
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
    python_val: T,
    expected_python_type: Type[T],
) -> str
```
Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div


| Parameter | Type |
|-|-|
| `python_val` | `T` |
| `expected_python_type` | `Type[T]` |

#### to_literal()

```python
def to_literal(
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
| `python_val` | `T` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### to_python_value()

```python
def to_python_value(
    lv: Literal,
    expected_python_type: Type[T],
) -> Optional[T]
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `lv` | `Literal` |
| `expected_python_type` | `Type[T]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `name` | `None` |  |
| `python_type` | `None` | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` | `None` | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

## flyte.types.TypeTransformerFailedError

Inappropriate argument type.


