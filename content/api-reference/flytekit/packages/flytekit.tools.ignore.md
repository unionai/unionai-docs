---
title: flytekit.tools.ignore
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.tools.ignore

## Directory

### Classes

| Class | Description |
|-|-|
| [`ABC`](.././flytekit.tools.ignore#flytekittoolsignoreabc) | Helper class that provides a standard way to create an ABC using. |
| [`DockerIgnore`](.././flytekit.tools.ignore#flytekittoolsignoredockerignore) | Uses docker-py's PatternMatcher to check whether a path is ignored. |
| [`FlyteIgnore`](.././flytekit.tools.ignore#flytekittoolsignoreflyteignore) | Uses a . |
| [`GitIgnore`](.././flytekit.tools.ignore#flytekittoolsignoregitignore) | Uses git cli (if available) to list all ignored files and compare with those. |
| [`Ignore`](.././flytekit.tools.ignore#flytekittoolsignoreignore) | Base for Ignores, implements core logic. |
| [`IgnoreGroup`](.././flytekit.tools.ignore#flytekittoolsignoreignoregroup) | Groups multiple Ignores and checks a path against them. |
| [`Path`](.././flytekit.tools.ignore#flytekittoolsignorepath) | PurePath subclass that can make system calls. |
| [`PatternMatcher`](.././flytekit.tools.ignore#flytekittoolsignorepatternmatcher) |  |
| [`StandardIgnore`](.././flytekit.tools.ignore#flytekittoolsignorestandardignore) | Retains the standard ignore functionality that previously existed. |

### Methods

| Method | Description |
|-|-|
| [`abstractmethod()`](#abstractmethod) | A decorator indicating abstract methods. |
| [`fnmatch()`](#fnmatch) | Test whether FILENAME matches PATTERN. |
| [`which()`](#which) | Given a command, mode, and a PATH string, return the path which. |


### Variables

| Property | Type | Description |
|-|-|-|
| `STANDARD_IGNORE_PATTERNS` | `list` |  |
| `logger` | `Logger` |  |

## Methods

#### abstractmethod()

```python
def abstractmethod(
    funcobj,
)
```
A decorator indicating abstract methods.

Requires that the metaclass is ABCMeta or derived from it.  A
class that has a metaclass derived from ABCMeta cannot be
instantiated unless all of its abstract methods are overridden.
The abstract methods can be called using any of the normal
'super' call mechanisms.  abstractmethod() may be used to declare
abstract methods for properties and descriptors.

Usage:

class C(metaclass=ABCMeta):
@abstractmethod
def my_abstract_method(self, arg1, arg2, argN):
...


| Parameter | Type |
|-|-|
| `funcobj` |  |

#### fnmatch()

```python
def fnmatch(
    name,
    pat,
)
```
Test whether FILENAME matches PATTERN.

Patterns are Unix shell style:

*       matches everything
?       matches any single character
[seq]   matches any character in seq
[!seq]  matches any char not in seq

An initial period in FILENAME is not special.
Both FILENAME and PATTERN are first case-normalized
if the operating system requires it.
If you don't want this, use fnmatchcase(FILENAME, PATTERN).


| Parameter | Type |
|-|-|
| `name` |  |
| `pat` |  |

#### which()

```python
def which(
    cmd,
    mode,
    path,
)
```
Given a command, mode, and a PATH string, return the path which
conforms to the given mode on the PATH, or None if there is no such
file.

`mode` defaults to os.F_OK | os.X_OK. `path` defaults to the result
of os.environ.get("PATH"), or can be overridden with a custom search
path.


| Parameter | Type |
|-|-|
| `cmd` |  |
| `mode` |  |
| `path` |  |

## flytekit.tools.ignore.ABC

Helper class that provides a standard way to create an ABC using
inheritance.


## flytekit.tools.ignore.DockerIgnore

Uses docker-py's PatternMatcher to check whether a path is ignored.


```python
class DockerIgnore(
    root: pathlib._local.Path,
)
```
| Parameter | Type |
|-|-|
| `root` | `pathlib._local.Path` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) |  |
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

#### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
) -> typing.Optional[tarfile.TarInfo]
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

## flytekit.tools.ignore.FlyteIgnore

Uses a .flyteignore file to determine ignored files.


```python
class FlyteIgnore(
    root: pathlib._local.Path,
)
```
| Parameter | Type |
|-|-|
| `root` | `pathlib._local.Path` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) |  |
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

#### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
) -> typing.Optional[tarfile.TarInfo]
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

## flytekit.tools.ignore.GitIgnore

Uses git cli (if available) to list all ignored files and compare with those.


```python
class GitIgnore(
    root: pathlib._local.Path,
)
```
| Parameter | Type |
|-|-|
| `root` | `pathlib._local.Path` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) |  |
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

#### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
) -> typing.Optional[tarfile.TarInfo]
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

## flytekit.tools.ignore.Ignore

Base for Ignores, implements core logic. Children have to implement _is_ignored


```python
class Ignore(
    root: str,
)
```
| Parameter | Type |
|-|-|
| `root` | `str` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) |  |
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

#### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
) -> typing.Optional[tarfile.TarInfo]
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

## flytekit.tools.ignore.IgnoreGroup

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

## flytekit.tools.ignore.Path

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

## flytekit.tools.ignore.PatternMatcher

```python
class PatternMatcher(
    patterns,
)
```
| Parameter | Type |
|-|-|
| `patterns` |  |

### Methods

| Method | Description |
|-|-|
| [`matches()`](#matches) |  |
| [`walk()`](#walk) |  |


#### matches()

```python
def matches(
    filepath,
)
```
| Parameter | Type |
|-|-|
| `filepath` |  |

#### walk()

```python
def walk(
    root,
)
```
| Parameter | Type |
|-|-|
| `root` |  |

## flytekit.tools.ignore.StandardIgnore

Retains the standard ignore functionality that previously existed. Could in theory
by fed with custom ignore patterns from cli.


```python
class StandardIgnore(
    root: pathlib._local.Path,
    patterns: typing.Optional[typing.List[str]],
)
```
| Parameter | Type |
|-|-|
| `root` | `pathlib._local.Path` |
| `patterns` | `typing.Optional[typing.List[str]]` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) |  |
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

#### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
) -> typing.Optional[tarfile.TarInfo]
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

