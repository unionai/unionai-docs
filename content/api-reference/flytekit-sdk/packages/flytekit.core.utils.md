---
title: flytekit.core.utils
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.utils

## Directory

### Classes

| Class | Description |
|-|-|
| [`ABC`](.././flytekit.core.utils#flytekitcoreutilsabc) | Helper class that provides a standard way to create an ABC using. |
| [`Any`](.././flytekit.core.utils#flytekitcoreutilsany) | Special type indicating an unconstrained type. |
| [`AutoDeletingTempDir`](.././flytekit.core.utils#flytekitcoreutilsautodeletingtempdir) | Creates a posix safe tempdir which is auto deleted once out of scope. |
| [`ClassDecorator`](.././flytekit.core.utils#flytekitcoreutilsclassdecorator) | Abstract class for class decorators. |
| [`Directory`](.././flytekit.core.utils#flytekitcoreutilsdirectory) | None. |
| [`Path`](.././flytekit.core.utils#flytekitcoreutilspath) | PurePath subclass that can make system calls. |
| [`PodTemplate`](.././flytekit.core.utils#flytekitcoreutilspodtemplate) | Custom PodTemplate specification for a Task. |
| [`ResourceSpec`](.././flytekit.core.utils#flytekitcoreutilsresourcespec) | None. |
| [`SerializationSettings`](.././flytekit.core.utils#flytekitcoreutilsserializationsettings) | These settings are provided while serializing a workflow and task, before registration. |
| [`timeit`](.././flytekit.core.utils#flytekitcoreutilstimeit) | A context manager and a decorator that measures the execution time of the wrapped code block or functions. |

## flytekit.core.utils.ABC

Helper class that provides a standard way to create an ABC using
inheritance.


## flytekit.core.utils.Any

Special type indicating an unconstrained type.

- Any is compatible with every type.
- Any assumed to have all methods.
- All values assumed to be instances of Any.

Note that all the above statements are true from the point of view of
static type checkers. At runtime, Any should not be used with instance
checks.


## flytekit.core.utils.AutoDeletingTempDir

Creates a posix safe tempdir which is auto deleted once out of scope


```python
def AutoDeletingTempDir(
    working_dir_prefix,
    tmp_dir,
    cleanup,
):
```
| Parameter | Type |
|-|-|
| `working_dir_prefix` |  |
| `tmp_dir` |  |
| `cleanup` |  |

### Methods

| Method | Description |
|-|-|
| [`force_cleanup()`](#force_cleanup) | None |
| [`get_named_tempfile()`](#get_named_tempfile) | None |
| [`list_dir()`](#list_dir) | The list of absolute filepaths for all immediate sub-paths |


#### force_cleanup()

```python
def force_cleanup()
```
#### get_named_tempfile()

```python
def get_named_tempfile(
    name,
):
```
| Parameter | Type |
|-|-|
| `name` |  |

#### list_dir()

```python
def list_dir()
```
The list of absolute filepaths for all immediate sub-paths


### Properties

| Property | Type | Description |
|-|-|-|
| name |  |  |

## flytekit.core.utils.ClassDecorator

Abstract class for class decorators.
We can attach config on the decorator class and use it in the upper level.


```python
def ClassDecorator(
    task_function,
    kwargs,
):
```
If the decorator is called with arguments, func will be None.
If the decorator is called without arguments, func will be function to be decorated.


| Parameter | Type |
|-|-|
| `task_function` |  |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`execute()`](#execute) | This method will be called when the decorated function is called |
| [`get_extra_config()`](#get_extra_config) | Get the config of the decorator |


#### execute()

```python
def execute(
    args,
    kwargs,
):
```
This method will be called when the decorated function is called.


| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### get_extra_config()

```python
def get_extra_config()
```
Get the config of the decorator.


## flytekit.core.utils.Directory

```python
def Directory(
    path,
):
```
| Parameter | Type |
|-|-|
| `path` |  |

### Methods

| Method | Description |
|-|-|
| [`list_dir()`](#list_dir) | The list of absolute filepaths for all immediate sub-paths |


#### list_dir()

```python
def list_dir()
```
The list of absolute filepaths for all immediate sub-paths


### Properties

| Property | Type | Description |
|-|-|-|
| name |  |  |

## flytekit.core.utils.Path

PurePath subclass that can make system calls.

Path represents a filesystem path but unlike PurePath, also offers
methods to do system calls on path objects. Depending on your system,
instantiating a Path will return either a PosixPath or a WindowsPath
object. You can also instantiate a PosixPath or WindowsPath directly,
but cannot instantiate a WindowsPath on a POSIX system or vice versa.


```python
def Path(
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`absolute()`](#absolute) | Return an absolute version of this path by prepending the current |
| [`as_posix()`](#as_posix) | Return the string representation of the path with forward (/) |
| [`as_uri()`](#as_uri) | Return the path as a 'file' URI |
| [`chmod()`](#chmod) | Change the permissions of the path, like os |
| [`cwd()`](#cwd) | Return a new path pointing to the current working directory |
| [`exists()`](#exists) | Whether this path exists |
| [`expanduser()`](#expanduser) | Return a new path with expanded ~ and ~user constructs |
| [`glob()`](#glob) | Iterate over this subtree and yield all existing files (of any |
| [`group()`](#group) | Return the group name of the file gid |
| [`hardlink_to()`](#hardlink_to) | Make this path a hard link pointing to the same file as *target* |
| [`home()`](#home) | Return a new path pointing to the user's home directory (as |
| [`is_absolute()`](#is_absolute) | True if the path is absolute (has both a root and, if applicable, |
| [`is_block_device()`](#is_block_device) | Whether this path is a block device |
| [`is_char_device()`](#is_char_device) | Whether this path is a character device |
| [`is_dir()`](#is_dir) | Whether this path is a directory |
| [`is_fifo()`](#is_fifo) | Whether this path is a FIFO |
| [`is_file()`](#is_file) | Whether this path is a regular file (also True for symlinks pointing |
| [`is_junction()`](#is_junction) | Whether this path is a junction |
| [`is_mount()`](#is_mount) | Check if this path is a mount point |
| [`is_relative_to()`](#is_relative_to) | Return True if the path is relative to another path or False |
| [`is_reserved()`](#is_reserved) | Return True if the path contains one of the special names reserved |
| [`is_socket()`](#is_socket) | Whether this path is a socket |
| [`is_symlink()`](#is_symlink) | Whether this path is a symbolic link |
| [`iterdir()`](#iterdir) | Yield path objects of the directory contents |
| [`joinpath()`](#joinpath) | Combine this path with one or several arguments, and return a |
| [`lchmod()`](#lchmod) | Like chmod(), except if the path points to a symlink, the symlink's |
| [`lstat()`](#lstat) | Like stat(), except if the path points to a symlink, the symlink's |
| [`match()`](#match) | Return True if this path matches the given pattern |
| [`mkdir()`](#mkdir) | Create a new directory at this given path |
| [`open()`](#open) | Open the file pointed to by this path and return a file object, as |
| [`owner()`](#owner) | Return the login name of the file owner |
| [`read_bytes()`](#read_bytes) | Open the file in bytes mode, read it, and close the file |
| [`read_text()`](#read_text) | Open the file in text mode, read it, and close the file |
| [`readlink()`](#readlink) | Return the path to which the symbolic link points |
| [`relative_to()`](#relative_to) | Return the relative path to another path identified by the passed |
| [`rename()`](#rename) | Rename this path to the target path |
| [`replace()`](#replace) | Rename this path to the target path, overwriting if that path exists |
| [`resolve()`](#resolve) | Make the path absolute, resolving all symlinks on the way and also |
| [`rglob()`](#rglob) | Recursively yield all existing files (of any kind, including |
| [`rmdir()`](#rmdir) | Remove this directory |
| [`samefile()`](#samefile) | Return whether other_path is the same or not as this file |
| [`stat()`](#stat) | Return the result of the stat() system call on this path, like |
| [`symlink_to()`](#symlink_to) | Make this path a symlink pointing to the target path |
| [`touch()`](#touch) | Create this file with the given access mode, if it doesn't exist |
| [`unlink()`](#unlink) | Remove this file or link |
| [`walk()`](#walk) | Walk the directory tree from this directory, similar to os |
| [`with_name()`](#with_name) | Return a new path with the file name changed |
| [`with_segments()`](#with_segments) | Construct a new path object from any number of path-like objects |
| [`with_stem()`](#with_stem) | Return a new path with the stem changed |
| [`with_suffix()`](#with_suffix) | Return a new path with the file suffix changed |
| [`write_bytes()`](#write_bytes) | Open the file in bytes mode, write to it, and close the file |
| [`write_text()`](#write_text) | Open the file in text mode, write to it, and close the file |


#### absolute()

```python
def absolute()
```
Return an absolute version of this path by prepending the current
working directory. No normalization or symlink resolution is performed.

Use resolve() to get the canonical path to a file.


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
Return the path as a 'file' URI.


#### chmod()

```python
def chmod(
    mode,
    follow_symlinks,
):
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
):
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


#### glob()

```python
def glob(
    pattern,
    case_sensitive,
):
```
Iterate over this subtree and yield all existing files (of any
kind, including directories) matching the given relative pattern.


| Parameter | Type |
|-|-|
| `pattern` |  |
| `case_sensitive` |  |

#### group()

```python
def group()
```
Return the group name of the file gid.


#### hardlink_to()

```python
def hardlink_to(
    target,
):
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
Return a new path pointing to the user's home directory (as
returned by os.path.expanduser('~')).


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
def is_dir()
```
Whether this path is a directory.


#### is_fifo()

```python
def is_fifo()
```
Whether this path is a FIFO.


#### is_file()

```python
def is_file()
```
Whether this path is a regular file (also True for symlinks pointing
to regular files).


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
):
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
):
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
):
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
):
```
Return True if this path matches the given pattern.


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
):
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
):
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
def owner()
```
Return the login name of the file owner.


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
):
```
Open the file in text mode, read it, and close the file.


| Parameter | Type |
|-|-|
| `encoding` |  |
| `errors` |  |

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
):
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
):
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
):
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
):
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
):
```
Recursively yield all existing files (of any kind, including
directories) matching the given relative pattern, anywhere in
this subtree.


| Parameter | Type |
|-|-|
| `pattern` |  |
| `case_sensitive` |  |

#### rmdir()

```python
def rmdir()
```
Remove this directory.  The directory must be empty.


#### samefile()

```python
def samefile(
    other_path,
):
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
):
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
):
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
):
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
):
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
):
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
):
```
Return a new path with the file name changed.


| Parameter | Type |
|-|-|
| `name` |  |

#### with_segments()

```python
def with_segments(
    pathsegments,
):
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
):
```
Return a new path with the stem changed.


| Parameter | Type |
|-|-|
| `stem` |  |

#### with_suffix()

```python
def with_suffix(
    suffix,
):
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
):
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
):
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
| anchor |  |  |
| drive |  |  |
| name |  |  |
| parent |  |  |
| parents |  |  |
| parts |  |  |
| root |  |  |
| stem |  |  |
| suffix |  |  |
| suffixes |  |  |

## flytekit.core.utils.PodTemplate

Custom PodTemplate specification for a Task.


```python
def PodTemplate(
    pod_spec: typing.Optional[ForwardRef('V1PodSpec')],
    primary_container_name: str,
    labels: typing.Optional[typing.Dict[str, str]],
    annotations: typing.Optional[typing.Dict[str, str]],
):
```
| Parameter | Type |
|-|-|
| `pod_spec` | `typing.Optional[ForwardRef('V1PodSpec')]` |
| `primary_container_name` | `str` |
| `labels` | `typing.Optional[typing.Dict[str, str]]` |
| `annotations` | `typing.Optional[typing.Dict[str, str]]` |

## flytekit.core.utils.ResourceSpec

```python
def ResourceSpec(
    requests: flytekit.core.resources.Resources,
    limits: flytekit.core.resources.Resources,
):
```
| Parameter | Type |
|-|-|
| `requests` | `flytekit.core.resources.Resources` |
| `limits` | `flytekit.core.resources.Resources` |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) | None |
| [`from_json()`](#from_json) | None |
| [`from_multiple_resource()`](#from_multiple_resource) | Convert Resources that represent both a requests and limits into a ResourceSpec |
| [`to_dict()`](#to_dict) | None |
| [`to_json()`](#to_json) | None |


#### from_dict()

```python
def from_dict(
    d,
    dialect,
):
```
| Parameter | Type |
|-|-|
| `d` |  |
| `dialect` |  |

#### from_json()

```python
def from_json(
    data: typing.Union[str, bytes, bytearray],
    decoder: collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]],
    from_dict_kwargs: typing.Any,
):
```
| Parameter | Type |
|-|-|
| `data` | `typing.Union[str, bytes, bytearray]` |
| `decoder` | `collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]]` |
| `from_dict_kwargs` | `typing.Any` |

#### from_multiple_resource()

```python
def from_multiple_resource(
    resource: flytekit.core.resources.Resources,
):
```
Convert Resources that represent both a requests and limits into a ResourceSpec.


| Parameter | Type |
|-|-|
| `resource` | `flytekit.core.resources.Resources` |

#### to_dict()

```python
def to_dict()
```
#### to_json()

```python
def to_json(
    encoder: collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]],
    to_dict_kwargs: typing.Any,
):
```
| Parameter | Type |
|-|-|
| `encoder` | `collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]]` |
| `to_dict_kwargs` | `typing.Any` |

## flytekit.core.utils.SerializationSettings

These settings are provided while serializing a workflow and task, before registration. This is required to get
runtime information at serialization time, as well as some defaults.

Attributes:
project (str): The project (if any) with which to register entities under.
domain (str): The domain (if any) with which to register entities under.
version (str): The version (if any) with which to register entities under.
image_config (ImageConfig): The image config used to define task container images.
env (Optional[Dict[str, str]]): Environment variables injected into task container definitions.
flytekit_virtualenv_root (Optional[str]):  During out of container serialize the absolute path of the flytekit
virtualenv at serialization time won't match the in-container value at execution time. This optional value
is used to provide the in-container virtualenv path
python_interpreter (Optional[str]): The python executable to use. This is used for spark tasks in out of
container execution.
entrypoint_settings (Optional[EntrypointSettings]): Information about the command, path and version of the
entrypoint program.
fast_serialization_settings (Optional[FastSerializationSettings]): If the code is being serialized so that it
can be fast registered (and thus omit building a Docker image) this object contains additional parameters
for serialization.
source_root (Optional[str]): The root directory of the source code.


```python
def SerializationSettings(
    image_config: ImageConfig,
    project: typing.Optional[str],
    domain: typing.Optional[str],
    version: typing.Optional[str],
    env: Optional[Dict[str, str]],
    git_repo: Optional[str],
    python_interpreter: str,
    flytekit_virtualenv_root: Optional[str],
    fast_serialization_settings: Optional[FastSerializationSettings],
    source_root: Optional[str],
):
```
| Parameter | Type |
|-|-|
| `image_config` | `ImageConfig` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `version` | `typing.Optional[str]` |
| `env` | `Optional[Dict[str, str]]` |
| `git_repo` | `Optional[str]` |
| `python_interpreter` | `str` |
| `flytekit_virtualenv_root` | `Optional[str]` |
| `fast_serialization_settings` | `Optional[FastSerializationSettings]` |
| `source_root` | `Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`default_entrypoint_settings()`](#default_entrypoint_settings) | Assumes the entrypoint is installed in a virtual-environment where the interpreter is |
| [`for_image()`](#for_image) | None |
| [`from_dict()`](#from_dict) | None |
| [`from_json()`](#from_json) | None |
| [`from_transport()`](#from_transport) | None |
| [`new_builder()`](#new_builder) | Creates a ``SerializationSettings |
| [`schema()`](#schema) | None |
| [`should_fast_serialize()`](#should_fast_serialize) | Whether or not the serialization settings specify that entities should be serialized for fast registration |
| [`to_dict()`](#to_dict) | None |
| [`to_json()`](#to_json) | None |
| [`venv_root_from_interpreter()`](#venv_root_from_interpreter) | Computes the path of the virtual environment root, based on the passed in python interpreter path |
| [`with_serialized_context()`](#with_serialized_context) | Use this method to create a new SerializationSettings that has an environment variable set with the SerializedContext |


#### default_entrypoint_settings()

```python
def default_entrypoint_settings(
    interpreter_path: str,
):
```
Assumes the entrypoint is installed in a virtual-environment where the interpreter is


| Parameter | Type |
|-|-|
| `interpreter_path` | `str` |

#### for_image()

```python
def for_image(
    image: str,
    version: str,
    project: str,
    domain: str,
    python_interpreter_path: str,
):
```
| Parameter | Type |
|-|-|
| `image` | `str` |
| `version` | `str` |
| `project` | `str` |
| `domain` | `str` |
| `python_interpreter_path` | `str` |

#### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
):
```
| Parameter | Type |
|-|-|
| `kvs` | `typing.Union[dict, list, str, int, float, bool, NoneType]` |
| `infer_missing` |  |

#### from_json()

```python
def from_json(
    s: typing.Union[str, bytes, bytearray],
    parse_float,
    parse_int,
    parse_constant,
    infer_missing,
    kw,
):
```
| Parameter | Type |
|-|-|
| `s` | `typing.Union[str, bytes, bytearray]` |
| `parse_float` |  |
| `parse_int` |  |
| `parse_constant` |  |
| `infer_missing` |  |
| `kw` |  |

#### from_transport()

```python
def from_transport(
    s: str,
):
```
| Parameter | Type |
|-|-|
| `s` | `str` |

#### new_builder()

```python
def new_builder()
```
Creates a ``SerializationSettings.Builder`` that copies the existing serialization settings parameters and
allows for customization.


#### schema()

```python
def schema(
    infer_missing: bool,
    only,
    exclude,
    many: bool,
    context,
    load_only,
    dump_only,
    partial: bool,
    unknown,
):
```
| Parameter | Type |
|-|-|
| `infer_missing` | `bool` |
| `only` |  |
| `exclude` |  |
| `many` | `bool` |
| `context` |  |
| `load_only` |  |
| `dump_only` |  |
| `partial` | `bool` |
| `unknown` |  |

#### should_fast_serialize()

```python
def should_fast_serialize()
```
Whether or not the serialization settings specify that entities should be serialized for fast registration.


#### to_dict()

```python
def to_dict(
    encode_json,
):
```
| Parameter | Type |
|-|-|
| `encode_json` |  |

#### to_json()

```python
def to_json(
    skipkeys: bool,
    ensure_ascii: bool,
    check_circular: bool,
    allow_nan: bool,
    indent: typing.Union[int, str, NoneType],
    separators: typing.Tuple[str, str],
    default: typing.Callable,
    sort_keys: bool,
    kw,
):
```
| Parameter | Type |
|-|-|
| `skipkeys` | `bool` |
| `ensure_ascii` | `bool` |
| `check_circular` | `bool` |
| `allow_nan` | `bool` |
| `indent` | `typing.Union[int, str, NoneType]` |
| `separators` | `typing.Tuple[str, str]` |
| `default` | `typing.Callable` |
| `sort_keys` | `bool` |
| `kw` |  |

#### venv_root_from_interpreter()

```python
def venv_root_from_interpreter(
    interpreter_path: str,
):
```
Computes the path of the virtual environment root, based on the passed in python interpreter path
for example /opt/venv/bin/python3 -> /opt/venv


| Parameter | Type |
|-|-|
| `interpreter_path` | `str` |

#### with_serialized_context()

```python
def with_serialized_context()
```
Use this method to create a new SerializationSettings that has an environment variable set with the SerializedContext
This is useful in transporting SerializedContext to serialized and registered tasks.
The setting will be available in the `env` field with the key `SERIALIZED_CONTEXT_ENV_VAR`
:return: A newly constructed SerializationSettings, or self, if it already has the serializationSettings


### Properties

| Property | Type | Description |
|-|-|-|
| entrypoint_settings |  |  |
| serialized_context |  |  |

## flytekit.core.utils.timeit

A context manager and a decorator that measures the execution time of the wrapped code block or functions.
It will append a timing information to TimeLineDeck. For instance:

@timeit("Function description")
def function()

with timeit("Wrapped code block description"):
# your code


```python
def timeit(
    name: str,
):
```
| Parameter | Type |
|-|-|
| `name` | `str` |

