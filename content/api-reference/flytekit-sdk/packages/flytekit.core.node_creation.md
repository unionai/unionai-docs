---
title: flytekit.core.node_creation
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.node_creation

## Directory

### Classes

| Class | Description |
|-|-|
| [`BranchEvalMode`](.././flytekit.core.node_creation#flytekitcorenode_creationbranchevalmode) | This is a 3-way class, with the None value meaning that we are not within a conditional context. |
| [`ExecutionState`](.././flytekit.core.node_creation#flytekitcorenode_creationexecutionstate) | This is the context that is active when executing a task or a local workflow. |
| [`FlyteContext`](.././flytekit.core.node_creation#flytekitcorenode_creationflytecontext) | This is an internal-facing context object, that most users will not have to deal with. |
| [`LaunchPlan`](.././flytekit.core.node_creation#flytekitcorenode_creationlaunchplan) | Launch Plans are one of the core constructs of Flyte. |
| [`Node`](.././flytekit.core.node_creation#flytekitcorenode_creationnode) | This class will hold all the things necessary to make an SdkNode but we won't make one until we know things like. |
| [`PythonTask`](.././flytekit.core.node_creation#flytekitcorenode_creationpythontask) | Base Class for all Tasks with a Python native ``Interface``. |
| [`VoidPromise`](.././flytekit.core.node_creation#flytekitcorenode_creationvoidpromise) | This object is returned for tasks that do not return any outputs (declared interface is empty). |
| [`WorkflowBase`](.././flytekit.core.node_creation#flytekitcorenode_creationworkflowbase) | None. |

## flytekit.core.node_creation.BranchEvalMode

This is a 3-way class, with the None value meaning that we are not within a conditional context. The other two
values are
* Active - This means that the next ``then`` should run
* Skipped - The next ``then`` should not run


## flytekit.core.node_creation.ExecutionState

This is the context that is active when executing a task or a local workflow. This carries the necessary state to
execute.
Some required things during execution deal with temporary directories, ExecutionParameters that are passed to the
user etc.

Attributes:
mode (ExecutionState.Mode): Defines the context in which the task is executed (local, hosted, etc).
working_dir (os.PathLike): Specifies the remote, external directory where inputs, outputs and other protobufs
are uploaded
engine_dir (os.PathLike):
branch_eval_mode Optional[BranchEvalMode]: Used to determine whether a branch node should execute.
user_space_params Optional[ExecutionParameters]: Provides run-time, user-centric context such as a statsd
handler, a logging handler, the current execution id and a working directory.


```python
def ExecutionState(
    working_dir: Union[os.PathLike, str],
    mode: Optional[ExecutionState.Mode],
    engine_dir: Optional[Union[os.PathLike, str]],
    branch_eval_mode: Optional[BranchEvalMode],
    user_space_params: Optional[ExecutionParameters],
):
```
| Parameter | Type |
|-|-|
| `working_dir` | `Union[os.PathLike, str]` |
| `mode` | `Optional[ExecutionState.Mode]` |
| `engine_dir` | `Optional[Union[os.PathLike, str]]` |
| `branch_eval_mode` | `Optional[BranchEvalMode]` |
| `user_space_params` | `Optional[ExecutionParameters]` |

### Methods

| Method | Description |
|-|-|
| [`branch_complete()`](#branch_complete) | Indicates that we are within a conditional / ifelse block and the active branch is not done |
| [`is_local_execution()`](#is_local_execution) | None |
| [`take_branch()`](#take_branch) | Indicates that we are within an if-else block and the current branch has evaluated to true |
| [`with_params()`](#with_params) | Produces a copy of the current execution state and overrides the copy's parameters with passed parameter values |


#### branch_complete()

```python
def branch_complete()
```
Indicates that we are within a conditional / ifelse block and the active branch is not done.
Default to SKIPPED


#### is_local_execution()

```python
def is_local_execution()
```
#### take_branch()

```python
def take_branch()
```
Indicates that we are within an if-else block and the current branch has evaluated to true.
Useful only in local execution mode


#### with_params()

```python
def with_params(
    working_dir: Optional[os.PathLike],
    mode: Optional[Mode],
    engine_dir: Optional[os.PathLike],
    branch_eval_mode: Optional[BranchEvalMode],
    user_space_params: Optional[ExecutionParameters],
):
```
Produces a copy of the current execution state and overrides the copy's parameters with passed parameter values.


| Parameter | Type |
|-|-|
| `working_dir` | `Optional[os.PathLike]` |
| `mode` | `Optional[Mode]` |
| `engine_dir` | `Optional[os.PathLike]` |
| `branch_eval_mode` | `Optional[BranchEvalMode]` |
| `user_space_params` | `Optional[ExecutionParameters]` |

## flytekit.core.node_creation.FlyteContext

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

## flytekit.core.node_creation.LaunchPlan

Launch Plans are one of the core constructs of Flyte. Please take a look at the discussion in the
:std:ref:`core concepts <flyte:divedeep-launchplans>` if you are unfamiliar with them.

Every workflow is registered with a default launch plan, which is just a launch plan with none of the additional
attributes set - no default values, fixed values, schedules, etc. Assuming you have the following workflow

.. code-block:: python

@workflow
def wf(a: int, c: str) -> str:
...

Create the default launch plan with

.. code-block:: python

LaunchPlan.get_or_create(workflow=my_wf)

If you specify additional parameters, you'll also have to give the launch plan a unique name. Default and
fixed inputs can be expressed as Python native values like so:

.. literalinclude:: ../../../tests/flytekit/unit/core/test_launch_plan.py
:start-after: # fixed_and_default_start
:end-before: # fixed_and_default_end
:language: python
:dedent: 4

Additionally, a launch plan can be configured to run on a schedule and emit notifications.


Please see the relevant Schedule and Notification objects as well.

To configure the remaining parameters, you'll need to import the relevant model objects as well.

.. literalinclude:: ../../../tests/flytekit/unit/core/test_launch_plan.py
:start-after: # schedule_start
:end-before: # schedule_end
:language: python
:dedent: 4

.. code-block:: python

from flytekit.models.common import Annotations, AuthRole, Labels, RawOutputDataConfig

Then use as follows

.. literalinclude:: ../../../tests/flytekit/unit/core/test_launch_plan.py
:start-after: # auth_role_start
:end-before: # auth_role_end
:language: python
:dedent: 4


```python
def LaunchPlan(
    name: str,
    workflow: _annotated_workflow.WorkflowBase,
    parameters: _interface_models.ParameterMap,
    fixed_inputs: _literal_models.LiteralMap,
    schedule: Optional[_schedule_model.Schedule],
    notifications: Optional[List[_common_models.Notification]],
    labels: Optional[_common_models.Labels],
    annotations: Optional[_common_models.Annotations],
    raw_output_data_config: Optional[_common_models.RawOutputDataConfig],
    max_parallelism: Optional[int],
    security_context: Optional[security.SecurityContext],
    trigger: Optional[LaunchPlanTriggerBase],
    overwrite_cache: Optional[bool],
    auto_activate: bool,
):
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `workflow` | `_annotated_workflow.WorkflowBase` |
| `parameters` | `_interface_models.ParameterMap` |
| `fixed_inputs` | `_literal_models.LiteralMap` |
| `schedule` | `Optional[_schedule_model.Schedule]` |
| `notifications` | `Optional[List[_common_models.Notification]]` |
| `labels` | `Optional[_common_models.Labels]` |
| `annotations` | `Optional[_common_models.Annotations]` |
| `raw_output_data_config` | `Optional[_common_models.RawOutputDataConfig]` |
| `max_parallelism` | `Optional[int]` |
| `security_context` | `Optional[security.SecurityContext]` |
| `trigger` | `Optional[LaunchPlanTriggerBase]` |
| `overwrite_cache` | `Optional[bool]` |
| `auto_activate` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`clone_with()`](#clone_with) | None |
| [`construct_node_metadata()`](#construct_node_metadata) | None |
| [`create()`](#create) | None |
| [`get_default_launch_plan()`](#get_default_launch_plan) | Users should probably call the get_or_create function defined below instead |
| [`get_or_create()`](#get_or_create) | This function offers a friendlier interface for creating launch plans |


#### clone_with()

```python
def clone_with(
    name: str,
    parameters: Optional[_interface_models.ParameterMap],
    fixed_inputs: Optional[_literal_models.LiteralMap],
    schedule: Optional[_schedule_model.Schedule],
    notifications: Optional[List[_common_models.Notification]],
    labels: Optional[_common_models.Labels],
    annotations: Optional[_common_models.Annotations],
    raw_output_data_config: Optional[_common_models.RawOutputDataConfig],
    max_parallelism: Optional[int],
    security_context: Optional[security.SecurityContext],
    trigger: Optional[LaunchPlanTriggerBase],
    overwrite_cache: Optional[bool],
    auto_activate: bool,
):
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `parameters` | `Optional[_interface_models.ParameterMap]` |
| `fixed_inputs` | `Optional[_literal_models.LiteralMap]` |
| `schedule` | `Optional[_schedule_model.Schedule]` |
| `notifications` | `Optional[List[_common_models.Notification]]` |
| `labels` | `Optional[_common_models.Labels]` |
| `annotations` | `Optional[_common_models.Annotations]` |
| `raw_output_data_config` | `Optional[_common_models.RawOutputDataConfig]` |
| `max_parallelism` | `Optional[int]` |
| `security_context` | `Optional[security.SecurityContext]` |
| `trigger` | `Optional[LaunchPlanTriggerBase]` |
| `overwrite_cache` | `Optional[bool]` |
| `auto_activate` | `bool` |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
#### create()

```python
def create(
    name: str,
    workflow: _annotated_workflow.WorkflowBase,
    default_inputs: Optional[Dict[str, Any]],
    fixed_inputs: Optional[Dict[str, Any]],
    schedule: Optional[_schedule_model.Schedule],
    notifications: Optional[List[_common_models.Notification]],
    labels: Optional[_common_models.Labels],
    annotations: Optional[_common_models.Annotations],
    raw_output_data_config: Optional[_common_models.RawOutputDataConfig],
    max_parallelism: Optional[int],
    security_context: Optional[security.SecurityContext],
    auth_role: Optional[_common_models.AuthRole],
    trigger: Optional[LaunchPlanTriggerBase],
    overwrite_cache: Optional[bool],
    auto_activate: bool,
):
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `workflow` | `_annotated_workflow.WorkflowBase` |
| `default_inputs` | `Optional[Dict[str, Any]]` |
| `fixed_inputs` | `Optional[Dict[str, Any]]` |
| `schedule` | `Optional[_schedule_model.Schedule]` |
| `notifications` | `Optional[List[_common_models.Notification]]` |
| `labels` | `Optional[_common_models.Labels]` |
| `annotations` | `Optional[_common_models.Annotations]` |
| `raw_output_data_config` | `Optional[_common_models.RawOutputDataConfig]` |
| `max_parallelism` | `Optional[int]` |
| `security_context` | `Optional[security.SecurityContext]` |
| `auth_role` | `Optional[_common_models.AuthRole]` |
| `trigger` | `Optional[LaunchPlanTriggerBase]` |
| `overwrite_cache` | `Optional[bool]` |
| `auto_activate` | `bool` |

#### get_default_launch_plan()

```python
def get_default_launch_plan(
    ctx: FlyteContext,
    workflow: _annotated_workflow.WorkflowBase,
):
```
Users should probably call the get_or_create function defined below instead. A default launch plan is the one
that will just pick up whatever default values are defined in the workflow function signature (if any) and
use the default auth information supplied during serialization, with no notifications or schedules.



| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `workflow` | `_annotated_workflow.WorkflowBase` |

#### get_or_create()

```python
def get_or_create(
    workflow: _annotated_workflow.WorkflowBase,
    name: Optional[str],
    default_inputs: Optional[Dict[str, Any]],
    fixed_inputs: Optional[Dict[str, Any]],
    schedule: Optional[_schedule_model.Schedule],
    notifications: Optional[List[_common_models.Notification]],
    labels: Optional[_common_models.Labels],
    annotations: Optional[_common_models.Annotations],
    raw_output_data_config: Optional[_common_models.RawOutputDataConfig],
    max_parallelism: Optional[int],
    security_context: Optional[security.SecurityContext],
    auth_role: Optional[_common_models.AuthRole],
    trigger: Optional[LaunchPlanTriggerBase],
    overwrite_cache: Optional[bool],
    auto_activate: bool,
):
```
This function offers a friendlier interface for creating launch plans. If the name for the launch plan is not
supplied, this assumes you are looking for the default launch plan for the workflow. If it is specified, it
will be used. If creating the default launch plan, none of the other arguments may be specified.

The resulting launch plan is also cached and if called again with the same name, the
cached version is returned



| Parameter | Type |
|-|-|
| `workflow` | `_annotated_workflow.WorkflowBase` |
| `name` | `Optional[str]` |
| `default_inputs` | `Optional[Dict[str, Any]]` |
| `fixed_inputs` | `Optional[Dict[str, Any]]` |
| `schedule` | `Optional[_schedule_model.Schedule]` |
| `notifications` | `Optional[List[_common_models.Notification]]` |
| `labels` | `Optional[_common_models.Labels]` |
| `annotations` | `Optional[_common_models.Annotations]` |
| `raw_output_data_config` | `Optional[_common_models.RawOutputDataConfig]` |
| `max_parallelism` | `Optional[int]` |
| `security_context` | `Optional[security.SecurityContext]` |
| `auth_role` | `Optional[_common_models.AuthRole]` |
| `trigger` | `Optional[LaunchPlanTriggerBase]` |
| `overwrite_cache` | `Optional[bool]` |
| `auto_activate` | `bool` |

### Properties

| Property | Type | Description |
|-|-|-|
| annotations |  |  |
| fixed_inputs |  |  |
| interface |  |  |
| labels |  |  |
| max_parallelism |  |  |
| name |  |  |
| notifications |  |  |
| overwrite_cache |  |  |
| parameters |  |  |
| python_interface |  |  |
| raw_output_data_config |  |  |
| saved_inputs |  |  |
| schedule |  |  |
| security_context |  |  |
| should_auto_activate |  |  |
| trigger |  |  |
| workflow |  |  |

## flytekit.core.node_creation.Node

This class will hold all the things necessary to make an SdkNode but we won't make one until we know things like
ID, which from the registration step


```python
def Node(
    id: str,
    metadata: _workflow_model.NodeMetadata,
    bindings: List[_literal_models.Binding],
    upstream_nodes: List[Node],
    flyte_entity: Any,
):
```
| Parameter | Type |
|-|-|
| `id` | `str` |
| `metadata` | `_workflow_model.NodeMetadata` |
| `bindings` | `List[_literal_models.Binding]` |
| `upstream_nodes` | `List[Node]` |
| `flyte_entity` | `Any` |

### Methods

| Method | Description |
|-|-|
| [`runs_before()`](#runs_before) | This is typically something we shouldn't do |
| [`with_overrides()`](#with_overrides) | None |


#### runs_before()

```python
def runs_before(
    other: Node,
):
```
This is typically something we shouldn't do. This modifies an attribute of the other instance rather than
self. But it's done so only because we wanted this English function to be the same as the shift function.
That is, calling node_1.runs_before(node_2) and node_1 >> node_2 are the same. The shift operator going the
other direction is not implemented to further avoid confusion. Right shift was picked rather than left shift
because that's what most users are familiar with.


| Parameter | Type |
|-|-|
| `other` | `Node` |

#### with_overrides()

```python
def with_overrides(
    node_name: Optional[str],
    aliases: Optional[Dict[str, str]],
    requests: Optional[Resources],
    limits: Optional[Resources],
    timeout: Optional[Union[int, datetime.timedelta, object]],
    retries: Optional[int],
    interruptible: Optional[bool],
    name: Optional[str],
    task_config: Optional[Any],
    container_image: Optional[str],
    accelerator: Optional[BaseAccelerator],
    cache: Optional[bool],
    cache_version: Optional[str],
    cache_serialize: Optional[bool],
    shared_memory: Optional[Union[L[True], str]],
    pod_template: Optional[PodTemplate],
    resources: Optional[Resources],
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `node_name` | `Optional[str]` |
| `aliases` | `Optional[Dict[str, str]]` |
| `requests` | `Optional[Resources]` |
| `limits` | `Optional[Resources]` |
| `timeout` | `Optional[Union[int, datetime.timedelta, object]]` |
| `retries` | `Optional[int]` |
| `interruptible` | `Optional[bool]` |
| `name` | `Optional[str]` |
| `task_config` | `Optional[Any]` |
| `container_image` | `Optional[str]` |
| `accelerator` | `Optional[BaseAccelerator]` |
| `cache` | `Optional[bool]` |
| `cache_version` | `Optional[str]` |
| `cache_serialize` | `Optional[bool]` |
| `shared_memory` | `Optional[Union[L[True], str]]` |
| `pod_template` | `Optional[PodTemplate]` |
| `resources` | `Optional[Resources]` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| bindings |  |  |
| flyte_entity |  |  |
| id |  |  |
| metadata |  |  |
| name |  |  |
| outputs |  |  |
| run_entity |  |  |
| upstream_nodes |  |  |

## flytekit.core.node_creation.PythonTask

Base Class for all Tasks with a Python native ``Interface``. This should be directly used for task types, that do
not have a python function to be executed. Otherwise refer to :py:class:`flytekit.PythonFunctionTask`.


```python
def PythonTask(
    task_type: str,
    name: str,
    task_config: typing.Optional[~T],
    interface: typing.Optional[flytekit.core.interface.Interface],
    environment: typing.Optional[typing.Dict[str, str]],
    disable_deck: typing.Optional[bool],
    enable_deck: typing.Optional[bool],
    deck_fields: typing.Optional[typing.Tuple[flytekit.deck.deck.DeckField, ...]],
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `task_type` | `str` |
| `name` | `str` |
| `task_config` | `typing.Optional[~T]` |
| `interface` | `typing.Optional[flytekit.core.interface.Interface]` |
| `environment` | `typing.Optional[typing.Dict[str, str]]` |
| `disable_deck` | `typing.Optional[bool]` |
| `enable_deck` | `typing.Optional[bool]` |
| `deck_fields` | `typing.Optional[typing.Tuple[flytekit.deck.deck.DeckField, ...]]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | Generates a node that encapsulates this task in a workflow definition |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition |
| [`dispatch_execute()`](#dispatch_execute) | This method translates Flyte's Type system based input values and invokes the actual call to the executor |
| [`execute()`](#execute) | This method will be invoked to execute the task |
| [`find_lhs()`](#find_lhs) | None |
| [`get_config()`](#get_config) | Returns the task config as a serializable dictionary |
| [`get_container()`](#get_container) | Returns the container definition (if any) that is used to run the task on hosted Flyte |
| [`get_custom()`](#get_custom) | Return additional plugin-specific custom data (if any) as a serializable dictionary |
| [`get_extended_resources()`](#get_extended_resources) | Returns the extended resources to allocate to the task on hosted Flyte |
| [`get_input_types()`](#get_input_types) | Returns the names and python types as a dictionary for the inputs of this task |
| [`get_k8s_pod()`](#get_k8s_pod) | Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte |
| [`get_sql()`](#get_sql) | Returns the Sql definition (if any) that is used to run the task on hosted Flyte |
| [`get_type_for_input_var()`](#get_type_for_input_var) | Returns the python type for an input variable by name |
| [`get_type_for_output_var()`](#get_type_for_output_var) | Returns the python type for the specified output variable by name |
| [`local_execute()`](#local_execute) | This function is used only in the local execution path and is responsible for calling dispatch execute |
| [`local_execution_mode()`](#local_execution_mode) | None |
| [`post_execute()`](#post_execute) | Post execute is called after the execution has completed, with the user_params and can be used to clean-up, |
| [`pre_execute()`](#pre_execute) | This is the method that will be invoked directly before executing the task method and before all the inputs |
| [`sandbox_execute()`](#sandbox_execute) | Call dispatch_execute, in the context of a local sandbox execution |


#### compile()

```python
def compile(
    ctx: flytekit.core.context_manager.FlyteContext,
    args,
    kwargs,
):
```
Generates a node that encapsulates this task in a workflow definition.


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


#### dispatch_execute()

```python
def dispatch_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
):
```
This method translates Flyte's Type system based input values and invokes the actual call to the executor
This method is also invoked during runtime.

* ``VoidPromise`` is returned in the case when the task itself declares no outputs.
* ``Literal Map`` is returned when the task returns either one more outputs in the declaration. Individual outputs
may be none
* ``DynamicJobSpec`` is returned when a dynamic workflow is executed


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

#### execute()

```python
def execute(
    kwargs,
):
```
This method will be invoked to execute the task.


| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### find_lhs()

```python
def find_lhs()
```
#### get_config()

```python
def get_config(
    settings: flytekit.configuration.SerializationSettings,
):
```
Returns the task config as a serializable dictionary. This task config consists of metadata about the custom
defined for this task.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_container()

```python
def get_container(
    settings: flytekit.configuration.SerializationSettings,
):
```
Returns the container definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_custom()

```python
def get_custom(
    settings: flytekit.configuration.SerializationSettings,
):
```
Return additional plugin-specific custom data (if any) as a serializable dictionary.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_extended_resources()

```python
def get_extended_resources(
    settings: flytekit.configuration.SerializationSettings,
):
```
Returns the extended resources to allocate to the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_input_types()

```python
def get_input_types()
```
Returns the names and python types as a dictionary for the inputs of this task.


#### get_k8s_pod()

```python
def get_k8s_pod(
    settings: flytekit.configuration.SerializationSettings,
):
```
Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_sql()

```python
def get_sql(
    settings: flytekit.configuration.SerializationSettings,
):
```
Returns the Sql definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_type_for_input_var()

```python
def get_type_for_input_var(
    k: str,
    v: typing.Any,
):
```
Returns the python type for an input variable by name.


| Parameter | Type |
|-|-|
| `k` | `str` |
| `v` | `typing.Any` |

#### get_type_for_output_var()

```python
def get_type_for_output_var(
    k: str,
    v: typing.Any,
):
```
Returns the python type for the specified output variable by name.


| Parameter | Type |
|-|-|
| `k` | `str` |
| `v` | `typing.Any` |

#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
):
```
This function is used only in the local execution path and is responsible for calling dispatch execute.
Use this function when calling a task with native values (or Promises containing Flyte literals derived from
Python native values).


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
#### post_execute()

```python
def post_execute(
    user_params: typing.Optional[flytekit.core.context_manager.ExecutionParameters],
    rval: typing.Any,
):
```
Post execute is called after the execution has completed, with the user_params and can be used to clean-up,
or alter the outputs to match the intended tasks outputs. If not overridden, then this function is a No-op



| Parameter | Type |
|-|-|
| `user_params` | `typing.Optional[flytekit.core.context_manager.ExecutionParameters]` |
| `rval` | `typing.Any` |

#### pre_execute()

```python
def pre_execute(
    user_params: typing.Optional[flytekit.core.context_manager.ExecutionParameters],
):
```
This is the method that will be invoked directly before executing the task method and before all the inputs
are converted. One particular case where this is useful is if the context is to be modified for the user process
to get some user space parameters. This also ensures that things like SparkSession are already correctly
setup before the type transformers are called

This should return either the same context of the mutated context


| Parameter | Type |
|-|-|
| `user_params` | `typing.Optional[flytekit.core.context_manager.ExecutionParameters]` |

#### sandbox_execute()

```python
def sandbox_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
):
```
Call dispatch_execute, in the context of a local sandbox execution. Not invoked during runtime.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

### Properties

| Property | Type | Description |
|-|-|-|
| deck_fields |  |  |
| disable_deck |  |  |
| docs |  |  |
| enable_deck |  |  |
| environment |  |  |
| instantiated_in |  |  |
| interface |  |  |
| lhs |  |  |
| location |  |  |
| metadata |  |  |
| name |  |  |
| python_interface |  |  |
| security_context |  |  |
| task_config |  |  |
| task_type |  |  |
| task_type_version |  |  |

## flytekit.core.node_creation.VoidPromise

This object is returned for tasks that do not return any outputs (declared interface is empty)
VoidPromise cannot be interacted with and does not allow comparisons or any operations


```python
def VoidPromise(
    task_name: str,
    ref: Optional[NodeOutput],
):
```
| Parameter | Type |
|-|-|
| `task_name` | `str` |
| `ref` | `Optional[NodeOutput]` |

### Methods

| Method | Description |
|-|-|
| [`runs_before()`](#runs_before) | This is a placeholder and should do nothing |
| [`with_overrides()`](#with_overrides) | None |


#### runs_before()

```python
def runs_before(
    args,
    kwargs,
):
```
This is a placeholder and should do nothing. It is only here to enable local execution of workflows
where a task returns nothing.


| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### with_overrides()

```python
def with_overrides(
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| ref |  |  |
| task_name |  |  |

## flytekit.core.node_creation.WorkflowBase

```python
def WorkflowBase(
    name: str,
    workflow_metadata: WorkflowMetadata,
    workflow_metadata_defaults: WorkflowMetadataDefaults,
    python_interface: Interface,
    on_failure: Optional[Union[WorkflowBase, Task]],
    docs: Optional[Documentation],
    default_options: Optional[Options],
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `workflow_metadata` | `WorkflowMetadata` |
| `workflow_metadata_defaults` | `WorkflowMetadataDefaults` |
| `python_interface` | `Interface` |
| `on_failure` | `Optional[Union[WorkflowBase, Task]]` |
| `docs` | `Optional[Documentation]` |
| `default_options` | `Optional[Options]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | None |
| [`construct_node_metadata()`](#construct_node_metadata) | None |
| [`execute()`](#execute) | None |
| [`local_execute()`](#local_execute) | None |
| [`local_execution_mode()`](#local_execution_mode) | None |


#### compile()

```python
def compile(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
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
    ctx: FlyteContext,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
### Properties

| Property | Type | Description |
|-|-|-|
| default_options |  |  |
| docs |  |  |
| failure_node |  |  |
| interface |  |  |
| name |  |  |
| nodes |  |  |
| on_failure |  |  |
| output_bindings |  |  |
| python_interface |  |  |
| short_name |  |  |
| workflow_metadata |  |  |
| workflow_metadata_defaults |  |  |

