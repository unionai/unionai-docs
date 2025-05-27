---
title: flytekit.remote.entities
version: 0.1.dev2192+g7c539c3.d20250403
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


| Parameter | Type |
|-|-|
| `flyte_node` | `FlyteNode` |
| `parallelism` | `int` |
| `min_successes` | `int` |
| `min_success_ratio` | `float` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> ArrayNode
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### promote_from_model()

```python
def promote_from_model(
    model: _workflow_model.ArrayNode,
    flyte_node: FlyteNode,
) -> FlyteArrayNode
```
| Parameter | Type |
|-|-|
| `model` | `_workflow_model.ArrayNode` |
| `flyte_node` | `FlyteNode` |

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
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `flyte_node` |  |  |
| `is_empty` |  |  |
| `node` |  |  |

## flytekit.remote.entities.FlyteBranchNode

```python
class FlyteBranchNode(
    if_else: _workflow_model.IfElseBlock,
)
```
BranchNode is a special node that alter the flow of the workflow graph. It allows the control flow to branch at
runtime based on a series of conditions that get evaluated on various parameters (e.g. inputs, primitives).



| Parameter | Type |
|-|-|
| `if_else` | `_workflow_model.IfElseBlock` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_objct,
)
```
| Parameter | Type |
|-|-|
| `pb2_objct` |  |

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
| Parameter | Type |
|-|-|
| `base_model` | `_workflow_model.BranchNode` |
| `sub_workflows` | `Dict[id_models.Identifier, _workflow_model.WorkflowTemplate]` |
| `node_launch_plans` | `Dict[id_models.Identifier, _launch_plan_model.LaunchPlanSpec]` |
| `tasks` | `Dict[id_models.Identifier, FlyteTask]` |
| `converted_sub_workflows` | `Dict[id_models.Identifier, FlyteWorkflow]` |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `if_else` |  | {{< multiline >}}:rtype: IfElseBlock
{{< /multiline >}} |
| `is_empty` |  |  |

## flytekit.remote.entities.FlyteGateNode

```python
class FlyteGateNode(
    signal: typing.Optional[flytekit.models.core.workflow.SignalCondition],
    sleep: typing.Optional[flytekit.models.core.workflow.SleepCondition],
    approve: typing.Optional[flytekit.models.core.workflow.ApproveCondition],
)
```
| Parameter | Type |
|-|-|
| `signal` | `typing.Optional[flytekit.models.core.workflow.SignalCondition]` |
| `sleep` | `typing.Optional[flytekit.models.core.workflow.SleepCondition]` |
| `approve` | `typing.Optional[flytekit.models.core.workflow.ApproveCondition]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.workflow_pb2.GateNode,
) -> GateNode
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.workflow_pb2.GateNode` |

#### promote_from_model()

```python
def promote_from_model(
    model: _workflow_model.GateNode,
)
```
| Parameter | Type |
|-|-|
| `model` | `_workflow_model.GateNode` |

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
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `approve` |  |  |
| `condition` |  |  |
| `is_empty` |  |  |
| `signal` |  |  |
| `sleep` |  |  |

## flytekit.remote.entities.FlyteLaunchPlan

A class encapsulating a remote Flyte launch plan.


```python
class FlyteLaunchPlan(
    id,
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `id` |  |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

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
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### compile()

```python
def compile(
    ctx: FlyteContext,
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

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
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2,
) -> e: LaunchPlanSpec
```
| Parameter | Type |
|-|-|
| `pb2` |  |

#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, NoneType]
```
| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `kwargs` | ``**kwargs`` |

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
| Parameter | Type |
|-|-|
| `id` | `id_models.Identifier` |
| `model` | `_launch_plan_models.LaunchPlanSpec` |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `annotations` |  | {{< multiline >}}The annotations to execute the workflow with
:rtype: flytekit.models.common.Annotations
{{< /multiline >}} |
| `auth_role` |  | {{< multiline >}}The authorization method with which to execute the workflow.
:rtype: flytekit.models.common.AuthRole
{{< /multiline >}} |
| `default_inputs` |  | {{< multiline >}}Input values to be passed for the execution
:rtype: flytekit.models.interface.ParameterMap
{{< /multiline >}} |
| `entity_metadata` |  | {{< multiline >}}:rtype: LaunchPlanMetadata
{{< /multiline >}} |
| `entity_type_text` |  |  |
| `fixed_inputs` |  | {{< multiline >}}Fixed, non-overridable inputs for the Launch Plan
:rtype: flytekit.models.literals.LiteralMap
{{< /multiline >}} |
| `flyte_workflow` |  |  |
| `id` |  |  |
| `interface` |  | {{< multiline >}}The interface is not technically part of the admin.LaunchPlanSpec in the IDL, however the workflow ID is, and
from the workflow ID, fetch will fill in the interface. This is nice because then you can __call__ the=
object and get a node.
{{< /multiline >}} |
| `is_empty` |  |  |
| `is_scheduled` |  |  |
| `labels` |  | {{< multiline >}}The labels to execute the workflow with
:rtype: flytekit.models.common.Labels
{{< /multiline >}} |
| `max_parallelism` |  |  |
| `name` |  |  |
| `overwrite_cache` |  |  |
| `python_interface` |  |  |
| `raw_output_data_config` |  | {{< multiline >}}Where to store offloaded data like Blobs and Schemas
:rtype: flytekit.models.common.RawOutputDataConfig
{{< /multiline >}} |
| `resource_type` |  |  |
| `security_context` |  |  |
| `workflow_id` |  | {{< multiline >}}Unique identifier for the workflow in question
:rtype: flytekit.models.core.identifier.Identifier
{{< /multiline >}} |

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
| Parameter | Type |
|-|-|
| `id` |  |
| `upstream_nodes` |  |
| `bindings` |  |
| `metadata` |  |
| `task_node` | `Optional[FlyteTaskNode]` |
| `workflow_node` | `Optional[FlyteWorkflowNode]` |
| `branch_node` | `Optional[FlyteBranchNode]` |
| `gate_node` | `Optional[FlyteGateNode]` |
| `array_node` | `Optional[FlyteArrayNode]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: Node
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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
| Parameter | Type |
|-|-|
| `model` | `_workflow_model.Node` |
| `sub_workflows` | `Optional[Dict[id_models.Identifier, _workflow_model.WorkflowTemplate]]` |
| `node_launch_plans` | `Optional[Dict[id_models.Identifier, _launch_plan_model.LaunchPlanSpec]]` |
| `tasks` | `Dict[id_models.Identifier, FlyteTask]` |
| `converted_sub_workflows` | `Dict[id_models.Identifier, FlyteWorkflow]` |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `array_node` |  |  |
| `branch_node` |  | {{< multiline >}}[Optional] Information about the branch node to evaluate in this node.

:rtype: BranchNode
{{< /multiline >}} |
| `flyte_entity` |  |  |
| `gate_node` |  |  |
| `id` |  | {{< multiline >}}A workflow-level unique identifier that identifies this node in the workflow. "inputs" and
"outputs" are reserved node ids that cannot be used by other nodes.

:rtype: Text
{{< /multiline >}} |
| `inputs` |  | {{< multiline >}}Specifies how to bind the underlying interface's inputs.  All required inputs specified
in the underlying interface must be fulfilled.

:rtype: list[flytekit.models.literals.Binding]
{{< /multiline >}} |
| `is_empty` |  |  |
| `metadata` |  | {{< multiline >}}Extra metadata about the node.

:rtype: NodeMetadata
{{< /multiline >}} |
| `output_aliases` |  | {{< multiline >}}[Optional] A node can define aliases for a subset of its outputs. This
is particularly useful if different nodes need to conform to the same interface (e.g. all branches in
a branch node). Downstream nodes must refer to this node's outputs using the alias if one is specified.

:rtype: list[Alias]
{{< /multiline >}} |
| `target` |  | {{< multiline >}}:rtype: T
{{< /multiline >}} |
| `task_node` |  | {{< multiline >}}[Optional] Information about the Task to execute in this node.

:rtype: TaskNode
{{< /multiline >}} |
| `upstream_node_ids` |  | {{< multiline >}}[Optional] Specifies execution dependency for this node ensuring it will
only get scheduled to run after all its upstream nodes have completed. This node will have
an implicit dependency on any node that appears in inputs field.

:rtype: list[Text]
{{< /multiline >}} |
| `upstream_nodes` |  |  |
| `workflow_node` |  | {{< multiline >}}[Optional] Information about the Workflow to execute in this mode.

:rtype: WorkflowNode
{{< /multiline >}} |

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
| Parameter | Type |
|-|-|
| `id` |  |
| `type` |  |
| `metadata` |  |
| `interface` |  |
| `custom` |  |
| `container` |  |
| `task_type_version` | `int` |
| `security_context` |  |
| `config` |  |
| `k8s_pod` |  |
| `sql` |  |
| `extended_resources` |  |
| `should_register` | `bool` |

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
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### compile()

```python
def compile(
    ctx: flytekit.core.context_manager.FlyteContext,
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

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
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: TaskSpec
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, NoneType]
```
| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `kwargs` | ``**kwargs`` |

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
| Parameter | Type |
|-|-|
| `base_model` | `_task_model.TaskTemplate` |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `config` |  | {{< multiline >}}Arbitrary dictionary containing metadata for parsing and handling custom plugins.

:rtype: dict[Text, T]
{{< /multiline >}} |
| `container` |  | {{< multiline >}}If not None, the target of execution should be a container.

:rtype: Container
{{< /multiline >}} |
| `custom` |  | {{< multiline >}}Arbitrary dictionary containing metadata for custom plugins.

:rtype: dict[Text, T]
{{< /multiline >}} |
| `docs` |  | {{< multiline >}}:rtype: Description entity for the task
{{< /multiline >}} |
| `entity_type_text` |  |  |
| `extended_resources` |  |  |
| `id` |  | {{< multiline >}}This is generated by the system and uniquely identifies the task.

:rtype: flytekit.models.core.identifier.Identifier
{{< /multiline >}} |
| `interface` |  | {{< multiline >}}The interface definition for this task.

:rtype: flytekit.models.interface.TypedInterface
{{< /multiline >}} |
| `is_empty` |  |  |
| `k8s_pod` |  |  |
| `metadata` |  | {{< multiline >}}This contains information needed at runtime to determine behavior such as whether or not outputs are
discoverable, timeouts, and retries.

:rtype: TaskMetadata
{{< /multiline >}} |
| `name` |  |  |
| `python_interface` |  |  |
| `resource_type` |  |  |
| `security_context` |  |  |
| `should_register` |  |  |
| `sql` |  |  |
| `task_type_version` |  |  |
| `template` |  | {{< multiline >}}:rtype: TaskTemplate
{{< /multiline >}} |
| `type` |  | {{< multiline >}}This is used to identify additional extensions for use by Propeller or SDK.

:rtype: Text
{{< /multiline >}} |

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



| Parameter | Type |
|-|-|
| `flyte_task` | `FlyteTask` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) | Takes the idl wrapper for a TaskNode,. |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: TaskNode
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### promote_from_model()

```python
def promote_from_model(
    task: FlyteTask,
) -> FlyteTaskNode
```
Takes the idl wrapper for a TaskNode,
and returns the hydrated Flytekit object for it by fetching it with the FlyteTask control plane.


| Parameter | Type |
|-|-|
| `task` | `FlyteTask` |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `flyte_task` |  |  |
| `is_empty` |  |  |
| `overrides` |  |  |
| `reference_id` |  | {{< multiline >}}A globally unique identifier for the task.
{{< /multiline >}} |

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
| Parameter | Type |
|-|-|
| `id` | `id_models.Identifier` |
| `nodes` | `List[FlyteNode]` |
| `interface` |  |
| `output_bindings` |  |
| `metadata` |  |
| `metadata_defaults` |  |
| `subworkflows` | `Optional[List[FlyteWorkflow]]` |
| `tasks` | `Optional[List[FlyteTask]]` |
| `launch_plans` | `Optional[Dict[id_models.Identifier, launch_plan_models.LaunchPlanSpec]]` |
| `compiled_closure` | `Optional[compiler_models.CompiledWorkflowClosure]` |
| `should_register` | `bool` |

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
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### compile()

```python
def compile(
    ctx: flytekit.core.context_manager.FlyteContext,
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

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
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: WorkflowSpec
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### get_non_system_nodes()

```python
def get_non_system_nodes(
    nodes: List[_workflow_models.Node],
) -> List[_workflow_models.Node]
```
| Parameter | Type |
|-|-|
| `nodes` | `List[_workflow_models.Node]` |

#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, NoneType]
```
| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `kwargs` | ``**kwargs`` |

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



| Parameter | Type |
|-|-|
| `closure` | `compiler_models.CompiledWorkflowClosure` |
| `node_launch_plans` | `Optional[Dict[id_models, launch_plan_models.LaunchPlanSpec]]` |

#### promote_from_model()

```python
def promote_from_model(
    base_model: _workflow_models.WorkflowTemplate,
    sub_workflows: Optional[Dict[Identifier, _workflow_models.WorkflowTemplate]],
    tasks: Optional[Dict[Identifier, FlyteTask]],
    node_launch_plans: Optional[Dict[Identifier, launch_plan_models.LaunchPlanSpec]],
) -> FlyteWorkflow
```
| Parameter | Type |
|-|-|
| `base_model` | `_workflow_models.WorkflowTemplate` |
| `sub_workflows` | `Optional[Dict[Identifier, _workflow_models.WorkflowTemplate]]` |
| `tasks` | `Optional[Dict[Identifier, FlyteTask]]` |
| `node_launch_plans` | `Optional[Dict[Identifier, launch_plan_models.LaunchPlanSpec]]` |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

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

## flytekit.remote.entities.FlyteWorkflowNode

A class encapsulating a workflow that a Flyte node needs to execute.


```python
class FlyteWorkflowNode(
    flyte_workflow: FlyteWorkflow,
    flyte_launch_plan: FlyteLaunchPlan,
)
```
Refers to a the workflow the node is to execute. One of the references must be supplied.



| Parameter | Type |
|-|-|
| `flyte_workflow` | `FlyteWorkflow` |
| `flyte_launch_plan` | `FlyteLaunchPlan` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: WorkflowNode
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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
| Parameter | Type |
|-|-|
| `base_model` | `_workflow_model.WorkflowNode` |
| `sub_workflows` | `Dict[id_models.Identifier, _workflow_model.WorkflowTemplate]` |
| `node_launch_plans` | `Dict[id_models.Identifier, _launch_plan_model.LaunchPlanSpec]` |
| `tasks` | `Dict[Identifier, FlyteTask]` |
| `converted_sub_workflows` | `Dict[id_models.Identifier, FlyteWorkflow]` |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `flyte_launch_plan` |  |  |
| `flyte_workflow` |  |  |
| `is_empty` |  |  |
| `launchplan_ref` |  | {{< multiline >}}A globally unique identifier for the launch plan, which should map to Admin.
{{< /multiline >}} |
| `reference` |  | {{< multiline >}}:rtype: flytekit.models.core.identifier.Identifier
{{< /multiline >}} |
| `sub_workflow_ref` |  | {{< multiline >}}[Optional] Reference to a subworkflow, that should be defined with the compiler context.

:rtype: flytekit.models.core.identifier.Identifier
{{< /multiline >}} |

