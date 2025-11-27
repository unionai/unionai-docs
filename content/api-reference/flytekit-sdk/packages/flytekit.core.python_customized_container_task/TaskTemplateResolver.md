---
title: TaskTemplateResolver
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TaskTemplateResolver

**Package:** `flytekit.core.python_customized_container_task`

This is a special resolver that resolves the task above at execution time, using only the ``TaskTemplate``,
meaning it should only be used for tasks that contain all pertinent information within the template itself.

This class differs from some TaskResolverMixin pattern a bit. Most of the other resolvers you'll find,

* restores the same task when ``load_task`` is called as the object that ``loader_args`` was called on.
  That is, even though at run time it's in a container on a cluster and is obviously a different Python process,
  the Python object in memory should look the same.
* offers a one-to-one mapping between the list of strings returned by the ``loader_args`` function, an the task,
  at least within the container.

This resolver differs in that,
* when loading a task, the task that is a loaded is always an ``ExecutableTemplateShimTask``, regardless of what
  kind of task it was originally. It will only ever have what's available to it from the ``TaskTemplate``. No
  information that wasn't serialized into the template will be available.
* all tasks will result in the same list of strings for a given subclass of the ``ShimTaskExecutor``
  executor. The strings will be ``["{{.taskTemplatePath}}", "path.to.your.executor"]``

Also, ``get_all_tasks`` will always return an empty list, at least for now.


```python
def TaskTemplateResolver()
```
## Methods

| Method | Description |
|-|-|
| [`find_lhs()`](#find_lhs) |  |
| [`get_all_tasks()`](#get_all_tasks) | Future proof method. |
| [`load_task()`](#load_task) | Given the set of identifier keys, should return one Python Task or raise an error if not found. |
| [`loader_args()`](#loader_args) | Return a list of strings that can help identify the parameter Task. |
| [`name()`](#name) |  |
| [`task_name()`](#task_name) | Overridable function that can optionally return a custom name for a given task. |


### find_lhs()

```python
def find_lhs()
```
### get_all_tasks()

```python
def get_all_tasks()
```
Future proof method. Just making it easy to access all tasks (Not required today as we auto register them)


### load_task()

```python
def load_task(
    loader_args: List[str],
) -> ExecutableTemplateShimTask
```
Given the set of identifier keys, should return one Python Task or raise an error if not found


| Parameter | Type | Description |
|-|-|-|
| `loader_args` | `List[str]` | |

### loader_args()

```python
def loader_args(
    settings: SerializationSettings,
    t: PythonCustomizedContainerTask,
) -> List[str]
```
Return a list of strings that can help identify the parameter Task


| Parameter | Type | Description |
|-|-|-|
| `settings` | `SerializationSettings` | |
| `t` | `PythonCustomizedContainerTask` | |

### name()

```python
def name()
```
### task_name()

```python
def task_name(
    t: flytekit.core.base_task.Task,
) -> typing.Optional[str]
```
Overridable function that can optionally return a custom name for a given task


| Parameter | Type | Description |
|-|-|-|
| `t` | `flytekit.core.base_task.Task` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `instantiated_in` |  |  |
| `lhs` |  |  |
| `location` |  |  |

