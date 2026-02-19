---
title: ExecutionClosure
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ExecutionClosure

**Package:** `flytekit.models.execution`

```python
class ExecutionClosure(
    phase: int,
    started_at: datetime.datetime,
    duration: datetime.timedelta,
    error: typing.Optional[_core_execution.ExecutionError],
    outputs: typing.Optional[LiteralMapBlob],
    abort_metadata: typing.Optional[AbortMetadata],
    created_at: typing.Optional[datetime.datetime],
    updated_at: typing.Optional[datetime.datetime],
)
```
| Parameter | Type | Description |
|-|-|-|
| `phase` | `int` | From the flytekit.models.core.execution.WorkflowExecutionPhase enum |
| `started_at` | `datetime.datetime` | |
| `duration` | `datetime.timedelta` | Duration for which the execution has been running. |
| `error` | `typing.Optional[_core_execution.ExecutionError]` | |
| `outputs` | `typing.Optional[LiteralMapBlob]` | |
| `abort_metadata` | `typing.Optional[AbortMetadata]` | Specifies metadata around an aborted workflow execution. |
| `created_at` | `typing.Optional[datetime.datetime]` | |
| `updated_at` | `typing.Optional[datetime.datetime]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `abort_metadata` | `None` |  |
| `created_at` | `None` |  |
| `duration` | `None` |  |
| `error` | `None` |  |
| `is_empty` | `None` |  |
| `outputs` | `None` |  |
| `phase` | `None` | From the flytekit.models.core.execution.WorkflowExecutionPhase enum |
| `started_at` | `None` |  |
| `updated_at` | `None` |  |

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
:rtype: flyteidl.admin.execution_pb2.ExecutionClosure


