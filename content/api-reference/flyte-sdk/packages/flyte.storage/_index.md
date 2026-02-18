---
title: flyte.storage
version: 2.0.0b59
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
sidebar_expanded: true
---

# flyte.storage

## Directory

### Classes

| Class | Description |
|-|-|
| [`ABFS`](../flyte.storage/abfs) | Any Azure Blob Storage specific configuration. |
| [`GCS`](../flyte.storage/gcs) | Any GCS specific configuration. |
| [`S3`](../flyte.storage/s3) | S3 specific configuration. |
| [`Storage`](../flyte.storage/storage) | Data storage configuration that applies across any provider. |

### Methods

| Method | Description |
|-|-|
| [`exists()`](#exists) | Check if a path exists. |
| [`exists_sync()`](#exists_sync) |  |
| [`get()`](#get) |  |
| [`get_configured_fsspec_kwargs()`](#get_configured_fsspec_kwargs) |  |
| [`get_random_local_directory()`](#get_random_local_directory) | :return: a random directory. |
| [`get_random_local_path()`](#get_random_local_path) | Use file_path_or_file_name, when you want a random directory, but want to preserve the leaf file name. |
| [`get_stream()`](#get_stream) | Get a stream of data from a remote location. |
| [`get_underlying_filesystem()`](#get_underlying_filesystem) |  |
| [`is_remote()`](#is_remote) | Let's find a replacement. |
| [`join()`](#join) | Join multiple paths together. |
| [`open()`](#open) | Asynchronously open a file and return an async context manager. |
| [`put()`](#put) |  |
| [`put_stream()`](#put_stream) | Put a stream of data to a remote location. |


## Methods

#### exists()

```python
def exists(
    path: str,
    kwargs,
) -> bool
```
Check if a path exists.



| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | Path to be checked. |
| `kwargs` | `**kwargs` | Additional arguments to be passed to the underlying filesystem. :return: True if the path exists, False otherwise. |

#### exists_sync()

```python
def exists_sync(
    path: str,
    kwargs,
) -> bool
```
| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |
| `kwargs` | `**kwargs` | |

#### get()

```python
def get(
    from_path: str,
    to_path: Optional[str | pathlib.Path],
    recursive: bool,
    kwargs,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `from_path` | `str` | |
| `to_path` | `Optional[str \| pathlib.Path]` | |
| `recursive` | `bool` | |
| `kwargs` | `**kwargs` | |

#### get_configured_fsspec_kwargs()

```python
def get_configured_fsspec_kwargs(
    protocol: typing.Optional[str],
    anonymous: bool,
) -> typing.Dict[str, typing.Any]
```
| Parameter | Type | Description |
|-|-|-|
| `protocol` | `typing.Optional[str]` | |
| `anonymous` | `bool` | |

#### get_random_local_directory()

```python
def get_random_local_directory()
```
:return: a random directory
:rtype: pathlib.Path


#### get_random_local_path()

```python
def get_random_local_path(
    file_path_or_file_name: pathlib.Path | str | None,
) -> pathlib.Path
```
Use file_path_or_file_name, when you want a random directory, but want to preserve the leaf file name


| Parameter | Type | Description |
|-|-|-|
| `file_path_or_file_name` | `pathlib.Path \| str \| None` | |

#### get_stream()

```python
def get_stream(
    path: str,
    chunk_size,
    kwargs,
) -> AsyncGenerator[bytes, None]
```
Get a stream of data from a remote location.
This is useful for downloading streaming data from a remote location.
Example usage:
```python
import flyte.storage as storage
async for chunk in storage.get_stream(path="s3://my_bucket/my_file.txt"):
    process(chunk)
```



| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | Path to the remote location where the data will be downloaded. |
| `chunk_size` |  | Size of each chunk to be read from the file. :return: An async iterator that yields chunks of bytes. |
| `kwargs` | `**kwargs` | Additional arguments to be passed to the underlying filesystem. |

#### get_underlying_filesystem()

```python
def get_underlying_filesystem(
    protocol: typing.Optional[str],
    anonymous: bool,
    path: typing.Optional[str],
    kwargs,
) -> fsspec.AbstractFileSystem
```
| Parameter | Type | Description |
|-|-|-|
| `protocol` | `typing.Optional[str]` | |
| `anonymous` | `bool` | |
| `path` | `typing.Optional[str]` | |
| `kwargs` | `**kwargs` | |

#### is_remote()

```python
def is_remote(
    path: typing.Union[pathlib.Path | str],
) -> bool
```
Let's find a replacement


| Parameter | Type | Description |
|-|-|-|
| `path` | `typing.Union[pathlib.Path \| str]` | |

#### join()

```python
def join(
    paths: str,
) -> str
```
Join multiple paths together. This is a wrapper around os.path.join.
# TODO replace with proper join with fsspec root etc



| Parameter | Type | Description |
|-|-|-|
| `paths` | `str` | Paths to be joined. |

#### open()

```python
def open(
    path: str,
    mode: str,
    kwargs,
) -> AsyncReadableFile | AsyncWritableFile
```
Asynchronously open a file and return an async context manager.
This function checks if the underlying filesystem supports obstore bypass.
If it does, it uses obstore to open the file. Otherwise, it falls back to
the standard _open function which uses AsyncFileSystem.

It will raise NotImplementedError if neither obstore nor AsyncFileSystem is supported.


| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |
| `mode` | `str` | |
| `kwargs` | `**kwargs` | |

#### put()

```python
def put(
    from_path: str,
    to_path: Optional[str],
    recursive: bool,
    batch_size: Optional[int],
    kwargs,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `from_path` | `str` | |
| `to_path` | `Optional[str]` | |
| `recursive` | `bool` | |
| `batch_size` | `Optional[int]` | |
| `kwargs` | `**kwargs` | |

#### put_stream()

```python
def put_stream(
    data_iterable: typing.AsyncIterable[bytes] | bytes,
    name: str | None,
    to_path: str | None,
    kwargs,
) -> str
```
Put a stream of data to a remote location. This is useful for streaming data to a remote location.
Example usage:
```python
import flyte.storage as storage
storage.put_stream(iter([b'hello']), name="my_file.txt")
OR
storage.put_stream(iter([b'hello']), to_path="s3://my_bucket/my_file.txt")
```



| Parameter | Type | Description |
|-|-|-|
| `data_iterable` | `typing.AsyncIterable[bytes] \| bytes` | Iterable of bytes to be streamed. |
| `name` | `str \| None` | Name of the file to be created. If not provided, a random name will be generated. |
| `to_path` | `str \| None` | Path to the remote location where the data will be stored. |
| `kwargs` | `**kwargs` | Additional arguments to be passed to the underlying filesystem. :rtype: str :return: The path to the remote location where the data was stored. |

