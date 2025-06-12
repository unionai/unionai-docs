---
title: Scaling
weight: 100
variants: +flyte +serverless +byoc +selfmanaged
---

# Scaling

Flyte is designed to scale effortlessly, allowing you to run workflows with large fan-outs.
To run many tasks concurrently, you simply use the `asyncio.gather()` function.
Here is an example:

{{< code file="/external/migrate-to-unionai-examples-flyte2/scaling.py" lang="python" >}}
