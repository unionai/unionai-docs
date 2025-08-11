---
title: Task configuration
weight: 60
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Task configuration

As we saw in [**Getting started**](../getting-started), you can run any Python function as a task in Flyte just by decorating it with `@env.task`.

This allows you to run your Python code in a distributed manner, with each function running in its own container.
Flyte manages the spinning up of the containers, the execution of the code, and the passing of data between the tasks.

In **Getting started** we demonstrated the simplest possible case, a `TaskEnvironment` with only a `name` parameter, and an `env.task` decorator, with no parameters:

```python
env = flyte.TaskEnvironment(name="hello_world")

@env.task
async def say_hello(data: str, lt: List[int]) -> str:
    ...
```

> [!NOTE]
> Notice how the `TaskEnvironment` is assigned to the variable `env` and then that variable is
> used in the `@env.task`. This is what connects the `TaskEnvironment` to the task definition.
>
> In the following we will often use `@env.task` generically to refer to the decorator,
> but it is important to remember that it is actually a decorator attached to a specific
> `TaskEnvironment` object, and the `env` part can be any variable name you like.

This will run your task in the default container environment with default settings.

But, of course, one of the key advantages of Flyte is the ability to control the software environment, hardware environment, and other execution parameters for each task, right in your Python code.
In this section we will explore the various configuration options available for tasks in Flyte.

## Task configuration levels

Task configuration is done at three levels. From most general to most specific, they are:

* The `TaskEnvironment` level: setting parameters when defining the `TaskEnvironment` object.
* The `@env.task` decorator level: Setting parameters in the `@env.task` decorator when defining a task function.
* The task invocation level: Using the `task.override()` method when invoking task execution.

Each level has its own set of parameters, and some parameters are shared across levels.
For shared parameters, the more specific level will override the more general one.

### Example

Here is an example of how these levels work together, showing each level with all available parameters:

```python
import flyte

# Level 1: TaskEnvironment - Base configuration
env = flyte.TaskEnvironment(
    name="data_processing_env",
    image=flyte.Image.from_debian_base(),
    resources=flyte.Resources(cpu=1, memory="512Mi"),
    env={"MY_VAR": "value"},
    secrets=flyte.Secret(key="my_api_key", as_env_var="MY_API_KEY"),
    cache="disable",
    pod_template=my_pod_template_spec,
    reusable=flyte.ReusePolicy(replicas=2, idle_ttl=300),
    depends_on=[another_env],
    description="My task environment",
    plugin_config=my_plugin_config
)

# Level 2: Decorator - Override some environment settings
@env.task(
    name="data_processing_task",
    secrets=flyte.Secret(key="my_api_key_2", as_env_var="MY_API_KEY"),
    cache="auto"
    pod_template=my_pod_template_spec_2,
    report=True,
    max_inline_io_bytes=100 * 1024
    retries=3,
    timeout=60
    docs="This task processes data and generates a report."
)
async def process_data(data_path: str) -> str:
    return f"Processed {data_path}"

@env.task
async def main_workflow() -> str:
    result = await process_data.override(
        resources=flyte.Resources(cpu=4, memory="2Gi"),
        env={"MY_VAR": "new_value"},
        secrets=flyte.Secret(key="my_api_key_3", as_env_var="MY_API_KEY"),
        cache="enable",
        max_inline_io_bytes=100 * 1024,
        retries=3,
        timeout=60
    )("input.csv")
    return result
```

### Parameter interaction

Here is an overview of all task configuration parameters available at each level and how they interact:

| Parameter | `TaskEnvironment` | `@env.task` decorator | `task.override()` invocation |
|-----------|-------------|-----------|------------|
| **name** | ✅ Yes (required) | ✅ Yes (sets friendly name)| ❌ No |
| **image** | ✅ Yes | ❌ No | ❌ No |
| **resources** | ✅ Yes | ❌ No | ✅ Yes (if not `reusable`) |
| **env** | ✅ Yes | ❌ No | ✅ Yes (if not `reusable`) |
| **secrets** | ✅ Yes | ✅ Yes (if not `reusable`) | ✅ Yes (if not `reusable`) |
| **cache** | ✅ Yes | ✅ Yes | ✅ Yes |
| **pod_template** | ✅ Yes | ✅ Yes | ❌ No |
| **reusable** | ✅ Yes (see below)| ❌ No | ✅ Yes |
| **depends_on** | ✅ Yes | ❌ No | ❌ No |
| **description** | ✅ Yes | ❌ No | ❌ No |
| **plugin_config** | ✅ Yes | ❌ No | ❌ No |
| **report** | ❌ No | ✅ Yes | ❌ No |
| **max_inline_io_bytes** | ❌ No | ✅ Yes | ✅ Yes |
| **retries** | ❌ No | ✅ Yes | ✅ Yes |
| **timeout** | ❌ No | ✅ Yes | ✅ Yes |
| **docs** | ❌ No | ✅ Yes | ❌ No |

## Task configuration parameters

The full set of parameters available for configuring a task environment, task definition, and task invocation are:

### `name`

* Type: `str`

* In a `TaskEnvironment` constructor it defines the name of the environment and is required.
  Used in conjunction with the name of each `@env.task` functions to define the fully-qualified task name. For example:

  ```python
  env = flyte.TaskEnvironment(name="my_env")

  @env.task
  async def my_task(data: str) -> str:
      ...
  ```

  Here, the fully qualified name of the task will be `my_env.my_task`.

* Can optionally be set in the `@env.task` decorator level, in which case it overrides,
  not the `TaskEnvironment` name but the friendly name of the task.
  By default, the friendly name of a task is the name of the function.
  The friendly name is used for display purposes in the UI.

### `image`

* Type: `Union[str, Image, Literal['auto']]`

* Specifies the Docker image to use for the task container.
  Can be a URL reference to a Docker image, an [`Image` object](../../api-reference/flyte-sdk/packages/flyte#flyteimage), or the string `auto`.
  If set to `auto`, or if this parameter is not set, the [default image]() will be used.
  See [Container images](./container-images).

* Only settable at the `TaskEnvironment` level.

### `resources`

* Type: `Optional[Resources]`

* Specifies the compute resources, such as CPU and Memory, required by the task environment using a
  [`Resources`](../../api-reference/flyte-sdk/packages/flyte#flyteresources) object.

<!-- [TODO: add when available]
  See [Resource specification](./resources) for more details.
-->

* Can be set at the `TaskEnvironment` level and overridden at the `task.override()` invocation level
  (but only if `reuseable` is not in effect).

### `env`

* Type: `Optional[Dict[str, str]]`

* A dictionary of environment variables to be made available in the task container.
  These variables can be used to configure the task at runtime, such as setting API keys or other configuration values.

### `secrets`

* Type: `Optional[SecretRequest]` where `SecretRequest` is an alias for `Union[str, Secret, List[str | Secret]]`

* The secrets to be made available in the environment.
  See the [Secrets section](./secrets) and the API docs for the [`Secret` object](../../api-reference/flyte-sdk/packages/flyte#flytesecret).

* Can be set at the `TaskEnvironment` level and overridden at the `@env.task` decorator level and at the `task.override()` invocation level, but, in both cases, only if `reuseable` is not in effect.

### `cache`

* Type: `Union[CacheRequest]` where `CacheRequest` is an alias for `Literal["auto", "override", "disable", "enabled"] | Cache`.

* Specifies the caching policy to be used for this task.
  See [Caching](./caching).

* Can be set at the `TaskEnvironment` level and overridden at the `@env.task` decorator level
  and at the `task.override()` invocation level.

### `pod_template`

* Type: `Optional[Union[str, kubernetes.client.V1PodTemplate]]`

* A pod template that defines the Kubernetes pod configuration for the task.
  A string reference to a named template or a `kubernetes.client.V1PodTemplate` object.

<!-- TODO: Add when available
See [Using pod templates](./pod-templates).
-->

* Can be set at the `TaskEnvironment` level and overridden at the `@env.task` decorator level, but not at the `task.override()` invocation level.

### `reusable`

{{< variant flyte >}}
{{< markdown >}}

> [!NOTE]
> The `reusable` setting controls the [**reusable containers** feature](./reusable-containers).
> This feature is only available when running your Flyte code on a Union.ai backend.
> See [one of the Union.ai product variants of this page]({{< docs_home byoc v2>}}/user-guide/reusable-containers) for details.

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged serverless >}}
{{< markdown >}}

* Type: `ReusePolicy | None`

* A `ReusePolicy` that defines whether the task environment can be reused.
  If set, the task environment will be reused across multiple task invocations.
  See [Reusable containers](./reusable-containers) and the API docs for the [`ReusePolicy` object](../../api-reference/flyte-sdk/packages/flyte#flytereusepolicy).


When a `TaskEnvironment` has `reusable` set, then `resources`, `env`, and `secrets` can only be overridden in `task.override()` if accompanied by an
explicit `reusable="off"` in the same `task.override()` invocation.
For example:

```python
env = flyte.TaskEnvironment(
    name="my_env",
    resources=Resources(cpu=1),
    reusable=flyte.ReusePolicy(replicas=2, idle_ttl=300)
)

@env.task
async def my_task(data: str) -> str:
    ...

@env.task
async def main_workflow() -> str:
    # `my_task.override(resources=Resources(cpu=4))` will fail. Instead use:
    result = await my_task.override(reusable="off", resources=Resources(cpu=4))
```

Additionally, `secrets` can only be overridden at the `@env.task` decorator level if the `TaskEnvironment` (`env`) does not have `reusable` set.

{{< /markdown >}}
{{< /variant >}}

### `depends_on`

* Type: `List[Environment]`

* A list of [`Environment`](../../api-reference/flyte-sdk/packages/flyte#flyteenvironment)
   objects that this `TaskEnvironment` depends on.
   When deploying this `TaskEnvironment`, the system will ensure that any dependencies
   of the listed `Environment`s are also available.
   This is useful when you have a set of environments that depend on each other.

<!-- TODO: Add when available
See [Environment dependencies](./environment-dependencies)
-->

* Can only be set at the `TaskEnvironment` level, not at the `@env.task` decorator level or the `task.override()` invocation level.

### `description`

* Type: `Optional[str]`

* A description of the task environment.
  This can be used to provide additional context about the task environment, such as its purpose or usage.

* Can only be set at the `TaskEnvironment` level, not at the `@env.task` decorator level
  or the `task.override()` invocation level.

### `plugin_config`

* Type: `Optional[Any]`

* Additional configuration for plugins that can be used with the task environment.
  This can include settings for specific plugins that are used in the task environment.

* Can only be set at the `TaskEnvironment` level, not at the `@env.task` decorator level
  or the `task.override()` invocation level.

### `report`

* Type: `bool`
* Whether to generate the HTML report for the task.
  If set to `True`, the task will generate an HTML report that can be viewed in the Flyte UI.
* Can only be set at the `@env.task` decorator level,
  not at the `TaskEnvironment` level or the `task.override()` invocation level.

### `max_inline_io_bytes`

* Type: `int`

* Maximum allowed size (in bytes) for all inputs and outputs passed directly to the task
  (e.g., primitives, strings, dicts).
  Does not apply to [`flyte.File`, `flyte.Dir`](../task-programming/files-and-directories), or [`flyte.DataFrame`](../task-programming/dataclasses-and-structures) (since these are passed by reference).

* Can be set at the `@env.task` decorator level and overridden at the `task.override()` invocation level.
  If not set, the default value is `MAX_INLINE_IO_BYTES` (which is 100 MiB).

### `retries`

* Type: `Union[int, RetryStrategy]`

* The number of retries for the task, or a `RetryStrategy` object that defines the retry behavior.
  If set to `0`, no retries will be attempted.

<!-- TODO: Add when available
See [Retries](./retries).
-->

* Can be set at the `@env.task` decorator level and overridden at the `task.override()` invocation level.

### `timeout`

* Type: `Union[timedelta, int]`

* The timeout for the task, either as a `timedelta` object or an integer representing seconds.
  If set to `0`, no timeout will be applied.

<!-- TODO: Add when available
See [Timeouts](./timeouts).
-->

* Can be set at the `@env.task` decorator level and overridden at the `task.override()` invocation level.

### `docs`

* Type: `Optional[Documentation]`

* Documentation for the task, including usage examples and explanations of the task's behavior.

* Can only be set at the `@env.task` decorator level. It cannot be overridden.
