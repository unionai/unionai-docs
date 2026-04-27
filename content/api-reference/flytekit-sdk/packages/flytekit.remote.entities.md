---
title: flytekit.remote.entities
version: 1.16.19
variants: +flyte +union
layout: py_api
---

# flytekit.remote.entities

This module contains shadow entities for all Flyte entities as represented in Flyte Admin / Control Plane.
The goal is to enable easy access, manipulation of these entities.
## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteArrayNode`](.././flytekit.remote.entities#flytekitremoteentitiesflytearraynode) |  |
| [`FlyteBranchNode`](.././flytekit.remote.entities#flytekitremoteentitiesflytebranchnode) |  |
| [`FlyteGateNode`](.././flytekit.remote.entities#flytekitremoteentitiesflytegatenode) |  |
| [`FlyteLaunchPlan`](.././flytekit.remote.entities#flytekitremoteentitiesflytelaunchplan) | A class encapsulating a remote Flyte launch plan. |
| [`FlyteNode`](.././flytekit.remote.entities#flytekitremoteentitiesflytenode) | A class encapsulating a remote Flyte node. |
| [`FlyteTask`](.././flytekit.remote.entities#flytekitremoteentitiesflytetask) | A class encapsulating a remote Flyte task. |
| [`FlyteTaskNode`](.././flytekit.remote.entities#flytekitremoteentitiesflytetasknode) | A class encapsulating a task that a Flyte node needs to execute. |
| [`FlyteWorkflow`](.././flytekit.remote.entities#flytekitremoteentitiesflyteworkflow) | A class encapsulating a remote Flyte workflow. |
| [`FlyteWorkflowNode`](.././flytekit.remote.entities#flytekitremoteentitiesflyteworkflownode) | A class encapsulating a workflow that a Flyte node needs to execute. |

## flytekit.remote.entities.FlyteArrayNode

### Parameters

```python
class FlyteArrayNode(
    flyte_node: FlyteNode,
    parallelism: int,
    min_successes: int,
    min_success_ratio: float,
)
```
TODO: docstring


| Parameter | Type | Description |
|-|-|-|
| `flyte_node` | `FlyteNode` | |
| `parallelism` | `int` | |
| `min_successes` | `int` | |
| `min_success_ratio` | `float` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `flyte_node` | `FlyteNode` |  |
| `is_empty` | `None` |  |
| `node` | `Node` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> ArrayNode
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### promote_from_model()

```python
def promote_from_model(
    model: _workflow_model.ArrayNode,
    flyte_node: FlyteNode,
) -> FlyteArrayNode
```
| Parameter | Type | Description |
|-|-|-|
| `model` | `_workflow_model.ArrayNode` | |
| `flyte_node` | `FlyteNode` | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.remote.entities.FlyteBranchNode

### Parameters

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

### Properties

| Property | Type | Description |
|-|-|-|
| `if_else` | `flytekit.models.core.workflow.IfElseBlock` |  |
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_objct,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_objct` |  | |

#### promote_from_model()

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

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.workflow_pb2.BranchNode

## flytekit.remote.entities.FlyteGateNode

### Parameters

```python
class FlyteGateNode(
    signal: typing.Optional[flytekit.models.core.workflow.SignalCondition],
    sleep: typing.Optional[flytekit.models.core.workflow.SleepCondition],
    approve: typing.Optional[flytekit.models.core.workflow.ApproveCondition],
)
```
| Parameter | Type | Description |
|-|-|-|
| `signal` | `typing.Optional[flytekit.models.core.workflow.SignalCondition]` | |
| `sleep` | `typing.Optional[flytekit.models.core.workflow.SleepCondition]` | |
| `approve` | `typing.Optional[flytekit.models.core.workflow.ApproveCondition]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `approve` | `typing.Optional[flytekit.models.core.workflow.ApproveCondition]` |  |
| `condition` | `typing.Union[flytekit.models.core.workflow.SignalCondition, flytekit.models.core.workflow.SleepCondition, flytekit.models.core.workflow.ApproveCondition]` |  |
| `is_empty` | `None` |  |
| `signal` | `typing.Optional[flytekit.models.core.workflow.SignalCondition]` |  |
| `sleep` | `typing.Optional[flytekit.models.core.workflow.SignalCondition]` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.workflow_pb2.GateNode,
) -> GateNode
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.workflow_pb2.GateNode` | |

#### promote_from_model()

```python
def promote_from_model(
    model: _workflow_model.GateNode,
)
```
| Parameter | Type | Description |
|-|-|-|
| `model` | `_workflow_model.GateNode` | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.remote.entities.FlyteLaunchPlan

A class encapsulating a remote Flyte launch plan.


### Parameters

```python
class FlyteLaunchPlan(
    id,
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `id` |  | |
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `annotations` | `flytekit.models.common.Annotations` | The annotations to execute the workflow with |
| `auth_role` | `None` | The authorization method with which to execute the workflow. |
| `concurrency_policy` | `typing.Optional[flytekit.models.concurrency.ConcurrencyPolicy]` | Concurrency settings for the launch plan. |
| `default_inputs` | `None` | Input values to be passed for the execution |
| `entity_metadata` | `None` |  |
| `entity_type_text` | `str` |  |
| `fixed_inputs` | `None` | Fixed, non-overridable inputs for the Launch Plan |
| `flyte_workflow` | `Optional[FlyteWorkflow]` |  |
| `id` | `id_models.Identifier` |  |
| `interface` | `Optional[_interface.TypedInterface]` | The interface is not technically part of the admin.LaunchPlanSpec in the IDL, however the workflow ID is, and from the workflow ID, fetch will fill in the interface. This is nice because then you can __call__ the= object and get a node. |
| `is_empty` | `None` |  |
| `is_scheduled` | `bool` |  |
| `labels` | `flytekit.models.common.Labels` | The labels to execute the workflow with |
| `max_parallelism` | `typing.Optional[int]` |  |
| `name` | `str` |  |
| `overwrite_cache` | `typing.Optional[bool]` |  |
| `python_interface` | `typing.Optional[ForwardRef('Interface')]` |  |
| `raw_output_data_config` | `None` | Where to store offloaded data like Blobs and Schemas |
| `resource_type` | `id_models.ResourceType` |  |
| `security_context` | `typing.Optional[flytekit.models.security.SecurityContext]` |  |
| `workflow_id` | `id_models.Identifier` | Unique identifier for the workflow in question |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition. |
| [`execute()`](#execute) |  |
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### compile()

```python
def compile(
    ctx: FlyteContext,
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
Used when constructing the node that encapsulates this task as part of a broader workflow definition.


#### execute()

```python
def execute(
    kwargs,
) -> typing.Any
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` |  | |

**Returns:** LaunchPlanSpec

#### local_execute()

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

#### local_execution_mode()

```python
def local_execution_mode()
```
#### promote_from_model()

```python
def promote_from_model(
    id: id_models.Identifier,
    model: _launch_plan_models.LaunchPlanSpec,
) -> FlyteLaunchPlan
```
| Parameter | Type | Description |
|-|-|-|
| `id` | `id_models.Identifier` | |
| `model` | `_launch_plan_models.LaunchPlanSpec` | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.admin.launch_plan_pb2.LaunchPlanSpec

## flytekit.remote.entities.FlyteNode

A class encapsulating a remote Flyte node.


### Parameters

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

### Properties

| Property | Type | Description |
|-|-|-|
| `array_node` | `typing.Optional[flytekit.models.core.workflow.ArrayNode]` |  |
| `branch_node` | `None` | [Optional] Information about the branch node to evaluate in this node. |
| `flyte_entity` | `Union[FlyteTask, FlyteWorkflow, FlyteLaunchPlan, FlyteBranchNode, FlyteArrayNode]` |  |
| `gate_node` | `typing.Optional[flytekit.models.core.workflow.GateNode]` |  |
| `id` | `None` | A workflow-level unique identifier that identifies this node in the workflow. "inputs" and "outputs" are reserved node ids that cannot be used by other nodes. |
| `inputs` | `None` | Specifies how to bind the underlying interface's inputs.  All required inputs specified in the underlying interface must be fulfilled. |
| `is_empty` | `None` |  |
| `metadata` | `None` | Extra metadata about the node. |
| `output_aliases` | `None` | [Optional] A node can define aliases for a subset of its outputs. This is particularly useful if different nodes need to conform to the same interface (e.g. all branches in a branch node). Downstream nodes must refer to this node's outputs using the alias if one is specified. |
| `target` | `None` |  |
| `task_node` | `Optional[FlyteTaskNode]` | [Optional] Information about the Task to execute in this node. |
| `upstream_node_ids` | `List[str]` | [Optional] Specifies execution dependency for this node ensuring it will only get scheduled to run after all its upstream nodes have completed. This node will have an implicit dependency on any node that appears in inputs field. |
| `upstream_nodes` | `List[FlyteNode]` |  |
| `workflow_node` | `None` | [Optional] Information about the Workflow to execute in this mode. |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** Node

#### promote_from_model()

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

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.workflow_pb2.Node

## flytekit.remote.entities.FlyteTask

A class encapsulating a remote Flyte task.


### Parameters

```python
class FlyteTask(
    id,
    type,
    metadata,
    interface,
    custom,
    container,
    task_type_version: int,
    security_context,
    config,
    k8s_pod,
    sql,
    extended_resources,
    should_register: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `id` |  | |
| `type` |  | |
| `metadata` |  | |
| `interface` |  | |
| `custom` |  | |
| `container` |  | |
| `task_type_version` | `int` | |
| `security_context` |  | |
| `config` |  | |
| `k8s_pod` |  | |
| `sql` |  | |
| `extended_resources` |  | |
| `should_register` | `bool` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `config` | `None` | Arbitrary dictionary containing metadata for parsing and handling custom plugins. |
| `container` | `None` | If not None, the target of execution should be a container. |
| `custom` | `None` | Arbitrary dictionary containing metadata for custom plugins. |
| `docs` | `None` |  |
| `entity_type_text` | `str` |  |
| `extended_resources` | `None` |  |
| `id` | `None` | This is generated by the system and uniquely identifies the task. |
| `interface` | `None` | The interface definition for this task. |
| `is_empty` | `None` |  |
| `k8s_pod` | `None` |  |
| `metadata` | `None` | This contains information needed at runtime to determine behavior such as whether or not outputs are discoverable, timeouts, and retries. |
| `name` | `str` |  |
| `python_interface` | `typing.Optional[ForwardRef('Interface')]` |  |
| `resource_type` | `_identifier_model.ResourceType` |  |
| `security_context` | `None` |  |
| `should_register` | `bool` |  |
| `sql` | `None` |  |
| `task_type_version` | `None` |  |
| `template` | `None` |  |
| `type` | `None` | This is used to identify additional extensions for use by Propeller or SDK. |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition. |
| [`execute()`](#execute) |  |
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### compile()

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

#### construct_node_metadata()

```python
def construct_node_metadata()
```
Used when constructing the node that encapsulates this task as part of a broader workflow definition.


#### execute()

```python
def execute(
    kwargs,
) -> typing.Any
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** TaskSpec

#### local_execute()

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

#### local_execution_mode()

```python
def local_execution_mode()
```
#### promote_from_model()

```python
def promote_from_model(
    base_model: _task_model.TaskTemplate,
) -> FlyteTask
```
| Parameter | Type | Description |
|-|-|-|
| `base_model` | `_task_model.TaskTemplate` | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.admin.tasks_pb2.TaskSpec

## flytekit.remote.entities.FlyteTaskNode

A class encapsulating a task that a Flyte node needs to execute.


### Parameters

```python
class FlyteTaskNode(
    flyte_task: FlyteTask,
)
```
Refers to the task that the Node is to execute.
This is currently a oneof in protobuf, but there's only one option currently.
This code should be updated when more options are available.



| Parameter | Type | Description |
|-|-|-|
| `flyte_task` | `FlyteTask` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `flyte_task` | `FlyteTask` |  |
| `is_empty` | `None` |  |
| `overrides` | `flytekit.models.core.workflow.TaskNodeOverrides` |  |
| `reference_id` | `id_models.Identifier` | A globally unique identifier for the task. |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) | Takes the idl wrapper for a TaskNode,. |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** TaskNode

#### promote_from_model()

```python
def promote_from_model(
    task: FlyteTask,
) -> FlyteTaskNode
```
Takes the idl wrapper for a TaskNode,
and returns the hydrated Flytekit object for it by fetching it with the FlyteTask control plane.


| Parameter | Type | Description |
|-|-|-|
| `task` | `FlyteTask` | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.workflow_pb2.TaskNode

## flytekit.remote.entities.FlyteWorkflow

A class encapsulating a remote Flyte workflow.


### Parameters

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

### Properties

| Property | Type | Description |
|-|-|-|
| `docs` | `None` |  |
| `entity_type_text` | `str` |  |
| `failure_node` | `Node` | Node failure_node: A catch-all node. This node is executed whenever the execution engine determines the workflow has failed. The interface of this node must match the Workflow interface with an additional input named "error" of type pb.lyft.flyte.core.Error. |
| `flyte_nodes` | `List[FlyteNode]` |  |
| `flyte_sub_workflows` | `List[FlyteWorkflow]` |  |
| `flyte_tasks` | `Optional[List[FlyteTask]]` |  |
| `id` | `Identifier` | This is an autogenerated id by the system. The id is globally unique across Flyte. |
| `interface` | `TypedInterface` | Defines a strongly typed interface for the Workflow (inputs, outputs). This can include some optional parameters. |
| `is_empty` | `None` |  |
| `metadata` | `WorkflowMetadata` | This contains information on how to run the workflow. |
| `metadata_defaults` | `WorkflowMetadataDefaults` | This contains information on how to run the workflow. |
| `name` | `str` |  |
| `nodes` | `List[Node]` | A list of nodes. In addition, "globals" is a special reserved node id that can be used to consume workflow inputs |
| `outputs` | `List[Binding]` | A list of output bindings that specify how to construct workflow outputs. Bindings can pull node outputs or specify literals. All workflow outputs specified in the interface field must be bound in order for the workflow to be validated. A workflow has an implicit dependency on all of its nodes to execute successfully in order to bind final outputs. |
| `python_interface` | `typing.Optional[ForwardRef('Interface')]` |  |
| `resource_type` | `None` |  |
| `should_register` | `bool` |  |
| `sub_workflows` | `None` |  |
| `template` | `None` |  |

### Methods

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
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### compile()

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

#### construct_node_metadata()

```python
def construct_node_metadata()
```
Used when constructing the node that encapsulates this task as part of a broader workflow definition.


#### execute()

```python
def execute(
    kwargs,
) -> typing.Any
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | flyteidl.admin.workflow_pb2.WorkflowSpec |

**Returns:** WorkflowSpec

#### get_non_system_nodes()

```python
def get_non_system_nodes(
    nodes: List[_workflow_models.Node],
) -> List[_workflow_models.Node]
```
| Parameter | Type | Description |
|-|-|-|
| `nodes` | `List[_workflow_models.Node]` | |

#### local_execute()

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

#### local_execution_mode()

```python
def local_execution_mode()
```
#### promote_from_closure()

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

#### promote_from_model()

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

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.admin.workflow_pb2.WorkflowSpec

## flytekit.remote.entities.FlyteWorkflowNode

A class encapsulating a workflow that a Flyte node needs to execute.


### Parameters

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

### Properties

| Property | Type | Description |
|-|-|-|
| `flyte_launch_plan` | `FlyteLaunchPlan` |  |
| `flyte_workflow` | `FlyteWorkflow` |  |
| `is_empty` | `None` |  |
| `launchplan_ref` | `id_models.Identifier` | A globally unique identifier for the launch plan, which should map to Admin. |
| `reference` | `None` |  |
| `sub_workflow_ref` | `None` | [Optional] Reference to a subworkflow, that should be defined with the compiler context. |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** WorkflowNode

#### promote_from_model()

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

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.workflow_pb2.WorkflowNode

