---
title: Task configuration
weight: 60
variants: +flyte +serverless +byoc +selfmanaged
---

# Task configuration

<!-- TODO:
link from here to various environment strategies, when available
- Single environment app (workflow)
- Multi-env workflow, deployed together
- Deploying all environments recursively (coming soon)
- Managing environments with different dependencies.
-->

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

Here is an example of how these levels work together:

```python
import flyte

# Level 1: TaskEnvironment - Base configuration
env = flyte.TaskEnvironment(
    name="data_processing",
    resources=flyte.Resources(cpu=1, memory="512Mi"),
    cache="disable",
    secrets=flyte.Secret("db-credentials")
)

# Level 2: Decorator - Override some environment settings
@env.task(
    cache="auto",           # Overrides environment cache policy
    retries=3,              # Decorator-only parameter
    timeout=300,            # Decorator-only parameter
)
async def process_data(data_path: str) -> str:
    """Process data with custom cache and retry settings."""
    return f"Processed {data_path}"

@env.task
async def main_workflow() -> str:
    # Level 3: Invocation - Runtime overrides
    result = await process_data.override(
        resources=flyte.Resources(cpu=4, memory="2Gi"),  # Override environment resources
    )("input.csv")

    return result
```

## Task configuration parameters

Here is a comprehensive overview of the task configuration parameters available at each level and how they interact:

| Parameter | `TaskEnvironment` | `@env.task` decorator | `task.override()` invocation |
|-----------|-------------|-----------|------------|
| **name** | ✅ Yes (required) | ✅ Yes (sets friendly name, does not override. See below)| ❌ No |
| **image** | ✅ Yes | ❌ No | ❌ No |
| **resources** | ✅ Yes | ❌ No | ✅ Yes (if not `reusable`)|
| **env** | ✅ Yes | ❌ No | ✅ Yes (if not `reusable`) |
| **secrets** | ✅ Yes | ✅ Yes (if not `reusable`) | ✅ Yes (if not `reusable`) |
| **cache** | ✅ Yes | ✅ Yes | ✅ Yes |
| **pod_template** | ✅ Yes | ✅ Yes | ❌ No |
| **reusable** | ✅ Yes (see below)| ❌ No | ✅ Yes (can be disabled with `off`) |
| **depends_on** | ✅ Yes | ❌ No | ❌ No |
| **description** | ✅ Yes | ❌ No | ❌ No |
| **plugin_config** | ✅ Yes | ❌ No | ❌ No |
| **report** | ❌ No | ✅ Yes | ❌ No |
| **max_inline_io_bytes** | ❌ No | ✅ Yes | ✅ Yes |
| **retries** | ❌ No | ✅ Yes | ✅ Yes |
| **timeout** | ❌ No | ✅ Yes | ✅ Yes |
| **docs** | ❌ No | ✅ Yes | ❌ No |

### Reusable container constraints


### Key patterns

1. **Environment-only**: Infrastructure settings (`image`, `depends_on`, `plugin_config`)
2. **Runtime-only**: Execution behavior (`retries`, `timeout`, `report`)
3. **Full chain**: Core execution settings (`cache`, `secrets`)
4. **Reusable-constrained**: Resource-related settings (`resources`, `env`, `secrets`)

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

* Type: `ReusePolicy | None`

* A `ReusePolicy` that defines whether the task environment can be reused.
  If set, the task environment will be reused across multiple task invocations.
  See [Reusable containers](./reusable-containers) and the API docs for the [`ReusePolicy` object](../../api-reference/flyte-sdk/packages/flyte#flytereusepolicy).

> [!NOTE]
> The `reusable` setting controls the [**reusable containers** feature](./reusable-containers).
> This feature is currently not implemented in the Flyte OSS backend.
> It is only available when running on a Union.ai backend.

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

### `depends_on`

* Type: `List[Environment]`)

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
  ==>

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





## Configuration at the `TaskEnvironment` level

A `TaskEnvironment` object represents a collection of settings.
You can apply this collection to multiple different individual task definitions using the `@env.task` decorator,
where `env` is the variable to which you assigned the `TaskEnvironment` object.
For example:

```python
env = flyte.TaskEnvironment(name="my_env", resources=flyte.Resources(cpu=1, memory="250Mi"))

@env.task
async def my_task(data: str) -> str:
    ...
```

Here we define a task environment with resource requirements (1 CPU and 250 MiB of memory).
Every time a task decorated with `@env.task` (like `my_task`) is invoked, that execution will run in its own container with these resource settings.
Note that *each invocation* of *each `@env.task` function* will have its own container (unless you are employing [reusable containers](./reusable-containers)),
but because they share the same `env`, all of these containers will have the same resource configuration.

## Configuration at the `@env.task` level

Each task decorated with `@env.task` will inherit the settings from its `TaskEnvironment` object.
Then, within the decorator you can set additional paremeters.
Some of these are settable only at the `@env.task` level while other are shared with `TaskEnvironment`.
When one of these shared parameters is set in the decorator it will override any setting from the `TaskEnvironment` for that specific task function only.

For example:

```python
@env.task()
async def my_task(data: str) -> str:
    ...

@env.task(resources=flyte.Resources(cpu=2, memory="500Mi"))
async def my_big_task(data: str) -> str:
    ...

```
Here we have the original definition of `my_task` above, unchanged, but we add another task, `my_big_task`.
The `my_big_task` function is decorated with `@env.task` but with an additional `resources` parameter.
This will override the `resources` parameter defined in `env`, specifying that `my_big_task` requires 2 CPUs and 500 MiB of memory.

The full set of parameters for the `@env.task` decorator are:

```python
def task(
        self,
        _func=None,
        *,
        name: Optional[str] = None,
        cache: Union[CacheRequest] | None = None,
        retries: Union[int, RetryStrategy] = 0,
        timeout: Union[timedelta, int] = 0,
        docs: Optional[Documentation] = None,
        secrets: Optional[SecretRequest] = None,
        pod_template: Optional[Union[str, "V1PodTemplate"]] = None,
        report: bool = False,
        max_inline_io_bytes: int = MAX_INLINE_IO_BYTES,
    ) -> Union[AsyncFunctionTaskTemplate, Callable[P, R]]
```
        """
        Decorate a function to be a task.

        :param _func: Optional The function to decorate. If not provided, the decorator will return a callable that
        accepts a function to be decorated.
        :param name: Optional A friendly name for the task (defaults to the function name)
        :param cache: Optional The cache policy for the task, defaults to auto, which will cache the results of the
        task.
        :param retries: Optional The number of retries for the task, defaults to 0, which means no retries.
        :param docs: Optional The documentation for the task, if not provided the function docstring will be used.
        :param secrets: Optional The secrets that will be injected into the task at runtime.
        :param timeout: Optional The timeout for the task.
        :param pod_template: Optional The pod template for the task, if not provided the default pod template will be
        used.
        :param report: Optional Whether to generate the html report for the task, defaults to False.
        :param max_inline_io_bytes: Maximum allowed size (in bytes) for all inputs and outputs passed directly to the
         task (e.g., primitives, strings, dicts). Does not apply to files, directories, or dataframes.
        """

## Configuration at the task invocation level

When invoking a task you can use override the task environment and resource requirements for a specific task when












## Single task environment

In that example the tasks did run in separate containers but the containers themselves were identical.
This is because we defined a single task environment and used it for all the tasks.

We defined the task environment using [`flyte.TaskEnvironment`](../api-reference/flyte-sdk/packages/flyte#flytetaskenvironment), like this:

```python
env = flyte.TaskEnvironment(name="hello_world")
```

And then decorated each of the functions with `@env.task`, like this:

```python
@env.task
async def say_hello(data: str, lt: List[int]) -> str:
    ...


@env.task
async def square(i: int = 3) -> int:
    ...


@env.task
async def hello_wf(data: str = "default string") -> str:
    ...
```

## Multiple task environments

Because we used the same `env` for all the tasks, they all ran in the same environment, which means they all had the same configuration and dependencies.

To truly take advantage of distributed and heterogeneous compute environments offered by Union/Flyte, you have to define multiple task environments that differ.

Change the code in your `hello.py` file to define two different task environments:

```python
env1 = flyte.TaskEnvironment(name="env1")
env2 = flyte.TaskEnvironment(name="env2", resources=flyte.Resources(cpu=1, memory="250Mi"))
```

In this case we have defined two task environments: `env1` and `env2`.
The first one is the default environment, while the second one has specific resource requirements (1 CPU and 250 MiB of memory).
Now you can decorate your tasks with different environments:

```python
@env1.task
async def say_hello(data: str, lt: List[int]) -> str:
    ...


@env2.task
async def square(i: int = 3) -> int:
    ...


@env1.task
async def hello_wf(data: str = "default string") -> str:
    ...
```

When you run this on Union/Flyte, each task will run in its own container,
but now the containers will have different configurations based on the task environment they are associated with:

<!-- TODO:
We need to talk about depends_on attribute, otherwise downstream environments will not be built
-->

* The `hello_wf` and `say_hello` tasks will run in containers with the default configuration (defined by `env1`)
* The `square` task will run in a container with the specified CPU and memory (defined by the `env2`).

Here we used the `resources` parameter to specify hardware requirements for the task.

- Via the SDK when triggering a run: `flyte.run(task_queue="gcp-useast1-1", ...)`
- Via the CLI when triggering a run: `flyte run --task_queue "gcp-useast-1" ...`
- Via the launch form when running, rerunning, or recovering a run
- Via Environments: `env=flyte.TaskEnvironment(task_queue="gcp-useast-1", ...`
- Via overrides: `await my_task.override(task_queue="gcp-useast-1", ...)`

import flyte

env = flyte.TaskEnvironment("x")

@env.task(max_inline_io_bytes=100*1024*1024)
async def foo():
   ...

@env.task
async def main():
   await foo.with_overrides(max_inline_io_bytes=1)()