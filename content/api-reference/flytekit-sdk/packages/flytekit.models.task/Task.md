---
title: Task
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Task

**Package:** `flytekit.models.task`

```python
class Task(
    id,
    closure,
    short_description,
)
```
| Parameter | Type | Description |
|-|-|-|
| `id` |  | |
| `closure` |  | |
| `short_description` |  | |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

### serialize_to_string()

```python
def serialize_to_string()
```
### short_string()

```python
def short_string()
```
:rtype: Text


### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.task_pb2.Task


## Properties

| Property | Type | Description |
|-|-|-|
| `closure` |  | {{< multiline >}}The closure for the underlying workload.
:rtype: TaskClosure
{{< /multiline >}} |
| `id` |  | {{< multiline >}}The (project, domain, name, version) identifier for this task.
:rtype: flytekit.models.core.identifier.Identifier
{{< /multiline >}} |
| `is_empty` |  |  |
| `short_description` |  | {{< multiline >}}The short description of the task.
:rtype: str
{{< /multiline >}} |

