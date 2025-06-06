---
title: Task environments
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
---

# Task environments

In the previous section we saw how you can instrument your pure Python functions to run them on Union.ai.
By decorating your functions with `@env.task` you can run them in a distributed manner, with each function running in its own container.

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

Because we used the same `env` for all the tasks, they all ran in the same environment, which means they all had the same configuration and dependencies.

To truly take advantage of distributed and heterogeneous compute environments offered by Flyte/Union, you have to define multiple task environments that differ.

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

When you run this on Flyte/Union each task will run in its own container,
but now the containers will have different configurations based on the task environment they are associated with:

* The `hello_wf` and `say_hello` tasks will run in containers with the default configuration (defined by `env1`)
* The `square` task will run in a container with the specified CPU and memory (defined by the `env2`).

Here we used the `resources` parameter to specify hardware requirements for the task.

Another important parameter is `image`, which allows you to specify a Docker image for the task container.
You can set this parameter to use a specific Docker image that contains the dependencies required by your task.
Just as the `resources` parameter let you define hardware requirements, the `image` parameter lets you define the software environment in which your task will run.

In the next section we will show how to do this.