---
title: TaskExecutionMetadata
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TaskExecutionMetadata

**Package:** `flytekit.models.task`

```python
class TaskExecutionMetadata(
    task_execution_id,
    namespace,
    labels,
    annotations,
    k8s_service_account,
    environment_variables,
    identity,
)
```
Runtime task execution metadata.



| Parameter | Type | Description |
|-|-|-|
| `task_execution_id` |  | |
| `namespace` |  | |
| `labels` |  | |
| `annotations` |  | |
| `k8s_service_account` |  | |
| `environment_variables` |  | |
| `identity` |  | |

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
:rtype: flyteidl.admin.agent_pb2.TaskExecutionMetadata


## Properties

| Property | Type | Description |
|-|-|-|
| `annotations` |  |  |
| `environment_variables` |  |  |
| `identity` |  |  |
| `is_empty` |  |  |
| `k8s_service_account` |  |  |
| `labels` |  |  |
| `namespace` |  |  |
| `task_execution_id` |  |  |

