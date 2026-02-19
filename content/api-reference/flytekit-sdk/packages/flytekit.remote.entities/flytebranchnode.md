---
title: FlyteBranchNode
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteBranchNode

**Package:** `flytekit.remote.entities`

```python
class FlyteBranchNode(
    if_else: _workflow_model.IfElseBlock,
)
```
BranchNode is a special node that alter the flow of the workflow graph. It allows the control flow to branch at
runtime based on a series of conditions that get evaluated on various parameters (e.g. inputs, primitives).



| Parameter | Type | Description |
|-|-|-|
| `if_else` | `_workflow_model.IfElseBlock` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `if_else` | `None` | :rtype: IfElseBlock |
| `is_empty` | `None` |  |

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
    pb2_objct,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_objct` |  | |

### promote_from_model()

```python
def promote_from_model(
    base_model: _workflow_model.BranchNode,
    sub_workflows: Dict[id_models.Identifier, _workflow_model.WorkflowTemplate],
    node_launch_plans: Dict[id_models.Identifier, _launch_plan_model.LaunchPlanSpec],
    tasks: Dict[id_models.Identifier, FlyteTask],
    converted_sub_workflows: Dict[id_models.Identifier, FlyteWorkflow],
) -> Tuple[FlyteBranchNode, Dict[id_models.Identifier, FlyteWorkflow]]
```
| Parameter | Type | Description |
|-|-|-|
| `base_model` | `_workflow_model.BranchNode` | |
| `sub_workflows` | `Dict[id_models.Identifier, _workflow_model.WorkflowTemplate]` | |
| `node_launch_plans` | `Dict[id_models.Identifier, _launch_plan_model.LaunchPlanSpec]` | |
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
:rtype: flyteidl.core.workflow_pb2.BranchNode


