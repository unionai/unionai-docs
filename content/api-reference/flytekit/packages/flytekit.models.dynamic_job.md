---
title: flytekit.models.dynamic_job
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.dynamic_job

## Directory

### Classes

| Class | Description |
|-|-|
| [`DynamicJobSpec`](.././flytekit.models.dynamic_job#flytekitmodelsdynamic_jobdynamicjobspec) |  |

## flytekit.models.dynamic_job.DynamicJobSpec

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



| Parameter | Type |
|-|-|
| `tasks` |  |
| `nodes` |  |
| `min_successes` |  |
| `outputs` |  |
| `subworkflows` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `min_successes` |  | {{< multiline >}}An absolute number of the minimum number of successful completions of subtasks. As
soon as this criteria is met, the future job will be marked as successful and outputs will be computed.
{{< /multiline >}} |
| `nodes` |  | {{< multiline >}}A collection of dynamic nodes.
{{< /multiline >}} |
| `outputs` |  | {{< multiline >}}Describes how to bind the final output of the future task from the outputs of executed nodes.
The referenced ids in bindings should have the generated id for the subtask.
{{< /multiline >}} |
| `subworkflows` |  | {{< multiline >}}A collection of subworkflows to execute.
{{< /multiline >}} |
| `tasks` |  | {{< multiline >}}A collection of tasks to execute.
{{< /multiline >}} |

