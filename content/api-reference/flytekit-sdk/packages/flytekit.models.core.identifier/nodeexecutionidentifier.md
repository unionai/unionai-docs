---
title: NodeExecutionIdentifier
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# NodeExecutionIdentifier

**Package:** `flytekit.models.core.identifier`

```python
class NodeExecutionIdentifier(
    node_id,
    execution_id,
)
```
| Parameter | Type | Description |
|-|-|-|
| `node_id` |  | |
| `execution_id` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `execution_id` | `None` | :rtype: WorkflowExecutionIdentifier |
| `is_empty` | `None` |  |
| `node_id` | `None` | :rtype: Text |

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
:rtype: flyteidl.core.identifier_pb2.NodeExecutionIdentifier


