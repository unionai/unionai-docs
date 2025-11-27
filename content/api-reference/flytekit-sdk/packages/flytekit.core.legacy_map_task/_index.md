---
title: flytekit.core.legacy_map_task
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.legacy_map_task


Flytekit map tasks specify how to run a single task across a list of inputs. Map tasks themselves are constructed with
a reference task as well as run-time parameters that limit execution concurrency and failure tolerations.

## Directory

### Classes

| Class | Description |
|-|-|
| [`MapPythonTask`](../flytekit.core.legacy_map_task/mappythontask) | A MapPythonTask defines a {{< py_class_ref flytekit.PythonTask >}} which specifies how to run. |
| [`MapTaskResolver`](../flytekit.core.legacy_map_task/maptaskresolver) | Special resolver that is used for MapTasks. |

### Methods

| Method | Description |
|-|-|
| [`map_task()`](#map_task) | Use a map task for parallelizable tasks that run across a list of an input type. |


### Variables

| Property | Type | Description |
|-|-|-|
| `CONTAINER_ARRAY_TASK` | `str` |  |

## Methods

#### map_task()

```python
def map_task(
    task_function: typing.Union[flytekit.core.python_function_task.PythonFunctionTask, flytekit.core.python_function_task.PythonInstanceTask, functools.partial],
    concurrency: int,
    min_success_ratio: float,
    kwargs,
)
```
Use a map task for parallelizable tasks that run across a list of an input type. A map task can be composed of
any individual {{<py_class_ref "flytekit.PythonFunctionTask">}}.

Invoke a map task with arguments using {{<py_class_ref list>}} version of the expected input.

Usage:

<!--
.. literalinclude:: ../../../tests/flytekit/unit/core/test_map_task.py
   :start-after: # test_map_task_start
   :end-before: # test_map_task_end
   :language: python
   :dedent: 4
-->

```python
@task
def my_mappable_task(a: int) -> typing.Optional[str]:
    return str(a)

@workflow
def my_wf(x: typing.List[int]) -> typing.List[typing.Optional[str]]:
    return map_task(
        my_mappable_task,
        metadata=TaskMetadata(retries=1),
        concurrency=10,
        min_success_ratio=0.75,
    )(a=x).with_overrides(requests=Resources(cpu="10M"))
```
At run time, the underlying map task will be run for every value in the input collection. Attributes
such as {{<py_class_ref "flytekit.TaskMetadata">}} and ``with_overrides`` are applied to individual instances
of the mapped task.

**Map Task Plugins**

There are two plugins to run maptasks that ship as part of flyteplugins:

1. K8s Array
2. [`AWS batch`](https://docs.flyte.org/en/latest/deployment/plugin_setup/aws/batch.html)

Enabling a plugin is controlled in the plugin configuration at [`values-sandbox.yaml`](https://github.com/flyteorg/flyte/blob/10cee9f139824512b6c5be1667d321bdbc8835fa/charts/flyte/values-sandbox.yaml#L152-L162).

**K8s Array**

By default, the map task uses the ``K8s Array`` plugin. It executes array tasks by launching a pod for every instance in the array. It’s simple to use, has a straightforward implementation, and works out of the box.

**AWS batch**

Learn more about ``AWS batch`` setup configuration [`here`](https://docs.flyte.org/en/latest/deployment/plugin_setup/aws/batch.html#deployment-plugin-setup-aws-array).

A custom plugin can also be implemented to handle the task type.



| Parameter | Type | Description |
|-|-|-|
| `task_function` | `typing.Union[flytekit.core.python_function_task.PythonFunctionTask, flytekit.core.python_function_task.PythonInstanceTask, functools.partial]` | This argument is implicitly passed and represents the repeatable function |
| `concurrency` | `int` | If specified, this limits the number of mapped tasks than can run in parallel to the given batch size. If the size of the input exceeds the concurrency value, then multiple batches will be run serially until all inputs are processed. If left unspecified, this means unbounded concurrency. |
| `min_success_ratio` | `float` | If specified, this determines the minimum fraction of total jobs which can complete successfully before terminating this task and marking it successful. |
| `kwargs` | `**kwargs` | |

