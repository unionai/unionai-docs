---
title: TypeEngine
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TypeEngine

**Package:** `flytekit.core.type_engine`

Core Extensible TypeEngine of Flytekit. This should be used to extend the capabilities of FlyteKits type system.
Users can implement their own TypeTransformers and register them with the TypeEngine. This will allow special handling
of user objects


## Methods

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


### async_to_literal()

```python
def async_to_literal(
    ctx: FlyteContext,
    python_val: typing.Any,
    python_type: Type[T],
    expected: LiteralType,
) -> Literal
```
Converts a python value of a given type and expected ``LiteralType`` into a resolved ``Literal`` value.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `python_val` | `typing.Any` | |
| `python_type` | `Type[T]` | |
| `expected` | `LiteralType` | |

### async_to_python_value()

```python
def async_to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type,
) -> typing.Any
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `lv` | `Literal` | |
| `expected_python_type` | `Type` | |

### calculate_hash()

```python
def calculate_hash(
    python_val: typing.Any,
    python_type: Type[T],
) -> Optional[str]
```
| Parameter | Type | Description |
|-|-|-|
| `python_val` | `typing.Any` | |
| `python_type` | `Type[T]` | |

### dict_to_literal_map()

```python
def dict_to_literal_map(
    ctx: FlyteContext,
    d: typing.Dict[str, typing.Any],
    type_hints: Optional[typing.Dict[str, type]],
) -> LiteralMap
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `d` | `typing.Dict[str, typing.Any]` | |
| `type_hints` | `Optional[typing.Dict[str, type]]` | |

### dict_to_literal_map_pb()

```python
def dict_to_literal_map_pb(
    ctx: FlyteContext,
    d: typing.Dict[str, typing.Any],
    type_hints: Optional[typing.Dict[str, type]],
) -> Optional[literals_pb2.LiteralMap]
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
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
) -> TypeTransformer[T]
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
    flyte_variable_dict: typing.Dict[str, _interface_models.Variable],
) -> typing.Dict[str, type]
```
Transforms a dictionary of flyte-specific ``Variable`` objects to a dictionary of regular python values.


| Parameter | Type | Description |
|-|-|-|
| `flyte_variable_dict` | `typing.Dict[str, _interface_models.Variable]` | |

### lazy_import_transformers()

```python
def lazy_import_transformers()
```
Only load the transformers if needed.


### literal_map_to_kwargs()

```python
def literal_map_to_kwargs(
    ctx: FlyteContext,
    lm: LiteralMap,
    python_types: typing.Optional[typing.Dict[str, type]],
    literal_types: typing.Optional[typing.Dict[str, _interface_models.Variable]],
) -> typing.Dict[str, typing.Any]
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `lm` | `LiteralMap` | |
| `python_types` | `typing.Optional[typing.Dict[str, type]]` | |
| `literal_types` | `typing.Optional[typing.Dict[str, _interface_models.Variable]]` | |

### named_tuple_to_variable_map()

```python
def named_tuple_to_variable_map(
    t: typing.NamedTuple,
) -> _interface_models.VariableMap
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
    ctx: FlyteContext,
    python_val: typing.Any,
    expected_python_type: Type[typing.Any],
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `python_val` | `typing.Any` | |
| `expected_python_type` | `Type[typing.Any]` | |

### to_literal()

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


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `python_val` | `typing.Any` | |
| `python_type` | `Type[T]` | |
| `expected` | `LiteralType` | |

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
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type,
) -> typing.Any
```
Converts a Literal value with an expected python type into a python value.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `lv` | `Literal` | |
| `expected_python_type` | `Type` | |

### unwrap_offloaded_literal()

```python
def unwrap_offloaded_literal(
    ctx: FlyteContext,
    lv: Literal,
) -> Literal
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `lv` | `Literal` | |

