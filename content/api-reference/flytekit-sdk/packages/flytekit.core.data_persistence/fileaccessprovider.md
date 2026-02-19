---
title: FileAccessProvider
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FileAccessProvider

**Package:** `flytekit.core.data_persistence`

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
| Parameter | Type | Description |
|-|-|-|
| `local_sandbox_dir` | `typing.Union[str, os.PathLike]` | A local temporary working directory, that should be used to store data |
| `raw_output_prefix` | `str` | |
| `data_config` | `typing.Optional[flytekit.configuration.DataConfig]` | |
| `execution_metadata` | `typing.Optional[dict]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `data_config` | `None` |  |
| `local_access` | `None` |  |
| `local_sandbox_dir` | `None` | This is a context based temp dir. |
| `raw_output_fs` | `None` | Returns a file system corresponding to the provided raw output prefix |
| `raw_output_prefix` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`async_get_data()`](#async_get_data) |  |
| [`async_put_data()`](#async_put_data) | The implication here is that we're always going to put data to the remote location, so we. |
| [`async_put_raw_data()`](#async_put_raw_data) | This is a more flexible version of put that accepts a file-like object or a string path. |
| [`download()`](#download) | Downloads from remote to local. |
| [`download_directory()`](#download_directory) | Downloads directory from given remote to local path. |
| [`exists()`](#exists) |  |
| [`generate_new_custom_path()`](#generate_new_custom_path) | Generates a new path with the raw output prefix and a random string appended to it. |
| [`get()`](#get) |  |
| [`get_async_filesystem_for_path()`](#get_async_filesystem_for_path) |  |
| [`get_data()`](#get_data) |  |
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
| [`put_data()`](#put_data) | The implication here is that we're always going to put data to the remote location, so we. |
| [`put_raw_data()`](#put_raw_data) | This is a more flexible version of put that accepts a file-like object or a string path. |
| [`recursive_paths()`](#recursive_paths) |  |
| [`sep()`](#sep) |  |
| [`strip_file_header()`](#strip_file_header) | Drops file:// if it exists from the file. |
| [`upload()`](#upload) |  |
| [`upload_directory()`](#upload_directory) |  |


### async_get_data()

```python
def async_get_data(
    remote_path: str,
    local_path: str,
    is_multipart: bool,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `remote_path` | `str` | |
| `local_path` | `str` | |
| `is_multipart` | `bool` | |
| `kwargs` | `**kwargs` | |

### async_put_data()

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



| Parameter | Type | Description |
|-|-|-|
| `local_path` | `typing.Union[str, os.PathLike]` | |
| `remote_path` | `str` | |
| `is_multipart` | `bool` | |
| `kwargs` | `**kwargs` | |

### async_put_raw_data()

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



| Parameter | Type | Description |
|-|-|-|
| `lpath` | `typing.Union[str, os.PathLike, pathlib._local.Path, bytes, _io.BufferedReader, _io.BytesIO, _io.StringIO]` | A file-like object or a string path |
| `upload_prefix` | `typing.Optional[str]` | A prefix to add to the path, see above for usage, can be an "". If None then a random string will be generated |
| `file_name` | `typing.Optional[str]` | A file name to add to the path. If None, then the file name will be the tail of the path if lpath is a file, or a random string if lpath is a buffer |
| `read_chunk_size_bytes` | `int` | If lpath is a buffer, this is the chunk size to read from it |
| `encoding` | `str` | If lpath is a io.StringIO, this is the encoding to use to encode it to binary. |
| `skip_raw_data_prefix` | `bool` | If True, the raw data prefix will not be prepended to the upload_prefix |
| `kwargs` | `**kwargs` | Additional kwargs are passed into the fsspec put() call or the open() call :return: Returns the final path data was written to. |

### download()

```python
def download(
    remote_path: str,
    local_path: str,
    kwargs,
)
```
Downloads from remote to local


| Parameter | Type | Description |
|-|-|-|
| `remote_path` | `str` | |
| `local_path` | `str` | |
| `kwargs` | `**kwargs` | |

### download_directory()

```python
def download_directory(
    remote_path: str,
    local_path: str,
    kwargs,
)
```
Downloads directory from given remote to local path


| Parameter | Type | Description |
|-|-|-|
| `remote_path` | `str` | |
| `local_path` | `str` | |
| `kwargs` | `**kwargs` | |

### exists()

```python
def exists(
    path: str,
) -> bool
```
| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |

### generate_new_custom_path()

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



| Parameter | Type | Description |
|-|-|-|
| `fs` | `typing.Optional[fsspec.spec.AbstractFileSystem]` | The filesystem to use. If None, the context's raw output filesystem is used. |
| `alt` | `typing.Optional[str]` | An alternate first member of the prefix to use instead of the default. |
| `stem` | `typing.Optional[str]` | A stem to append to the path. :return: The new path. |

### get()

```python
def get(
    from_path: str,
    to_path: str,
    recursive: bool,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `from_path` | `str` | |
| `to_path` | `str` | |
| `recursive` | `bool` | |
| `kwargs` | `**kwargs` | |

### get_async_filesystem_for_path()

```python
def get_async_filesystem_for_path(
    path: str,
    anonymous: bool,
    kwargs,
) -> typing.Union[fsspec.asyn.AsyncFileSystem, fsspec.spec.AbstractFileSystem]
```
| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |
| `anonymous` | `bool` | |
| `kwargs` | `**kwargs` | |

### get_data()

```python
def get_data(
    remote_path: str,
    local_path: str,
    is_multipart: bool,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `remote_path` | `str` | |
| `local_path` | `str` | |
| `is_multipart` | `bool` | |
| `kwargs` | `**kwargs` | |

### get_file_tail()

```python
def get_file_tail(
    file_path_or_file_name: str,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `file_path_or_file_name` | `str` | |

### get_filesystem()

```python
def get_filesystem(
    protocol: typing.Optional[str],
    anonymous: bool,
    path: typing.Optional[str],
    kwargs,
) -> fsspec.spec.AbstractFileSystem
```
| Parameter | Type | Description |
|-|-|-|
| `protocol` | `typing.Optional[str]` | |
| `anonymous` | `bool` | |
| `path` | `typing.Optional[str]` | |
| `kwargs` | `**kwargs` | |

### get_filesystem_for_path()

```python
def get_filesystem_for_path(
    path: str,
    anonymous: bool,
    kwargs,
) -> fsspec.spec.AbstractFileSystem
```
| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |
| `anonymous` | `bool` | |
| `kwargs` | `**kwargs` | |

### get_random_local_directory()

```python
def get_random_local_directory()
```
### get_random_local_path()

```python
def get_random_local_path(
    file_path_or_file_name: typing.Optional[str],
) -> str
```
Use file_path_or_file_name, when you want a random directory, but want to preserve the leaf file name


| Parameter | Type | Description |
|-|-|-|
| `file_path_or_file_name` | `typing.Optional[str]` | |

### get_random_remote_directory()

```python
def get_random_remote_directory()
```
### get_random_remote_path()

```python
def get_random_remote_path(
    file_path_or_file_name: typing.Optional[str],
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `file_path_or_file_name` | `typing.Optional[str]` | |

### get_random_string()

```python
def get_random_string()
```
### is_remote()

```python
def is_remote(
    path: typing.Union[str, os.PathLike],
) -> bool
```
Deprecated. Let's find a replacement


| Parameter | Type | Description |
|-|-|-|
| `path` | `typing.Union[str, os.PathLike]` | |

### join()

```python
def join(
    args: *args,
    unstrip: bool,
    fs: typing.Optional[fsspec.spec.AbstractFileSystem],
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `unstrip` | `bool` | |
| `fs` | `typing.Optional[fsspec.spec.AbstractFileSystem]` | |

### put_data()

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



| Parameter | Type | Description |
|-|-|-|
| `local_path` | `typing.Union[str, os.PathLike]` | |
| `remote_path` | `str` | |
| `is_multipart` | `bool` | |
| `kwargs` | `**kwargs` | |

### put_raw_data()

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



| Parameter | Type | Description |
|-|-|-|
| `lpath` | `typing.Union[str, os.PathLike, pathlib._local.Path, bytes, _io.BufferedReader, _io.BytesIO, _io.StringIO]` | A file-like object or a string path |
| `upload_prefix` | `typing.Optional[str]` | A prefix to add to the path, see above for usage, can be an "". If None then a random string will be generated |
| `file_name` | `typing.Optional[str]` | A file name to add to the path. If None, then the file name will be the tail of the path if lpath is a file, or a random string if lpath is a buffer |
| `read_chunk_size_bytes` | `int` | If lpath is a buffer, this is the chunk size to read from it |
| `encoding` | `str` | If lpath is a io.StringIO, this is the encoding to use to encode it to binary. |
| `skip_raw_data_prefix` | `bool` | If True, the raw data prefix will not be prepended to the upload_prefix |
| `kwargs` | `**kwargs` | Additional kwargs are passed into the fsspec put() call or the open() call :return: Returns the final path data was written to. |

### recursive_paths()

```python
def recursive_paths(
    f: str,
    t: str,
) -> typing.Tuple[str, str]
```
| Parameter | Type | Description |
|-|-|-|
| `f` | `str` | |
| `t` | `str` | |

### sep()

```python
def sep(
    file_system: typing.Optional[fsspec.spec.AbstractFileSystem],
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `file_system` | `typing.Optional[fsspec.spec.AbstractFileSystem]` | |

### strip_file_header()

```python
def strip_file_header(
    path: str,
    trim_trailing_sep: bool,
) -> str
```
Drops file:// if it exists from the file


| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |
| `trim_trailing_sep` | `bool` | |

### upload()

```python
def upload(
    file_path: str,
    to_path: str,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `file_path` | `str` | |
| `to_path` | `str` | |
| `kwargs` | `**kwargs` | |

### upload_directory()

```python
def upload_directory(
    local_path: str,
    remote_path: str,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `local_path` | `str` | |
| `remote_path` | `str` | |
| `kwargs` | `**kwargs` | |

