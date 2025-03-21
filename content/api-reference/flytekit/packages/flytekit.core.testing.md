---
title: flytekit.core.testing
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.testing

## Directory

### Classes

| Class | Description |
|-|-|
| [`MagicMock`](.././flytekit.core.testing#flytekitcoretestingmagicmock) | MagicMock is a subclass of Mock with default implementations. |
| [`PythonTask`](.././flytekit.core.testing#flytekitcoretestingpythontask) | Base Class for all Tasks with a Python native ``Interface``. |
| [`ReferenceEntity`](.././flytekit.core.testing#flytekitcoretestingreferenceentity) | None. |
| [`WorkflowBase`](.././flytekit.core.testing#flytekitcoretestingworkflowbase) | None. |

## flytekit.core.testing.MagicMock

MagicMock is a subclass of Mock with default implementations
of most of the magic methods. You can use MagicMock without having to
configure the magic methods yourself.

If you use the `spec` or `spec_set` arguments then *only* magic
methods that exist in the spec will be created.

Attributes and the return value of a `MagicMock` will also be `MagicMocks`.


```python
def MagicMock(
    args,
    kw,
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kw` |  |

### Methods

| Method | Description |
|-|-|
| [`assert_any_call()`](#assert_any_call) | assert the mock has been called with the specified arguments |
| [`assert_called()`](#assert_called) | assert that the mock was called at least once |
| [`assert_called_once()`](#assert_called_once) | assert that the mock was called only once |
| [`assert_called_once_with()`](#assert_called_once_with) | assert that the mock was called exactly once and that that call was |
| [`assert_called_with()`](#assert_called_with) | assert that the last call was made with the specified arguments |
| [`assert_has_calls()`](#assert_has_calls) | assert the mock has been called with the specified calls |
| [`assert_not_called()`](#assert_not_called) | assert that the mock was never called |
| [`attach_mock()`](#attach_mock) | Attach a mock as an attribute of this one, replacing its name and |
| [`configure_mock()`](#configure_mock) | Set attributes on the mock through keyword arguments |
| [`mock_add_spec()`](#mock_add_spec) | Add a spec to a mock |
| [`reset_mock()`](#reset_mock) | Restore the mock object to its initial state |


#### assert_any_call()

```python
def assert_any_call(
    args,
    kwargs,
):
```
assert the mock has been called with the specified arguments.

The assert passes if the mock has *ever* been called, unlike
`assert_called_with` and `assert_called_once_with` that only pass if
the call is the most recent one.


| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### assert_called()

```python
def assert_called()
```
assert that the mock was called at least once



#### assert_called_once()

```python
def assert_called_once()
```
assert that the mock was called only once.



#### assert_called_once_with()

```python
def assert_called_once_with(
    args,
    kwargs,
):
```
assert that the mock was called exactly once and that that call was
with the specified arguments.


| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### assert_called_with()

```python
def assert_called_with(
    args,
    kwargs,
):
```
assert that the last call was made with the specified arguments.

Raises an AssertionError if the args and keyword args passed in are
different to the last call to the mock.


| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### assert_has_calls()

```python
def assert_has_calls(
    calls,
    any_order,
):
```
assert the mock has been called with the specified calls.
The `mock_calls` list is checked for the calls.

If `any_order` is False (the default) then the calls must be
sequential. There can be extra calls before or after the
specified calls.

If `any_order` is True then the calls can be in any order, but
they must all appear in `mock_calls`.


| Parameter | Type |
|-|-|
| `calls` |  |
| `any_order` |  |

#### assert_not_called()

```python
def assert_not_called()
```
assert that the mock was never called.



#### attach_mock()

```python
def attach_mock(
    mock,
    attribute,
):
```
Attach a mock as an attribute of this one, replacing its name and
parent. Calls to the attached mock will be recorded in the
`method_calls` and `mock_calls` attributes of this one.


| Parameter | Type |
|-|-|
| `mock` |  |
| `attribute` |  |

#### configure_mock()

```python
def configure_mock(
    kwargs,
):
```
Set attributes on the mock through keyword arguments.

Attributes plus return values and side effects can be set on child
mocks using standard dot notation and unpacking a dictionary in the
method call:

>>> attrs = {'method.return_value': 3, 'other.side_effect': KeyError}
>>> mock.configure_mock(**attrs)


| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### mock_add_spec()

```python
def mock_add_spec(
    spec,
    spec_set,
):
```
Add a spec to a mock. `spec` can either be an object or a
list of strings. Only attributes on the `spec` can be fetched as
attributes from the mock.

If `spec_set` is True then only attributes on the spec can be set.


| Parameter | Type |
|-|-|
| `spec` |  |
| `spec_set` |  |

#### reset_mock()

```python
def reset_mock(
    args,
    return_value: bool,
    kwargs,
):
```
Restore the mock object to its initial state.


| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `return_value` | `bool` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| call_args |  |  |
| call_args_list |  |  |
| call_count |  |  |
| called |  |  |
| mock_calls |  |  |
| return_value |  |  |
| side_effect |  |  |

## flytekit.core.testing.PythonTask

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

## flytekit.core.testing.ReferenceEntity

```python
def ReferenceEntity(
    reference: typing.Union[flytekit.core.reference_entity.WorkflowReference, flytekit.core.reference_entity.TaskReference, flytekit.core.reference_entity.LaunchPlanReference],
    inputs: typing.Dict[str, typing.Type],
    outputs: typing.Dict[str, typing.Type],
):
```
| Parameter | Type |
|-|-|
| `reference` | `typing.Union[flytekit.core.reference_entity.WorkflowReference, flytekit.core.reference_entity.TaskReference, flytekit.core.reference_entity.LaunchPlanReference]` |
| `inputs` | `typing.Dict[str, typing.Type]` |
| `outputs` | `typing.Dict[str, typing.Type]` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | None |
| [`construct_node_metadata()`](#construct_node_metadata) | None |
| [`execute()`](#execute) | None |
| [`local_execute()`](#local_execute) | Please see the local_execute comments in the main task |
| [`local_execution_mode()`](#local_execution_mode) | None |
| [`unwrap_literal_map_and_execute()`](#unwrap_literal_map_and_execute) | Please see the implementation of the dispatch_execute function in the real task |


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
):
```
Please see the implementation of the dispatch_execute function in the real task.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

### Properties

| Property | Type | Description |
|-|-|-|
| id |  |  |
| interface |  |  |
| name |  |  |
| python_interface |  |  |
| reference |  |  |

## flytekit.core.testing.WorkflowBase

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

