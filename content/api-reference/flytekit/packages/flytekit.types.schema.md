---
title: flytekit.types.schema
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.types.schema

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteSchema`](.././flytekit.types.schema#flytekittypesschemaflyteschema) | None. |
| [`FlyteSchemaTransformer`](.././flytekit.types.schema#flytekittypesschemaflyteschematransformer) | Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`LocalIOSchemaReader`](.././flytekit.types.schema#flytekittypesschemalocalioschemareader) | Base SchemaReader to handle any readers (that can manage their own IO or otherwise). |
| [`LocalIOSchemaWriter`](.././flytekit.types.schema#flytekittypesschemalocalioschemawriter) | Abstract base class for generic types. |
| [`SchemaEngine`](.././flytekit.types.schema#flytekittypesschemaschemaengine) | This is the core Engine that handles all schema sub-systems. |
| [`SchemaFormat`](.././flytekit.types.schema#flytekittypesschemaschemaformat) | Represents the schema storage format (at rest). |
| [`SchemaHandler`](.././flytekit.types.schema#flytekittypesschemaschemahandler) | None. |
| [`SchemaOpenMode`](.././flytekit.types.schema#flytekittypesschemaschemaopenmode) | Create a collection of name/value pairs. |
| [`SchemaReader`](.././flytekit.types.schema#flytekittypesschemaschemareader) | Base SchemaReader to handle any readers (that can manage their own IO or otherwise). |
| [`SchemaWriter`](.././flytekit.types.schema#flytekittypesschemaschemawriter) | Abstract base class for generic types. |

## flytekit.types.schema.FlyteSchema

```python
def FlyteSchema(
    local_path: typing.Optional[str],
    remote_path: typing.Optional[str],
    supported_mode: SchemaOpenMode,
    downloader: typing.Optional[typing.Callable],
):
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
| [`as_readonly()`](#as_readonly) | None |
| [`column_names()`](#column_names) | None |
| [`columns()`](#columns) | None |
| [`deserialize_flyte_schema()`](#deserialize_flyte_schema) | None |
| [`format()`](#format) | None |
| [`from_dict()`](#from_dict) | None |
| [`from_json()`](#from_json) | None |
| [`open()`](#open) | Returns a reader or writer depending on the mode of the object when created |
| [`serialize_flyte_schema()`](#serialize_flyte_schema) | None |
| [`to_dict()`](#to_dict) | None |
| [`to_json()`](#to_json) | None |


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
):
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
):
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
):
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
):
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
):
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
):
```
| Parameter | Type |
|-|-|
| `encoder` | `collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]]` |
| `to_dict_kwargs` | `typing.Any` |

### Properties

| Property | Type | Description |
|-|-|-|
| local_path |  |  |
| supported_mode |  |  |

## flytekit.types.schema.FlyteSchemaTransformer

Base transformer type that should be implemented for every python native type that can be handled by flytekit


```python
def FlyteSchemaTransformer()
```
### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) | None |
| [`async_to_literal()`](#async_to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type |
| [`async_to_python_value()`](#async_to_python_value) | Converts the given Literal to a Python Type |
| [`dict_to_flyte_schema()`](#dict_to_flyte_schema) | None |
| [`from_binary_idl()`](#from_binary_idl) | If the input is from flytekit, the Life Cycle will be as follows: |
| [`from_generic_idl()`](#from_generic_idl) | If the input is from Flyte Console, the Life Cycle will be as follows: |
| [`get_literal_type()`](#get_literal_type) | Converts the python type to a Flyte LiteralType |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type |
| [`isinstance_generic()`](#isinstance_generic) | None |
| [`to_html()`](#to_html) | Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div |
| [`to_literal()`](#to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type |
| [`to_python_value()`](#to_python_value) | Converts the given Literal to a Python Type |


#### assert_type()

```python
def assert_type(
    t: Type[FlyteSchema],
    v: typing.Any,
):
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
):
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
):
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
):
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
):
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
):
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
):
```
Converts the python type to a Flyte LiteralType


| Parameter | Type |
|-|-|
| `t` | `Type[FlyteSchema]` |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
):
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
):
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
):
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

#### to_python_value()

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

### Properties

| Property | Type | Description |
|-|-|-|
| is_async |  |  |
| name |  |  |
| python_type |  |  |
| type_assertions_enabled |  |  |

## flytekit.types.schema.LocalIOSchemaReader

Base SchemaReader to handle any readers (that can manage their own IO or otherwise)
Use the simplified base LocalIOSchemaReader for non distributed dataframes


```python
def LocalIOSchemaReader(
    from_path: str,
    cols: typing.Optional[typing.Dict[str, type]],
    fmt: SchemaFormat,
):
```
| Parameter | Type |
|-|-|
| `from_path` | `str` |
| `cols` | `typing.Optional[typing.Dict[str, type]]` |
| `fmt` | `SchemaFormat` |

### Methods

| Method | Description |
|-|-|
| [`all()`](#all) | None |
| [`iter()`](#iter) | None |


#### all()

```python
def all(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### iter()

```python
def iter(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| column_names |  |  |
| from_path |  |  |

## flytekit.types.schema.LocalIOSchemaWriter

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
def LocalIOSchemaWriter(
    to_local_path: str,
    cols: typing.Optional[typing.Dict[str, type]],
    fmt: SchemaFormat,
):
```
| Parameter | Type |
|-|-|
| `to_local_path` | `str` |
| `cols` | `typing.Optional[typing.Dict[str, type]]` |
| `fmt` | `SchemaFormat` |

### Methods

| Method | Description |
|-|-|
| [`write()`](#write) | None |


#### write()

```python
def write(
    dfs,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `dfs` |  |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| column_names |  |  |
| to_path |  |  |

## flytekit.types.schema.SchemaEngine

This is the core Engine that handles all schema sub-systems. All schema types needs to be registered with this
to allow direct support for that type in FlyteSchema.
e.g. of possible supported types are Pandas.DataFrame, Spark.DataFrame, Vaex.DataFrame, etc.


### Methods

| Method | Description |
|-|-|
| [`get_handler()`](#get_handler) | None |
| [`register_handler()`](#register_handler) | Register a new handler that can create a SchemaReader and SchemaWriter for the expected type |


#### get_handler()

```python
def get_handler(
    t: Type,
):
```
| Parameter | Type |
|-|-|
| `t` | `Type` |

#### register_handler()

```python
def register_handler(
    h: SchemaHandler,
):
```
Register a new handler that can create a SchemaReader and SchemaWriter for the expected type.


| Parameter | Type |
|-|-|
| `h` | `SchemaHandler` |

## flytekit.types.schema.SchemaFormat

Represents the schema storage format (at rest).
Currently only parquet is supported


## flytekit.types.schema.SchemaHandler

```python
def SchemaHandler(
    name: str,
    object_type: Type,
    reader: Type[SchemaReader],
    writer: Type[SchemaWriter],
    handles_remote_io: bool,
):
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `object_type` | `Type` |
| `reader` | `Type[SchemaReader]` |
| `writer` | `Type[SchemaWriter]` |
| `handles_remote_io` | `bool` |

## flytekit.types.schema.SchemaOpenMode

Create a collection of name/value pairs.

Example enumeration:

>>> class Color(Enum):
...     RED = 1
...     BLUE = 2
...     GREEN = 3

Access them by:

- attribute access:

>>> Color.RED
<Color.RED: 1>

- value lookup:

>>> Color(1)
<Color.RED: 1>

- name lookup:

>>> Color['RED']
<Color.RED: 1>

Enumerations can be iterated over, and know how many members they have:

>>> len(Color)
3

>>> list(Color)
[<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

Methods can be added to enumerations, and members can have their own
attributes -- see the documentation for details.


## flytekit.types.schema.SchemaReader

Base SchemaReader to handle any readers (that can manage their own IO or otherwise)
Use the simplified base LocalIOSchemaReader for non distributed dataframes


```python
def SchemaReader(
    from_path: str,
    cols: typing.Optional[typing.Dict[str, type]],
    fmt: SchemaFormat,
):
```
| Parameter | Type |
|-|-|
| `from_path` | `str` |
| `cols` | `typing.Optional[typing.Dict[str, type]]` |
| `fmt` | `SchemaFormat` |

### Methods

| Method | Description |
|-|-|
| [`all()`](#all) | None |
| [`iter()`](#iter) | None |


#### all()

```python
def all(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### iter()

```python
def iter(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| column_names |  |  |
| from_path |  |  |

## flytekit.types.schema.SchemaWriter

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
def SchemaWriter(
    to_path: str,
    cols: typing.Optional[typing.Dict[str, type]],
    fmt: SchemaFormat,
):
```
| Parameter | Type |
|-|-|
| `to_path` | `str` |
| `cols` | `typing.Optional[typing.Dict[str, type]]` |
| `fmt` | `SchemaFormat` |

### Methods

| Method | Description |
|-|-|
| [`write()`](#write) | None |


#### write()

```python
def write(
    dfs,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `dfs` |  |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| column_names |  |  |
| to_path |  |  |

