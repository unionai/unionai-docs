---
title: Failure node
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
---

# Failure node

The failure node feature enables you to designate a specific node to execute in the event of a failure within your workflow.

For example, a workflow involves creating a cluster at the beginning, followed by the execution of tasks, and concludes with the deletion of the cluster once all tasks are completed.
However, if any task within the workflow encounters an error, the system will abort the entire workflow and won’t delete the cluster.
This poses a challenge if you still need to clean up the cluster even in a task failure.

To address this issue, you can add a failure node into your workflow.
This ensures that critical actions, such as deleting the cluster, are executed even in the event of failures occurring throughout the workflow execution.


```python
import typing

import {{< key kit_import >}}
from flytekit import WorkflowFailurePolicy
from flytekit.types.error.error import FlyteError


@{{< key kit_as >}}.task
def create_cluster(name: str):
    print(f"Creating cluster: {name}")
```

Create a task that will fail during execution:

```python

# Create a task that will fail during execution
@{{< key kit_as >}}.task
def t1(a: int, b: str):
    print(f"{a} {b}")
    raise ValueError("Fail!")
```

Create a task that will be executed if any of the tasks in the workflow fail:

```python
@{{< key kit_as >}}.task
def clean_up(name: str, err: typing.Optional[FlyteError] = None):
    print(f"Deleting cluster {name} due to {err}")
```

Specify the `on_failure` to a cleanup task. This task will be executed if any of the tasks in the workflow fail.

The inputs of `clean_up` must exactly match the workflow’s inputs.
Additionally, the `err` parameter will be populated with the error message encountered during execution.

```python
@{{< key kit_as >}}.workflow
def wf(a: int, b: str):
    create_cluster(name=f"cluster-{a}")
    t1(a=a, b=b)
```

By setting the failure policy to `FAIL_AFTER_EXECUTABLE_NODES_COMPLETE` to ensure that the `wf1` is executed even if the subworkflow fails.
In this case, both parent and child workflows will fail, resulting in the `clean_up` task being executed twice:

```python
# In this case, both parent and child workflows will fail,
# resulting in the `clean_up` task being executed twice.
@{{< key kit_as >}}.workflow(on_failure=clean_up, failure_policy=WorkflowFailurePolicy.FAIL_AFTER_EXECUTABLE_NODES_COMPLETE)
def wf1(name: str = "my_cluster"):
    c = create_cluster(name=name)
    subwf(name="another_cluster")
    t = t1(a=1, b="2")
    d = delete_cluster(name=name)
    c >> t >> d
```

You can also set the `on_failure` to a workflow.
This workflow will be executed if any of the tasks in the workflow fail:

```python
@{{< key kit_as >}}.workflow(on_failure=clean_up_wf)
def wf2(name: str = "my_cluster"):
    c = create_cluster(name=name)
    t = t1(a=1, b="2")
    d = delete_cluster(name=name)
    c >> t >> d
```
