---
title: flytekit.core.reference
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.reference

## Directory

### Classes

| Class | Description |
|-|-|
| [`ReferenceLaunchPlan`](.././flytekit.core.reference#flytekitcorereferencereferencelaunchplan) | A reference launch plan serves as a pointer to a Launch Plan that already exists on your Flyte installation. |
| [`ReferenceTask`](.././flytekit.core.reference#flytekitcorereferencereferencetask) | This is a reference task, the body of the function passed in through the constructor will never be used, only the. |
| [`ReferenceWorkflow`](.././flytekit.core.reference#flytekitcorereferencereferenceworkflow) | A reference workflow is a pointer to a workflow that already exists on your Flyte installation. |

### Errors

| Exception | Description |
|-|-|
| [`FlyteValidationException`](.././flytekit.core.reference#flytekitcorereferenceflytevalidationexception) | Assertion failed. |

### Methods

| Method | Description |
|-|-|
| [`get_reference_entity()`](#get_reference_entity) | See the documentation for :py:class:`flytekit. |


### Variables

| Property | Type | Description |
|-|-|-|
| `annotations` | `_Feature` |  |

## Methods

#### get_reference_entity()

```python
def get_reference_entity(
    resource_type: int,
    project: str,
    domain: str,
    name: str,
    version: str,
    inputs: Dict[str, Type],
    outputs: Dict[str, Type],
)
```
See the documentation for :py:class:`flytekit.reference_task` and :py:class:`flytekit.reference_workflow` as well.

This function is the general form of the two aforementioned functions. It's better for programmatic usage, as
the interface is passed in as arguments instead of analyzed from type annotations.

.. literalinclude:: ../../../tests/flytekit/unit/core/test_references.py
:start-after: # docs_ref_start
:end-before: # docs_ref_end
:language: python
:dedent: 4



| Parameter | Type |
|-|-|
| `resource_type` | `int` |
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |
| `inputs` | `Dict[str, Type]` |
| `outputs` | `Dict[str, Type]` |

## flytekit.core.reference.FlyteValidationException

Assertion failed.


```python
class FlyteValidationException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.core.reference.ReferenceLaunchPlan

A reference launch plan serves as a pointer to a Launch Plan that already exists on your Flyte installation. This
object will not initiate a network call to Admin, which is why the user is asked to provide the expected interface.
If at registration time the interface provided causes an issue with compilation, an error will be returned.


```python
class ReferenceLaunchPlan(
    project: str,
    domain: str,
    name: str,
    version: str,
    inputs: Dict[str, Type],
    outputs: Dict[str, Type],
)
```
| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |
| `inputs` | `Dict[str, Type]` |
| `outputs` | `Dict[str, Type]` |

### Methods

| Method | Description |
|-|-|
| [`clone_with()`](#clone_with) |  |
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`create()`](#create) |  |
| [`execute()`](#execute) |  |
| [`get_default_launch_plan()`](#get_default_launch_plan) | Users should probably call the get_or_create function defined below instead. |
| [`get_or_create()`](#get_or_create) | This function offers a friendlier interface for creating launch plans. |
| [`local_execute()`](#local_execute) | Please see the local_execute comments in the main task. |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`unwrap_literal_map_and_execute()`](#unwrap_literal_map_and_execute) | Please see the implementation of the dispatch_execute function in the real task. |


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

#### execute()

```python
def execute(
    kwargs,
) -> typing.Any
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

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

#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, NoneType]
```
Please see the local_execute comments in the main task.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
#### unwrap_literal_map_and_execute()

```python
def unwrap_literal_map_and_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
) -> flytekit.models.literals.LiteralMap
```
Please see the implementation of the dispatch_execute function in the real task.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

### Properties

| Property | Type | Description |
|-|-|-|
| `annotations` |  |  |
| `fixed_inputs` |  |  |
| `id` |  |  |
| `interface` |  |  |
| `labels` |  |  |
| `max_parallelism` |  |  |
| `name` |  |  |
| `notifications` |  |  |
| `overwrite_cache` |  |  |
| `parameters` |  |  |
| `python_interface` |  |  |
| `raw_output_data_config` |  |  |
| `reference` |  |  |
| `saved_inputs` |  |  |
| `schedule` |  |  |
| `security_context` |  |  |
| `should_auto_activate` |  |  |
| `trigger` |  |  |
| `workflow` |  |  |

## flytekit.core.reference.ReferenceTask

This is a reference task, the body of the function passed in through the constructor will never be used, only the
signature of the function will be. The signature should also match the signature of the task you're referencing,
as stored by Flyte Admin, if not, workflows using this will break upon compilation.


```python
class ReferenceTask(
    project: str,
    domain: str,
    name: str,
    version: str,
    inputs: Dict[str, type],
    outputs: Dict[str, Type],
)
```
| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |
| `inputs` | `Dict[str, type]` |
| `outputs` | `Dict[str, Type]` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`dispatch_execute()`](#dispatch_execute) | This method translates Flyte's Type system based input values and invokes the actual call to the executor. |
| [`execute()`](#execute) |  |
| [`find_lhs()`](#find_lhs) |  |
| [`get_config()`](#get_config) | Returns the task config as a serializable dictionary. |
| [`get_container()`](#get_container) | Returns the container definition (if any) that is used to run the task on hosted Flyte. |
| [`get_custom()`](#get_custom) | Return additional plugin-specific custom data (if any) as a serializable dictionary. |
| [`get_extended_resources()`](#get_extended_resources) | Returns the extended resources to allocate to the task on hosted Flyte. |
| [`get_input_types()`](#get_input_types) | Returns the names and python types as a dictionary for the inputs of this task. |
| [`get_k8s_pod()`](#get_k8s_pod) | Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte. |
| [`get_sql()`](#get_sql) | Returns the Sql definition (if any) that is used to run the task on hosted Flyte. |
| [`get_type_for_input_var()`](#get_type_for_input_var) | Returns the python type for an input variable by name. |
| [`get_type_for_output_var()`](#get_type_for_output_var) | Returns the python type for the specified output variable by name. |
| [`local_execute()`](#local_execute) | Please see the local_execute comments in the main task. |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`post_execute()`](#post_execute) | Post execute is called after the execution has completed, with the user_params and can be used to clean-up,. |
| [`pre_execute()`](#pre_execute) | This is the method that will be invoked directly before executing the task method and before all the inputs. |
| [`sandbox_execute()`](#sandbox_execute) | Call dispatch_execute, in the context of a local sandbox execution. |
| [`unwrap_literal_map_and_execute()`](#unwrap_literal_map_and_execute) | Please see the implementation of the dispatch_execute function in the real task. |


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
#### dispatch_execute()

```python
def dispatch_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
) -> typing.Union[flytekit.models.literals.LiteralMap, flytekit.models.dynamic_job.DynamicJobSpec, typing.Coroutine]
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
) -> typing.Any
```
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
) -> typing.Optional[typing.Dict[str, str]]
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
) -> typing.Optional[flytekit.models.task.Container]
```
Returns the container definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_custom()

```python
def get_custom(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[typing.Dict[str, typing.Any]]
```
Return additional plugin-specific custom data (if any) as a serializable dictionary.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_extended_resources()

```python
def get_extended_resources(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flyteidl.core.tasks_pb2.ExtendedResources]
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
) -> typing.Optional[flytekit.models.task.K8sPod]
```
Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_sql()

```python
def get_sql(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flytekit.models.task.Sql]
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
) -> typing.Type[typing.Any]
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
) -> typing.Type[typing.Any]
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
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, NoneType]
```
Please see the local_execute comments in the main task.


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
) -> typing.Any
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
) -> typing.Optional[flytekit.core.context_manager.ExecutionParameters]
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
) -> flytekit.models.literals.LiteralMap
```
Call dispatch_execute, in the context of a local sandbox execution. Not invoked during runtime.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

#### unwrap_literal_map_and_execute()

```python
def unwrap_literal_map_and_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
) -> flytekit.models.literals.LiteralMap
```
Please see the implementation of the dispatch_execute function in the real task.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

### Properties

| Property | Type | Description |
|-|-|-|
| `deck_fields` |  | {{< multiline >}}If not empty, this task will output deck html file for the specified decks
{{< /multiline >}} |
| `disable_deck` |  | {{< multiline >}}If true, this task will not output deck html file
{{< /multiline >}} |
| `docs` |  |  |
| `enable_deck` |  | {{< multiline >}}If true, this task will output deck html file
{{< /multiline >}} |
| `environment` |  | {{< multiline >}}Any environment variables that supplied during the execution of the task.
{{< /multiline >}} |
| `id` |  |  |
| `instantiated_in` |  |  |
| `interface` |  |  |
| `lhs` |  |  |
| `location` |  |  |
| `metadata` |  |  |
| `name` |  |  |
| `python_interface` |  |  |
| `reference` |  |  |
| `security_context` |  |  |
| `task_config` |  | {{< multiline >}}Returns the user-specified task config which is used for plugin-specific handling of the task.
{{< /multiline >}} |
| `task_type` |  |  |
| `task_type_version` |  |  |

## flytekit.core.reference.ReferenceWorkflow

A reference workflow is a pointer to a workflow that already exists on your Flyte installation. This
object will not initiate a network call to Admin, which is why the user is asked to provide the expected interface.
If at registration time the interface provided causes an issue with compilation, an error will be returned.


```python
class ReferenceWorkflow(
    project: str,
    domain: str,
    name: str,
    version: str,
    inputs: Dict[str, Type],
    outputs: Dict[str, Type],
)
```
| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |
| `inputs` | `Dict[str, Type]` |
| `outputs` | `Dict[str, Type]` |

### Methods

| Method | Description |
|-|-|
| [`add()`](#add) |  |
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`execute()`](#execute) |  |
| [`find_lhs()`](#find_lhs) |  |
| [`get_all_tasks()`](#get_all_tasks) | Future proof method. |
| [`load_task()`](#load_task) | Given the set of identifier keys, should return one Python Task or raise an error if not found. |
| [`loader_args()`](#loader_args) | This is responsible for turning an instance of a task into args that the load_task function can reconstitute. |
| [`local_execute()`](#local_execute) | Please see the local_execute comments in the main task. |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`task_name()`](#task_name) | Overridable function that can optionally return a custom name for a given task. |
| [`unwrap_literal_map_and_execute()`](#unwrap_literal_map_and_execute) | Please see the implementation of the dispatch_execute function in the real task. |


#### add()

```python
def add(
    t: flytekit.core.python_auto_container.PythonAutoContainerTask,
)
```
| Parameter | Type |
|-|-|
| `t` | `flytekit.core.python_auto_container.PythonAutoContainerTask` |

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
#### execute()

```python
def execute(
    kwargs,
) -> typing.Any
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### find_lhs()

```python
def find_lhs()
```
#### get_all_tasks()

```python
def get_all_tasks()
```
Future proof method. Just making it easy to access all tasks (Not required today as we auto register them)


#### load_task()

```python
def load_task(
    loader_args: typing.List[str],
) -> flytekit.core.python_auto_container.PythonAutoContainerTask
```
Given the set of identifier keys, should return one Python Task or raise an error if not found


| Parameter | Type |
|-|-|
| `loader_args` | `typing.List[str]` |

#### loader_args()

```python
def loader_args(
    settings: flytekit.configuration.SerializationSettings,
    t: flytekit.core.python_auto_container.PythonAutoContainerTask,
) -> typing.List[str]
```
This is responsible for turning an instance of a task into args that the load_task function can reconstitute.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |
| `t` | `flytekit.core.python_auto_container.PythonAutoContainerTask` |

#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, NoneType]
```
Please see the local_execute comments in the main task.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
#### task_name()

```python
def task_name(
    t: PythonAutoContainerTask,
) -> str
```
Overridable function that can optionally return a custom name for a given task


| Parameter | Type |
|-|-|
| `t` | `PythonAutoContainerTask` |

#### unwrap_literal_map_and_execute()

```python
def unwrap_literal_map_and_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
) -> flytekit.models.literals.LiteralMap
```
Please see the implementation of the dispatch_execute function in the real task.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

### Properties

| Property | Type | Description |
|-|-|-|
| `default_options` |  |  |
| `docs` |  |  |
| `failure_node` |  |  |
| `function` |  |  |
| `id` |  |  |
| `instantiated_in` |  |  |
| `interface` |  |  |
| `lhs` |  |  |
| `location` |  |  |
| `name` |  |  |
| `nodes` |  |  |
| `on_failure` |  |  |
| `output_bindings` |  |  |
| `python_interface` |  |  |
| `reference` |  |  |
| `short_name` |  |  |
| `workflow_metadata` |  |  |
| `workflow_metadata_defaults` |  |  |

