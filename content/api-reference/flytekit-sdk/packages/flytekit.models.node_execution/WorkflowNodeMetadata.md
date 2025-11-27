---
title: WorkflowNodeMetadata
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# WorkflowNodeMetadata

**Package:** `flytekit.models.node_execution`

```python
class WorkflowNodeMetadata(
    execution_id: flytekit.models.core.identifier.WorkflowExecutionIdentifier,
)
```
| Parameter | Type | Description |
|-|-|-|
| `execution_id` | `flytekit.models.core.identifier.WorkflowExecutionIdentifier` | |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


### from_flyte_idl()

```python
def from_flyte_idl(
    p: flyteidl.admin.node_execution_pb2.WorkflowNodeMetadata,
) -> WorkflowNodeMetadata
```
| Parameter | Type | Description |
|-|-|-|
| `p` | `flyteidl.admin.node_execution_pb2.WorkflowNodeMetadata` | |

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
## Properties

| Property | Type | Description |
|-|-|-|
| `execution_id` |  |  |
| `is_empty` |  |  |

