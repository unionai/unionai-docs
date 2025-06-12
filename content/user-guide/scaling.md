---
title: Scaling
weight: 100
variants: +flyte +serverless +byoc +selfmanaged
---

# Scaling

Flyte is designed to scale effortlessly, allowing you to run workflows with large fan-outs.
To run many tasks concurrently, you simply use the `asyncio.gather()` function.
Here is an example:

```python
import asyncio

import flyte

env = flyte.TaskEnvironment("large_fanout")


@env.task
async def my_task(x: int) -> int:
    """
    A task that simply returns the input integer.
    """
    return x


@env.task
async def main(r: int):
    """
    A task that fans out to multiple instances of my_task.
    """
    results = []
    for i in range(r):
        results.append(my_task(x=i))
    return await asyncio.gather(*results)


if __name__ == "__main__":
    storage_cfg = flyte.S3.for_sandbox()
    flyte.init(
        endpoint="dns:///localhost:8090",
        insecure=True,
        org="testorg",
        project="testproject",
        domain="development",
        storage=storage_cfg,
    )
    r = flyte.run(main, r=1000)  # Adjust the number of fanouts as needed
    print(r.name)

```