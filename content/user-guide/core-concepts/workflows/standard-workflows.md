---
title: Standard workflows
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---

# Standard workflows

A standard workflow is defined by a Python function decorated with the `@{{< key kit_as >}}.workflow` decorator.
The function is written in a domain specific language (DSL), a subset of Python syntax that describes the directed acyclic graph (DAG) that is deployed and executed on {{< key product_name >}}.
The syntax of a standard workflow definition can only include the following:

* Calls to functions decorated with `@{{< key kit_as >}}.task` and assignment of variables to the returned values.
* Calls to other functions decorated with `@{{< key kit_as >}}.workflow` and assignment of variables to the returned values (see [Subworkflows](./subworkflows-and-sub-launch-plans)).
* Calls to [`LaunchPlan` objects](../launch-plans) (see [When to use sub-launch plans](./subworkflows-and-sub-launch-plans#when-to-use-sub-launch-plans))
* Calls to functions decorated with `@{{< key kit_as >}}.dynamic` and assignment of variables to the returned values (see [Dynamic workflows](./dynamic-workflows)).
* Calls to functions decorated with `@eager` and assignment of variables to the returned values (see [Eager workflows](./eager-workflows)).
* The special [`conditional` construct](../../programming/conditionals).
* Statements using the [chaining operator `>>`](../../programming/chaining-entities).

## Evaluation of a standard workflow

{{< variant byoc selfmanaged flyte >}}
{{< markdown >}}
When a standard workflow is [run locally in a Python environment](../../development-cycle/running-your-code#running-a-script-in-local-python) it is executed as a normal Python function.
However, when it is registered to {{< key product_name >}}, the top level `@{{< key kit_as >}}.workflow`-decorated function is evaluated as follows:
{{< /markdown >}}
{{< /variant >}}
{{< variant serverless >}}
{{< markdown >}}
When a standard workflow is [run locally in a Python environment](../../development-cycle/running-your-code#running-a-script-in-local-python) it is executed as a normal Python function.
However, when it is registered to {{< key product_name >}}, the top level `@{{< key kit_as >}}.workflow`-decorated function is evaluated as follows:
{{< /markdown >}}
{{< /variant >}}

* Inputs to the workflow are materialized as lazily-evaluated promises which are propagated to downstream tasks and subworkflows.
* All values returned by calls to functions decorated with `@{{< key kit_as >}}.task` , `@{{< key kit_as >}}.dynamic`and `@eager` are also materialized as lazily-evaluated promises.

The resulting structure is used to construct the Directed Acyclic Graph (DAG) and deploy the required containers to the cluster.
The actual evaluation of these promises occurs when the tasks (or dynamic or eager workflows) are executed in their respective containers.

## Conditional construct

Because standard workflows cannot directly include Python `if` statements, a special `conditional` construct is provided that allows you to define conditional logic in a workflow.
For details, see [Conditionals](../../programming/conditionals).
<!-- TODO: Add link to API -->

## Chaining operator

When {{< key product_name >}} builds the DAG for a standard workflow, it uses the passing of values from one task to another to determine the dependency relationships between tasks.

There may be cases where you want to define a dependency between two tasks that is not based on the output of one task being passed as an input to another.
In that case, you can use the chaining operator `>>` to define the dependencies between tasks.
For details, see [Chaining {{< key product_name >}} entities](../../programming/chaining-entities).

## Workflow decorator parameters

The `@{{< key kit_as >}}.workflow` decorator can take the following parameters:

* `failure_policy`: Use the options in [`flytekit.WorkflowFailurePolicy`](../../../api-reference/flytekit-sdk).
<!-- TODO: Add link to API -->

{{< variant byoc selfmanaged flyte >}}
{{< markdown >}}
* `interruptible`: Indicates if tasks launched from this workflow are interruptible by default. See [Interruptible instances](../tasks/task-hardware-environment/interruptible-instances).
{{< /markdown >}}
{{< /variant >}}

* `on_failure`: Invoke this workflow or task on failure. The workflow specified must have the same parameter signature as the current workflow, with an additional parameter called `error`.

* `docs`: A description entity for the workflow.
