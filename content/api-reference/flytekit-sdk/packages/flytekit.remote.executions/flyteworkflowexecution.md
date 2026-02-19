---
title: FlyteWorkflowExecution
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteWorkflowExecution

**Package:** `flytekit.remote.executions`

A class encapsulating a workflow execution being run on a Flyte remote backend.


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

## Properties

| Property | Type | Description |
|-|-|-|
| `closure` | `None` | :rtype: ExecutionClosure |
| `error` | `None` | If execution is in progress, raise an exception.  Otherwise, return None if no error was present upon reaching completion. |
| `execution_url` | `None` |  |
| `flyte_workflow` | `None` |  |
| `id` | `None` | :rtype: flytekit.models.core.identifier.WorkflowExecutionIdentifier |
| `inputs` | `None` |  |
| `is_done` | `None` | Whether or not the execution is complete. |
| `is_empty` | `None` |  |
| `is_successful` | `None` | Whether or not the execution is successful. |
| `node_executions` | `None` | Get a dictionary of node executions that are a part of this workflow execution. |
| `outputs` | `None` | :return: Returns the outputs LiteralsResolver to the execution :raises: ``FlyteAssertion`` error if execution is in progress or execution ended in error. |
| `spec` | `None` | :rtype: ExecutionSpec |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`sync()`](#sync) | Sync the state of the current execution and returns a new object with the updated state. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`wait()`](#wait) | Wait for the execution to complete. |


### from_flyte_idl()

```python
def from_flyte_idl(
    pb,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb` |  | |

### promote_from_model()

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

### serialize_to_string()

```python
def serialize_to_string()
```
### short_string()

```python
def short_string()
```
:rtype: Text


### sync()

```python
def sync(
    sync_nodes: bool,
) -> 'FlyteWorkflowExecution'
```
Sync the state of the current execution and returns a new object with the updated state.


| Parameter | Type | Description |
|-|-|-|
| `sync_nodes` | `bool` | |

### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.execution_pb2.Execution


### wait()

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

