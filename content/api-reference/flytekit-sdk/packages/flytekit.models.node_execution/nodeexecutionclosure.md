---
title: NodeExecutionClosure
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# NodeExecutionClosure

**Package:** `flytekit.models.node_execution`

```python
class NodeExecutionClosure(
    phase,
    started_at,
    duration,
    output_uri,
    deck_uri,
    error,
    workflow_node_metadata: typing.Optional[flytekit.models.node_execution.WorkflowNodeMetadata],
    task_node_metadata: typing.Optional[flytekit.models.node_execution.TaskNodeMetadata],
    created_at: typing.Optional[datetime.datetime],
    updated_at: typing.Optional[datetime.datetime],
)
```
| Parameter | Type | Description |
|-|-|-|
| `phase` |  | |
| `started_at` |  | |
| `duration` |  | |
| `output_uri` |  | |
| `deck_uri` |  | |
| `error` |  | |
| `workflow_node_metadata` | `typing.Optional[flytekit.models.node_execution.WorkflowNodeMetadata]` | |
| `task_node_metadata` | `typing.Optional[flytekit.models.node_execution.TaskNodeMetadata]` | |
| `created_at` | `typing.Optional[datetime.datetime]` | |
| `updated_at` | `typing.Optional[datetime.datetime]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `created_at` | `None` |  |
| `deck_uri` | `None` | :rtype: str |
| `duration` | `None` | :rtype: datetime.timedelta |
| `error` | `None` | :rtype: flytekit.models.core.execution.ExecutionError |
| `is_empty` | `None` |  |
| `output_uri` | `None` | :rtype: Text |
| `phase` | `None` | :rtype: int |
| `started_at` | `None` | :rtype: datetime.datetime |
| `target_metadata` | `None` |  |
| `task_node_metadata` | `None` |  |
| `updated_at` | `None` |  |
| `workflow_node_metadata` | `None` |  |

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
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

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
:rtype: flyteidl.admin.node_execution_pb2.NodeExecutionClosure


