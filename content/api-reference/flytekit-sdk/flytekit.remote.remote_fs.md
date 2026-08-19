---
title: flytekit.remote.remote_fs
version: 1.16.28
variants: +flyte +union
layout: py_api
---

# flytekit.remote.remote_fs

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteFS`](.././flytekit.remote.remote_fs#flytekitremoteremote_fsflytefs) | Want this to behave mostly just like the HTTP file system. |
| [`FlytePathResolver`](.././flytekit.remote.remote_fs#flytekitremoteremote_fsflytepathresolver) |  |
| [`HttpFileWriter`](.././flytekit.remote.remote_fs#flytekitremoteremote_fshttpfilewriter) |  |

### Methods

| Method | Description |
|-|-|
| [`get_flyte_fs()`](#get_flyte_fs) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `REMOTE_PLACEHOLDER` | `str` |  |

## Methods

#### get_flyte_fs()

```python
def get_flyte_fs(
    remote: FlyteRemote,
) -> typing.Type[FlyteFS]
```
| Parameter | Type | Description |
|-|-|-|
| `remote` | `FlyteRemote` | |

## flytekit.remote.remote_fs.FlyteFS

Want this to behave mostly just like the HTTP file system.


### Parameters

```python
class FlyteFS(
    remote: FlyteRemote,
    asynchronous: bool = False,
    **storage_options,
)
```
NB: if this is called async, you must await set_client

Parameters
----------
block_size: int
    Blocks to read bytes; if 0, will default to raw requests file-like
    objects instead of HTTPFile instances
simple_links: bool
    If True, will consider both HTML &lt;a&gt; tags and anything that looks
    like a URL; if False, will consider only the former.
same_scheme: True
    When doing ls/glob, if this is True, only consider paths that have
    http/https matching the input URLs.
size_policy: this argument is deprecated
client_kwargs: dict
    Passed to aiohttp.ClientSession, see
    https://docs.aiohttp.org/en/stable/client_reference.html
    For example, ``{'auth': aiohttp.BasicAuth('user', 'pass')}``
get_client: Callable[..., aiohttp.ClientSession]
    A callable, which takes keyword arguments and constructs
    an aiohttp.ClientSession. Its state will be managed by
    the HTTPFileSystem class.
storage_options: key-value
    Any other parameters passed on to requests
cache_type, cache_options: defaults used in open()


| Parameter | Type | Description |
|-|-|-|
| `remote` | `FlyteRemote` | |
| `asynchronous` | `bool` | |
| `**storage_options` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `fsid` | `str` | Persistent filesystem id that can be used to compare filesystems across sessions. |

### Methods

| Method | Description |
|-|-|
| [`exists()`](#exists) | Is there a file at the given path. |
| [`extract_common()`](#extract_common) | This function that will take a list of strings and return the longest prefix that they all have in common. |
| [`get_filename_root()`](#get_filename_root) | Given a dictionary of file paths to hashes and content lengths, return a consistent filename root. |
| [`get_hashes_and_lengths()`](#get_hashes_and_lengths) | Returns a flat list of absolute file paths to their hashes and content lengths. |


#### exists()

```python
def exists(
    path,
    **kwargs,
)
```
Is there a file at the given path


| Parameter | Type | Description |
|-|-|-|
| `path` |  | |
| `**kwargs` |  | |

#### extract_common()

```python
def extract_common(
    native_urls: typing.List[str],
) -> str
```
This function that will take a list of strings and return the longest prefix that they all have in common.
That is, if you have
    ['s3://my-s3-bucket/flytesnacks/development/ABCYZWMPACZAJ2MABGMOZ6CCPY======/source/empty.md',
     's3://my-s3-bucket/flytesnacks/development/ABCXKL5ZZWXY3PDLM3OONUHHME======/source/nested/more.txt',
     's3://my-s3-bucket/flytesnacks/development/ABCXBAPBKONMADXVW5Q3J6YBWM======/source/original.txt']
this will return back 's3://my-s3-bucket/flytesnacks/development/'
Note that trailing characters after a separator that just happen to be the same will also be stripped.


| Parameter | Type | Description |
|-|-|-|
| `native_urls` | `typing.List[str]` | |

#### get_filename_root()

```python
def get_filename_root(
    file_info: HashStructure,
) -> str
```
Given a dictionary of file paths to hashes and content lengths, return a consistent filename root.
This is done by hashing the sorted list of file paths and then base32 encoding the result.
If the input is empty, then generate a random string


| Parameter | Type | Description |
|-|-|-|
| `file_info` | `HashStructure` | |

#### get_hashes_and_lengths()

```python
def get_hashes_and_lengths(
    p: pathlib.Path,
) -> HashStructure
```
Returns a flat list of absolute file paths to their hashes and content lengths
this output is used both for the file upload request, and to create consistently a filename root for
uploaded folders. We'll also use it for single files just for consistency.
If a directory then all the files in the directory will be hashed.
If a single file then just that file will be hashed.
Skip symlinks


| Parameter | Type | Description |
|-|-|-|
| `p` | `pathlib.Path` | |

## flytekit.remote.remote_fs.FlytePathResolver

### Methods

| Method | Description |
|-|-|
| [`add_mapping()`](#add_mapping) | Thread safe method to dd a mapping from a flyte uri to a remote path. |
| [`resolve_remote_path()`](#resolve_remote_path) | Given a flyte uri, return the remote path if it exists or was created in current session, otherwise return None. |


#### add_mapping()

```python
def add_mapping(
    flyte_uri: str,
    remote_path: str,
)
```
Thread safe method to dd a mapping from a flyte uri to a remote path


| Parameter | Type | Description |
|-|-|-|
| `flyte_uri` | `str` | |
| `remote_path` | `str` | |

#### resolve_remote_path()

```python
def resolve_remote_path(
    flyte_uri: str,
) -> typing.Optional[str]
```
Given a flyte uri, return the remote path if it exists or was created in current session, otherwise return None


| Parameter | Type | Description |
|-|-|-|
| `flyte_uri` | `str` | |

## flytekit.remote.remote_fs.HttpFileWriter

### Parameters

```python
class HttpFileWriter(
    remote: FlyteRemote,
    filename: str,
    **kwargs,
)
```
Template for files with buffered reading and writing

Parameters
----------
fs: instance of FileSystem
path: str
    location in file-system
mode: str
    Normal file modes. Currently only 'wb', 'ab' or 'rb'. Some file
    systems may be read-only, and some may not support append.
block_size: int
    Buffer size for reading or writing, 'default' for class default
autocommit: bool
    Whether to write to final destination; may only impact what
    happens when file is being closed.
cache_type: {"readahead", "none", "mmap", "bytes"}, default "readahead"
    Caching policy in read mode. See the definitions in ``core``.
cache_options : dict
    Additional options passed to the constructor for the cache specified
    by `cache_type`.
size: int
    If given and in read mode, suppressed having to look up the file size
kwargs:
    Gets stored as self.kwargs


| Parameter | Type | Description |
|-|-|-|
| `remote` | `FlyteRemote` | |
| `filename` | `str` | |
| `**kwargs` |  | |

