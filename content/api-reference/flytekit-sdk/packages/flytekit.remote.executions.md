---
title: flytekit.remote.executions
version: 1.16.19
variants: +flyte +union
layout: py_api
---

# flytekit.remote.executions

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteNodeExecution`](.././flytekit.remote.executions#flytekitremoteexecutionsflytenodeexecution) | A class encapsulating a node execution being run on a Flyte remote backend. |
| [`FlyteTaskExecution`](.././flytekit.remote.executions#flytekitremoteexecutionsflytetaskexecution) | A class encapsulating a task execution being run on a Flyte remote backend. |
| [`FlyteWorkflowExecution`](.././flytekit.remote.executions#flytekitremoteexecutionsflyteworkflowexecution) | A class encapsulating a workflow execution being run on a Flyte remote backend. |
| [`RemoteExecutionBase`](.././flytekit.remote.executions#flytekitremoteexecutionsremoteexecutionbase) |  |

## flytekit.remote.executions.FlyteNodeExecution

A class encapsulating a node execution being run on a Flyte remote backend.


### Parameters

```python
class FlyteNodeExecution(
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `closure` | `None` |  |
| `error` | `core_execution_models.ExecutionError` | If execution is in progress, raise an exception. Otherwise, return None if no error was present upon reaching completion. |
| `executions` | `List[Union[FlyteTaskExecution, FlyteWorkflowExecution]]` |  |
| `id` | `None` |  |
| `input_uri` | `None` |  |
| `inputs` | `Optional[LiteralsResolver]` |  |
| `interface` | `'flytekit.remote.interface.TypedInterface'` | Return the interface of the task or subworkflow associated with this node execution. |
| `is_done` | `bool` | Whether or not the execution is complete. |
| `is_empty` | `None` |  |
| `metadata` | `flyteidl.admin.node_execution_pb2.NodeExecutionMetaData` |  |
| `outputs` | `Optional[LiteralsResolver]` |  |
| `subworkflow_node_executions` | `Dict[str, FlyteNodeExecution]` | This returns underlying node executions in instances where the current node execution is a parent node. This happens when it's either a static or dynamic subworkflow. |
| `task_executions` | `List[FlyteTaskExecution]` |  |
| `workflow_executions` | `List[FlyteWorkflowExecution]` |  |

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
    p: flyteidl.admin.node_execution_pb2.NodeExecution,
) -> NodeExecution
```
| Parameter | Type | Description |
|-|-|-|
| `p` | `flyteidl.admin.node_execution_pb2.NodeExecution` | |

#### promote_from_model()

```python
def promote_from_model(
    base_model: node_execution_models.NodeExecution,
) -> 'FlyteNodeExecution'
```
| Parameter | Type | Description |
|-|-|-|
| `base_model` | `node_execution_models.NodeExecution` | |

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
## flytekit.remote.executions.FlyteTaskExecution

A class encapsulating a task execution being run on a Flyte remote backend.


### Parameters

```python
class FlyteTaskExecution(
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `closure` | `None` |  |
| `error` | `Optional[core_execution_models.ExecutionError]` | If execution is in progress, raise an exception. Otherwise, return None if no error was present upon reaching completion. |
| `id` | `None` |  |
| `input_uri` | `None` |  |
| `inputs` | `Optional[LiteralsResolver]` |  |
| `is_done` | `bool` | Whether or not the execution is complete. |
| `is_empty` | `None` |  |
| `is_parent` | `None` |  |
| `outputs` | `Optional[LiteralsResolver]` |  |
| `task` | `Optional[FlyteTask]` |  |

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
    proto,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` |  | |

**Returns:** TaskExecution

#### promote_from_model()

```python
def promote_from_model(
    base_model: admin_task_execution_models.TaskExecution,
) -> 'FlyteTaskExecution'
```
| Parameter | Type | Description |
|-|-|-|
| `base_model` | `admin_task_execution_models.TaskExecution` | |

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
**Returns:** flyteidl.admin.task_execution_pb2.TaskExecution

## flytekit.remote.executions.FlyteWorkflowExecution

A class encapsulating a workflow execution being run on a Flyte remote backend.


### Parameters

```python
class FlyteWorkflowExecution(
    type_hints: Optional[Dict[str, typing.Type]],
    remote: Optional['FlyteRemote'],
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `type_hints` | `Optional[Dict[str, typing.Type]]` | |
| `remote` | `Optional['FlyteRemote']` | |
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `closure` | `None` |  |
| `error` | `core_execution_models.ExecutionError` | If execution is in progress, raise an exception.  Otherwise, return None if no error was present upon reaching completion. |
| `execution_url` | `Optional[str]` |  |
| `flyte_workflow` | `Optional[FlyteWorkflow]` |  |
| `id` | `_identifier.WorkflowExecutionIdentifier` |  |
| `inputs` | `Optional[LiteralsResolver]` |  |
| `is_done` | `bool` | Whether or not the execution is complete. |
| `is_empty` | `None` |  |
| `is_successful` | `bool` | Whether or not the execution is successful. |
| `node_executions` | `Dict[str, FlyteNodeExecution]` | Get a dictionary of node executions that are a part of this workflow execution. |
| `outputs` | `Optional[LiteralsResolver]` |  |
| `spec` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`sync()`](#sync) | Sync the state of the current execution and returns a new object with the updated state. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`wait()`](#wait) | Wait for the execution to complete. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb` |  | |

**Returns:** Execution

#### promote_from_model()

```python
def promote_from_model(
    base_model: execution_models.Execution,
    remote: Optional['FlyteRemote'],
    type_hints: Optional[Dict[str, typing.Type]],
) -> 'FlyteWorkflowExecution'
```
| Parameter | Type | Description |
|-|-|-|
| `base_model` | `execution_models.Execution` | |
| `remote` | `Optional['FlyteRemote']` | |
| `type_hints` | `Optional[Dict[str, typing.Type]]` | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### sync()

```python
def sync(
    sync_nodes: bool,
) -> 'FlyteWorkflowExecution'
```
Sync the state of the current execution and returns a new object with the updated state.


| Parameter | Type | Description |
|-|-|-|
| `sync_nodes` | `bool` | |

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.admin.execution_pb2.Execution

#### wait()

```python
def wait(
    timeout: Optional[Union[timedelta, int]],
    poll_interval: Optional[Union[timedelta, int]],
    sync_nodes: bool,
) -> 'FlyteWorkflowExecution'
```
Wait for the execution to complete. This is a blocking call.



| Parameter | Type | Description |
|-|-|-|
| `timeout` | `Optional[Union[timedelta, int]]` | The maximum amount of time to wait for the execution to complete. It can be a timedelta or a duration in seconds as int. |
| `poll_interval` | `Optional[Union[timedelta, int]]` | The amount of time to wait between polling the state of the execution. It can be a timedelta or a duration in seconds as int. |
| `sync_nodes` | `bool` | Whether to sync the state of the nodes as well. |

## flytekit.remote.executions.RemoteExecutionBase

### Parameters

```python
class RemoteExecutionBase(
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `error` | `core_execution_models.ExecutionError` |  |
| `inputs` | `Optional[LiteralsResolver]` |  |
| `is_done` | `bool` |  |
| `outputs` | `Optional[LiteralsResolver]` |  |

