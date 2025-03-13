---
title: Task parameters
weight: 3
variants: +flyte +serverless +byoc +byok
---

# Task parameters

You pass the following parameters to the `@union.task` decorator:

{{/* TODO: consider organizing by category rather than alphabetically. */}}

* `accelerator`: The accelerator to use for this task.
  For more information, see [Specifying accelerators](https://docs.flyte.org/en/latest/api/flytekit/extras.accelerators.html#specifying-accelerators).

* `cache`: See [Caching](../caching.md).

* `cache_serialize`: See [Caching](../caching.md).

* `cache_version`: See [Caching](../caching.md).

* `cache_ignore_input_vars`: Input variables that should not be included when calculating the hash for the cache.

* `container_image`: See [`ImageSpec`](./task-software-environment/imagespec.md).

* `deprecated`: A string that can be used to provide a warning message for deprecated task.
  The absence of a string, or an empty string, indicates that the task is active and not deprecated.

* `docs`: Documentation about this task.

* `enable_deck`: If true, this task will output a Flyte Deck which can be used to visualize the task execution
  (see [Decks&#x2B00;](https://docs.flyte.org/en/latest/user_guide/development_lifecycle/decks.html#id1)).

```python
@union.task(enable_deck=True)
def my_task(my_str: str):
    print("hello {my_str}")
```

* `environment`: See [Environment variables](./task-software-environment/environment-variables.md).

* `interruptible`: See [Interruptible instances](./task-hardware-environment/interruptible-instances.md).

* `limits`: See [Customizing task resources](./task-hardware-environment/customizing-task-resources.md).

* `node_dependency_hints`: A list of tasks, launch plans, or workflows that this task depends on.
  This is only for dynamic tasks/workflows, where Union cannot automatically determine the dependencies prior to runtime.
  Even on dynamic tasks this is optional, but in some scenarios it will make registering the workflow easier,
  because it allows registration to be done the same as for static tasks/workflows.
  For example this is useful to run launch plans dynamically, because launch plans must be registered on Flyteadmin before they can be run.
  Tasks and workflows do not have this requirement.

```python
@union.workflow
def workflow0():
  launchplan0 = LaunchPlan.get_or_create(workflow0)
    # Specify node_dependency_hints so that launchplan0
    # will be registered on flyteadmin, despite this being a dynamic task.
@union.dynamic(node_dependency_hints=[launchplan0])
def launch_dynamically():
    # To run a sub-launchplan it must have previously been registered on flyteadmin.
    return [launchplan0]*10
```

* `pod_template`: See [Task hardware environment](./task-hardware-environment/index.md#pod_template-and-pod_template_name-task-parameters).

* `pod_template_name`: See [Task hardware environment](./task-hardware-environment/index.md#pod_template-and-pod_template_name-task-parameters).

* `requests`: See [Customizing task resources](./task-hardware-environment/customizing-task-resources.md)

* `retries`: Number of times to retry this task during a workflow execution.
  Tasks can define a retry strategy to let the system know how to handle failures (For example: retry 3 times on any kind of error).
  For more information, see [Interruptible instances](./task-hardware-environment/interruptible-instances.md)
  There are two kinds of retries *system retries* and *user retries*.

* `secret_requests`: See [Managing secrets](../../development-cycle/managing-secrets.md)

* `task_config`: Configuration for a specific task type.
  See the [Union Agents documentation](../../integrations/agents/index.md) and
  [Flyte plugins documentation](https://docs.flyte.org/en/latest/flytesnacks/integrations.html) for the right object to use.

* `task_resolver`: Provide a custom task resolver.

* `timeout`: The max amount of time for which one execution of this task should be executed for.
  The execution will be terminated if the runtime exceeds the given timeout (approximately).
  To ensure that the system is always making progress, tasks must be guaranteed to end gracefully/successfully.
  The system defines a default timeout period for the tasks.
  It is possible for task authors to define a timeout period, after which the task is marked as `failure`.
  Note that a timed-out task will be retried if it has a retry strategy defined.
  The timeout can be handled in the
  [TaskMetadata](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.TaskMetadata.html?highlight=retries.md#flytekit.TaskMetadata).

## Use `partial` to provide default arguments to tasks

You can use the `functools.partial` function to assign default or constant values to the parameters of your tasks:
```python
import functools
import union

@union.task
def slope(x: list[int], y: list[int]) -> float:
    sum_xy = sum([x[i] * y[i] for i in range(len(x))])
    sum_x_squared = sum([x[i] ** 2 for i in range(len(x))])
    n = len(x)
    return (n * sum_xy - sum(x) * sum(y)) / (n * sum_x_squared - sum(x) ** 2)

@union.workflow
def simple_wf_with_partial(x: list[int], y: list[int]) -> float:
    partial_task = functools.partial(slope, x=x)
    return partial_task(y=y)
```

## Named outputs

By default, {@= Product =@} employs a standardized convention to assign names to the outputs of tasks or workflows.
Each output is sequentially labeled as `o1`, `o2`, `o3`, ... `on`, where `o` serves as the standard prefix,
and `1`, `2`, ... `n` indicates the positional index within the returned values.

However, {@= Product =@} allows the customization of output names for tasks or workflows.
This customization becomes beneficial when you're returning multiple outputs
and you wish to assign a distinct name to each of them.

The following example illustrates the process of assigning names to outputs for both a task and a workflow.


Define a `NamedTuple` and assign it as an output to a task:

```python
import union
from typing import NamedTuple

slope_value = NamedTuple("slope_value", [("slope", float)])

@union.task
def slope(x: list[int], y: list[int]) -> slope_value:
    sum_xy = sum([x[i] * y[i] for i in range(len(x))])
    sum_x_squared = sum([x[i] ** 2 for i in range(len(x))])
    n = len(x)
    return (n * sum_xy - sum(x) * sum(y)) / (n * sum_x_squared - sum(x) ** 2)
```

Likewise, assign a `NamedTuple` to the output of `intercept` task:

```python
intercept_value = NamedTuple("intercept_value", [("intercept", float)])

@union.task
def intercept(x: list[int], y: list[int], slope: float) -> intercept_value:
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
    intercept = mean_y - slope * mean_x
    return intercept
```

{{< note >}}
While it's possible to create `NamedTuple`s directly within the code,
it's often better to declare them explicitly. This helps prevent potential linting errors in tools like mypy.

```python
def slope() -> NamedTuple("slope_value", slope=float):
    pass
```
{{< /note >}}

You can easily unpack the `NamedTuple` outputs directly within a workflow.
Additionally, you can also have the workflow return a `NamedTuple` as an output.

{{< note >}}
Remember that we are extracting individual task execution outputs by dereferencing them.
This is necessary because `NamedTuple`s function as tuples and require this dereferencing:
{{< /note >}}

```python
slope_and_intercept_values = NamedTuple("slope_and_intercept_values", [("slope", float), ("intercept", float)])


@union.workflow
def simple_wf_with_named_outputs(x: list[int] = [-3, 0, 3], y: list[int] = [7, 4, -2]) -> slope_and_intercept_values:
    slope_value = slope(x=x, y=y)
    intercept_value = intercept(x=x, y=y, slope=slope_value.slope)
    return slope_and_intercept_values(slope=slope_value.slope, intercept=intercept_value.intercept)

```

You can run the workflow locally as follows:

```python
if __name__ == "__main__":
    print(f"Running simple_wf_with_named_outputs() {simple_wf_with_named_outputs()}")
```
