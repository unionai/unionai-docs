---
title: Task
version: 2.0.0b50
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Task

**Package:** `flyte.remote`

```python
class Task(
    pb2: task_definition_pb2.Task,
)
```
Initialize a Task object.



| Parameter | Type | Description |
|-|-|-|
| `pb2` | `task_definition_pb2.Task` | The task protobuf definition. |

## Properties

| Property | Type | Description |
|-|-|-|
| `name` | `None` | The name of the task. |
| `url` | `None` | Get the console URL for viewing the task. |
| `version` | `None` | The version of the task. |

## Methods

| Method | Description |
|-|-|
| [`get()`](#get) | Get a task by its ID or name. |
| [`listall()`](#listall) | Get all runs for the current project and domain. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


### get()

```python
def get(
    name: str,
    project: str | None,
    domain: str | None,
    version: str | None,
    auto_version: AutoVersioning | None,
) -> LazyEntity
```
Get a task by its ID or name. If both are provided, the ID will take precedence.

Either version or auto_version are required parameters.



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | The name of the task. |
| `project` | `str \| None` | The project of the task. |
| `domain` | `str \| None` | The domain of the task. |
| `version` | `str \| None` | The version of the task. |
| `auto_version` | `AutoVersioning \| None` | If set to "latest", the latest-by-time ordered from now, version of the task will be used. If set to "current", the version will be derived from the callee tasks context. This is useful if you are deploying all environments with the same version. If auto_version is current, you can only access the task from within a task context. |

### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Task.listall.aio()`.
```python
def listall(
    cls,
    by_task_name: str | None,
    by_task_env: str | None,
    project: str | None,
    domain: str | None,
    sort_by: Tuple[str, Literal['asc', 'desc']] | None,
    limit: int,
) -> Union[AsyncIterator[Task], Iterator[Task]]
```
Get all runs for the current project and domain.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `by_task_name` | `str \| None` | If provided, only tasks with this name will be returned. |
| `by_task_env` | `str \| None` | If provided, only tasks with this environment prefix will be returned. |
| `project` | `str \| None` | The project to filter tasks by. If None, the current project will be used. |
| `domain` | `str \| None` | The domain to filter tasks by. If None, the current domain will be used. |
| `sort_by` | `Tuple[str, Literal['asc', 'desc']] \| None` | The sorting criteria for the project list, in the format (field, order). |
| `limit` | `int` | The maximum number of tasks to return. :return: An iterator of runs. |

### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.

Returns:
    dict: A dictionary representation of the object.


### to_json()

```python
def to_json()
```
Convert the object to a JSON string.

Returns:
    str: A JSON string representation of the object.


