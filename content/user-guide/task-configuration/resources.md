---
title: Resources
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
---

# Resources

Flyte allows you to specify resource requirements for your tasks, ensuring they have the necessary CPU, memory, and other resources to execute successfully.

## Overview

By default, tasks run with a standard set of resources. However, you can customize the resource allocation for each task using the `Resources` class.

## Basic Usage

To specify resource requirements for a task, you can set the `resources` parameter in the `TaskEnvironment` or directly in the task decorator.

```python
import flyte

env = flyte.TaskEnvironment(
    name="my-env",
    resources=flyte.Resources(memory="1Gi", cpu="500m")
)

@env.task
def my_task(x: int) -> int:
    return x * x
```

## Resource Types

Flyte supports the following resource types:

- **CPU**: The amount of CPU to allocate (e.g., `500m` for 500 milliCPU).
- **Memory**: The amount of memory to allocate (e.g., `1Gi` for 1 GiB).
- **GPU**: The number of GPUs to allocate (e.g., `1` for 1 GPU).

## Advanced Usage

You can also specify resource requirements at the task level, allowing for more granular control.

```python
@env.task
def my_task(x: int) -> int:
    return x * x

@env.task
def my_other_task(y: int) -> int:
    return y + y
```

In this example, `my_task` will use the resources defined in the `TaskEnvironment`, while `my_other_task` will use the default resources.

## Best Practices

- **Right-size resources**: Allocate only the resources your tasks need to avoid wasting resources.
- **Monitor resource usage**: Keep an eye on resource usage to identify potential bottlenecks or inefficiencies.
- **Use resource limits**: Set resource limits to prevent tasks from consuming excessive resources and impacting other tasks.

## Conclusion

By specifying resource requirements for your tasks, you can ensure they have the necessary resources to execute successfully while optimizing resource usage across your Flyte workflows.
