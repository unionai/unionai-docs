---
title: flytekit.core.data_persistence
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.data_persistence


The Data persistence module is used by core flytekit and most of the core TypeTransformers to manage data fetch & store,
between the durable backend store and the runtime environment. This is designed to be a pluggable system, with a default
simple implementation that ships with the core.

## Directory

### Classes

| Class | Description |
|-|-|
| [`FileAccessProvider`](.././flytekit.core.data_persistence#flytekitcoredata_persistencefileaccessprovider) | This is the class that is available through the FlyteContext and can be used for persisting data to the remote. |

### Methods

| Method | Description |
|-|-|
| [`azure_setup_args()`](#azure_setup_args) |  |
| [`get_additional_fsspec_call_kwargs()`](#get_additional_fsspec_call_kwargs) | These are different from the setup args functions defined above. |
| [`get_fsspec_storage_options()`](#get_fsspec_storage_options) |  |
| [`s3_setup_args()`](#s3_setup_args) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `default_local_file_access_provider` | `FileAccessProvider` |  |
| `flyte_tmp_dir` | `str` |  |

## Methods

#### azure_setup_args()

```python
def azure_setup_args(
    azure_cfg: flytekit.configuration.AzureBlobStorageConfig,
    anonymous: bool,
) -> typing.Dict[str, typing.Any]
```
| Parameter | Type |
|-|-|
| `azure_cfg` | `flytekit.configuration.AzureBlobStorageConfig` |
| `anonymous` | `bool` |

#### get_additional_fsspec_call_kwargs()

```python
def get_additional_fsspec_call_kwargs(
    protocol: typing.Union[str, tuple],
    method_name: str,
) -> typing.Dict[str, typing.Any]
```
These are different from the setup args functions defined above. Those kwargs are applied when asking fsspec
to create the filesystem. These kwargs returned here are for when the filesystem's methods are invoked.



| Parameter | Type |
|-|-|
| `protocol` | `typing.Union[str, tuple]` |
| `method_name` | `str` |

#### get_fsspec_storage_options()

```python
def get_fsspec_storage_options(
    protocol: str,
    data_config: typing.Optional[flytekit.configuration.DataConfig],
    anonymous: bool,
    kwargs,
) -> typing.Dict[str, typing.Any]
```
| Parameter | Type |
|-|-|
| `protocol` | `str` |
| `data_config` | `typing.Optional[flytekit.configuration.DataConfig]` |
| `anonymous` | `bool` |
| `kwargs` | ``**kwargs`` |

#### s3_setup_args()

```python
def s3_setup_args(
    s3_cfg: flytekit.configuration.S3Config,
    anonymous: bool,
) -> typing.Dict[str, typing.Any]
```
| Parameter | Type |
|-|-|
| `s3_cfg` | `flytekit.configuration.S3Config` |
| `anonymous` | `bool` |

## flytekit.core.data_persistence.FileAccessProvider

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
) -> n: Returns the final path data was written to.
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
) -> n: The new path.
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
) -> n: Returns the final path data was written to.
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

