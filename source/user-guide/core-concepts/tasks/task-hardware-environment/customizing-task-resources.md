# Customizing task resources

When defining a task function, you can specify resource requirements for the pod that runs the task.
Union.ai will take this into account to ensure that the task pod is scheduled to run on a Kubernetes node that meets the specified resource profile.

Resources are specified in the `@union.task` decorator. Here is an example:

```{code-block} python
from flytekit.extras.accelerators import A100

@union.task(
    requests=Resources(mem="120Gi", cpu="44", gpu="8", ephemeral_storage="100Gi"),
    limits=Resources(mem="200Gi", cpu="100", gpu="12", ephemeral_storage="200Gi"),
    accelerator=GPUAccelerator("nvidia-tesla-a100")
)
def my_task()
    ...
```

There are three separate resource-related settings:

* `requests`
* `limits`
* `accelerator`

## The `requests` and `limits` settings

The `requests` and `limits` settings each takes a [`Resource`](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.Resources.html#flytekit-resources) object, which itself has five possible attributes:

* `cpu`: Number of CPU cores (in whole numbers or millicores (`m`)).
* `gpu`: Number of GPU cores (in whole numbers or millicores (`m`)).
* `mem`: Main memory (in `Mi`, `Gi`, etc.).
* `ephemeral_storage`: Ephemeral storage (in `Mi`,  `Gi` etc.).

Note that CPU and GPU allocations can be specified either as whole numbers or in millicores (`m`). For example, `cpu="2500m"` means two and a half CPU cores and `gpu="3000m"`, meaning three GPU cores.

The type of ephemeral storage used depends on the node type and configuration you request from the Union.ai team. By default, all nodes will use network-attached storage for ephemeral storage. However, if a node type has attached NVMe SSD storage, you can request that the Union.ai team configure your cluster to use the attached NVMe as ephemeral storage for that node type.

The `requests` setting tells the system that the task requires _at least_ the resources specified and therefore the pod running this task should be scheduled only on a node that meets or exceeds the resource profile specified.

The `limits` setting serves as a hard upper bound on the resource profile of nodes to be scheduled to run the task.
The task will not be scheduled on a node that exceeds the resource profile specified (in any of the specified attributes).

:::{admonition} GPUs take only `limits`
GPUs should only be specified in the `limits` section of the task decorator:

* You should specify GPU requirements only in `limits`, not in `requests`, because Kubernetes will use the `limits` value as the `requests` value anyway.

* You *can* specify GPU in both `limits` and `requests` but the two values must be equal.

* You cannot specify GPU `requests` without specifying `limits`.
:::

## The `accelerator` setting

{@@ if serverless @@}

The `accelerator` setting further specifies the *type* of GPU required for the task.

{@@ elif byoc @@}

The `accelerator` setting further specifies the *type* of specialized hardware required for the task.
This may be a GPU, a specific variation of a GPU, a fractional GPU, or a different hardware device, such as a TPU.

{@@ endif @@}

See [Accelerators](./accelerators.md) for more information.

## Execution defaults and resource quotas

The execution defaults and resource quotas can be found on the right sidebar of the Dashboard.
They can be edited by selecting the gear icon:

![](/_static/images/user-guide/core-concepts/tasks/task-hardware-environment/customizing-task-resources/execution-defaults-gear.png)

This will open a dialog:

![](/_static/images/user-guide/core-concepts/tasks/task-hardware-environment/customizing-task-resources/execution-defaults-dialog.png)


:::{admonition} Note on ephemeral storage
An ephemeral storage default value of zero means that the task pod will consume storage on the node as needed.
This makes it possible for a pod to get evicted if a node doesn't have enough storage. If your tasks are built to rely on
ephemeral storage, we recommend being explicit with the ephemeral storage you request so as to avoid pod eviction.
:::

{@@ if byoc @@}

## Task resource validation

If you attempt to execute a workflow with unsatisfiable resource requests, the execution will fail immediately rather than being allowed to queue forever.

To remedy such a failure, you should make sure that the appropriate node types are:
* Physically available in your cluster, meaning you have arranged with the Union.ai team to include them when [configuring your data plane](../../../data-plane-setup/configuring-your-data-plane.md).
* Specified in the task decorator (via the `requests`, `limits`, `accelerator`, or other parameters).

Go to the **Resources > Compute** dashboard to find the available node types and their resource profiles.
To make changes to your cluster configuration, go to the [Union.ai Support Portal](https://get.support.union.ai/servicedesk/customer/portal/1/group/6/create/30).

See also [Customizing Task Resources](https://docs.flyte.org/en/latest/deployment/configuration/customizable_resources.html#task-resources) in the Flyte OSS docs.

{@@ endif @@}

## The `with_overrides` method

When `requests`, `limits`, or `accelerator` are specified in the `@union.task` decorator, they apply every time that a task is invoked from a workflow.
In some cases, you may wish to change the resources specified from one invocation to another.
To do that, use the [`with_overrides` method](https://docs.flyte.org/en/latest/flytesnacks/examples/productionizing/customizing_resources.html#resource-with-overrides) of the task function.
For example:

```{code-block} python
@union.task
def my_task(ff: FlyteFile):
    ...

@union.workflow
def my_workflow():
    my_task(ff=smallFile)
    my_task(ff=bigFile).withoverrides(requests=Resources(mem="120Gi", cpu="10"))
```
