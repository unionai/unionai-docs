---
title: Mapping over launch plans
weight: 8
variants: -flyte +serverless +byoc +selfmanaged
---

{{< variant flyte >}}
    {{< markdown >}}
    **Mapping over entities other than Python tasks is a Union specific feature that is not available in Flyte OSS**
    {{< /markdown >}}
{{< /variant >}}

# Mapping over launch plans

You can map over launch plans the same way you can [map over tasks](../tasks/task-types#map-tasks) to execute workflows in parallel across a series of inputs.

You can either map over a `LaunchPlan` object defined in one of your Python modules or a [reference launch plan](./reference-launch-plans) that points to a previously registered launch plan.

## Launch plan defined in your code

Here we define a workflow called `interest_workflow` that we want to parallelize, along with a launch plan called `interest_workflow_lp`, in a file we'll call `map_interest_wf.py`.
We then write a separate workflow, `map_interest_wf`, that uses a `map` to parallelize `interest_workflow` over a list of inputs.

```python
import {{< key kit_import >}}

# Task to calculate monthly interest payment on a loan
@{{< key kit_as >}}.task
def calculate_interest(principal: int, rate: float, time: int) -> float:
    return (principal * rate * time) / 12

# Workflow using the calculate_interest task
@{{< key kit_as >}}.workflow
def interest_workflow(principal: int, rate: float, time: int) -> float:
    return calculate_interest(principal=principal, rate=rate, time=time)

# Create LaunchPlan for interest_workflow
lp = {{< key kit_as >}}.LaunchPlan.get_or_create(
    workflow=interest_workflow,
    name="interest_workflow_lp",
)

# Mapping over the launch plan to calculate interest for multiple loans
@{{< key kit_as >}}.workflow
def map_interest_wf() -> list[float]:
    principal = [1000, 5000, 10000]
    rate = [0.05, 0.04, 0.03]  # Different interest rates for each loan
    time = [12, 24, 36]        # Loan periods in months
    return {{< key kit_as >}}.{{<key map_func>}}(lp)(principal=principal, rate=rate, time=time)

# Mapping over the launch plan to calculate interest for multiple loans while fixing an input
@{{< key kit_as >}}.workflow
def map_interest_fixed_principal_wf() -> list[float]:
    rate = [0.05, 0.04, 0.03]  # Different interest rates for each loan
    time = [12, 24, 36]        # Loan periods in months
    # Note: principal is set to 1000 for all the calculations
    return {{< key kit_as >}}.{{<key map_func>}}(lp, bound_inputs={'principal':1000})(rate=rate, time=time)
```


You can run the `map_interest` workflow locally:

```shell
$ {{< key cli >}} run map_interest_wf.py map_interest_wf
```


You can also run the `map_interest` workflow remotely on {{< key product_name >}}:

```shell
$ {{< key cli >}} run --remote map_interest_wf.py map_interest_wf
```

<!-- TODO: Remove up the mention of Flytesnacks below -->
## Previously registered launch plan

To demonstrate the ability to map over previously registered launch plans, in this example, we map over the [`simple_wf`](https://github.com/flyteorg/flytesnacks/blob/master/examples/basics/basics/workflow.py#L25) launch plan from the basic workflow example in the [Flytesnacks repository](https://github.com/flyteorg/flytesnacks).

Recall that when a workflow is registered, an associated launch plan is created automatically. One of these launch plans will be leveraged in this example, though custom launch plans can also be used.


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
    $ {{< key cli >}} register --project flytesnacks --domain development --version v1 basics/workflow.py
    ```

    Note that the `simple_wf` workflow is defined as follows:

    ```python
    @{{< key kit_as >}}.workflow
    def simple_wf(x: list[int], y: list[int]) -> float:
        slope_value = slope(x=x, y=y)
        intercept_value = intercept(x=x, y=y, slope=slope_value)
        return intercept_value
    ```

4. Create a file called `map_simple_wf.py` and copy the following code into it:

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
        pass


    @{{< key kit_as >}}.workflow
    def map_simple_wf() -> list[float]:
        x = [[-3, 0, 3], [-8, 2, 4], [7, 3, 1]]
        y = [[7, 4, -2], [-2, 4, 7], [3, 6, 4]]
        return {{< key kit_as >}}.{{<key map_func>}}(simple_wf_lp)(x=x, y=y)

    ```

    Note the fact that the reference launch plan has an interface that corresponds exactly to the registered `simple_wf` we wish to map over.

5. Register the `map_simple_wf` workflow. Reference launch plans cannot be run locally, so we will register the `map_simple_wf` workflow to {{< key product_name >}} and run it remotely.

    ```shell
    $ {{< key cli >}} register map_simple_wf.py
    ```

6. In the {{< key product_name >}} UI, run the `map_simple_wf` workflow.
