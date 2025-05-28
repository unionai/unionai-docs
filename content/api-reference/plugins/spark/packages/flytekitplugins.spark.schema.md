---
title: flytekitplugins.spark.schema
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.spark.schema

## Directory

### Classes

| Class | Description |
|-|-|
| [`SparkDataFrameSchemaReader`](.././flytekitplugins.spark.schema#flytekitpluginssparkschemasparkdataframeschemareader) | Implements how SparkDataFrame should be read using the ``open`` method of FlyteSchema. |
| [`SparkDataFrameSchemaWriter`](.././flytekitplugins.spark.schema#flytekitpluginssparkschemasparkdataframeschemawriter) | Implements how SparkDataFrame should be written to using ``open`` method of FlyteSchema. |
| [`SparkDataFrameTransformer`](.././flytekitplugins.spark.schema#flytekitpluginssparkschemasparkdataframetransformer) | Transforms Spark DataFrame's to and from a Schema (typed/untyped). |

## flytekitplugins.spark.schema.SparkDataFrameSchemaReader

Implements how SparkDataFrame should be read using the ``open`` method of FlyteSchema


```python
class SparkDataFrameSchemaReader(
    from_path: str,
    cols: typing.Optional[typing.Dict[str, type]],
    fmt: <enum 'SchemaFormat'>,
)
```
| Parameter | Type |
|-|-|
| `from_path` | `str` |
| `cols` | `typing.Optional[typing.Dict[str, type]]` |
| `fmt` | `<enum 'SchemaFormat'>` |

### Methods

| Method | Description |
|-|-|
| [`all()`](#all) |  |
| [`iter()`](#iter) |  |


#### all()

```python
def all(
    kwargs,
) -> pyspark.sql.dataframe.DataFrame
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### iter()

```python
def iter(
    kwargs,
) -> typing.Generator[~T, NoneType, NoneType]
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `column_names` |  |  |
| `from_path` |  |  |

## flytekitplugins.spark.schema.SparkDataFrameSchemaWriter

Implements how SparkDataFrame should be written to using ``open`` method of FlyteSchema


```python
class SparkDataFrameSchemaWriter(
    to_path: str,
    cols: typing.Optional[typing.Dict[str, type]],
    fmt: <enum 'SchemaFormat'>,
)
```
| Parameter | Type |
|-|-|
| `to_path` | `str` |
| `cols` | `typing.Optional[typing.Dict[str, type]]` |
| `fmt` | `<enum 'SchemaFormat'>` |

### Methods

| Method | Description |
|-|-|
| [`write()`](#write) |  |


#### write()

```python
def write(
    dfs: pyspark.sql.dataframe.DataFrame,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `dfs` | `pyspark.sql.dataframe.DataFrame` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `column_names` |  |  |
| `to_path` |  |  |

## flytekitplugins.spark.schema.SparkDataFrameTransformer

Transforms Spark DataFrame's to and from a Schema (typed/untyped)


```python
def SparkDataFrameTransformer()
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
    t: typing.Type[pyspark.sql.dataframe.DataFrame],
) -> flytekit.models.types.LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type |
|-|-|
| `t` | `typing.Type[pyspark.sql.dataframe.DataFrame]` |

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
    ctx: flytekit.core.context_manager.FlyteContext,
    python_val: pyspark.sql.dataframe.DataFrame,
    python_type: typing.Type[pyspark.sql.dataframe.DataFrame],
    expected: flytekit.models.types.LiteralType,
) -> flytekit.models.literals.Literal
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `python_val` | `pyspark.sql.dataframe.DataFrame` |
| `python_type` | `typing.Type[pyspark.sql.dataframe.DataFrame]` |
| `expected` | `flytekit.models.types.LiteralType` |

#### to_python_value()

```python
def to_python_value(
    ctx: flytekit.core.context_manager.FlyteContext,
    lv: flytekit.models.literals.Literal,
    expected_python_type: typing.Type[pyspark.sql.dataframe.DataFrame],
) -> ~T
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `lv` | `flytekit.models.literals.Literal` |
| `expected_python_type` | `typing.Type[pyspark.sql.dataframe.DataFrame]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_async` |  |  |
| `name` |  |  |
| `python_type` |  | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` |  | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

