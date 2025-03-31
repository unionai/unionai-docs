---
title: flytekit.image_spec.default_builder
version: 0.1.dev2175+gcd6bd01.d20250325
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
| [`ImageSpecBuilder`](.././flytekit.image_spec.default_builder#flytekitimage_specdefault_builderimagespecbuilder) |  |
| [`Path`](.././flytekit.image_spec.default_builder#flytekitimage_specdefault_builderpath) | PurePath subclass that can make system calls. |
| [`StandardIgnore`](.././flytekit.image_spec.default_builder#flytekitimage_specdefault_builderstandardignore) | Retains the standard ignore functionality that previously existed. |
| [`Template`](.././flytekit.image_spec.default_builder#flytekitimage_specdefault_buildertemplate) | A string class for supporting $-substitutions. |

### Methods

| Method | Description |
|-|-|
| [`NamedTuple()`](#namedtuple) | Typed version of namedtuple. |
| [`_copy_lock_files_into_context()`](#_copy_lock_files_into_context) |  |
| [`_is_flytekit()`](#_is_flytekit) | Return True if `package` is flytekit. |
| [`_secret_id()`](#_secret_id) |  |
| [`create_docker_context()`](#create_docker_context) | Populate tmp_dir with Dockerfile as specified by the `image_spec`. |
| [`get_flytekit_for_pypi()`](#get_flytekit_for_pypi) | Get flytekit version on PyPI. |
| [`ls_files()`](#ls_files) | user_modules_and_packages is a list of the Python modules and packages, expressed as absolute paths, that the. |
| [`prepare_poetry_lock_command()`](#prepare_poetry_lock_command) |  |
| [`prepare_python_executable()`](#prepare_python_executable) |  |
| [`prepare_python_install()`](#prepare_python_install) |  |
| [`prepare_uv_lock_command()`](#prepare_uv_lock_command) |  |
| [`run()`](#run) | Run command with arguments and return a CompletedProcess instance. |


### Variables

| Property | Type | Description |
|-|-|-|
| `APT_INSTALL_COMMAND_TEMPLATE` | `Template` |  |
| `DOCKER_FILE_TEMPLATE` | `Template` |  |
| `MICROMAMBA_INSTALL_COMMAND_TEMPLATE` | `Template` |  |
| `POETRY_LOCK_TEMPLATE` | `Template` |  |
| `UV_LOCK_INSTALL_TEMPLATE` | `Template` |  |
| `UV_PYTHON_INSTALL_COMMAND_TEMPLATE` | `Template` |  |

## Methods

#### NamedTuple()

```python
def NamedTuple(
    typename,
    fields,
    kwargs,
)
```
Typed version of namedtuple.

Usage::

class Employee(NamedTuple):
name: str
id: int

This is equivalent to::

Employee = collections.namedtuple('Employee', ['name', 'id'])

The resulting class has an extra __annotations__ attribute, giving a
dict that maps field names to types.  (The field names are also in
the _fields attribute, which is part of the namedtuple API.)
An alternative equivalent functional syntax is also accepted::

Employee = NamedTuple('Employee', [('name', str), ('id', int)])


| Parameter | Type |
|-|-|
| `typename` |  |
| `fields` |  |
| `kwargs` | ``**kwargs`` |

#### _copy_lock_files_into_context()

```python
def _copy_lock_files_into_context(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
    lock_file: str,
    tmp_dir: pathlib._local.Path,
)
```
| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |
| `lock_file` | `str` |
| `tmp_dir` | `pathlib._local.Path` |

#### _is_flytekit()

```python
def _is_flytekit(
    package: str,
) -> bool
```
Return True if `package` is flytekit. `package` is expected to be a valid version
spec. i.e. `flytekit==1.12.3`, `flytekit`, `flytekit~=1.12.3`.


| Parameter | Type |
|-|-|
| `package` | `str` |

#### _secret_id()

```python
def _secret_id(
    index: int,
) -> str
```
| Parameter | Type |
|-|-|
| `index` | `int` |

#### create_docker_context()

```python
def create_docker_context(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
    tmp_dir: pathlib._local.Path,
)
```
Populate tmp_dir with Dockerfile as specified by the `image_spec`.


| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |
| `tmp_dir` | `pathlib._local.Path` |

#### get_flytekit_for_pypi()

```python
def get_flytekit_for_pypi()
```
Get flytekit version on PyPI.


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

#### prepare_poetry_lock_command()

```python
def prepare_poetry_lock_command(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
    tmp_dir: pathlib._local.Path,
) -> typing.Tuple[string.Template, typing.List[str]]
```
| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |
| `tmp_dir` | `pathlib._local.Path` |

#### prepare_python_executable()

```python
def prepare_python_executable(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
) -> flytekit.image_spec.default_builder._PythonInstallTemplate
```
| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |

#### prepare_python_install()

```python
def prepare_python_install(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
    tmp_dir: pathlib._local.Path,
) -> str
```
| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |
| `tmp_dir` | `pathlib._local.Path` |

#### prepare_uv_lock_command()

```python
def prepare_uv_lock_command(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
    tmp_dir: pathlib._local.Path,
) -> typing.Tuple[string.Template, typing.List[str]]
```
| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |
| `tmp_dir` | `pathlib._local.Path` |

#### run()

```python
def run(
    popenargs,
    input,
    capture_output,
    timeout,
    check,
    kwargs,
)
```
Run command with arguments and return a CompletedProcess instance.

The returned instance will have attributes args, returncode, stdout and
stderr. By default, stdout and stderr are not captured, and those attributes
will be None. Pass stdout=PIPE and/or stderr=PIPE in order to capture them,
or pass capture_output=True to capture both.

If check is True and the exit code was non-zero, it raises a
CalledProcessError. The CalledProcessError object will have the return code
in the returncode attribute, and output & stderr attributes if those streams
were captured.

If timeout (seconds) is given and the process takes too long,
a TimeoutExpired exception will be raised.

There is an optional argument "input", allowing you to
pass bytes or a string to the subprocess's stdin.  If you use this argument
you may not also use the Popen constructor's "stdin" argument, as
it will be used internally.

By default, all communication is in bytes, and therefore any "input" should
be bytes, and the stdout and stderr will be bytes. If in text mode, any
"input" should be a string, and stdout and stderr will be strings decoded
according to locale encoding, or by "encoding" if set. Text mode is
triggered by setting any of text, encoding, errors or universal_newlines.

The other arguments are the same as for the Popen constructor.


| Parameter | Type |
|-|-|
| `popenargs` |  |
| `input` |  |
| `capture_output` |  |
| `timeout` |  |
| `check` |  |
| `kwargs` | ``**kwargs`` |

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
| [`build_image()`](#build_image) | Build the docker image and push it to the registry. |
| [`should_build()`](#should_build) | Whether or not the builder should build the ImageSpec. |


#### build_image()

```python
def build_image(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
) -> str
```
Build the docker image and push it to the registry.



| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |

#### should_build()

```python
def should_build(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
) -> bool
```
Whether or not the builder should build the ImageSpec.



| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |

## flytekit.image_spec.default_builder.DockerIgnore

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

## flytekit.image_spec.default_builder.GitIgnore

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

## flytekit.image_spec.default_builder.IgnoreGroup

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

## flytekit.image_spec.default_builder.ImageSpec

This class is used to specify the docker image that will be used to run the task.



```python
class ImageSpec(
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
)
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
| [`exist()`](#exist) | Check if the image exists in the registry. |
| [`force_push()`](#force_push) | Builder that returns a new image spec with force push enabled. |
| [`from_env()`](#from_env) | Create ImageSpec with the environment's Python version and packages pinned to the ones in the environment. |
| [`image_name()`](#image_name) | Full image name with tag. |
| [`is_container()`](#is_container) | Check if the current container image in the pod is built from current image spec. |
| [`with_apt_packages()`](#with_apt_packages) | Builder that returns a new image spec with an additional list of apt packages that will be executed during the building process. |
| [`with_commands()`](#with_commands) | Builder that returns a new image spec with an additional list of commands that will be executed during the building process. |
| [`with_copy()`](#with_copy) | Builder that returns a new image spec with the source files copied to the destination directory. |
| [`with_packages()`](#with_packages) | Builder that returns a new image speck with additional python packages that will be installed during the building process. |


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
) -> ImageSpec
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
) -> ImageSpec
```
Builder that returns a new image spec with an additional list of apt packages that will be executed during the building process.


| Parameter | Type |
|-|-|
| `apt_packages` | `typing.Union[str, typing.List[str]]` |

#### with_commands()

```python
def with_commands(
    commands: typing.Union[str, typing.List[str]],
) -> ImageSpec
```
Builder that returns a new image spec with an additional list of commands that will be executed during the building process.


| Parameter | Type |
|-|-|
| `commands` | `typing.Union[str, typing.List[str]]` |

#### with_copy()

```python
def with_copy(
    src: typing.Union[str, typing.List[str]],
) -> ImageSpec
```
Builder that returns a new image spec with the source files copied to the destination directory.


| Parameter | Type |
|-|-|
| `src` | `typing.Union[str, typing.List[str]]` |

#### with_packages()

```python
def with_packages(
    packages: typing.Union[str, typing.List[str]],
) -> ImageSpec
```
Builder that returns a new image speck with additional python packages that will be installed during the building process.


| Parameter | Type |
|-|-|
| `packages` | `typing.Union[str, typing.List[str]]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `tag` |  | {{< multiline >}}Calculate a hash from the image spec. The hash will be the tag of the image.
We will also read the content of the requirement file and the source root to calculate the hash.
Therefore, it will generate different hash if new dependencies are added or the source code is changed.

Keep in mind the fields source_root and copy may be changed by update_image_spec_copy_handling, so when
you call this property in relation to that function matter will change the output.
{{< /multiline >}} |

## flytekit.image_spec.default_builder.ImageSpecBuilder

### Methods

| Method | Description |
|-|-|
| [`build_image()`](#build_image) | Build the docker image and push it to the registry. |
| [`should_build()`](#should_build) | Whether or not the builder should build the ImageSpec. |


#### build_image()

```python
def build_image(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
) -> typing.Optional[str]
```
Build the docker image and push it to the registry.



| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |

#### should_build()

```python
def should_build(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
) -> bool
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

## flytekit.image_spec.default_builder.StandardIgnore

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

## flytekit.image_spec.default_builder.Template

A string class for supporting $-substitutions.


```python
class Template(
    template,
)
```
| Parameter | Type |
|-|-|
| `template` |  |

### Methods

| Method | Description |
|-|-|
| [`get_identifiers()`](#get_identifiers) |  |
| [`is_valid()`](#is_valid) |  |
| [`safe_substitute()`](#safe_substitute) |  |
| [`substitute()`](#substitute) |  |


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
)
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
)
```
| Parameter | Type |
|-|-|
| `mapping` |  |
| `kws` |  |

