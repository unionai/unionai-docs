---
title: flytekit.remote.entities
version: 1.15.4.dev2+g3e3ce2426
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
| [`Binding`](.././flytekit.remote.entities#flytekitremoteentitiesbinding) | None. |
| [`FlyteArrayNode`](.././flytekit.remote.entities#flytekitremoteentitiesflytearraynode) | None. |
| [`FlyteBranchNode`](.././flytekit.remote.entities#flytekitremoteentitiesflytebranchnode) | None. |
| [`FlyteContext`](.././flytekit.remote.entities#flytekitremoteentitiesflytecontext) | This is an internal-facing context object, that most users will not have to deal with. |
| [`FlyteGateNode`](.././flytekit.remote.entities#flytekitremoteentitiesflytegatenode) | None. |
| [`FlyteLaunchPlan`](.././flytekit.remote.entities#flytekitremoteentitiesflytelaunchplan) | A class encapsulating a remote Flyte launch plan. |
| [`FlyteNode`](.././flytekit.remote.entities#flytekitremoteentitiesflytenode) | A class encapsulating a remote Flyte node. |
| [`FlyteTask`](.././flytekit.remote.entities#flytekitremoteentitiesflytetask) | A class encapsulating a remote Flyte task. |
| [`FlyteTaskNode`](.././flytekit.remote.entities#flytekitremoteentitiesflytetasknode) | A class encapsulating a task that a Flyte node needs to execute. |
| [`FlyteWorkflow`](.././flytekit.remote.entities#flytekitremoteentitiesflyteworkflow) | A class encapsulating a remote Flyte workflow. |
| [`FlyteWorkflowNode`](.././flytekit.remote.entities#flytekitremoteentitiesflyteworkflownode) | A class encapsulating a workflow that a Flyte node needs to execute. |
| [`Identifier`](.././flytekit.remote.entities#flytekitremoteentitiesidentifier) | None. |
| [`Node`](.././flytekit.remote.entities#flytekitremoteentitiesnode) | None. |
| [`RemoteEntity`](.././flytekit.remote.entities#flytekitremoteentitiesremoteentity) | Helper class that provides a standard way to create an ABC using. |
| [`TaskSpec`](.././flytekit.remote.entities#flytekitremoteentitiestaskspec) | None. |
| [`TypedInterface`](.././flytekit.remote.entities#flytekitremoteentitiestypedinterface) | None. |
| [`WorkflowMetadata`](.././flytekit.remote.entities#flytekitremoteentitiesworkflowmetadata) | None. |
| [`WorkflowMetadataDefaults`](.././flytekit.remote.entities#flytekitremoteentitiesworkflowmetadatadefaults) | None. |
| [`WorkflowSpec`](.././flytekit.remote.entities#flytekitremoteentitiesworkflowspec) | None. |

## flytekit.remote.entities.Binding

```python
def Binding(
    var,
    binding,
):
```
An input/output binding of a variable to either static value or a node output.



| Parameter | Type |
|-|-|
| `var` |  |
| `binding` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
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
| binding |  |  |
| is_empty |  |  |
| var |  |  |

## flytekit.remote.entities.FlyteArrayNode

```python
def FlyteArrayNode(
    flyte_node: FlyteNode,
    parallelism: int,
    min_successes: int,
    min_success_ratio: float,
):
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
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`promote_from_model()`](#promote_from_model) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### promote_from_model()

```python
def promote_from_model(
    model: _workflow_model.ArrayNode,
    flyte_node: FlyteNode,
):
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
| flyte_node |  |  |
| is_empty |  |  |
| node |  |  |

## flytekit.remote.entities.FlyteBranchNode

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

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`promote_from_model()`](#promote_from_model) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_objct,
):
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
):
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
| if_else |  |  |
| is_empty |  |  |

## flytekit.remote.entities.FlyteContext

This is an internal-facing context object, that most users will not have to deal with. It's essentially a globally
available grab bag of settings and objects that allows flytekit to do things like convert complex types, run and
compile workflows, serialize Flyte entities, etc.

Even though this object as a ``current_context`` function on it, it should not be called directly. Please use the
:py:class:`flytekit.FlyteContextManager` object instead.

Please do not confuse this object with the :py:class:`flytekit.ExecutionParameters` object.


```python
def FlyteContext(
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
):
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
| [`current_context()`](#current_context) | This method exists only to maintain backwards compatibility |
| [`enter_conditional_section()`](#enter_conditional_section) | None |
| [`get_deck()`](#get_deck) | Returns the deck that was created as part of the last execution |
| [`get_origin_stackframe_repr()`](#get_origin_stackframe_repr) | None |
| [`new_builder()`](#new_builder) | None |
| [`new_compilation_state()`](#new_compilation_state) | Creates and returns a default compilation state |
| [`new_execution_state()`](#new_execution_state) | Creates and returns a new default execution state |
| [`set_stackframe()`](#set_stackframe) | None |
| [`with_client()`](#with_client) | None |
| [`with_compilation_state()`](#with_compilation_state) | None |
| [`with_execution_state()`](#with_execution_state) | None |
| [`with_file_access()`](#with_file_access) | None |
| [`with_new_compilation_state()`](#with_new_compilation_state) | None |
| [`with_output_metadata_tracker()`](#with_output_metadata_tracker) | None |
| [`with_serialization_settings()`](#with_serialization_settings) | None |
| [`with_worker_queue()`](#with_worker_queue) | None |


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
):
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
):
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
):
```
| Parameter | Type |
|-|-|
| `s` | `traceback.FrameSummary` |

#### with_client()

```python
def with_client(
    c: SynchronousFlyteClient,
):
```
| Parameter | Type |
|-|-|
| `c` | `SynchronousFlyteClient` |

#### with_compilation_state()

```python
def with_compilation_state(
    c: CompilationState,
):
```
| Parameter | Type |
|-|-|
| `c` | `CompilationState` |

#### with_execution_state()

```python
def with_execution_state(
    es: ExecutionState,
):
```
| Parameter | Type |
|-|-|
| `es` | `ExecutionState` |

#### with_file_access()

```python
def with_file_access(
    fa: FileAccessProvider,
):
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
):
```
| Parameter | Type |
|-|-|
| `t` | `OutputMetadataTracker` |

#### with_serialization_settings()

```python
def with_serialization_settings(
    ss: SerializationSettings,
):
```
| Parameter | Type |
|-|-|
| `ss` | `SerializationSettings` |

#### with_worker_queue()

```python
def with_worker_queue(
    wq: Controller,
):
```
| Parameter | Type |
|-|-|
| `wq` | `Controller` |

### Properties

| Property | Type | Description |
|-|-|-|
| user_space_params |  |  |

## flytekit.remote.entities.FlyteGateNode

```python
def FlyteGateNode(
    signal: typing.Optional[flytekit.models.core.workflow.SignalCondition],
    sleep: typing.Optional[flytekit.models.core.workflow.SleepCondition],
    approve: typing.Optional[flytekit.models.core.workflow.ApproveCondition],
):
```
| Parameter | Type |
|-|-|
| `signal` | `typing.Optional[flytekit.models.core.workflow.SignalCondition]` |
| `sleep` | `typing.Optional[flytekit.models.core.workflow.SleepCondition]` |
| `approve` | `typing.Optional[flytekit.models.core.workflow.ApproveCondition]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`promote_from_model()`](#promote_from_model) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.workflow_pb2.GateNode,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.workflow_pb2.GateNode` |

#### promote_from_model()

```python
def promote_from_model(
    model: _workflow_model.GateNode,
):
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
| approve |  |  |
| condition |  |  |
| is_empty |  |  |
| signal |  |  |
| sleep |  |  |

## flytekit.remote.entities.FlyteLaunchPlan

A class encapsulating a remote Flyte launch plan.


```python
def FlyteLaunchPlan(
    id,
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `id` |  |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | None |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition |
| [`execute()`](#execute) | None |
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`local_execute()`](#local_execute) | None |
| [`local_execution_mode()`](#local_execution_mode) | None |
| [`promote_from_model()`](#promote_from_model) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### compile()

```python
def compile(
    ctx: FlyteContext,
    args,
    kwargs,
):
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
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2,
):
```
| Parameter | Type |
|-|-|
| `pb2` |  |

#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
):
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
):
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
| annotations |  |  |
| auth_role |  |  |
| default_inputs |  |  |
| entity_metadata |  |  |
| entity_type_text |  |  |
| fixed_inputs |  |  |
| flyte_workflow |  |  |
| id |  |  |
| interface |  |  |
| is_empty |  |  |
| is_scheduled |  |  |
| labels |  |  |
| max_parallelism |  |  |
| name |  |  |
| overwrite_cache |  |  |
| python_interface |  |  |
| raw_output_data_config |  |  |
| resource_type |  |  |
| security_context |  |  |
| workflow_id |  |  |

## flytekit.remote.entities.FlyteNode

A class encapsulating a remote Flyte node.


```python
def FlyteNode(
    id,
    upstream_nodes,
    bindings,
    metadata,
    task_node: Optional[FlyteTaskNode],
    workflow_node: Optional[FlyteWorkflowNode],
    branch_node: Optional[FlyteBranchNode],
    gate_node: Optional[FlyteGateNode],
    array_node: Optional[FlyteArrayNode],
):
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
| [`promote_from_model()`](#promote_from_model) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
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
):
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
| array_node |  |  |
| branch_node |  |  |
| flyte_entity |  |  |
| gate_node |  |  |
| id |  |  |
| inputs |  |  |
| is_empty |  |  |
| metadata |  |  |
| output_aliases |  |  |
| target |  |  |
| task_node |  |  |
| upstream_node_ids |  |  |
| upstream_nodes |  |  |
| workflow_node |  |  |

## flytekit.remote.entities.FlyteTask

A class encapsulating a remote Flyte task.


```python
def FlyteTask(
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
):
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
| [`compile()`](#compile) | None |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition |
| [`execute()`](#execute) | None |
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`local_execute()`](#local_execute) | None |
| [`local_execution_mode()`](#local_execution_mode) | None |
| [`promote_from_model()`](#promote_from_model) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### compile()

```python
def compile(
    ctx: flytekit.core.context_manager.FlyteContext,
    args,
    kwargs,
):
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
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
):
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
):
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
| config |  |  |
| container |  |  |
| custom |  |  |
| docs |  |  |
| entity_type_text |  |  |
| extended_resources |  |  |
| id |  |  |
| interface |  |  |
| is_empty |  |  |
| k8s_pod |  |  |
| metadata |  |  |
| name |  |  |
| python_interface |  |  |
| resource_type |  |  |
| security_context |  |  |
| should_register |  |  |
| sql |  |  |
| task_type_version |  |  |
| template |  |  |
| type |  |  |

## flytekit.remote.entities.FlyteTaskNode

A class encapsulating a task that a Flyte node needs to execute.


```python
def FlyteTaskNode(
    flyte_task: FlyteTask,
):
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
| [`promote_from_model()`](#promote_from_model) | Takes the idl wrapper for a TaskNode, |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### promote_from_model()

```python
def promote_from_model(
    task: FlyteTask,
):
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
| flyte_task |  |  |
| is_empty |  |  |
| overrides |  |  |
| reference_id |  |  |

## flytekit.remote.entities.FlyteWorkflow

A class encapsulating a remote Flyte workflow.


```python
def FlyteWorkflow(
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
):
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
| [`compile()`](#compile) | None |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition |
| [`execute()`](#execute) | None |
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`get_non_system_nodes()`](#get_non_system_nodes) | None |
| [`local_execute()`](#local_execute) | None |
| [`local_execution_mode()`](#local_execution_mode) | None |
| [`promote_from_closure()`](#promote_from_closure) | Extracts out the relevant portions of a FlyteWorkflow from a closure from the control plane |
| [`promote_from_model()`](#promote_from_model) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### compile()

```python
def compile(
    ctx: flytekit.core.context_manager.FlyteContext,
    args,
    kwargs,
):
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
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### get_non_system_nodes()

```python
def get_non_system_nodes(
    nodes: List[_workflow_models.Node],
):
```
| Parameter | Type |
|-|-|
| `nodes` | `List[_workflow_models.Node]` |

#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
):
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
):
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
):
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
| docs |  |  |
| entity_type_text |  |  |
| failure_node |  |  |
| flyte_nodes |  |  |
| flyte_sub_workflows |  |  |
| flyte_tasks |  |  |
| id |  |  |
| interface |  |  |
| is_empty |  |  |
| metadata |  |  |
| metadata_defaults |  |  |
| name |  |  |
| nodes |  |  |
| outputs |  |  |
| python_interface |  |  |
| resource_type |  |  |
| should_register |  |  |
| sub_workflows |  |  |
| template |  |  |

## flytekit.remote.entities.FlyteWorkflowNode

A class encapsulating a workflow that a Flyte node needs to execute.


```python
def FlyteWorkflowNode(
    flyte_workflow: FlyteWorkflow,
    flyte_launch_plan: FlyteLaunchPlan,
):
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
| [`promote_from_model()`](#promote_from_model) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
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
):
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
| flyte_launch_plan |  |  |
| flyte_workflow |  |  |
| is_empty |  |  |
| launchplan_ref |  |  |
| reference |  |  |
| sub_workflow_ref |  |  |

## flytekit.remote.entities.Identifier

```python
def Identifier(
    resource_type,
    project,
    domain,
    name,
    version,
):
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
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`resource_type_name()`](#resource_type_name) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
):
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
| domain |  |  |
| is_empty |  |  |
| name |  |  |
| project |  |  |
| resource_type |  |  |
| version |  |  |

## flytekit.remote.entities.Node

```python
def Node(
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
):
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
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
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
| array_node |  |  |
| branch_node |  |  |
| gate_node |  |  |
| id |  |  |
| inputs |  |  |
| is_empty |  |  |
| metadata |  |  |
| output_aliases |  |  |
| target |  |  |
| task_node |  |  |
| upstream_node_ids |  |  |
| workflow_node |  |  |

## flytekit.remote.entities.RemoteEntity

Helper class that provides a standard way to create an ABC using
inheritance.


```python
def RemoteEntity(
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | None |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition |
| [`execute()`](#execute) | None |
| [`local_execute()`](#local_execute) | None |
| [`local_execution_mode()`](#local_execution_mode) | None |


#### compile()

```python
def compile(
    ctx: flytekit.core.context_manager.FlyteContext,
    args,
    kwargs,
):
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
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
):
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
| id |  |  |
| name |  |  |
| python_interface |  |  |

## flytekit.remote.entities.TaskSpec

```python
def TaskSpec(
    template: flytekit.models.task.TaskTemplate,
    docs: typing.Optional[flytekit.models.documentation.Documentation],
):
```
| Parameter | Type |
|-|-|
| `template` | `flytekit.models.task.TaskTemplate` |
| `docs` | `typing.Optional[flytekit.models.documentation.Documentation]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
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
| docs |  |  |
| is_empty |  |  |
| template |  |  |

## flytekit.remote.entities.TypedInterface

```python
def TypedInterface(
    inputs,
    outputs,
):
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
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`transform_interface_to_list()`](#transform_interface_to_list) | Takes a single task interface and interpolates it to an array interface - to allow performing distributed |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto: flyteidl.core.interface_pb2.TypedInterface,
):
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
):
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
| inputs |  |  |
| is_empty |  |  |
| outputs |  |  |

## flytekit.remote.entities.WorkflowMetadata

```python
def WorkflowMetadata(
    on_failure,
):
```
Metadata for the workflow.



| Parameter | Type |
|-|-|
| `on_failure` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
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
| is_empty |  |  |
| on_failure |  |  |

## flytekit.remote.entities.WorkflowMetadataDefaults

```python
def WorkflowMetadataDefaults(
    interruptible,
):
```
Metadata Defaults for the workflow.


| Parameter | Type |
|-|-|
| `interruptible` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
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
| interruptible |  |  |
| is_empty |  |  |

## flytekit.remote.entities.WorkflowSpec

```python
def WorkflowSpec(
    template: flytekit.models.core.workflow.WorkflowTemplate,
    sub_workflows: typing.List[flytekit.models.core.workflow.WorkflowTemplate],
    docs: typing.Optional[flytekit.models.documentation.Documentation],
):
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
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
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
| docs |  |  |
| is_empty |  |  |
| sub_workflows |  |  |
| template |  |  |

