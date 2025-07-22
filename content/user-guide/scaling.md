---
title: Scaling
weight: 14
variants: +flyte +serverless +byoc +selfmanaged
---

# Scaling

Flyte is designed to scale effortlessly, allowing you to run workflows with large fan-outs.
To run many tasks concurrently, you simply use the [`asyncio.gather`](https://docs.python.org/3/library/asyncio-task.html#asyncio.gather) function.
Here is an example:

{{< code file="/external/migrate-to-unionai-examples-flyte2/scaling.py" lang="python" >}}

Note that we are using the [`flyte.group`](../api-reference/flyte-sdk/packages/flyte#group) context manager which allows you to group actions together in the UI.
