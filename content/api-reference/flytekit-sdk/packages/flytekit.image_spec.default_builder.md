---
title: flytekit.image_spec.default_builder
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.image_spec.default_builder

## Directory

### Classes

| Class | Description |
|-|-|
| [`CopyFileDetection`](.././flytekit.image_spec.default_builder#flytekitimage_specdefault_buildercopyfiledetection) | Create a collection of name/value pairs. |
| [`DefaultImageBuilder`](.././flytekit.image_spec.default_builder#flytekitimage_specdefault_builderdefaultimagebuilder) | Image builder using Docker and buildkit. |
| [`DockerIgnore`](.././flytekit.image_spec.default_builder#flytekitimage_specdefault_builderdockerignore) | Uses docker-py's PatternMatcher to check whether a path is ignored. |
| [`GitIgnore`](.././flytekit.image_spec.default_builder#flytekitimage_specdefault_buildergitignore) | Uses git cli (if available) to list all ignored files and compare with those. |
| [`IgnoreGroup`](.././flytekit.image_spec.default_builder#flytekitimage_specdefault_builderignoregroup) | Groups multiple Ignores and checks a path against them. |
| [`ImageSpec`](.././flytekit.image_spec.default_builder#flytekitimage_specdefault_builderimagespec) | This class is used to specify the docker image that will be used to run the task. |
| [`ImageSpecBuilder`](.././flytekit.image_spec.default_builder#flytekitimage_specdefault_builderimagespecbuilder) | None. |
| [`Path`](.././flytekit.image_spec.default_builder#flytekitimage_specdefault_builderpath) | PurePath subclass that can make system calls. |
| [`StandardIgnore`](.././flytekit.image_spec.default_builder#flytekitimage_specdefault_builderstandardignore) | Retains the standard ignore functionality that previously existed. |
| [`Template`](.././flytekit.image_spec.default_builder#flytekitimage_specdefault_buildertemplate) | A string class for supporting $-substitutions. |

## flytekit.image_spec.default_builder.CopyFileDetection

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


## flytekit.image_spec.default_builder.DefaultImageBuilder

Image builder using Docker and buildkit.


### Methods

| Method | Description |
|-|-|
| [`build_image()`](#build_image) | Build the docker image and push it to the registry |
| [`should_build()`](#should_build) | Whether or not the builder should build the ImageSpec |


#### build_image()

```python
def build_image(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
):
```
Build the docker image and push it to the registry.



| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |

#### should_build()

```python
def should_build(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
):
```
Whether or not the builder should build the ImageSpec.



| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |

## flytekit.image_spec.default_builder.DockerIgnore

Uses docker-py's PatternMatcher to check whether a path is ignored.


```python
def DockerIgnore(
    root: pathlib.Path,
):
```
| Parameter | Type |
|-|-|
| `root` | `pathlib.Path` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) | None |
| [`tar_filter()`](#tar_filter) | None |


#### is_ignored()

```python
def is_ignored(
    path: str,
):
```
| Parameter | Type |
|-|-|
| `path` | `str` |

#### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
):
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

## flytekit.image_spec.default_builder.GitIgnore

Uses git cli (if available) to list all ignored files and compare with those.


```python
def GitIgnore(
    root: pathlib.Path,
):
```
| Parameter | Type |
|-|-|
| `root` | `pathlib.Path` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) | None |
| [`tar_filter()`](#tar_filter) | None |


#### is_ignored()

```python
def is_ignored(
    path: str,
):
```
| Parameter | Type |
|-|-|
| `path` | `str` |

#### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
):
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

## flytekit.image_spec.default_builder.IgnoreGroup

Groups multiple Ignores and checks a path against them. A file is ignored if any
Ignore considers it ignored.


```python
def IgnoreGroup(
    root: str,
    ignores: typing.List[typing.Type[flytekit.tools.ignore.Ignore]],
):
```
| Parameter | Type |
|-|-|
| `root` | `str` |
| `ignores` | `typing.List[typing.Type[flytekit.tools.ignore.Ignore]]` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) | None |
| [`list_ignored()`](#list_ignored) | None |
| [`tar_filter()`](#tar_filter) | None |


#### is_ignored()

```python
def is_ignored(
    path: str,
):
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
):
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

## flytekit.image_spec.default_builder.ImageSpec

This class is used to specify the docker image that will be used to run the task.



```python
def ImageSpec(
    name: str,
    python_version: str,
    builder: typing.Optional[str],
    source_root: typing.Optional[str],
    env: typing.Optional[typing.Dict[str, str]],
    registry: typing.Optional[str],
    packages: typing.Optional[typing.List[str]],
    conda_packages: typing.Optional[typing.List[str]],
    conda_channels: typing.Optional[typing.List[str]],
    requirements: typing.Optional[str],
    apt_packages: typing.Optional[typing.List[str]],
    cuda: typing.Optional[str],
    cudnn: typing.Optional[str],
    base_image: typing.Union[str, ForwardRef('ImageSpec'), NoneType],
    platform: str,
    pip_index: typing.Optional[str],
    pip_extra_index_url: typing.Optional[typing.List[str]],
    pip_secret_mounts: typing.Optional[typing.List[typing.Tuple[str, str]]],
    pip_extra_args: typing.Optional[str],
    registry_config: typing.Optional[str],
    entrypoint: typing.Optional[typing.List[str]],
    commands: typing.Optional[typing.List[str]],
    tag_format: typing.Optional[str],
    source_copy_mode: typing.Optional[flytekit.constants.CopyFileDetection],
    copy: typing.Optional[typing.List[str]],
    python_exec: typing.Optional[str],
):
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `python_version` | `str` |
| `builder` | `typing.Optional[str]` |
| `source_root` | `typing.Optional[str]` |
| `env` | `typing.Optional[typing.Dict[str, str]]` |
| `registry` | `typing.Optional[str]` |
| `packages` | `typing.Optional[typing.List[str]]` |
| `conda_packages` | `typing.Optional[typing.List[str]]` |
| `conda_channels` | `typing.Optional[typing.List[str]]` |
| `requirements` | `typing.Optional[str]` |
| `apt_packages` | `typing.Optional[typing.List[str]]` |
| `cuda` | `typing.Optional[str]` |
| `cudnn` | `typing.Optional[str]` |
| `base_image` | `typing.Union[str, ForwardRef('ImageSpec'), NoneType]` |
| `platform` | `str` |
| `pip_index` | `typing.Optional[str]` |
| `pip_extra_index_url` | `typing.Optional[typing.List[str]]` |
| `pip_secret_mounts` | `typing.Optional[typing.List[typing.Tuple[str, str]]]` |
| `pip_extra_args` | `typing.Optional[str]` |
| `registry_config` | `typing.Optional[str]` |
| `entrypoint` | `typing.Optional[typing.List[str]]` |
| `commands` | `typing.Optional[typing.List[str]]` |
| `tag_format` | `typing.Optional[str]` |
| `source_copy_mode` | `typing.Optional[flytekit.constants.CopyFileDetection]` |
| `copy` | `typing.Optional[typing.List[str]]` |
| `python_exec` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`exist()`](#exist) | Check if the image exists in the registry |
| [`force_push()`](#force_push) | Builder that returns a new image spec with force push enabled |
| [`from_env()`](#from_env) | Create ImageSpec with the environment's Python version and packages pinned to the ones in the environment |
| [`image_name()`](#image_name) | Full image name with tag |
| [`is_container()`](#is_container) | Check if the current container image in the pod is built from current image spec |
| [`with_apt_packages()`](#with_apt_packages) | Builder that returns a new image spec with an additional list of apt packages that will be executed during the building process |
| [`with_commands()`](#with_commands) | Builder that returns a new image spec with an additional list of commands that will be executed during the building process |
| [`with_copy()`](#with_copy) | Builder that returns a new image spec with the source files copied to the destination directory |
| [`with_packages()`](#with_packages) | Builder that returns a new image speck with additional python packages that will be installed during the building process |


#### exist()

```python
def exist()
```
Check if the image exists in the registry.
Return True if the image exists in the registry, False otherwise.
Return None if failed to check if the image exists due to the permission issue or other reasons.


#### force_push()

```python
def force_push()
```
Builder that returns a new image spec with force push enabled.


#### from_env()

```python
def from_env(
    pinned_packages: typing.Optional[typing.List[str]],
    kwargs,
):
```
Create ImageSpec with the environment's Python version and packages pinned to the ones in the environment.


| Parameter | Type |
|-|-|
| `pinned_packages` | `typing.Optional[typing.List[str]]` |
| `kwargs` | ``**kwargs`` |

#### image_name()

```python
def image_name()
```
Full image name with tag.


#### is_container()

```python
def is_container()
```
Check if the current container image in the pod is built from current image spec.
:return: True if the current container image in the pod is built from current image spec, False otherwise.


#### with_apt_packages()

```python
def with_apt_packages(
    apt_packages: typing.Union[str, typing.List[str]],
):
```
Builder that returns a new image spec with an additional list of apt packages that will be executed during the building process.


| Parameter | Type |
|-|-|
| `apt_packages` | `typing.Union[str, typing.List[str]]` |

#### with_commands()

```python
def with_commands(
    commands: typing.Union[str, typing.List[str]],
):
```
Builder that returns a new image spec with an additional list of commands that will be executed during the building process.


| Parameter | Type |
|-|-|
| `commands` | `typing.Union[str, typing.List[str]]` |

#### with_copy()

```python
def with_copy(
    src: typing.Union[str, typing.List[str]],
):
```
Builder that returns a new image spec with the source files copied to the destination directory.


| Parameter | Type |
|-|-|
| `src` | `typing.Union[str, typing.List[str]]` |

#### with_packages()

```python
def with_packages(
    packages: typing.Union[str, typing.List[str]],
):
```
Builder that returns a new image speck with additional python packages that will be installed during the building process.


| Parameter | Type |
|-|-|
| `packages` | `typing.Union[str, typing.List[str]]` |

### Properties

| Property | Type | Description |
|-|-|-|
| tag |  |  |

## flytekit.image_spec.default_builder.ImageSpecBuilder

### Methods

| Method | Description |
|-|-|
| [`build_image()`](#build_image) | Build the docker image and push it to the registry |
| [`should_build()`](#should_build) | Whether or not the builder should build the ImageSpec |


#### build_image()

```python
def build_image(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
):
```
Build the docker image and push it to the registry.



| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |

#### should_build()

```python
def should_build(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
):
```
Whether or not the builder should build the ImageSpec.



| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |

## flytekit.image_spec.default_builder.Path

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

## flytekit.image_spec.default_builder.StandardIgnore

Retains the standard ignore functionality that previously existed. Could in theory
by fed with custom ignore patterns from cli.


```python
def StandardIgnore(
    root: pathlib.Path,
    patterns: typing.Optional[typing.List[str]],
):
```
| Parameter | Type |
|-|-|
| `root` | `pathlib.Path` |
| `patterns` | `typing.Optional[typing.List[str]]` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) | None |
| [`tar_filter()`](#tar_filter) | None |


#### is_ignored()

```python
def is_ignored(
    path: str,
):
```
| Parameter | Type |
|-|-|
| `path` | `str` |

#### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
):
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

## flytekit.image_spec.default_builder.Template

A string class for supporting $-substitutions.


```python
def Template(
    template,
):
```
| Parameter | Type |
|-|-|
| `template` |  |

### Methods

| Method | Description |
|-|-|
| [`get_identifiers()`](#get_identifiers) | None |
| [`is_valid()`](#is_valid) | None |
| [`safe_substitute()`](#safe_substitute) | None |
| [`substitute()`](#substitute) | None |


#### get_identifiers()

```python
def get_identifiers()
```
#### is_valid()

```python
def is_valid()
```
#### safe_substitute()

```python
def safe_substitute(
    mapping,
    kws,
):
```
| Parameter | Type |
|-|-|
| `mapping` |  |
| `kws` |  |

#### substitute()

```python
def substitute(
    mapping,
    kws,
):
```
| Parameter | Type |
|-|-|
| `mapping` |  |
| `kws` |  |

