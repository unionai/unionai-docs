---
title: DictTransformer
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# DictTransformer

**Package:** `flytekit.extend`

Transformer that transforms an univariate dictionary Dict[str, T] to a Literal Map or
transforms an untyped dictionary to a Binary Scalar Literal with a Struct Literal Type.


```python
def DictTransformer()
```
Initialize self.  See help(type(self)) for accurate signature.


No parameters
## Methods

### assert_type()

```python
def assert_type(
    t: Type[T],
    v: T,
):
```
| Parameter | Type |
|-|-|
| `t` | `Type[T]` |
| `v` | `T` |
### async_to_literal()

```python
def async_to_literal(
    ctx: FlyteContext,
    python_val: typing.Any,
    python_type: Type[dict],
    expected: LiteralType,
):
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
### async_to_python_value()

```python
def async_to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[dict],
):
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[dict]` |
### dict_to_binary_literal()

```python
def dict_to_binary_literal(
    ctx: FlyteContext,
    v: dict,
    python_type: Type[dict],
    allow_pickle: bool,
):
```
Converts a Python dictionary to a Flyte-specific ``Literal`` using MessagePack encoding.
Falls back to Pickle if encoding fails and `allow_pickle` is True.


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `v` | `dict` |
| `python_type` | `Type[dict]` |
| `allow_pickle` | `bool` |
### dict_to_generic_literal()

```python
def dict_to_generic_literal(
    ctx: FlyteContext,
    v: dict,
    python_type: Type[dict],
    allow_pickle: bool,
):
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
### extract_types()

```python
def extract_types(
    t: Optional[Type[dict]],
):
```
| Parameter | Type |
|-|-|
| `t` | `Optional[Type[dict]]` |
### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: Binary,
    expected_python_type: Type[T],
):
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
### from_generic_idl()

```python
def from_generic_idl(
    generic: Struct,
    expected_python_type: Type[T],
):
```
TODO: Support all Flyte Types.
This is for dataclass attribute access from input created from the Flyte Console.

Note:
- This can be removed in the future when the Flyte Console support generate Binary IDL Scalar as input.


| Parameter | Type |
|-|-|
| `generic` | `Struct` |
| `expected_python_type` | `Type[T]` |
### get_literal_type()

```python
def get_literal_type(
    t: Type[dict],
):
```
Transforms a native python dictionary to a flyte-specific ``LiteralType``


| Parameter | Type |
|-|-|
| `t` | `Type[dict]` |
### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
):
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type |
|-|-|
| `literal_type` | `LiteralType` |
### is_pickle()

```python
def is_pickle(
    python_type: Type[dict],
):
```
| Parameter | Type |
|-|-|
| `python_type` | `Type[dict]` |
### isinstance_generic()

```python
def isinstance_generic(
    obj,
    generic_alias,
):
```
| Parameter | Type |
|-|-|
| `obj` |  |
| `generic_alias` |  |
### to_html()

```python
def to_html(
    ctx: FlyteContext,
    python_val: T,
    expected_python_type: Type[T],
):
```
Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `T` |
| `expected_python_type` | `Type[T]` |
### to_literal()

```python
def to_literal(
    ctx: FlyteContext,
    python_val: typing.Any,
    python_type: Type[T],
    expected: LiteralType,
):
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
### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
):
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[T]` |
