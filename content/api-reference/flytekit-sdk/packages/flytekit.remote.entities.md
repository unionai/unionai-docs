---
title: flytekit.remote.entities
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
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
| `flyte_node` | `None` |  |
| `is_empty` | `None` |  |
| `node` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.remote.entities.FlyteBranchNode

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
| `if_else` | `None` | :rtype: IfElseBlock |
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.workflow_pb2.BranchNode


## flytekit.remote.entities.FlyteGateNode

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
| `approve` | `None` |  |
| `condition` | `None` |  |
| `is_empty` | `None` |  |
| `signal` | `None` |  |
| `sleep` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.remote.entities.FlyteLaunchPlan

A class encapsulating a remote Flyte launch plan.


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
| `annotations` | `None` | The annotations to execute the workflow with :rtype: flytekit.models.common.Annotations |
| `auth_role` | `None` | The authorization method with which to execute the workflow. :rtype: flytekit.models.common.AuthRole |
| `concurrency_policy` | `None` | Concurrency settings for the launch plan. :rtype: flytekit.models.concurrency.ConcurrencyPolicy |
| `default_inputs` | `None` | Input values to be passed for the execution :rtype: flytekit.models.interface.ParameterMap |
| `entity_metadata` | `None` | :rtype: LaunchPlanMetadata |
| `entity_type_text` | `None` |  |
| `fixed_inputs` | `None` | Fixed, non-overridable inputs for the Launch Plan :rtype: flytekit.models.literals.LiteralMap |
| `flyte_workflow` | `None` |  |
| `id` | `None` |  |
| `interface` | `None` | The interface is not technically part of the admin.LaunchPlanSpec in the IDL, however the workflow ID is, and from the workflow ID, fetch will fill in the interface. This is nice because then you can __call__ the= object and get a node. |
| `is_empty` | `None` |  |
| `is_scheduled` | `None` |  |
| `labels` | `None` | The labels to execute the workflow with :rtype: flytekit.models.common.Labels |
| `max_parallelism` | `None` |  |
| `name` | `None` |  |
| `overwrite_cache` | `None` |  |
| `python_interface` | `None` |  |
| `raw_output_data_config` | `None` | Where to store offloaded data like Blobs and Schemas :rtype: flytekit.models.common.RawOutputDataConfig |
| `resource_type` | `None` |  |
| `security_context` | `None` |  |
| `workflow_id` | `None` | Unique identifier for the workflow in question :rtype: flytekit.models.core.identifier.Identifier |

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
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.launch_plan_pb2.LaunchPlanSpec


## flytekit.remote.entities.FlyteNode

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

### Properties

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

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.workflow_pb2.Node


## flytekit.remote.entities.FlyteTask

A class encapsulating a remote Flyte task.


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
| `config` | `None` | Arbitrary dictionary containing metadata for parsing and handling custom plugins.  :rtype: dict[Text, T] |
| `container` | `None` | If not None, the target of execution should be a container.  :rtype: Container |
| `custom` | `None` | Arbitrary dictionary containing metadata for custom plugins.  :rtype: dict[Text, T] |
| `docs` | `None` | :rtype: Description entity for the task |
| `entity_type_text` | `None` |  |
| `extended_resources` | `None` |  |
| `id` | `None` | This is generated by the system and uniquely identifies the task.  :rtype: flytekit.models.core.identifier.Identifier |
| `interface` | `None` | The interface definition for this task.  :rtype: flytekit.models.interface.TypedInterface |
| `is_empty` | `None` |  |
| `k8s_pod` | `None` |  |
| `metadata` | `None` | This contains information needed at runtime to determine behavior such as whether or not outputs are discoverable, timeouts, and retries.  :rtype: TaskMetadata |
| `name` | `None` |  |
| `python_interface` | `None` |  |
| `resource_type` | `None` |  |
| `security_context` | `None` |  |
| `should_register` | `None` |  |
| `sql` | `None` |  |
| `task_type_version` | `None` |  |
| `template` | `None` | :rtype: TaskTemplate |
| `type` | `None` | This is used to identify additional extensions for use by Propeller or SDK.  :rtype: Text |

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
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.tasks_pb2.TaskSpec


## flytekit.remote.entities.FlyteTaskNode

A class encapsulating a task that a Flyte node needs to execute.


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
| `flyte_task` | `None` |  |
| `is_empty` | `None` |  |
| `overrides` | `None` |  |
| `reference_id` | `None` | A globally unique identifier for the task. |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) | Takes the idl wrapper for a TaskNode,. |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.workflow_pb2.TaskNode


## flytekit.remote.entities.FlyteWorkflow

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

### Properties

| Property | Type | Description |
|-|-|-|
| `docs` | `None` | :rtype: Description entity for the workflow |
| `entity_type_text` | `None` |  |
| `failure_node` | `None` | Node failure_node: A catch-all node. This node is executed whenever the execution engine determines the workflow has failed. The interface of this node must match the Workflow interface with an additional input named "error" of type pb.lyft.flyte.core.Error. |
| `flyte_nodes` | `None` |  |
| `flyte_sub_workflows` | `None` |  |
| `flyte_tasks` | `None` |  |
| `id` | `None` | This is an autogenerated id by the system. The id is globally unique across Flyte. |
| `interface` | `None` | Defines a strongly typed interface for the Workflow (inputs, outputs). This can include some optional parameters. |
| `is_empty` | `None` |  |
| `metadata` | `None` | This contains information on how to run the workflow. |
| `metadata_defaults` | `None` | This contains information on how to run the workflow. :rtype: WorkflowMetadataDefaults |
| `name` | `None` |  |
| `nodes` | `None` | A list of nodes. In addition, "globals" is a special reserved node id that can be used to consume workflow inputs |
| `outputs` | `None` | A list of output bindings that specify how to construct workflow outputs. Bindings can pull node outputs or specify literals. All workflow outputs specified in the interface field must be bound in order for the workflow to be validated. A workflow has an implicit dependency on all of its nodes to execute successfully in order to bind final outputs. |
| `python_interface` | `None` |  |
| `resource_type` | `None` |  |
| `should_register` | `None` |  |
| `sub_workflows` | `None` | :rtype: list[flytekit.models.core.workflow.WorkflowTemplate] |
| `template` | `None` | :rtype: flytekit.models.core.workflow.WorkflowTemplate |

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
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


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
| `pb2_object` |  | flyteidl.admin.workflow_pb2.WorkflowSpec :rtype: WorkflowSpec |

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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.workflow_pb2.WorkflowSpec


## flytekit.remote.entities.FlyteWorkflowNode

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

### Properties

| Property | Type | Description |
|-|-|-|
| `flyte_launch_plan` | `None` |  |
| `flyte_workflow` | `None` |  |
| `is_empty` | `None` |  |
| `launchplan_ref` | `None` | A globally unique identifier for the launch plan, which should map to Admin. |
| `reference` | `None` | :rtype: flytekit.models.core.identifier.Identifier |
| `sub_workflow_ref` | `None` | [Optional] Reference to a subworkflow, that should be defined with the compiler context.  :rtype: flytekit.models.core.identifier.Identifier |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.workflow_pb2.WorkflowNode


