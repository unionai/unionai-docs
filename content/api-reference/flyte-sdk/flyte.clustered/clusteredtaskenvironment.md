---
title: ClusteredTaskEnvironment
version: 2.6.6
variants: +flyte +union
layout: py_api
---

# ClusteredTaskEnvironment

**Package:** `flyte.clustered`

A TaskEnvironment that emits a Kubernetes JobSet for distributed multi-node training.

Inherits all fields from TaskEnvironment (name, image, resources, env_vars, secrets,
pod_template, queue, cache, reusable). The fields below are specific to clustered execution.



## Parameters

```python
class ClusteredTaskEnvironment(
    name: str,
    depends_on: List[Environment] = <factory>,
    pod_template: Optional[Union[str, PodTemplate]] = None,
    description: Optional[str] = None,
    secrets: Optional[SecretRequest] = None,
    env_vars: Optional[Dict[str, str]] = None,
    resources: Optional[Resources] = None,
    interruptible: bool = False,
    image: Union[str, Image, Literal['auto'], None] = 'auto',
    include: Tuple[str, ...] = <factory>,
    cache: CacheRequest = 'disable',
    reusable: ReusePolicy | None = None,
    plugin_config: Optional[Any] = None,
    queue: Optional[str] = None,
    replicas: int,
    nproc_per_node: int,
    runtime: Runtime = <factory>,
    interconnect: Literal['tcp'] = 'tcp',
    failure_policy: ClusterFailurePolicy = <factory>,
    ttl_seconds_after_finished: Optional[int] = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `depends_on` | `List[Environment]` | |
| `pod_template` | `Optional[Union[str, PodTemplate]]` | |
| `description` | `Optional[str]` | |
| `secrets` | `Optional[SecretRequest]` | |
| `env_vars` | `Optional[Dict[str, str]]` | |
| `resources` | `Optional[Resources]` | |
| `interruptible` | `bool` | |
| `image` | `Union[str, Image, Literal['auto'], None]` | |
| `include` | `Tuple[str, ...]` | |
| `cache` | `CacheRequest` | |
| `reusable` | `ReusePolicy \| None` | |
| `plugin_config` | `Optional[Any]` | |
| `queue` | `Optional[str]` | |
| `replicas` | `int` | Number of pods (== number of nodes). Required. |
| `nproc_per_node` | `int` | Number of processes per pod, passed to `torchrun --nproc-per-node`. Must be &gt;= 1 and, when resources.gpu is set, &lt;= resources.gpu. Required. |
| `runtime` | `Runtime` | Launcher configuration. Phase 1 supports only TorchRun(). |
| `interconnect` | `Literal['tcp']` | Network fabric. Currently only "tcp" is supported. |
| `failure_policy` | `ClusterFailurePolicy` | JobSet-level restart and eviction policy. |
| `ttl_seconds_after_finished` | `Optional[int]` | Seconds to retain the JobSet after completion. |

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
| [`to_custom_dict()`](#to_custom_dict) | Serialize this environment to the dict shape expected by ClusteredTaskSpec proto. |


### add_dependency()

```python
def add_dependency(
    *env: Environment,
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
| `*env` | `Environment` | One or more `Environment` instances to add as dependencies. |

### clone_with()

```python
def clone_with(
    name: str,
    image: Optional[Union[str, Image, Literal['auto']]] = None,
    resources: Optional[Resources] = None,
    env_vars: Optional[Dict[str, str]] = None,
    secrets: Optional[SecretRequest] = None,
    depends_on: Optional[List[Environment]] = None,
    description: Optional[str] = None,
    interruptible: Optional[bool] = None,
    include: Optional[Tuple[str, ...]] = None,
    **kwargs: Any,
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
| `**kwargs` | `Any` | Additional `TaskEnvironment`-specific overrides (e.g., `cache`, `reusable`, `plugin_config`). |

### from_task()

```python
def from_task(
    name: str,
    *tasks: TaskTemplate,
    depends_on: Optional[List['Environment']] = None,
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
| `*tasks` | `TaskTemplate` | The list of tasks to create the environment from. |
| `depends_on` | `Optional[List['Environment']]` | Optional list of environments that this environment depends on. |

**Returns**

The created TaskEnvironment.


**Raises**

| Exception | Description |
|-|-|
| `ValueError` | If tasks are assigned to multiple environments or have different images. |

### task()

```python
def task(
    _func: F | None = None,
    short_name: Optional[str] = None,
    cache: CacheRequest | None = None,
    retries: Union[int, RetryStrategy] = 0,
    timeout: TimeoutType = 0,
    docs: Optional[Documentation] = None,
    pod_template: Optional[Union[str, PodTemplate]] = None,
    report: bool = False,
    interruptible: bool | None = None,
    max_inline_io_bytes: int = 10485760,
    queue: Optional[str] = None,
    triggers: Tuple[Trigger, ...] | Trigger = (),
    links: Tuple[Link, ...] | Link = (),
    task_resolver: Any | None = None,
    entrypoint: bool = False,
    produces_artifacts: bool = False,
) -> Callable[[F], AsyncFunctionTaskTemplate[P, R, F]] | AsyncFunctionTaskTemplate[P, R, F]
```
Decorate a function to be a task.



| Parameter | Type | Description |
|-|-|-|
| `_func` | `F \| None` | Optional The function to decorate. If not provided, the decorator will return a callable that accepts a function to be decorated. |
| `short_name` | `Optional[str]` | Optional friendly name for the task or action, used in parts of the UI (defaults to the function name). Overriding `short_name` does not change the task's fully-qualified name. |
| `cache` | `CacheRequest \| None` | Optional The cache policy for the task, defaults to auto, which will cache the results of the task. |
| `retries` | `Union[int, RetryStrategy]` | Number of user retries (`int`) or a `RetryStrategy` object. `RetryStrategy` accepts an optional `backoff=Backoff(base, factor, cap)` to pace retries exponentially. Defaults to `0` (no retries). |
| `timeout` | `TimeoutType` | Task timeout. Accepts a `timedelta`, an integer number of seconds, or a `Timeout` object carrying any combination of `max_runtime`, `max_queued_time`, and `deadline`. A bare `timedelta`/`int` is interpreted as `max_runtime`. A bound is treated as unlimited when unset (`None`) or zero (`0` / `timedelta(0)`); `timeout=0` is the default and means no time bound. |
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
| `produces_artifacts` | `bool` | Optional Whether the backend should extract artifact metadata stamped on this task's output literals (via `flyte.artifacts.new(...)`) and record them as generated artifacts on the action, defaults to False. |

**Returns:** A TaskTemplate that can be used to deploy the task.

### to_custom_dict()

```python
def to_custom_dict()
```
Serialize this environment to the dict shape expected by ClusteredTaskSpec proto.

Imported lazily so the heavy clustered_pb2 module is only loaded at serialization
time rather than on every `flyte.clustered` import.


