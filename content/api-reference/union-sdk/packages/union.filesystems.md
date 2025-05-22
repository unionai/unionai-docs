---
title: union.filesystems
version: 0.1.171.dev4+g052020f1.d20250404
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# union.filesystems

Module for fsspec implementations.
## Directory

### Classes

| Class | Description |
|-|-|
| [`AsyncUnionFS`](.././union.filesystems#unionfilesystemsasyncunionfs) | Async file operations, default implementations. |
| [`AsyncUnionMetaFS`](.././union.filesystems#unionfilesystemsasyncunionmetafs) | Async file operations, default implementations. |

## union.filesystems.AsyncUnionFS

Async file operations, default implementations

Passes bulk operations to asyncio.gather for concurrent operation.

Implementations that have concurrent batch operations and/or async methods
should inherit from this class instead of AbstractFileSystem. Docstrings are
copied from the un-underscored method in AbstractFileSystem, if not given.


```python
class AsyncUnionFS(
    logger: logging.Logger,
    loop: typing.Optional[asyncio.events.AbstractEventLoop],
    args,
    kwargs,
)
```
Create and configure file-system instance

Instances may be cachable, so if similar enough arguments are seen
a new instance is not required. The token attribute exists to allow
implementations to cache instances if they wish.

A reasonable default should be provided if there are no arguments.

Subclasses should call this method.

Parameters
----------
use_listings_cache, listings_expiry_time, max_paths:
    passed to ``DirCache``, if the implementation supports
    directory listing caching. Pass use_listings_cache=False
    to disable such caching.
skip_instance_cache: bool
    If this is a cachable implementation, pass True here to force
    creating a new instance even if a matching instance exists, and prevent
    storing this instance.
asynchronous: bool
loop: asyncio-compatible IOLoop or None


| Parameter | Type |
|-|-|
| `logger` | `logging.Logger` |
| `loop` | `typing.Optional[asyncio.events.AbstractEventLoop]` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`cat()`](#cat) | Fetch (potentially multiple) paths' contents. |
| [`cat_file()`](#cat_file) | Get the content of a file. |
| [`cat_ranges()`](#cat_ranges) | Get the contents of byte ranges from one or more files. |
| [`checksum()`](#checksum) | Unique value for current version of file. |
| [`clear_instance_cache()`](#clear_instance_cache) | Clear the cache of filesystem instances. |
| [`copy()`](#copy) | Copy within two locations in the filesystem. |
| [`cp()`](#cp) | Alias of `AbstractFileSystem. |
| [`cp_file()`](#cp_file) |  |
| [`created()`](#created) | Return the created timestamp of a file as a datetime. |
| [`current()`](#current) | Return the most recently instantiated FileSystem. |
| [`delete()`](#delete) | Alias of `AbstractFileSystem. |
| [`disk_usage()`](#disk_usage) | Alias of `AbstractFileSystem. |
| [`download()`](#download) | Alias of `AbstractFileSystem. |
| [`du()`](#du) | Space used by files and optionally directories within a path. |
| [`end_transaction()`](#end_transaction) | Finish write transaction, non-context version. |
| [`exists()`](#exists) | Is there a file at the given path. |
| [`expand_path()`](#expand_path) | Turn one or more globs or directories into a list of all matching paths. |
| [`find()`](#find) | List all files below path. |
| [`from_dict()`](#from_dict) | Recreate a filesystem instance from dictionary representation. |
| [`from_json()`](#from_json) | Recreate a filesystem instance from JSON representation. |
| [`get()`](#get) | Copy file(s) to local. |
| [`get_file()`](#get_file) | Copy single remote file to local. |
| [`get_mapper()`](#get_mapper) | Create key/value store based on this file-system. |
| [`glob()`](#glob) | Find files by glob-matching. |
| [`head()`](#head) | Get the first ``size`` bytes from file. |
| [`info()`](#info) | Give details of entry at path. |
| [`invalidate_cache()`](#invalidate_cache) | Discard any cached directory information. |
| [`isdir()`](#isdir) | Is this entry directory-like?. |
| [`isfile()`](#isfile) | Is this entry file-like?. |
| [`lexists()`](#lexists) | If there is a file at the given path (including. |
| [`listdir()`](#listdir) | Alias of `AbstractFileSystem. |
| [`ls()`](#ls) | List objects at path. |
| [`makedir()`](#makedir) | Alias of `AbstractFileSystem. |
| [`makedirs()`](#makedirs) | Recursively make directories. |
| [`mkdir()`](#mkdir) | Create directory entry at path. |
| [`mkdirs()`](#mkdirs) | Alias of `AbstractFileSystem. |
| [`modified()`](#modified) | Return the modified timestamp of a file as a datetime. |
| [`move()`](#move) | Alias of `AbstractFileSystem. |
| [`mv()`](#mv) | Move file(s) from one location to another. |
| [`open()`](#open) | Return a file-like object from the filesystem. |
| [`open_async()`](#open_async) |  |
| [`pipe()`](#pipe) | Put value into path. |
| [`pipe_file()`](#pipe_file) | Set the bytes of given file. |
| [`put()`](#put) | Copy file(s) from local. |
| [`put_file()`](#put_file) | Copy single file to remote. |
| [`read_block()`](#read_block) | Read a block of bytes from. |
| [`read_bytes()`](#read_bytes) | Alias of `AbstractFileSystem. |
| [`read_text()`](#read_text) | Get the contents of the file as a string. |
| [`rename()`](#rename) | Alias of `AbstractFileSystem. |
| [`rm()`](#rm) | Delete files. |
| [`rm_file()`](#rm_file) | Delete a file. |
| [`rmdir()`](#rmdir) | Remove a directory, if empty. |
| [`sign()`](#sign) | Create a signed URL representing the given path. |
| [`size()`](#size) | Size in bytes of file. |
| [`sizes()`](#sizes) | Size in bytes of each file in a list of paths. |
| [`start_transaction()`](#start_transaction) | Begin write transaction for deferring files, non-context version. |
| [`stat()`](#stat) | Alias of `AbstractFileSystem. |
| [`tail()`](#tail) | Get the last ``size`` bytes from file. |
| [`to_dict()`](#to_dict) | JSON-serializable dictionary representation of this filesystem instance. |
| [`to_json()`](#to_json) | JSON representation of this filesystem instance. |
| [`touch()`](#touch) | Create empty file, or update timestamp. |
| [`tree()`](#tree) | Return a tree-like structure of the filesystem starting from the given path as a string. |
| [`ukey()`](#ukey) | Hash of file properties, to tell if it has changed. |
| [`unstrip_protocol()`](#unstrip_protocol) | Format FS-specific path to generic, including protocol. |
| [`upload()`](#upload) | Alias of `AbstractFileSystem. |
| [`walk()`](#walk) | Return all files under the given path. |
| [`write_bytes()`](#write_bytes) | Alias of `AbstractFileSystem. |
| [`write_text()`](#write_text) | Write the text to the given file. |


#### cat()

```python
def cat(
    path,
    recursive,
    on_error,
    kwargs,
)
```
Fetch (potentially multiple) paths' contents

Parameters
----------
recursive: bool
    If True, assume the path(s) are directories, and get all the
    contained files
on_error : "raise", "omit", "return"
    If raise, an underlying exception will be raised (converted to KeyError
    if the type is in self.missing_exceptions); if omit, keys with exception
    will simply not be included in the output; if "return", all keys are
    included in the output, but the value will be bytes or an exception
    instance.
kwargs: passed to cat_file

Returns
-------
dict of {path: contents} if there are multiple paths
or the path has been otherwise expanded


| Parameter | Type |
|-|-|
| `path` |  |
| `recursive` |  |
| `on_error` |  |
| `kwargs` | ``**kwargs`` |

#### cat_file()

```python
def cat_file(
    path,
    start,
    end,
    kwargs,
)
```
Get the content of a file

Parameters
----------
path: URL of file on this filesystems
start, end: int
    Bytes limits of the read. If negative, backwards from end,
    like usual python slices. Either can be None for start or
    end of file, respectively
kwargs: passed to ``open()``.


| Parameter | Type |
|-|-|
| `path` |  |
| `start` |  |
| `end` |  |
| `kwargs` | ``**kwargs`` |

#### cat_ranges()

```python
def cat_ranges(
    paths,
    starts,
    ends,
    max_gap,
    on_error,
    kwargs,
)
```
Get the contents of byte ranges from one or more files

Parameters
----------
paths: list
    A list of of filepaths on this filesystems
starts, ends: int or list
    Bytes limits of the read. If using a single int, the same value will be
    used to read all the specified files.


| Parameter | Type |
|-|-|
| `paths` |  |
| `starts` |  |
| `ends` |  |
| `max_gap` |  |
| `on_error` |  |
| `kwargs` | ``**kwargs`` |

#### checksum()

```python
def checksum(
    path,
)
```
Unique value for current version of file

If the checksum is the same from one moment to another, the contents
are guaranteed to be the same. If the checksum changes, the contents
*might* have changed.

This should normally be overridden; default will probably capture
creation/modification timestamp (which would be good) or maybe
access timestamp (which would be bad)


| Parameter | Type |
|-|-|
| `path` |  |

#### clear_instance_cache()

```python
def clear_instance_cache()
```
Clear the cache of filesystem instances.

Notes
-----
Unless overridden by setting the ``cachable`` class attribute to False,
the filesystem class stores a reference to newly created instances. This
prevents Python's normal rules around garbage collection from working,
since the instances refcount will not drop to zero until
``clear_instance_cache`` is called.


#### copy()

```python
def copy(
    path1,
    path2,
    recursive,
    maxdepth,
    on_error,
    kwargs,
)
```
Copy within two locations in the filesystem

on_error : "raise", "ignore"
    If raise, any not-found exceptions will be raised; if ignore any
    not-found exceptions will cause the path to be skipped; defaults to
    raise unless recursive is true, where the default is ignore


| Parameter | Type |
|-|-|
| `path1` |  |
| `path2` |  |
| `recursive` |  |
| `maxdepth` |  |
| `on_error` |  |
| `kwargs` | ``**kwargs`` |

#### cp()

```python
def cp(
    path1,
    path2,
    kwargs,
)
```
Alias of `AbstractFileSystem.copy`.


| Parameter | Type |
|-|-|
| `path1` |  |
| `path2` |  |
| `kwargs` | ``**kwargs`` |

#### cp_file()

```python
def cp_file(
    path1,
    path2,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `path1` |  |
| `path2` |  |
| `kwargs` | ``**kwargs`` |

#### created()

```python
def created(
    path,
)
```
Return the created timestamp of a file as a datetime.datetime


| Parameter | Type |
|-|-|
| `path` |  |

#### current()

```python
def current()
```
Return the most recently instantiated FileSystem

If no instance has been created, then create one with defaults


#### delete()

```python
def delete(
    path,
    recursive,
    maxdepth,
)
```
Alias of `AbstractFileSystem.rm`.


| Parameter | Type |
|-|-|
| `path` |  |
| `recursive` |  |
| `maxdepth` |  |

#### disk_usage()

```python
def disk_usage(
    path,
    total,
    maxdepth,
    kwargs,
)
```
Alias of `AbstractFileSystem.du`.


| Parameter | Type |
|-|-|
| `path` |  |
| `total` |  |
| `maxdepth` |  |
| `kwargs` | ``**kwargs`` |

#### download()

```python
def download(
    rpath,
    lpath,
    recursive,
    kwargs,
)
```
Alias of `AbstractFileSystem.get`.


| Parameter | Type |
|-|-|
| `rpath` |  |
| `lpath` |  |
| `recursive` |  |
| `kwargs` | ``**kwargs`` |

#### du()

```python
def du(
    path,
    total,
    maxdepth,
    withdirs,
    kwargs,
)
```
Space used by files and optionally directories within a path

Directory size does not include the size of its contents.

Parameters
----------
path: str
total: bool
    Whether to sum all the file sizes
maxdepth: int or None
    Maximum number of directory levels to descend, None for unlimited.
withdirs: bool
    Whether to include directory paths in the output.
kwargs: passed to ``find``

Returns
-------
Dict of {path: size} if total=False, or int otherwise, where numbers
refer to bytes used.


| Parameter | Type |
|-|-|
| `path` |  |
| `total` |  |
| `maxdepth` |  |
| `withdirs` |  |
| `kwargs` | ``**kwargs`` |

#### end_transaction()

```python
def end_transaction()
```
Finish write transaction, non-context version


#### exists()

```python
def exists(
    path,
    kwargs,
)
```
Is there a file at the given path


| Parameter | Type |
|-|-|
| `path` |  |
| `kwargs` | ``**kwargs`` |

#### expand_path()

```python
def expand_path(
    path,
    recursive,
    maxdepth,
    kwargs,
)
```
Turn one or more globs or directories into a list of all matching paths
to files or directories.

kwargs are passed to ``glob`` or ``find``, which may in turn call ``ls``


| Parameter | Type |
|-|-|
| `path` |  |
| `recursive` |  |
| `maxdepth` |  |
| `kwargs` | ``**kwargs`` |

#### find()

```python
def find(
    path,
    maxdepth,
    withdirs,
    detail,
    kwargs,
)
```
List all files below path.

Like posix ``find`` command without conditions

Parameters
----------
path : str
maxdepth: int or None
    If not None, the maximum number of levels to descend
withdirs: bool
    Whether to include directory paths in the output. This is True
    when used by glob, but users usually only want files.
kwargs are passed to ``ls``.


| Parameter | Type |
|-|-|
| `path` |  |
| `maxdepth` |  |
| `withdirs` |  |
| `detail` |  |
| `kwargs` | ``**kwargs`` |

#### from_dict()

```python
def from_dict(
    dct: dict[str, Any],
) -> AbstractFileSystem
```
Recreate a filesystem instance from dictionary representation.

See ``.to_dict()`` for the expected structure of the input.

Parameters
----------
dct: Dict[str, Any]

Returns
-------
file system instance, not necessarily of this particular class.

Warnings
--------
This can import arbitrary modules (as determined by the ``cls`` key).
Make sure you haven't installed any modules that may execute malicious code
at import time.


| Parameter | Type |
|-|-|
| `dct` | `dict[str, Any]` |

#### from_json()

```python
def from_json(
    blob: str,
) -> AbstractFileSystem
```
Recreate a filesystem instance from JSON representation.

See ``.to_json()`` for the expected structure of the input.

Parameters
----------
blob: str

Returns
-------
file system instance, not necessarily of this particular class.

Warnings
--------
This can import arbitrary modules (as determined by the ``cls`` key).
Make sure you haven't installed any modules that may execute malicious code
at import time.


| Parameter | Type |
|-|-|
| `blob` | `str` |

#### get()

```python
def get(
    rpath,
    lpath,
    recursive,
    callback,
    maxdepth,
    kwargs,
)
```
Copy file(s) to local.

Copies a specific file or tree of files (if recursive=True). If lpath
ends with a "/", it will be assumed to be a directory, and target files
will go within. Can submit a list of paths, which may be glob-patterns
and will be expanded.

Calls get_file for each source.


| Parameter | Type |
|-|-|
| `rpath` |  |
| `lpath` |  |
| `recursive` |  |
| `callback` |  |
| `maxdepth` |  |
| `kwargs` | ``**kwargs`` |

#### get_file()

```python
def get_file(
    rpath,
    lpath,
    callback,
    outfile,
    kwargs,
)
```
Copy single remote file to local


| Parameter | Type |
|-|-|
| `rpath` |  |
| `lpath` |  |
| `callback` |  |
| `outfile` |  |
| `kwargs` | ``**kwargs`` |

#### get_mapper()

```python
def get_mapper(
    root,
    check,
    create,
    missing_exceptions,
)
```
Create key/value store based on this file-system

Makes a MutableMapping interface to the FS at the given root path.
See ``fsspec.mapping.FSMap`` for further details.


| Parameter | Type |
|-|-|
| `root` |  |
| `check` |  |
| `create` |  |
| `missing_exceptions` |  |

#### glob()

```python
def glob(
    path,
    maxdepth,
    kwargs,
)
```
Find files by glob-matching.

If the path ends with '/', only folders are returned.

We support ``"**"``,
``"?"`` and ``"[..]"``. We do not support ^ for pattern negation.

The `maxdepth` option is applied on the first `**` found in the path.

kwargs are passed to ``ls``.


| Parameter | Type |
|-|-|
| `path` |  |
| `maxdepth` |  |
| `kwargs` | ``**kwargs`` |

#### head()

```python
def head(
    path,
    size,
)
```
Get the first ``size`` bytes from file


| Parameter | Type |
|-|-|
| `path` |  |
| `size` |  |

#### info()

```python
def info(
    path,
    kwargs,
)
```
Give details of entry at path

Returns a single dictionary, with exactly the same information as ``ls``
would with ``detail=True``.

The default implementation calls ls and could be overridden by a
shortcut. kwargs are passed on to ```ls()``.

Some file systems might not be able to measure the file's size, in
which case, the returned dict will include ``'size': None``.

Returns
-------
dict with keys: name (full path in the FS), size (in bytes), type (file,
directory, or something else) and other FS-specific keys.


| Parameter | Type |
|-|-|
| `path` |  |
| `kwargs` | ``**kwargs`` |

#### invalidate_cache()

```python
def invalidate_cache(
    path,
)
```
Discard any cached directory information

Parameters
----------
path: string or None
    If None, clear all listings cached else listings at or under given
    path.


| Parameter | Type |
|-|-|
| `path` |  |

#### isdir()

```python
def isdir(
    path,
)
```
Is this entry directory-like?


| Parameter | Type |
|-|-|
| `path` |  |

#### isfile()

```python
def isfile(
    path,
)
```
Is this entry file-like?


| Parameter | Type |
|-|-|
| `path` |  |

#### lexists()

```python
def lexists(
    path,
    kwargs,
)
```
If there is a file at the given path (including
broken links)


| Parameter | Type |
|-|-|
| `path` |  |
| `kwargs` | ``**kwargs`` |

#### listdir()

```python
def listdir(
    path,
    detail,
    kwargs,
)
```
Alias of `AbstractFileSystem.ls`.


| Parameter | Type |
|-|-|
| `path` |  |
| `detail` |  |
| `kwargs` | ``**kwargs`` |

#### ls()

```python
def ls(
    path,
    detail,
    kwargs,
)
```
List objects at path.

This should include subdirectories and files at that location. The
difference between a file and a directory must be clear when details
are requested.

The specific keys, or perhaps a FileInfo class, or similar, is TBD,
but must be consistent across implementations.
Must include:

- full path to the entry (without protocol)
- size of the entry, in bytes. If the value cannot be determined, will
  be ``None``.
- type of entry, "file", "directory" or other

Additional information
may be present, appropriate to the file-system, e.g., generation,
checksum, etc.

May use refresh=True|False to allow use of self._ls_from_cache to
check for a saved listing and avoid calling the backend. This would be
common where listing may be expensive.

Parameters
----------
path: str
detail: bool
    if True, gives a list of dictionaries, where each is the same as
    the result of ``info(path)``. If False, gives a list of paths
    (str).
kwargs: may have additional backend-specific options, such as version
    information

Returns
-------
List of strings if detail is False, or list of directory information
dicts if detail is True.


| Parameter | Type |
|-|-|
| `path` |  |
| `detail` |  |
| `kwargs` | ``**kwargs`` |

#### makedir()

```python
def makedir(
    path,
    create_parents,
    kwargs,
)
```
Alias of `AbstractFileSystem.mkdir`.


| Parameter | Type |
|-|-|
| `path` |  |
| `create_parents` |  |
| `kwargs` | ``**kwargs`` |

#### makedirs()

```python
def makedirs(
    path,
    exist_ok,
)
```
Recursively make directories

Creates directory at path and any intervening required directories.
Raises exception if, for instance, the path already exists but is a
file.

Parameters
----------
path: str
    leaf directory name
exist_ok: bool (False)
    If False, will error if the target already exists


| Parameter | Type |
|-|-|
| `path` |  |
| `exist_ok` |  |

#### mkdir()

```python
def mkdir(
    path,
    create_parents,
    kwargs,
)
```
Create directory entry at path

For systems that don't have true directories, may create an for
this instance only and not touch the real filesystem

Parameters
----------
path: str
    location
create_parents: bool
    if True, this is equivalent to ``makedirs``
kwargs:
    may be permissions, etc.


| Parameter | Type |
|-|-|
| `path` |  |
| `create_parents` |  |
| `kwargs` | ``**kwargs`` |

#### mkdirs()

```python
def mkdirs(
    path,
    exist_ok,
)
```
Alias of `AbstractFileSystem.makedirs`.


| Parameter | Type |
|-|-|
| `path` |  |
| `exist_ok` |  |

#### modified()

```python
def modified(
    path,
)
```
Return the modified timestamp of a file as a datetime.datetime


| Parameter | Type |
|-|-|
| `path` |  |

#### move()

```python
def move(
    path1,
    path2,
    kwargs,
)
```
Alias of `AbstractFileSystem.mv`.


| Parameter | Type |
|-|-|
| `path1` |  |
| `path2` |  |
| `kwargs` | ``**kwargs`` |

#### mv()

```python
def mv(
    path1,
    path2,
    recursive,
    maxdepth,
    kwargs,
)
```
Move file(s) from one location to another


| Parameter | Type |
|-|-|
| `path1` |  |
| `path2` |  |
| `recursive` |  |
| `maxdepth` |  |
| `kwargs` | ``**kwargs`` |

#### open()

```python
def open(
    path,
    mode,
    block_size,
    cache_options,
    compression,
    kwargs,
)
```
Return a file-like object from the filesystem

The resultant instance must function correctly in a context ``with``
block.

Parameters
----------
path: str
    Target file
mode: str like 'rb', 'w'
    See builtin ``open()``
    Mode "x" (exclusive write) may be implemented by the backend. Even if
    it is, whether  it is checked up front or on commit, and whether it is
    atomic is implementation-dependent.
block_size: int
    Some indication of buffering - this is a value in bytes
cache_options : dict, optional
    Extra arguments to pass through to the cache.
compression: string or None
    If given, open file using compression codec. Can either be a compression
    name (a key in ``fsspec.compression.compr``) or "infer" to guess the
    compression from the filename suffix.
encoding, errors, newline: passed on to TextIOWrapper for text mode


| Parameter | Type |
|-|-|
| `path` |  |
| `mode` |  |
| `block_size` |  |
| `cache_options` |  |
| `compression` |  |
| `kwargs` | ``**kwargs`` |

#### open_async()

```python
def open_async(
    path: str,
    mode,
    kwargs,
) -> fsspec.asyn.AbstractAsyncStreamedFile
```
| Parameter | Type |
|-|-|
| `path` | `str` |
| `mode` |  |
| `kwargs` | ``**kwargs`` |

#### pipe()

```python
def pipe(
    path,
    value,
    kwargs,
)
```
Put value into path

(counterpart to ``cat``)

Parameters
----------
path: string or dict(str, bytes)
    If a string, a single remote location to put ``value`` bytes; if a dict,
    a mapping of {path: bytesvalue}.
value: bytes, optional
    If using a single path, these are the bytes to put there. Ignored if
    ``path`` is a dict


| Parameter | Type |
|-|-|
| `path` |  |
| `value` |  |
| `kwargs` | ``**kwargs`` |

#### pipe_file()

```python
def pipe_file(
    path,
    value,
    mode,
    kwargs,
)
```
Set the bytes of given file


| Parameter | Type |
|-|-|
| `path` |  |
| `value` |  |
| `mode` |  |
| `kwargs` | ``**kwargs`` |

#### put()

```python
def put(
    lpath,
    rpath,
    recursive,
    callback,
    maxdepth,
    kwargs,
)
```
Copy file(s) from local.

Copies a specific file or tree of files (if recursive=True). If rpath
ends with a "/", it will be assumed to be a directory, and target files
will go within.

Calls put_file for each source.


| Parameter | Type |
|-|-|
| `lpath` |  |
| `rpath` |  |
| `recursive` |  |
| `callback` |  |
| `maxdepth` |  |
| `kwargs` | ``**kwargs`` |

#### put_file()

```python
def put_file(
    lpath,
    rpath,
    callback,
    mode,
    kwargs,
)
```
Copy single file to remote


| Parameter | Type |
|-|-|
| `lpath` |  |
| `rpath` |  |
| `callback` |  |
| `mode` |  |
| `kwargs` | ``**kwargs`` |

#### read_block()

```python
def read_block(
    fn,
    offset,
    length,
    delimiter,
)
```
Read a block of bytes from

Starting at ``offset`` of the file, read ``length`` bytes.  If
``delimiter`` is set then we ensure that the read starts and stops at
delimiter boundaries that follow the locations ``offset`` and ``offset
+ length``.  If ``offset`` is zero then we start at zero.  The
bytestring returned WILL include the end delimiter string.

If offset+length is beyond the eof, reads to eof.

Parameters
----------
fn: string
    Path to filename
offset: int
    Byte offset to start read
length: int
    Number of bytes to read. If None, read to end.
delimiter: bytes (optional)
    Ensure reading starts and stops at delimiter bytestring

Examples
--------
>>> fs.read_block('data/file.csv', 0, 13)  # doctest: +SKIP
b'Alice, 100\nBo'
>>> fs.read_block('data/file.csv', 0, 13, delimiter=b'\n')  # doctest: +SKIP
b'Alice, 100\nBob, 200\n'

Use ``length=None`` to read to the end of the file.
>>> fs.read_block('data/file.csv', 0, None, delimiter=b'\n')  # doctest: +SKIP
b'Alice, 100\nBob, 200\nCharlie, 300'

See Also
--------
:func:`fsspec.utils.read_block`


| Parameter | Type |
|-|-|
| `fn` |  |
| `offset` |  |
| `length` |  |
| `delimiter` |  |

#### read_bytes()

```python
def read_bytes(
    path,
    start,
    end,
    kwargs,
)
```
Alias of `AbstractFileSystem.cat_file`.


| Parameter | Type |
|-|-|
| `path` |  |
| `start` |  |
| `end` |  |
| `kwargs` | ``**kwargs`` |

#### read_text()

```python
def read_text(
    path,
    encoding,
    errors,
    newline,
    kwargs,
)
```
Get the contents of the file as a string.

Parameters
----------
path: str
    URL of file on this filesystems
encoding, errors, newline: same as `open`.


| Parameter | Type |
|-|-|
| `path` |  |
| `encoding` |  |
| `errors` |  |
| `newline` |  |
| `kwargs` | ``**kwargs`` |

#### rename()

```python
def rename(
    path1,
    path2,
    kwargs,
)
```
Alias of `AbstractFileSystem.mv`.


| Parameter | Type |
|-|-|
| `path1` |  |
| `path2` |  |
| `kwargs` | ``**kwargs`` |

#### rm()

```python
def rm(
    path,
    recursive,
    maxdepth,
)
```
Delete files.

Parameters
----------
path: str or list of str
    File(s) to delete.
recursive: bool
    If file(s) are directories, recursively delete contents and then
    also remove the directory
maxdepth: int or None
    Depth to pass to walk for finding files to delete, if recursive.
    If None, there will be no limit and infinite recursion may be
    possible.


| Parameter | Type |
|-|-|
| `path` |  |
| `recursive` |  |
| `maxdepth` |  |

#### rm_file()

```python
def rm_file(
    path,
)
```
Delete a file


| Parameter | Type |
|-|-|
| `path` |  |

#### rmdir()

```python
def rmdir(
    path,
)
```
Remove a directory, if empty


| Parameter | Type |
|-|-|
| `path` |  |

#### sign()

```python
def sign(
    path,
    expiration,
    kwargs,
)
```
Create a signed URL representing the given path

Some implementations allow temporary URLs to be generated, as a
way of delegating credentials.

Parameters
----------
path : str
     The path on the filesystem
expiration : int
    Number of seconds to enable the URL for (if supported)

Returns
-------
URL : str
    The signed URL

Raises
------
NotImplementedError : if method is not implemented for a filesystem


| Parameter | Type |
|-|-|
| `path` |  |
| `expiration` |  |
| `kwargs` | ``**kwargs`` |

#### size()

```python
def size(
    path,
)
```
Size in bytes of file


| Parameter | Type |
|-|-|
| `path` |  |

#### sizes()

```python
def sizes(
    paths,
)
```
Size in bytes of each file in a list of paths


| Parameter | Type |
|-|-|
| `paths` |  |

#### start_transaction()

```python
def start_transaction()
```
Begin write transaction for deferring files, non-context version


#### stat()

```python
def stat(
    path,
    kwargs,
)
```
Alias of `AbstractFileSystem.info`.


| Parameter | Type |
|-|-|
| `path` |  |
| `kwargs` | ``**kwargs`` |

#### tail()

```python
def tail(
    path,
    size,
)
```
Get the last ``size`` bytes from file


| Parameter | Type |
|-|-|
| `path` |  |
| `size` |  |

#### to_dict()

```python
def to_dict(
    include_password: bool,
) -> dict[str, Any]
```
JSON-serializable dictionary representation of this filesystem instance.

Parameters
----------
include_password: bool, default True
    Whether to include the password (if any) in the output.

Returns
-------
Dictionary with keys ``cls`` (the python location of this class),
protocol (text name of this class's protocol, first one in case of
multiple), ``args`` (positional args, usually empty), and all other
keyword arguments as their own keys.

Warnings
--------
Serialized filesystems may contain sensitive information which have been
passed to the constructor, such as passwords and tokens. Make sure you
store and send them in a secure environment!


| Parameter | Type |
|-|-|
| `include_password` | `bool` |

#### to_json()

```python
def to_json(
    include_password: bool,
) -> str
```
JSON representation of this filesystem instance.

Parameters
----------
include_password: bool, default True
    Whether to include the password (if any) in the output.

Returns
-------
JSON string with keys ``cls`` (the python location of this class),
protocol (text name of this class's protocol, first one in case of
multiple), ``args`` (positional args, usually empty), and all other
keyword arguments as their own keys.

Warnings
--------
Serialized filesystems may contain sensitive information which have been
passed to the constructor, such as passwords and tokens. Make sure you
store and send them in a secure environment!


| Parameter | Type |
|-|-|
| `include_password` | `bool` |

#### touch()

```python
def touch(
    path,
    truncate,
    kwargs,
)
```
Create empty file, or update timestamp

Parameters
----------
path: str
    file location
truncate: bool
    If True, always set file size to 0; if False, update timestamp and
    leave file unchanged, if backend allows this


| Parameter | Type |
|-|-|
| `path` |  |
| `truncate` |  |
| `kwargs` | ``**kwargs`` |

#### tree()

```python
def tree(
    path: str,
    recursion_limit: int,
    max_display: int,
    display_size: bool,
    prefix: str,
    is_last: bool,
    first: bool,
    indent_size: int,
) -> str
```
Return a tree-like structure of the filesystem starting from the given path as a string.

Parameters
----------
    path: Root path to start traversal from
    recursion_limit: Maximum depth of directory traversal
    max_display: Maximum number of items to display per directory
    display_size: Whether to display file sizes
    prefix: Current line prefix for visual tree structure
    is_last: Whether current item is last in its level
    first: Whether this is the first call (displays root path)
    indent_size: Number of spaces by indent

Returns
-------
    str: A string representing the tree structure.

Example
-------
    >>> from fsspec import filesystem

    >>> fs = filesystem('ftp', host='test.rebex.net', user='demo', password='password')
    >>> tree = fs.tree(display_size=True, recursion_limit=3, indent_size=8, max_display=10)
    >>> print(tree)


| Parameter | Type |
|-|-|
| `path` | `str` |
| `recursion_limit` | `int` |
| `max_display` | `int` |
| `display_size` | `bool` |
| `prefix` | `str` |
| `is_last` | `bool` |
| `first` | `bool` |
| `indent_size` | `int` |

#### ukey()

```python
def ukey(
    path,
)
```
Hash of file properties, to tell if it has changed


| Parameter | Type |
|-|-|
| `path` |  |

#### unstrip_protocol()

```python
def unstrip_protocol(
    name: str,
) -> str
```
Format FS-specific path to generic, including protocol


| Parameter | Type |
|-|-|
| `name` | `str` |

#### upload()

```python
def upload(
    lpath,
    rpath,
    recursive,
    kwargs,
)
```
Alias of `AbstractFileSystem.put`.


| Parameter | Type |
|-|-|
| `lpath` |  |
| `rpath` |  |
| `recursive` |  |
| `kwargs` | ``**kwargs`` |

#### walk()

```python
def walk(
    path,
    maxdepth,
    topdown,
    on_error,
    kwargs,
)
```
Return all files under the given path.

List all files, recursing into subdirectories; output is iterator-style,
like ``os.walk()``. For a simple list of files, ``find()`` is available.

When topdown is True, the caller can modify the dirnames list in-place (perhaps
using del or slice assignment), and walk() will
only recurse into the subdirectories whose names remain in dirnames;
this can be used to prune the search, impose a specific order of visiting,
or even to inform walk() about directories the caller creates or renames before
it resumes walk() again.
Modifying dirnames when topdown is False has no effect. (see os.walk)

Note that the "files" outputted will include anything that is not
a directory, such as links.

Parameters
----------
path: str
    Root to recurse into
maxdepth: int
    Maximum recursion depth. None means limitless, but not recommended
    on link-based file-systems.
topdown: bool (True)
    Whether to walk the directory tree from the top downwards or from
    the bottom upwards.
on_error: "omit", "raise", a callable
    if omit (default), path with exception will simply be empty;
    If raise, an underlying exception will be raised;
    if callable, it will be called with a single OSError instance as argument
kwargs: passed to ``ls``


| Parameter | Type |
|-|-|
| `path` |  |
| `maxdepth` |  |
| `topdown` |  |
| `on_error` |  |
| `kwargs` | ``**kwargs`` |

#### write_bytes()

```python
def write_bytes(
    path,
    value,
    kwargs,
)
```
Alias of `AbstractFileSystem.pipe_file`.


| Parameter | Type |
|-|-|
| `path` |  |
| `value` |  |
| `kwargs` | ``**kwargs`` |

#### write_text()

```python
def write_text(
    path,
    value,
    encoding,
    errors,
    newline,
    kwargs,
)
```
Write the text to the given file.

An existing file will be overwritten.

Parameters
----------
path: str
    URL of file on this filesystems
value: str
    Text to write.
encoding, errors, newline: same as `open`.


| Parameter | Type |
|-|-|
| `path` |  |
| `value` |  |
| `encoding` |  |
| `errors` |  |
| `newline` |  |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `fsid` |  | {{< multiline >}}Persistent filesystem id that can be used to compare filesystems
across sessions.
{{< /multiline >}} |
| `loop` |  |  |
| `max_attempts` |  |  |
| `max_concurrent_tasks` |  |  |
| `retries` |  |  |
| `transaction` |  | {{< multiline >}}A context within which files are committed together upon exit

Requires the file class to implement `.commit()` and `.discard()`
for the normal and exception cases.
{{< /multiline >}} |

## union.filesystems.AsyncUnionMetaFS

Async file operations, default implementations

Passes bulk operations to asyncio.gather for concurrent operation.

Implementations that have concurrent batch operations and/or async methods
should inherit from this class instead of AbstractFileSystem. Docstrings are
copied from the un-underscored method in AbstractFileSystem, if not given.


```python
class AsyncUnionMetaFS(
    logger: logging.Logger,
    loop: typing.Optional[asyncio.events.AbstractEventLoop],
    args,
    kwargs,
)
```
Create and configure file-system instance

Instances may be cachable, so if similar enough arguments are seen
a new instance is not required. The token attribute exists to allow
implementations to cache instances if they wish.

A reasonable default should be provided if there are no arguments.

Subclasses should call this method.

Parameters
----------
use_listings_cache, listings_expiry_time, max_paths:
    passed to ``DirCache``, if the implementation supports
    directory listing caching. Pass use_listings_cache=False
    to disable such caching.
skip_instance_cache: bool
    If this is a cachable implementation, pass True here to force
    creating a new instance even if a matching instance exists, and prevent
    storing this instance.
asynchronous: bool
loop: asyncio-compatible IOLoop or None


| Parameter | Type |
|-|-|
| `logger` | `logging.Logger` |
| `loop` | `typing.Optional[asyncio.events.AbstractEventLoop]` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`cat()`](#cat) | Fetch (potentially multiple) paths' contents. |
| [`cat_file()`](#cat_file) | Get the content of a file. |
| [`cat_ranges()`](#cat_ranges) | Get the contents of byte ranges from one or more files. |
| [`checksum()`](#checksum) | Unique value for current version of file. |
| [`clear_instance_cache()`](#clear_instance_cache) | Clear the cache of filesystem instances. |
| [`copy()`](#copy) | Copy within two locations in the filesystem. |
| [`cp()`](#cp) | Alias of `AbstractFileSystem. |
| [`cp_file()`](#cp_file) |  |
| [`created()`](#created) | Return the created timestamp of a file as a datetime. |
| [`current()`](#current) | Return the most recently instantiated FileSystem. |
| [`delete()`](#delete) | Alias of `AbstractFileSystem. |
| [`disk_usage()`](#disk_usage) | Alias of `AbstractFileSystem. |
| [`download()`](#download) | Alias of `AbstractFileSystem. |
| [`du()`](#du) | Space used by files and optionally directories within a path. |
| [`end_transaction()`](#end_transaction) | Finish write transaction, non-context version. |
| [`exists()`](#exists) | Is there a file at the given path. |
| [`expand_path()`](#expand_path) | Turn one or more globs or directories into a list of all matching paths. |
| [`find()`](#find) | List all files below path. |
| [`from_dict()`](#from_dict) | Recreate a filesystem instance from dictionary representation. |
| [`from_json()`](#from_json) | Recreate a filesystem instance from JSON representation. |
| [`get()`](#get) | Copy file(s) to local. |
| [`get_file()`](#get_file) | Copy single remote file to local. |
| [`get_mapper()`](#get_mapper) | Create key/value store based on this file-system. |
| [`glob()`](#glob) | Find files by glob-matching. |
| [`head()`](#head) | Get the first ``size`` bytes from file. |
| [`info()`](#info) | Give details of entry at path. |
| [`invalidate_cache()`](#invalidate_cache) | Discard any cached directory information. |
| [`isdir()`](#isdir) | Is this entry directory-like?. |
| [`isfile()`](#isfile) | Is this entry file-like?. |
| [`lexists()`](#lexists) | If there is a file at the given path (including. |
| [`listdir()`](#listdir) | Alias of `AbstractFileSystem. |
| [`ls()`](#ls) | List objects at path. |
| [`makedir()`](#makedir) | Alias of `AbstractFileSystem. |
| [`makedirs()`](#makedirs) | Recursively make directories. |
| [`mkdir()`](#mkdir) | Create directory entry at path. |
| [`mkdirs()`](#mkdirs) | Alias of `AbstractFileSystem. |
| [`modified()`](#modified) | Return the modified timestamp of a file as a datetime. |
| [`move()`](#move) | Alias of `AbstractFileSystem. |
| [`mv()`](#mv) | Move file(s) from one location to another. |
| [`open()`](#open) | Return a file-like object from the filesystem. |
| [`open_async()`](#open_async) |  |
| [`pipe()`](#pipe) | Put value into path. |
| [`pipe_file()`](#pipe_file) | Set the bytes of given file. |
| [`put()`](#put) | Copy file(s) from local. |
| [`put_file()`](#put_file) | Copy single file to remote. |
| [`read_block()`](#read_block) | Read a block of bytes from. |
| [`read_bytes()`](#read_bytes) | Alias of `AbstractFileSystem. |
| [`read_text()`](#read_text) | Get the contents of the file as a string. |
| [`rename()`](#rename) | Alias of `AbstractFileSystem. |
| [`rm()`](#rm) | Delete files. |
| [`rm_file()`](#rm_file) | Delete a file. |
| [`rmdir()`](#rmdir) | Remove a directory, if empty. |
| [`sign()`](#sign) | Create a signed URL representing the given path. |
| [`size()`](#size) | Size in bytes of file. |
| [`sizes()`](#sizes) | Size in bytes of each file in a list of paths. |
| [`start_transaction()`](#start_transaction) | Begin write transaction for deferring files, non-context version. |
| [`stat()`](#stat) | Alias of `AbstractFileSystem. |
| [`tail()`](#tail) | Get the last ``size`` bytes from file. |
| [`to_dict()`](#to_dict) | JSON-serializable dictionary representation of this filesystem instance. |
| [`to_json()`](#to_json) | JSON representation of this filesystem instance. |
| [`touch()`](#touch) | Create empty file, or update timestamp. |
| [`tree()`](#tree) | Return a tree-like structure of the filesystem starting from the given path as a string. |
| [`ukey()`](#ukey) | Hash of file properties, to tell if it has changed. |
| [`unstrip_protocol()`](#unstrip_protocol) | Format FS-specific path to generic, including protocol. |
| [`upload()`](#upload) | Alias of `AbstractFileSystem. |
| [`walk()`](#walk) | Return all files under the given path. |
| [`write_bytes()`](#write_bytes) | Alias of `AbstractFileSystem. |
| [`write_text()`](#write_text) | Write the text to the given file. |


#### cat()

```python
def cat(
    path,
    recursive,
    on_error,
    kwargs,
)
```
Fetch (potentially multiple) paths' contents

Parameters
----------
recursive: bool
    If True, assume the path(s) are directories, and get all the
    contained files
on_error : "raise", "omit", "return"
    If raise, an underlying exception will be raised (converted to KeyError
    if the type is in self.missing_exceptions); if omit, keys with exception
    will simply not be included in the output; if "return", all keys are
    included in the output, but the value will be bytes or an exception
    instance.
kwargs: passed to cat_file

Returns
-------
dict of {path: contents} if there are multiple paths
or the path has been otherwise expanded


| Parameter | Type |
|-|-|
| `path` |  |
| `recursive` |  |
| `on_error` |  |
| `kwargs` | ``**kwargs`` |

#### cat_file()

```python
def cat_file(
    path,
    start,
    end,
    kwargs,
)
```
Get the content of a file

Parameters
----------
path: URL of file on this filesystems
start, end: int
    Bytes limits of the read. If negative, backwards from end,
    like usual python slices. Either can be None for start or
    end of file, respectively
kwargs: passed to ``open()``.


| Parameter | Type |
|-|-|
| `path` |  |
| `start` |  |
| `end` |  |
| `kwargs` | ``**kwargs`` |

#### cat_ranges()

```python
def cat_ranges(
    paths,
    starts,
    ends,
    max_gap,
    on_error,
    kwargs,
)
```
Get the contents of byte ranges from one or more files

Parameters
----------
paths: list
    A list of of filepaths on this filesystems
starts, ends: int or list
    Bytes limits of the read. If using a single int, the same value will be
    used to read all the specified files.


| Parameter | Type |
|-|-|
| `paths` |  |
| `starts` |  |
| `ends` |  |
| `max_gap` |  |
| `on_error` |  |
| `kwargs` | ``**kwargs`` |

#### checksum()

```python
def checksum(
    path,
)
```
Unique value for current version of file

If the checksum is the same from one moment to another, the contents
are guaranteed to be the same. If the checksum changes, the contents
*might* have changed.

This should normally be overridden; default will probably capture
creation/modification timestamp (which would be good) or maybe
access timestamp (which would be bad)


| Parameter | Type |
|-|-|
| `path` |  |

#### clear_instance_cache()

```python
def clear_instance_cache()
```
Clear the cache of filesystem instances.

Notes
-----
Unless overridden by setting the ``cachable`` class attribute to False,
the filesystem class stores a reference to newly created instances. This
prevents Python's normal rules around garbage collection from working,
since the instances refcount will not drop to zero until
``clear_instance_cache`` is called.


#### copy()

```python
def copy(
    path1,
    path2,
    recursive,
    maxdepth,
    on_error,
    kwargs,
)
```
Copy within two locations in the filesystem

on_error : "raise", "ignore"
    If raise, any not-found exceptions will be raised; if ignore any
    not-found exceptions will cause the path to be skipped; defaults to
    raise unless recursive is true, where the default is ignore


| Parameter | Type |
|-|-|
| `path1` |  |
| `path2` |  |
| `recursive` |  |
| `maxdepth` |  |
| `on_error` |  |
| `kwargs` | ``**kwargs`` |

#### cp()

```python
def cp(
    path1,
    path2,
    kwargs,
)
```
Alias of `AbstractFileSystem.copy`.


| Parameter | Type |
|-|-|
| `path1` |  |
| `path2` |  |
| `kwargs` | ``**kwargs`` |

#### cp_file()

```python
def cp_file(
    path1,
    path2,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `path1` |  |
| `path2` |  |
| `kwargs` | ``**kwargs`` |

#### created()

```python
def created(
    path,
)
```
Return the created timestamp of a file as a datetime.datetime


| Parameter | Type |
|-|-|
| `path` |  |

#### current()

```python
def current()
```
Return the most recently instantiated FileSystem

If no instance has been created, then create one with defaults


#### delete()

```python
def delete(
    path,
    recursive,
    maxdepth,
)
```
Alias of `AbstractFileSystem.rm`.


| Parameter | Type |
|-|-|
| `path` |  |
| `recursive` |  |
| `maxdepth` |  |

#### disk_usage()

```python
def disk_usage(
    path,
    total,
    maxdepth,
    kwargs,
)
```
Alias of `AbstractFileSystem.du`.


| Parameter | Type |
|-|-|
| `path` |  |
| `total` |  |
| `maxdepth` |  |
| `kwargs` | ``**kwargs`` |

#### download()

```python
def download(
    rpath,
    lpath,
    recursive,
    kwargs,
)
```
Alias of `AbstractFileSystem.get`.


| Parameter | Type |
|-|-|
| `rpath` |  |
| `lpath` |  |
| `recursive` |  |
| `kwargs` | ``**kwargs`` |

#### du()

```python
def du(
    path,
    total,
    maxdepth,
    withdirs,
    kwargs,
)
```
Space used by files and optionally directories within a path

Directory size does not include the size of its contents.

Parameters
----------
path: str
total: bool
    Whether to sum all the file sizes
maxdepth: int or None
    Maximum number of directory levels to descend, None for unlimited.
withdirs: bool
    Whether to include directory paths in the output.
kwargs: passed to ``find``

Returns
-------
Dict of {path: size} if total=False, or int otherwise, where numbers
refer to bytes used.


| Parameter | Type |
|-|-|
| `path` |  |
| `total` |  |
| `maxdepth` |  |
| `withdirs` |  |
| `kwargs` | ``**kwargs`` |

#### end_transaction()

```python
def end_transaction()
```
Finish write transaction, non-context version


#### exists()

```python
def exists(
    path,
    kwargs,
)
```
Is there a file at the given path


| Parameter | Type |
|-|-|
| `path` |  |
| `kwargs` | ``**kwargs`` |

#### expand_path()

```python
def expand_path(
    path,
    recursive,
    maxdepth,
    kwargs,
)
```
Turn one or more globs or directories into a list of all matching paths
to files or directories.

kwargs are passed to ``glob`` or ``find``, which may in turn call ``ls``


| Parameter | Type |
|-|-|
| `path` |  |
| `recursive` |  |
| `maxdepth` |  |
| `kwargs` | ``**kwargs`` |

#### find()

```python
def find(
    path,
    maxdepth,
    withdirs,
    detail,
    kwargs,
)
```
List all files below path.

Like posix ``find`` command without conditions

Parameters
----------
path : str
maxdepth: int or None
    If not None, the maximum number of levels to descend
withdirs: bool
    Whether to include directory paths in the output. This is True
    when used by glob, but users usually only want files.
kwargs are passed to ``ls``.


| Parameter | Type |
|-|-|
| `path` |  |
| `maxdepth` |  |
| `withdirs` |  |
| `detail` |  |
| `kwargs` | ``**kwargs`` |

#### from_dict()

```python
def from_dict(
    dct: dict[str, Any],
) -> AbstractFileSystem
```
Recreate a filesystem instance from dictionary representation.

See ``.to_dict()`` for the expected structure of the input.

Parameters
----------
dct: Dict[str, Any]

Returns
-------
file system instance, not necessarily of this particular class.

Warnings
--------
This can import arbitrary modules (as determined by the ``cls`` key).
Make sure you haven't installed any modules that may execute malicious code
at import time.


| Parameter | Type |
|-|-|
| `dct` | `dict[str, Any]` |

#### from_json()

```python
def from_json(
    blob: str,
) -> AbstractFileSystem
```
Recreate a filesystem instance from JSON representation.

See ``.to_json()`` for the expected structure of the input.

Parameters
----------
blob: str

Returns
-------
file system instance, not necessarily of this particular class.

Warnings
--------
This can import arbitrary modules (as determined by the ``cls`` key).
Make sure you haven't installed any modules that may execute malicious code
at import time.


| Parameter | Type |
|-|-|
| `blob` | `str` |

#### get()

```python
def get(
    rpath,
    lpath,
    recursive,
    callback,
    maxdepth,
    kwargs,
)
```
Copy file(s) to local.

Copies a specific file or tree of files (if recursive=True). If lpath
ends with a "/", it will be assumed to be a directory, and target files
will go within. Can submit a list of paths, which may be glob-patterns
and will be expanded.

Calls get_file for each source.


| Parameter | Type |
|-|-|
| `rpath` |  |
| `lpath` |  |
| `recursive` |  |
| `callback` |  |
| `maxdepth` |  |
| `kwargs` | ``**kwargs`` |

#### get_file()

```python
def get_file(
    rpath,
    lpath,
    callback,
    outfile,
    kwargs,
)
```
Copy single remote file to local


| Parameter | Type |
|-|-|
| `rpath` |  |
| `lpath` |  |
| `callback` |  |
| `outfile` |  |
| `kwargs` | ``**kwargs`` |

#### get_mapper()

```python
def get_mapper(
    root,
    check,
    create,
    missing_exceptions,
)
```
Create key/value store based on this file-system

Makes a MutableMapping interface to the FS at the given root path.
See ``fsspec.mapping.FSMap`` for further details.


| Parameter | Type |
|-|-|
| `root` |  |
| `check` |  |
| `create` |  |
| `missing_exceptions` |  |

#### glob()

```python
def glob(
    path,
    maxdepth,
    kwargs,
)
```
Find files by glob-matching.

If the path ends with '/', only folders are returned.

We support ``"**"``,
``"?"`` and ``"[..]"``. We do not support ^ for pattern negation.

The `maxdepth` option is applied on the first `**` found in the path.

kwargs are passed to ``ls``.


| Parameter | Type |
|-|-|
| `path` |  |
| `maxdepth` |  |
| `kwargs` | ``**kwargs`` |

#### head()

```python
def head(
    path,
    size,
)
```
Get the first ``size`` bytes from file


| Parameter | Type |
|-|-|
| `path` |  |
| `size` |  |

#### info()

```python
def info(
    path,
    kwargs,
)
```
Give details of entry at path

Returns a single dictionary, with exactly the same information as ``ls``
would with ``detail=True``.

The default implementation calls ls and could be overridden by a
shortcut. kwargs are passed on to ```ls()``.

Some file systems might not be able to measure the file's size, in
which case, the returned dict will include ``'size': None``.

Returns
-------
dict with keys: name (full path in the FS), size (in bytes), type (file,
directory, or something else) and other FS-specific keys.


| Parameter | Type |
|-|-|
| `path` |  |
| `kwargs` | ``**kwargs`` |

#### invalidate_cache()

```python
def invalidate_cache(
    path,
)
```
Discard any cached directory information

Parameters
----------
path: string or None
    If None, clear all listings cached else listings at or under given
    path.


| Parameter | Type |
|-|-|
| `path` |  |

#### isdir()

```python
def isdir(
    path,
)
```
Is this entry directory-like?


| Parameter | Type |
|-|-|
| `path` |  |

#### isfile()

```python
def isfile(
    path,
)
```
Is this entry file-like?


| Parameter | Type |
|-|-|
| `path` |  |

#### lexists()

```python
def lexists(
    path,
    kwargs,
)
```
If there is a file at the given path (including
broken links)


| Parameter | Type |
|-|-|
| `path` |  |
| `kwargs` | ``**kwargs`` |

#### listdir()

```python
def listdir(
    path,
    detail,
    kwargs,
)
```
Alias of `AbstractFileSystem.ls`.


| Parameter | Type |
|-|-|
| `path` |  |
| `detail` |  |
| `kwargs` | ``**kwargs`` |

#### ls()

```python
def ls(
    path,
    detail,
    kwargs,
)
```
List objects at path.

This should include subdirectories and files at that location. The
difference between a file and a directory must be clear when details
are requested.

The specific keys, or perhaps a FileInfo class, or similar, is TBD,
but must be consistent across implementations.
Must include:

- full path to the entry (without protocol)
- size of the entry, in bytes. If the value cannot be determined, will
  be ``None``.
- type of entry, "file", "directory" or other

Additional information
may be present, appropriate to the file-system, e.g., generation,
checksum, etc.

May use refresh=True|False to allow use of self._ls_from_cache to
check for a saved listing and avoid calling the backend. This would be
common where listing may be expensive.

Parameters
----------
path: str
detail: bool
    if True, gives a list of dictionaries, where each is the same as
    the result of ``info(path)``. If False, gives a list of paths
    (str).
kwargs: may have additional backend-specific options, such as version
    information

Returns
-------
List of strings if detail is False, or list of directory information
dicts if detail is True.


| Parameter | Type |
|-|-|
| `path` |  |
| `detail` |  |
| `kwargs` | ``**kwargs`` |

#### makedir()

```python
def makedir(
    path,
    create_parents,
    kwargs,
)
```
Alias of `AbstractFileSystem.mkdir`.


| Parameter | Type |
|-|-|
| `path` |  |
| `create_parents` |  |
| `kwargs` | ``**kwargs`` |

#### makedirs()

```python
def makedirs(
    path,
    exist_ok,
)
```
Recursively make directories

Creates directory at path and any intervening required directories.
Raises exception if, for instance, the path already exists but is a
file.

Parameters
----------
path: str
    leaf directory name
exist_ok: bool (False)
    If False, will error if the target already exists


| Parameter | Type |
|-|-|
| `path` |  |
| `exist_ok` |  |

#### mkdir()

```python
def mkdir(
    path,
    create_parents,
    kwargs,
)
```
Create directory entry at path

For systems that don't have true directories, may create an for
this instance only and not touch the real filesystem

Parameters
----------
path: str
    location
create_parents: bool
    if True, this is equivalent to ``makedirs``
kwargs:
    may be permissions, etc.


| Parameter | Type |
|-|-|
| `path` |  |
| `create_parents` |  |
| `kwargs` | ``**kwargs`` |

#### mkdirs()

```python
def mkdirs(
    path,
    exist_ok,
)
```
Alias of `AbstractFileSystem.makedirs`.


| Parameter | Type |
|-|-|
| `path` |  |
| `exist_ok` |  |

#### modified()

```python
def modified(
    path,
)
```
Return the modified timestamp of a file as a datetime.datetime


| Parameter | Type |
|-|-|
| `path` |  |

#### move()

```python
def move(
    path1,
    path2,
    kwargs,
)
```
Alias of `AbstractFileSystem.mv`.


| Parameter | Type |
|-|-|
| `path1` |  |
| `path2` |  |
| `kwargs` | ``**kwargs`` |

#### mv()

```python
def mv(
    path1,
    path2,
    recursive,
    maxdepth,
    kwargs,
)
```
Move file(s) from one location to another


| Parameter | Type |
|-|-|
| `path1` |  |
| `path2` |  |
| `recursive` |  |
| `maxdepth` |  |
| `kwargs` | ``**kwargs`` |

#### open()

```python
def open(
    path,
    mode,
    block_size,
    cache_options,
    compression,
    kwargs,
)
```
Return a file-like object from the filesystem

The resultant instance must function correctly in a context ``with``
block.

Parameters
----------
path: str
    Target file
mode: str like 'rb', 'w'
    See builtin ``open()``
    Mode "x" (exclusive write) may be implemented by the backend. Even if
    it is, whether  it is checked up front or on commit, and whether it is
    atomic is implementation-dependent.
block_size: int
    Some indication of buffering - this is a value in bytes
cache_options : dict, optional
    Extra arguments to pass through to the cache.
compression: string or None
    If given, open file using compression codec. Can either be a compression
    name (a key in ``fsspec.compression.compr``) or "infer" to guess the
    compression from the filename suffix.
encoding, errors, newline: passed on to TextIOWrapper for text mode


| Parameter | Type |
|-|-|
| `path` |  |
| `mode` |  |
| `block_size` |  |
| `cache_options` |  |
| `compression` |  |
| `kwargs` | ``**kwargs`` |

#### open_async()

```python
def open_async(
    path: str,
    mode,
    kwargs,
) -> fsspec.asyn.AbstractAsyncStreamedFile
```
| Parameter | Type |
|-|-|
| `path` | `str` |
| `mode` |  |
| `kwargs` | ``**kwargs`` |

#### pipe()

```python
def pipe(
    path,
    value,
    kwargs,
)
```
Put value into path

(counterpart to ``cat``)

Parameters
----------
path: string or dict(str, bytes)
    If a string, a single remote location to put ``value`` bytes; if a dict,
    a mapping of {path: bytesvalue}.
value: bytes, optional
    If using a single path, these are the bytes to put there. Ignored if
    ``path`` is a dict


| Parameter | Type |
|-|-|
| `path` |  |
| `value` |  |
| `kwargs` | ``**kwargs`` |

#### pipe_file()

```python
def pipe_file(
    path,
    value,
    mode,
    kwargs,
)
```
Set the bytes of given file


| Parameter | Type |
|-|-|
| `path` |  |
| `value` |  |
| `mode` |  |
| `kwargs` | ``**kwargs`` |

#### put()

```python
def put(
    lpath,
    rpath,
    recursive,
    callback,
    maxdepth,
    kwargs,
)
```
Copy file(s) from local.

Copies a specific file or tree of files (if recursive=True). If rpath
ends with a "/", it will be assumed to be a directory, and target files
will go within.

Calls put_file for each source.


| Parameter | Type |
|-|-|
| `lpath` |  |
| `rpath` |  |
| `recursive` |  |
| `callback` |  |
| `maxdepth` |  |
| `kwargs` | ``**kwargs`` |

#### put_file()

```python
def put_file(
    lpath,
    rpath,
    callback,
    mode,
    kwargs,
)
```
Copy single file to remote


| Parameter | Type |
|-|-|
| `lpath` |  |
| `rpath` |  |
| `callback` |  |
| `mode` |  |
| `kwargs` | ``**kwargs`` |

#### read_block()

```python
def read_block(
    fn,
    offset,
    length,
    delimiter,
)
```
Read a block of bytes from

Starting at ``offset`` of the file, read ``length`` bytes.  If
``delimiter`` is set then we ensure that the read starts and stops at
delimiter boundaries that follow the locations ``offset`` and ``offset
+ length``.  If ``offset`` is zero then we start at zero.  The
bytestring returned WILL include the end delimiter string.

If offset+length is beyond the eof, reads to eof.

Parameters
----------
fn: string
    Path to filename
offset: int
    Byte offset to start read
length: int
    Number of bytes to read. If None, read to end.
delimiter: bytes (optional)
    Ensure reading starts and stops at delimiter bytestring

Examples
--------
>>> fs.read_block('data/file.csv', 0, 13)  # doctest: +SKIP
b'Alice, 100\nBo'
>>> fs.read_block('data/file.csv', 0, 13, delimiter=b'\n')  # doctest: +SKIP
b'Alice, 100\nBob, 200\n'

Use ``length=None`` to read to the end of the file.
>>> fs.read_block('data/file.csv', 0, None, delimiter=b'\n')  # doctest: +SKIP
b'Alice, 100\nBob, 200\nCharlie, 300'

See Also
--------
:func:`fsspec.utils.read_block`


| Parameter | Type |
|-|-|
| `fn` |  |
| `offset` |  |
| `length` |  |
| `delimiter` |  |

#### read_bytes()

```python
def read_bytes(
    path,
    start,
    end,
    kwargs,
)
```
Alias of `AbstractFileSystem.cat_file`.


| Parameter | Type |
|-|-|
| `path` |  |
| `start` |  |
| `end` |  |
| `kwargs` | ``**kwargs`` |

#### read_text()

```python
def read_text(
    path,
    encoding,
    errors,
    newline,
    kwargs,
)
```
Get the contents of the file as a string.

Parameters
----------
path: str
    URL of file on this filesystems
encoding, errors, newline: same as `open`.


| Parameter | Type |
|-|-|
| `path` |  |
| `encoding` |  |
| `errors` |  |
| `newline` |  |
| `kwargs` | ``**kwargs`` |

#### rename()

```python
def rename(
    path1,
    path2,
    kwargs,
)
```
Alias of `AbstractFileSystem.mv`.


| Parameter | Type |
|-|-|
| `path1` |  |
| `path2` |  |
| `kwargs` | ``**kwargs`` |

#### rm()

```python
def rm(
    path,
    recursive,
    maxdepth,
)
```
Delete files.

Parameters
----------
path: str or list of str
    File(s) to delete.
recursive: bool
    If file(s) are directories, recursively delete contents and then
    also remove the directory
maxdepth: int or None
    Depth to pass to walk for finding files to delete, if recursive.
    If None, there will be no limit and infinite recursion may be
    possible.


| Parameter | Type |
|-|-|
| `path` |  |
| `recursive` |  |
| `maxdepth` |  |

#### rm_file()

```python
def rm_file(
    path,
)
```
Delete a file


| Parameter | Type |
|-|-|
| `path` |  |

#### rmdir()

```python
def rmdir(
    path,
)
```
Remove a directory, if empty


| Parameter | Type |
|-|-|
| `path` |  |

#### sign()

```python
def sign(
    path,
    expiration,
    kwargs,
)
```
Create a signed URL representing the given path

Some implementations allow temporary URLs to be generated, as a
way of delegating credentials.

Parameters
----------
path : str
     The path on the filesystem
expiration : int
    Number of seconds to enable the URL for (if supported)

Returns
-------
URL : str
    The signed URL

Raises
------
NotImplementedError : if method is not implemented for a filesystem


| Parameter | Type |
|-|-|
| `path` |  |
| `expiration` |  |
| `kwargs` | ``**kwargs`` |

#### size()

```python
def size(
    path,
)
```
Size in bytes of file


| Parameter | Type |
|-|-|
| `path` |  |

#### sizes()

```python
def sizes(
    paths,
)
```
Size in bytes of each file in a list of paths


| Parameter | Type |
|-|-|
| `paths` |  |

#### start_transaction()

```python
def start_transaction()
```
Begin write transaction for deferring files, non-context version


#### stat()

```python
def stat(
    path,
    kwargs,
)
```
Alias of `AbstractFileSystem.info`.


| Parameter | Type |
|-|-|
| `path` |  |
| `kwargs` | ``**kwargs`` |

#### tail()

```python
def tail(
    path,
    size,
)
```
Get the last ``size`` bytes from file


| Parameter | Type |
|-|-|
| `path` |  |
| `size` |  |

#### to_dict()

```python
def to_dict(
    include_password: bool,
) -> dict[str, Any]
```
JSON-serializable dictionary representation of this filesystem instance.

Parameters
----------
include_password: bool, default True
    Whether to include the password (if any) in the output.

Returns
-------
Dictionary with keys ``cls`` (the python location of this class),
protocol (text name of this class's protocol, first one in case of
multiple), ``args`` (positional args, usually empty), and all other
keyword arguments as their own keys.

Warnings
--------
Serialized filesystems may contain sensitive information which have been
passed to the constructor, such as passwords and tokens. Make sure you
store and send them in a secure environment!


| Parameter | Type |
|-|-|
| `include_password` | `bool` |

#### to_json()

```python
def to_json(
    include_password: bool,
) -> str
```
JSON representation of this filesystem instance.

Parameters
----------
include_password: bool, default True
    Whether to include the password (if any) in the output.

Returns
-------
JSON string with keys ``cls`` (the python location of this class),
protocol (text name of this class's protocol, first one in case of
multiple), ``args`` (positional args, usually empty), and all other
keyword arguments as their own keys.

Warnings
--------
Serialized filesystems may contain sensitive information which have been
passed to the constructor, such as passwords and tokens. Make sure you
store and send them in a secure environment!


| Parameter | Type |
|-|-|
| `include_password` | `bool` |

#### touch()

```python
def touch(
    path,
    truncate,
    kwargs,
)
```
Create empty file, or update timestamp

Parameters
----------
path: str
    file location
truncate: bool
    If True, always set file size to 0; if False, update timestamp and
    leave file unchanged, if backend allows this


| Parameter | Type |
|-|-|
| `path` |  |
| `truncate` |  |
| `kwargs` | ``**kwargs`` |

#### tree()

```python
def tree(
    path: str,
    recursion_limit: int,
    max_display: int,
    display_size: bool,
    prefix: str,
    is_last: bool,
    first: bool,
    indent_size: int,
) -> str
```
Return a tree-like structure of the filesystem starting from the given path as a string.

Parameters
----------
    path: Root path to start traversal from
    recursion_limit: Maximum depth of directory traversal
    max_display: Maximum number of items to display per directory
    display_size: Whether to display file sizes
    prefix: Current line prefix for visual tree structure
    is_last: Whether current item is last in its level
    first: Whether this is the first call (displays root path)
    indent_size: Number of spaces by indent

Returns
-------
    str: A string representing the tree structure.

Example
-------
    >>> from fsspec import filesystem

    >>> fs = filesystem('ftp', host='test.rebex.net', user='demo', password='password')
    >>> tree = fs.tree(display_size=True, recursion_limit=3, indent_size=8, max_display=10)
    >>> print(tree)


| Parameter | Type |
|-|-|
| `path` | `str` |
| `recursion_limit` | `int` |
| `max_display` | `int` |
| `display_size` | `bool` |
| `prefix` | `str` |
| `is_last` | `bool` |
| `first` | `bool` |
| `indent_size` | `int` |

#### ukey()

```python
def ukey(
    path,
)
```
Hash of file properties, to tell if it has changed


| Parameter | Type |
|-|-|
| `path` |  |

#### unstrip_protocol()

```python
def unstrip_protocol(
    name: str,
) -> str
```
Format FS-specific path to generic, including protocol


| Parameter | Type |
|-|-|
| `name` | `str` |

#### upload()

```python
def upload(
    lpath,
    rpath,
    recursive,
    kwargs,
)
```
Alias of `AbstractFileSystem.put`.


| Parameter | Type |
|-|-|
| `lpath` |  |
| `rpath` |  |
| `recursive` |  |
| `kwargs` | ``**kwargs`` |

#### walk()

```python
def walk(
    path,
    maxdepth,
    topdown,
    on_error,
    kwargs,
)
```
Return all files under the given path.

List all files, recursing into subdirectories; output is iterator-style,
like ``os.walk()``. For a simple list of files, ``find()`` is available.

When topdown is True, the caller can modify the dirnames list in-place (perhaps
using del or slice assignment), and walk() will
only recurse into the subdirectories whose names remain in dirnames;
this can be used to prune the search, impose a specific order of visiting,
or even to inform walk() about directories the caller creates or renames before
it resumes walk() again.
Modifying dirnames when topdown is False has no effect. (see os.walk)

Note that the "files" outputted will include anything that is not
a directory, such as links.

Parameters
----------
path: str
    Root to recurse into
maxdepth: int
    Maximum recursion depth. None means limitless, but not recommended
    on link-based file-systems.
topdown: bool (True)
    Whether to walk the directory tree from the top downwards or from
    the bottom upwards.
on_error: "omit", "raise", a callable
    if omit (default), path with exception will simply be empty;
    If raise, an underlying exception will be raised;
    if callable, it will be called with a single OSError instance as argument
kwargs: passed to ``ls``


| Parameter | Type |
|-|-|
| `path` |  |
| `maxdepth` |  |
| `topdown` |  |
| `on_error` |  |
| `kwargs` | ``**kwargs`` |

#### write_bytes()

```python
def write_bytes(
    path,
    value,
    kwargs,
)
```
Alias of `AbstractFileSystem.pipe_file`.


| Parameter | Type |
|-|-|
| `path` |  |
| `value` |  |
| `kwargs` | ``**kwargs`` |

#### write_text()

```python
def write_text(
    path,
    value,
    encoding,
    errors,
    newline,
    kwargs,
)
```
Write the text to the given file.

An existing file will be overwritten.

Parameters
----------
path: str
    URL of file on this filesystems
value: str
    Text to write.
encoding, errors, newline: same as `open`.


| Parameter | Type |
|-|-|
| `path` |  |
| `value` |  |
| `encoding` |  |
| `errors` |  |
| `newline` |  |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `fsid` |  | {{< multiline >}}Persistent filesystem id that can be used to compare filesystems
across sessions.
{{< /multiline >}} |
| `loop` |  |  |
| `transaction` |  | {{< multiline >}}A context within which files are committed together upon exit

Requires the file class to implement `.commit()` and `.discard()`
for the normal and exception cases.
{{< /multiline >}} |

