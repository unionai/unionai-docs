---
title: DictTransformer
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# DictTransformer

**Package:** `flytekit.core.type_engine`

Transformer that transforms an univariate dictionary Dict[str, T] to a Literal Map or
transforms an untyped dictionary to a Binary Scalar Literal with a Struct Literal Type.



```python
def DictTransformer()
```
## Properties

| Property | Type | Description |
|-|-|-|
| `is_async` | `None` |  |
| `name` | `None` |  |
| `python_type` | `None` | This returns the python type |
| `type_assertions_enabled` | `None` | Indicates if the transformer wants type assertions to be enabled at the core type engine layer |

## Methods

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


### assert_type()

```python
def assert_type(
    t: Type[T],
    v: T,
)
```
| Parameter | Type | Description |
|-|-|-|
| `t` | `Type[T]` | |
| `v` | `T` | |

### async_to_literal()

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


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | A FlyteContext, useful in accessing the filesystem and other attributes |
| `python_val` | `typing.Any` | The actual value to be transformed |
| `python_type` | `Type[dict]` | The assumed type of the value (this matches the declared type on the function) |
| `expected` | `LiteralType` | Expected Literal Type |

### async_to_python_value()

```python
def async_to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[dict],
) -> dict
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | FlyteContext |
| `lv` | `Literal` | The received literal Value |
| `expected_python_type` | `Type[dict]` | Expected native python type that should be returned |

### dict_to_binary_literal()

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


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `v` | `dict` | |
| `python_type` | `Type[dict]` | |
| `allow_pickle` | `bool` | |

### dict_to_generic_literal()

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


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `v` | `dict` | |
| `python_type` | `Type[dict]` | |
| `allow_pickle` | `bool` | |

### extract_types()

```python
def extract_types(
    t: Optional[Type[dict]],
) -> typing.Tuple
```
| Parameter | Type | Description |
|-|-|-|
| `t` | `Optional[Type[dict]]` | |

### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: Binary,
    expected_python_type: Type[T],
) -> Optional[T]
```
This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access.｀

For untyped dict, dataclass, and pydantic basemodel:
Life Cycle (Untyped Dict as example):
    python val -&gt; msgpack bytes -&gt; binary literal scalar -&gt; msgpack bytes -&gt; python val
                  (to_literal)                             (from_binary_idl)

For attribute access:
Life Cycle:
    python val -&gt; msgpack bytes -&gt; binary literal scalar -&gt; resolved golang value -&gt; binary literal scalar -&gt; msgpack bytes -&gt; python val
                  (to_literal)                            (propeller attribute access)                       (from_binary_idl)


| Parameter | Type | Description |
|-|-|-|
| `binary_idl_object` | `Binary` | |
| `expected_python_type` | `Type[T]` | |

### from_generic_idl()

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


| Parameter | Type | Description |
|-|-|-|
| `generic` | `Struct` | |
| `expected_python_type` | `Type[T]` | |

### get_literal_type()

```python
def get_literal_type(
    t: Type[dict],
) -> LiteralType
```
Transforms a native python dictionary to a flyte-specific ``LiteralType``


| Parameter | Type | Description |
|-|-|-|
| `t` | `Type[dict]` | |

### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> Union[Type[dict], typing.Dict[Type, Type]]
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type | Description |
|-|-|-|
| `literal_type` | `LiteralType` | |

### is_pickle()

```python
def is_pickle(
    python_type: Type[dict],
) -> bool
```
| Parameter | Type | Description |
|-|-|-|
| `python_type` | `Type[dict]` | |

### isinstance_generic()

```python
def isinstance_generic(
    obj,
    generic_alias,
)
```
| Parameter | Type | Description |
|-|-|-|
| `obj` |  | |
| `generic_alias` |  | |

### to_html()

```python
def to_html(
    ctx: FlyteContext,
    python_val: T,
    expected_python_type: Type[T],
) -> str
```
Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `python_val` | `T` | |
| `expected_python_type` | `Type[T]` | |

### to_literal()

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


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | A FlyteContext, useful in accessing the filesystem and other attributes |
| `python_val` | `typing.Any` | The actual value to be transformed |
| `python_type` | `Type[T]` | The assumed type of the value (this matches the declared type on the function) |
| `expected` | `LiteralType` | Expected Literal Type |

### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
) -> Optional[T]
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | FlyteContext |
| `lv` | `Literal` | The received literal Value |
| `expected_python_type` | `Type[T]` | Expected native python type that should be returned |

