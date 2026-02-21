---
title: flytekit.core.shim_task
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.shim_task

## Directory

### Classes

| Class | Description |
|-|-|
| [`ExecutableTemplateShimTask`](.././flytekit.core.shim_task#flytekitcoreshim_taskexecutabletemplateshimtask) | The canonical ``@task`` decorated Python function task is pretty simple to reason about. |
| [`ShimTaskExecutor`](.././flytekit.core.shim_task#flytekitcoreshim_taskshimtaskexecutor) |  |

### Variables

| Property | Type | Description |
|-|-|-|
| `T` | `TypeVar` |  |

## flytekit.core.shim_task.ExecutableTemplateShimTask

The canonical ``@task`` decorated Python function task is pretty simple to reason about. At execution time (either
locally or on a Flyte cluster), the function runs.

This class, along with the ``ShimTaskExecutor`` class below, represents another execution pattern. This pattern,
has two components:

* The ``TaskTemplate``, or something like it like a ``FlyteTask``.
* An executor, which can use information from the task template (including the ``custom`` field)

Basically at execution time (both locally and on a Flyte cluster), the task template is given to the executor,
which is responsible for computing and returning the results.

&gt; [!NOTE]
&gt; The interface at execution time will have to derived from the Flyte IDL interface, which means it may be lossy.
  This is because when a task is serialized from Python into the ``TaskTemplate`` some information is lost because
   Flyte IDL can't keep track of every single Python type (or Java type if writing in the Java flytekit).

This class also implements the ``dispatch_execute`` and ``execute`` functions to make it look like a ``PythonTask``
that the ``entrypoint.py`` can execute, even though this class doesn't inherit from ``PythonTask``.



```python
class ExecutableTemplateShimTask(
    tt: _task_model.TaskTemplate,
    executor_type: Type[ShimTaskExecutor],
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `tt` | `_task_model.TaskTemplate` | |
| `executor_type` | `Type[ShimTaskExecutor]` | |
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `executor` | `None` |  |
| `executor_type` | `None` |  |
| `name` | `None` | Return the name of the underlying task. |
| `task_template` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`dispatch_execute()`](#dispatch_execute) | This function is largely similar to the base PythonTask, with the exception that we have to infer the Python. |
| [`execute()`](#execute) | Rather than running here, send everything to the executor. |
| [`post_execute()`](#post_execute) | This function is a stub, just here to keep dispatch_execute compatibility between this class and PythonTask. |
| [`pre_execute()`](#pre_execute) | This function is a stub, just here to keep dispatch_execute compatibility between this class and PythonTask. |


#### dispatch_execute()

```python
def dispatch_execute(
    ctx: FlyteContext,
    input_literal_map: _literal_models.LiteralMap,
) -> Union[_literal_models.LiteralMap, _dynamic_job.DynamicJobSpec]
```
This function is largely similar to the base PythonTask, with the exception that we have to infer the Python
interface before executing. Also, we refer to ``self.task_template`` rather than just ``self`` similar to task
classes that derive from the base ``PythonTask``.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `input_literal_map` | `_literal_models.LiteralMap` | |

#### execute()

```python
def execute(
    kwargs,
) -> Any
```
Rather than running here, send everything to the executor.


| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

#### post_execute()

```python
def post_execute(
    _: Optional[ExecutionParameters],
    rval: Any,
) -> Any
```
This function is a stub, just here to keep dispatch_execute compatibility between this class and PythonTask.


| Parameter | Type | Description |
|-|-|-|
| `_` | `Optional[ExecutionParameters]` | |
| `rval` | `Any` | |

#### pre_execute()

```python
def pre_execute(
    user_params: Optional[ExecutionParameters],
) -> Optional[ExecutionParameters]
```
This function is a stub, just here to keep dispatch_execute compatibility between this class and PythonTask.


| Parameter | Type | Description |
|-|-|-|
| `user_params` | `Optional[ExecutionParameters]` | |

## flytekit.core.shim_task.ShimTaskExecutor

```python
class ShimTaskExecutor(
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `instantiated_in` | `None` |  |
| `lhs` | `None` |  |
| `location` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`execute_from_model()`](#execute_from_model) | This function must be overridden and is where all the business logic for running a task should live. |
| [`find_lhs()`](#find_lhs) |  |


#### execute_from_model()

```python
def execute_from_model(
    tt: _task_model.TaskTemplate,
    kwargs,
) -> Any
```
This function must be overridden and is where all the business logic for running a task should live. Keep in
mind that you're only working with the ``TaskTemplate``. You won't have access to any information in the task
that wasn't serialized into the template.



| Parameter | Type | Description |
|-|-|-|
| `tt` | `_task_model.TaskTemplate` | This is the template, the serialized form of the task. |
| `kwargs` | `**kwargs` | These are the Python native input values to the task. :return: Python native output values from the task. |

#### find_lhs()

```python
def find_lhs()
```
