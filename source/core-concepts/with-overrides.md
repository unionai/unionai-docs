# `with_overrides`

The `with_overrides` method allows you to specify parameter overrides on [tasks](./tasks/index), [subworkflows, and sub-launch plans](./workflows/subworkflows-and-sub-launch-plans) at execution time. This is useful when you want to change the behavior of a task, subworkflow, or sub-launch plan without modifying the original definition.

The following parameters can be specified in `with_overrides` when calling a `task`:

* `accelerator`: Specify [accelerators](./tasks/task-hardware-environment/accelerators).
* `cache_serialize`: Enable [cache serialization](./caching).
* `cache_version`: Specify the [cache version](./caching).
* `cache`: Enable [caching](./caching).
* `container_image`: Specify a [container image](./tasks/task-software-environment/imagespec).
* `interruptible`: Specify whether the task is [interruptible](./tasks/task-hardware-environment/interruptible-instances).
* `limits`: Specify [resource limits](./tasks/task-hardware-environment/customizing-task-resources).
* `name`: Give a specific name to this task execution. This will appear in the UI (see below).
* `requests`: Specify [resource requests](./tasks/task-hardware-environment/customizing-task-resources).
* `retries`: Specify the [number of times to retry this task](./tasks/task-parameters.md#retries).
* `task_config`: Specify a [task config](./tasks/task-parameters.md#task_config).
* `timeout`: Specify the [task timeout](./tasks/task-parameters.md#timeout).

Additionally, when calling a workflow or launch plan from within a high-level workflow (in other worlds when invoking a subworkflow or sub-launch plan), you can specify the following parameters in `with_overrides`:

* `cache_serialize`: Enable [cache serialization](./caching).
* `cache_version`: Specify the [cache version](./caching).
* `cache`: Enable [caching](./caching).

## Using `with_overrides` with `name`

Using `with_overrides` with `name` is a paricularly useful feature. For example, you can use `with_overrides(name="my_task")` to give a specific name to the task execution, which will appear in the UI.
The name specified can be chosenor generated at invocation time without the need to modify the task definition.
For example the following code:

```python
@workflow
def wf() -> int:
    my_task(a=1, b=1, c=1).with_overrides(name="all-1")
    my_task(a=2, b=2, c=2).with_overrides(name="all-2")
    return my_task(a=1, b=1, c=1)
```

Would produce the following workflow display in the UI:

![workflow_with_overrides_name](/_static/images/with_overrides_name.png)