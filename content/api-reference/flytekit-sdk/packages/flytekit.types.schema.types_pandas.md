---
title: flytekit.types.schema.types_pandas
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.types.schema.types_pandas

## Directory

### Classes

| Class | Description |
|-|-|
| [`PandasDataFrameTransformer`](.././flytekit.types.schema.types_pandas#flytekittypesschematypes_pandaspandasdataframetransformer) | Transforms a pd. |
| [`PandasSchemaReader`](.././flytekit.types.schema.types_pandas#flytekittypesschematypes_pandaspandasschemareader) |  |
| [`PandasSchemaWriter`](.././flytekit.types.schema.types_pandas#flytekittypesschematypes_pandaspandasschemawriter) |  |
| [`ParquetIO`](.././flytekit.types.schema.types_pandas#flytekittypesschematypes_pandasparquetio) |  |

## flytekit.types.schema.types_pandas.PandasDataFrameTransformer

Transforms a pd.DataFrame to Schema without column types.



```python
def PandasDataFrameTransformer()
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
| Parameter | Type | Description |
|-|-|-|
| `t` | `Type[T]` | |
| `v` | `T` | |

#### async_to_literal()

```python
def async_to_literal(
    ctx: flytekit.core.context_manager.FlyteContext,
    python_val: pandas.DataFrame,
    python_type: typing.Type[pandas.DataFrame],
    expected: flytekit.models.types.LiteralType,
) -> flytekit.models.literals.Literal
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | A FlyteContext, useful in accessing the filesystem and other attributes |
| `python_val` | `pandas.DataFrame` | The actual value to be transformed |
| `python_type` | `typing.Type[pandas.DataFrame]` | The assumed type of the value (this matches the declared type on the function) |
| `expected` | `flytekit.models.types.LiteralType` | Expected Literal Type |

#### async_to_python_value()

```python
def async_to_python_value(
    ctx: flytekit.core.context_manager.FlyteContext,
    lv: flytekit.models.literals.Literal,
    expected_python_type: typing.Type[pandas.DataFrame],
) -> pandas.DataFrame
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | FlyteContext |
| `lv` | `flytekit.models.literals.Literal` | The received literal Value |
| `expected_python_type` | `typing.Type[pandas.DataFrame]` | Expected native python type that should be returned |

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
    t: typing.Type[pandas.DataFrame],
) -> flytekit.models.types.LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type | Description |
|-|-|-|
| `t` | `typing.Type[pandas.DataFrame]` | |

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

#### to_html()

```python
def to_html(
    ctx: flytekit.core.context_manager.FlyteContext,
    python_val: pandas.DataFrame,
    expected_python_type: typing.Type[~T],
)
```
Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `python_val` | `pandas.DataFrame` | |
| `expected_python_type` | `typing.Type[~T]` | |

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


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | A FlyteContext, useful in accessing the filesystem and other attributes |
| `python_val` | `typing.Any` | The actual value to be transformed |
| `python_type` | `Type[T]` | The assumed type of the value (this matches the declared type on the function) |
| `expected` | `LiteralType` | Expected Literal Type |

#### to_python_value()

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

## flytekit.types.schema.types_pandas.PandasSchemaReader

```python
class PandasSchemaReader(
    local_dir: str,
    cols: typing.Optional[typing.Dict[str, type]],
    fmt: <enum 'SchemaFormat'>,
)
```
| Parameter | Type | Description |
|-|-|-|
| `local_dir` | `str` | |
| `cols` | `typing.Optional[typing.Dict[str, type]]` | |
| `fmt` | `<enum 'SchemaFormat'>` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `column_names` | `None` |  |
| `from_path` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`all()`](#all) |  |
| [`iter()`](#iter) |  |


#### all()

```python
def all(
    kwargs,
) -> T
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

#### iter()

```python
def iter(
    kwargs,
) -> typing.Generator[T, None, None]
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

## flytekit.types.schema.types_pandas.PandasSchemaWriter

```python
class PandasSchemaWriter(
    local_dir: str,
    cols: typing.Optional[typing.Dict[str, type]],
    fmt: <enum 'SchemaFormat'>,
)
```
| Parameter | Type | Description |
|-|-|-|
| `local_dir` | `str` | |
| `cols` | `typing.Optional[typing.Dict[str, type]]` | |
| `fmt` | `<enum 'SchemaFormat'>` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `column_names` | `None` |  |
| `to_path` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`write()`](#write) |  |


#### write()

```python
def write(
    dfs,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `dfs` |  | |
| `kwargs` | `**kwargs` | |

## flytekit.types.schema.types_pandas.ParquetIO

### Methods

| Method | Description |
|-|-|
| [`read()`](#read) |  |
| [`write()`](#write) | Writes data frame as a chunk to the local directory owned by the Schema object. |


#### read()

```python
def read(
    files: os.PathLike,
    columns: typing.Optional[typing.List[str]],
    kwargs,
) -> pandas.DataFrame
```
| Parameter | Type | Description |
|-|-|-|
| `files` | `os.PathLike` | |
| `columns` | `typing.Optional[typing.List[str]]` | |
| `kwargs` | `**kwargs` | |

#### write()

```python
def write(
    df: pandas.DataFrame,
    to_file: os.PathLike,
    coerce_timestamps: str,
    allow_truncated_timestamps: bool,
    kwargs,
)
```
Writes data frame as a chunk to the local directory owned by the Schema object.  Will later be uploaded to s3.


| Parameter | Type | Description |
|-|-|-|
| `df` | `pandas.DataFrame` | data frame to write as parquet |
| `to_file` | `os.PathLike` | Sink file to write the dataframe to |
| `coerce_timestamps` | `str` | format to store timestamp in parquet. 'us', 'ms', 's' are allowed values. Note: if your timestamps will lose data due to the coercion, your write will fail!  Nanoseconds are problematic in the Parquet format and will not work. See allow_truncated_timestamps. |
| `allow_truncated_timestamps` | `bool` | default False. Allow truncation when coercing timestamps to a coarser resolution. |
| `kwargs` | `**kwargs` | |

