---
title: flyte.storage
version: 0.2.0b14
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
| [`get()`](#get) |  |
| [`get_random_local_directory()`](#get_random_local_directory) | :return: a random directory. |
| [`get_random_local_path()`](#get_random_local_path) | Use file_path_or_file_name, when you want a random directory, but want to preserve the leaf file name. |
| [`get_stream()`](#get_stream) | Get a stream of data from a remote location. |
| [`get_underlying_filesystem()`](#get_underlying_filesystem) |  |
| [`is_remote()`](#is_remote) | Let's find a replacement. |
| [`join()`](#join) | Join multiple paths together. |
| [`put()`](#put) |  |
| [`put_stream()`](#put_stream) | Put a stream of data to a remote location. |


## Methods

#### get()

```python
def get(
    from_path: str,
    to_path: typing.Union[str, pathlib._local.Path, NoneType],
    recursive: bool,
    kwargs,
) -> str
```
| Parameter | Type |
|-|-|
| `from_path` | `str` |
| `to_path` | `typing.Union[str, pathlib._local.Path, NoneType]` |
| `recursive` | `bool` |
| `kwargs` | `**kwargs` |

#### get_random_local_directory()

```python
def get_random_local_directory()
```
:return: a random directory
:rtype: pathlib.Path


#### get_random_local_path()

```python
def get_random_local_path(
    file_path_or_file_name: pathlib._local.Path | str | None,
) -> pathlib._local.Path
```
Use file_path_or_file_name, when you want a random directory, but want to preserve the leaf file name


| Parameter | Type |
|-|-|
| `file_path_or_file_name` | `pathlib._local.Path \| str \| None` |

#### get_stream()

```python
def get_stream(
    path: str,
    chunk_size,
    kwargs,
) -> typing.AsyncIterator[bytes]
```
Get a stream of data from a remote location.
This is useful for downloading streaming data from a remote location.
Example usage:
```python
import flyte.storage as storage
obj = storage.get_stream(path="s3://my_bucket/my_file.txt")
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
) -> fsspec.spec.AbstractFileSystem
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
    path: typing.Union[pathlib._local.Path, str],
) -> bool
```
Let's find a replacement


| Parameter | Type |
|-|-|
| `path` | `typing.Union[pathlib._local.Path, str]` |

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

#### put()

```python
def put(
    from_path: str,
    to_path: typing.Optional[str],
    recursive: bool,
    kwargs,
) -> str
```
| Parameter | Type |
|-|-|
| `from_path` | `str` |
| `to_path` | `typing.Optional[str]` |
| `recursive` | `bool` |
| `kwargs` | `**kwargs` |

#### put_stream()

```python
def put_stream(
    data_iterable: typing.Union[typing.AsyncIterable[bytes], bytes],
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
| `data_iterable` | `typing.Union[typing.AsyncIterable[bytes], bytes]` |
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

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | :return: Config. |
| [`for_sandbox()`](#for_sandbox) | :return:. |
| [`get_fsspec_kwargs()`](#get_fsspec_kwargs) | Returns the configuration as kwargs for constructing an fsspec filesystem. |


#### auto()

```python
def auto()
```
:return: Config


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

