---
title: EagerFailureTaskResolver
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# EagerFailureTaskResolver

**Package:** `flytekit.core.python_function_task`

## Properties

| Property | Type | Description |
|-|-|-|
| `location` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`get_all_tasks()`](#get_all_tasks) | Future proof method. |
| [`load_task()`](#load_task) | Given the set of identifier keys, should return one Python Task or raise an error if not found. |
| [`loader_args()`](#loader_args) | Return a list of strings that can help identify the parameter Task. |
| [`name()`](#name) |  |
| [`task_name()`](#task_name) | Overridable function that can optionally return a custom name for a given task. |


### get_all_tasks()

```python
def get_all_tasks()
```
Future proof method. Just making it easy to access all tasks (Not required today as we auto register them)


### load_task()

```python
def load_task(
    loader_args: List[str],
) -> Task
```
Given the set of identifier keys, should return one Python Task or raise an error if not found


| Parameter | Type | Description |
|-|-|-|
| `loader_args` | `List[str]` | |

### loader_args()

```python
def loader_args(
    settings: SerializationSettings,
    t: Task,
) -> List[str]
```
Return a list of strings that can help identify the parameter Task


| Parameter | Type | Description |
|-|-|-|
| `settings` | `SerializationSettings` | |
| `t` | `Task` | |

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

