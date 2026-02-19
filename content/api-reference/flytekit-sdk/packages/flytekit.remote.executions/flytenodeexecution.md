---
title: FlyteNodeExecution
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteNodeExecution

**Package:** `flytekit.remote.executions`

A class encapsulating a node execution being run on a Flyte remote backend.


```python
class FlyteNodeExecution(
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `closure` | `None` | :rtype: NodeExecutionClosure |
| `error` | `None` | If execution is in progress, raise an exception. Otherwise, return None if no error was present upon reaching completion. |
| `executions` | `None` |  |
| `id` | `None` | :rtype: flytekit.models.core.identifier.NodeExecutionIdentifier |
| `input_uri` | `None` | :rtype: Text |
| `inputs` | `None` |  |
| `interface` | `None` | Return the interface of the task or subworkflow associated with this node execution. |
| `is_done` | `None` | Whether or not the execution is complete. |
| `is_empty` | `None` |  |
| `metadata` | `None` |  |
| `outputs` | `None` | :return: Returns the outputs LiteralsResolver to the execution :raises: ``FlyteAssertion`` error if execution is in progress or execution ended in error. |
| `subworkflow_node_executions` | `None` | This returns underlying node executions in instances where the current node execution is a parent node. This happens when it's either a static or dynamic subworkflow. |
| `task_executions` | `None` |  |
| `workflow_executions` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) |  |
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

### promote_from_model()

```python
def promote_from_model(
    base_model: node_execution_models.NodeExecution,
) -> 'FlyteNodeExecution'
```
| Parameter | Type | Description |
|-|-|-|
| `base_model` | `node_execution_models.NodeExecution` | |

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
