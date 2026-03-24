---
title: flytekit.models.admin.task_execution
version: 1.16.15
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.models.admin.task_execution

## Directory

### Classes

| Class | Description |
|-|-|
| [`TaskExecution`](.././flytekit.models.admin.task_execution#flytekitmodelsadmintask_executiontaskexecution) |  |
| [`TaskExecutionClosure`](.././flytekit.models.admin.task_execution#flytekitmodelsadmintask_executiontaskexecutionclosure) |  |

## flytekit.models.admin.task_execution.TaskExecution

### Parameters

```python
class TaskExecution(
    id,
    input_uri,
    closure,
    is_parent,
)
```
| Parameter | Type | Description |
|-|-|-|
| `id` |  | |
| `input_uri` |  | |
| `closure` |  | |
| `is_parent` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `closure` | `None` |  |
| `id` | `None` |  |
| `input_uri` | `None` |  |
| `is_empty` | `None` |  |
| `is_parent` | `None` |  |

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
    proto,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` |  | |

**Returns:** TaskExecution

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
**Returns:** flyteidl.admin.task_execution_pb2.TaskExecution

## flytekit.models.admin.task_execution.TaskExecutionClosure

### Parameters

```python
class TaskExecutionClosure(
    phase,
    logs,
    started_at,
    duration,
    created_at,
    updated_at,
    output_uri,
    error,
    metadata,
)
```
| Parameter | Type | Description |
|-|-|-|
| `phase` |  | |
| `logs` |  | |
| `started_at` |  | |
| `duration` |  | |
| `created_at` |  | |
| `updated_at` |  | |
| `output_uri` |  | |
| `error` |  | |
| `metadata` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `created_at` | `None` |  |
| `duration` | `None` |  |
| `error` | `None` |  |
| `is_empty` | `None` |  |
| `logs` | `None` |  |
| `metadata` | `None` |  |
| `output_uri` | `None` |  |
| `phase` | `None` | Enum value from flytekit.models.core.execution.TaskExecutionPhase |
| `started_at` | `None` |  |
| `updated_at` | `None` |  |

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
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

**Returns:** TaskExecutionClosure

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
**Returns:** flyteidl.admin.task_execution_pb2.TaskExecutionClosure

