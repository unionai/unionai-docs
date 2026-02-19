---
title: FlyteWorkflowNode
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteWorkflowNode

**Package:** `flytekit.remote.entities`

A class encapsulating a workflow that a Flyte node needs to execute.


```python
class FlyteWorkflowNode(
    flyte_workflow: FlyteWorkflow,
    flyte_launch_plan: FlyteLaunchPlan,
)
```
Refers to a the workflow the node is to execute. One of the references must be supplied.



| Parameter | Type | Description |
|-|-|-|
| `flyte_workflow` | `FlyteWorkflow` | |
| `flyte_launch_plan` | `FlyteLaunchPlan` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `flyte_launch_plan` | `None` |  |
| `flyte_workflow` | `None` |  |
| `is_empty` | `None` |  |
| `launchplan_ref` | `None` | A globally unique identifier for the launch plan, which should map to Admin. |
| `reference` | `None` | :rtype: flytekit.models.core.identifier.Identifier |
| `sub_workflow_ref` | `None` | [Optional] Reference to a subworkflow, that should be defined with the compiler context.  :rtype: flytekit.models.core.identifier.Identifier |

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
    base_model: _workflow_model.WorkflowNode,
    sub_workflows: Dict[id_models.Identifier, _workflow_model.WorkflowTemplate],
    node_launch_plans: Dict[id_models.Identifier, _launch_plan_model.LaunchPlanSpec],
    tasks: Dict[Identifier, FlyteTask],
    converted_sub_workflows: Dict[id_models.Identifier, FlyteWorkflow],
) -> Tuple[FlyteWorkflowNode, Dict[id_models.Identifier, FlyteWorkflow]]
```
| Parameter | Type | Description |
|-|-|-|
| `base_model` | `_workflow_model.WorkflowNode` | |
| `sub_workflows` | `Dict[id_models.Identifier, _workflow_model.WorkflowTemplate]` | |
| `node_launch_plans` | `Dict[id_models.Identifier, _launch_plan_model.LaunchPlanSpec]` | |
| `tasks` | `Dict[Identifier, FlyteTask]` | |
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
:rtype: flyteidl.core.workflow_pb2.WorkflowNode


