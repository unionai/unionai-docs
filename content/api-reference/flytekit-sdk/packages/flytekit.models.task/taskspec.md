---
title: TaskSpec
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TaskSpec

**Package:** `flytekit.models.task`

```python
class TaskSpec(
    template: flytekit.models.task.TaskTemplate,
    docs: typing.Optional[flytekit.models.documentation.Documentation],
)
```
| Parameter | Type | Description |
|-|-|-|
| `template` | `flytekit.models.task.TaskTemplate` | |
| `docs` | `typing.Optional[flytekit.models.documentation.Documentation]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `docs` | `None` | :rtype: Description entity for the task |
| `is_empty` | `None` |  |
| `template` | `None` | :rtype: TaskTemplate |

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
:rtype: flyteidl.admin.tasks_pb2.TaskSpec


