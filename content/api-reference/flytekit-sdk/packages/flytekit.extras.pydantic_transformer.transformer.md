---
title: flytekit.extras.pydantic_transformer.transformer
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.extras.pydantic_transformer.transformer

## Directory

### Classes

| Class | Description |
|-|-|
| [`PydanticTransformer`](.././flytekit.extras.pydantic_transformer.transformer#flytekitextraspydantic_transformertransformerpydantictransformer) |  |

### Variables

| Property | Type | Description |
|-|-|-|
| `CACHE_KEY_METADATA` | `str` |  |
| `FLYTE_USE_OLD_DC_FORMAT` | `str` |  |
| `MESSAGEPACK` | `str` |  |
| `SERIALIZATION_FORMAT` | `str` |  |

## flytekit.extras.pydantic_transformer.transformer.PydanticTransformer

```python
def PydanticTransformer()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_async` | `None` |  |
| `name` | `None` |  |
| `python_type` | `None` | This returns the python type |
| `type_assertions_enabled` | `None` | Indicates if the transformer wants type assertions to be enabled at the core type engine layer |

### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`from_binary_idl()`](#from_binary_idl) | This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access. |
| [`from_generic_idl()`](#from_generic_idl) | TODO: Support all Flyte Types. |
| [`get_literal_type()`](#get_literal_type) | Converts the python type to a Flyte LiteralType. |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type. |
| [`isinstance_generic()`](#isinstance_generic) |  |
| [`to_generic_literal()`](#to_generic_literal) | Note: This is deprecated and will be removed in the future. |
| [`to_html()`](#to_html) | Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div. |
| [`to_literal()`](#to_literal) | For pydantic basemodel, we have to go through json first. |
| [`to_python_value()`](#to_python_value) | There will have 2 kinds of literal values:. |


#### assert_type()

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

#### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: flytekit.models.literals.Binary,
    expected_python_type: typing.Type[pydantic.main.BaseModel],
) -> pydantic.main.BaseModel
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
| `binary_idl_object` | `flytekit.models.literals.Binary` | |
| `expected_python_type` | `typing.Type[pydantic.main.BaseModel]` | |

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


| Parameter | Type | Description |
|-|-|-|
| `generic` | `Struct` | |
| `expected_python_type` | `Type[T]` | |

#### get_literal_type()

```python
def get_literal_type(
    t: typing.Type[pydantic.main.BaseModel],
) -> flytekit.models.types.LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type | Description |
|-|-|-|
| `t` | `typing.Type[pydantic.main.BaseModel]` | |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> Type[T]
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type | Description |
|-|-|-|
| `literal_type` | `LiteralType` | |

#### isinstance_generic()

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

#### to_generic_literal()

```python
def to_generic_literal(
    ctx: flytekit.core.context_manager.FlyteContext,
    python_val: pydantic.main.BaseModel,
    python_type: typing.Type[pydantic.main.BaseModel],
    expected: flytekit.models.types.LiteralType,
) -> flytekit.models.literals.Literal
```
Note: This is deprecated and will be removed in the future.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `python_val` | `pydantic.main.BaseModel` | |
| `python_type` | `typing.Type[pydantic.main.BaseModel]` | |
| `expected` | `flytekit.models.types.LiteralType` | |

#### to_html()

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

#### to_literal()

```python
def to_literal(
    ctx: flytekit.core.context_manager.FlyteContext,
    python_val: pydantic.main.BaseModel,
    python_type: typing.Type[pydantic.main.BaseModel],
    expected: flytekit.models.types.LiteralType,
) -> flytekit.models.literals.Literal
```
For pydantic basemodel, we have to go through json first.
This is for handling enum in basemodel.
More details: https://github.com/flyteorg/flytekit/pull/2792


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `python_val` | `pydantic.main.BaseModel` | |
| `python_type` | `typing.Type[pydantic.main.BaseModel]` | |
| `expected` | `flytekit.models.types.LiteralType` | |

#### to_python_value()

```python
def to_python_value(
    ctx: flytekit.core.context_manager.FlyteContext,
    lv: flytekit.models.literals.Literal,
    expected_python_type: typing.Type[pydantic.main.BaseModel],
) -> pydantic.main.BaseModel
```
There will have 2 kinds of literal values:
1. protobuf Struct (From Flyte Console)
2. binary scalar (Others)
Hence we have to handle 2 kinds of cases.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `lv` | `flytekit.models.literals.Literal` | |
| `expected_python_type` | `typing.Type[pydantic.main.BaseModel]` | |

