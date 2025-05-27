---
title: Map tasks
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---

## Map tasks

A map task allows you to execute many instances of a task within a single workflow node.
This enables you to execute a task across a set of inputs without having to create a node for each input, resulting in significant performance improvements.

Map tasks find application in various scenarios, including:
* When multiple inputs require running through the same code logic.
* Processing multiple data batches concurrently.

Just like normal tasks, map tasks are automatically parallelized to the extent possible given resources available in the cluster.

```python
THRESHOLD = 11

@{{< key kit_as >}}.task
def detect_anomalies(data_point: int) -> bool:
    return data_point > THRESHOLD

@{{< key kit_as >}}.workflow
def map_workflow(data: list[int] = [10, 12, 11, 10, 13, 12, 100, 11, 12, 10]) -> list[bool]:
    # Use the map task to apply the anomaly detection function to each data point
    return {{< key kit_as >}}.{{<key map_func>}}(detect_anomalies)(data_point=data)

```

> [!NOTE]
> Map tasks can also map over launch plans. For more information and example code, see [Mapping over launch plans](../launch-plans/mapping-over-launch-plans).

To customize resource allocations, such as memory usage for individual map tasks, you can leverage `with_overrides`. Here’s an example using the `detect_anomalies` map task within a workflow:

```python
import union

@{{< key kit_as >}}.workflow
def map_workflow_with_resource_overrides(
    data: list[int] = [10, 12, 11, 10, 13, 12, 100, 11, 12, 10]
) -> list[bool]:

    return (
        {{< key kit_as >}}.{{<key map_func>}}(detect_anomalies)(data_point=data)
        .with_overrides(requests={{< key kit_as >}}.Resources(mem="2Gi"))
    )
```

You can also configure `concurrency` and `min_success_ratio` for a map task:

- `concurrency` limits the number of mapped tasks that can run in parallel to the specified batch size. If the input size exceeds the concurrency value, multiple batches will run serially until all inputs are processed. If left unspecified, it implies unbounded concurrency.
- `min_success_ratio` determines the minimum fraction of total jobs that must complete successfully before terminating the map task and marking it as successful.

```python
@{{< key kit_as >}}.workflow
def map_workflow_with_additional_params(
    data: list[int] = [10, 12, 11, 10, 13, 12, 100, 11, 12, 10]
) -> list[typing.Optional[bool]]:

    return {{< key kit_as >}}.{{<key map_func>}}(
        detect_anomalies,
        concurrency=1,
        min_success_ratio=0.75
    )(data_point=data)
```

For more details see [Map Task example](https://github.com/unionai-oss/union-cloud-docs-examples/tree/main/map_task) in the `unionai-examples` repository and [Map Tasks]() section.
<!-- TODO: Add link to API -->
