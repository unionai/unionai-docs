---
title: flytekit.remote.executions
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
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


```python
class FlyteNodeExecution(
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
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p: flyteidl.admin.node_execution_pb2.NodeExecution,
) -> NodeExecution
```
| Parameter | Type |
|-|-|
| `p` | `flyteidl.admin.node_execution_pb2.NodeExecution` |

#### promote_from_model()

```python
def promote_from_model(
    base_model: node_execution_models.NodeExecution,
) -> 'FlyteNodeExecution'
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
| `closure` |  | {{< multiline >}}:rtype: NodeExecutionClosure
{{< /multiline >}} |
| `error` |  | {{< multiline >}}If execution is in progress, raise an exception. Otherwise, return None if no error was present upon
reaching completion.
{{< /multiline >}} |
| `executions` |  |  |
| `id` |  | {{< multiline >}}:rtype: flytekit.models.core.identifier.NodeExecutionIdentifier
{{< /multiline >}} |
| `input_uri` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `inputs` |  |  |
| `interface` |  | {{< multiline >}}Return the interface of the task or subworkflow associated with this node execution.
{{< /multiline >}} |
| `is_done` |  | {{< multiline >}}Whether or not the execution is complete.
{{< /multiline >}} |
| `is_empty` |  |  |
| `metadata` |  |  |
| `outputs` |  | {{< multiline >}}:return: Returns the outputs LiteralsResolver to the execution
:raises: ``FlyteAssertion`` error if execution is in progress or execution ended in error.
{{< /multiline >}} |
| `subworkflow_node_executions` |  | {{< multiline >}}This returns underlying node executions in instances where the current node execution is
a parent node. This happens when it's either a static or dynamic subworkflow.
{{< /multiline >}} |
| `task_executions` |  |  |
| `workflow_executions` |  |  |

## flytekit.remote.executions.FlyteTaskExecution

A class encapsulating a task execution being run on a Flyte remote backend.


```python
class FlyteTaskExecution(
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
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> e: TaskExecution
```
| Parameter | Type |
|-|-|
| `proto` |  |

#### promote_from_model()

```python
def promote_from_model(
    base_model: admin_task_execution_models.TaskExecution,
) -> 'FlyteTaskExecution'
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.task_execution_pb2.TaskExecution


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `closure` |  | {{< multiline >}}:rtype: TaskExecutionClosure
{{< /multiline >}} |
| `error` |  | {{< multiline >}}If execution is in progress, raise an exception. Otherwise, return None if no error was present upon
reaching completion.
{{< /multiline >}} |
| `id` |  | {{< multiline >}}:rtype: flytekit.models.core.identifier.TaskExecutionIdentifier
{{< /multiline >}} |
| `input_uri` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `inputs` |  |  |
| `is_done` |  | {{< multiline >}}Whether or not the execution is complete.
{{< /multiline >}} |
| `is_empty` |  |  |
| `is_parent` |  | {{< multiline >}}:rtype: bool
{{< /multiline >}} |
| `outputs` |  | {{< multiline >}}:return: Returns the outputs LiteralsResolver to the execution
:raises: ``FlyteAssertion`` error if execution is in progress or execution ended in error.
{{< /multiline >}} |
| `task` |  |  |

## flytekit.remote.executions.FlyteWorkflowExecution

A class encapsulating a workflow execution being run on a Flyte remote backend.


```python
class FlyteWorkflowExecution(
    type_hints: Optional[Dict[str, typing.Type]],
    remote: Optional['FlyteRemote'],
    args,
    kwargs,
)
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
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`sync()`](#sync) | Sync the state of the current execution and returns a new object with the updated state. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |
| [`wait()`](#wait) | Wait for the execution to complete. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb,
) -> e: Execution
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
) -> 'FlyteWorkflowExecution'
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
:rtype: Text


#### sync()

```python
def sync(
    sync_nodes: bool,
) -> 'FlyteWorkflowExecution'
```
Sync the state of the current execution and returns a new object with the updated state.


| Parameter | Type |
|-|-|
| `sync_nodes` | `bool` |

#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.execution_pb2.Execution


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


#### wait()

```python
def wait(
    timeout: Optional[Union[timedelta, int]],
    poll_interval: Optional[Union[timedelta, int]],
    sync_nodes: bool,
) -> 'FlyteWorkflowExecution'
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
| `closure` |  | {{< multiline >}}:rtype: ExecutionClosure
{{< /multiline >}} |
| `error` |  | {{< multiline >}}If execution is in progress, raise an exception.  Otherwise, return None if no error was present upon
reaching completion.
{{< /multiline >}} |
| `execution_url` |  |  |
| `flyte_workflow` |  |  |
| `id` |  | {{< multiline >}}:rtype: flytekit.models.core.identifier.WorkflowExecutionIdentifier
{{< /multiline >}} |
| `inputs` |  |  |
| `is_done` |  | {{< multiline >}}Whether or not the execution is complete.
{{< /multiline >}} |
| `is_empty` |  |  |
| `is_successful` |  | {{< multiline >}}Whether or not the execution is successful.
{{< /multiline >}} |
| `node_executions` |  | {{< multiline >}}Get a dictionary of node executions that are a part of this workflow execution.
{{< /multiline >}} |
| `outputs` |  | {{< multiline >}}:return: Returns the outputs LiteralsResolver to the execution
:raises: ``FlyteAssertion`` error if execution is in progress or execution ended in error.
{{< /multiline >}} |
| `spec` |  | {{< multiline >}}:rtype: ExecutionSpec
{{< /multiline >}} |

## flytekit.remote.executions.RemoteExecutionBase

```python
class RemoteExecutionBase(
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `error` |  |  |
| `inputs` |  |  |
| `is_done` |  |  |
| `outputs` |  | {{< multiline >}}:return: Returns the outputs LiteralsResolver to the execution
:raises: ``FlyteAssertion`` error if execution is in progress or execution ended in error.
{{< /multiline >}} |

