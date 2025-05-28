---
title: flytekit.models.admin.task_execution
version: 0.1.dev2192+g7c539c3.d20250403
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
| Parameter | Type |
|-|-|
| `id` |  |
| `input_uri` |  |
| `closure` |  |
| `is_parent` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> e: TaskExecution
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.task_execution_pb2.TaskExecution


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `closure` |  | {{< multiline >}}:rtype: TaskExecutionClosure
{{< /multiline >}} |
| `id` |  | {{< multiline >}}:rtype: flytekit.models.core.identifier.TaskExecutionIdentifier
{{< /multiline >}} |
| `input_uri` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `is_empty` |  |  |
| `is_parent` |  | {{< multiline >}}:rtype: bool
{{< /multiline >}} |

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
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
) -> e: TaskExecutionClosure
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.task_execution_pb2.TaskExecutionClosure


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `created_at` |  | {{< multiline >}}:rtype: datetime.datetime
{{< /multiline >}} |
| `duration` |  | {{< multiline >}}:rtype: datetime.timedelta
{{< /multiline >}} |
| `error` |  | {{< multiline >}}:rtype: flytekit.models.core.execution.ExecutionError
{{< /multiline >}} |
| `is_empty` |  |  |
| `logs` |  | {{< multiline >}}:rtype: list[flytekit.models.core.execution.TaskLog]
{{< /multiline >}} |
| `metadata` |  | {{< multiline >}}:rtype: flytekit.models.event.TaskExecutionMetadata
{{< /multiline >}} |
| `output_uri` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `phase` |  | {{< multiline >}}Enum value from flytekit.models.core.execution.TaskExecutionPhase
:rtype: flytekit.models.core.execution.TaskExecutionPhase
{{< /multiline >}} |
| `started_at` |  | {{< multiline >}}:rtype: datetime.datetime
{{< /multiline >}} |
| `updated_at` |  | {{< multiline >}}:rtype: datetime.datetime
{{< /multiline >}} |

