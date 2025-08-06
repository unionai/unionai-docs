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
To do this you have to configure your tasks.
We will explore how to do this in the following sections.

Task configuration is done at three levels. From most general to most specific, they are: The `TaskEnvironment` level, the `@env.task` decorator level, and the task invocation level.

Each level has some settings specific to it (because they only make sense at that level) and some settings in common with the other levels.
In the case of common settings, the more setting at the more specific level will override the one at the more general level

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

### Task environment parameters

The full set of parameters for the [`TaskEnvironment`](../../api-reference/flyte-sdk/packages/flyte#flytetaskenvironment) are:

* `name` (`str`, required):
   The name for the task environment. A string.

* `depends_on` (`List[Environment]`):
   A list of [`Environment`](../../api-reference/flyte-sdk/packages/flyte#flyteenvironment)
   objects that this [`TaskEnvironment`](../../api-reference/flyte-sdk/packages/flyte#flytetaskenvironment) depends on.
   When deploying this `TaskEnvironment`, the system will ensure that any dependencies
   of the listed `Environment`s are also available.
   This is useful when you have a set of environments that depend on each other.
   <!-- See environment dependencies -->

* `pod_template` (`Optional[Union[str, kubernetes.client.V1PodTemplate]]`):
   A pod template that defines the Kubernetes pod configuration for the task.
   A string reference to a named template or a `kubernetes.client.V1PodTemplate` object.
   <!-- see Using podtemplates -->

* `description` (`Optional[str]`):
   A description of the task environment.

* `secrets` (`Optional[SecretRequest]`):
   The secrets to be made available in the environment.
   A [`Secret`](../../api-reference/flyte-sdk/packages/flyte#flytesecret) object.
   See [Secrets](./secrets).

* `env` (`Optional[Dict[str, str]]`):
   A dictionary of environment variables that will be made available in the task container.

* `resources` (`Optional[Resources]`):
   The compute resources, such as CPU and Memory, required by the task environment.
   A [`Resources`](../../api-reference/flyte-sdk/packages/flyte#flyteresources) object.
   <!-- See resource specification -->

* `image` (`Union[str, Image, Literal['auto']]`):
   The Docker image to use for the task container.
   Can be a URL reference to a Docker image, an [`Image` object](../../api-reference/flyte-sdk/packages/flyte#flyteimage), or the string `auto`.
   If set to `auto`, or if this parameter is not set, the [default image]() will be used.
   See [Container images](./container-images).

* `cache` (`Union[CacheRequest]`):
   A `CacheRequest` object that defines how the task results should be cached.
   See [Caching](./caching).

* `reusable` (`ReusePolicy | None`):
   A `ReusePolicy` that defines whether the task environment can be reused.

   > [!NOTE]
   > [Reusable containers]({{< docs-home byoc v2 >}}/user-guide/reusable-containers)
   > are only available when running on Union.ai backend.

* `plugin_config` (`Optional[Any]`):
   Additional configuration for plugins that can be used with the task environment.
   <!-- see plugins -->

All parameters are optional except `name`.

<!-- TODO: Reference advance task environment mgmt/config including clone_with and depends_on -->

## Configuration at the `@env.task` level

Each task decorated with `@env.task` will inherit the settings from its `TaskEnvironment` object.
But there are addional settings settable only at the `@env.task` level and others in common with `TAskEnvironment`, which, when set, will override the setting from the `TaskEnvironment` for that specific task function definition only.

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

The full signature of the `@env.task` decorator is (defined in ):

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


 that can be used when


, Task
1. **`TaskEnvironment`: The `TaskEnvironment` object defines a collection of settings that define the container environment in a task will run.
   When you declare a TaskEnvironment you assign it to a variable. You then use that variable name  which all tasks decorated with `env.task` will run. This includes dependencies, resource requirements, and other settings.
   You can think of it as a blueprint for how the tasks in your workflow will run.
   The `TaskEnvironment` is used to define the environment in which the


 task will run, including dependencies,
   resource requirements, and other settings.


   You can define multiple `TaskEnvironment`s, each with its own configuration,
   and then use them to decorate your tasks.

which will be used for all

in which one or morethe task will run, including dependencies
   and resource requirements.
2. **Task resources**: Specify the hardware resources required by the task, such as CPU and memory.
3. **Task overrides**: Allow you to override the task environment and resource requirements


 your tasktask configuration works task environments in Flyte.


Previously we deomonstrated the simplets possible configuraiton of
When setting up your functions to run as Flyte tasks, there is some conifguration


 this section, we will explore how to configure tasks in Flyte/Union, including:

- Defining task environments
-
- Specifying resource requirements

Previously we saw how you can decorate your pure Python functions to run them on Union/Flyte.
By decorating your functions with `@env.task` you can run them in a distributed manner, with each function running in its own container.

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