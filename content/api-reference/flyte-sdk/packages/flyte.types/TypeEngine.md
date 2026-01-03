---
title: TypeEngine
version: 2.0.0b43
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TypeEngine

**Package:** `flyte.types`

Core Extensible TypeEngine of Flytekit. This should be used to extend the capabilities of FlyteKits type system.
Users can implement their own TypeTransformers and register them with the TypeEngine. This will allow special
 handling
of user objects


## Methods

| Method | Description |
|-|-|
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


### dict_to_literal_map()

```python
def dict_to_literal_map(
    d: typing.Dict[str, typing.Any],
    type_hints: Optional[typing.Dict[str, type]],
) -> LiteralMap
```
Given a dictionary mapping string keys to python values and a dictionary containing guessed types for such
string keys,
convert to a LiteralMap.


| Parameter | Type | Description |
|-|-|-|
| `d` | `typing.Dict[str, typing.Any]` | |
| `type_hints` | `Optional[typing.Dict[str, type]]` | |

### get_available_transformers()

```python
def get_available_transformers()
```
Returns all python types for which transformers are available


### get_transformer()

```python
def get_transformer(
    python_type: Type,
) -> TypeTransformer
```
Implements a recursive search for the transformer.


| Parameter | Type | Description |
|-|-|-|
| `python_type` | `Type` | |

### guess_python_type()

```python
def guess_python_type(
    flyte_type: LiteralType,
) -> Type[T]
```
Transforms a flyte-specific ``LiteralType`` to a regular python value.


| Parameter | Type | Description |
|-|-|-|
| `flyte_type` | `LiteralType` | |

### guess_python_types()

```python
def guess_python_types(
    flyte_variable_dict: typing.Dict[str, interface_pb2.Variable],
) -> typing.Dict[str, Type[Any]]
```
Transforms a dictionary of flyte-specific ``Variable`` objects to a dictionary of regular python values.


| Parameter | Type | Description |
|-|-|-|
| `flyte_variable_dict` | `typing.Dict[str, interface_pb2.Variable]` | |

### lazy_import_transformers()

```python
def lazy_import_transformers()
```
Only load the transformers if needed.


### literal_map_to_kwargs()

```python
def literal_map_to_kwargs(
    lm: LiteralMap,
    python_types: typing.Optional[typing.Dict[str, type]],
    literal_types: typing.Optional[typing.Dict[str, interface_pb2.Variable]],
) -> typing.Dict[str, typing.Any]
```
Given a ``LiteralMap`` (usually an input into a task - intermediate), convert to kwargs for the task


| Parameter | Type | Description |
|-|-|-|
| `lm` | `LiteralMap` | |
| `python_types` | `typing.Optional[typing.Dict[str, type]]` | |
| `literal_types` | `typing.Optional[typing.Dict[str, interface_pb2.Variable]]` | |

### named_tuple_to_variable_map()

```python
def named_tuple_to_variable_map(
    t: typing.NamedTuple,
) -> interface_pb2.VariableMap
```
Converts a python-native ``NamedTuple`` to a flyte-specific VariableMap of named literals.


| Parameter | Type | Description |
|-|-|-|
| `t` | `typing.NamedTuple` | |

### register()

```python
def register(
    transformer: TypeTransformer,
    additional_types: Optional[typing.List[Type]],
)
```
This should be used for all types that respond with the right type annotation when you use type(...) function


| Parameter | Type | Description |
|-|-|-|
| `transformer` | `TypeTransformer` | |
| `additional_types` | `Optional[typing.List[Type]]` | |

### register_additional_type()

```python
def register_additional_type(
    transformer: TypeTransformer[T],
    additional_type: Type[T],
    override,
)
```
| Parameter | Type | Description |
|-|-|-|
| `transformer` | `TypeTransformer[T]` | |
| `additional_type` | `Type[T]` | |
| `override` |  | |

### register_restricted_type()

```python
def register_restricted_type(
    name: str,
    type: Type[T],
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `type` | `Type[T]` | |

### to_html()

```python
def to_html(
    python_val: typing.Any,
    expected_python_type: Type[typing.Any],
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `python_val` | `typing.Any` | |
| `expected_python_type` | `Type[typing.Any]` | |

### to_literal()

```python
def to_literal(
    python_val: typing.Any,
    python_type: Type[T],
    expected: types_pb2.LiteralType,
) -> literals_pb2.Literal
```
| Parameter | Type | Description |
|-|-|-|
| `python_val` | `typing.Any` | |
| `python_type` | `Type[T]` | |
| `expected` | `types_pb2.LiteralType` | |

### to_literal_checks()

```python
def to_literal_checks(
    python_val: typing.Any,
    python_type: Type[T],
    expected: LiteralType,
)
```
| Parameter | Type | Description |
|-|-|-|
| `python_val` | `typing.Any` | |
| `python_type` | `Type[T]` | |
| `expected` | `LiteralType` | |

### to_literal_type()

```python
def to_literal_type(
    python_type: Type[T],
) -> LiteralType
```
Converts a python type into a flyte specific ``LiteralType``


| Parameter | Type | Description |
|-|-|-|
| `python_type` | `Type[T]` | |

### to_python_value()

```python
def to_python_value(
    lv: Literal,
    expected_python_type: Type,
) -> typing.Any
```
Converts a Literal value with an expected python type into a python value.


| Parameter | Type | Description |
|-|-|-|
| `lv` | `Literal` | |
| `expected_python_type` | `Type` | |

### unwrap_offloaded_literal()

```python
def unwrap_offloaded_literal(
    lv: literals_pb2.Literal,
) -> literals_pb2.Literal
```
| Parameter | Type | Description |
|-|-|-|
| `lv` | `literals_pb2.Literal` | |

