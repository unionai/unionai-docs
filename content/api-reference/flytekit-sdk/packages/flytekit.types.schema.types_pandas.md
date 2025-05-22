---
title: flytekit.types.schema.types_pandas
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.types.schema.types_pandas

## Directory

### Classes

| Class | Description |
|-|-|
| [`PandasDataFrameTransformer`](.././flytekit.types.schema.types_pandas#flytekittypesschematypes_pandaspandasdataframetransformer) | Transforms a pd. |
| [`PandasSchemaReader`](.././flytekit.types.schema.types_pandas#flytekittypesschematypes_pandaspandasschemareader) | Base SchemaReader to handle any readers (that can manage their own IO or otherwise). |
| [`PandasSchemaWriter`](.././flytekit.types.schema.types_pandas#flytekittypesschematypes_pandaspandasschemawriter) | Abstract base class for generic types. |
| [`ParquetIO`](.././flytekit.types.schema.types_pandas#flytekittypesschematypes_pandasparquetio) |  |

## flytekit.types.schema.types_pandas.PandasDataFrameTransformer

Transforms a pd.DataFrame to Schema without column types.


```python
def PandasDataFrameTransformer()
```
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
| Parameter | Type |
|-|-|
| `t` | `Type[T]` |
| `v` | `T` |

#### async_to_literal()

```python
def async_to_literal(
    ctx: flytekit.core.context_manager.FlyteContext,
    python_val: pandas.core.frame.DataFrame,
    python_type: typing.Type[pandas.core.frame.DataFrame],
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
| `python_val` | `pandas.core.frame.DataFrame` |
| `python_type` | `typing.Type[pandas.core.frame.DataFrame]` |
| `expected` | `flytekit.models.types.LiteralType` |

#### async_to_python_value()

```python
def async_to_python_value(
    ctx: flytekit.core.context_manager.FlyteContext,
    lv: flytekit.models.literals.Literal,
    expected_python_type: typing.Type[pandas.core.frame.DataFrame],
) -> pandas.core.frame.DataFrame
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `lv` | `flytekit.models.literals.Literal` |
| `expected_python_type` | `typing.Type[pandas.core.frame.DataFrame]` |

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
    t: typing.Type[pandas.core.frame.DataFrame],
) -> flytekit.models.types.LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type |
|-|-|
| `t` | `typing.Type[pandas.core.frame.DataFrame]` |

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
    ctx: flytekit.core.context_manager.FlyteContext,
    python_val: pandas.core.frame.DataFrame,
    expected_python_type: typing.Type[~T],
)
```
Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `python_val` | `pandas.core.frame.DataFrame` |
| `expected_python_type` | `typing.Type[~T]` |

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


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `typing.Any` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
) -> Optional[T]
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[T]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_async` |  |  |
| `name` |  |  |
| `python_type` |  | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` |  | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

## flytekit.types.schema.types_pandas.PandasSchemaReader

Base SchemaReader to handle any readers (that can manage their own IO or otherwise)
Use the simplified base LocalIOSchemaReader for non distributed dataframes


```python
class PandasSchemaReader(
    local_dir: str,
    cols: typing.Optional[typing.Dict[str, type]],
    fmt: <enum 'SchemaFormat'>,
)
```
| Parameter | Type |
|-|-|
| `local_dir` | `str` |
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
) -> T
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### iter()

```python
def iter(
    kwargs,
) -> typing.Generator[T, None, None]
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `column_names` |  |  |
| `from_path` |  |  |

## flytekit.types.schema.types_pandas.PandasSchemaWriter

Abstract base class for generic types.

On Python 3.12 and newer, generic classes implicitly inherit from
Generic when they declare a parameter list after the class's name::

    class Mapping[KT, VT]:
        def __getitem__(self, key: KT) -> VT:
            ...
        # Etc.

On older versions of Python, however, generic classes have to
explicitly inherit from Generic.

After a class has been declared to be generic, it can then be used as
follows::

    def lookup_name[KT, VT](mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
        try:
            return mapping[key]
        except KeyError:
            return default


```python
class PandasSchemaWriter(
    local_dir: str,
    cols: typing.Optional[typing.Dict[str, type]],
    fmt: <enum 'SchemaFormat'>,
)
```
| Parameter | Type |
|-|-|
| `local_dir` | `str` |
| `cols` | `typing.Optional[typing.Dict[str, type]]` |
| `fmt` | `<enum 'SchemaFormat'>` |

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
| Parameter | Type |
|-|-|
| `dfs` |  |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `column_names` |  |  |
| `to_path` |  |  |

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
) -> pandas.core.frame.DataFrame
```
| Parameter | Type |
|-|-|
| `files` | `os.PathLike` |
| `columns` | `typing.Optional[typing.List[str]]` |
| `kwargs` | ``**kwargs`` |

#### write()

```python
def write(
    df: pandas.core.frame.DataFrame,
    to_file: os.PathLike,
    coerce_timestamps: str,
    allow_truncated_timestamps: bool,
    kwargs,
)
```
Writes data frame as a chunk to the local directory owned by the Schema object.  Will later be uploaded to s3.


| Parameter | Type |
|-|-|
| `df` | `pandas.core.frame.DataFrame` |
| `to_file` | `os.PathLike` |
| `coerce_timestamps` | `str` |
| `allow_truncated_timestamps` | `bool` |
| `kwargs` | ``**kwargs`` |

