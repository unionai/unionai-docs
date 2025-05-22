---
title: Subworkflows and sub-launch plans
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
---

# Subworkflows and sub-launch plans

In {{< key product_name >}} it is possible to invoke one workflow from within another.
A parent workflow can invoke a child workflow in two ways: as a **subworkflow** or via a [**sub-launch plan**](../launch-plans/running-launch-plans#sub-launch-plans).

In both cases the child workflow is defined and registered normally, exists in the system normally, and can be run independently.

But, if the child workflow is invoked from within the parent **by directly calling the child's function**, then it becomes a **subworkflow**.
The DAG of the subworkflow is embedded directly into the DAG of the parent and effectively become part of the parent workflow execution, sharing the same execution ID and execution context.

On the other hand, if the child workflow is invoked from within the parent [**by calling the child's launch plan**](../launch-plans), this is called a **sub-launch plan**. It results in a new top-level workflow execution being invoked with its own execution ID and execution context.
It also appears as a separate top-level entity in the system.
The only difference is that it happens to have been kicked off from within another workflow instead of from the command line or the UI.

Here is an example:

```python
import {{< key kit_import >}}

@{{< key kit_as >}}.workflow
def sub_wf(a: int, b: int) -> int:
    return t(a=a, b=b)

# Get the default launch plan of sub_wf, which we name sub_wf_lp
sub_wf_lp = {{< key kit_as >}}.LaunchPlan.get_or_create(sub_wf)

@{{< key kit_as >}}.workflow
def main_wf():
    # Invoke sub_wf directly.
    # An embedded subworkflow results.
    sub_wf(a=3, b=4)

    # Invoke sub_wf through its default launch plan, here called sub_wf_lp
    # An independent subworkflow results.
    sub_wf_lp(a=1, b=2)
```

## When to use subworkflows

Subworkflows allow you to manage parallelism between a workflow and its launched sub-flows, as they execute within the same context as the parent workflow.
Consequently, all nodes of a subworkflow adhere to the overall constraints imposed by the parent workflow.

<!-- TODO: a diagram of the above example. -->

Here's an example illustrating the calculation of slope, intercept and the corresponding y-value.

```python
import {{< key kit_import >}}


@{{< key kit_as >}}.task
def slope(x: list[int], y: list[int]) -> float:
    sum_xy = sum([x[i] * y[i] for i in range(len(x))])
    sum_x_squared = sum([x[i] ** 2 for i in range(len(x))])
    n = len(x)
    return (n * sum_xy - sum(x) * sum(y)) / (n * sum_x_squared - sum(x) ** 2)


@{{< key kit_as >}}.task
def intercept(x: list[int], y: list[int], slope: float) -> float:
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
    intercept = mean_y - slope * mean_x
    return intercept


@{{< key kit_as >}}.workflow
def slope_intercept_wf(x: list[int], y: list[int]) -> (float, float):
    slope_value = slope(x=x, y=y)
    intercept_value = intercept(x=x, y=y, slope=slope_value)
    return (slope_value, intercept_value)


@{{< key kit_as >}}.task
def regression_line(val: int, slope_value: float, intercept_value: float) -> float:
    return (slope_value * val) + intercept_value  # y = mx + c


@{{< key kit_as >}}.workflow
def regression_line_wf(val: int = 5, x: list[int] = [-3, 0, 3], y: list[int] = [7, 4, -2]) -> float:
    slope_value, intercept_value = slope_intercept_wf(x=x, y=y)
    return regression_line(val=val, slope_value=slope_value, intercept_value=intercept_value)
```

The `slope_intercept_wf` computes the slope and intercept of the regression line.
Subsequently, the `regression_line_wf` triggers `slope_intercept_wf` and then computes the y-value.

It is possible to nest a workflow that contains a subworkflow within yet another workflow.
Workflows can be easily constructed from other workflows, even if they also function as standalone entities.
For example, each workflow in the example below has the capability to exist and run independently:

```python
import {{< key kit_import >}}

@{{< key kit_as >}}.workflow
def nested_regression_line_wf() -> float:
    return regression_line_wf()
```

## When to use sub-launch plans

Sub-launch plans can be useful for implementing exceptionally large or complicated workflows that can’t be adequately implemented as [dynamic workflows](../workflows/dynamic-workflows) or [map tasks](../tasks/task-types#map-tasks).
Dynamic workflows and map tasks share the same context and single underlying Kubernetes resource definitions.
Sub-launch plan invoked workflows do not share the same context.
They are executed as separate top-level entities, allowing for better parallelism and scale.

Here is an example of invoking a workflow multiple times through its launch plan:

```python
import {{< key kit_import >}}


@{{< key kit_as >}}.task
def my_task(a: int, b: int, c: int) -> int:
    return a + b + c


@{{< key kit_as >}}.workflow
def my_workflow(a: int, b: int, c: int) -> int:
    return my_task(a=a, b=b, c=c)


my_workflow_lp = {{< key kit_as >}}.LaunchPlan.get_or_create(my_workflow)


@{{< key kit_as >}}.workflow
def wf() -> list[int]:
    return [my_workflow_lp(a=i, b=i, c=i) for i in [1, 2, 3]]
```
