---
title: flytekit.types.file.file
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.types.file.file

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteFile`](.././flytekit.types.file.file#flytekittypesfilefileflytefile) |  |
| [`FlyteFilePathTransformer`](.././flytekit.types.file.file#flytekittypesfilefileflytefilepathtransformer) | Base transformer type that should be implemented for every python native type that can be handled by flytekit. |

### Methods

| Method | Description |
|-|-|
| [`noop()`](#noop) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `MESSAGEPACK` | `str` |  |
| `T` | `TypeVar` |  |

## Methods

#### noop()

```python
def noop()
```
## flytekit.types.file.file.FlyteFile

```python
class FlyteFile(
    path: typing.Union[str, os.PathLike],
    downloader: typing.Callable,
    remote_path: typing.Optional[typing.Union[os.PathLike, str, bool]],
    metadata: typing.Optional[dict[str, str]],
)
```
FlyteFile's init method.



| Parameter | Type |
|-|-|
| `path` | `typing.Union[str, os.PathLike]` |
| `downloader` | `typing.Callable` |
| `remote_path` | `typing.Optional[typing.Union[os.PathLike, str, bool]]` |
| `metadata` | `typing.Optional[dict[str, str]]` |

### Methods

| Method | Description |
|-|-|
| [`deserialize_flyte_file()`](#deserialize_flyte_file) |  |
| [`download()`](#download) |  |
| [`extension()`](#extension) |  |
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`from_source()`](#from_source) | Create a new FlyteFile object with the remote source set to the input. |
| [`new()`](#new) | Create a new FlyteFile object in the current Flyte working directory. |
| [`new_remote_file()`](#new_remote_file) | Create a new FlyteFile object with a remote path. |
| [`open()`](#open) | Returns a streaming File handle. |
| [`serialize_flyte_file()`](#serialize_flyte_file) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


#### deserialize_flyte_file()

```python
def deserialize_flyte_file(
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### download()

```python
def download()
```
#### extension()

```python
def extension()
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

#### from_source()

```python
def from_source(
    source: str | os.PathLike,
) -> FlyteFile
```
Create a new FlyteFile object with the remote source set to the input


| Parameter | Type |
|-|-|
| `source` | `str \| os.PathLike` |

#### new()

```python
def new(
    filename: str | os.PathLike,
) -> FlyteFile
```
Create a new FlyteFile object in the current Flyte working directory


| Parameter | Type |
|-|-|
| `filename` | `str \| os.PathLike` |

#### new_remote_file()

```python
def new_remote_file(
    name: typing.Optional[str],
    alt: typing.Optional[str],
) -> FlyteFile
```
Create a new FlyteFile object with a remote path.



| Parameter | Type |
|-|-|
| `name` | `typing.Optional[str]` |
| `alt` | `typing.Optional[str]` |

#### open()

```python
def open(
    mode: str,
    cache_type: typing.Optional[str],
    cache_options: typing.Optional[typing.Dict[str, typing.Any]],
)
```
Returns a streaming File handle

```python
@task
def copy_file(ff: FlyteFile) -> FlyteFile:
    new_file = FlyteFile.new_remote_file()
    with ff.open("rb", cache_type="readahead") as r:
        with new_file.open("wb") as w:
            w.write(r.read())
    return new_file
```



| Parameter | Type |
|-|-|
| `mode` | `str` |
| `cache_type` | `typing.Optional[str]` |
| `cache_options` | `typing.Optional[typing.Dict[str, typing.Any]]` |

#### serialize_flyte_file()

```python
def serialize_flyte_file(
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
| `downloaded` |  |  |
| `remote_path` |  |  |
| `remote_source` |  | {{< multiline >}}If this is an input to a task, and the original path is an ``s3`` bucket, Flytekit downloads the
file for the user. In case the user wants access to the original path, it will be here.
{{< /multiline >}} |

## flytekit.types.file.file.FlyteFilePathTransformer

Base transformer type that should be implemented for every python native type that can be handled by flytekit


```python
def FlyteFilePathTransformer()
```
### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`async_to_literal()`](#async_to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`async_to_python_value()`](#async_to_python_value) | Converts the given Literal to a Python Type. |
| [`dict_to_flyte_file()`](#dict_to_flyte_file) |  |
| [`from_binary_idl()`](#from_binary_idl) | If the input is from flytekit, the Life Cycle will be as follows:. |
| [`from_generic_idl()`](#from_generic_idl) | If the input is from Flyte Console, the Life Cycle will be as follows:. |
| [`get_additional_headers()`](#get_additional_headers) |  |
| [`get_format()`](#get_format) |  |
| [`get_literal_type()`](#get_literal_type) | Converts the python type to a Flyte LiteralType. |
| [`get_mime_type_from_extension()`](#get_mime_type_from_extension) |  |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type. |
| [`isinstance_generic()`](#isinstance_generic) |  |
| [`to_html()`](#to_html) | Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div. |
| [`to_literal()`](#to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`to_python_value()`](#to_python_value) | Converts the given Literal to a Python Type. |
| [`validate_file_type()`](#validate_file_type) | This method validates the type of the file at source_path against the expected python_type. |


#### assert_type()

```python
def assert_type(
    t: typing.Union[typing.Type[FlyteFile], os.PathLike],
    v: typing.Union[FlyteFile, os.PathLike, str],
)
```
| Parameter | Type |
|-|-|
| `t` | `typing.Union[typing.Type[FlyteFile], os.PathLike]` |
| `v` | `typing.Union[FlyteFile, os.PathLike, str]` |

#### async_to_literal()

```python
def async_to_literal(
    ctx: FlyteContext,
    python_val: typing.Union[FlyteFile, os.PathLike, str],
    python_type: typing.Type[FlyteFile],
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
| `python_val` | `typing.Union[FlyteFile, os.PathLike, str]` |
| `python_type` | `typing.Type[FlyteFile]` |
| `expected` | `LiteralType` |

#### async_to_python_value()

```python
def async_to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: typing.Union[typing.Type[FlyteFile], os.PathLike],
) -> FlyteFile
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `typing.Union[typing.Type[FlyteFile], os.PathLike]` |

#### dict_to_flyte_file()

```python
def dict_to_flyte_file(
    dict_obj: typing.Dict[str, str],
    expected_python_type: typing.Union[typing.Type[FlyteFile], os.PathLike],
) -> FlyteFile
```
| Parameter | Type |
|-|-|
| `dict_obj` | `typing.Dict[str, str]` |
| `expected_python_type` | `typing.Union[typing.Type[FlyteFile], os.PathLike]` |

#### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: Binary,
    expected_python_type: typing.Union[typing.Type[FlyteFile], os.PathLike],
) -> FlyteFile
```
If the input is from flytekit, the Life Cycle will be as follows:

Life Cycle:
binary IDL                 -> resolved binary         -> bytes                   -> expected Python object
(flytekit customized          (propeller processing)     (flytekit binary IDL)      (flytekit customized
serialization)                                                                       deserialization)

Example Code:
    @dataclass
    class DC:
        ff: FlyteFile

    @workflow
    def wf(dc: DC):
        t_ff(dc.ff)

Note:
- The deserialization is the same as put a flyte file in a dataclass, which will deserialize by the mashumaro's API.

Related PR:
- Title: Override Dataclass Serialization/Deserialization Behavior for FlyteTypes via Mashumaro
- Link: https://github.com/flyteorg/flytekit/pull/2554


| Parameter | Type |
|-|-|
| `binary_idl_object` | `Binary` |
| `expected_python_type` | `typing.Union[typing.Type[FlyteFile], os.PathLike]` |

#### from_generic_idl()

```python
def from_generic_idl(
    generic: Struct,
    expected_python_type: typing.Union[typing.Type[FlyteFile], os.PathLike],
) -> FlyteFile
```
If the input is from Flyte Console, the Life Cycle will be as follows:

Life Cycle:
json str            -> protobuf struct         -> resolved protobuf struct   -> expected Python object
(console user input)   (console output)           (propeller)                   (flytekit customized deserialization)

Example Code:
@dataclass
class DC:
    ff: FlyteFile

@workflow
def wf(dc: DC):
    t_ff(dc.ff)

Note:
- The deserialization is the same as put a flyte file in a dataclass, which will deserialize by the mashumaro's API.

Related PR:
- Title: Override Dataclass Serialization/Deserialization Behavior for FlyteTypes via Mashumaro
- Link: https://github.com/flyteorg/flytekit/pull/2554


| Parameter | Type |
|-|-|
| `generic` | `Struct` |
| `expected_python_type` | `typing.Union[typing.Type[FlyteFile], os.PathLike]` |

#### get_additional_headers()

```python
def get_additional_headers(
    source_path: str | os.PathLike,
) -> typing.Dict[str, str]
```
| Parameter | Type |
|-|-|
| `source_path` | `str \| os.PathLike` |

#### get_format()

```python
def get_format(
    t: typing.Union[typing.Type[FlyteFile], os.PathLike],
) -> str
```
| Parameter | Type |
|-|-|
| `t` | `typing.Union[typing.Type[FlyteFile], os.PathLike]` |

#### get_literal_type()

```python
def get_literal_type(
    t: typing.Union[typing.Type[FlyteFile], os.PathLike],
) -> LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type |
|-|-|
| `t` | `typing.Union[typing.Type[FlyteFile], os.PathLike]` |

#### get_mime_type_from_extension()

```python
def get_mime_type_from_extension(
    extension: str,
) -> typing.Union[str, typing.Sequence[str]]
```
| Parameter | Type |
|-|-|
| `extension` | `str` |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> typing.Type[FlyteFile[typing.Any]]
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

#### validate_file_type()

```python
def validate_file_type(
    python_type: typing.Type[FlyteFile],
    source_path: typing.Union[str, os.PathLike],
)
```
This method validates the type of the file at source_path against the expected python_type.
It uses the magic library to determine the real type of the file. If the magic library is not installed,
it logs a debug message and returns. If the actual file does not exist, it returns without raising an error.



| Parameter | Type |
|-|-|
| `python_type` | `typing.Type[FlyteFile]` |
| `source_path` | `typing.Union[str, os.PathLike]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_async` |  |  |
| `name` |  |  |
| `python_type` |  | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` |  | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

