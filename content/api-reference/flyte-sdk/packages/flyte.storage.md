---
title: flyte.storage
version: 2.0.0b26
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flyte.storage

## Directory

### Classes

| Class | Description |
|-|-|
| [`ABFS`](.././flyte.storage#flytestorageabfs) | Any Azure Blob Storage specific configuration. |
| [`GCS`](.././flyte.storage#flytestoragegcs) | Any GCS specific configuration. |
| [`S3`](.././flyte.storage#flytestorages3) | S3 specific configuration. |
| [`Storage`](.././flyte.storage#flytestoragestorage) | Data storage configuration that applies across any provider. |

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



| Parameter | Type |
|-|-|
| `path` | `str` |
| `kwargs` | `**kwargs` |

#### exists_sync()

```python
def exists_sync(
    path: str,
    kwargs,
) -> bool
```
| Parameter | Type |
|-|-|
| `path` | `str` |
| `kwargs` | `**kwargs` |

#### get()

```python
def get(
    from_path: str,
    to_path: Optional[str | pathlib.Path],
    recursive: bool,
    kwargs,
) -> str
```
| Parameter | Type |
|-|-|
| `from_path` | `str` |
| `to_path` | `Optional[str \| pathlib.Path]` |
| `recursive` | `bool` |
| `kwargs` | `**kwargs` |

#### get_configured_fsspec_kwargs()

```python
def get_configured_fsspec_kwargs(
    protocol: typing.Optional[str],
    anonymous: bool,
) -> typing.Dict[str, typing.Any]
```
| Parameter | Type |
|-|-|
| `protocol` | `typing.Optional[str]` |
| `anonymous` | `bool` |

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


| Parameter | Type |
|-|-|
| `file_path_or_file_name` | `pathlib.Path \| str \| None` |

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



| Parameter | Type |
|-|-|
| `path` | `str` |
| `chunk_size` |  |
| `kwargs` | `**kwargs` |

#### get_underlying_filesystem()

```python
def get_underlying_filesystem(
    protocol: typing.Optional[str],
    anonymous: bool,
    path: typing.Optional[str],
    kwargs,
) -> fsspec.AbstractFileSystem
```
| Parameter | Type |
|-|-|
| `protocol` | `typing.Optional[str]` |
| `anonymous` | `bool` |
| `path` | `typing.Optional[str]` |
| `kwargs` | `**kwargs` |

#### is_remote()

```python
def is_remote(
    path: typing.Union[pathlib.Path | str],
) -> bool
```
Let's find a replacement


| Parameter | Type |
|-|-|
| `path` | `typing.Union[pathlib.Path \| str]` |

#### join()

```python
def join(
    paths: str,
) -> str
```
Join multiple paths together. This is a wrapper around os.path.join.
# TODO replace with proper join with fsspec root etc



| Parameter | Type |
|-|-|
| `paths` | `str` |

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


| Parameter | Type |
|-|-|
| `path` | `str` |
| `mode` | `str` |
| `kwargs` | `**kwargs` |

#### put()

```python
def put(
    from_path: str,
    to_path: Optional[str],
    recursive: bool,
    kwargs,
) -> str
```
| Parameter | Type |
|-|-|
| `from_path` | `str` |
| `to_path` | `Optional[str]` |
| `recursive` | `bool` |
| `kwargs` | `**kwargs` |

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



| Parameter | Type |
|-|-|
| `data_iterable` | `typing.AsyncIterable[bytes] \| bytes` |
| `name` | `str \| None` |
| `to_path` | `str \| None` |
| `kwargs` | `**kwargs` |

## flyte.storage.ABFS

Any Azure Blob Storage specific configuration.


```python
class ABFS(
    retries: int,
    backoff: datetime.timedelta,
    enable_debug: bool,
    attach_execution_metadata: bool,
    account_name: typing.Optional[str],
    account_key: typing.Optional[str],
    tenant_id: typing.Optional[str],
    client_id: typing.Optional[str],
    client_secret: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `retries` | `int` |
| `backoff` | `datetime.timedelta` |
| `enable_debug` | `bool` |
| `attach_execution_metadata` | `bool` |
| `account_name` | `typing.Optional[str]` |
| `account_key` | `typing.Optional[str]` |
| `tenant_id` | `typing.Optional[str]` |
| `client_id` | `typing.Optional[str]` |
| `client_secret` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Construct the config object automatically from environment variables. |
| [`get_fsspec_kwargs()`](#get_fsspec_kwargs) | Returns the configuration as kwargs for constructing an fsspec filesystem. |


#### auto()

```python
def auto()
```
Construct the config object automatically from environment variables.


#### get_fsspec_kwargs()

```python
def get_fsspec_kwargs(
    anonymous: bool,
    kwargs,
) -> typing.Dict[str, typing.Any]
```
Returns the configuration as kwargs for constructing an fsspec filesystem.


| Parameter | Type |
|-|-|
| `anonymous` | `bool` |
| `kwargs` | `**kwargs` |

## flyte.storage.GCS

Any GCS specific configuration.


```python
class GCS(
    retries: int,
    backoff: datetime.timedelta,
    enable_debug: bool,
    attach_execution_metadata: bool,
    gsutil_parallelism: bool,
)
```
| Parameter | Type |
|-|-|
| `retries` | `int` |
| `backoff` | `datetime.timedelta` |
| `enable_debug` | `bool` |
| `attach_execution_metadata` | `bool` |
| `gsutil_parallelism` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Construct the config object automatically from environment variables. |
| [`get_fsspec_kwargs()`](#get_fsspec_kwargs) | Returns the configuration as kwargs for constructing an fsspec filesystem. |


#### auto()

```python
def auto()
```
Construct the config object automatically from environment variables.


#### get_fsspec_kwargs()

```python
def get_fsspec_kwargs(
    anonymous: bool,
    kwargs,
) -> typing.Dict[str, typing.Any]
```
Returns the configuration as kwargs for constructing an fsspec filesystem.


| Parameter | Type |
|-|-|
| `anonymous` | `bool` |
| `kwargs` | `**kwargs` |

## flyte.storage.S3

S3 specific configuration


```python
class S3(
    retries: int,
    backoff: datetime.timedelta,
    enable_debug: bool,
    attach_execution_metadata: bool,
    endpoint: typing.Optional[str],
    access_key_id: typing.Optional[str],
    secret_access_key: typing.Optional[str],
    region: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `retries` | `int` |
| `backoff` | `datetime.timedelta` |
| `enable_debug` | `bool` |
| `attach_execution_metadata` | `bool` |
| `endpoint` | `typing.Optional[str]` |
| `access_key_id` | `typing.Optional[str]` |
| `secret_access_key` | `typing.Optional[str]` |
| `region` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | :return: Config. |
| [`for_sandbox()`](#for_sandbox) | :return:. |
| [`get_fsspec_kwargs()`](#get_fsspec_kwargs) | Returns the configuration as kwargs for constructing an fsspec filesystem. |


#### auto()

```python
def auto(
    region: str | None,
) -> S3
```
:return: Config


| Parameter | Type |
|-|-|
| `region` | `str \| None` |

#### for_sandbox()

```python
def for_sandbox()
```
:return:


#### get_fsspec_kwargs()

```python
def get_fsspec_kwargs(
    anonymous: bool,
    kwargs,
) -> typing.Dict[str, typing.Any]
```
Returns the configuration as kwargs for constructing an fsspec filesystem.


| Parameter | Type |
|-|-|
| `anonymous` | `bool` |
| `kwargs` | `**kwargs` |

## flyte.storage.Storage

Data storage configuration that applies across any provider.


```python
class Storage(
    retries: int,
    backoff: datetime.timedelta,
    enable_debug: bool,
    attach_execution_metadata: bool,
)
```
| Parameter | Type |
|-|-|
| `retries` | `int` |
| `backoff` | `datetime.timedelta` |
| `enable_debug` | `bool` |
| `attach_execution_metadata` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Construct the config object automatically from environment variables. |
| [`get_fsspec_kwargs()`](#get_fsspec_kwargs) | Returns the configuration as kwargs for constructing an fsspec filesystem. |


#### auto()

```python
def auto()
```
Construct the config object automatically from environment variables.


#### get_fsspec_kwargs()

```python
def get_fsspec_kwargs(
    anonymous: bool,
    kwargs,
) -> typing.Dict[str, typing.Any]
```
Returns the configuration as kwargs for constructing an fsspec filesystem.


| Parameter | Type |
|-|-|
| `anonymous` | `bool` |
| `kwargs` | `**kwargs` |

