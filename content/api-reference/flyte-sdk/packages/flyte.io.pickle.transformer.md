---
title: flyte.io.pickle.transformer
version: 0.2.0b7
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flyte.io.pickle.transformer

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlytePickle`](.././flyte.io.pickle.transformer#flyteiopickletransformerflytepickle) | This type is only used by flytekit internally. |
| [`FlytePickleTransformer`](.././flyte.io.pickle.transformer#flyteiopickletransformerflytepickletransformer) | Base transformer type that should be implemented for every python native type that can be handled by flytekit. |

### Variables

| Property | Type | Description |
|-|-|-|
| `T` | `TypeVar` |  |

## flyte.io.pickle.transformer.FlytePickle

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

## flyte.io.pickle.transformer.FlytePickleTransformer

Base transformer type that should be implemented for every python native type that can be handled by flytekit


```python
def FlytePickleTransformer()
```
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
    t: typing.Type[~T],
    v: ~T,
)
```
| Parameter | Type |
|-|-|
| `t` | `typing.Type[~T]` |
| `v` | `~T` |

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
    t: typing.Type[~T],
) -> flyteidl.core.types_pb2.LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type |
|-|-|
| `t` | `typing.Type[~T]` |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: flyteidl.core.types_pb2.LiteralType,
) -> typing.Type[flyte.io.pickle.transformer.FlytePickle.__class_getitem__.<locals>._SpecificFormatClass]
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type |
|-|-|
| `literal_type` | `flyteidl.core.types_pb2.LiteralType` |

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
    python_val: ~T,
    python_type: typing.Type[~T],
    expected: flyteidl.core.types_pb2.LiteralType,
) -> flyteidl.core.literals_pb2.Literal
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type |
|-|-|
| `python_val` | `~T` |
| `python_type` | `typing.Type[~T]` |
| `expected` | `flyteidl.core.types_pb2.LiteralType` |

#### to_python_value()

```python
def to_python_value(
    lv: flyteidl.core.literals_pb2.Literal,
    expected_python_type: typing.Type[~T],
) -> ~T
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `lv` | `flyteidl.core.literals_pb2.Literal` |
| `expected_python_type` | `typing.Type[~T]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `name` |  |  |
| `python_type` |  | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` |  | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

