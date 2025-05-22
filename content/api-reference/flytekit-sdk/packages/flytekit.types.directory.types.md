---
title: flytekit.types.directory.types
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.types.directory.types

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteDirToMultipartBlobTransformer`](.././flytekit.types.directory.types#flytekittypesdirectorytypesflytedirtomultipartblobtransformer) | This transformer handles conversion between the Python native FlyteDirectory class defined above, and the Flyte. |
| [`FlyteDirectory`](.././flytekit.types.directory.types#flytekittypesdirectorytypesflytedirectory) |  |

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
## flytekit.types.directory.types.FlyteDirToMultipartBlobTransformer

This transformer handles conversion between the Python native FlyteDirectory class defined above, and the Flyte
IDL literal/type of Multipart Blob. Please see the FlyteDirectory comments for additional information.

> [!CAUTION] caution:
> The transformer will not check if the given path is actually a directory. This is because the path could be
   a remote reference.


```python
def FlyteDirToMultipartBlobTransformer()
```
### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`async_to_literal()`](#async_to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`async_to_python_value()`](#async_to_python_value) | Converts the given Literal to a Python Type. |
| [`dict_to_flyte_directory()`](#dict_to_flyte_directory) |  |
| [`from_binary_idl()`](#from_binary_idl) | If the input is from flytekit, the Life Cycle will be as follows:. |
| [`from_generic_idl()`](#from_generic_idl) | If the input is from Flyte Console, the Life Cycle will be as follows:. |
| [`get_format()`](#get_format) |  |
| [`get_literal_type()`](#get_literal_type) | Converts the python type to a Flyte LiteralType. |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type. |
| [`isinstance_generic()`](#isinstance_generic) |  |
| [`to_html()`](#to_html) | Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div. |
| [`to_literal()`](#to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`to_python_value()`](#to_python_value) | Converts the given Literal to a Python Type. |


#### assert_type()

```python
def assert_type(
    t: typing.Type[FlyteDirectory],
    v: typing.Union[FlyteDirectory, os.PathLike, str],
)
```
| Parameter | Type |
|-|-|
| `t` | `typing.Type[FlyteDirectory]` |
| `v` | `typing.Union[FlyteDirectory, os.PathLike, str]` |

#### async_to_literal()

```python
def async_to_literal(
    ctx: FlyteContext,
    python_val: FlyteDirectory,
    python_type: typing.Type[FlyteDirectory],
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
| `python_val` | `FlyteDirectory` |
| `python_type` | `typing.Type[FlyteDirectory]` |
| `expected` | `LiteralType` |

#### async_to_python_value()

```python
def async_to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: typing.Type[FlyteDirectory],
) -> FlyteDirectory
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `typing.Type[FlyteDirectory]` |

#### dict_to_flyte_directory()

```python
def dict_to_flyte_directory(
    dict_obj: typing.Dict[str, str],
    expected_python_type: typing.Type[FlyteDirectory],
) -> FlyteDirectory
```
| Parameter | Type |
|-|-|
| `dict_obj` | `typing.Dict[str, str]` |
| `expected_python_type` | `typing.Type[FlyteDirectory]` |

#### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: Binary,
    expected_python_type: typing.Type[FlyteDirectory],
) -> FlyteDirectory
```
If the input is from flytekit, the Life Cycle will be as follows:

Life Cycle:
binary IDL                 -> resolved binary         -> bytes                   -> expected Python object
(flytekit customized          (propeller processing)     (flytekit binary IDL)      (flytekit customized
serialization)                                                                       deserialization)

Example Code:
@dataclass
class DC:
    fd: FlyteDirectory

@workflow
def wf(dc: DC):
    t_fd(dc.fd)

Note:
- The deserialization is the same as put a flyte directory in a dataclass, which will deserialize by the mashumaro's API.

Related PR:
- Title: Override Dataclass Serialization/Deserialization Behavior for FlyteTypes via Mashumaro
- Link: https://github.com/flyteorg/flytekit/pull/2554


| Parameter | Type |
|-|-|
| `binary_idl_object` | `Binary` |
| `expected_python_type` | `typing.Type[FlyteDirectory]` |

#### from_generic_idl()

```python
def from_generic_idl(
    generic: Struct,
    expected_python_type: typing.Type[FlyteDirectory],
) -> FlyteDirectory
```
If the input is from Flyte Console, the Life Cycle will be as follows:

Life Cycle:
json str            -> protobuf struct         -> resolved protobuf struct   -> expected Python object
(console user input)   (console output)           (propeller)                   (flytekit customized deserialization)

Example Code:
@dataclass
class DC:
    fd: FlyteDirectory

@workflow
def wf(dc: DC):
    t_fd(dc.fd)

Note:
- The deserialization is the same as put a flyte directory in a dataclass, which will deserialize by the mashumaro's API.

Related PR:
- Title: Override Dataclass Serialization/Deserialization Behavior for FlyteTypes via Mashumaro
- Link: https://github.com/flyteorg/flytekit/pull/2554


| Parameter | Type |
|-|-|
| `generic` | `Struct` |
| `expected_python_type` | `typing.Type[FlyteDirectory]` |

#### get_format()

```python
def get_format(
    t: typing.Type[FlyteDirectory],
) -> str
```
| Parameter | Type |
|-|-|
| `t` | `typing.Type[FlyteDirectory]` |

#### get_literal_type()

```python
def get_literal_type(
    t: typing.Type[FlyteDirectory],
) -> LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type |
|-|-|
| `t` | `typing.Type[FlyteDirectory]` |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> typing.Type[FlyteDirectory[typing.Any]]
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

## flytekit.types.directory.types.FlyteDirectory

```python
class FlyteDirectory(
    path: typing.Union[str, os.PathLike],
    downloader: typing.Optional[typing.Callable],
    remote_directory: typing.Optional[typing.Union[os.PathLike, str, typing.Literal[False]]],
)
```
| Parameter | Type |
|-|-|
| `path` | `typing.Union[str, os.PathLike]` |
| `downloader` | `typing.Optional[typing.Callable]` |
| `remote_directory` | `typing.Optional[typing.Union[os.PathLike, str, typing.Literal[False]]]` |

### Methods

| Method | Description |
|-|-|
| [`crawl()`](#crawl) | Crawl returns a generator of all files prefixed by any sub-folders under the given "FlyteDirectory". |
| [`deserialize_flyte_dir()`](#deserialize_flyte_dir) |  |
| [`download()`](#download) |  |
| [`extension()`](#extension) |  |
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`from_source()`](#from_source) | Create a new FlyteDirectory object with the remote source set to the input. |
| [`listdir()`](#listdir) | This function will list all files and folders in the given directory, but without downloading the contents. |
| [`new()`](#new) | Create a new FlyteDirectory object in current Flyte working directory. |
| [`new_dir()`](#new_dir) | This will create a new folder under the current folder. |
| [`new_file()`](#new_file) | This will create a new file under the current folder. |
| [`new_remote()`](#new_remote) | Create a new FlyteDirectory object using the currently configured default remote in the context (i. |
| [`schema()`](#schema) |  |
| [`serialize_flyte_dir()`](#serialize_flyte_dir) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


#### crawl()

```python
def crawl(
    maxdepth: typing.Optional[int],
    topdown: bool,
    kwargs,
) -> Generator[Tuple[typing.Union[str, os.PathLike[Any]], typing.Dict[Any, Any]], None, None]
```
Crawl returns a generator of all files prefixed by any sub-folders under the given "FlyteDirectory".
if details=True is passed, then it will return a dictionary as specified by fsspec.

Example:

    >>> list(fd.crawl())
    [("/base", "file1"), ("/base", "dir1/file1"), ("/base", "dir2/file1"), ("/base", "dir1/dir/file1")]

    >>> list(x.crawl(detail=True))
    [('/tmp/test', {'my-dir/ab.py': {'name': '/tmp/test/my-dir/ab.py', 'size': 0, 'type': 'file',
     'created': 1677720780.2318847, 'islink': False, 'mode': 33188, 'uid': 501, 'gid': 0,
      'mtime': 1677720780.2317934, 'ino': 1694329, 'nlink': 1}})]


| Parameter | Type |
|-|-|
| `maxdepth` | `typing.Optional[int]` |
| `topdown` | `bool` |
| `kwargs` | ``**kwargs`` |

#### deserialize_flyte_dir()

```python
def deserialize_flyte_dir(
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
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
) -> ~A
```
| Parameter | Type |
|-|-|
| `kvs` | `typing.Union[dict, list, str, int, float, bool, NoneType]` |
| `infer_missing` |  |

#### from_json()

```python
def from_json(
    s: typing.Union[str, bytes, bytearray],
    parse_float,
    parse_int,
    parse_constant,
    infer_missing,
    kw,
) -> ~A
```
| Parameter | Type |
|-|-|
| `s` | `typing.Union[str, bytes, bytearray]` |
| `parse_float` |  |
| `parse_int` |  |
| `parse_constant` |  |
| `infer_missing` |  |
| `kw` |  |

#### from_source()

```python
def from_source(
    source: str | os.PathLike,
) -> FlyteDirectory
```
Create a new FlyteDirectory object with the remote source set to the input


| Parameter | Type |
|-|-|
| `source` | `str \| os.PathLike` |

#### listdir()

```python
def listdir(
    directory: FlyteDirectory,
) -> typing.List[typing.Union[FlyteDirectory, FlyteFile]]
```
This function will list all files and folders in the given directory, but without downloading the contents.
In addition, it will return a list of FlyteFile and FlyteDirectory objects that have ability to lazily download the
contents of the file/folder. For example:

```python
entity = FlyteDirectory.listdir(directory)
for e in entity:
    print("s3 object:", e.remote_source)
    # s3 object: s3://test-flytedir/file1.txt
    # s3 object: s3://test-flytedir/file2.txt
    # s3 object: s3://test-flytedir/sub_dir

open(entity[0], "r")  # This will download the file to the local disk.
open(entity[0], "r")  # flytekit will read data from the local disk if you open it again.
```


| Parameter | Type |
|-|-|
| `directory` | `FlyteDirectory` |

#### new()

```python
def new(
    dirname: str | os.PathLike,
) -> FlyteDirectory
```
Create a new FlyteDirectory object in current Flyte working directory.


| Parameter | Type |
|-|-|
| `dirname` | `str \| os.PathLike` |

#### new_dir()

```python
def new_dir(
    name: typing.Optional[str],
) -> FlyteDirectory
```
This will create a new folder under the current folder.
If given a name, it will use the name given, otherwise it'll pick a random string.
Collisions are not checked.


| Parameter | Type |
|-|-|
| `name` | `typing.Optional[str]` |

#### new_file()

```python
def new_file(
    name: typing.Optional[str],
) -> FlyteFile
```
This will create a new file under the current folder.
If given a name, it will use the name given, otherwise it'll pick a random string.
Collisions are not checked.


| Parameter | Type |
|-|-|
| `name` | `typing.Optional[str]` |

#### new_remote()

```python
def new_remote(
    stem: typing.Optional[str],
    alt: typing.Optional[str],
) -> FlyteDirectory
```
Create a new FlyteDirectory object using the currently configured default remote in the context (i.e.
the raw_output_prefix configured in the current FileAccessProvider object in the context).
This is used if you explicitly have a folder somewhere that you want to create files under.
If you want to write a whole folder, you can let your task return a FlyteDirectory object,
and let flytekit handle the uploading.



| Parameter | Type |
|-|-|
| `stem` | `typing.Optional[str]` |
| `alt` | `typing.Optional[str]` |

#### schema()

```python
def schema(
    infer_missing: bool,
    only,
    exclude,
    many: bool,
    context,
    load_only,
    dump_only,
    partial: bool,
    unknown,
) -> SchemaType[A]
```
| Parameter | Type |
|-|-|
| `infer_missing` | `bool` |
| `only` |  |
| `exclude` |  |
| `many` | `bool` |
| `context` |  |
| `load_only` |  |
| `dump_only` |  |
| `partial` | `bool` |
| `unknown` |  |

#### serialize_flyte_dir()

```python
def serialize_flyte_dir(
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
def to_dict(
    encode_json,
) -> typing.Dict[str, typing.Union[dict, list, str, int, float, bool, NoneType]]
```
| Parameter | Type |
|-|-|
| `encode_json` |  |

#### to_json()

```python
def to_json(
    skipkeys: bool,
    ensure_ascii: bool,
    check_circular: bool,
    allow_nan: bool,
    indent: typing.Union[int, str, NoneType],
    separators: typing.Tuple[str, str],
    default: typing.Callable,
    sort_keys: bool,
    kw,
) -> str
```
| Parameter | Type |
|-|-|
| `skipkeys` | `bool` |
| `ensure_ascii` | `bool` |
| `check_circular` | `bool` |
| `allow_nan` | `bool` |
| `indent` | `typing.Union[int, str, NoneType]` |
| `separators` | `typing.Tuple[str, str]` |
| `default` | `typing.Callable` |
| `sort_keys` | `bool` |
| `kw` |  |

### Properties

| Property | Type | Description |
|-|-|-|
| `downloaded` |  |  |
| `remote_directory` |  |  |
| `remote_source` |  | {{< multiline >}}If this is an input to a task, and the original path is s3://something, flytekit will download the
directory for the user. In case the user wants access to the original path, it will be here.
{{< /multiline >}} |
| `sep` |  |  |

