---
title: NodeExecutionGetDataResponse
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# NodeExecutionGetDataResponse

**Package:** `flytekit.models.execution`

Currently, node, task, and workflow execution all have the same get data response. So we'll create this common
superclass to reduce code duplication until things diverge in the future.


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


## Properties

| Property | Type | Description |
|-|-|-|
| `dynamic_workflow` |  |  |
| `full_inputs` |  | {{< multiline >}}:rtype: _literals_models.LiteralMap
{{< /multiline >}} |
| `full_outputs` |  | {{< multiline >}}:rtype: _literals_models.LiteralMap
{{< /multiline >}} |
| `inputs` |  | {{< multiline >}}:rtype: _common_models.UrlBlob
{{< /multiline >}} |
| `is_empty` |  |  |
| `outputs` |  | {{< multiline >}}:rtype: _common_models.UrlBlob
{{< /multiline >}} |

