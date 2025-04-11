---
title: union
version: 0.1.0
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# union


Union SDK for authoring Compound AI applications, services and workflows.

## Environments

Environment class to define a new environment for a set of tasks.

Example usage:

```python
env = Environment(name="my_env", image="my_image", resources=Resources(cpu="1", memory="1Gi"))

@env.task
async def my_task():
    pass
```

## Directory

### Classes

| Class | Description |
|-|-|
| [`Environment`](.././union#unionenvironment) | Environment class to define a new environment for a set of tasks. |
| [`Image`](.././union#unionimage) | This is an abstract representation of Container Images, which can be used to create layered images programmatically. |
| [`Resources`](.././union#unionresources) | Resources such as CPU, Memory, and GPU that can be allocated to a task. |
| [`ReusePolicy`](.././union#unionreusepolicy) | ReusePolicy can be used to configure a task to reuse the environment. |
| [`Secret`](.././union#unionsecret) | Secrets are used to inject sensitive information into tasks. |

### Methods

| Method | Description |
|-|-|
| [`ctx()`](#ctx) | Retrieve the current task context from the context variable. |
| [`group()`](#group) | Create a new group with the given name. |
| [`init()`](#init) | Initialize the Union system with the given configuration. |
| [`with_runcontext()`](#with_runcontext) | Create a new `AsyncRunnable` instance with the given run context. |


## Methods

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

#### init()

```python
def init(
    root_dir: Path | None,
    api_key: str | None,
    endpoint: str | None,
    headless: bool,
    project: str | None,
    domain: str | None,
    mode: Mode,
    controller_sync_period_seconds: float,
    controller_max_concurrent_launches: int,
    interactive: Literal['auto', 'on', 'off'],
    log_level: int,
)
```
Initialize the Union system with the given configuration. This method should be called before any other Union
remote API methods are called. Thread-safe implementation.



| Parameter | Type |
|-|-|
| `root_dir` | `Path \| None` |
| `api_key` | `str \| None` |
| `endpoint` | `str \| None` |
| `headless` | `bool` |
| `project` | `str \| None` |
| `domain` | `str \| None` |
| `mode` | `Mode` |
| `controller_sync_period_seconds` | `float` |
| `controller_max_concurrent_launches` | `int` |
| `interactive` | `Literal['auto', 'on', 'off']` |
| `log_level` | `int` |

#### with_runcontext()

```python
def with_runcontext(
    name: Optional[str],
    service_account: Optional[str],
    version: Optional[str],
) -> _Runner
```
Create a new `AsyncRunnable` instance with the given run context.

Example:
```python
import union
env = union.Environment("example")

@env.task
async def example_task(x: int, y: str) -> str:
    return f"{x} {y}"

if __name__ == "__main__":
    union.with_runcontext(run_id="example_run_id").run(example_task, 1, y="hello")
```



| Parameter | Type |
|-|-|
| `name` | `Optional[str]` |
| `service_account` | `Optional[str]` |
| `version` | `Optional[str]` |

## union.Environment

Environment class to define a new environment for a set of tasks.

Example usage:
```python
env = Environment(name="my_env", image="my_image", resources=Resources(cpu="1", memory="1Gi"))

@env.task
async def my_task():
    pass
```



```python
class Environment(
    name: str,
    image: Union[str, Image, Literal['auto']],
    resources: Optional[Resources],
    cache: Union[CacheRequest],
    env: Optional[Dict[str, str]],
    reusable: Union[ReusePolicy, Literal['auto'], None],
    secrets: Optional[SecretRequest],
    description: Optional[str],
    pod_template: Optional[Union[str, 'V1PodTemplate']],
    env_dep_hints: List[Environment],
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `image` | `Union[str, Image, Literal['auto']]` |
| `resources` | `Optional[Resources]` |
| `cache` | `Union[CacheRequest]` |
| `env` | `Optional[Dict[str, str]]` |
| `reusable` | `Union[ReusePolicy, Literal['auto'], None]` |
| `secrets` | `Optional[SecretRequest]` |
| `description` | `Optional[str]` |
| `pod_template` | `Optional[Union[str, 'V1PodTemplate']]` |
| `env_dep_hints` | `List[Environment]` |

### Methods

| Method | Description |
|-|-|
| [`add_dependency()`](#add_dependency) | Add a dependency to the environment. |
| [`add_task()`](#add_task) | Add a task to the environment. |
| [`clone_with()`](#clone_with) | Clone the environment with new settings. |
| [`set_built_image()`](#set_built_image) |  |


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
) -> TaskAPI
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
    cache: Union[CacheRequest, None],
    env: Optional[Dict[str, str]],
    reusable: Union[ReusePolicy, None],
    secrets: Optional[SecretRequest],
    env_dep_hints: Optional[List[Environment]],
) -> Environment
```
Clone the environment with new settings.


| Parameter | Type |
|-|-|
| `name` | `str` |
| `image` | `Optional[Union[str, Image, Literal['auto']]]` |
| `resources` | `Optional[Resources]` |
| `cache` | `Union[CacheRequest, None]` |
| `env` | `Optional[Dict[str, str]]` |
| `reusable` | `Union[ReusePolicy, None]` |
| `secrets` | `Optional[SecretRequest]` |
| `env_dep_hints` | `Optional[List[Environment]]` |

#### set_built_image()

```python
def set_built_image(
    image: str,
)
```
| Parameter | Type |
|-|-|
| `image` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| `task` |  | {{< multiline >}}Decorator to create a new task with the environment settings.
The task will be executed in its own container with the specified image, resources, and environment variables,
unless reusePolicy is set, in which case the same container will be reused for all tasks with the same
environment settings.

{{< /multiline >}} |
| `tasks` |  | {{< multiline >}}Get all tasks defined in the environment.
{{< /multiline >}} |

## union.Image

This is an abstract representation of Container Images, which can be used to create layered images programmatically.


```python
def Image()
```
### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Use this method to create a new image with the auto image. |
| [`ubuntu_python()`](#ubuntu_python) | Use this method to create a new image with the default ubuntu-python image. |
| [`with_apt_packages()`](#with_apt_packages) | Use this method to create a new image with the specified apt packages layered on top of the current image. |
| [`with_commands()`](#with_commands) | Use this method to create a new image with the specified commands layered on top of the current image. |
| [`with_conda_packages()`](#with_conda_packages) | Use this method to create a new image with the specified conda packages layered on top of the current image. |
| [`with_pip_packages()`](#with_pip_packages) | Use this method to create a new image with the specified pip packages layered on top of the current image. |
| [`with_poetry()`](#with_poetry) | Use this method to create a new image with the specified poetry file layered on top of the current image. |
| [`with_registry()`](#with_registry) | Use this method to create a new image with the specified registry. |
| [`with_requirements()`](#with_requirements) | Use this method to create a new image with the specified requirements file layered on top of the current image. |
| [`with_source()`](#with_source) | Use this method to create a new image with the specified source code layered on top of the current image. |
| [`with_uvlock()`](#with_uvlock) | Use this method to create a new image with the specified uvlock file layered on top of the current image. |


#### auto()

```python
def auto()
```
Use this method to create a new image with the auto image

:return: Image


#### ubuntu_python()

```python
def ubuntu_python(
    name: str,
    platform: Architecture,
) -> Image
```
Use this method to create a new image with the default ubuntu-python image



| Parameter | Type |
|-|-|
| `name` | `str` |
| `platform` | `Architecture` |

#### with_apt_packages()

```python
def with_apt_packages(
    packages: List[str],
) -> Image
```
Use this method to create a new image with the specified apt packages layered on top of the current image



| Parameter | Type |
|-|-|
| `packages` | `List[str]` |

#### with_commands()

```python
def with_commands(
    commands: List[str],
) -> Image
```
Use this method to create a new image with the specified commands layered on top of the current image



| Parameter | Type |
|-|-|
| `commands` | `List[str]` |

#### with_conda_packages()

```python
def with_conda_packages(
    packages: List[str],
    channels: Optional[List[str]],
) -> Image
```
Use this method to create a new image with the specified conda packages layered on top of the current image



| Parameter | Type |
|-|-|
| `packages` | `List[str]` |
| `channels` | `Optional[List[str]]` |

#### with_pip_packages()

```python
def with_pip_packages(
    packages: List[str],
) -> Image
```
Use this method to create a new image with the specified pip packages layered on top of the current image

Example:
```python
@union.task(image=(union.Image
                .ubuntu_python()
                .with_pip_packages(["requests", "numpy"])))
def my_task(x: int) -> int:
    import numpy as np
    return np.sum([x, 1])
```



| Parameter | Type |
|-|-|
| `packages` | `List[str]` |

#### with_poetry()

```python
def with_poetry(
    file: Path,
) -> Image
```
Use this method to create a new image with the specified poetry file layered on top of the current image



| Parameter | Type |
|-|-|
| `file` | `Path` |

#### with_registry()

```python
def with_registry(
    url: str,
) -> Image
```
Use this method to create a new image with the specified registry



| Parameter | Type |
|-|-|
| `url` | `str` |

#### with_requirements()

```python
def with_requirements(
    file: Path,
) -> Image
```
Use this method to create a new image with the specified requirements file layered on top of the current image



| Parameter | Type |
|-|-|
| `file` | `Path` |

#### with_source()

```python
def with_source(
    root: Path,
) -> Image
```
Use this method to create a new image with the specified source code layered on top of the current image



| Parameter | Type |
|-|-|
| `root` | `Path` |

#### with_uvlock()

```python
def with_uvlock(
    file: Path,
) -> Image
```
Use this method to create a new image with the specified uvlock file layered on top of the current image



| Parameter | Type |
|-|-|
| `file` | `Path` |

### Properties

| Property | Type | Description |
|-|-|-|
| `uri` |  | {{< multiline >}}Returns the URI of the image in the format <registry>/<name>:<tag>
{{< /multiline >}} |

## union.Resources

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
    gpu: typing.Union[typing.Literal['T4:1', 'T4:2', 'T4:3', 'T4:4', 'T4:5', 'T4:6', 'T4:7', 'T4:8', 'L4:1', 'L4:2', 'L4:3', 'L4:4', 'L4:5', 'L4:6', 'L4:7', 'L4:8', 'L40s:1', 'L40s:2', 'L40s:3', 'L40s:4', 'L40s:5', 'L40s:6', 'L40s:7', 'L40s:8', 'A100:1', 'A100:2', 'A100:3', 'A100:4', 'A100:5', 'A100:6', 'A100:7', 'A100:8', 'A100 80G:1', 'A100 80G:2', 'A100 80G:3', 'A100 80G:4', 'A100 80G:5', 'A100 80G:6', 'A100 80G:7', 'A100 80G:8', 'H100:1', 'H100:2', 'H100:3', 'H100:4', 'H100:5', 'H100:6', 'H100:7', 'H100:8'], int, NoneType],
    disk: typing.Optional[str],
    shared_memory: typing.Union[str, typing.Literal['auto'], NoneType],
)
```
| Parameter | Type |
|-|-|
| `cpu` | `typing.Union[int, float, str, typing.Tuple[int \| float \| str, int \| float \| str], NoneType]` |
| `memory` | `typing.Union[str, typing.Tuple[str, str], NoneType]` |
| `gpu` | `typing.Union[typing.Literal['T4:1', 'T4:2', 'T4:3', 'T4:4', 'T4:5', 'T4:6', 'T4:7', 'T4:8', 'L4:1', 'L4:2', 'L4:3', 'L4:4', 'L4:5', 'L4:6', 'L4:7', 'L4:8', 'L40s:1', 'L40s:2', 'L40s:3', 'L40s:4', 'L40s:5', 'L40s:6', 'L40s:7', 'L40s:8', 'A100:1', 'A100:2', 'A100:3', 'A100:4', 'A100:5', 'A100:6', 'A100:7', 'A100:8', 'A100 80G:1', 'A100 80G:2', 'A100 80G:3', 'A100 80G:4', 'A100 80G:5', 'A100 80G:6', 'A100 80G:7', 'A100 80G:8', 'H100:1', 'H100:2', 'H100:3', 'H100:4', 'H100:5', 'H100:6', 'H100:7', 'H100:8'], int, NoneType]` |
| `disk` | `typing.Optional[str]` |
| `shared_memory` | `typing.Union[str, typing.Literal['auto'], NoneType]` |

### Methods

| Method | Description |
|-|-|
| [`get_accelerator()`](#get_accelerator) | Get the accelerator string for the task. |
| [`get_shared_memory()`](#get_shared_memory) | Get the shared memory string for the task. |


#### get_accelerator()

```python
def get_accelerator()
```
Get the accelerator string for the task.

:return: The accelerator string.


#### get_shared_memory()

```python
def get_shared_memory()
```
Get the shared memory string for the task.

:return: The shared memory string.


## union.ReusePolicy

ReusePolicy can be used to configure a task to reuse the environment. This is useful when the environment creation
is expensive and the runtime of the task is short. The environment will be reused for the next invocation of the
task, even the python process maybe be reused by subsequent task invocations. A good mental model is to think of
the environment as a container that is reused for multiple tasks, more like a long-running service.

Caution: It is important to note that the environment is shared, so managing memory and resources is important.



```python
class ReusePolicy(
    replicas: typing.Union[int, typing.Tuple[int, int]],
    ttl: typing.Union[int, datetime.timedelta, NoneType],
)
```
| Parameter | Type |
|-|-|
| `replicas` | `typing.Union[int, typing.Tuple[int, int]]` |
| `ttl` | `typing.Union[int, datetime.timedelta, NoneType]` |

## union.Secret

Secrets are used to inject sensitive information into tasks. Secrets can be mounted as environment variables or
files. The secret key is the name of the secret in the secret store. The group is optional and maybe used with some
secret stores to organize secrets. The secret_mount is used to specify how the secret should be mounted. If the
secret_mount is set to "env" the secret will be mounted as an environment variable. If the secret_mount is set to
"file" the secret will be mounted as a file. The as_env_var is an optional parameter that can be used to specify the
name of the environment variable that the secret should be mounted as.

Example:
```python
@task(secrets="my_secret")
def my_task():
    pass

@task(secrets=Secret("my_secret", secret_mount="file"))
def my_task2():
    pass
```



```python
class Secret(
    key: str,
    group: typing.Optional[str],
    secret_mount: typing.Literal['env', 'file'],
    as_env_var: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `key` | `str` |
| `group` | `typing.Optional[str]` |
| `secret_mount` | `typing.Literal['env', 'file']` |
| `as_env_var` | `typing.Optional[str]` |

