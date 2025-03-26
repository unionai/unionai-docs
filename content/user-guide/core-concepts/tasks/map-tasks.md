---
title: Map tasks
weight: 1
variants: +flyte +serverless +byoc +byok
---

## Map tasks

A map task allows you to execute many instances of a task within a single workflow node.
This enables you to execute a task across a set of inputs without having to create a node for each input, resulting in significant performance improvements.

Map tasks find application in various scenarios, including:

* When multiple inputs require running through the same code logic.
* Processing multiple data batches concurrently.
* Conducting hyperparameter optimization.

Just like normal tasks, map tasks are automatically parallelized to the extent possible given resources available in the cluster.

```python
THRESHOLD = 11

@{{< key kit_as >}}.task
def detect_anomalies(data_point: int) -> bool:
    return data_point > THRESHOLD

@{{< key kit_as >}}.workflow
def map_workflow(data: list[int] = [10, 12, 11, 10, 13, 12, 100, 11, 12, 10]) -> list[bool]:
    # Use the map task to apply the anomaly detection function to each data point
    return map_task(detect_anomalies)(data_point=data)

```

> [!NOTE]
> Map tasks can also map over launch plans. For more information and example code, see [Mapping over launch plans](../launch-plans/mapping-over-launch-plans).

For more details see [Map Task example](https://github.com/unionai-oss/union-cloud-docs-examples/tree/main/map_task) in the `unionai-examples` repository and [Map Tasks]() section.
<!-- TODO: Add link to API -->
