---
title: FlyteWorkflow
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteWorkflow

**Package:** `flytekit.remote.entities`

A class encapsulating a remote Flyte workflow.


```python
class FlyteWorkflow(
    id: id_models.Identifier,
    nodes: List[FlyteNode],
    interface,
    output_bindings,
    metadata,
    metadata_defaults,
    subworkflows: Optional[List[FlyteWorkflow]],
    tasks: Optional[List[FlyteTask]],
    launch_plans: Optional[Dict[id_models.Identifier, launch_plan_models.LaunchPlanSpec]],
    compiled_closure: Optional[compiler_models.CompiledWorkflowClosure],
    should_register: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `id` | `id_models.Identifier` | |
| `nodes` | `List[FlyteNode]` | |
| `interface` |  | |
| `output_bindings` |  | |
| `metadata` |  | |
| `metadata_defaults` |  | |
| `subworkflows` | `Optional[List[FlyteWorkflow]]` | |
| `tasks` | `Optional[List[FlyteTask]]` | |
| `launch_plans` | `Optional[Dict[id_models.Identifier, launch_plan_models.LaunchPlanSpec]]` | |
| `compiled_closure` | `Optional[compiler_models.CompiledWorkflowClosure]` | |
| `should_register` | `bool` | |

## Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition. |
| [`execute()`](#execute) |  |
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`get_non_system_nodes()`](#get_non_system_nodes) |  |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`promote_from_closure()`](#promote_from_closure) | Extracts out the relevant portions of a FlyteWorkflow from a closure from the control plane. |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


### compile()

```python
def compile(
    ctx: flytekit.core.context_manager.FlyteContext,
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### construct_node_metadata()

```python
def construct_node_metadata()
```
Used when constructing the node that encapsulates this task as part of a broader workflow definition.


### execute()

```python
def execute(
    kwargs,
) -> typing.Any
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | flyteidl.admin.workflow_pb2.WorkflowSpec :rtype: WorkflowSpec |

### get_non_system_nodes()

```python
def get_non_system_nodes(
    nodes: List[_workflow_models.Node],
) -> List[_workflow_models.Node]
```
| Parameter | Type | Description |
|-|-|-|
| `nodes` | `List[_workflow_models.Node]` | |

### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, NoneType]
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `kwargs` | `**kwargs` | |

### local_execution_mode()

```python
def local_execution_mode()
```
### promote_from_closure()

```python
def promote_from_closure(
    closure: compiler_models.CompiledWorkflowClosure,
    node_launch_plans: Optional[Dict[id_models, launch_plan_models.LaunchPlanSpec]],
)
```
Extracts out the relevant portions of a FlyteWorkflow from a closure from the control plane.



| Parameter | Type | Description |
|-|-|-|
| `closure` | `compiler_models.CompiledWorkflowClosure` | This is the closure returned by Admin |
| `node_launch_plans` | `Optional[Dict[id_models, launch_plan_models.LaunchPlanSpec]]` | The reason this exists is because the compiled closure doesn't have launch plans. It only has subworkflows and tasks. Why this is unclear. If supplied, this map of launch plans will be |

### promote_from_model()

```python
def promote_from_model(
    base_model: _workflow_models.WorkflowTemplate,
    sub_workflows: Optional[Dict[Identifier, _workflow_models.WorkflowTemplate]],
    tasks: Optional[Dict[Identifier, FlyteTask]],
    node_launch_plans: Optional[Dict[Identifier, launch_plan_models.LaunchPlanSpec]],
) -> FlyteWorkflow
```
| Parameter | Type | Description |
|-|-|-|
| `base_model` | `_workflow_models.WorkflowTemplate` | |
| `sub_workflows` | `Optional[Dict[Identifier, _workflow_models.WorkflowTemplate]]` | |
| `tasks` | `Optional[Dict[Identifier, FlyteTask]]` | |
| `node_launch_plans` | `Optional[Dict[Identifier, launch_plan_models.LaunchPlanSpec]]` | |

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
:rtype: flyteidl.admin.workflow_pb2.WorkflowSpec


## Properties

| Property | Type | Description |
|-|-|-|
| `docs` |  | {{< multiline >}}:rtype: Description entity for the workflow
{{< /multiline >}} |
| `entity_type_text` |  |  |
| `failure_node` |  | {{< multiline >}}Node failure_node: A catch-all node. This node is executed whenever the execution engine determines the
workflow has failed. The interface of this node must match the Workflow interface with an additional input
named "error" of type pb.lyft.flyte.core.Error.
{{< /multiline >}} |
| `flyte_nodes` |  |  |
| `flyte_sub_workflows` |  |  |
| `flyte_tasks` |  |  |
| `id` |  | {{< multiline >}}This is an autogenerated id by the system. The id is globally unique across Flyte.
{{< /multiline >}} |
| `interface` |  | {{< multiline >}}Defines a strongly typed interface for the Workflow (inputs, outputs). This can include some optional
parameters.
{{< /multiline >}} |
| `is_empty` |  |  |
| `metadata` |  | {{< multiline >}}This contains information on how to run the workflow.
{{< /multiline >}} |
| `metadata_defaults` |  | {{< multiline >}}This contains information on how to run the workflow.
:rtype: WorkflowMetadataDefaults
{{< /multiline >}} |
| `name` |  |  |
| `nodes` |  | {{< multiline >}}A list of nodes. In addition, "globals" is a special reserved node id that can be used to consume
workflow inputs
{{< /multiline >}} |
| `outputs` |  | {{< multiline >}}A list of output bindings that specify how to construct workflow outputs. Bindings can
pull node outputs or specify literals. All workflow outputs specified in the interface field must be bound
in order for the workflow to be validated. A workflow has an implicit dependency on all of its nodes
to execute successfully in order to bind final outputs.
{{< /multiline >}} |
| `python_interface` |  |  |
| `resource_type` |  |  |
| `should_register` |  |  |
| `sub_workflows` |  | {{< multiline >}}:rtype: list[flytekit.models.core.workflow.WorkflowTemplate]
{{< /multiline >}} |
| `template` |  | {{< multiline >}}:rtype: flytekit.models.core.workflow.WorkflowTemplate
{{< /multiline >}} |

