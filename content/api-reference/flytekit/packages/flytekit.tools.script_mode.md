---
title: flytekit.tools.script_mode
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.tools.script_mode

## Directory

### Classes

| Class | Description |
|-|-|
| [`CopyFileDetection`](.././flytekit.tools.script_mode#flytekittoolsscript_modecopyfiledetection) | Create a collection of name/value pairs. |
| [`IgnoreGroup`](.././flytekit.tools.script_mode#flytekittoolsscript_modeignoregroup) | Groups multiple Ignores and checks a path against them. |
| [`ModuleType`](.././flytekit.tools.script_mode#flytekittoolsscript_modemoduletype) | Create a module object. |
| [`Path`](.././flytekit.tools.script_mode#flytekittoolsscript_modepath) | PurePath subclass that can make system calls. |
| [`datetime`](.././flytekit.tools.script_mode#flytekittoolsscript_modedatetime) | datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]]). |
| [`timezone`](.././flytekit.tools.script_mode#flytekittoolsscript_modetimezone) | Fixed offset from UTC implementation of tzinfo. |

### Methods

| Method | Description |
|-|-|
| [`_file_is_in_directory()`](#_file_is_in_directory) | Return True if file is in directory and in its children. |
| [`_filehash_update()`](#_filehash_update) |  |
| [`_find_project_root()`](#_find_project_root) | Find the root of the project. |
| [`_pathhash_update()`](#_pathhash_update) |  |
| [`add_imported_modules_from_source()`](#add_imported_modules_from_source) | Copies modules into destination that are in modules. |
| [`compress_scripts()`](#compress_scripts) | Compresses the single script while maintaining the folder structure for that file. |
| [`get_all_modules()`](#get_all_modules) | Import python file with module_name in source_path and return all modules. |
| [`list_all_files()`](#list_all_files) |  |
| [`list_imported_modules_as_files()`](#list_imported_modules_as_files) | Copies modules into destination that are in modules. |
| [`lru_cache()`](#lru_cache) | Least-recently-used cache decorator. |
| [`ls_files()`](#ls_files) | user_modules_and_packages is a list of the Python modules and packages, expressed as absolute paths, that the. |
| [`tar_strip_file_attributes()`](#tar_strip_file_attributes) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `EXCLUDE_DIRS` | `set` |  |
| `annotations` | `_Feature` |  |
| `logger` | `Logger` |  |

## Methods

#### _file_is_in_directory()

```python
def _file_is_in_directory(
    file: str,
    directory: str,
) -> bool
```
Return True if file is in directory and in its children.


| Parameter | Type |
|-|-|
| `file` | `str` |
| `directory` | `str` |

#### _filehash_update()

```python
def _filehash_update(
    path: Union[os.PathLike, str],
    hasher: hashlib._Hash,
)
```
| Parameter | Type |
|-|-|
| `path` | `Union[os.PathLike, str]` |
| `hasher` | `hashlib._Hash` |

#### _find_project_root()

```python
def _find_project_root(
    source_path,
) -> str
```
Find the root of the project.
The root of the project is considered to be the first ancestor from source_path that does
not contain a __init__.py file.

N.B.: This assumption only holds for regular packages (as opposed to namespace packages)


| Parameter | Type |
|-|-|
| `source_path` |  |

#### _pathhash_update()

```python
def _pathhash_update(
    path: Union[os.PathLike, str],
    hasher: hashlib._Hash,
)
```
| Parameter | Type |
|-|-|
| `path` | `Union[os.PathLike, str]` |
| `hasher` | `hashlib._Hash` |

#### add_imported_modules_from_source()

```python
def add_imported_modules_from_source(
    source_path: str,
    destination: str,
    modules: List[ModuleType],
)
```
Copies modules into destination that are in modules. The module files are copied only if:

1. Not a site-packages. These are installed packages and not user files.
2. Not in the sys.base_prefix or sys.prefix. These are also installed and not user files.
3. Does not share a common path with the source_path.


| Parameter | Type |
|-|-|
| `source_path` | `str` |
| `destination` | `str` |
| `modules` | `List[ModuleType]` |

#### compress_scripts()

```python
def compress_scripts(
    source_path: str,
    destination: str,
    modules: List[ModuleType],
)
```
Compresses the single script while maintaining the folder structure for that file.

For example, given the follow file structure:
.
├── flyte
│   ├── __init__.py
│   └── workflows
│       ├── example.py
│       ├── another_example.py
│       ├── yet_another_example.py
│       ├── unused_example.py
│       └── __init__.py

Let's say you want to compress `example.py` imports `another_example.py`. And `another_example.py`
imports on `yet_another_example.py`. This will  produce a tar file that contains only that
file alongside with the folder structure, i.e.:

.
├── flyte
│   ├── __init__.py
│   └── workflows
│       ├── example.py
│       ├── another_example.py
│       ├── yet_another_example.py
│       └── __init__.py


| Parameter | Type |
|-|-|
| `source_path` | `str` |
| `destination` | `str` |
| `modules` | `List[ModuleType]` |

#### get_all_modules()

```python
def get_all_modules(
    source_path: str,
    module_name: Optional[str],
) -> List[ModuleType]
```
Import python file with module_name in source_path and return all modules.


| Parameter | Type |
|-|-|
| `source_path` | `str` |
| `module_name` | `Optional[str]` |

#### list_all_files()

```python
def list_all_files(
    source_path: str,
    deref_symlinks,
    ignore_group: Optional[IgnoreGroup],
) -> List[str]
```
| Parameter | Type |
|-|-|
| `source_path` | `str` |
| `deref_symlinks` |  |
| `ignore_group` | `Optional[IgnoreGroup]` |

#### list_imported_modules_as_files()

```python
def list_imported_modules_as_files(
    source_path: str,
    modules: List[ModuleType],
) -> List[str]
```
Copies modules into destination that are in modules. The module files are copied only if:

1. Not a site-packages. These are installed packages and not user files.
2. Not in the sys.base_prefix or sys.prefix. These are also installed and not user files.
3. Does not share a common path with the source_path.


| Parameter | Type |
|-|-|
| `source_path` | `str` |
| `modules` | `List[ModuleType]` |

#### lru_cache()

```python
def lru_cache(
    maxsize,
    typed,
)
```
Least-recently-used cache decorator.

If *maxsize* is set to None, the LRU features are disabled and the cache
can grow without bound.

If *typed* is True, arguments of different types will be cached separately.
For example, f(decimal.Decimal("3.0")) and f(3.0) will be treated as
distinct calls with distinct results. Some types such as str and int may
be cached separately even when typed is false.

Arguments to the cached function must be hashable.

View the cache statistics named tuple (hits, misses, maxsize, currsize)
with f.cache_info().  Clear the cache and statistics with f.cache_clear().
Access the underlying function with f.__wrapped__.

See:  https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)


| Parameter | Type |
|-|-|
| `maxsize` |  |
| `typed` |  |

#### ls_files()

```python
def ls_files(
    source_path: str,
    copy_file_detection: CopyFileDetection,
    deref_symlinks: bool,
    ignore_group: Optional[IgnoreGroup],
) -> Tuple[List[str], str]
```
user_modules_and_packages is a list of the Python modules and packages, expressed as absolute paths, that the
user has run this pyflyte command with. For pyflyte run for instance, this is just a list of one.
This is used for two reasons.
- Everything in this list needs to be returned. Files are returned and folders are walked.
- A common source path is derived from this is, which is just the common folder that contains everything in the
list. For ex. if you do
$ pyflyte --pkgs a.b,a.c package
Then the common root is just the folder a/. The modules list is filtered against this root. Only files
representing modules under this root are included

If the copy enum is set to loaded_modules, then the loaded sys modules will be used.


| Parameter | Type |
|-|-|
| `source_path` | `str` |
| `copy_file_detection` | `CopyFileDetection` |
| `deref_symlinks` | `bool` |
| `ignore_group` | `Optional[IgnoreGroup]` |

#### tar_strip_file_attributes()

```python
def tar_strip_file_attributes(
    tar_info: tarfile.TarInfo,
) -> tarfile.TarInfo
```
| Parameter | Type |
|-|-|
| `tar_info` | `tarfile.TarInfo` |

## flytekit.tools.script_mode.CopyFileDetection

Create a collection of name/value pairs.

Example enumeration:

>>> class Color(Enum):
...     RED = 1
...     BLUE = 2
...     GREEN = 3

Access them by:

- attribute access:

>>> Color.RED
<Color.RED: 1>

- value lookup:

>>> Color(1)
<Color.RED: 1>

- name lookup:

>>> Color['RED']
<Color.RED: 1>

Enumerations can be iterated over, and know how many members they have:

>>> len(Color)
3

>>> list(Color)
[<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

Methods can be added to enumerations, and members can have their own
attributes -- see the documentation for details.


## flytekit.tools.script_mode.IgnoreGroup

Groups multiple Ignores and checks a path against them. A file is ignored if any
Ignore considers it ignored.


```python
class IgnoreGroup(
    root: str,
    ignores: typing.List[typing.Type[flytekit.tools.ignore.Ignore]],
)
```
| Parameter | Type |
|-|-|
| `root` | `str` |
| `ignores` | `typing.List[typing.Type[flytekit.tools.ignore.Ignore]]` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) |  |
| [`list_ignored()`](#list_ignored) |  |
| [`tar_filter()`](#tar_filter) |  |


#### is_ignored()

```python
def is_ignored(
    path: str,
) -> bool
```
| Parameter | Type |
|-|-|
| `path` | `str` |

#### list_ignored()

```python
def list_ignored()
```
#### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
) -> typing.Optional[tarfile.TarInfo]
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

## flytekit.tools.script_mode.ModuleType

Create a module object.

The name must be a string; the optional doc argument can have any type.


## flytekit.tools.script_mode.Path

PurePath subclass that can make system calls.

Path represents a filesystem path but unlike PurePath, also offers
methods to do system calls on path objects. Depending on your system,
instantiating a Path will return either a PosixPath or a WindowsPath
object. You can also instantiate a PosixPath or WindowsPath directly,
but cannot instantiate a WindowsPath on a POSIX system or vice versa.


```python
class Path(
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`absolute()`](#absolute) | Return an absolute version of this path. |
| [`as_posix()`](#as_posix) | Return the string representation of the path with forward (/). |
| [`as_uri()`](#as_uri) | Return the path as a URI. |
| [`chmod()`](#chmod) | Change the permissions of the path, like os. |
| [`cwd()`](#cwd) | Return a new path pointing to the current working directory. |
| [`exists()`](#exists) | Whether this path exists. |
| [`expanduser()`](#expanduser) | Return a new path with expanded ~ and ~user constructs. |
| [`from_uri()`](#from_uri) | Return a new path from the given 'file' URI. |
| [`full_match()`](#full_match) | Return True if this path matches the given glob-style pattern. |
| [`glob()`](#glob) | Iterate over this subtree and yield all existing files (of any. |
| [`group()`](#group) | Return the group name of the file gid. |
| [`hardlink_to()`](#hardlink_to) | Make this path a hard link pointing to the same file as *target*. |
| [`home()`](#home) | Return a new path pointing to expanduser('~'). |
| [`is_absolute()`](#is_absolute) | True if the path is absolute (has both a root and, if applicable,. |
| [`is_block_device()`](#is_block_device) | Whether this path is a block device. |
| [`is_char_device()`](#is_char_device) | Whether this path is a character device. |
| [`is_dir()`](#is_dir) | Whether this path is a directory. |
| [`is_fifo()`](#is_fifo) | Whether this path is a FIFO. |
| [`is_file()`](#is_file) | Whether this path is a regular file (also True for symlinks pointing. |
| [`is_junction()`](#is_junction) | Whether this path is a junction. |
| [`is_mount()`](#is_mount) | Check if this path is a mount point. |
| [`is_relative_to()`](#is_relative_to) | Return True if the path is relative to another path or False. |
| [`is_reserved()`](#is_reserved) | Return True if the path contains one of the special names reserved. |
| [`is_socket()`](#is_socket) | Whether this path is a socket. |
| [`is_symlink()`](#is_symlink) | Whether this path is a symbolic link. |
| [`iterdir()`](#iterdir) | Yield path objects of the directory contents. |
| [`joinpath()`](#joinpath) | Combine this path with one or several arguments, and return a. |
| [`lchmod()`](#lchmod) | Like chmod(), except if the path points to a symlink, the symlink's. |
| [`lstat()`](#lstat) | Like stat(), except if the path points to a symlink, the symlink's. |
| [`match()`](#match) | Return True if this path matches the given pattern. |
| [`mkdir()`](#mkdir) | Create a new directory at this given path. |
| [`open()`](#open) | Open the file pointed to by this path and return a file object, as. |
| [`owner()`](#owner) | Return the login name of the file owner. |
| [`read_bytes()`](#read_bytes) | Open the file in bytes mode, read it, and close the file. |
| [`read_text()`](#read_text) | Open the file in text mode, read it, and close the file. |
| [`readlink()`](#readlink) | Return the path to which the symbolic link points. |
| [`relative_to()`](#relative_to) | Return the relative path to another path identified by the passed. |
| [`rename()`](#rename) | Rename this path to the target path. |
| [`replace()`](#replace) | Rename this path to the target path, overwriting if that path exists. |
| [`resolve()`](#resolve) | Make the path absolute, resolving all symlinks on the way and also. |
| [`rglob()`](#rglob) | Recursively yield all existing files (of any kind, including. |
| [`rmdir()`](#rmdir) | Remove this directory. |
| [`samefile()`](#samefile) | Return whether other_path is the same or not as this file. |
| [`stat()`](#stat) | Return the result of the stat() system call on this path, like. |
| [`symlink_to()`](#symlink_to) | Make this path a symlink pointing to the target path. |
| [`touch()`](#touch) | Create this file with the given access mode, if it doesn't exist. |
| [`unlink()`](#unlink) | Remove this file or link. |
| [`walk()`](#walk) | Walk the directory tree from this directory, similar to os. |
| [`with_name()`](#with_name) | Return a new path with the file name changed. |
| [`with_segments()`](#with_segments) | Construct a new path object from any number of path-like objects. |
| [`with_stem()`](#with_stem) | Return a new path with the stem changed. |
| [`with_suffix()`](#with_suffix) | Return a new path with the file suffix changed. |
| [`write_bytes()`](#write_bytes) | Open the file in bytes mode, write to it, and close the file. |
| [`write_text()`](#write_text) | Open the file in text mode, write to it, and close the file. |


#### absolute()

```python
def absolute()
```
Return an absolute version of this path
No normalization or symlink resolution is performed.

Use resolve() to resolve symlinks and remove '..' segments.


#### as_posix()

```python
def as_posix()
```
Return the string representation of the path with forward (/)
slashes.


#### as_uri()

```python
def as_uri()
```
Return the path as a URI.


#### chmod()

```python
def chmod(
    mode,
    follow_symlinks,
)
```
Change the permissions of the path, like os.chmod().


| Parameter | Type |
|-|-|
| `mode` |  |
| `follow_symlinks` |  |

#### cwd()

```python
def cwd()
```
Return a new path pointing to the current working directory.


#### exists()

```python
def exists(
    follow_symlinks,
)
```
Whether this path exists.

This method normally follows symlinks; to check whether a symlink exists,
add the argument follow_symlinks=False.


| Parameter | Type |
|-|-|
| `follow_symlinks` |  |

#### expanduser()

```python
def expanduser()
```
Return a new path with expanded ~ and ~user constructs
(as returned by os.path.expanduser)


#### from_uri()

```python
def from_uri(
    uri,
)
```
Return a new path from the given 'file' URI.


| Parameter | Type |
|-|-|
| `uri` |  |

#### full_match()

```python
def full_match(
    pattern,
    case_sensitive,
)
```
Return True if this path matches the given glob-style pattern. The
pattern is matched against the entire path.


| Parameter | Type |
|-|-|
| `pattern` |  |
| `case_sensitive` |  |

#### glob()

```python
def glob(
    pattern,
    case_sensitive,
    recurse_symlinks,
)
```
Iterate over this subtree and yield all existing files (of any
kind, including directories) matching the given relative pattern.


| Parameter | Type |
|-|-|
| `pattern` |  |
| `case_sensitive` |  |
| `recurse_symlinks` |  |

#### group()

```python
def group(
    follow_symlinks,
)
```
Return the group name of the file gid.


| Parameter | Type |
|-|-|
| `follow_symlinks` |  |

#### hardlink_to()

```python
def hardlink_to(
    target,
)
```
Make this path a hard link pointing to the same file as *target*.

Note the order of arguments (self, target) is the reverse of os.link's.


| Parameter | Type |
|-|-|
| `target` |  |

#### home()

```python
def home()
```
Return a new path pointing to expanduser('~').



#### is_absolute()

```python
def is_absolute()
```
True if the path is absolute (has both a root and, if applicable,
a drive).


#### is_block_device()

```python
def is_block_device()
```
Whether this path is a block device.


#### is_char_device()

```python
def is_char_device()
```
Whether this path is a character device.


#### is_dir()

```python
def is_dir(
    follow_symlinks,
)
```
Whether this path is a directory.


| Parameter | Type |
|-|-|
| `follow_symlinks` |  |

#### is_fifo()

```python
def is_fifo()
```
Whether this path is a FIFO.


#### is_file()

```python
def is_file(
    follow_symlinks,
)
```
Whether this path is a regular file (also True for symlinks pointing
to regular files).


| Parameter | Type |
|-|-|
| `follow_symlinks` |  |

#### is_junction()

```python
def is_junction()
```
Whether this path is a junction.


#### is_mount()

```python
def is_mount()
```
Check if this path is a mount point


#### is_relative_to()

```python
def is_relative_to(
    other,
    _deprecated,
)
```
Return True if the path is relative to another path or False.



| Parameter | Type |
|-|-|
| `other` |  |
| `_deprecated` |  |

#### is_reserved()

```python
def is_reserved()
```
Return True if the path contains one of the special names reserved
by the system, if any.


#### is_socket()

```python
def is_socket()
```
Whether this path is a socket.


#### is_symlink()

```python
def is_symlink()
```
Whether this path is a symbolic link.


#### iterdir()

```python
def iterdir()
```
Yield path objects of the directory contents.

The children are yielded in arbitrary order, and the
special entries '.' and '..' are not included.


#### joinpath()

```python
def joinpath(
    pathsegments,
)
```
Combine this path with one or several arguments, and return a
new path representing either a subpath (if all arguments are relative
paths) or a totally different path (if one of the arguments is
anchored).


| Parameter | Type |
|-|-|
| `pathsegments` |  |

#### lchmod()

```python
def lchmod(
    mode,
)
```
Like chmod(), except if the path points to a symlink, the symlink's
permissions are changed, rather than its target's.


| Parameter | Type |
|-|-|
| `mode` |  |

#### lstat()

```python
def lstat()
```
Like stat(), except if the path points to a symlink, the symlink's
status information is returned, rather than its target's.


#### match()

```python
def match(
    path_pattern,
    case_sensitive,
)
```
Return True if this path matches the given pattern. If the pattern is
relative, matching is done from the right; otherwise, the entire path
is matched. The recursive wildcard '**' is *not* supported by this
method.


| Parameter | Type |
|-|-|
| `path_pattern` |  |
| `case_sensitive` |  |

#### mkdir()

```python
def mkdir(
    mode,
    parents,
    exist_ok,
)
```
Create a new directory at this given path.


| Parameter | Type |
|-|-|
| `mode` |  |
| `parents` |  |
| `exist_ok` |  |

#### open()

```python
def open(
    mode,
    buffering,
    encoding,
    errors,
    newline,
)
```
Open the file pointed to by this path and return a file object, as
the built-in open() function does.


| Parameter | Type |
|-|-|
| `mode` |  |
| `buffering` |  |
| `encoding` |  |
| `errors` |  |
| `newline` |  |

#### owner()

```python
def owner(
    follow_symlinks,
)
```
Return the login name of the file owner.


| Parameter | Type |
|-|-|
| `follow_symlinks` |  |

#### read_bytes()

```python
def read_bytes()
```
Open the file in bytes mode, read it, and close the file.


#### read_text()

```python
def read_text(
    encoding,
    errors,
    newline,
)
```
Open the file in text mode, read it, and close the file.


| Parameter | Type |
|-|-|
| `encoding` |  |
| `errors` |  |
| `newline` |  |

#### readlink()

```python
def readlink()
```
Return the path to which the symbolic link points.


#### relative_to()

```python
def relative_to(
    other,
    _deprecated,
    walk_up,
)
```
Return the relative path to another path identified by the passed
arguments.  If the operation is not possible (because this is not
related to the other path), raise ValueError.

The *walk_up* parameter controls whether `..` may be used to resolve
the path.


| Parameter | Type |
|-|-|
| `other` |  |
| `_deprecated` |  |
| `walk_up` |  |

#### rename()

```python
def rename(
    target,
)
```
Rename this path to the target path.

The target path may be absolute or relative. Relative paths are
interpreted relative to the current working directory, *not* the
directory of the Path object.

Returns the new Path instance pointing to the target path.


| Parameter | Type |
|-|-|
| `target` |  |

#### replace()

```python
def replace(
    target,
)
```
Rename this path to the target path, overwriting if that path exists.

The target path may be absolute or relative. Relative paths are
interpreted relative to the current working directory, *not* the
directory of the Path object.

Returns the new Path instance pointing to the target path.


| Parameter | Type |
|-|-|
| `target` |  |

#### resolve()

```python
def resolve(
    strict,
)
```
Make the path absolute, resolving all symlinks on the way and also
normalizing it.


| Parameter | Type |
|-|-|
| `strict` |  |

#### rglob()

```python
def rglob(
    pattern,
    case_sensitive,
    recurse_symlinks,
)
```
Recursively yield all existing files (of any kind, including
directories) matching the given relative pattern, anywhere in
this subtree.


| Parameter | Type |
|-|-|
| `pattern` |  |
| `case_sensitive` |  |
| `recurse_symlinks` |  |

#### rmdir()

```python
def rmdir()
```
Remove this directory.  The directory must be empty.


#### samefile()

```python
def samefile(
    other_path,
)
```
Return whether other_path is the same or not as this file
(as returned by os.path.samefile()).


| Parameter | Type |
|-|-|
| `other_path` |  |

#### stat()

```python
def stat(
    follow_symlinks,
)
```
Return the result of the stat() system call on this path, like
os.stat() does.


| Parameter | Type |
|-|-|
| `follow_symlinks` |  |

#### symlink_to()

```python
def symlink_to(
    target,
    target_is_directory,
)
```
Make this path a symlink pointing to the target path.
Note the order of arguments (link, target) is the reverse of os.symlink.


| Parameter | Type |
|-|-|
| `target` |  |
| `target_is_directory` |  |

#### touch()

```python
def touch(
    mode,
    exist_ok,
)
```
Create this file with the given access mode, if it doesn't exist.


| Parameter | Type |
|-|-|
| `mode` |  |
| `exist_ok` |  |

#### unlink()

```python
def unlink(
    missing_ok,
)
```
Remove this file or link.
If the path is a directory, use rmdir() instead.


| Parameter | Type |
|-|-|
| `missing_ok` |  |

#### walk()

```python
def walk(
    top_down,
    on_error,
    follow_symlinks,
)
```
Walk the directory tree from this directory, similar to os.walk().


| Parameter | Type |
|-|-|
| `top_down` |  |
| `on_error` |  |
| `follow_symlinks` |  |

#### with_name()

```python
def with_name(
    name,
)
```
Return a new path with the file name changed.


| Parameter | Type |
|-|-|
| `name` |  |

#### with_segments()

```python
def with_segments(
    pathsegments,
)
```
Construct a new path object from any number of path-like objects.
Subclasses may override this method to customize how new path objects
are created from methods like `iterdir()`.


| Parameter | Type |
|-|-|
| `pathsegments` |  |

#### with_stem()

```python
def with_stem(
    stem,
)
```
Return a new path with the stem changed.


| Parameter | Type |
|-|-|
| `stem` |  |

#### with_suffix()

```python
def with_suffix(
    suffix,
)
```
Return a new path with the file suffix changed.  If the path
has no suffix, add given suffix.  If the given suffix is an empty
string, remove the suffix from the path.


| Parameter | Type |
|-|-|
| `suffix` |  |

#### write_bytes()

```python
def write_bytes(
    data,
)
```
Open the file in bytes mode, write to it, and close the file.


| Parameter | Type |
|-|-|
| `data` |  |

#### write_text()

```python
def write_text(
    data,
    encoding,
    errors,
    newline,
)
```
Open the file in text mode, write to it, and close the file.


| Parameter | Type |
|-|-|
| `data` |  |
| `encoding` |  |
| `errors` |  |
| `newline` |  |

### Properties

| Property | Type | Description |
|-|-|-|
| `anchor` |  | {{< multiline >}}The concatenation of the drive and root, or ''.
{{< /multiline >}} |
| `drive` |  | {{< multiline >}}The drive prefix (letter or UNC path), if any.
{{< /multiline >}} |
| `name` |  | {{< multiline >}}The final path component, if any.
{{< /multiline >}} |
| `parent` |  | {{< multiline >}}The logical parent of the path.
{{< /multiline >}} |
| `parents` |  | {{< multiline >}}A sequence of this path's logical parents.
{{< /multiline >}} |
| `parts` |  | {{< multiline >}}An object providing sequence-like access to the
components in the filesystem path.
{{< /multiline >}} |
| `root` |  | {{< multiline >}}The root of the path, if any.
{{< /multiline >}} |
| `stem` |  | {{< multiline >}}The final path component, minus its last suffix.
{{< /multiline >}} |
| `suffix` |  | {{< multiline >}}The final component's last suffix, if any.

This includes the leading period. For example: '.txt'
{{< /multiline >}} |
| `suffixes` |  | {{< multiline >}}A list of the final component's suffixes, if any.

These include the leading periods. For example: ['.tar', '.gz']
{{< /multiline >}} |

## flytekit.tools.script_mode.datetime

datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])

The year, month and day arguments are required. tzinfo may be None, or an
instance of a tzinfo subclass. The remaining arguments may be ints.


## flytekit.tools.script_mode.timezone

Fixed offset from UTC implementation of tzinfo.


