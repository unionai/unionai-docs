---
title: Tasks and environment
weight: 60
variants: +flyte +serverless +byoc +selfmanaged
---

# Tasks and environments

<!-- TODO:
link from here to various environment strategies, when available
- Single environment app (workflow)
- Multi-env workflow, deployed together
- Deploying all environments recursively (coming soon)
- Managing environments with different dependencies.
-->

Previously we saw how you can instrument your pure Python functions to run them on Union/Flyte.
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

## Task environment parameters

The full signature of the `flyte.TaskEnvironment` constructor is:

```python
class TaskEnvironment(
    name: str,
    depends_on: List[Environment],
    pod_template: Optional[Union[str, 'V1PodTemplate']],
    description: Optional[str],
    secrets: Optional[SecretRequest],
    env: Optional[Dict[str, str]],
    resources: Optional[Resources],
    image: Union[str, Image, Literal['auto']],
    cache: Union[CacheRequest],
    reusable: ReusePolicy | None,
    plugin_config: Optional[Any],
)
```

(See also: [Task Environment API reference](../../api-reference/flyte-sdk/packages/flyte#flytetaskenvironment))

The parameters of `TaskEnvironment` are:

* `name` (required):
   The name for the task environment. A string.

* `depends_on`:
   A list of [`Environment`](../../api-reference/flyte-sdk/packages/flyte#flyteenvironment)
   objects that this [`TaskEnvironment`](../../api-reference/flyte-sdk/packages/flyte#flytetaskenvironment) depends on.
   When deploying this `TaskEnvironment`, the system will ensure that any dependencies
   of the listed `Environment`s are also available.
   This is useful when you have a set of environments that depend on each other.
   <!-- See environment dependencies -->

* `pod_template`:
   A pod template that defines the Kubernetes pod configuration for the task.
   A string reference to a named template or a `kubernetes.client.V1PodTemplate` object.
   <!-- see container tasks and podtemplates -->

* `description`:
   A description of the task environment.
   A string.

* `secrets`:
   The secrets to be made available into the environment.
   A [`Secret`](../../api-reference/flyte-sdk/packages/flyte#flytesecret) object.
   See [Secrets](./secrets).

* `env`:
   A dictionary of environment variables that will be made available in the task container.

* `resources`:
   The compute resources, such as CPU and Memory, required by the task environment.
   A [`Resources`](../../api-reference/flyte-sdk/packages/flyte#flyteresources) object.
   <!-- See resource specification -->

* `image`:
   The Docker image to use for the task container.
   Can be a URL reference to a Docker image, an [`Image` object](../../api-reference/flyte-sdk/packages/flyte#flyteimage), or the string "auto".
   If set to "auto", or if this parameter is not set, the [default image]() will be used.
   See [Container images](./container-images).

* `cache`:
   A `CacheRequest` object that defines how the task results should be cached.
   See [Caching](./caching).

* `reusable`: A `ReusePolicy` that defines whether the task environment can be reused.
   > [!NOTE]
   > [Reusable containers]({{< docs-home byoc v2 >}}/user-guide/reusable-containers)
   > are only available when running on Union.ai backend.)

* `plugin_config`: Additional configuration for plugins that can be used with the task environment.
<!-- see plugins -->

All parameters are optional except `name`.
