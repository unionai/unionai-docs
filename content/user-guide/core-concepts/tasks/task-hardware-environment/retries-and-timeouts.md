---
title: Retries and timeouts
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
---

# Retries and timeouts

## Retry types

{{< key product_name>}} allows you to automatically retry failing tasks. This section explains the configuration and application of retries.

Errors causing task failure are categorized into two main types, influencing the retry logic differently:

* `SYSTEM`: These errors arise from infrastructure-related failures, such as hardware malfunctions or network issues.
  They are typically transient and can often be resolved with a retry.

* `USER`: These errors are due to issues in the user-defined code, like a value error or a logic mistake, which usually require code modifications to resolve.

## Configuring retries

Retries in {{< key product_name>}} are configurable to address both `USER` and `SYSTEM` errors, allowing for tailored fault tolerance strategies:

`USER` error can be handled by setting the `retries` attribute in the task decorator to define how many times a task should retry.
This is straightforward and directly controlled in the task definition:

```python
import random
from flytekit import task

@task(retries=3)
def compute_mean(data: List[float]) -> float:
    if random() < 0.05:
        raise FlyteRecoverableException("Something bad happened 🔥")
    return sum(data) / len(data)
```

{{< variant flyte >}}
{{< markdown >}}

`SYSTEM` errors are managed at the platform level through settings like `max-node-retries-system-failures` in the FlytePropeller configuration.
This setting helps manage retries without requiring changes to the task code.

Additionally, the `interruptible-failure-threshold` option in the `node-config` key defines how many system-level retries are considered interruptible.
This is particularly useful for tasks running on preemptible instances.

For more details, refer to the Flyte Propeller Configuration.

{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}

`SYSTEM` errors are managed at the platform level through settings internal tothe {{< key product_name >}} implementation.

{{< /markdown >}}
{{< /variant >}}

## Retrying interruptible tasks

Tasks marked as interruptible can be preempted and retried without counting against the USER error budget.
This is useful for tasks running on preemptible compute resources like spot instances.

See [Interruptible instances](./interruptible-instances)

## Retrying map tasks

For map tasks, the interruptible behavior aligns with that of regular tasks. The retries field in the task annotation is not necessary for handling SYSTEM errors, as these are managed by the platform’s configuration. Alternatively, the USER budget is set by defining retries in the task decorator.

See [Map tasks](../map-tasks).

## Timeouts

To protect against zombie tasks that hang due to system-level issues, you can supply the timeout argument to the task decorator to make sure that problematic tasks adhere to a maximum runtime.

In this example, we make sure that the task is terminated after it’s been running for more that one hour.

```python
from datetime import timedelta

@task(timeout=timedelta(hours=1))
def compute_mean(data: List[float]) -> float:
    return sum(data) / len(data)
```

Notice that the timeout argument takes a built-in Python `timedelta` object.
