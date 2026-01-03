---
title: TaskEnvironment
version: 2.0.0b43
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TaskEnvironment

**Package:** `flyte`

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
    depends_on: List[Environment],
    pod_template: Optional[Union[str, PodTemplate]],
    description: Optional[str],
    secrets: Optional[SecretRequest],
    env_vars: Optional[Dict[str, str]],
    resources: Optional[Resources],
    interruptible: bool,
    image: Union[str, Image, Literal['auto']],
    cache: CacheRequest,
    reusable: ReusePolicy | None,
    plugin_config: Optional[Any],
    queue: Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Name of the environment |
| `depends_on` | `List[Environment]` | Environment dependencies to hint, so when you deploy the environment, the dependencies are also deployed. This is useful when you have a set of environments that depend on each other. |
| `pod_template` | `Optional[Union[str, PodTemplate]]` | Optional pod template to use for tasks in this environment. If not set, the default pod template will be used. |
| `description` | `Optional[str]` | |
| `secrets` | `Optional[SecretRequest]` | Secrets to inject into the environment. |
| `env_vars` | `Optional[Dict[str, str]]` | Environment variables to set for the environment. |
| `resources` | `Optional[Resources]` | Resources to allocate for the environment. |
| `interruptible` | `bool` | |
| `image` | `Union[str, Image, Literal['auto']]` | Docker image to use for the environment. If set to "auto", will use the default image. |
| `cache` | `CacheRequest` | Cache policy for the environment. |
| `reusable` | `ReusePolicy \| None` | Reuse policy for the environment, if set, a python process may be reused for multiple tasks. |
| `plugin_config` | `Optional[Any]` | Optional plugin configuration for custom task types. If set, all tasks in this environment will use the specified plugin configuration. |
| `queue` | `Optional[str]` | Optional queue name to use for tasks in this environment. If not set, the default queue will be used. |

## Methods

| Method | Description |
|-|-|
| [`add_dependency()`](#add_dependency) | Add a dependency to the environment. |
| [`clone_with()`](#clone_with) | Clone the TaskEnvironment with new parameters. |
| [`from_task()`](#from_task) | Create a TaskEnvironment from a list of tasks. |
| [`task()`](#task) | Decorate a function to be a task. |


### add_dependency()

```python
def add_dependency(
    env: Environment,
)
```
Add a dependency to the environment.


| Parameter | Type | Description |
|-|-|-|
| `env` | `Environment` | |

### clone_with()

```python
def clone_with(
    name: str,
    image: Optional[Union[str, Image, Literal['auto']]],
    resources: Optional[Resources],
    env_vars: Optional[Dict[str, str]],
    secrets: Optional[SecretRequest],
    depends_on: Optional[List[Environment]],
    description: Optional[str],
    interruptible: Optional[bool],
    kwargs: **kwargs,
) -> TaskEnvironment
```
Clone the TaskEnvironment with new parameters.

Besides the base environment parameters, you can override kwargs like `cache`, `reusable`, etc.



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | The name of the environment. |
| `image` | `Optional[Union[str, Image, Literal['auto']]]` | The image to use for the environment. |
| `resources` | `Optional[Resources]` | The resources to allocate for the environment. |
| `env_vars` | `Optional[Dict[str, str]]` | The environment variables to set for the environment. |
| `secrets` | `Optional[SecretRequest]` | The secrets to inject into the environment. |
| `depends_on` | `Optional[List[Environment]]` | The environment dependencies to hint, so when you deploy the environment, the dependencies are also deployed. This is useful when you have a set of environments that depend on each other. |
| `description` | `Optional[str]` | The description of the environment. |
| `interruptible` | `Optional[bool]` | Whether the environment is interruptible and can be scheduled on spot/preemptible instances. |
| `kwargs` | `**kwargs` | Additional parameters to override the environment (e.g., cache, reusable, plugin_config). |

### from_task()

```python
def from_task(
    name: str,
    tasks: TaskTemplate,
) -> TaskEnvironment
```
Create a TaskEnvironment from a list of tasks. All tasks should have the same image or no Image defined.
Similarity of Image is determined by the python reference, not by value.

If images are different, an error is raised. If no image is defined, the image is set to "auto".

For any other tasks that need to be use these tasks, the returned environment can be used in the `depends_on`
attribute of the other TaskEnvironment.



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | The name of the environment. |
| `tasks` | `TaskTemplate` | The list of tasks to create the environment from.  :raises ValueError: If tasks are assigned to multiple environments or have different images. :return: The created TaskEnvironment. |

### task()

```python
def task(
    _func: F | None,
    short_name: Optional[str],
    cache: CacheRequest | None,
    retries: Union[int, RetryStrategy],
    timeout: Union[timedelta, int],
    docs: Optional[Documentation],
    pod_template: Optional[Union[str, PodTemplate]],
    report: bool,
    interruptible: bool | None,
    max_inline_io_bytes: int,
    queue: Optional[str],
    triggers: Tuple[Trigger, ...] | Trigger,
    links: Tuple[Link, ...] | Link,
) -> Callable[[F], AsyncFunctionTaskTemplate[P, R, F]] | AsyncFunctionTaskTemplate[P, R, F]
```
Decorate a function to be a task.



| Parameter | Type | Description |
|-|-|-|
| `_func` | `F \| None` | Optional The function to decorate. If not provided, the decorator will return a callable that accepts a function to be decorated. |
| `short_name` | `Optional[str]` | Optional A friendly name for the task (defaults to the function name) |
| `cache` | `CacheRequest \| None` | Optional The cache policy for the task, defaults to auto, which will cache the results of the task. |
| `retries` | `Union[int, RetryStrategy]` | Optional The number of retries for the task, defaults to 0, which means no retries. |
| `timeout` | `Union[timedelta, int]` | Optional The timeout for the task. |
| `docs` | `Optional[Documentation]` | Optional The documentation for the task, if not provided the function docstring will be used. |
| `pod_template` | `Optional[Union[str, PodTemplate]]` | Optional The pod template for the task, if not provided the default pod template will be used. |
| `report` | `bool` | Optional Whether to generate the html report for the task, defaults to False. |
| `interruptible` | `bool \| None` | Optional Whether the task is interruptible, defaults to environment setting. |
| `max_inline_io_bytes` | `int` | Maximum allowed size (in bytes) for all inputs and outputs passed directly to the task (e.g., primitives, strings, dicts). Does not apply to files, directories, or dataframes. |
| `queue` | `Optional[str]` | Optional queue name to use for this task. If not set, the environment's queue will be used.  :return: A TaskTemplate that can be used to deploy the task. |
| `triggers` | `Tuple[Trigger, ...] \| Trigger` | Optional A tuple of triggers to associate with the task. This allows the task to be run on a schedule or in response to events. Triggers can be defined using the `flyte.trigger` module. |
| `links` | `Tuple[Link, ...] \| Link` | Optional A tuple of links to associate with the task. Links can be used to provide additional context or information about the task. Links should implement the `flyte.Link` protocol |

## Properties

| Property | Type | Description |
|-|-|-|
| `tasks` | `None` | Get all tasks defined in the environment. |

