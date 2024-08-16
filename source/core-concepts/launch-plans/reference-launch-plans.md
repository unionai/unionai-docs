# Reference launch plans

A reference launch plan references previously defined, serialized, and registered launch plans. You can reference launch plans from other projects and create workflows that use launch plans declared by others.

When you create a reference launch plan, be sure to verify that the workflow interface corresponds to that of the referenced workflow.

```{note}
Reference launch plans cannot be run locally. To test locally, mock them out.
```

## Example

In this example, we create a reference launch plan for the [`simple_wf`](https://github.com/flyteorg/flytesnacks/blob/7a300ac43f3da41a4e01bd4dae9d45e8c0094ce3/examples/basics/basics/workflow.py#L25) workflow from the [Flytesnacks repository](https://github.com/flyteorg/flytesnacks).

1. Clone the Flytesnacks repository:
```{code-block} bash
git clone git@github.com:flyteorg/flytesnacks.git
```
2. Navigate to the `basics` directory:
```{code-block} bash
cd flytesnacks/examples/basics
```
3. Register the `simple_wf` workflow:
{@@ if serverless @@}
```{code-block} bash
unionai register --project default --domain development --version v1 basics/workflow.py.
```
{@@ elif byoc @@}
```{code-block} bash
unionai register --project flytesnacks --domain development --version v1 basics/workflow.py.
```
{@@ endif @@}
4. Create a file called `simple_wf_ref_lp.py` and copy the following code into it:
{@@ if serverless @@}
```{code-block} python
from flytekit import reference_launch_plan, workflow, map_task


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
def run_simple_wf() -> float:
    x = [-8, 2, 4]
    y = [-2, 4, 7]
    return simple_wf_lp(x=x, y=y)

```
{@@ elif byoc @@}
```{code-block} python
from flytekit import reference_launch_plan, workflow, map_task


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
def run_simple_wf() -> float:
    x = [-8, 2, 4]
    y = [-2, 4, 7]
    return simple_wf_lp(x=x, y=y)
```
{@@ endif @@}
5. Register the `simple_wf_ref_lp` launch plan:
{@@ if serverless @@}
```{code-block} bash
unionai register simple_wf_ref_lp.py
```
{@@ elif byoc @@}
```{code-block} bash
unionai register simple_wf_ref_lp.py
```
{@@ endif @@}
6. In the Union UI, run the workflow `run_simple_wf`.

