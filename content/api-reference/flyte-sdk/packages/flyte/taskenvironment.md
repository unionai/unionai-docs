---
title: TaskEnvironment
version: 2.2.1
variants: +flyte +union
layout: py_api
---

# TaskEnvironment

**Package:** `flyte`

Define an execution environment for a set of tasks.

Task configuration in Flyte has three levels (most general to most specific):

1. **TaskEnvironment** — sets defaults for all tasks in the environment
2. **@env.task decorator** — overrides per-task settings
3. **task.override()** — overrides at invocation time

For shared parameters, the more specific level overrides the more general one.

```python
env = flyte.TaskEnvironment(
    name="my_env",
    image=flyte.Image.from_debian_base(python="3.12").with_pip_packages("pandas"),
    resources=flyte.Resources(cpu="1", memory="1Gi"),
)

@env.task
async def my_task():
    pass
```

**Parameter interaction across configuration levels:**

| Parameter | `TaskEnvironment` | `@env.task` | `task.override()` |
|-----------|:-----------------:|:-----------:|:-----------------:|
| `name` | Yes (required) | — | — |
| `image` | Yes | — | — |
| `depends_on` | Yes | — | — |
| `description` | Yes | — | — |
| `plugin_config` | Yes | — | — |
| `resources` | Yes | — | Yes* |
| `env_vars` | Yes | — | Yes* |
| `secrets` | Yes | — | Yes* |
| `cache` | Yes | Yes | Yes |
| `pod_template` | Yes | Yes | Yes |
| `reusable` | Yes | — | Yes |
| `interruptible` | Yes | Yes | Yes |
| `queue` | Yes | Yes | Yes |
| `short_name` | — | Yes | Yes |
| `retries` | — | Yes | Yes |
| `timeout` | — | Yes | Yes |
| `max_inline_io_bytes` | — | Yes | Yes |
| `links` | — | Yes | Yes |
| `report` | — | Yes | — |
| `triggers` | — | Yes | — |
| `docs` | — | Yes | — |

*When `reusable` is set, `resources`, `env_vars`, and `secrets` can only
be overridden via `task.override()` with `reusable="off"` in the same call.



## Parameters

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
    image: Union[str, Image, Literal['auto'], None],
    include: Tuple[str, ...],
    cache: CacheRequest,
    reusable: ReusePolicy | None,
    plugin_config: Optional[Any],
    queue: Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Name of the environment (required). Must be snake_case or kebab-case. TaskEnvironment level only. The fully-qualified name of each task is `&lt;env_name&gt;.&lt;function_name&gt;` (e.g., environment `"my_env"` containing function `my_task` produces FQN `"my_env.my_task"`). Neither component is overridable. |
| `depends_on` | `List[Environment]` | List of other environments this one depends on. Used at deploy time to ensure dependencies are also deployed. TaskEnvironment level only. |
| `pod_template` | `Optional[Union[str, PodTemplate]]` | Kubernetes pod template for advanced configuration (sidecars, volumes, etc.). Also settable in `@env.task` and `task.override`. |
| `description` | `Optional[str]` | Human-readable description (max 255 characters). TaskEnvironment level only. |
| `secrets` | `Optional[SecretRequest]` | Secrets to inject. Overridable via `task.override(secrets=...)` when not using reusable containers. |
| `env_vars` | `Optional[Dict[str, str]]` | Environment variables as `dict[str, str]`. Overridable via `task.override(env_vars=...)` when not using reusable containers. |
| `resources` | `Optional[Resources]` | Compute resources (CPU, memory, GPU, disk). Overridable via `task.override(resources=...)` when not using reusable containers. |
| `interruptible` | `bool` | Whether tasks can run on spot/preemptible instances. Also settable in `@env.task` and `task.override`. |
| `image` | `Union[str, Image, Literal['auto'], None]` | Docker image for the environment. Can be a string (image URI), an `Image` object, or `"auto"` to use the default image. TaskEnvironment level only. |
| `include` | `Tuple[str, ...]` | |
| `cache` | `CacheRequest` | Cache policy — `"auto"`, `"override"`, `"disable"`, or a `Cache` object. Also settable in `@env.task(cache=...)` and `task.override(cache=...)`. |
| `reusable` | `ReusePolicy \| None` | `ReusePolicy` for container reuse. Also overridable via `task.override(reusable=...)`. Note: when `reusable` is set on the environment, overriding `resources`, `env_vars`, or `secrets` in `task.override()` requires passing `reusable="off"` in the same call. Additionally, `secrets` cannot be overridden at the `@env.task` decorator level when the environment has `reusable` set. |
| `plugin_config` | `Optional[Any]` | Plugin configuration for custom task types (e.g., Ray, Spark). Cannot be combined with `reusable`. TaskEnvironment level only. |
| `queue` | `Optional[str]` | Queue name for scheduling. Queues identify specific partitions of your compute infrastructure (e.g., a particular cluster in a multi-cluster deployment) and are configured as part of your Flyte/Union deployment. Also settable in `@env.task` and `task.override`. |

## Properties

| Property | Type | Description |
|-|-|-|
| `sandbox` | `_SandboxNamespace` | Access the sandbox namespace for creating sandboxed tasks. |
| `tasks` | `Dict[str, TaskTemplate]` | Get all tasks defined in the environment. |

## Methods

| Method | Description |
|-|-|
| [`add_dependency()`](#add_dependency) | Add one or more environment dependencies so they are deployed together. |
| [`clone_with()`](#clone_with) | Create a new `TaskEnvironment` that shares most settings with this one. |
| [`from_task()`](#from_task) | Create a TaskEnvironment from a list of tasks. |
| [`task()`](#task) | Decorate a function to be a task. |


### add_dependency()

```python
def add_dependency(
    env: Environment,
)
```
Add one or more environment dependencies so they are deployed together.

When you deploy this environment, any environments added via
`add_dependency` will also be deployed. This is an alternative to
passing `depends_on=[...]` at construction time, useful when the
dependency is defined after the environment is created.

Duplicate dependencies are silently ignored. An environment cannot
depend on itself.



| Parameter | Type | Description |
|-|-|-|
| `env` | `Environment` | One or more `Environment` instances to add as dependencies. |

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
    include: Optional[Tuple[str, ...]],
    kwargs: **kwargs,
) -> TaskEnvironment
```
Create a new `TaskEnvironment` that shares most settings with this one
but differs in name and selected overrides.

Use `clone_with` when you need several environments that share a common
base configuration (image, resources, secrets, etc.) but vary in one or
two settings, avoiding repetition.

```python
gpu_env = flyte.TaskEnvironment(
    name="gpu_env",
    image=my_image,
    resources=flyte.Resources(gpu="A100:1", memory="16Gi"),
)

# Same image and resources, different name and cache policy
gpu_env_cached = gpu_env.clone_with("gpu_env_cached", cache="auto")
```

Any parameter not explicitly passed inherits the value from the
original environment.



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Name for the new environment (required). |
| `image` | `Optional[Union[str, Image, Literal['auto']]]` | Override the container image. |
| `resources` | `Optional[Resources]` | Override compute resources. |
| `env_vars` | `Optional[Dict[str, str]]` | Override environment variables. |
| `secrets` | `Optional[SecretRequest]` | Override secrets. |
| `depends_on` | `Optional[List[Environment]]` | Override deployment dependencies. |
| `description` | `Optional[str]` | Override the description. |
| `interruptible` | `Optional[bool]` | Override the interruptible setting. |
| `include` | `Optional[Tuple[str, ...]]` | |
| `kwargs` | `**kwargs` | Additional `TaskEnvironment`-specific overrides (e.g., `cache`, `reusable`, `plugin_config`). |

### from_task()

```python
def from_task(
    name: str,
    tasks: TaskTemplate,
    depends_on: Optional[List['Environment']],
) -> TaskEnvironment
```
Create a TaskEnvironment from a list of tasks. All tasks should have the same image or no Image defined.
Similarity of Image is determined by the python reference, not by value.

If images are different, an error is raised. If no image is defined, the image is set to "auto".

For any other tasks that need to be use by these tasks, the returned environment can be used in the `depends_on`
attribute of the other TaskEnvironment.



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | The name of the environment. |
| `tasks` | `TaskTemplate` | The list of tasks to create the environment from. |
| `depends_on` | `Optional[List['Environment']]` | Optional list of environments that this environment depends on. |

**Returns:** The created TaskEnvironment.

**Raises**

| Exception | Description |
|-|-|
| `ValueError` | If tasks are assigned to multiple environments or have different images. |

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
    task_resolver: Any | None,
    entrypoint: bool,
) -> Callable[[F], AsyncFunctionTaskTemplate[P, R, F]] | AsyncFunctionTaskTemplate[P, R, F]
```
Decorate a function to be a task.



| Parameter | Type | Description |
|-|-|-|
| `_func` | `F \| None` | Optional The function to decorate. If not provided, the decorator will return a callable that accepts a function to be decorated. |
| `short_name` | `Optional[str]` | Optional friendly name for the task or action, used in parts of the UI (defaults to the function name). Overriding `short_name` does not change the task's fully-qualified name. |
| `cache` | `CacheRequest \| None` | Optional The cache policy for the task, defaults to auto, which will cache the results of the task. |
| `retries` | `Union[int, RetryStrategy]` | Number of retries (`int`) or a `RetryStrategy` object that defines retry behavior. Defaults to `0` (no retries). |
| `timeout` | `Union[timedelta, int]` | Task timeout, as a `timedelta` object or an integer number of seconds. `0` means no timeout. |
| `docs` | `Optional[Documentation]` | Optional The documentation for the task, if not provided the function docstring will be used. |
| `pod_template` | `Optional[Union[str, PodTemplate]]` | Optional The pod template for the task, if not provided the default pod template will be used. |
| `report` | `bool` | Optional Whether to generate the html report for the task, defaults to False. |
| `interruptible` | `bool \| None` | Optional Whether the task is interruptible, defaults to environment setting. |
| `max_inline_io_bytes` | `int` | Maximum allowed size (in bytes) for all inputs and outputs passed directly to the task (e.g., primitives, strings, dicts). Does not apply to files, directories, or dataframes. Default is 10 MiB. |
| `queue` | `Optional[str]` | Optional queue name to use for this task. If not set, the environment's queue will be used. |
| `triggers` | `Tuple[Trigger, ...] \| Trigger` | Optional A tuple of triggers to associate with the task. This allows the task to be run on a schedule or in response to events. Triggers can be defined using the `flyte.trigger` module. |
| `links` | `Tuple[Link, ...] \| Link` | Optional A tuple of links to associate with the task. Links can be used to provide additional context or information about the task. Links should implement the `flyte.Link` protocol |
| `task_resolver` | `Any \| None` | Optional TaskResolver protocol to load tasks using custom policy. |
| `entrypoint` | `bool` | Optionally mark a task as an entrypoint task, defaults to False. This serves as a hint to the UI. |

**Returns:** A TaskTemplate that can be used to deploy the task.

