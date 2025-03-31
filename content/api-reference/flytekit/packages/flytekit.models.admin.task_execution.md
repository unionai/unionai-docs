---
title: flytekit.models.admin.task_execution
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
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
| Parameter | Type |
|-|-|
| `id` |  |
| `input_uri` |  |
| `closure` |  |
| `is_parent` |  |

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
    proto,
) -> TaskExecution
```
| Parameter | Type |
|-|-|
| `proto` |  |

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
| `closure` |  |  |
| `id` |  |  |
| `input_uri` |  |  |
| `is_empty` |  |  |
| `is_parent` |  |  |

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
| Parameter | Type |
|-|-|
| `phase` |  |
| `logs` |  |
| `started_at` |  |
| `duration` |  |
| `created_at` |  |
| `updated_at` |  |
| `output_uri` |  |
| `error` |  |
| `metadata` |  |

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
    p,
) -> TaskExecutionClosure
```
| Parameter | Type |
|-|-|
| `p` |  |

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
| `created_at` |  |  |
| `duration` |  |  |
| `error` |  |  |
| `is_empty` |  |  |
| `logs` |  |  |
| `metadata` |  |  |
| `output_uri` |  |  |
| `phase` |  | {{< multiline >}}Enum value from flytekit.models.core.execution.TaskExecutionPhase
{{< /multiline >}} |
| `started_at` |  |  |
| `updated_at` |  |  |

