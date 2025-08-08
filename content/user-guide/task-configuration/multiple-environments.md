---
title: Multiple environments
weight: 200
variants: +flyte +serverless +byoc +selfmanaged
---

# Multiple environments

<!-- TODO:
link from here to various environment strategies, when available
- Single environment app (workflow)
- Multi-env workflow, deployed together
- Deploying all environments recursively (coming soon)
- Managing environments with different dependencies.
-->

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