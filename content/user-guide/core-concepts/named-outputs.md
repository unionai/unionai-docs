---
title: Named outputs
weight: 9
variants: +flyte +serverless +byoc +selfmanaged
---

# Named outputs

By default, {{< key product_name >}} employs a standardized convention to assign names to the outputs of tasks or workflows. Each output is sequentially labeled as `o1`, `o2`, `o3`, and so on.

You can, however, customize these output names by using a `NamedTuple`.

To begin, import the required dependencies:

```python
# basics/named_outputs.py

from typing import NamedTuple

import {{< key kit_import>}}
```

Here we define a `NamedTuple` and assign it as an output to a task called `slope`:

```python
slope_value = NamedTuple("slope_value", [("slope", float)])

@{{<key kit_as>}}.task
def slope(x: list[int], y: list[int]) -> slope_value:
    sum_xy = sum([x[i] * y[i] for i in range(len(x))])
    sum_x_squared = sum([x[i] ** 2 for i in range(len(x))])
    n = len(x)
    return (n * sum_xy - sum(x) * sum(y)) / (n * sum_x_squared - sum(x) ** 2)
```

Similarly, we define another `NamedTuple` and assign it to the output of another task, `intercept`:

```python
intercept_value = NamedTuple("intercept_value", [("intercept", float)])

@{{<key kit_as>}}.task
def intercept(x: list[int], y: list[int], slope: float) -> intercept_value:
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
    intercept = mean_y - slope * mean_x
    return intercept
```

> [!Note]
> While it’s possible to create `NamedTuples` directly within the code,
> it’s often better to declare them explicitly.
> This helps prevent potential linting errors in tools like `mypy`.
>
> ```python
> def slope() -> NamedTuple("slope_value", slope=float):
>     pass
> ```

You can easily unpack the `NamedTuple` outputs directly within a workflow.
Additionally, you can also have the workflow return a `NamedTuple` as an output.

>[!Note]
> Remember that we are extracting individual task execution outputs by dereferencing them.
> This is necessary because `NamedTuples` function as tuples and require dereferencing.

```python
slope_and_intercept_values = NamedTuple("slope_and_intercept_values", [("slope", float), ("intercept", float)])

@{{< key kit_as >}}.workflow
def simple_wf_with_named_outputs(x: list[int] = [-3, 0, 3], y: list[int] = [7, 4, -2]) -> slope_and_intercept_values:
    slope_value = slope(x=x, y=y)
    intercept_value = intercept(x=x, y=y, slope=slope_value.slope)
    return slope_and_intercept_values(slope=slope_value.slope, intercept=intercept_value.intercept)
```