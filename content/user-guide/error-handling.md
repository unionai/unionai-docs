---
title: Error handling
weight: 4
variants: +flyte +serverless +byoc +selfmanaged
---

# Error handling

One of the key features of Flyte 2 is the ability to recover from user-level errors in a workflow execution.
This includes out-of-memory errors and other exceptions.

This is a direct result of the fact that workflows are now written in regular Python, and provide you with all the power and flexibility of Python error handling.
Let's look at an example:

First, we import the necessary modules and set up the task environment:

```python
import asyncio

import flyte
import flyte.errors

env = flyte.TaskEnvironment(name="failure_handling", resources=flyte.Resources(cpu=1, memory="250Mi"))
```

Note that we define our task environment with a resource allocation of 1 CPU and 250 MiB of memory.

Next, we define two tasks: one that will intentionally cause an out-of-memory (OOM) error, and another that will always succeed:

```python
@env.task
async def oomer(x: int):
    large_list = [0] * 100000000 * x  # This will cause an OOM error if x is too large
    print(len(large_list))


@env.task
async def always_succeeds() -> int:
    await asyncio.sleep(1)
    return 42
```

Finally, we define the main task (the top level workflow task) that will handle the failure recovery logic:

```python
@env.task
async def error_handling() -> int:
    try:
        await oomer(1000)  # This is likely to cause an OOM error
    except flyte.errors.OOMError as e:
        print(f"Failed with oom trying with more resources: {e}, of type {type(e)}, {e.code}")
        try:
            await oomer.override(resources=flyte.Resources(cpu=1, memory="1Gi"))(5)
        except flyte.errors.OOMError as e:
            print(f"Failed with OOM Again giving up: {e}, of type {type(e)}, {e.code}")
            raise e
    finally:
        await always_succeeds()
    return await always_succeeds()


if __name__ == "__main__":
    flyte.init_auto_from_config("./config.yaml")
    run = flyte.run(error_handling)
    print(run.name)
    print(run.url)
    run.wait(run)

```

The top `try...catch` block attempts to run the `oomer` task with a parameter that is likely to cause an OOM error.
If the error occurs, it catches the `flyte.errors.OOMError` and attempts to run the `oomer` task again with increased resources.

This type of dynamic error handling allows you to gracefully recover from user-level errors in your workflows.
