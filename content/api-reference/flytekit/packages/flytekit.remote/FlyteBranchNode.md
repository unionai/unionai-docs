---
title: FlyteBranchNode
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# FlyteBranchNode

**Package:** `flytekit.remote`

```python
def FlyteBranchNode(
    if_else: _workflow_model.IfElseBlock,
):
```
BranchNode is a special node that alter the flow of the workflow graph. It allows the control flow to branch at
runtime based on a series of conditions that get evaluated on various parameters (e.g. inputs, primitives).



| Parameter | Type |
|-|-|
| `if_else` | `_workflow_model.IfElseBlock` |
## Methods

### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_objct,
):
```
| Parameter | Type |
|-|-|
| `pb2_objct` |  |
### promote_from_model()

```python
def promote_from_model(
    base_model: _workflow_model.BranchNode,
    sub_workflows: Dict[id_models.Identifier, _workflow_model.WorkflowTemplate],
    node_launch_plans: Dict[id_models.Identifier, _launch_plan_model.LaunchPlanSpec],
    tasks: Dict[id_models.Identifier, FlyteTask],
    converted_sub_workflows: Dict[id_models.Identifier, FlyteWorkflow],
):
```
| Parameter | Type |
|-|-|
| `base_model` | `_workflow_model.BranchNode` |
| `sub_workflows` | `Dict[id_models.Identifier, _workflow_model.WorkflowTemplate]` |
| `node_launch_plans` | `Dict[id_models.Identifier, _launch_plan_model.LaunchPlanSpec]` |
| `tasks` | `Dict[id_models.Identifier, FlyteTask]` |
| `converted_sub_workflows` | `Dict[id_models.Identifier, FlyteWorkflow]` |
### serialize_to_string()

```python
def serialize_to_string()
```
No parameters
### short_string()

```python
def short_string()
```
No parameters
### to_flyte_idl()

```python
def to_flyte_idl()
```
No parameters
### verbose_string()

```python
def verbose_string()
```
No parameters
