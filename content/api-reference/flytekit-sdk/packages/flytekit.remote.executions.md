---
title: flytekit.remote.executions
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.remote.executions

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteNodeExecution`](.././flytekit.remote.executions#flytekitremoteexecutionsflytenodeexecution) | A class encapsulating a node execution being run on a Flyte remote backend. |
| [`FlyteTask`](.././flytekit.remote.executions#flytekitremoteexecutionsflytetask) | A class encapsulating a remote Flyte task. |
| [`FlyteTaskExecution`](.././flytekit.remote.executions#flytekitremoteexecutionsflytetaskexecution) | A class encapsulating a task execution being run on a Flyte remote backend. |
| [`FlyteWorkflow`](.././flytekit.remote.executions#flytekitremoteexecutionsflyteworkflow) | A class encapsulating a remote Flyte workflow. |
| [`FlyteWorkflowExecution`](.././flytekit.remote.executions#flytekitremoteexecutionsflyteworkflowexecution) | A class encapsulating a workflow execution being run on a Flyte remote backend. |
| [`LiteralsResolver`](.././flytekit.remote.executions#flytekitremoteexecutionsliteralsresolver) | LiteralsResolver is a helper class meant primarily for use with the FlyteRemote experience or any other situation. |
| [`RemoteExecutionBase`](.././flytekit.remote.executions#flytekitremoteexecutionsremoteexecutionbase) | None. |
| [`TypedInterface`](.././flytekit.remote.executions#flytekitremoteexecutionstypedinterface) | None. |
| [`timedelta`](.././flytekit.remote.executions#flytekitremoteexecutionstimedelta) | Difference between two datetime values. |

## flytekit.remote.executions.FlyteNodeExecution

A class encapsulating a node execution being run on a Flyte remote backend.


```python
def FlyteNodeExecution(
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
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`promote_from_model()`](#promote_from_model) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p: flyteidl.admin.node_execution_pb2.NodeExecution,
):
```
| Parameter | Type |
|-|-|
| `p` | `flyteidl.admin.node_execution_pb2.NodeExecution` |

#### promote_from_model()

```python
def promote_from_model(
    base_model: node_execution_models.NodeExecution,
):
```
| Parameter | Type |
|-|-|
| `base_model` | `node_execution_models.NodeExecution` |

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
| closure |  |  |
| error |  |  |
| executions |  |  |
| id |  |  |
| input_uri |  |  |
| inputs |  |  |
| interface |  |  |
| is_done |  |  |
| is_empty |  |  |
| metadata |  |  |
| outputs |  |  |
| subworkflow_node_executions |  |  |
| task_executions |  |  |
| workflow_executions |  |  |

## flytekit.remote.executions.FlyteTask

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

## flytekit.remote.executions.FlyteTaskExecution

A class encapsulating a task execution being run on a Flyte remote backend.


```python
def FlyteTaskExecution(
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
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
):
```
| Parameter | Type |
|-|-|
| `proto` |  |

#### promote_from_model()

```python
def promote_from_model(
    base_model: admin_task_execution_models.TaskExecution,
):
```
| Parameter | Type |
|-|-|
| `base_model` | `admin_task_execution_models.TaskExecution` |

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
| closure |  |  |
| error |  |  |
| id |  |  |
| input_uri |  |  |
| inputs |  |  |
| is_done |  |  |
| is_empty |  |  |
| is_parent |  |  |
| outputs |  |  |
| task |  |  |

## flytekit.remote.executions.FlyteWorkflow

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

## flytekit.remote.executions.FlyteWorkflowExecution

A class encapsulating a workflow execution being run on a Flyte remote backend.


```python
def FlyteWorkflowExecution(
    type_hints: Optional[Dict[str, typing.Type]],
    remote: Optional['FlyteRemote'],
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `type_hints` | `Optional[Dict[str, typing.Type]]` |
| `remote` | `Optional['FlyteRemote']` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`sync()`](#sync) | Sync the state of the current execution and returns a new object with the updated state |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |
| [`wait()`](#wait) | Wait for the execution to complete |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb,
):
```
| Parameter | Type |
|-|-|
| `pb` |  |

#### promote_from_model()

```python
def promote_from_model(
    base_model: execution_models.Execution,
    remote: Optional['FlyteRemote'],
    type_hints: Optional[Dict[str, typing.Type]],
):
```
| Parameter | Type |
|-|-|
| `base_model` | `execution_models.Execution` |
| `remote` | `Optional['FlyteRemote']` |
| `type_hints` | `Optional[Dict[str, typing.Type]]` |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### sync()

```python
def sync(
    sync_nodes: bool,
):
```
Sync the state of the current execution and returns a new object with the updated state.


| Parameter | Type |
|-|-|
| `sync_nodes` | `bool` |

#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
#### wait()

```python
def wait(
    timeout: Optional[Union[timedelta, int]],
    poll_interval: Optional[Union[timedelta, int]],
    sync_nodes: bool,
):
```
Wait for the execution to complete. This is a blocking call.



| Parameter | Type |
|-|-|
| `timeout` | `Optional[Union[timedelta, int]]` |
| `poll_interval` | `Optional[Union[timedelta, int]]` |
| `sync_nodes` | `bool` |

### Properties

| Property | Type | Description |
|-|-|-|
| closure |  |  |
| error |  |  |
| execution_url |  |  |
| flyte_workflow |  |  |
| id |  |  |
| inputs |  |  |
| is_done |  |  |
| is_empty |  |  |
| is_successful |  |  |
| node_executions |  |  |
| outputs |  |  |
| spec |  |  |

## flytekit.remote.executions.LiteralsResolver

LiteralsResolver is a helper class meant primarily for use with the FlyteRemote experience or any other situation
where you might be working with LiteralMaps. This object allows the caller to specify the Python type that should
correspond to an element of the map.


```python
def LiteralsResolver(
    literals: typing.Dict[str, Literal],
    variable_map: Optional[Dict[str, _interface_models.Variable]],
    ctx: Optional[FlyteContext],
):
```
| Parameter | Type |
|-|-|
| `literals` | `typing.Dict[str, Literal]` |
| `variable_map` | `Optional[Dict[str, _interface_models.Variable]]` |
| `ctx` | `Optional[FlyteContext]` |

### Methods

| Method | Description |
|-|-|
| [`as_python_native()`](#as_python_native) | This should return the native Python representation, compatible with unpacking |
| [`clear()`](#clear) | D |
| [`copy()`](#copy) | None |
| [`fromkeys()`](#fromkeys) | None |
| [`get()`](#get) | This will get the ``attr`` value from the Literal map, and invoke the TypeEngine to convert it into a Python |
| [`get_literal()`](#get_literal) | None |
| [`items()`](#items) | D |
| [`keys()`](#keys) | D |
| [`pop()`](#pop) | D |
| [`popitem()`](#popitem) | D |
| [`setdefault()`](#setdefault) | D |
| [`update()`](#update) | D |
| [`update_type_hints()`](#update_type_hints) | None |
| [`values()`](#values) | D |


#### as_python_native()

```python
def as_python_native(
    python_interface: Interface,
):
```
This should return the native Python representation, compatible with unpacking.
This function relies on Python interface outputs being ordered correctly.



| Parameter | Type |
|-|-|
| `python_interface` | `Interface` |

#### clear()

```python
def clear()
```
D.clear() -> None.  Remove all items from D.


#### copy()

```python
def copy()
```
#### fromkeys()

```python
def fromkeys(
    iterable,
    value,
):
```
| Parameter | Type |
|-|-|
| `iterable` |  |
| `value` |  |

#### get()

```python
def get(
    attr: str,
    as_type: Optional[typing.Type],
):
```
This will get the ``attr`` value from the Literal map, and invoke the TypeEngine to convert it into a Python
native value. A Python type can optionally be supplied. If successful, the native value will be cached and
future calls will return the cached value instead.



| Parameter | Type |
|-|-|
| `attr` | `str` |
| `as_type` | `Optional[typing.Type]` |

#### get_literal()

```python
def get_literal(
    key: str,
):
```
| Parameter | Type |
|-|-|
| `key` | `str` |

#### items()

```python
def items()
```
D.items() -> a set-like object providing a view on D's items


#### keys()

```python
def keys()
```
D.keys() -> a set-like object providing a view on D's keys


#### pop()

```python
def pop(
    key,
    default,
):
```
D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised.


| Parameter | Type |
|-|-|
| `key` |  |
| `default` |  |

#### popitem()

```python
def popitem()
```
D.popitem() -> (k, v), remove and return some (key, value) pair
as a 2-tuple; but raise KeyError if D is empty.


#### setdefault()

```python
def setdefault(
    key,
    default,
):
```
D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D


| Parameter | Type |
|-|-|
| `key` |  |
| `default` |  |

#### update()

```python
def update(
    other,
    kwds,
):
```
D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
If E present and has a .keys() method, does:     for k in E.keys(): D[k] = E[k]
If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k, v in F.items(): D[k] = v


| Parameter | Type |
|-|-|
| `other` |  |
| `kwds` |  |

#### update_type_hints()

```python
def update_type_hints(
    type_hints: typing.Dict[str, typing.Type],
):
```
| Parameter | Type |
|-|-|
| `type_hints` | `typing.Dict[str, typing.Type]` |

#### values()

```python
def values()
```
D.values() -> an object providing a view on D's values


### Properties

| Property | Type | Description |
|-|-|-|
| literals |  |  |
| native_values |  |  |
| variable_map |  |  |

## flytekit.remote.executions.RemoteExecutionBase

```python
def RemoteExecutionBase(
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
| error |  |  |
| inputs |  |  |
| is_done |  |  |
| outputs |  |  |

## flytekit.remote.executions.TypedInterface

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

## flytekit.remote.executions.timedelta

Difference between two datetime values.

timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

All arguments are optional and default to 0.
Arguments may be integers or floats, and may be positive or negative.


