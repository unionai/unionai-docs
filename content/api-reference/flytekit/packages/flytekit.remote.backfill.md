---
title: flytekit.remote.backfill
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.remote.backfill

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteLaunchPlan`](.././flytekit.remote.backfill#flytekitremotebackfillflytelaunchplan) | A class encapsulating a remote Flyte launch plan. |
| [`ImperativeWorkflow`](.././flytekit.remote.backfill#flytekitremotebackfillimperativeworkflow) | An imperative workflow is a programmatic analogue to the typical ``@workflow`` function-based workflow and is. |
| [`LaunchPlan`](.././flytekit.remote.backfill#flytekitremotebackfilllaunchplan) | Launch Plans are one of the core constructs of Flyte. |
| [`WorkflowBase`](.././flytekit.remote.backfill#flytekitremotebackfillworkflowbase) |  |
| [`WorkflowFailurePolicy`](.././flytekit.remote.backfill#flytekitremotebackfillworkflowfailurepolicy) | Defines the behavior for a workflow execution in the case of an observed node execution failure. |
| [`croniter`](.././flytekit.remote.backfill#flytekitremotebackfillcroniter) |  |
| [`datetime`](.././flytekit.remote.backfill#flytekitremotebackfilldatetime) | datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]]). |
| [`timedelta`](.././flytekit.remote.backfill#flytekitremotebackfilltimedelta) | Difference between two datetime values. |

### Methods

| Method | Description |
|-|-|
| [`create_backfill_workflow()`](#create_backfill_workflow) | Generates a new imperative workflow for the launchplan that can be used to backfill the given launchplan. |


## Methods

#### create_backfill_workflow()

```python
def create_backfill_workflow(
    start_date: datetime.datetime,
    end_date: datetime.datetime,
    for_lp: typing.Union[flytekit.core.launch_plan.LaunchPlan, flytekit.remote.entities.FlyteLaunchPlan],
    parallel: bool,
    per_node_timeout: datetime.timedelta,
    per_node_retries: int,
    failure_policy: typing.Optional[flytekit.core.workflow.WorkflowFailurePolicy],
) -> typing.Tuple[flytekit.core.workflow.WorkflowBase, datetime.datetime, datetime.datetime]
```
Generates a new imperative workflow for the launchplan that can be used to backfill the given launchplan.
This can only be used to generate  backfilling workflow only for schedulable launchplans

the Backfill plan is generated as (start_date - exclusive, end_date inclusive)

.. code-block:: python
:caption: Correct usage for dates example

lp = Launchplan.get_or_create(...)
start_date = datetime.datetime(2023, 1, 1)
end_date =  start_date + datetime.timedelta(days=10)
wf = create_backfill_workflow(start_date, end_date, for_lp=lp)


.. code-block:: python
:caption: Incorrect date example

wf = create_backfill_workflow(end_date, start_date, for_lp=lp) # end_date is before start_date
# OR
wf = create_backfill_workflow(start_date, start_date, for_lp=lp) # start and end date are same




| Parameter | Type |
|-|-|
| `start_date` | `datetime.datetime` |
| `end_date` | `datetime.datetime` |
| `for_lp` | `typing.Union[flytekit.core.launch_plan.LaunchPlan, flytekit.remote.entities.FlyteLaunchPlan]` |
| `parallel` | `bool` |
| `per_node_timeout` | `datetime.timedelta` |
| `per_node_retries` | `int` |
| `failure_policy` | `typing.Optional[flytekit.core.workflow.WorkflowFailurePolicy]` |

## flytekit.remote.backfill.FlyteLaunchPlan

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

## flytekit.remote.backfill.ImperativeWorkflow

An imperative workflow is a programmatic analogue to the typical ``@workflow`` function-based workflow and is
better suited to programmatic applications.

Assuming you have some tasks like so

.. literalinclude:: ../../../tests/flytekit/unit/core/test_imperative.py
:start-after: # docs_tasks_start
:end-before: # docs_tasks_end
:language: python
:dedent: 4

You could create a workflow imperatively like so

.. literalinclude:: ../../../tests/flytekit/unit/core/test_imperative.py
:start-after: # docs_start
:end-before: # docs_end
:language: python
:dedent: 4

This workflow would be identical on the back-end to

.. literalinclude:: ../../../tests/flytekit/unit/core/test_imperative.py
:start-after: # docs_equivalent_start
:end-before: # docs_equivalent_end
:language: python
:dedent: 4

Note that the only reason we need the ``NamedTuple`` is so we can name the output the same thing as in the
imperative example. The imperative paradigm makes the naming of workflow outputs easier, but this isn't a big
deal in function-workflows because names tend to not be necessary.


```python
class ImperativeWorkflow(
    name: str,
    failure_policy: Optional[WorkflowFailurePolicy],
    interruptible: bool,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `failure_policy` | `Optional[WorkflowFailurePolicy]` |
| `interruptible` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`add_entity()`](#add_entity) | Anytime you add an entity, all the inputs to the entity must be bound. |
| [`add_launch_plan()`](#add_launch_plan) |  |
| [`add_on_failure_handler()`](#add_on_failure_handler) | This is a special function that mimics the add_entity function, but this is only used. |
| [`add_subwf()`](#add_subwf) |  |
| [`add_task()`](#add_task) |  |
| [`add_workflow_input()`](#add_workflow_input) | Adds an input to the workflow. |
| [`add_workflow_output()`](#add_workflow_output) | Add an output with the given name from the given node output. |
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`create_conditional()`](#create_conditional) |  |
| [`execute()`](#execute) | Called by local_execute. |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`ready()`](#ready) | This function returns whether or not the workflow is in a ready state, which means. |


#### add_entity()

```python
def add_entity(
    entity: Union[PythonTask, _annotated_launch_plan.LaunchPlan, WorkflowBase],
    kwargs,
) -> Node
```
Anytime you add an entity, all the inputs to the entity must be bound.


| Parameter | Type |
|-|-|
| `entity` | `Union[PythonTask, _annotated_launch_plan.LaunchPlan, WorkflowBase]` |
| `kwargs` | ``**kwargs`` |

#### add_launch_plan()

```python
def add_launch_plan(
    launch_plan: _annotated_launch_plan.LaunchPlan,
    kwargs,
) -> Node
```
| Parameter | Type |
|-|-|
| `launch_plan` | `_annotated_launch_plan.LaunchPlan` |
| `kwargs` | ``**kwargs`` |

#### add_on_failure_handler()

```python
def add_on_failure_handler(
    entity,
)
```
This is a special function that mimics the add_entity function, but this is only used
to add the failure node. Failure nodes are special because we don't want
them to be part of the main workflow.


| Parameter | Type |
|-|-|
| `entity` |  |

#### add_subwf()

```python
def add_subwf(
    sub_wf: WorkflowBase,
    kwargs,
) -> Node
```
| Parameter | Type |
|-|-|
| `sub_wf` | `WorkflowBase` |
| `kwargs` | ``**kwargs`` |

#### add_task()

```python
def add_task(
    task: PythonTask,
    kwargs,
) -> Node
```
| Parameter | Type |
|-|-|
| `task` | `PythonTask` |
| `kwargs` | ``**kwargs`` |

#### add_workflow_input()

```python
def add_workflow_input(
    input_name: str,
    python_type: Type,
) -> Promise
```
Adds an input to the workflow.


| Parameter | Type |
|-|-|
| `input_name` | `str` |
| `python_type` | `Type` |

#### add_workflow_output()

```python
def add_workflow_output(
    output_name: str,
    p: Union[Promise, List[Promise], Dict[str, Promise]],
    python_type: Optional[Type],
)
```
Add an output with the given name from the given node output.


| Parameter | Type |
|-|-|
| `output_name` | `str` |
| `p` | `Union[Promise, List[Promise], Dict[str, Promise]]` |
| `python_type` | `Optional[Type]` |

#### compile()

```python
def compile(
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
#### create_conditional()

```python
def create_conditional(
    name: str,
) -> ConditionalSection
```
| Parameter | Type |
|-|-|
| `name` | `str` |

#### execute()

```python
def execute(
    kwargs,
)
```
Called by local_execute. This function is how local execution for imperative workflows runs. Because when an
entity is added using the add_entity function, all inputs to that entity should've been already declared, we
can just iterate through the nodes in order and we shouldn't run into any dependency issues. That is, we force
the user to declare entities already in a topological sort. To keep track of outputs, we create a map to
start things off, filled in only with the workflow inputs (if any). As things are run, their outputs are stored
in this map.
After all nodes are run, we fill in workflow level outputs the same way as any other previous node.


| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### local_execute()

```python
def local_execute(
    ctx: FlyteContext,
    kwargs,
) -> Union[Tuple[Promise], Promise, VoidPromise, None]
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
#### ready()

```python
def ready()
```
This function returns whether or not the workflow is in a ready state, which means
* Has at least one node
* All workflow inputs are bound

These conditions assume that all nodes and workflow i/o changes were done with the functions above, which
do additional checking.


### Properties

| Property | Type | Description |
|-|-|-|
| `compilation_state` |  | {{< multiline >}}Compilation is done a bit at a time, one task or other entity call at a time. This is why this workflow
class has to keep track of its own compilation state.
{{< /multiline >}} |
| `default_options` |  |  |
| `docs` |  |  |
| `failure_node` |  |  |
| `inputs` |  | {{< multiline >}}This holds the input promises to the workflow. The nodes in these Promise objects should always point to
the global start node.
{{< /multiline >}} |
| `interface` |  |  |
| `name` |  |  |
| `nodes` |  |  |
| `on_failure` |  |  |
| `output_bindings` |  |  |
| `python_interface` |  |  |
| `short_name` |  |  |
| `workflow_metadata` |  |  |
| `workflow_metadata_defaults` |  |  |

## flytekit.remote.backfill.LaunchPlan

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
class LaunchPlan(
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
)
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
| [`clone_with()`](#clone_with) |  |
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`create()`](#create) |  |
| [`get_default_launch_plan()`](#get_default_launch_plan) | Users should probably call the get_or_create function defined below instead. |
| [`get_or_create()`](#get_or_create) | This function offers a friendlier interface for creating launch plans. |


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
) -> LaunchPlan
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
) -> LaunchPlan
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
) -> LaunchPlan
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
) -> LaunchPlan
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
| `annotations` |  |  |
| `fixed_inputs` |  |  |
| `interface` |  |  |
| `labels` |  |  |
| `max_parallelism` |  |  |
| `name` |  |  |
| `notifications` |  |  |
| `overwrite_cache` |  |  |
| `parameters` |  |  |
| `python_interface` |  |  |
| `raw_output_data_config` |  |  |
| `saved_inputs` |  |  |
| `schedule` |  |  |
| `security_context` |  |  |
| `should_auto_activate` |  |  |
| `trigger` |  |  |
| `workflow` |  |  |

## flytekit.remote.backfill.WorkflowBase

```python
class WorkflowBase(
    name: str,
    workflow_metadata: WorkflowMetadata,
    workflow_metadata_defaults: WorkflowMetadataDefaults,
    python_interface: Interface,
    on_failure: Optional[Union[WorkflowBase, Task]],
    docs: Optional[Documentation],
    default_options: Optional[Options],
    kwargs,
)
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
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`execute()`](#execute) |  |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |


#### compile()

```python
def compile(
    kwargs,
)
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
)
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### local_execute()

```python
def local_execute(
    ctx: FlyteContext,
    kwargs,
) -> Union[Tuple[Promise], Promise, VoidPromise, None]
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
| `default_options` |  |  |
| `docs` |  |  |
| `failure_node` |  |  |
| `interface` |  |  |
| `name` |  |  |
| `nodes` |  |  |
| `on_failure` |  |  |
| `output_bindings` |  |  |
| `python_interface` |  |  |
| `short_name` |  |  |
| `workflow_metadata` |  |  |
| `workflow_metadata_defaults` |  |  |

## flytekit.remote.backfill.WorkflowFailurePolicy

Defines the behavior for a workflow execution in the case of an observed node execution failure. By default, a
workflow execution will immediately enter a failed state if a component node fails.


## flytekit.remote.backfill.croniter

```python
class croniter(
    expr_format,
    start_time,
    ret_type,
    day_or,
    max_years_between_matches,
    is_prev,
    hash_id,
    implement_cron_bug,
    second_at_beginning,
    expand_from_start_time,
)
```
| Parameter | Type |
|-|-|
| `expr_format` |  |
| `start_time` |  |
| `ret_type` |  |
| `day_or` |  |
| `max_years_between_matches` |  |
| `is_prev` |  |
| `hash_id` |  |
| `implement_cron_bug` |  |
| `second_at_beginning` |  |
| `expand_from_start_time` |  |

### Methods

| Method | Description |
|-|-|
| [`all_next()`](#all_next) | Returns a generator yielding consecutive dates. |
| [`all_prev()`](#all_prev) | Returns a generator yielding previous dates. |
| [`datetime_to_timestamp()`](#datetime_to_timestamp) | Converts a `datetime` object `d` into a UNIX timestamp. |
| [`expand()`](#expand) | Expand a cron expression format into a noramlized format of. |
| [`get_current()`](#get_current) |  |
| [`get_next()`](#get_next) |  |
| [`get_prev()`](#get_prev) |  |
| [`is_leap()`](#is_leap) |  |
| [`is_valid()`](#is_valid) |  |
| [`iter()`](#iter) |  |
| [`match()`](#match) |  |
| [`match_range()`](#match_range) |  |
| [`next()`](#next) |  |
| [`set_current()`](#set_current) |  |
| [`timedelta_to_seconds()`](#timedelta_to_seconds) | Converts a 'datetime. |
| [`timestamp_to_datetime()`](#timestamp_to_datetime) | Converts a UNIX `timestamp` into a `datetime` object. |
| [`value_alias()`](#value_alias) |  |


#### all_next()

```python
def all_next(
    ret_type,
    start_time,
    update_current,
)
```
Returns a generator yielding consecutive dates.

May be used instead of an implicit call to __iter__ whenever a
non-default `ret_type` needs to be specified.


| Parameter | Type |
|-|-|
| `ret_type` |  |
| `start_time` |  |
| `update_current` |  |

#### all_prev()

```python
def all_prev(
    ret_type,
    start_time,
    update_current,
)
```
Returns a generator yielding previous dates.


| Parameter | Type |
|-|-|
| `ret_type` |  |
| `start_time` |  |
| `update_current` |  |

#### datetime_to_timestamp()

```python
def datetime_to_timestamp(
    d,
)
```
Converts a `datetime` object `d` into a UNIX timestamp.


| Parameter | Type |
|-|-|
| `d` |  |

#### expand()

```python
def expand(
    expr_format,
    hash_id,
    second_at_beginning,
    from_timestamp,
)
```
Expand a cron expression format into a noramlized format of
list[list[int | 'l' | '*']]. The first list representing each element
of the epxression, and each sub-list representing the allowed values
for that expression component.

A tuple is returned, the first value being the expanded epxression
list, and the second being a `nth_weekday_of_month` mapping.

Examples:

# Every minute
>>> croniter.expand('* * * * *')
([['*'], ['*'], ['*'], ['*'], ['*']], {})

# On the hour
>>> croniter.expand('0 0 * * *')
([[0], [0], ['*'], ['*'], ['*']], {})

# Hours 0-5 and 10 monday through friday
>>> croniter.expand('0-5,10 * * * mon-fri')
([[0, 1, 2, 3, 4, 5, 10], ['*'], ['*'], ['*'], [1, 2, 3, 4, 5]], {})

Note that some special values such as nth day of week are expanded to a
special mapping format for later processing:

# Every minute on the 3rd tuesday of the month
>>> croniter.expand('* * * * 2#3')
([['*'], ['*'], ['*'], ['*'], [2]], {2: {3}})

# Every hour on the last day of the month
>>> croniter.expand('0 * l * *')
([[0], ['*'], ['l'], ['*'], ['*']], {})

# On the hour every 15 seconds
>>> croniter.expand('0 0 * * * */15')
([[0], [0], ['*'], ['*'], ['*'], [0, 15, 30, 45]], {})


| Parameter | Type |
|-|-|
| `expr_format` |  |
| `hash_id` |  |
| `second_at_beginning` |  |
| `from_timestamp` |  |

#### get_current()

```python
def get_current(
    ret_type,
)
```
| Parameter | Type |
|-|-|
| `ret_type` |  |

#### get_next()

```python
def get_next(
    ret_type,
    start_time,
    update_current,
)
```
| Parameter | Type |
|-|-|
| `ret_type` |  |
| `start_time` |  |
| `update_current` |  |

#### get_prev()

```python
def get_prev(
    ret_type,
    start_time,
    update_current,
)
```
| Parameter | Type |
|-|-|
| `ret_type` |  |
| `start_time` |  |
| `update_current` |  |

#### is_leap()

```python
def is_leap(
    year,
)
```
| Parameter | Type |
|-|-|
| `year` |  |

#### is_valid()

```python
def is_valid(
    expression,
    hash_id,
    encoding,
    second_at_beginning,
)
```
| Parameter | Type |
|-|-|
| `expression` |  |
| `hash_id` |  |
| `encoding` |  |
| `second_at_beginning` |  |

#### iter()

```python
def iter(
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### match()

```python
def match(
    cron_expression,
    testdate,
    day_or,
    second_at_beginning,
)
```
| Parameter | Type |
|-|-|
| `cron_expression` |  |
| `testdate` |  |
| `day_or` |  |
| `second_at_beginning` |  |

#### match_range()

```python
def match_range(
    cron_expression,
    from_datetime,
    to_datetime,
    day_or,
    second_at_beginning,
)
```
| Parameter | Type |
|-|-|
| `cron_expression` |  |
| `from_datetime` |  |
| `to_datetime` |  |
| `day_or` |  |
| `second_at_beginning` |  |

#### next()

```python
def next(
    ret_type,
    start_time,
    is_prev,
    update_current,
)
```
| Parameter | Type |
|-|-|
| `ret_type` |  |
| `start_time` |  |
| `is_prev` |  |
| `update_current` |  |

#### set_current()

```python
def set_current(
    start_time,
    force,
)
```
| Parameter | Type |
|-|-|
| `start_time` |  |
| `force` |  |

#### timedelta_to_seconds()

```python
def timedelta_to_seconds(
    td,
)
```
Converts a 'datetime.timedelta' object `td` into seconds contained in
the duration.
Note: We cannot use `timedelta.total_seconds()` because this is not
supported by Python 2.6.


| Parameter | Type |
|-|-|
| `td` |  |

#### timestamp_to_datetime()

```python
def timestamp_to_datetime(
    timestamp,
    tzinfo,
)
```
Converts a UNIX `timestamp` into a `datetime` object.


| Parameter | Type |
|-|-|
| `timestamp` |  |
| `tzinfo` |  |

#### value_alias()

```python
def value_alias(
    val,
    field_index,
    len_expressions,
)
```
| Parameter | Type |
|-|-|
| `val` |  |
| `field_index` |  |
| `len_expressions` |  |

## flytekit.remote.backfill.datetime

datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])

The year, month and day arguments are required. tzinfo may be None, or an
instance of a tzinfo subclass. The remaining arguments may be ints.


## flytekit.remote.backfill.timedelta

Difference between two datetime values.

timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

All arguments are optional and default to 0.
Arguments may be integers or floats, and may be positive or negative.


