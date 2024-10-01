# Subworkflows and sub-launch plans

In Union it is possible to invoke one workflow from within another.
A parent workflow can invoke a child workflow in two ways: as a **subworkflow** or via a [**sub-launch plan**](../launch-plans/running-launch-plans.md#sub-launch-plans).

In both cases the child workflow is defined and registered normally, exists in the system normally, and can be run independently.

But, if the child workflow is invoked from within the parent **by directly calling the child's function**, then it becomes a **subworkflow**.
The DAG of the subworkflow is embedded directly into the DAG of the parent and effectively become part of the parent workflow execution, sharing the same execution ID and execution context.

On the other hand, if the child workflow is invoked from within the parent [**by calling the child's launch plan**](../launch-plans/index), this is called a **sub-launch plan** and it results in a new top-level workflow execution being invoked with its own execution ID and execution context.
It also appears as a separate top-level entity in the system.
The only difference is that it happens to have been kicked off from within another workflow instead of from the command line or the UI.

Here is an example:

```{literalinclude} ../../../_static/includes/core-concepts/workflows/subworkflows-and-sub-launch-plans/example_1.py
:language: python
```

## When to use subworkflows

Subworkflows allow you to manage parallelism between a workflow and its launched sub-flows, as they execute within the same context as the parent workflow.
Consequently, all nodes of a subworkflow adhere to the overall constraints imposed by the parent workflow.

% TODO: a diagram of the above example

Here's an example illustrating the calculation of slope, intercept and the corresponding y-value.

```{literalinclude} ../../../_static/includes/core-concepts/workflows/subworkflows-and-sub-launch-plans/example_2.py
:language: python
```

The `slope_intercept_wf` computes the slope and intercept of the regression line.
Subsequently, the `regression_line_wf` triggers `slope_intercept_wf` and then computes the y-value.

It is possible to nest a workflow that contains a subworkflow within yet another workflow.
Workflows can be easily constructed from other workflows, even if they also function as standalone entities.
For example, each workflow in the example below has the capability to exist and run independently:

```{literalinclude} ../../../_static/includes/core-concepts/workflows/subworkflows-and-sub-launch-plans/example_3.py
:language: python
```

## When to use sub-launch plans

Sub-launch plans can be useful for implementing exceptionally large or complicated workflows that can’t be adequately implemented as [dynamic workflows](../workflows/dynamic-workflows) or [map tasks](../tasks/task-types.md#map-tasks).
Dynamic workflows and map tasks share the same context and single underlying Kubernetes resource definitions.
Sub-launch plan invoked workflows do not share the same context.
They are executed as a separate top-level entities and thus can be distributed among different Flytepropeller workers and shards, allowing for better parallelism and scale.

Here is an example of invoking a workflow multiple times through its launch plan:

```{literalinclude} ../../../_static/includes/core-concepts/workflows/subworkflows-and-sub-launch-plans/example_4.py
:language: python
:emphasize-lines: 2, 15, 18-20
```
