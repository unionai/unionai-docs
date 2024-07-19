# Overriding parameters

The `with_overrides` method allows you to specify parameter overrides on [tasks](../core-concepts/tasks/index),
[subworkflows, and sub-launch plans](../core-concepts/workflows/subworkflows-and-sub-launch-plans) at execution time.
This is useful when you want to change the behavior of a task, subworkflow, or sub-launch plan without modifying the original definition.

When calling a task, the following parameters you can specify the following parameters in `with_overrides`:

* `accelerator`: Specify [accelerators](../core-concepts/tasks/task-hardware-environment/accelerators).
* `cache_serialize`: Enable [cache serialization](../core-concepts/caching).
* `cache_version`: Specify the [cache version](../core-concepts/caching).
* `cache`: Enable [caching](../core-concepts/caching).
* `container_image`: Specify a [container image](../core-concepts/tasks/task-software-environment/imagespec).
* `interruptible`: Specify whether the task is [interruptible](../core-concepts/tasks/task-hardware-environment/interruptible-instances).
* `limits`: Specify [resource limits](../core-concepts/tasks/task-hardware-environment/customizing-task-resources).
* `name`: Give a specific name to this task execution. This will appear in the UI (see [below](#using-with_overrides-with-name)).
* `requests`: Specify [resource requests](../core-concepts/tasks/task-hardware-environment/customizing-task-resources).
* `retries`: Specify the [number of times to retry this task](../core-concepts/tasks/task-parameters.md#retries).
* `task_config`: Specify a [task config](../core-concepts/tasks/task-parameters.md#task_config).
* `timeout`: Specify the [task timeout](../core-concepts/tasks/task-parameters.md#timeout).

For example, let's say you have a task that does not have caching enabled.
You can use `with_overrides` to enable caching at execution time as follows:

```python
my_task(a=1, b=2, c=3).with_overrides(cache=True)
```

When calling a workflow or launch plan from within a high-level workflow
(in other words, when invoking a subworkflow or sub-launch plan),
you can specify the following parameters in `with_overrides`:

* `cache_serialize`: Enable [cache serialization](../core-concepts/caching).
* `cache_version`: Specify the [cache version](../core-concepts/caching).
* `cache`: Enable [caching](../core-concepts/caching).

## Using `with_overrides` with `name`

Using `with_overrides` with `name` is a particularly useful feature.
For example, you can use `with_overrides(name="my_task")` to give a specific name to the task execution, which will appear in the UI.
The name specified can be chosen or generated at invocation time without modifying the task definition.

```python
@workflow
def wf() -> int:
    my_task(a=1, b=1, c=1).with_overrides(name="all-1")
    my_task(a=2, b=2, c=2).with_overrides(name="all-2")
    return my_task(a=1, b=1, c=1)
```

The above code would produce the following workflow display in the UI:

![workflow_with_overrides_name](/_static/images/with_overrides_name.png)