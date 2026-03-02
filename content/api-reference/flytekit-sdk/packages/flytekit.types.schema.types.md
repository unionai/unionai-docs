---
title: flytekit.types.schema.types
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.types.schema.types

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteSchema`](.././flytekit.types.schema.types#flytekittypesschematypesflyteschema) |  |
| [`FlyteSchemaTransformer`](.././flytekit.types.schema.types#flytekittypesschematypesflyteschematransformer) |  |
| [`LocalIOSchemaReader`](.././flytekit.types.schema.types#flytekittypesschematypeslocalioschemareader) |  |
| [`LocalIOSchemaWriter`](.././flytekit.types.schema.types#flytekittypesschematypeslocalioschemawriter) |  |
| [`SchemaEngine`](.././flytekit.types.schema.types#flytekittypesschematypesschemaengine) | This is the core Engine that handles all schema sub-systems. |
| [`SchemaFormat`](.././flytekit.types.schema.types#flytekittypesschematypesschemaformat) | Represents the schema storage format (at rest). |
| [`SchemaHandler`](.././flytekit.types.schema.types#flytekittypesschematypesschemahandler) |  |
| [`SchemaOpenMode`](.././flytekit.types.schema.types#flytekittypesschematypesschemaopenmode) |  |
| [`SchemaReader`](.././flytekit.types.schema.types#flytekittypesschematypesschemareader) | Base SchemaReader to handle any readers (that can manage their own IO or otherwise). |
| [`SchemaWriter`](.././flytekit.types.schema.types#flytekittypesschematypesschemawriter) |  |

### Methods

| Method | Description |
|-|-|
| [`generate_ordered_files()`](#generate_ordered_files) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `MESSAGEPACK` | `str` |  |
| `T` | `TypeVar` |  |

## Methods

#### generate_ordered_files()

```python
def generate_ordered_files(
    directory: os.PathLike,
    n: int,
) -> typing.Generator[str, None, None]
```
| Parameter | Type | Description |
|-|-|-|
| `directory` | `os.PathLike` | |
| `n` | `int` | |

## flytekit.types.schema.types.FlyteSchema

```python
class FlyteSchema(
    local_path: typing.Optional[str],
    remote_path: typing.Optional[str],
    supported_mode: SchemaOpenMode,
    downloader: typing.Optional[typing.Callable],
)
```
| Parameter | Type | Description |
|-|-|-|
| `local_path` | `typing.Optional[str]` | |
| `remote_path` | `typing.Optional[str]` | |
| `supported_mode` | `SchemaOpenMode` | |
| `downloader` | `typing.Optional[typing.Callable]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `local_path` | `None` |  |
| `supported_mode` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`as_readonly()`](#as_readonly) |  |
| [`column_names()`](#column_names) |  |
| [`columns()`](#columns) |  |
| [`deserialize_flyte_schema()`](#deserialize_flyte_schema) |  |
| [`format()`](#format) |  |
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`open()`](#open) | Returns a reader or writer depending on the mode of the object when created. |
| [`serialize_flyte_schema()`](#serialize_flyte_schema) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


#### as_readonly()

```python
def as_readonly()
```
#### column_names()

```python
def column_names()
```
#### columns()

```python
def columns()
```
#### deserialize_flyte_schema()

```python
def deserialize_flyte_schema(
    info,
) -> FlyteSchema
```
| Parameter | Type | Description |
|-|-|-|
| `info` |  | |

#### format()

```python
def format()
```
#### from_dict()

```python
def from_dict(
    d,
    dialect,
)
```
| Parameter | Type | Description |
|-|-|-|
| `d` |  | |
| `dialect` |  | |

#### from_json()

```python
def from_json(
    data: typing.Union[str, bytes, bytearray],
    decoder: collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]],
    from_dict_kwargs: typing.Any,
) -> ~T
```
| Parameter | Type | Description |
|-|-|-|
| `data` | `typing.Union[str, bytes, bytearray]` | |
| `decoder` | `collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]]` | |
| `from_dict_kwargs` | `typing.Any` | |

#### open()

```python
def open(
    dataframe_fmt: typing.Optional[type],
    override_mode: typing.Optional[SchemaOpenMode],
) -> typing.Union[SchemaReader, SchemaWriter]
```
Returns a reader or writer depending on the mode of the object when created. This mode can be
overridden, but will depend on whether the override can be performed. For example, if the Object was
created in a read-mode a "write mode" override is not allowed.
if the object was created in write-mode, a read is allowed.



| Parameter | Type | Description |
|-|-|-|
| `dataframe_fmt` | `typing.Optional[type]` | Type of the dataframe for example pandas.DataFrame etc |
| `override_mode` | `typing.Optional[SchemaOpenMode]` | overrides the default mode (Read, Write) SchemaOpenMode.READ, SchemaOpenMode.Write So if you have written to a schema and want to re-open it for reading, you can use this mode. A ReadOnly Schema object cannot be opened in write mode. |

#### serialize_flyte_schema()

```python
def serialize_flyte_schema()
```
#### to_dict()

```python
def to_dict()
```
#### to_json()

```python
def to_json(
    encoder: collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]],
    to_dict_kwargs: typing.Any,
) -> typing.Union[str, bytes, bytearray]
```
| Parameter | Type | Description |
|-|-|-|
| `encoder` | `collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]]` | |
| `to_dict_kwargs` | `typing.Any` | |

## flytekit.types.schema.types.FlyteSchemaTransformer

```python
def FlyteSchemaTransformer()
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
| [`dict_to_flyte_schema()`](#dict_to_flyte_schema) |  |
| [`from_binary_idl()`](#from_binary_idl) | If the input is from flytekit, the Life Cycle will be as follows:. |
| [`from_generic_idl()`](#from_generic_idl) | If the input is from Flyte Console, the Life Cycle will be as follows:. |
| [`get_literal_type()`](#get_literal_type) | Converts the python type to a Flyte LiteralType. |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type. |
| [`isinstance_generic()`](#isinstance_generic) |  |
| [`to_html()`](#to_html) | Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div. |
| [`to_literal()`](#to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`to_python_value()`](#to_python_value) | Converts the given Literal to a Python Type. |


#### assert_type()

```python
def assert_type(
    t: Type[FlyteSchema],
    v: typing.Any,
)
```
| Parameter | Type | Description |
|-|-|-|
| `t` | `Type[FlyteSchema]` | |
| `v` | `typing.Any` | |

#### async_to_literal()

```python
def async_to_literal(
    ctx: FlyteContext,
    python_val: FlyteSchema,
    python_type: Type[FlyteSchema],
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
| `python_val` | `FlyteSchema` | The actual value to be transformed |
| `python_type` | `Type[FlyteSchema]` | The assumed type of the value (this matches the declared type on the function) |
| `expected` | `LiteralType` | Expected Literal Type |

#### async_to_python_value()

```python
def async_to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[FlyteSchema],
) -> FlyteSchema
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | FlyteContext |
| `lv` | `Literal` | The received literal Value |
| `expected_python_type` | `Type[FlyteSchema]` | Expected native python type that should be returned |

#### dict_to_flyte_schema()

```python
def dict_to_flyte_schema(
    dict_obj: typing.Dict[str, str],
    expected_python_type: Type[FlyteSchema],
) -> FlyteSchema
```
| Parameter | Type | Description |
|-|-|-|
| `dict_obj` | `typing.Dict[str, str]` | |
| `expected_python_type` | `Type[FlyteSchema]` | |

#### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: Binary,
    expected_python_type: Type[FlyteSchema],
) -> FlyteSchema
```
If the input is from flytekit, the Life Cycle will be as follows:

Life Cycle:
binary IDL                 -&gt; resolved binary         -&gt; bytes                   -&gt; expected Python object
(flytekit customized          (propeller processing)     (flytekit binary IDL)      (flytekit customized
serialization)                                                                       deserialization)

Example Code:
@dataclass
class DC:
    fs: FlyteSchema

@workflow
def wf(dc: DC):
    t_fs(dc.fs)

Note:
- The deserialization is the same as put a flyte schema in a dataclass, which will deserialize by the mashumaro's API.

Related PR:
- Title: Override Dataclass Serialization/Deserialization Behavior for FlyteTypes via Mashumaro
- Link: https://github.com/flyteorg/flytekit/pull/2554


| Parameter | Type | Description |
|-|-|-|
| `binary_idl_object` | `Binary` | |
| `expected_python_type` | `Type[FlyteSchema]` | |

#### from_generic_idl()

```python
def from_generic_idl(
    generic: Struct,
    expected_python_type: Type[FlyteSchema],
) -> FlyteSchema
```
If the input is from Flyte Console, the Life Cycle will be as follows:

Life Cycle:
json str            -&gt; protobuf struct         -&gt; resolved protobuf struct   -&gt; expected Python object
(console user input)   (console output)           (propeller)                   (flytekit customized deserialization)

Example Code:
@dataclass
class DC:
    fs: FlyteSchema

@workflow
def wf(dc: DC):
    t_fs(dc.fs)

Note:
- The deserialization is the same as put a flyte schema in a dataclass, which will deserialize by the mashumaro's API.

Related PR:
- Title: Override Dataclass Serialization/Deserialization Behavior for FlyteTypes via Mashumaro
- Link: https://github.com/flyteorg/flytekit/pull/2554


| Parameter | Type | Description |
|-|-|-|
| `generic` | `Struct` | |
| `expected_python_type` | `Type[FlyteSchema]` | |

#### get_literal_type()

```python
def get_literal_type(
    t: Type[FlyteSchema],
) -> LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type | Description |
|-|-|-|
| `t` | `Type[FlyteSchema]` | |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> Type[FlyteSchema]
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

## flytekit.types.schema.types.LocalIOSchemaReader

```python
class LocalIOSchemaReader(
    from_path: str,
    cols: typing.Optional[typing.Dict[str, type]],
    fmt: SchemaFormat,
)
```
| Parameter | Type | Description |
|-|-|-|
| `from_path` | `str` | |
| `cols` | `typing.Optional[typing.Dict[str, type]]` | |
| `fmt` | `SchemaFormat` | |

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

## flytekit.types.schema.types.LocalIOSchemaWriter

```python
class LocalIOSchemaWriter(
    to_local_path: str,
    cols: typing.Optional[typing.Dict[str, type]],
    fmt: SchemaFormat,
)
```
| Parameter | Type | Description |
|-|-|-|
| `to_local_path` | `str` | |
| `cols` | `typing.Optional[typing.Dict[str, type]]` | |
| `fmt` | `SchemaFormat` | |

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

## flytekit.types.schema.types.SchemaEngine

This is the core Engine that handles all schema sub-systems. All schema types needs to be registered with this
to allow direct support for that type in FlyteSchema.
e.g. of possible supported types are Pandas.DataFrame, Spark.DataFrame, Vaex.DataFrame, etc.



### Methods

| Method | Description |
|-|-|
| [`get_handler()`](#get_handler) |  |
| [`register_handler()`](#register_handler) | Register a new handler that can create a SchemaReader and SchemaWriter for the expected type. |


#### get_handler()

```python
def get_handler(
    t: Type,
) -> SchemaHandler
```
| Parameter | Type | Description |
|-|-|-|
| `t` | `Type` | |

#### register_handler()

```python
def register_handler(
    h: SchemaHandler,
)
```
Register a new handler that can create a SchemaReader and SchemaWriter for the expected type.


| Parameter | Type | Description |
|-|-|-|
| `h` | `SchemaHandler` | |

## flytekit.types.schema.types.SchemaFormat

Represents the schema storage format (at rest).
Currently only parquet is supported



## flytekit.types.schema.types.SchemaHandler

```python
class SchemaHandler(
    name: str,
    object_type: Type,
    reader: Type[SchemaReader],
    writer: Type[SchemaWriter],
    handles_remote_io: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `object_type` | `Type` | |
| `reader` | `Type[SchemaReader]` | |
| `writer` | `Type[SchemaWriter]` | |
| `handles_remote_io` | `bool` | |

## flytekit.types.schema.types.SchemaOpenMode

## flytekit.types.schema.types.SchemaReader

Base SchemaReader to handle any readers (that can manage their own IO or otherwise)
Use the simplified base LocalIOSchemaReader for non distributed dataframes



```python
class SchemaReader(
    from_path: str,
    cols: typing.Optional[typing.Dict[str, type]],
    fmt: SchemaFormat,
)
```
| Parameter | Type | Description |
|-|-|-|
| `from_path` | `str` | |
| `cols` | `typing.Optional[typing.Dict[str, type]]` | |
| `fmt` | `SchemaFormat` | |

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

## flytekit.types.schema.types.SchemaWriter

```python
class SchemaWriter(
    to_path: str,
    cols: typing.Optional[typing.Dict[str, type]],
    fmt: SchemaFormat,
)
```
| Parameter | Type | Description |
|-|-|-|
| `to_path` | `str` | |
| `cols` | `typing.Optional[typing.Dict[str, type]]` | |
| `fmt` | `SchemaFormat` | |

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

