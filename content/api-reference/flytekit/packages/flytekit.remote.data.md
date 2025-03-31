---
title: flytekit.remote.data
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.remote.data

## Directory

### Classes

| Class | Description |
|-|-|
| [`BlobType`](.././flytekit.remote.data#flytekitremotedatablobtype) | This type represents offloaded data and is typically used for things like files. |
| [`FileAccessProvider`](.././flytekit.remote.data#flytekitremotedatafileaccessprovider) | This is the class that is available through the FlyteContext and can be used for persisting data to the remote. |
| [`Literal`](.././flytekit.remote.data#flytekitremotedataliteral) |  |
| [`RichCallback`](.././flytekit.remote.data#flytekitremotedatarichcallback) | Base class and interface for callback mechanism. |

### Methods

| Method | Description |
|-|-|
| [`MessageToJson()`](#messagetojson) | Converts protobuf message to JSON format. |
| [`download_literal()`](#download_literal) | Download a single literal to a file, if it is a blob or structured dataset. |
| [`literal_string_repr()`](#literal_string_repr) | This method is used to convert a literal to a string representation. |
| [`print()`](#print) | Print object(s) supplied via positional arguments. |


## Methods

#### MessageToJson()

```python
def MessageToJson(
    message,
    preserving_proto_field_name,
    indent,
    sort_keys,
    use_integers_for_enums,
    descriptor_pool,
    float_precision,
    ensure_ascii,
    always_print_fields_with_no_presence,
)
```
Converts protobuf message to JSON format.



| Parameter | Type |
|-|-|
| `message` |  |
| `preserving_proto_field_name` |  |
| `indent` |  |
| `sort_keys` |  |
| `use_integers_for_enums` |  |
| `descriptor_pool` |  |
| `float_precision` |  |
| `ensure_ascii` |  |
| `always_print_fields_with_no_presence` |  |

#### download_literal()

```python
def download_literal(
    file_access: flytekit.core.data_persistence.FileAccessProvider,
    var: str,
    data: flytekit.models.literals.Literal,
    download_to: typing.Optional[pathlib._local.Path],
)
```
Download a single literal to a file, if it is a blob or structured dataset.


| Parameter | Type |
|-|-|
| `file_access` | `flytekit.core.data_persistence.FileAccessProvider` |
| `var` | `str` |
| `data` | `flytekit.models.literals.Literal` |
| `download_to` | `typing.Optional[pathlib._local.Path]` |

#### literal_string_repr()

```python
def literal_string_repr(
    lit: flytekit.models.literals.Literal,
) -> typing.Any
```
This method is used to convert a literal to a string representation. This is useful in places, where we need to
use a shortened string representation of a literal, especially a FlyteFile, FlyteDirectory, or StructuredDataset.


| Parameter | Type |
|-|-|
| `lit` | `flytekit.models.literals.Literal` |

#### print()

```python
def print(
    objects: typing.Any,
    sep: str,
    end: str,
    file: typing.Optional[typing.IO[str]],
    flush: bool,
)
```
Print object(s) supplied via positional arguments.
This function has an identical signature to the built-in print.
For more advanced features, see the :class:`~rich.console.Console` class.



| Parameter | Type |
|-|-|
| `objects` | `typing.Any` |
| `sep` | `str` |
| `end` | `str` |
| `file` | `typing.Optional[typing.IO[str]]` |
| `flush` | `bool` |

## flytekit.remote.data.BlobType

This type represents offloaded data and is typically used for things like files.


```python
class BlobType(
    format,
    dimensionality,
)
```
| Parameter | Type |
|-|-|
| `format` |  |
| `dimensionality` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> BlobType
```
| Parameter | Type |
|-|-|
| `proto` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `dimensionality` |  | {{< multiline >}}An integer from BlobType.BlobDimensionality enum
{{< /multiline >}} |
| `format` |  | {{< multiline >}}A string describing the format of the underlying blob data.
{{< /multiline >}} |
| `is_empty` |  |  |

## flytekit.remote.data.FileAccessProvider

This is the class that is available through the FlyteContext and can be used for persisting data to the remote
durable store.


```python
class FileAccessProvider(
    local_sandbox_dir: typing.Union[str, os.PathLike],
    raw_output_prefix: str,
    data_config: typing.Optional[flytekit.configuration.DataConfig],
    execution_metadata: typing.Optional[dict],
)
```
| Parameter | Type |
|-|-|
| `local_sandbox_dir` | `typing.Union[str, os.PathLike]` |
| `raw_output_prefix` | `str` |
| `data_config` | `typing.Optional[flytekit.configuration.DataConfig]` |
| `execution_metadata` | `typing.Optional[dict]` |

### Methods

| Method | Description |
|-|-|
| [`async_get_data()`](#async_get_data) | . |
| [`async_put_data()`](#async_put_data) | The implication here is that we're always going to put data to the remote location, so we . |
| [`async_put_raw_data()`](#async_put_raw_data) | This is a more flexible version of put that accepts a file-like object or a string path. |
| [`download()`](#download) | Downloads from remote to local. |
| [`download_directory()`](#download_directory) | Downloads directory from given remote to local path. |
| [`exists()`](#exists) |  |
| [`generate_new_custom_path()`](#generate_new_custom_path) | Generates a new path with the raw output prefix and a random string appended to it. |
| [`get()`](#get) |  |
| [`get_async_filesystem_for_path()`](#get_async_filesystem_for_path) |  |
| [`get_data()`](#get_data) | . |
| [`get_file_tail()`](#get_file_tail) |  |
| [`get_filesystem()`](#get_filesystem) |  |
| [`get_filesystem_for_path()`](#get_filesystem_for_path) |  |
| [`get_random_local_directory()`](#get_random_local_directory) |  |
| [`get_random_local_path()`](#get_random_local_path) | Use file_path_or_file_name, when you want a random directory, but want to preserve the leaf file name. |
| [`get_random_remote_directory()`](#get_random_remote_directory) |  |
| [`get_random_remote_path()`](#get_random_remote_path) |  |
| [`get_random_string()`](#get_random_string) |  |
| [`is_remote()`](#is_remote) | Deprecated. |
| [`join()`](#join) |  |
| [`put_data()`](#put_data) | The implication here is that we're always going to put data to the remote location, so we . |
| [`put_raw_data()`](#put_raw_data) | This is a more flexible version of put that accepts a file-like object or a string path. |
| [`recursive_paths()`](#recursive_paths) |  |
| [`sep()`](#sep) |  |
| [`strip_file_header()`](#strip_file_header) | Drops file:// if it exists from the file. |
| [`upload()`](#upload) | . |
| [`upload_directory()`](#upload_directory) | . |


#### async_get_data()

```python
def async_get_data(
    remote_path: str,
    local_path: str,
    is_multipart: bool,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `remote_path` | `str` |
| `local_path` | `str` |
| `is_multipart` | `bool` |
| `kwargs` | ``**kwargs`` |

#### async_put_data()

```python
def async_put_data(
    local_path: typing.Union[str, os.PathLike],
    remote_path: str,
    is_multipart: bool,
    kwargs,
) -> str
```
The implication here is that we're always going to put data to the remote location, so we .remote to ensure
we don't use the true local proxy if the remote path is a file://



| Parameter | Type |
|-|-|
| `local_path` | `typing.Union[str, os.PathLike]` |
| `remote_path` | `str` |
| `is_multipart` | `bool` |
| `kwargs` | ``**kwargs`` |

#### async_put_raw_data()

```python
def async_put_raw_data(
    lpath: typing.Union[str, os.PathLike, pathlib._local.Path, bytes, _io.BufferedReader, _io.BytesIO, _io.StringIO],
    upload_prefix: typing.Optional[str],
    file_name: typing.Optional[str],
    read_chunk_size_bytes: int,
    encoding: str,
    skip_raw_data_prefix: bool,
    kwargs,
) -> str
```
This is a more flexible version of put that accepts a file-like object or a string path.
Writes to the raw output prefix only. If you want to write to another fs use put_data or get the fsspec
file system directly.
FYI: Currently the raw output prefix set by propeller is already unique per retry and looks like
s3://my-s3-bucket/data/o4/feda4e266c748463a97d-n0-0

If lpath is a folder, then recursive will be set.
If lpath is a streamable, then it can only be a single file.

Writes to:
{raw output prefix}/{upload_prefix}/{file_name}



| Parameter | Type |
|-|-|
| `lpath` | `typing.Union[str, os.PathLike, pathlib._local.Path, bytes, _io.BufferedReader, _io.BytesIO, _io.StringIO]` |
| `upload_prefix` | `typing.Optional[str]` |
| `file_name` | `typing.Optional[str]` |
| `read_chunk_size_bytes` | `int` |
| `encoding` | `str` |
| `skip_raw_data_prefix` | `bool` |
| `kwargs` | ``**kwargs`` |

#### download()

```python
def download(
    remote_path: str,
    local_path: str,
    kwargs,
)
```
Downloads from remote to local


| Parameter | Type |
|-|-|
| `remote_path` | `str` |
| `local_path` | `str` |
| `kwargs` | ``**kwargs`` |

#### download_directory()

```python
def download_directory(
    remote_path: str,
    local_path: str,
    kwargs,
)
```
Downloads directory from given remote to local path


| Parameter | Type |
|-|-|
| `remote_path` | `str` |
| `local_path` | `str` |
| `kwargs` | ``**kwargs`` |

#### exists()

```python
def exists(
    path: str,
) -> bool
```
| Parameter | Type |
|-|-|
| `path` | `str` |

#### generate_new_custom_path()

```python
def generate_new_custom_path(
    fs: typing.Optional[fsspec.spec.AbstractFileSystem],
    alt: typing.Optional[str],
    stem: typing.Optional[str],
) -> str
```
Generates a new path with the raw output prefix and a random string appended to it.
Optionally, you can provide an alternate prefix and a stem. If stem is provided, it
will be appended to the path instead of a random string. If alt is provided, it will
replace the first part of the output prefix, e.g. the S3 or GCS bucket.

If wanting to write to a non-random prefix in a non-default S3 bucket, this can be
called with alt="my-alt-bucket" and stem="my-stem" to generate a path like
s3://my-alt-bucket/default-prefix-part/my-stem



| Parameter | Type |
|-|-|
| `fs` | `typing.Optional[fsspec.spec.AbstractFileSystem]` |
| `alt` | `typing.Optional[str]` |
| `stem` | `typing.Optional[str]` |

#### get()

```python
def get(
    from_path: str,
    to_path: str,
    recursive: bool,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `from_path` | `str` |
| `to_path` | `str` |
| `recursive` | `bool` |
| `kwargs` | ``**kwargs`` |

#### get_async_filesystem_for_path()

```python
def get_async_filesystem_for_path(
    path: str,
    anonymous: bool,
    kwargs,
) -> typing.Union[fsspec.asyn.AsyncFileSystem, fsspec.spec.AbstractFileSystem]
```
| Parameter | Type |
|-|-|
| `path` | `str` |
| `anonymous` | `bool` |
| `kwargs` | ``**kwargs`` |

#### get_data()

```python
def get_data(
    remote_path: str,
    local_path: str,
    is_multipart: bool,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `remote_path` | `str` |
| `local_path` | `str` |
| `is_multipart` | `bool` |
| `kwargs` | ``**kwargs`` |

#### get_file_tail()

```python
def get_file_tail(
    file_path_or_file_name: str,
) -> str
```
| Parameter | Type |
|-|-|
| `file_path_or_file_name` | `str` |

#### get_filesystem()

```python
def get_filesystem(
    protocol: typing.Optional[str],
    anonymous: bool,
    path: typing.Optional[str],
    kwargs,
) -> fsspec.spec.AbstractFileSystem
```
| Parameter | Type |
|-|-|
| `protocol` | `typing.Optional[str]` |
| `anonymous` | `bool` |
| `path` | `typing.Optional[str]` |
| `kwargs` | ``**kwargs`` |

#### get_filesystem_for_path()

```python
def get_filesystem_for_path(
    path: str,
    anonymous: bool,
    kwargs,
) -> fsspec.spec.AbstractFileSystem
```
| Parameter | Type |
|-|-|
| `path` | `str` |
| `anonymous` | `bool` |
| `kwargs` | ``**kwargs`` |

#### get_random_local_directory()

```python
def get_random_local_directory()
```
#### get_random_local_path()

```python
def get_random_local_path(
    file_path_or_file_name: typing.Optional[str],
) -> str
```
Use file_path_or_file_name, when you want a random directory, but want to preserve the leaf file name


| Parameter | Type |
|-|-|
| `file_path_or_file_name` | `typing.Optional[str]` |

#### get_random_remote_directory()

```python
def get_random_remote_directory()
```
#### get_random_remote_path()

```python
def get_random_remote_path(
    file_path_or_file_name: typing.Optional[str],
) -> str
```
| Parameter | Type |
|-|-|
| `file_path_or_file_name` | `typing.Optional[str]` |

#### get_random_string()

```python
def get_random_string()
```
#### is_remote()

```python
def is_remote(
    path: typing.Union[str, os.PathLike],
) -> bool
```
Deprecated. Let's find a replacement


| Parameter | Type |
|-|-|
| `path` | `typing.Union[str, os.PathLike]` |

#### join()

```python
def join(
    args: `*args`,
    unstrip: bool,
    fs: typing.Optional[fsspec.spec.AbstractFileSystem],
) -> str
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `unstrip` | `bool` |
| `fs` | `typing.Optional[fsspec.spec.AbstractFileSystem]` |

#### put_data()

```python
def put_data(
    local_path: typing.Union[str, os.PathLike],
    remote_path: str,
    is_multipart: bool,
    kwargs,
) -> str
```
The implication here is that we're always going to put data to the remote location, so we .remote to ensure
we don't use the true local proxy if the remote path is a file://



| Parameter | Type |
|-|-|
| `local_path` | `typing.Union[str, os.PathLike]` |
| `remote_path` | `str` |
| `is_multipart` | `bool` |
| `kwargs` | ``**kwargs`` |

#### put_raw_data()

```python
def put_raw_data(
    lpath: typing.Union[str, os.PathLike, pathlib._local.Path, bytes, _io.BufferedReader, _io.BytesIO, _io.StringIO],
    upload_prefix: typing.Optional[str],
    file_name: typing.Optional[str],
    read_chunk_size_bytes: int,
    encoding: str,
    skip_raw_data_prefix: bool,
    kwargs,
) -> str
```
This is a more flexible version of put that accepts a file-like object or a string path.
Writes to the raw output prefix only. If you want to write to another fs use put_data or get the fsspec
file system directly.
FYI: Currently the raw output prefix set by propeller is already unique per retry and looks like
s3://my-s3-bucket/data/o4/feda4e266c748463a97d-n0-0

If lpath is a folder, then recursive will be set.
If lpath is a streamable, then it can only be a single file.

Writes to:
{raw output prefix}/{upload_prefix}/{file_name}



| Parameter | Type |
|-|-|
| `lpath` | `typing.Union[str, os.PathLike, pathlib._local.Path, bytes, _io.BufferedReader, _io.BytesIO, _io.StringIO]` |
| `upload_prefix` | `typing.Optional[str]` |
| `file_name` | `typing.Optional[str]` |
| `read_chunk_size_bytes` | `int` |
| `encoding` | `str` |
| `skip_raw_data_prefix` | `bool` |
| `kwargs` | ``**kwargs`` |

#### recursive_paths()

```python
def recursive_paths(
    f: str,
    t: str,
) -> typing.Tuple[str, str]
```
| Parameter | Type |
|-|-|
| `f` | `str` |
| `t` | `str` |

#### sep()

```python
def sep(
    file_system: typing.Optional[fsspec.spec.AbstractFileSystem],
) -> str
```
| Parameter | Type |
|-|-|
| `file_system` | `typing.Optional[fsspec.spec.AbstractFileSystem]` |

#### strip_file_header()

```python
def strip_file_header(
    path: str,
    trim_trailing_sep: bool,
) -> str
```
Drops file:// if it exists from the file


| Parameter | Type |
|-|-|
| `path` | `str` |
| `trim_trailing_sep` | `bool` |

#### upload()

```python
def upload(
    file_path: str,
    to_path: str,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `file_path` | `str` |
| `to_path` | `str` |
| `kwargs` | ``**kwargs`` |

#### upload_directory()

```python
def upload_directory(
    local_path: str,
    remote_path: str,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `local_path` | `str` |
| `remote_path` | `str` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `data_config` |  |  |
| `local_access` |  |  |
| `local_sandbox_dir` |  | {{< multiline >}}This is a context based temp dir.
{{< /multiline >}} |
| `raw_output_fs` |  | {{< multiline >}}Returns a file system corresponding to the provided raw output prefix
{{< /multiline >}} |
| `raw_output_prefix` |  |  |

## flytekit.remote.data.Literal

```python
class Literal(
    scalar: typing.Optional[flytekit.models.literals.Scalar],
    collection: typing.Optional[flytekit.models.literals.LiteralCollection],
    map: typing.Optional[flytekit.models.literals.LiteralMap],
    hash: typing.Optional[str],
    metadata: typing.Optional[typing.Dict[str, str]],
    offloaded_metadata: typing.Optional[flytekit.models.literals.LiteralOffloadedMetadata],
)
```
This IDL message represents a literal value in the Flyte ecosystem.



| Parameter | Type |
|-|-|
| `scalar` | `typing.Optional[flytekit.models.literals.Scalar]` |
| `collection` | `typing.Optional[flytekit.models.literals.LiteralCollection]` |
| `map` | `typing.Optional[flytekit.models.literals.LiteralMap]` |
| `hash` | `typing.Optional[str]` |
| `metadata` | `typing.Optional[typing.Dict[str, str]]` |
| `offloaded_metadata` | `typing.Optional[flytekit.models.literals.LiteralOffloadedMetadata]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`set_metadata()`](#set_metadata) | Note: This is a mutation on the literal. |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.literals_pb2.Literal,
) -> Literal
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.literals_pb2.Literal` |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### set_metadata()

```python
def set_metadata(
    metadata: typing.Dict[str, str],
)
```
Note: This is a mutation on the literal


| Parameter | Type |
|-|-|
| `metadata` | `typing.Dict[str, str]` |

#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `collection` |  | {{< multiline >}}If not None, this value holds a collection of Literal values which can be further unpacked.
{{< /multiline >}} |
| `hash` |  | {{< multiline >}}If not None, this value holds a hash that represents the literal for caching purposes.
{{< /multiline >}} |
| `is_empty` |  |  |
| `map` |  | {{< multiline >}}If not None, this value holds a map of Literal values which can be further unpacked.
{{< /multiline >}} |
| `metadata` |  | {{< multiline >}}This value holds metadata about the literal.
{{< /multiline >}} |
| `offloaded_metadata` |  | {{< multiline >}}This value holds metadata about the offloaded literal.
{{< /multiline >}} |
| `scalar` |  | {{< multiline >}}If not None, this value holds a scalar value which can be further unpacked.
{{< /multiline >}} |
| `value` |  | {{< multiline >}}Returns one of the scalar, collection, or map properties based on which one is set.
{{< /multiline >}} |

## flytekit.remote.data.RichCallback

Base class and interface for callback mechanism

This class can be used directly for monitoring file transfers by
providing ``callback=Callback(hooks=...)`` (see the ``hooks`` argument,
below), or subclassed for more specialised behaviour.

Parameters
----------
size: int (optional)
Nominal quantity for the value that corresponds to a complete
transfer, e.g., total number of tiles or total number of
bytes
value: int (0)
Starting internal counter value
hooks: dict or None
A dict of named functions to be called on each update. The signature
of these must be ``f(size, value, **kwargs)``


```python
class RichCallback(
    rich_kwargs: typing.Optional[typing.Dict],
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `rich_kwargs` | `typing.Optional[typing.Dict]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`absolute_update()`](#absolute_update) | Set the internal value state. |
| [`as_callback()`](#as_callback) | Transform callback=. |
| [`branch()`](#branch) | Set callbacks for child transfers. |
| [`branch_coro()`](#branch_coro) | Wraps a coroutine, and pass a new child callback to it. |
| [`branched()`](#branched) | Return callback for child transfers. |
| [`call()`](#call) | Execute hook(s) with current state. |
| [`close()`](#close) | Close callback. |
| [`no_op()`](#no_op) |  |
| [`relative_update()`](#relative_update) | Delta increment the internal counter. |
| [`set_size()`](#set_size) | Set the internal maximum size attribute. |
| [`wrap()`](#wrap) | Wrap an iterable to call ``relative_update`` on each iterations. |


#### absolute_update()

```python
def absolute_update(
    value,
)
```
Set the internal value state

Triggers ``call()``

Parameters
----------
value: int


| Parameter | Type |
|-|-|
| `value` |  |

#### as_callback()

```python
def as_callback(
    maybe_callback,
)
```
Transform callback=... into Callback instance

For the special value of ``None``, return the global instance of
``NoOpCallback``. This is an alternative to including
``callback=DEFAULT_CALLBACK`` directly in a method signature.


| Parameter | Type |
|-|-|
| `maybe_callback` |  |

#### branch()

```python
def branch(
    path_1,
    path_2,
    kwargs,
)
```
Set callbacks for child transfers

If this callback is operating at a higher level, e.g., put, which may
trigger transfers that can also be monitored. The passed kwargs are
to be *mutated* to add ``callback=``, if this class supports branching
to children.

Parameters
----------
path_1: str
Child's source path
path_2: str
Child's destination path
kwargs: dict
arguments passed to child method, e.g., put_file.

Returns
-------


| Parameter | Type |
|-|-|
| `path_1` |  |
| `path_2` |  |
| `kwargs` | ``**kwargs`` |

#### branch_coro()

```python
def branch_coro(
    fn,
)
```
Wraps a coroutine, and pass a new child callback to it.


| Parameter | Type |
|-|-|
| `fn` |  |

#### branched()

```python
def branched(
    path_1,
    path_2,
    kwargs,
)
```
Return callback for child transfers

If this callback is operating at a higher level, e.g., put, which may
trigger transfers that can also be monitored. The function returns a callback
that has to be passed to the child method, e.g., put_file,
as `callback=` argument.

The implementation uses `callback.branch` for compatibility.
When implementing callbacks, it is recommended to override this function instead
of `branch` and avoid calling `super().branched(...)`.

Prefer using this function over `branch`.

Parameters
----------
path_1: str
Child's source path
path_2: str
Child's destination path
**kwargs:
Arbitrary keyword arguments

Returns
-------
callback: Callback
A callback instance to be passed to the child method


| Parameter | Type |
|-|-|
| `path_1` |  |
| `path_2` |  |
| `kwargs` | ``**kwargs`` |

#### call()

```python
def call(
    hook_name,
    kwargs,
)
```
Execute hook(s) with current state

Each function is passed the internal size and current value

Parameters
----------
hook_name: str or None
If given, execute on this hook
kwargs: passed on to (all) hook(s)


| Parameter | Type |
|-|-|
| `hook_name` |  |
| `kwargs` | ``**kwargs`` |

#### close()

```python
def close()
```
Close callback.


#### no_op()

```python
def no_op(
    _,
    __,
)
```
| Parameter | Type |
|-|-|
| `_` |  |
| `__` |  |

#### relative_update()

```python
def relative_update(
    inc,
)
```
Delta increment the internal counter

Triggers ``call()``

Parameters
----------
inc: int


| Parameter | Type |
|-|-|
| `inc` |  |

#### set_size()

```python
def set_size(
    size,
)
```
Set the internal maximum size attribute

Usually called if not initially set at instantiation. Note that this
triggers a ``call()``.

Parameters
----------
size: int


| Parameter | Type |
|-|-|
| `size` |  |

#### wrap()

```python
def wrap(
    iterable,
)
```
Wrap an iterable to call ``relative_update`` on each iterations

Parameters
----------
iterable: Iterable
The iterable that is being wrapped


| Parameter | Type |
|-|-|
| `iterable` |  |

