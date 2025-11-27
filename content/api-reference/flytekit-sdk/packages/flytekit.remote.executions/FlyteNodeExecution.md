---
title: FlyteNodeExecution
version: 1.16.10
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
## Properties

| Property | Type | Description |
|-|-|-|
| `closure` |  | {{< multiline >}}:rtype: NodeExecutionClosure
{{< /multiline >}} |
| `error` |  | {{< multiline >}}If execution is in progress, raise an exception. Otherwise, return None if no error was present upon
reaching completion.
{{< /multiline >}} |
| `executions` |  |  |
| `id` |  | {{< multiline >}}:rtype: flytekit.models.core.identifier.NodeExecutionIdentifier
{{< /multiline >}} |
| `input_uri` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `inputs` |  |  |
| `interface` |  | {{< multiline >}}Return the interface of the task or subworkflow associated with this node execution.
{{< /multiline >}} |
| `is_done` |  | {{< multiline >}}Whether or not the execution is complete.
{{< /multiline >}} |
| `is_empty` |  |  |
| `metadata` |  |  |
| `outputs` |  | {{< multiline >}}:return: Returns the outputs LiteralsResolver to the execution
:raises: ``FlyteAssertion`` error if execution is in progress or execution ended in error.
{{< /multiline >}} |
| `subworkflow_node_executions` |  | {{< multiline >}}This returns underlying node executions in instances where the current node execution is
a parent node. This happens when it's either a static or dynamic subworkflow.
{{< /multiline >}} |
| `task_executions` |  |  |
| `workflow_executions` |  |  |

