---
title: flytekit.types.schema.types
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.types.schema.types

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteSchema`](.././flytekit.types.schema.types#flytekittypesschematypesflyteschema) |  |
| [`FlyteSchemaTransformer`](.././flytekit.types.schema.types#flytekittypesschematypesflyteschematransformer) | Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`LocalIOSchemaReader`](.././flytekit.types.schema.types#flytekittypesschematypeslocalioschemareader) | Base SchemaReader to handle any readers (that can manage their own IO or otherwise). |
| [`LocalIOSchemaWriter`](.././flytekit.types.schema.types#flytekittypesschematypeslocalioschemawriter) | Abstract base class for generic types. |
| [`SchemaEngine`](.././flytekit.types.schema.types#flytekittypesschematypesschemaengine) | This is the core Engine that handles all schema sub-systems. |
| [`SchemaHandler`](.././flytekit.types.schema.types#flytekittypesschematypesschemahandler) |  |
| [`SchemaReader`](.././flytekit.types.schema.types#flytekittypesschematypesschemareader) | Base SchemaReader to handle any readers (that can manage their own IO or otherwise). |
| [`SchemaWriter`](.././flytekit.types.schema.types#flytekittypesschematypesschemawriter) | Abstract base class for generic types. |

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
| Parameter | Type |
|-|-|
| `directory` | `os.PathLike` |
| `n` | `int` |

## flytekit.types.schema.types.FlyteSchema

```python
class FlyteSchema(
    local_path: typing.Optional[str],
    remote_path: typing.Optional[str],
    supported_mode: SchemaOpenMode,
    downloader: typing.Optional[typing.Callable],
)
```
| Parameter | Type |
|-|-|
| `local_path` | `typing.Optional[str]` |
| `remote_path` | `typing.Optional[str]` |
| `supported_mode` | `SchemaOpenMode` |
| `downloader` | `typing.Optional[typing.Callable]` |

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
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

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
| Parameter | Type |
|-|-|
| `d` |  |
| `dialect` |  |

#### from_json()

```python
def from_json(
    data: typing.Union[str, bytes, bytearray],
    decoder: collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]],
    from_dict_kwargs: typing.Any,
) -> ~T
```
| Parameter | Type |
|-|-|
| `data` | `typing.Union[str, bytes, bytearray]` |
| `decoder` | `collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]]` |
| `from_dict_kwargs` | `typing.Any` |

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



| Parameter | Type |
|-|-|
| `dataframe_fmt` | `typing.Optional[type]` |
| `override_mode` | `typing.Optional[SchemaOpenMode]` |

#### serialize_flyte_schema()

```python
def serialize_flyte_schema(
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

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
| Parameter | Type |
|-|-|
| `encoder` | `collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]]` |
| `to_dict_kwargs` | `typing.Any` |

### Properties

| Property | Type | Description |
|-|-|-|
| `local_path` |  |  |
| `supported_mode` |  |  |

## flytekit.types.schema.types.FlyteSchemaTransformer

Base transformer type that should be implemented for every python native type that can be handled by flytekit


```python
def FlyteSchemaTransformer()
```
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
| Parameter | Type |
|-|-|
| `t` | `Type[FlyteSchema]` |
| `v` | `typing.Any` |

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


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `FlyteSchema` |
| `python_type` | `Type[FlyteSchema]` |
| `expected` | `LiteralType` |

#### async_to_python_value()

```python
def async_to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[FlyteSchema],
) -> FlyteSchema
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[FlyteSchema]` |

#### dict_to_flyte_schema()

```python
def dict_to_flyte_schema(
    dict_obj: typing.Dict[str, str],
    expected_python_type: Type[FlyteSchema],
) -> FlyteSchema
```
| Parameter | Type |
|-|-|
| `dict_obj` | `typing.Dict[str, str]` |
| `expected_python_type` | `Type[FlyteSchema]` |

#### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: Binary,
    expected_python_type: Type[FlyteSchema],
) -> FlyteSchema
```
If the input is from flytekit, the Life Cycle will be as follows:

Life Cycle:
binary IDL                 -> resolved binary         -> bytes                   -> expected Python object
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


| Parameter | Type |
|-|-|
| `binary_idl_object` | `Binary` |
| `expected_python_type` | `Type[FlyteSchema]` |

#### from_generic_idl()

```python
def from_generic_idl(
    generic: Struct,
    expected_python_type: Type[FlyteSchema],
) -> FlyteSchema
```
If the input is from Flyte Console, the Life Cycle will be as follows:

Life Cycle:
json str            -> protobuf struct         -> resolved protobuf struct   -> expected Python object
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


| Parameter | Type |
|-|-|
| `generic` | `Struct` |
| `expected_python_type` | `Type[FlyteSchema]` |

#### get_literal_type()

```python
def get_literal_type(
    t: Type[FlyteSchema],
) -> LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type |
|-|-|
| `t` | `Type[FlyteSchema]` |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> Type[FlyteSchema]
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

## flytekit.types.schema.types.LocalIOSchemaReader

Base SchemaReader to handle any readers (that can manage their own IO or otherwise)
Use the simplified base LocalIOSchemaReader for non distributed dataframes


```python
class LocalIOSchemaReader(
    from_path: str,
    cols: typing.Optional[typing.Dict[str, type]],
    fmt: SchemaFormat,
)
```
| Parameter | Type |
|-|-|
| `from_path` | `str` |
| `cols` | `typing.Optional[typing.Dict[str, type]]` |
| `fmt` | `SchemaFormat` |

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

## flytekit.types.schema.types.LocalIOSchemaWriter

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
class LocalIOSchemaWriter(
    to_local_path: str,
    cols: typing.Optional[typing.Dict[str, type]],
    fmt: SchemaFormat,
)
```
| Parameter | Type |
|-|-|
| `to_local_path` | `str` |
| `cols` | `typing.Optional[typing.Dict[str, type]]` |
| `fmt` | `SchemaFormat` |

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
| Parameter | Type |
|-|-|
| `t` | `Type` |

#### register_handler()

```python
def register_handler(
    h: SchemaHandler,
)
```
Register a new handler that can create a SchemaReader and SchemaWriter for the expected type.


| Parameter | Type |
|-|-|
| `h` | `SchemaHandler` |

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
| Parameter | Type |
|-|-|
| `name` | `str` |
| `object_type` | `Type` |
| `reader` | `Type[SchemaReader]` |
| `writer` | `Type[SchemaWriter]` |
| `handles_remote_io` | `bool` |

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
| Parameter | Type |
|-|-|
| `from_path` | `str` |
| `cols` | `typing.Optional[typing.Dict[str, type]]` |
| `fmt` | `SchemaFormat` |

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

## flytekit.types.schema.types.SchemaWriter

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
class SchemaWriter(
    to_path: str,
    cols: typing.Optional[typing.Dict[str, type]],
    fmt: SchemaFormat,
)
```
| Parameter | Type |
|-|-|
| `to_path` | `str` |
| `cols` | `typing.Optional[typing.Dict[str, type]]` |
| `fmt` | `SchemaFormat` |

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

