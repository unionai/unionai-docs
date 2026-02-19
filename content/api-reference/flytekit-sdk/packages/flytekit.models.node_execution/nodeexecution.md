---
title: NodeExecution
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# NodeExecution

**Package:** `flytekit.models.node_execution`

```python
class NodeExecution(
    id,
    input_uri,
    closure,
    metadata: flyteidl.admin.node_execution_pb2.NodeExecutionMetaData,
)
```
| Parameter | Type | Description |
|-|-|-|
| `id` |  | |
| `input_uri` |  | |
| `closure` |  | |
| `metadata` | `flyteidl.admin.node_execution_pb2.NodeExecutionMetaData` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `closure` | `None` | :rtype: NodeExecutionClosure |
| `id` | `None` | :rtype: flytekit.models.core.identifier.NodeExecutionIdentifier |
| `input_uri` | `None` | :rtype: Text |
| `is_empty` | `None` |  |
| `metadata` | `None` |  |

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
    p: flyteidl.admin.node_execution_pb2.NodeExecution,
) -> NodeExecution
```
| Parameter | Type | Description |
|-|-|-|
| `p` | `flyteidl.admin.node_execution_pb2.NodeExecution` | |

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
