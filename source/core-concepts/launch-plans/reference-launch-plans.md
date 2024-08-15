# Reference launch plans

A reference launch plan references previously defined, serialized, and registered launch plans. You can reference launch plans from other projects and create workflows that use launch plans declared by others.

When you create a reference launch plan, be sure to verify that the workflow interface corresponds to that of the referenced workflow.

```{note}
Reference launch plans cannot be run locally. To run this example, clone the flytesnacks repo, register the `simple_wf` workflow (in `basics/basics/workflow.py`), create a separate file for the reference launch plan code below, and register the reference launch plan.
```

{@@ if serverless @@}
```{code-block} python
@reference_launch_plan(
    project="default",
    domain="development",
    name="basics.workflow.simple_wf",
    version="v1",
)
def simple_wf_lp(
    x: list[int], y: list[int]
) -> float:
    return 1.0


@workflow
def map_simple_wf() -> list[float]:
    x = [[-3, 0, 3], [-8, 2, 4], [7, 3, 1]]
    y = [[7, 4, -2], [-2, 4, 7], [3, 6, 4]]
    return map_task(simple_wf_lp)(x=x, y=y)

```
{@@ elif byoc @@}
```{code-block} python
@reference_launch_plan(
    project="flytesnacks",
    domain="development",
    name="basics.workflow.simple_wf",
    version="v1",
)
def simple_wf_lp(
    x: list[int], y: list[int]
) -> float:
    return 1.0


@workflow
def map_simple_wf() -> list[float]:
    x = [[-3, 0, 3], [-8, 2, 4], [7, 3, 1]]
    y = [[7, 4, -2], [-2, 4, 7], [3, 6, 4]]
    return map_task(simple_wf_lp)(x=x, y=y)

```
{@@ endif @@}

