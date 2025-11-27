---
title: FlyteDirectory
version: 0.1.198
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# FlyteDirectory

**Package:** `union`

```python
class FlyteDirectory(
    path: typing.Union[str, os.PathLike],
    downloader: typing.Optional[typing.Callable],
    remote_directory: typing.Optional[typing.Union[os.PathLike, str, typing.Literal[False]]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `path` | `typing.Union[str, os.PathLike]` | The source path that users are expected to call open() on |
| `downloader` | `typing.Optional[typing.Callable]` | Optional function that can be passed that used to delay downloading of the actual fil until a user actually calls open(). |
| `remote_directory` | `typing.Optional[typing.Union[os.PathLike, str, typing.Literal[False]]]` | If the user wants to return something and also specify where it should be uploaded to. If set to False, then flytekit will not upload the directory to the remote store. |

## Methods

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


### crawl()

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


| Parameter | Type | Description |
|-|-|-|
| `maxdepth` | `typing.Optional[int]` | |
| `topdown` | `bool` | |
| `kwargs` | `**kwargs` | |

### deserialize_flyte_dir()

```python
def deserialize_flyte_dir(
    info,
) -> FlyteDirectory
```
| Parameter | Type | Description |
|-|-|-|
| `info` |  | |

### download()

```python
def download()
```
### extension()

```python
def extension()
```
### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
) -> ~A
```
| Parameter | Type | Description |
|-|-|-|
| `kvs` | `typing.Union[dict, list, str, int, float, bool, NoneType]` | |
| `infer_missing` |  | |

### from_json()

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
| Parameter | Type | Description |
|-|-|-|
| `s` | `typing.Union[str, bytes, bytearray]` | |
| `parse_float` |  | |
| `parse_int` |  | |
| `parse_constant` |  | |
| `infer_missing` |  | |
| `kw` |  | |

### from_source()

```python
def from_source(
    source: str | os.PathLike,
) -> FlyteDirectory
```
Create a new FlyteDirectory object with the remote source set to the input


| Parameter | Type | Description |
|-|-|-|
| `source` | `str \| os.PathLike` | |

### listdir()

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


| Parameter | Type | Description |
|-|-|-|
| `directory` | `FlyteDirectory` | |

### new()

```python
def new(
    dirname: str | os.PathLike,
) -> FlyteDirectory
```
Create a new FlyteDirectory object in current Flyte working directory.


| Parameter | Type | Description |
|-|-|-|
| `dirname` | `str \| os.PathLike` | |

### new_dir()

```python
def new_dir(
    name: typing.Optional[str],
) -> FlyteDirectory
```
This will create a new folder under the current folder.
If given a name, it will use the name given, otherwise it'll pick a random string.
Collisions are not checked.


| Parameter | Type | Description |
|-|-|-|
| `name` | `typing.Optional[str]` | |

### new_file()

```python
def new_file(
    name: typing.Optional[str],
) -> FlyteFile
```
This will create a new file under the current folder.
If given a name, it will use the name given, otherwise it'll pick a random string.
Collisions are not checked.


| Parameter | Type | Description |
|-|-|-|
| `name` | `typing.Optional[str]` | |

### new_remote()

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



| Parameter | Type | Description |
|-|-|-|
| `stem` | `typing.Optional[str]` | A stem to append to the path as the final prefix "directory". |
| `alt` | `typing.Optional[str]` | An alternate first member of the prefix to use instead of the default. :return FlyteDirectory: A new FlyteDirectory object that points to a remote location. |

### schema()

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
| Parameter | Type | Description |
|-|-|-|
| `infer_missing` | `bool` | |
| `only` |  | |
| `exclude` |  | |
| `many` | `bool` | |
| `context` |  | |
| `load_only` |  | |
| `dump_only` |  | |
| `partial` | `bool` | |
| `unknown` |  | |

### serialize_flyte_dir()

```python
def serialize_flyte_dir()
```
### to_dict()

```python
def to_dict(
    encode_json,
) -> typing.Dict[str, typing.Union[dict, list, str, int, float, bool, NoneType]]
```
| Parameter | Type | Description |
|-|-|-|
| `encode_json` |  | |

### to_json()

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
| Parameter | Type | Description |
|-|-|-|
| `skipkeys` | `bool` | |
| `ensure_ascii` | `bool` | |
| `check_circular` | `bool` | |
| `allow_nan` | `bool` | |
| `indent` | `typing.Union[int, str, NoneType]` | |
| `separators` | `typing.Tuple[str, str]` | |
| `default` | `typing.Callable` | |
| `sort_keys` | `bool` | |
| `kw` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `downloaded` |  |  |
| `remote_directory` |  |  |
| `remote_source` |  | {{< multiline >}}If this is an input to a task, and the original path is s3://something, flytekit will download the
directory for the user. In case the user wants access to the original path, it will be here.
{{< /multiline >}} |
| `sep` |  |  |

