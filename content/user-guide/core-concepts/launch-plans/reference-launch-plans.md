---
title: Reference launch plans
weight: 7
variants: +flyte +serverless +byoc +selfmanaged
---

# Reference launch plans

A reference launch plan references previously defined, serialized, and registered launch plans. You can reference launch plans from other projects and create workflows that use launch plans declared by others.

When you create a reference launch plan, be sure to verify that the workflow interface corresponds to that of the referenced workflow.

> [!NOTE]
> Reference launch plans cannot be run locally. To test locally, mock them out.

## Example

<!-- TODO: Remove the mention of Flytesnacks below -->
In this example, we create a reference launch plan for the [`simple_wf`](https://github.com/flyteorg/flytesnacks/blob/master/examples/basics/basics/workflow.py#L25) workflow from the [Flytesnacks repository](https://github.com/flyteorg/flytesnacks).

1. Clone the Flytesnacks repository:

    ```shell
    $ git clone git@github.com:flyteorg/flytesnacks.git
    ```

2. Navigate to the `basics` directory:

    ```shell
    $ cd flytesnacks/examples/basics
    ```

3. Register the `simple_wf` workflow:

    ```shell
    $ {{< key cli >}} register --project flytesnacks --domain development --version v1 basics/workflow.py.
    ```

4. Create a file called `simple_wf_ref_lp.py` and copy the following code into it:

    ```python
    import {{< key kit_import >}}
    from flytekit import reference_launch_plan


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


    @{{< key kit_as >}}.workflow
    def run_simple_wf() -> float:
        x = [-8, 2, 4]
        y = [-2, 4, 7]
        return simple_wf_lp(x=x, y=y)
    ```

5. Register the `run_simple_wf` workflow:

    ```shell
    $ {{< key cli >}} register simple_wf_ref_lp.py
    ```

6. In the {{< key product_name >}} UI, run the workflow `run_simple_wf`.

