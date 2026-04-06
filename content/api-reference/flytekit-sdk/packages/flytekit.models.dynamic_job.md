---
title: flytekit.models.dynamic_job
version: 1.16.16
variants: +flyte +union
layout: py_api
---

# flytekit.models.dynamic_job

## Directory

### Classes

| Class | Description |
|-|-|
| [`DynamicJobSpec`](.././flytekit.models.dynamic_job#flytekitmodelsdynamic_jobdynamicjobspec) |  |

## flytekit.models.dynamic_job.DynamicJobSpec

### Parameters

```python
class DynamicJobSpec(
    tasks,
    nodes,
    min_successes,
    outputs,
    subworkflows,
)
```
Initializes a new FutureTaskDocument.



| Parameter | Type | Description |
|-|-|-|
| `tasks` |  | |
| `nodes` |  | |
| `min_successes` |  | |
| `outputs` |  | |
| `subworkflows` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `min_successes` | `None` | An absolute number of the minimum number of successful completions of subtasks. As     soon as this criteria is met, the future job will be marked as successful and outputs will be computed. |
| `nodes` | `None` | A collection of dynamic nodes. |
| `outputs` | `None` | Describes how to bind the final output of the future task from the outputs of executed nodes.     The referenced ids in bindings should have the generated id for the subtask. |
| `subworkflows` | `None` | A collection of subworkflows to execute. |
| `tasks` | `None` | A collection of tasks to execute. |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** DynamicJobSpec

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.dynamic_job.DynamicJobSpec

