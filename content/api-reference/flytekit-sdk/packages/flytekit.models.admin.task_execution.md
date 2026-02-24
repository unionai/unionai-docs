---
title: flytekit.models.admin.task_execution
version: 1.16.14
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
| `closure` | `None` | :rtype: TaskExecutionClosure |
| `id` | `None` | :rtype: flytekit.models.core.identifier.TaskExecutionIdentifier |
| `input_uri` | `None` | :rtype: Text |
| `is_empty` | `None` |  |
| `is_parent` | `None` | :rtype: bool |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.task_execution_pb2.TaskExecution


## flytekit.models.admin.task_execution.TaskExecutionClosure

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
| `created_at` | `None` | :rtype: datetime.datetime |
| `duration` | `None` | :rtype: datetime.timedelta |
| `error` | `None` | :rtype: flytekit.models.core.execution.ExecutionError |
| `is_empty` | `None` |  |
| `logs` | `None` | :rtype: list[flytekit.models.core.execution.TaskLog] |
| `metadata` | `None` | :rtype: flytekit.models.event.TaskExecutionMetadata |
| `output_uri` | `None` | :rtype: Text |
| `phase` | `None` | Enum value from flytekit.models.core.execution.TaskExecutionPhase :rtype: flytekit.models.core.execution.TaskExecutionPhase |
| `started_at` | `None` | :rtype: datetime.datetime |
| `updated_at` | `None` | :rtype: datetime.datetime |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.task_execution_pb2.TaskExecutionClosure


