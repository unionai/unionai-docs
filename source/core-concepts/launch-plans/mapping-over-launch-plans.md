## Mapping over launch plans

You can map over launch plans the same way you can [map over tasks](../tasks/task-types.md#map-tasks) to execute launch plans in parallel across a series of inputs.

```{note}
Mapping over launch plans requires the use of reference launch plans. For more information, see [Reference launch plans](reference-launch-plans).
```

### Example

In this example, we map over the [`simple_wf`](https://github.com/flyteorg/flytesnacks/blob/7a300ac43f3da41a4e01bd4dae9d45e8c0094ce3/examples/basics/basics/workflow.py#L25) workflow from the [Flytesnacks repository](https://github.com/flyteorg/flytesnacks).

1. Clone the Flytesnacks repository:
```{code-block} bash
git clone git@github.com:flyteorg/flytesnacks.git
```
2. Navigate to the `basics` directory:
```{code-block} bash
cd flytesnacks/examples/basics
```
{@@ if serverless @@}
3. Register the `simple_wf` workflow:
```{code-block} bash
unionai register --project default --domain development --version $(git rev-parse HEAD) basics/workflow.py.
```
4. Create a file called `map_simple_wf.py` and copy the following code into it:

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
5. Register the launch plan:
```{code-block} bash
unionai register --project default --domain development simple_wf_reference_launch_plan.py
```
{@@ elif byoc @@}
3. Register the `simple_wf` workflow:
```{code-block} bash
unionai register --project flytesnacks --domain development --version $(git rev-parse HEAD) basics/workflow.py.
```
4. Create a file called "simple_wf_reference_launch_plan.py" and copy the following code into it:

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
5. Register the launch plan:
```{code-block} bash
unionai register --project flytesnacks --domain development simple_wf_reference_launch_plan.py
```
{@@ endif @@}
6. In the Union UI, run the reference launch plan.
