---
title: flytekit.remote.entities
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.remote.entities


This module contains shadow entities for all Flyte entities as represented in Flyte Admin / Control Plane.
The goal is to enable easy access, manipulation of these entities.

## Directory

### Classes

| Class | Description |
|-|-|
| [`Binding`](.././flytekit.remote.entities#flytekitremoteentitiesbinding) |  |
| [`FlyteArrayNode`](.././flytekit.remote.entities#flytekitremoteentitiesflytearraynode) |  |
| [`FlyteBranchNode`](.././flytekit.remote.entities#flytekitremoteentitiesflytebranchnode) |  |
| [`FlyteContext`](.././flytekit.remote.entities#flytekitremoteentitiesflytecontext) | This is an internal-facing context object, that most users will not have to deal with. |
| [`FlyteGateNode`](.././flytekit.remote.entities#flytekitremoteentitiesflytegatenode) |  |
| [`FlyteLaunchPlan`](.././flytekit.remote.entities#flytekitremoteentitiesflytelaunchplan) | A class encapsulating a remote Flyte launch plan. |
| [`FlyteNode`](.././flytekit.remote.entities#flytekitremoteentitiesflytenode) | A class encapsulating a remote Flyte node. |
| [`FlyteTask`](.././flytekit.remote.entities#flytekitremoteentitiesflytetask) | A class encapsulating a remote Flyte task. |
| [`FlyteTaskNode`](.././flytekit.remote.entities#flytekitremoteentitiesflytetasknode) | A class encapsulating a task that a Flyte node needs to execute. |
| [`FlyteWorkflow`](.././flytekit.remote.entities#flytekitremoteentitiesflyteworkflow) | A class encapsulating a remote Flyte workflow. |
| [`FlyteWorkflowNode`](.././flytekit.remote.entities#flytekitremoteentitiesflyteworkflownode) | A class encapsulating a workflow that a Flyte node needs to execute. |
| [`Identifier`](.././flytekit.remote.entities#flytekitremoteentitiesidentifier) |  |
| [`Node`](.././flytekit.remote.entities#flytekitremoteentitiesnode) |  |
| [`RemoteEntity`](.././flytekit.remote.entities#flytekitremoteentitiesremoteentity) | Helper class that provides a standard way to create an ABC using. |
| [`TaskSpec`](.././flytekit.remote.entities#flytekitremoteentitiestaskspec) |  |
| [`TypedInterface`](.././flytekit.remote.entities#flytekitremoteentitiestypedinterface) |  |
| [`WorkflowMetadata`](.././flytekit.remote.entities#flytekitremoteentitiesworkflowmetadata) |  |
| [`WorkflowMetadataDefaults`](.././flytekit.remote.entities#flytekitremoteentitiesworkflowmetadatadefaults) |  |
| [`WorkflowSpec`](.././flytekit.remote.entities#flytekitremoteentitiesworkflowspec) |  |

### Methods

| Method | Description |
|-|-|
| [`create_and_link_node_from_remote()`](#create_and_link_node_from_remote) | This method is used to generate a node with bindings especially when using remote entities, like FlyteWorkflow,. |


### Variables

| Property | Type | Description |
|-|-|-|
| `annotations` | `_Feature` |  |
| `logger` | `Logger` |  |

## Methods

#### create_and_link_node_from_remote()

```python
def create_and_link_node_from_remote(
    ctx: FlyteContext,
    entity: HasFlyteInterface,
    overridden_interface: Optional[_interface_models.TypedInterface],
    add_node_to_compilation_state: bool,
    node_id: str,
    _inputs_not_allowed: Optional[Set[str]],
    _ignorable_inputs: Optional[Set[str]],
    kwargs,
) -> Optional[Union[Tuple[Promise], Promise, VoidPromise]]
```
This method is used to generate a node with bindings especially when using remote entities, like FlyteWorkflow,
FlyteTask and FlyteLaunchplan.

This method is kept separate from the similar named method `create_and_link_node` as remote entities have to be
handled differently. The major difference arises from the fact that the remote entities do not have a python
interface, so all comparisons need to happen using the Literals.



| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `entity` | `HasFlyteInterface` |
| `overridden_interface` | `Optional[_interface_models.TypedInterface]` |
| `add_node_to_compilation_state` | `bool` |
| `node_id` | `str` |
| `_inputs_not_allowed` | `Optional[Set[str]]` |
| `_ignorable_inputs` | `Optional[Set[str]]` |
| `kwargs` | ``**kwargs`` |

## flytekit.remote.entities.Binding

```python
class Binding(
    var,
    binding,
)
```
An input/output binding of a variable to either static value or a node output.



| Parameter | Type |
|-|-|
| `var` |  |
| `binding` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> flytekit.core.models.literals.Binding
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `binding` |  | {{< multiline >}}Data to use to bind this variable.
{{< /multiline >}} |
| `is_empty` |  |  |
| `var` |  | {{< multiline >}}A variable name, must match an input or output variable of the node.
{{< /multiline >}} |

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
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
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
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `if_else` |  |  |
| `is_empty` |  |  |

## flytekit.remote.entities.FlyteContext

This is an internal-facing context object, that most users will not have to deal with. It's essentially a globally
available grab bag of settings and objects that allows flytekit to do things like convert complex types, run and
compile workflows, serialize Flyte entities, etc.

Even though this object as a ``current_context`` function on it, it should not be called directly. Please use the
:py:class:`flytekit.FlyteContextManager` object instead.

Please do not confuse this object with the :py:class:`flytekit.ExecutionParameters` object.


```python
class FlyteContext(
    file_access: FileAccessProvider,
    level: int,
    flyte_client: Optional['friendly_client.SynchronousFlyteClient'],
    compilation_state: Optional[CompilationState],
    execution_state: Optional[ExecutionState],
    serialization_settings: Optional[SerializationSettings],
    in_a_condition: bool,
    origin_stackframe: Optional[traceback.FrameSummary],
    output_metadata_tracker: Optional[OutputMetadataTracker],
    worker_queue: Optional[Controller],
)
```
| Parameter | Type |
|-|-|
| `file_access` | `FileAccessProvider` |
| `level` | `int` |
| `flyte_client` | `Optional['friendly_client.SynchronousFlyteClient']` |
| `compilation_state` | `Optional[CompilationState]` |
| `execution_state` | `Optional[ExecutionState]` |
| `serialization_settings` | `Optional[SerializationSettings]` |
| `in_a_condition` | `bool` |
| `origin_stackframe` | `Optional[traceback.FrameSummary]` |
| `output_metadata_tracker` | `Optional[OutputMetadataTracker]` |
| `worker_queue` | `Optional[Controller]` |

### Methods

| Method | Description |
|-|-|
| [`current_context()`](#current_context) | This method exists only to maintain backwards compatibility. |
| [`enter_conditional_section()`](#enter_conditional_section) |  |
| [`get_deck()`](#get_deck) | Returns the deck that was created as part of the last execution. |
| [`get_origin_stackframe_repr()`](#get_origin_stackframe_repr) |  |
| [`new_builder()`](#new_builder) |  |
| [`new_compilation_state()`](#new_compilation_state) | Creates and returns a default compilation state. |
| [`new_execution_state()`](#new_execution_state) | Creates and returns a new default execution state. |
| [`set_stackframe()`](#set_stackframe) |  |
| [`with_client()`](#with_client) |  |
| [`with_compilation_state()`](#with_compilation_state) |  |
| [`with_execution_state()`](#with_execution_state) |  |
| [`with_file_access()`](#with_file_access) |  |
| [`with_new_compilation_state()`](#with_new_compilation_state) |  |
| [`with_output_metadata_tracker()`](#with_output_metadata_tracker) |  |
| [`with_serialization_settings()`](#with_serialization_settings) |  |
| [`with_worker_queue()`](#with_worker_queue) |  |


#### current_context()

```python
def current_context()
```
This method exists only to maintain backwards compatibility. Please use
``FlyteContextManager.current_context()`` instead.

Users of flytekit should be wary not to confuse the object returned from this function
with :py:func:`flytekit.current_context`


#### enter_conditional_section()

```python
def enter_conditional_section()
```
#### get_deck()

```python
def get_deck()
```
Returns the deck that was created as part of the last execution.

The return value depends on the execution environment. In a notebook, the return value is compatible with
IPython.display and should be rendered in the notebook.

.. code-block:: python

with flytekit.new_context() as ctx:
my_task(...)
ctx.get_deck()

OR if you wish to explicitly display

.. code-block:: python

from IPython import display
display(ctx.get_deck())


#### get_origin_stackframe_repr()

```python
def get_origin_stackframe_repr()
```
#### new_builder()

```python
def new_builder()
```
#### new_compilation_state()

```python
def new_compilation_state(
    prefix: str,
) -> CompilationState
```
Creates and returns a default compilation state. For most of the code this should be the entrypoint
of compilation, otherwise the code should always uses - with_compilation_state


| Parameter | Type |
|-|-|
| `prefix` | `str` |

#### new_execution_state()

```python
def new_execution_state(
    working_dir: Optional[os.PathLike],
) -> ExecutionState
```
Creates and returns a new default execution state. This should be used at the entrypoint of execution,
in all other cases it is preferable to use with_execution_state


| Parameter | Type |
|-|-|
| `working_dir` | `Optional[os.PathLike]` |

#### set_stackframe()

```python
def set_stackframe(
    s: traceback.FrameSummary,
)
```
| Parameter | Type |
|-|-|
| `s` | `traceback.FrameSummary` |

#### with_client()

```python
def with_client(
    c: SynchronousFlyteClient,
) -> Builder
```
| Parameter | Type |
|-|-|
| `c` | `SynchronousFlyteClient` |

#### with_compilation_state()

```python
def with_compilation_state(
    c: CompilationState,
) -> Builder
```
| Parameter | Type |
|-|-|
| `c` | `CompilationState` |

#### with_execution_state()

```python
def with_execution_state(
    es: ExecutionState,
) -> Builder
```
| Parameter | Type |
|-|-|
| `es` | `ExecutionState` |

#### with_file_access()

```python
def with_file_access(
    fa: FileAccessProvider,
) -> Builder
```
| Parameter | Type |
|-|-|
| `fa` | `FileAccessProvider` |

#### with_new_compilation_state()

```python
def with_new_compilation_state()
```
#### with_output_metadata_tracker()

```python
def with_output_metadata_tracker(
    t: OutputMetadataTracker,
) -> Builder
```
| Parameter | Type |
|-|-|
| `t` | `OutputMetadataTracker` |

#### with_serialization_settings()

```python
def with_serialization_settings(
    ss: SerializationSettings,
) -> Builder
```
| Parameter | Type |
|-|-|
| `ss` | `SerializationSettings` |

#### with_worker_queue()

```python
def with_worker_queue(
    wq: Controller,
) -> Builder
```
| Parameter | Type |
|-|-|
| `wq` | `Controller` |

### Properties

| Property | Type | Description |
|-|-|-|
| `user_space_params` |  |  |

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
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


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
) -> LaunchPlanSpec
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `annotations` |  | {{< multiline >}}The annotations to execute the workflow with
{{< /multiline >}} |
| `auth_role` |  | {{< multiline >}}The authorization method with which to execute the workflow.
{{< /multiline >}} |
| `default_inputs` |  | {{< multiline >}}Input values to be passed for the execution
{{< /multiline >}} |
| `entity_metadata` |  |  |
| `entity_type_text` |  |  |
| `fixed_inputs` |  | {{< multiline >}}Fixed, non-overridable inputs for the Launch Plan
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
{{< /multiline >}} |
| `max_parallelism` |  |  |
| `name` |  |  |
| `overwrite_cache` |  |  |
| `python_interface` |  |  |
| `raw_output_data_config` |  | {{< multiline >}}Where to store offloaded data like Blobs and Schemas
{{< /multiline >}} |
| `resource_type` |  |  |
| `security_context` |  |  |
| `workflow_id` |  | {{< multiline >}}Unique identifier for the workflow in question
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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> Node
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `array_node` |  |  |
| `branch_node` |  | {{< multiline >}}[Optional] Information about the branch node to evaluate in this node.

{{< /multiline >}} |
| `flyte_entity` |  |  |
| `gate_node` |  |  |
| `id` |  | {{< multiline >}}A workflow-level unique identifier that identifies this node in the workflow. "inputs" and
"outputs" are reserved node ids that cannot be used by other nodes.

{{< /multiline >}} |
| `inputs` |  | {{< multiline >}}Specifies how to bind the underlying interface's inputs.  All required inputs specified
in the underlying interface must be fulfilled.

{{< /multiline >}} |
| `is_empty` |  |  |
| `metadata` |  | {{< multiline >}}Extra metadata about the node.

{{< /multiline >}} |
| `output_aliases` |  | {{< multiline >}}[Optional] A node can define aliases for a subset of its outputs. This
is particularly useful if different nodes need to conform to the same interface (e.g. all branches in
a branch node). Downstream nodes must refer to this node's outputs using the alias if one is specified.

{{< /multiline >}} |
| `target` |  |  |
| `task_node` |  | {{< multiline >}}[Optional] Information about the Task to execute in this node.

{{< /multiline >}} |
| `upstream_node_ids` |  | {{< multiline >}}[Optional] Specifies execution dependency for this node ensuring it will
only get scheduled to run after all its upstream nodes have completed. This node will have
an implicit dependency on any node that appears in inputs field.

{{< /multiline >}} |
| `upstream_nodes` |  |  |
| `workflow_node` |  | {{< multiline >}}[Optional] Information about the Workflow to execute in this mode.

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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


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
) -> TaskSpec
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `config` |  | {{< multiline >}}Arbitrary dictionary containing metadata for parsing and handling custom plugins.

{{< /multiline >}} |
| `container` |  | {{< multiline >}}If not None, the target of execution should be a container.

{{< /multiline >}} |
| `custom` |  | {{< multiline >}}Arbitrary dictionary containing metadata for custom plugins.

{{< /multiline >}} |
| `docs` |  |  |
| `entity_type_text` |  |  |
| `extended_resources` |  |  |
| `id` |  | {{< multiline >}}This is generated by the system and uniquely identifies the task.

{{< /multiline >}} |
| `interface` |  | {{< multiline >}}The interface definition for this task.

{{< /multiline >}} |
| `is_empty` |  |  |
| `k8s_pod` |  |  |
| `metadata` |  | {{< multiline >}}This contains information needed at runtime to determine behavior such as whether or not outputs are
discoverable, timeouts, and retries.

{{< /multiline >}} |
| `name` |  |  |
| `python_interface` |  |  |
| `resource_type` |  |  |
| `security_context` |  |  |
| `should_register` |  |  |
| `sql` |  |  |
| `task_type_version` |  |  |
| `template` |  |  |
| `type` |  | {{< multiline >}}This is used to identify additional extensions for use by Propeller or SDK.

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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`promote_from_model()`](#promote_from_model) | Takes the idl wrapper for a TaskNode,. |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> TaskNode
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`get_non_system_nodes()`](#get_non_system_nodes) |  |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`promote_from_closure()`](#promote_from_closure) | Extracts out the relevant portions of a FlyteWorkflow from a closure from the control plane. |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


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
) -> WorkflowSpec
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `docs` |  |  |
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
| `sub_workflows` |  |  |
| `template` |  |  |

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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> WorkflowNode
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `flyte_launch_plan` |  |  |
| `flyte_workflow` |  |  |
| `is_empty` |  |  |
| `launchplan_ref` |  | {{< multiline >}}A globally unique identifier for the launch plan, which should map to Admin.
{{< /multiline >}} |
| `reference` |  |  |
| `sub_workflow_ref` |  | {{< multiline >}}[Optional] Reference to a subworkflow, that should be defined with the compiler context.

{{< /multiline >}} |

## flytekit.remote.entities.Identifier

```python
class Identifier(
    resource_type,
    project,
    domain,
    name,
    version,
)
```
| Parameter | Type |
|-|-|
| `resource_type` |  |
| `project` |  |
| `domain` |  |
| `name` |  |
| `version` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`resource_type_name()`](#resource_type_name) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
) -> Identifier
```
| Parameter | Type |
|-|-|
| `p` |  |

#### resource_type_name()

```python
def resource_type_name()
```
#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `domain` |  |  |
| `is_empty` |  |  |
| `name` |  |  |
| `project` |  |  |
| `resource_type` |  | {{< multiline >}}enum value from ResourceType
{{< /multiline >}} |
| `version` |  |  |

## flytekit.remote.entities.Node

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



| Parameter | Type |
|-|-|
| `id` |  |
| `metadata` |  |
| `inputs` |  |
| `upstream_node_ids` |  |
| `output_aliases` |  |
| `task_node` |  |
| `workflow_node` |  |
| `branch_node` |  |
| `gate_node` | `typing.Optional[flytekit.models.core.workflow.GateNode]` |
| `array_node` | `typing.Optional[flytekit.models.core.workflow.ArrayNode]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> Node
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `array_node` |  |  |
| `branch_node` |  | {{< multiline >}}[Optional] Information about the branch node to evaluate in this node.

{{< /multiline >}} |
| `gate_node` |  |  |
| `id` |  | {{< multiline >}}A workflow-level unique identifier that identifies this node in the workflow. "inputs" and
"outputs" are reserved node ids that cannot be used by other nodes.

{{< /multiline >}} |
| `inputs` |  | {{< multiline >}}Specifies how to bind the underlying interface's inputs.  All required inputs specified
in the underlying interface must be fulfilled.

{{< /multiline >}} |
| `is_empty` |  |  |
| `metadata` |  | {{< multiline >}}Extra metadata about the node.

{{< /multiline >}} |
| `output_aliases` |  | {{< multiline >}}[Optional] A node can define aliases for a subset of its outputs. This
is particularly useful if different nodes need to conform to the same interface (e.g. all branches in
a branch node). Downstream nodes must refer to this node's outputs using the alias if one is specified.

{{< /multiline >}} |
| `target` |  |  |
| `task_node` |  | {{< multiline >}}[Optional] Information about the Task to execute in this node.

{{< /multiline >}} |
| `upstream_node_ids` |  | {{< multiline >}}[Optional] Specifies execution dependency for this node ensuring it will
only get scheduled to run after all its upstream nodes have completed. This node will have
an implicit dependency on any node that appears in inputs field.

{{< /multiline >}} |
| `workflow_node` |  | {{< multiline >}}[Optional] Information about the Workflow to execute in this mode.

{{< /multiline >}} |

## flytekit.remote.entities.RemoteEntity

Helper class that provides a standard way to create an ABC using
inheritance.


```python
class RemoteEntity(
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition. |
| [`execute()`](#execute) |  |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |


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
### Properties

| Property | Type | Description |
|-|-|-|
| `id` |  |  |
| `name` |  |  |
| `python_interface` |  |  |

## flytekit.remote.entities.TaskSpec

```python
class TaskSpec(
    template: flytekit.models.task.TaskTemplate,
    docs: typing.Optional[flytekit.models.documentation.Documentation],
)
```
| Parameter | Type |
|-|-|
| `template` | `flytekit.models.task.TaskTemplate` |
| `docs` | `typing.Optional[flytekit.models.documentation.Documentation]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> TaskSpec
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `docs` |  |  |
| `is_empty` |  |  |
| `template` |  |  |

## flytekit.remote.entities.TypedInterface

```python
class TypedInterface(
    inputs,
    outputs,
)
```
Please note that this model is slightly incorrect, but is more user-friendly. The underlying inputs and
outputs are represented directly as Python dicts, rather than going through the additional VariableMap layer.



| Parameter | Type |
|-|-|
| `inputs` |  |
| `outputs` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`transform_interface_to_list()`](#transform_interface_to_list) | Takes a single task interface and interpolates it to an array interface - to allow performing distributed. |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto: flyteidl.core.interface_pb2.TypedInterface,
) -> TypedInterface
```
| Parameter | Type |
|-|-|
| `proto` | `flyteidl.core.interface_pb2.TypedInterface` |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### transform_interface_to_list()

```python
def transform_interface_to_list(
    bound_inputs: typing.Set[str],
    excluded_inputs: typing.Set[str],
) -> TypedInterface
```
Takes a single task interface and interpolates it to an array interface - to allow performing distributed
python map like functions


| Parameter | Type |
|-|-|
| `bound_inputs` | `typing.Set[str]` |
| `excluded_inputs` | `typing.Set[str]` |

#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `inputs` |  |  |
| `is_empty` |  |  |
| `outputs` |  |  |

## flytekit.remote.entities.WorkflowMetadata

```python
class WorkflowMetadata(
    on_failure,
)
```
Metadata for the workflow.



| Parameter | Type |
|-|-|
| `on_failure` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> WorkflowMetadata
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `on_failure` |  |  |

## flytekit.remote.entities.WorkflowMetadataDefaults

```python
class WorkflowMetadataDefaults(
    interruptible,
)
```
Metadata Defaults for the workflow.


| Parameter | Type |
|-|-|
| `interruptible` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> WorkflowMetadata
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `interruptible` |  |  |
| `is_empty` |  |  |

## flytekit.remote.entities.WorkflowSpec

```python
class WorkflowSpec(
    template: flytekit.models.core.workflow.WorkflowTemplate,
    sub_workflows: typing.List[flytekit.models.core.workflow.WorkflowTemplate],
    docs: typing.Optional[flytekit.models.documentation.Documentation],
)
```
This object fully encapsulates the specification of a workflow


| Parameter | Type |
|-|-|
| `template` | `flytekit.models.core.workflow.WorkflowTemplate` |
| `sub_workflows` | `typing.List[flytekit.models.core.workflow.WorkflowTemplate]` |
| `docs` | `typing.Optional[flytekit.models.documentation.Documentation]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> WorkflowSpec
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `docs` |  |  |
| `is_empty` |  |  |
| `sub_workflows` |  |  |
| `template` |  |  |

