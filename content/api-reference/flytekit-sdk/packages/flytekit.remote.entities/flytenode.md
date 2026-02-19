---
title: FlyteNode
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteNode

**Package:** `flytekit.remote.entities`

A class encapsulating a remote Flyte node.


```python
class FlyteNode(
    id,
    upstream_nodes,
    bindings,
    metadata,
    task_node: Optional[FlyteTaskNode],
    workflow_node: Optional[FlyteWorkflowNode],
    branch_node: Optional[FlyteBranchNode],
    gate_node: Optional[FlyteGateNode],
    array_node: Optional[FlyteArrayNode],
)
```
| Parameter | Type | Description |
|-|-|-|
| `id` |  | |
| `upstream_nodes` |  | |
| `bindings` |  | |
| `metadata` |  | |
| `task_node` | `Optional[FlyteTaskNode]` | |
| `workflow_node` | `Optional[FlyteWorkflowNode]` | |
| `branch_node` | `Optional[FlyteBranchNode]` | |
| `gate_node` | `Optional[FlyteGateNode]` | |
| `array_node` | `Optional[FlyteArrayNode]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `array_node` | `None` |  |
| `branch_node` | `None` | [Optional] Information about the branch node to evaluate in this node.  :rtype: BranchNode |
| `flyte_entity` | `None` |  |
| `gate_node` | `None` |  |
| `id` | `None` | A workflow-level unique identifier that identifies this node in the workflow. "inputs" and "outputs" are reserved node ids that cannot be used by other nodes.  :rtype: Text |
| `inputs` | `None` | Specifies how to bind the underlying interface's inputs.  All required inputs specified in the underlying interface must be fulfilled.  :rtype: list[flytekit.models.literals.Binding] |
| `is_empty` | `None` |  |
| `metadata` | `None` | Extra metadata about the node.  :rtype: NodeMetadata |
| `output_aliases` | `None` | [Optional] A node can define aliases for a subset of its outputs. This is particularly useful if different nodes need to conform to the same interface (e.g. all branches in a branch node). Downstream nodes must refer to this node's outputs using the alias if one is specified.  :rtype: list[Alias] |
| `target` | `None` | :rtype: T |
| `task_node` | `None` | [Optional] Information about the Task to execute in this node.  :rtype: TaskNode |
| `upstream_node_ids` | `None` | [Optional] Specifies execution dependency for this node ensuring it will only get scheduled to run after all its upstream nodes have completed. This node will have an implicit dependency on any node that appears in inputs field.  :rtype: list[Text] |
| `upstream_nodes` | `None` |  |
| `workflow_node` | `None` | [Optional] Information about the Workflow to execute in this mode.  :rtype: WorkflowNode |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) |  |
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

### promote_from_model()

```python
def promote_from_model(
    model: _workflow_model.Node,
    sub_workflows: Optional[Dict[id_models.Identifier, _workflow_model.WorkflowTemplate]],
    node_launch_plans: Optional[Dict[id_models.Identifier, _launch_plan_model.LaunchPlanSpec]],
    tasks: Dict[id_models.Identifier, FlyteTask],
    converted_sub_workflows: Dict[id_models.Identifier, FlyteWorkflow],
) -> Tuple[Optional[FlyteNode], Dict[id_models.Identifier, FlyteWorkflow]]
```
| Parameter | Type | Description |
|-|-|-|
| `model` | `_workflow_model.Node` | |
| `sub_workflows` | `Optional[Dict[id_models.Identifier, _workflow_model.WorkflowTemplate]]` | |
| `node_launch_plans` | `Optional[Dict[id_models.Identifier, _launch_plan_model.LaunchPlanSpec]]` | |
| `tasks` | `Dict[id_models.Identifier, FlyteTask]` | |
| `converted_sub_workflows` | `Dict[id_models.Identifier, FlyteWorkflow]` | |

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


