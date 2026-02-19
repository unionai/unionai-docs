---
title: FlyteFile
version: 0.1.201
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# FlyteFile

**Package:** `union`

```python
class FlyteFile(
    path: typing.Union[str, os.PathLike],
    downloader: typing.Callable,
    remote_path: typing.Optional[typing.Union[os.PathLike, str, bool]],
    metadata: typing.Optional[dict[str, str]],
)
```
FlyteFile's init method.



| Parameter | Type | Description |
|-|-|-|
| `path` | `typing.Union[str, os.PathLike]` | The source path that users are expected to call open() on. |
| `downloader` | `typing.Callable` | Optional function that can be passed that used to delay downloading of the actual fil until a user actually calls open(). |
| `remote_path` | `typing.Optional[typing.Union[os.PathLike, str, bool]]` | If the user wants to return something and also specify where it should be uploaded to. Alternatively, if the user wants to specify a remote path for a file that's already in the blob store, the path should point to the location and remote_path should be set to False. |
| `metadata` | `typing.Optional[dict[str, str]]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `downloaded` | `None` |  |
| `remote_path` | `None` |  |
| `remote_source` | `None` | If this is an input to a task, and the original path is an ``s3`` bucket, Flytekit downloads the file for the user. In case the user wants access to the original path, it will be here. |

## Methods

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


### deserialize_flyte_file()

```python
def deserialize_flyte_file(
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

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
    d,
    dialect,
)
```
| Parameter | Type | Description |
|-|-|-|
| `d` |  | |
| `dialect` |  | |

### from_json()

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

### from_source()

```python
def from_source(
    source: str | os.PathLike,
) -> FlyteFile
```
Create a new FlyteFile object with the remote source set to the input


| Parameter | Type | Description |
|-|-|-|
| `source` | `str \| os.PathLike` | |

### new()

```python
def new(
    filename: str | os.PathLike,
) -> FlyteFile
```
Create a new FlyteFile object in the current Flyte working directory


| Parameter | Type | Description |
|-|-|-|
| `filename` | `str \| os.PathLike` | |

### new_remote_file()

```python
def new_remote_file(
    name: typing.Optional[str],
    alt: typing.Optional[str],
) -> FlyteFile
```
Create a new FlyteFile object with a remote path.



| Parameter | Type | Description |
|-|-|-|
| `name` | `typing.Optional[str]` | If you want to specify a different name for the file, you can specify it here. |
| `alt` | `typing.Optional[str]` | If you want to specify a different prefix head than the default one, you can specify it here. |

### open()

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



| Parameter | Type | Description |
|-|-|-|
| `mode` | `str` | Open mode. For example :type mode: str |
| `cache_type` | `typing.Optional[str]` | Specifies the cache type. Possible values are "blockcache", "bytes", "mmap", "readahead", "first", or "background". This is especially useful for large file reads. See https://filesystem-spec.readthedocs.io/en/latest/api.html#readbuffering. :type cache_type: str, optional |
| `cache_options` | `typing.Optional[typing.Dict[str, typing.Any]]` | A Dict corresponding to the parameters for the chosen cache_type. Refer to fsspec caching options above. :type cache_options: Dict[str, Any], optional |

### serialize_flyte_file()

```python
def serialize_flyte_file(
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### to_dict()

```python
def to_dict()
```
### to_json()

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

