---
title: Imperative workflows
weight: 5
variants: +flyte +serverless +byoc +selfmanaged
---

# Imperative workflows

Workflows are commonly created by applying the `@{{< key kit_as >}}.workflow` decorator to Python functions.
During compilation, this involves processing the function's body and utilizing subsequent calls to
underlying tasks to establish and record the workflow structure. This is the *declarative* approach
and is suitable when manually drafting the workflow.

However, in cases where workflows are constructed programmatically, an imperative style is more appropriate.
For instance, if tasks have been defined already, their sequence and dependencies might have been specified in textual form (perhaps during a transition from a legacy system).
In such scenarios, you want to orchestrate these tasks.
This is where {{< key product_name >}}'s imperative workflows come into play, allowing you to programmatically construct workflows.

## Example

To begin, we define the `slope` and `intercept` tasks:

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
```

Create an imperative workflow:

```python
imperative_wf = Workflow(name="imperative_workflow")
```

Add the workflow inputs to the imperative workflow:

```python
imperative_wf.add_workflow_input("x", list[int])
imperative_wf.add_workflow_input("y", list[int])
```

> If you want to assign default values to the workflow inputs, you can create a [launch plan](../launch-plans).

Add the tasks that need to be triggered from within the workflow:

```python
node_t1 = imperative_wf.add_entity(slope, x=imperative_wf.inputs["x"], y=imperative_wf.inputs["y"])
node_t2 = imperative_wf.add_entity(
    intercept, x=imperative_wf.inputs["x"], y=imperative_wf.inputs["y"], slope=node_t1.outputs["o0"]
)
```

Lastly, add the workflow output:

```python
imperative_wf.add_workflow_output("wf_output", node_t2.outputs["o0"])
```

You can execute the workflow locally as follows:

```python
if __name__ == "__main__":
    print(f"Running imperative_wf() {imperative_wf(x=[-3, 0, 3], y=[7, 4, -2])}")
```

You also have the option to provide a list of inputs and
retrieve a list of outputs from the workflow:

```python
wf_input_y = imperative_wf.add_workflow_input("y", list[str])
node_t3 = wf.add_entity(some_task, a=[wf.inputs["x"], wf_input_y])

wf.add_workflow_output(
    "list_of_outputs",
    [node_t1.outputs["o0"], node_t2.outputs["o0"]],
    python_type=list[str],
)
```