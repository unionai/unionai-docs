---
title: flyte
version: 0.2.0b8
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flyte


Flyte SDK for authoring Compound AI applications, services and workflows.

## Environments

TaskEnvironment class to define a new environment for a set of tasks.

Example usage:

```python
env = flyte.TaskEnvironment(name="my_env", image="my_image", resources=Resources(cpu="1", memory="1Gi"))

@env.task
async def my_task():
    pass
```

## Directory

### Classes

| Class | Description |
|-|-|
| [`Cache`](.././flyte#flytecache) | Cache configuration for a task. |
| [`Device`](.././flyte#flytedevice) | Represents a device type, its quantity and partition if applicable. |
| [`Environment`](.././flyte#flyteenvironment) |  |
| [`Image`](.././flyte#flyteimage) | This is a representation of Container Images, which can be used to create layered images programmatically. |
| [`Resources`](.././flyte#flyteresources) | Resources such as CPU, Memory, and GPU that can be allocated to a task. |
| [`RetryStrategy`](.././flyte#flyteretrystrategy) | Retry strategy for the task or task environment. |
| [`ReusePolicy`](.././flyte#flytereusepolicy) | ReusePolicy can be used to configure a task to reuse the environment. |
| [`Secret`](.././flyte#flytesecret) | Secrets are used to inject sensitive information into tasks. |
| [`TaskEnvironment`](.././flyte#flytetaskenvironment) | Environment class to define a new environment for a set of tasks. |
| [`Timeout`](.././flyte#flytetimeout) | Timeout class to define a timeout for a task. |

### Protocols

| Protocol | Description |
|-|-|
| [`CachePolicy`](.././flyte#flytecachepolicy) | Base class for protocol classes. |

### Methods

| Method | Description |
|-|-|
| [`GPU()`](#gpu) | Create a GPU device instance. |
| [`TPU()`](#tpu) | Create a TPU device instance. |
| [`ctx()`](#ctx) | Retrieve the current task context from the context variable. |
| [`group()`](#group) | Create a new group with the given name. |
| [`trace()`](#trace) | A decorator that traces function execution with timing information. |
| [`with_runcontext()`](#with_runcontext) | Launch a new run with the given parameters as the context. |


### Variables

| Property | Type | Description |
|-|-|-|
| `TimeoutType` | `UnionType` |  |
| `__version__` | `str` |  |

## Methods

#### GPU()

```python
def GPU(
    device: typing.Literal['T4', 'A100', 'A100 80G', 'H100', 'L4', 'L40s'],
    quantity: typing.Literal[1, 2, 3, 4, 5, 6, 7, 8],
    partition: typing.Union[typing.Literal['1g.5gb', '2g.10gb', '3g.20gb', '4g.20gb', '7g.40gb'], typing.Literal['1g.10gb', '2g.20gb', '3g.40gb', '4g.40gb', '7g.80gb'], NoneType],
) -> flyte._resources.Device
```
Create a GPU device instance.


| Parameter | Type |
|-|-|
| `device` | `typing.Literal['T4', 'A100', 'A100 80G', 'H100', 'L4', 'L40s']` |
| `quantity` | `typing.Literal[1, 2, 3, 4, 5, 6, 7, 8]` |
| `partition` | `typing.Union[typing.Literal['1g.5gb', '2g.10gb', '3g.20gb', '4g.20gb', '7g.40gb'], typing.Literal['1g.10gb', '2g.20gb', '3g.40gb', '4g.40gb', '7g.80gb'], NoneType]` |

#### TPU()

```python
def TPU(
    device: typing.Literal['V5P', 'V6E'],
    partition: typing.Union[typing.Literal['2x2x1', '2x2x2', '2x4x4', '4x4x4', '4x4x8', '4x8x8', '8x8x8', '8x8x16', '8x16x16', '16x16x16', '16x16x24'], typing.Literal['1x1', '2x2', '2x4', '4x4', '4x8', '8x8', '8x16', '16x16'], NoneType],
)
```
Create a TPU device instance.


| Parameter | Type |
|-|-|
| `device` | `typing.Literal['V5P', 'V6E']` |
| `partition` | `typing.Union[typing.Literal['2x2x1', '2x2x2', '2x4x4', '4x4x4', '4x4x8', '4x8x8', '8x8x8', '8x8x16', '8x16x16', '16x16x16', '16x16x24'], typing.Literal['1x1', '2x2', '2x4', '4x4', '4x8', '8x8', '8x16', '16x16'], NoneType]` |

#### ctx()

```python
def ctx()
```
Retrieve the current task context from the context variable.


#### group()

```python
def group(
    name: str,
)
```
Create a new group with the given name. The method is intended to be used as a context manager.

Example:
```python
@task
async def my_task():
    ...
    with group("my_group"):
        t1(x,y)  # tasks in this block will be grouped under "my_group"
    ...
```



| Parameter | Type |
|-|-|
| `name` | `str` |

#### trace()

```python
def trace(
    func: typing.Callable[..., ~T],
) -> typing.Callable[..., ~T]
```
A decorator that traces function execution with timing information.
Works with regular functions, async functions, and async generators/iterators.


| Parameter | Type |
|-|-|
| `func` | `typing.Callable[..., ~T]` |

#### with_runcontext()

```python
def with_runcontext(
    mode: Mode | None,
    name: Optional[str],
    service_account: Optional[str],
    version: Optional[str],
    copy_style: CopyFiles,
    dry_run: bool,
    copy_bundle_to: pathlib.Path | None,
    interactive_mode: bool | None,
    raw_data_path: str | None,
    run_base_dir: str | None,
) -> _Runner
```
Launch a new run with the given parameters as the context.

Example:
```python
import flyte
env = flyte.TaskEnvironment("example")

@env.task
async def example_task(x: int, y: str) -> str:
    return f"{x} {y}"

if __name__ == "__main__":
    flyte.with_runcontext(name="example_run_id").run(example_task, 1, y="hello")
```



| Parameter | Type |
|-|-|
| `mode` | `Mode \| None` |
| `name` | `Optional[str]` |
| `service_account` | `Optional[str]` |
| `version` | `Optional[str]` |
| `copy_style` | `CopyFiles` |
| `dry_run` | `bool` |
| `copy_bundle_to` | `pathlib.Path \| None` |
| `interactive_mode` | `bool \| None` |
| `raw_data_path` | `str \| None` |
| `run_base_dir` | `str \| None` |

## flyte.Cache

Cache configuration for a task.


```python
class Cache(
    behavior: typing.Literal['auto', 'override', 'disable', 'enabled'],
    version_override: typing.Optional[str],
    serialize: bool,
    ignored_inputs: typing.Union[typing.Tuple[str, ...], str],
    salt: str,
    policies: typing.Union[typing.List[flyte._cache.cache.CachePolicy], flyte._cache.cache.CachePolicy, NoneType],
)
```
| Parameter | Type |
|-|-|
| `behavior` | `typing.Literal['auto', 'override', 'disable', 'enabled']` |
| `version_override` | `typing.Optional[str]` |
| `serialize` | `bool` |
| `ignored_inputs` | `typing.Union[typing.Tuple[str, ...], str]` |
| `salt` | `str` |
| `policies` | `typing.Union[typing.List[flyte._cache.cache.CachePolicy], flyte._cache.cache.CachePolicy, NoneType]` |

### Methods

| Method | Description |
|-|-|
| [`get_ignored_inputs()`](#get_ignored_inputs) |  |
| [`get_version()`](#get_version) |  |
| [`is_enabled()`](#is_enabled) | Check if the cache policy is enabled. |


#### get_ignored_inputs()

```python
def get_ignored_inputs()
```
#### get_version()

```python
def get_version(
    params: typing.Optional[flyte._cache.cache.VersionParameters],
) -> str
```
| Parameter | Type |
|-|-|
| `params` | `typing.Optional[flyte._cache.cache.VersionParameters]` |

#### is_enabled()

```python
def is_enabled()
```
Check if the cache policy is enabled.


## flyte.CachePolicy

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
protocol CachePolicy()
```
### Methods

| Method | Description |
|-|-|
| [`get_version()`](#get_version) |  |


#### get_version()

```python
def get_version(
    salt: str,
    params: flyte._cache.cache.VersionParameters,
) -> str
```
| Parameter | Type |
|-|-|
| `salt` | `str` |
| `params` | `flyte._cache.cache.VersionParameters` |

## flyte.Device

Represents a device type, its quantity and partition if applicable.
param device: The type of device (e.g., "T4", "A100").
param quantity: The number of devices of this type.
param partition: The partition of the device (e.g., "1g.5gb", "2g.10gb" for gpus) or ("1x1", ... for tpus).


```python
class Device(
    quantity: int,
    device: str | None,
    partition: str | None,
)
```
| Parameter | Type |
|-|-|
| `quantity` | `int` |
| `device` | `str \| None` |
| `partition` | `str \| None` |

## flyte.Environment

```python
class Environment(
    name: str,
    env_dep_hints: List[Environment],
    pod_template: Optional[Union[str, 'V1PodTemplate']],
    description: Optional[str],
    secrets: Optional[SecretRequest],
    env: Optional[Dict[str, str]],
    resources: Optional[Resources],
    image: Union[str, Image, Literal['auto']],
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `env_dep_hints` | `List[Environment]` |
| `pod_template` | `Optional[Union[str, 'V1PodTemplate']]` |
| `description` | `Optional[str]` |
| `secrets` | `Optional[SecretRequest]` |
| `env` | `Optional[Dict[str, str]]` |
| `resources` | `Optional[Resources]` |
| `image` | `Union[str, Image, Literal['auto']]` |

### Methods

| Method | Description |
|-|-|
| [`add_dependency()`](#add_dependency) | Add a dependency to the environment. |
| [`clone_with()`](#clone_with) |  |


#### add_dependency()

```python
def add_dependency(
    env: Environment,
)
```
Add a dependency to the environment.


| Parameter | Type |
|-|-|
| `env` | `Environment` |

#### clone_with()

```python
def clone_with(
    name: str,
    image: Optional[Union[str, Image, Literal['auto']]],
    resources: Optional[Resources],
    env: Optional[Dict[str, str]],
    secrets: Optional[SecretRequest],
    env_dep_hints: Optional[List[Environment]],
    kwargs: **kwargs,
) -> Environment
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `image` | `Optional[Union[str, Image, Literal['auto']]]` |
| `resources` | `Optional[Resources]` |
| `env` | `Optional[Dict[str, str]]` |
| `secrets` | `Optional[SecretRequest]` |
| `env_dep_hints` | `Optional[List[Environment]]` |
| `kwargs` | `**kwargs` |

## flyte.Image

This is a representation of Container Images, which can be used to create layered images programmatically.

Use by first calling one of the base constructor methods. These all begin with `from` or `default_`
The image can then be amended with additional layers using the various `with_*` methods.

Invariant for this class: The construction of Image objects must be doable everywhere. That is, if a
  user has a custom image that is not accessible, calling .with_source_file on a file that doesn't exist, the
  instantiation of the object itself must still go through. Further, the .identifier property of the image must
  also still go through. This is because it may have been already built somewhere else.
  Use validate() functions to check each layer for actual errors. These are invoked at actual
  build time. See self.id for more information


```python
class Image(
    base_image: Optional[str],
    dockerfile: Optional[Path],
    registry: Optional[str],
    name: Optional[str],
    platform: Tuple[Architecture, ...],
    tag: Optional[str],
    python_version: Tuple[int, int],
    is_final: bool,
    _layers: Tuple[Layer, ...],
)
```
| Parameter | Type |
|-|-|
| `base_image` | `Optional[str]` |
| `dockerfile` | `Optional[Path]` |
| `registry` | `Optional[str]` |
| `name` | `Optional[str]` |
| `platform` | `Tuple[Architecture, ...]` |
| `tag` | `Optional[str]` |
| `python_version` | `Tuple[int, int]` |
| `is_final` | `bool` |
| `_layers` | `Tuple[Layer, ...]` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Use this method to start using the default base image, built from this library's base Dockerfile. |
| [`clone()`](#clone) | Use this method to clone the current image and change the registry and name. |
| [`from_dockerfile()`](#from_dockerfile) | Use this method to create a new image with the specified dockerfile. |
| [`from_prebuilt()`](#from_prebuilt) | Use this method to start with a pre-built base image. |
| [`from_uv_debian()`](#from_uv_debian) | This creates a new debian-based base image. |
| [`from_uv_script()`](#from_uv_script) | Use this method to create a new image with the specified uv script. |
| [`validate()`](#validate) |  |
| [`with_apt_packages()`](#with_apt_packages) | Use this method to create a new image with the specified apt packages layered on top of the current image. |
| [`with_commands()`](#with_commands) | Use this method to create a new image with the specified commands layered on top of the current image. |
| [`with_env_vars()`](#with_env_vars) | Use this method to create a new image with the specified environment variables layered on top of. |
| [`with_local_v2()`](#with_local_v2) | Use this method to create a new image with the local v2 builder. |
| [`with_pip_packages()`](#with_pip_packages) | Use this method to create a new image with the specified pip packages layered on top of the current image. |
| [`with_requirements()`](#with_requirements) | Use this method to create a new image with the specified requirements file layered on top of the current image. |
| [`with_source_file()`](#with_source_file) | Use this method to create a new image with the specified local file layered on top of the current image. |
| [`with_source_folder()`](#with_source_folder) | Use this method to create a new image with the specified local directory layered on top of the current image. |
| [`with_uv_project()`](#with_uv_project) | Use this method to create a new image with the specified uv. |
| [`with_workdir()`](#with_workdir) | Use this method to create a new image with the specified working directory. |


#### auto()

```python
def auto(
    python_version: Optional[Tuple[int, int]],
    flyte_version: Optional[str],
    registry: Optional[str],
    name: Optional[str],
) -> Image
```
Use this method to start using the default base image, built from this library's base Dockerfile
Default images are multi-arch amd/arm64



| Parameter | Type |
|-|-|
| `python_version` | `Optional[Tuple[int, int]]` |
| `flyte_version` | `Optional[str]` |
| `registry` | `Optional[str]` |
| `name` | `Optional[str]` |

#### clone()

```python
def clone(
    registry: Optional[str],
    name: Optional[str],
    addl_layer: Optional[Layer],
) -> Image
```
Use this method to clone the current image and change the registry and name



| Parameter | Type |
|-|-|
| `registry` | `Optional[str]` |
| `name` | `Optional[str]` |
| `addl_layer` | `Optional[Layer]` |

#### from_dockerfile()

```python
def from_dockerfile(
    file: Path,
    registry: str,
    name: str,
    tag: Optional[str],
) -> Image
```
Use this method to create a new image with the specified dockerfile



| Parameter | Type |
|-|-|
| `file` | `Path` |
| `registry` | `str` |
| `name` | `str` |
| `tag` | `Optional[str]` |

#### from_prebuilt()

```python
def from_prebuilt(
    image_uri: str,
) -> Image
```
Use this method to start with a pre-built base image. This image must already exist in the registry of course.



| Parameter | Type |
|-|-|
| `image_uri` | `str` |

#### from_uv_debian()

```python
def from_uv_debian(
    registry: str,
    name: str,
    tag: Optional[str],
    python_version: Optional[Tuple[int, int]],
    arch: Union[Architecture, Tuple[Architecture, ...]],
) -> Image
```
This creates a new debian-based base image.
If using the Union or docker builders, image will have uv available and a virtualenv created at /opt/venv.



| Parameter | Type |
|-|-|
| `registry` | `str` |
| `name` | `str` |
| `tag` | `Optional[str]` |
| `python_version` | `Optional[Tuple[int, int]]` |
| `arch` | `Union[Architecture, Tuple[Architecture, ...]]` |

#### from_uv_script()

```python
def from_uv_script(
    script: Path | str,
    name: str,
    registry: str | None,
    python_version: Optional[Tuple[int, int]],
    arch: Union[Architecture, Tuple[Architecture, ...]],
) -> Image
```
Use this method to create a new image with the specified uv script.
It uses the header of the script to determine the python version, dependencies to install.
The script must be a valid uv script, otherwise an error will be raised.

Usually the header of the script will look like this:
Example:
```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx"]
# ///
```

For more information on the uv script format, see the documentation:
[UV: Declaring script dependencies](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies)



| Parameter | Type |
|-|-|
| `script` | `Path \| str` |
| `name` | `str` |
| `registry` | `str \| None` |
| `python_version` | `Optional[Tuple[int, int]]` |
| `arch` | `Union[Architecture, Tuple[Architecture, ...]]` |

#### validate()

```python
def validate()
```
#### with_apt_packages()

```python
def with_apt_packages(
    packages: Union[str, List[str], Tuple[str, ...]],
) -> Image
```
Use this method to create a new image with the specified apt packages layered on top of the current image



| Parameter | Type |
|-|-|
| `packages` | `Union[str, List[str], Tuple[str, ...]]` |

#### with_commands()

```python
def with_commands(
    commands: List[str],
) -> Image
```
Use this method to create a new image with the specified commands layered on top of the current image
Be sure not to use RUN in your command.



| Parameter | Type |
|-|-|
| `commands` | `List[str]` |

#### with_env_vars()

```python
def with_env_vars(
    env_vars: Dict[str, str],
) -> Image
```
Use this method to create a new image with the specified environment variables layered on top of
the current image. Cannot be used in conjunction with conda



| Parameter | Type |
|-|-|
| `env_vars` | `Dict[str, str]` |

#### with_local_v2()

```python
def with_local_v2()
```
Use this method to create a new image with the local v2 builder
This will override any existing builder

:return: Image


#### with_pip_packages()

```python
def with_pip_packages(
    packages: Union[str, List[str], Tuple[str, ...]],
    index_url: Optional[str],
    extra_index_urls: Union[str, List[str], Tuple[str, ...], None],
    pre: bool,
    extra_args: Optional[str],
) -> Image
```
Use this method to create a new image with the specified pip packages layered on top of the current image
Cannot be used in conjunction with conda

Example:
```python
@flyte.task(image=(flyte.Image
                .ubuntu_python()
                .with_pip_packages(["requests", "numpy"])))
def my_task(x: int) -> int:
    import numpy as np
    return np.sum([x, 1])
```



| Parameter | Type |
|-|-|
| `packages` | `Union[str, List[str], Tuple[str, ...]]` |
| `index_url` | `Optional[str]` |
| `extra_index_urls` | `Union[str, List[str], Tuple[str, ...], None]` |
| `pre` | `bool` |
| `extra_args` | `Optional[str]` |

#### with_requirements()

```python
def with_requirements(
    file: Path,
) -> Image
```
Use this method to create a new image with the specified requirements file layered on top of the current image
Cannot be used in conjunction with conda



| Parameter | Type |
|-|-|
| `file` | `Path` |

#### with_source_file()

```python
def with_source_file(
    context_source: Path,
    image_dest: Optional[str],
) -> Image
```
Use this method to create a new image with the specified local file layered on top of the current image.
If dest is not specified, it will be copied to the working directory of the image



| Parameter | Type |
|-|-|
| `context_source` | `Path` |
| `image_dest` | `Optional[str]` |

#### with_source_folder()

```python
def with_source_folder(
    context_source: Path,
    image_dest: Optional[str],
) -> Image
```
Use this method to create a new image with the specified local directory layered on top of the current image.
If dest is not specified, it will be copied to the working directory of the image



| Parameter | Type |
|-|-|
| `context_source` | `Path` |
| `image_dest` | `Optional[str]` |

#### with_uv_project()

```python
def with_uv_project(
    pyproject_file: Path,
) -> Image
```
Use this method to create a new image with the specified uv.lock file layered on top of the current image
Must have a corresponding pyproject.toml file in the same directory
Cannot be used in conjunction with conda
In the Union builders, using this will change the virtual env to /root/.venv



| Parameter | Type |
|-|-|
| `pyproject_file` | `Path` |

#### with_workdir()

```python
def with_workdir(
    workdir: str,
) -> Image
```
Use this method to create a new image with the specified working directory
This will override any existing working directory



| Parameter | Type |
|-|-|
| `workdir` | `str` |

## flyte.Resources

Resources such as CPU, Memory, and GPU that can be allocated to a task.

Example:
- Single CPU, 1GiB of memory, and 1 T4 GPU:
```python
@task(resources=Resources(cpu=1, memory="1GiB", gpu="T4:1"))
def my_task() -> int:
    return 42
```
- 1CPU with limit upto 2CPU, 2GiB of memory, and 8 A100 GPUs and 10GiB of disk:
```python
@task(resources=Resources(cpu=(1, 2), memory="2GiB", gpu="A100:8", disk="10GiB"))
def my_task() -> int:
    return 42
```



```python
class Resources(
    cpu: typing.Union[int, float, str, typing.Tuple[int | float | str, int | float | str], NoneType],
    memory: typing.Union[str, typing.Tuple[str, str], NoneType],
    gpu: typing.Union[typing.Literal['T4:1', 'T4:2', 'T4:3', 'T4:4', 'T4:5', 'T4:6', 'T4:7', 'T4:8', 'L4:1', 'L4:2', 'L4:3', 'L4:4', 'L4:5', 'L4:6', 'L4:7', 'L4:8', 'L40s:1', 'L40s:2', 'L40s:3', 'L40s:4', 'L40s:5', 'L40s:6', 'L40s:7', 'L40s:8', 'A100:1', 'A100:2', 'A100:3', 'A100:4', 'A100:5', 'A100:6', 'A100:7', 'A100:8', 'A100 80G:1', 'A100 80G:2', 'A100 80G:3', 'A100 80G:4', 'A100 80G:5', 'A100 80G:6', 'A100 80G:7', 'A100 80G:8', 'H100:1', 'H100:2', 'H100:3', 'H100:4', 'H100:5', 'H100:6', 'H100:7', 'H100:8'], int, flyte._resources.Device, NoneType],
    disk: typing.Optional[str],
    shm: typing.Union[str, typing.Literal['auto'], NoneType],
)
```
| Parameter | Type |
|-|-|
| `cpu` | `typing.Union[int, float, str, typing.Tuple[int \| float \| str, int \| float \| str], NoneType]` |
| `memory` | `typing.Union[str, typing.Tuple[str, str], NoneType]` |
| `gpu` | `typing.Union[typing.Literal['T4:1', 'T4:2', 'T4:3', 'T4:4', 'T4:5', 'T4:6', 'T4:7', 'T4:8', 'L4:1', 'L4:2', 'L4:3', 'L4:4', 'L4:5', 'L4:6', 'L4:7', 'L4:8', 'L40s:1', 'L40s:2', 'L40s:3', 'L40s:4', 'L40s:5', 'L40s:6', 'L40s:7', 'L40s:8', 'A100:1', 'A100:2', 'A100:3', 'A100:4', 'A100:5', 'A100:6', 'A100:7', 'A100:8', 'A100 80G:1', 'A100 80G:2', 'A100 80G:3', 'A100 80G:4', 'A100 80G:5', 'A100 80G:6', 'A100 80G:7', 'A100 80G:8', 'H100:1', 'H100:2', 'H100:3', 'H100:4', 'H100:5', 'H100:6', 'H100:7', 'H100:8'], int, flyte._resources.Device, NoneType]` |
| `disk` | `typing.Optional[str]` |
| `shm` | `typing.Union[str, typing.Literal['auto'], NoneType]` |

### Methods

| Method | Description |
|-|-|
| [`get_device()`](#get_device) | Get the accelerator string for the task. |
| [`get_shared_memory()`](#get_shared_memory) | Get the shared memory string for the task. |


#### get_device()

```python
def get_device()
```
Get the accelerator string for the task.

:return: If GPUs are requested, return a tuple of the device name, and potentially a partition string.
         Default cloud provider labels typically use the following values: `1g.5gb`, `2g.10gb`, etc.


#### get_shared_memory()

```python
def get_shared_memory()
```
Get the shared memory string for the task.

:return: The shared memory string.


## flyte.RetryStrategy

Retry strategy for the task or task environment. Retry strategy is optional or can be a simple number of retries.

Example:
- This will retry the task 5 times.
```
@task(retries=5)
def my_task():
    pass
```
- This will retry the task 5 times with a maximum backoff of 10 seconds and a backoff factor of 2.
```
@task(retries=RetryStrategy(count=5, max_backoff=10, backoff=2))
def my_task():
    pass
```



```python
class RetryStrategy(
    count: int,
    backoff: typing.Union[float, datetime.timedelta, NoneType],
    backoff_factor: typing.Union[int, float, NoneType],
)
```
| Parameter | Type |
|-|-|
| `count` | `int` |
| `backoff` | `typing.Union[float, datetime.timedelta, NoneType]` |
| `backoff_factor` | `typing.Union[int, float, NoneType]` |

## flyte.ReusePolicy

ReusePolicy can be used to configure a task to reuse the environment. This is useful when the environment creation
is expensive and the runtime of the task is short. The environment will be reused for the next invocation of the
task, even the python process maybe be reused by subsequent task invocations. A good mental model is to think of
the environment as a container that is reused for multiple tasks, more like a long-running service.

Caution: It is important to note that the environment is shared, so managing memory and resources is important.



```python
class ReusePolicy(
    replicas: typing.Union[int, typing.Tuple[int, int]],
    idle_ttl: typing.Union[int, datetime.timedelta, NoneType],
)
```
| Parameter | Type |
|-|-|
| `replicas` | `typing.Union[int, typing.Tuple[int, int]]` |
| `idle_ttl` | `typing.Union[int, datetime.timedelta, NoneType]` |

## flyte.Secret

Secrets are used to inject sensitive information into tasks. Secrets can be mounted as environment variables or
files. The secret key is the name of the secret in the secret store. The group is optional and maybe used with some
secret stores to organize secrets. The secret_mount is used to specify how the secret should be mounted. If the
secret_mount is set to "env" the secret will be mounted as an environment variable. If the secret_mount is set to
"file" the secret will be mounted as a file. The as_env_var is an optional parameter that can be used to specify the
name of the environment variable that the secret should be mounted as.

Example:
```python
@task(secrets="MY_SECRET")
async def my_task():
    os.environ["MY_SECRET"]  # This will be set to the value of the secret

@task(secrets=Secret("MY_SECRET", mount="/path/to/secret"))
async def my_task2():
    async with open("/path/to/secret") as f:
        secret_value = f.read()
```

TODO: Add support for secret versioning (some stores) and secret groups (some stores) and mounting as files.



```python
class Secret(
    key: str,
    group: typing.Optional[str],
    mount: pathlib._local.Path | None,
    as_env_var: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `key` | `str` |
| `group` | `typing.Optional[str]` |
| `mount` | `pathlib._local.Path \| None` |
| `as_env_var` | `typing.Optional[str]` |

## flyte.TaskEnvironment

Environment class to define a new environment for a set of tasks.

Example usage:
```python
env = flyte.TaskEnvironment(name="my_env", image="my_image", resources=Resources(cpu="1", memory="1Gi"))

@env.task
async def my_task():
    pass
```



```python
class TaskEnvironment(
    name: str,
    env_dep_hints: List[Environment],
    pod_template: Optional[Union[str, 'V1PodTemplate']],
    description: Optional[str],
    secrets: Optional[SecretRequest],
    env: Optional[Dict[str, str]],
    resources: Optional[Resources],
    image: Union[str, Image, Literal['auto']],
    cache: Union[CacheRequest],
    reusable: ReusePolicy | None,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `env_dep_hints` | `List[Environment]` |
| `pod_template` | `Optional[Union[str, 'V1PodTemplate']]` |
| `description` | `Optional[str]` |
| `secrets` | `Optional[SecretRequest]` |
| `env` | `Optional[Dict[str, str]]` |
| `resources` | `Optional[Resources]` |
| `image` | `Union[str, Image, Literal['auto']]` |
| `cache` | `Union[CacheRequest]` |
| `reusable` | `ReusePolicy \| None` |

### Methods

| Method | Description |
|-|-|
| [`add_dependency()`](#add_dependency) | Add a dependency to the environment. |
| [`add_task()`](#add_task) | Add a task to the environment. |
| [`clone_with()`](#clone_with) | Clone the TaskEnvironment with new parameters. |
| [`task()`](#task) |  |


#### add_dependency()

```python
def add_dependency(
    env: Environment,
)
```
Add a dependency to the environment.


| Parameter | Type |
|-|-|
| `env` | `Environment` |

#### add_task()

```python
def add_task(
    task: TaskTemplate,
) -> TaskTemplate
```
Add a task to the environment.


| Parameter | Type |
|-|-|
| `task` | `TaskTemplate` |

#### clone_with()

```python
def clone_with(
    name: str,
    image: Optional[Union[str, Image, Literal['auto']]],
    resources: Optional[Resources],
    env: Optional[Dict[str, str]],
    secrets: Optional[SecretRequest],
    env_dep_hints: Optional[List[Environment]],
    kwargs: **kwargs,
) -> TaskEnvironment
```
Clone the TaskEnvironment with new parameters.
besides the base environment parameters, you can override, kwargs like `cache`, `reusable`, etc.


| Parameter | Type |
|-|-|
| `name` | `str` |
| `image` | `Optional[Union[str, Image, Literal['auto']]]` |
| `resources` | `Optional[Resources]` |
| `env` | `Optional[Dict[str, str]]` |
| `secrets` | `Optional[SecretRequest]` |
| `env_dep_hints` | `Optional[List[Environment]]` |
| `kwargs` | `**kwargs` |

#### task()

```python
def task(
    _func,
    name: Optional[str],
    cache: Union[CacheRequest] | None,
    retries: Union[int, RetryStrategy],
    timeout: Union[timedelta, int],
    docs: Optional[Documentation],
    secrets: Optional[SecretRequest],
    pod_template: Optional[Union[str, 'V1PodTemplate']],
    report: bool,
) -> Union[AsyncFunctionTaskTemplate, Callable[P, R]]
```
| Parameter | Type |
|-|-|
| `_func` |  |
| `name` | `Optional[str]` |
| `cache` | `Union[CacheRequest] \| None` |
| `retries` | `Union[int, RetryStrategy]` |
| `timeout` | `Union[timedelta, int]` |
| `docs` | `Optional[Documentation]` |
| `secrets` | `Optional[SecretRequest]` |
| `pod_template` | `Optional[Union[str, 'V1PodTemplate']]` |
| `report` | `bool` |

### Properties

| Property | Type | Description |
|-|-|-|
| `tasks` |  | {{< multiline >}}Get all tasks defined in the environment.
{{< /multiline >}} |

## flyte.Timeout

Timeout class to define a timeout for a task.
The task timeout can be set to a maximum runtime and a maximum queued time.
Maximum runtime is the maximum time the task can run for (in one attempt).
Maximum queued time is the maximum time the task can stay in the queue before it starts executing.

Example usage:
```python
timeout = Timeout(max_runtime=timedelta(minutes=5), max_queued_time=timedelta(minutes=10))
@env.task(timeout=timeout)
async def my_task():
    pass
```


```python
class Timeout(
    max_runtime: datetime.timedelta | int,
    max_queued_time: datetime.timedelta | int | None,
)
```
| Parameter | Type |
|-|-|
| `max_runtime` | `datetime.timedelta \| int` |
| `max_queued_time` | `datetime.timedelta \| int \| None` |

