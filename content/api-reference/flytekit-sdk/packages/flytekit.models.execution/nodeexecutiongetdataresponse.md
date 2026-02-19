---
title: NodeExecutionGetDataResponse
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# NodeExecutionGetDataResponse

**Package:** `flytekit.models.execution`

```python
class NodeExecutionGetDataResponse(
    args,
    dynamic_workflow: typing.Optional[DynamicWorkflowNodeMetadata],
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `dynamic_workflow` | `typing.Optional[DynamicWorkflowNodeMetadata]` | |
| `kwargs` | `**kwargs` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `dynamic_workflow` | `None` |  |
| `full_inputs` | `None` | :rtype: _literals_models.LiteralMap |
| `full_outputs` | `None` | :rtype: _literals_models.LiteralMap |
| `inputs` | `None` | :rtype: _common_models.UrlBlob |
| `is_empty` | `None` |  |
| `outputs` | `None` | :rtype: _common_models.UrlBlob |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: _node_execution_pb2. |


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
:rtype: _node_execution_pb2.NodeExecutionGetDataResponse


