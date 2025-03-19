---
title: flytekit.core.cache
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.cache

## Directory

### Classes

| Class | Description |
|-|-|
| [`Cache`](.././flytekit.core.cache#flytekitcorecachecache) | Cache configuration for a task. |
| [`CachePolicy`](.././flytekit.core.cache#flytekitcorecachecachepolicy) | Base class for protocol classes. |
| [`Generic`](.././flytekit.core.cache#flytekitcorecachegeneric) | Abstract base class for generic types. |
| [`ImageSpec`](.././flytekit.core.cache#flytekitcorecacheimagespec) | This class is used to specify the docker image that will be used to run the task. |
| [`ParamSpec`](.././flytekit.core.cache#flytekitcorecacheparamspec) | Parameter specification. |
| [`PodTemplate`](.././flytekit.core.cache#flytekitcorecachepodtemplate) | Custom PodTemplate specification for a Task. |
| [`Protocol`](.././flytekit.core.cache#flytekitcorecacheprotocol) | Base class for protocol classes. |
| [`TypeVar`](.././flytekit.core.cache#flytekitcorecachetypevar) | Type variable. |
| [`VersionParameters`](.././flytekit.core.cache#flytekitcorecacheversionparameters) | Parameters used for version hash generation. |

## flytekit.core.cache.Cache

Cache configuration for a task.



```python
def Cache(
    version: typing.Optional[str],
    serialize: bool,
    ignored_inputs: typing.Union[typing.Tuple[str, ...], str],
    salt: str,
    policies: typing.Union[typing.List[flytekit.core.cache.CachePolicy], flytekit.core.cache.CachePolicy, NoneType],
):
```
| Parameter | Type |
|-|-|
| `version` | `typing.Optional[str]` |
| `serialize` | `bool` |
| `ignored_inputs` | `typing.Union[typing.Tuple[str, ...], str]` |
| `salt` | `str` |
| `policies` | `typing.Union[typing.List[flytekit.core.cache.CachePolicy], flytekit.core.cache.CachePolicy, NoneType]` |

### Methods

| Method | Description |
|-|-|
| [`get_ignored_inputs()`](#get_ignored_inputs) | None |
| [`get_version()`](#get_version) | None |


#### get_ignored_inputs()

```python
def get_ignored_inputs()
```
#### get_version()

```python
def get_version(
    params: flytekit.core.cache.VersionParameters,
):
```
| Parameter | Type |
|-|-|
| `params` | `flytekit.core.cache.VersionParameters` |

## flytekit.core.cache.CachePolicy

Base class for protocol classes.

Protocol classes are defined as::

class Proto(Protocol):
def meth(self) -> int:
...

Such classes are primarily used with static type checkers that recognize
structural subtyping (static duck-typing).

For example::

class C:
def meth(self) -> int:
return 0

def func(x: Proto) -> int:
return x.meth()

func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with
@typing.runtime_checkable act as simple-minded runtime protocols that check
only the presence of given attributes, ignoring their type signatures.
Protocol classes can be generic, they are defined as::

class GenProto[T](Protocol):
def meth(self) -> T:
...


```python
def CachePolicy(
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
| [`get_version()`](#get_version) | None |


#### get_version()

```python
def get_version(
    salt: str,
    params: flytekit.core.cache.VersionParameters,
):
```
| Parameter | Type |
|-|-|
| `salt` | `str` |
| `params` | `flytekit.core.cache.VersionParameters` |

## flytekit.core.cache.Generic

Abstract base class for generic types.

On Python 3.12 and newer, generic classes implicitly inherit from
Generic when they declare a parameter list after the class's name::

class Mapping[KT, VT]:
def __getitem__(self, key: KT) -> VT:
...
# Etc.

On older versions of Python, however, generic classes have to
explicitly inherit from Generic.

After a class has been declared to be generic, it can then be used as
follows::

def lookup_name[KT, VT](mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
try:
return mapping[key]
except KeyError:
return default


## flytekit.core.cache.ImageSpec

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

## flytekit.core.cache.ParamSpec

Parameter specification.


## flytekit.core.cache.PodTemplate

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

## flytekit.core.cache.Protocol

Base class for protocol classes.

Protocol classes are defined as::

class Proto(Protocol):
def meth(self) -> int:
...

Such classes are primarily used with static type checkers that recognize
structural subtyping (static duck-typing).

For example::

class C:
def meth(self) -> int:
return 0

def func(x: Proto) -> int:
return x.meth()

func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with
@typing.runtime_checkable act as simple-minded runtime protocols that check
only the presence of given attributes, ignoring their type signatures.
Protocol classes can be generic, they are defined as::

class GenProto[T](Protocol):
def meth(self) -> T:
...


## flytekit.core.cache.TypeVar

Type variable.


## flytekit.core.cache.VersionParameters

Parameters used for version hash generation.

param func: The function to generate a version for. This is an optional parameter and can be any callable
that matches the specified parameter and return types.
:type func: Optional[Callable[P, FuncOut]]


```python
def VersionParameters(
    func: typing.Callable[~P, ~FuncOut],
    container_image: typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, NoneType],
    pod_template: typing.Optional[flytekit.core.pod_template.PodTemplate],
    pod_template_name: typing.Optional[str],
):
```
| Parameter | Type |
|-|-|
| `func` | `typing.Callable[~P, ~FuncOut]` |
| `container_image` | `typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, NoneType]` |
| `pod_template` | `typing.Optional[flytekit.core.pod_template.PodTemplate]` |
| `pod_template_name` | `typing.Optional[str]` |

