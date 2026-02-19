---
title: Node
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Node

**Package:** `flytekit.models.core.workflow`

```python
class Node(
    id,
    metadata,
    inputs,
    upstream_node_ids,
    output_aliases,
    task_node,
    workflow_node,
    branch_node,
    gate_node: typing.Optional[flytekit.models.core.workflow.GateNode],
    array_node: typing.Optional[flytekit.models.core.workflow.ArrayNode],
)
```
A Workflow graph Node. One unit of execution in the graph. Each node can be linked to a Task,
a Workflow or a branch node.  One of the nodes must be specified.



| Parameter | Type | Description |
|-|-|-|
| `id` |  | |
| `metadata` |  | |
| `inputs` |  | |
| `upstream_node_ids` |  | |
| `output_aliases` |  | |
| `task_node` |  | |
| `workflow_node` |  | |
| `branch_node` |  | |
| `gate_node` | `typing.Optional[flytekit.models.core.workflow.GateNode]` | |
| `array_node` | `typing.Optional[flytekit.models.core.workflow.ArrayNode]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `array_node` | `None` |  |
| `branch_node` | `None` | [Optional] Information about the branch node to evaluate in this node.  :rtype: BranchNode |
| `gate_node` | `None` |  |
| `id` | `None` | A workflow-level unique identifier that identifies this node in the workflow. "inputs" and "outputs" are reserved node ids that cannot be used by other nodes.  :rtype: Text |
| `inputs` | `None` | Specifies how to bind the underlying interface's inputs.  All required inputs specified in the underlying interface must be fulfilled.  :rtype: list[flytekit.models.literals.Binding] |
| `is_empty` | `None` |  |
| `metadata` | `None` | Extra metadata about the node.  :rtype: NodeMetadata |
| `output_aliases` | `None` | [Optional] A node can define aliases for a subset of its outputs. This is particularly useful if different nodes need to conform to the same interface (e.g. all branches in a branch node). Downstream nodes must refer to this node's outputs using the alias if one is specified.  :rtype: list[Alias] |
| `target` | `None` | :rtype: T |
| `task_node` | `None` | [Optional] Information about the Task to execute in this node.  :rtype: TaskNode |
| `upstream_node_ids` | `None` | [Optional] Specifies execution dependency for this node ensuring it will only get scheduled to run after all its upstream nodes have completed. This node will have an implicit dependency on any node that appears in inputs field.  :rtype: list[Text] |
| `workflow_node` | `None` | [Optional] Information about the Workflow to execute in this mode.  :rtype: WorkflowNode |

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
:rtype: flyteidl.core.workflow_pb2.Node


