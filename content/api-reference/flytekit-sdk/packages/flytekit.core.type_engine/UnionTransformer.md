---
title: UnionTransformer
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# UnionTransformer

**Package:** `flytekit.core.type_engine`

Transformer that handles a typing.Union[T1, T2, ...]


```python
def UnionTransformer()
```
## Methods

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
    python_val: T,
    python_type: Type[T],
    expected: LiteralType,
) -> typing.Union[Literal, asyncio.Future]
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | A FlyteContext, useful in accessing the filesystem and other attributes |
| `python_val` | `T` | The actual value to be transformed |
| `python_type` | `Type[T]` | The assumed type of the value (this matches the declared type on the function) |
| `expected` | `LiteralType` | Expected Literal Type |

### async_to_python_value()

```python
def async_to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
) -> Optional[typing.Any]
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | FlyteContext |
| `lv` | `Literal` | The received literal Value |
| `expected_python_type` | `Type[T]` | Expected native python type that should be returned |

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
    python val -> msgpack bytes -> binary literal scalar -> msgpack bytes -> python val
                  (to_literal)                             (from_binary_idl)

For attribute access:
Life Cycle:
    python val -> msgpack bytes -> binary literal scalar -> resolved golang value -> binary literal scalar -> msgpack bytes -> python val
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
    t: Type[T],
) -> Optional[LiteralType]
```
Converts the python type to a Flyte LiteralType


| Parameter | Type | Description |
|-|-|-|
| `t` | `Type[T]` | |

### get_sub_type_in_optional()

```python
def get_sub_type_in_optional(
    t: Type[T],
) -> Type[T]
```
Return the generic Type T of the Optional type


| Parameter | Type | Description |
|-|-|-|
| `t` | `Type[T]` | |

### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> type
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type | Description |
|-|-|-|
| `literal_type` | `LiteralType` | |

### is_optional_type()

```python
def is_optional_type(
    t: Type,
) -> bool
```
| Parameter | Type | Description |
|-|-|-|
| `t` | `Type` | |

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

## Properties

| Property | Type | Description |
|-|-|-|
| `is_async` |  |  |
| `name` |  |  |
| `python_type` |  | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` |  | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

