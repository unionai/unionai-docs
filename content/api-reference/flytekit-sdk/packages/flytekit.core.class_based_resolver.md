---
title: flytekit.core.class_based_resolver
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.class_based_resolver

## Directory

### Classes

| Class | Description |
|-|-|
| [`ClassStorageTaskResolver`](.././flytekit.core.class_based_resolver#flytekitcoreclass_based_resolverclassstoragetaskresolver) | Stores tasks inside a class variable. |

## flytekit.core.class_based_resolver.ClassStorageTaskResolver

Stores tasks inside a class variable. The class must be inherited from at the point of usage because the task
loading process basically relies on the same sequence of things happening.


```python
class ClassStorageTaskResolver(
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`add()`](#add) |  |
| [`find_lhs()`](#find_lhs) |  |
| [`get_all_tasks()`](#get_all_tasks) | Future proof method. |
| [`load_task()`](#load_task) | Given the set of identifier keys, should return one Python Task or raise an error if not found. |
| [`loader_args()`](#loader_args) | This is responsible for turning an instance of a task into args that the load_task function can reconstitute. |
| [`name()`](#name) |  |
| [`task_name()`](#task_name) | Overridable function that can optionally return a custom name for a given task. |


#### add()

```python
def add(
    t: flytekit.core.python_auto_container.PythonAutoContainerTask,
)
```
| Parameter | Type |
|-|-|
| `t` | `flytekit.core.python_auto_container.PythonAutoContainerTask` |

#### find_lhs()

```python
def find_lhs()
```
#### get_all_tasks()

```python
def get_all_tasks()
```
Future proof method. Just making it easy to access all tasks (Not required today as we auto register them)


#### load_task()

```python
def load_task(
    loader_args: typing.List[str],
) -> flytekit.core.python_auto_container.PythonAutoContainerTask
```
Given the set of identifier keys, should return one Python Task or raise an error if not found


| Parameter | Type |
|-|-|
| `loader_args` | `typing.List[str]` |

#### loader_args()

```python
def loader_args(
    settings: flytekit.configuration.SerializationSettings,
    t: flytekit.core.python_auto_container.PythonAutoContainerTask,
) -> typing.List[str]
```
This is responsible for turning an instance of a task into args that the load_task function can reconstitute.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |
| `t` | `flytekit.core.python_auto_container.PythonAutoContainerTask` |

#### name()

```python
def name()
```
#### task_name()

```python
def task_name(
    t: flytekit.core.base_task.Task,
) -> typing.Optional[str]
```
Overridable function that can optionally return a custom name for a given task


| Parameter | Type |
|-|-|
| `t` | `flytekit.core.base_task.Task` |

### Properties

| Property | Type | Description |
|-|-|-|
| `instantiated_in` |  |  |
| `lhs` |  |  |
| `location` |  |  |

