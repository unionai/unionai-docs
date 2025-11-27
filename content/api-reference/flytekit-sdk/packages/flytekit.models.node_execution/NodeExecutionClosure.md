---
title: NodeExecutionClosure
version: 1.16.10
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


## Properties

| Property | Type | Description |
|-|-|-|
| `created_at` |  |  |
| `deck_uri` |  | {{< multiline >}}:rtype: str
{{< /multiline >}} |
| `duration` |  | {{< multiline >}}:rtype: datetime.timedelta
{{< /multiline >}} |
| `error` |  | {{< multiline >}}:rtype: flytekit.models.core.execution.ExecutionError
{{< /multiline >}} |
| `is_empty` |  |  |
| `output_uri` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `phase` |  | {{< multiline >}}:rtype: int
{{< /multiline >}} |
| `started_at` |  | {{< multiline >}}:rtype: datetime.datetime
{{< /multiline >}} |
| `target_metadata` |  |  |
| `task_node_metadata` |  |  |
| `updated_at` |  |  |
| `workflow_node_metadata` |  |  |

