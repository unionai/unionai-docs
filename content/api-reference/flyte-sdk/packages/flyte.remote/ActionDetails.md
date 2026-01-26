---
title: ActionDetails
version: 2.0.0b50
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ActionDetails

**Package:** `flyte.remote`

A class representing an action. It is used to manage the run of a task and its state on the remote Union API.


```python
class ActionDetails(
    pb2: run_definition_pb2.ActionDetails,
    _inputs: ActionInputs | None,
    _outputs: ActionOutputs | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `run_definition_pb2.ActionDetails` | |
| `_inputs` | `ActionInputs \| None` | |
| `_outputs` | `ActionOutputs \| None` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `abort_info` | `None` | Get the abort information if the action was aborted, otherwise returns None. |
| `action_id` | `None` | Get the action ID. |
| `attempts` | `None` | Get the number of attempts of the action. |
| `error_info` | `None` | Get the error information if the action failed, otherwise returns None. |
| `is_running` | `None` | Check if the action is currently running. |
| `metadata` | `None` | Get the metadata of the action. |
| `name` | `None` | Get the name of the action. |
| `phase` | `None` | Get the phase of the action.  Returns:     The current execution phase as an ActionPhase enum |
| `raw_phase` | `None` | Get the raw phase of the action. |
| `run_name` | `None` | Get the name of the run. |
| `runtime` | `None` | Get the runtime of the action. |
| `status` | `None` | Get the status of the action. |
| `task_name` | `None` | Get the name of the task. |

## Methods

| Method | Description |
|-|-|
| [`done()`](#done) | Check if the action is in a terminal state (completed or failed). |
| [`get()`](#get) | Get a run by its ID or name. |
| [`get_details()`](#get_details) | Get the details of the action. |
| [`inputs()`](#inputs) | Return the inputs of the action. |
| [`logs_available()`](#logs_available) | Check if logs are available for the action, optionally for a specific attempt. |
| [`outputs()`](#outputs) | Returns the outputs of the action, returns instantly if outputs are already cached, else fetches them and. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`watch()`](#watch) | Watch the action for updates. |
| [`watch_updates()`](#watch_updates) | Watch for updates to the action details, yielding each update until the action is done. |


### done()

```python
def done()
```
Check if the action is in a terminal state (completed or failed). This is a placeholder for checking the
action state.


### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await ActionDetails.get.aio()`.
```python
def get(
    cls,
    uri: str | None,
    run_name: str | None,
    name: str | None,
) -> ActionDetails
```
Get a run by its ID or name. If both are provided, the ID will take precedence.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `uri` | `str \| None` | The URI of the action. |
| `run_name` | `str \| None` | The name of the run. |
| `name` | `str \| None` | The name of the action. |

### get_details()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await ActionDetails.get_details.aio()`.
```python
def get_details(
    cls,
    action_id: identifier_pb2.ActionIdentifier,
) -> ActionDetails
```
Get the details of the action. This is a placeholder for getting the action details.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `action_id` | `identifier_pb2.ActionIdentifier` | |

### inputs()

```python
def inputs()
```
Return the inputs of the action.
Will return instantly if inputs are available else will fetch and return.


### logs_available()

```python
def logs_available(
    attempt: int | None,
) -> bool
```
Check if logs are available for the action, optionally for a specific attempt.
If attempt is None, it checks for the latest attempt.


| Parameter | Type | Description |
|-|-|-|
| `attempt` | `int \| None` | |

### outputs()

```python
def outputs()
```
Returns the outputs of the action, returns instantly if outputs are already cached, else fetches them and
returns. If Action is not in a terminal state, raise a RuntimeError.

:return: ActionOutputs


### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.

Returns:
    dict: A dictionary representation of the object.


### to_json()

```python
def to_json()
```
Convert the object to a JSON string.

Returns:
    str: A JSON string representation of the object.


### watch()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await ActionDetails.watch.aio()`.
```python
def watch(
    cls,
    action_id: identifier_pb2.ActionIdentifier,
) -> AsyncIterator[ActionDetails]
```
Watch the action for updates. This is a placeholder for watching the action.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `action_id` | `identifier_pb2.ActionIdentifier` | |

### watch_updates()

```python
def watch_updates(
    cache_data_on_done: bool,
) -> AsyncGenerator[ActionDetails, None]
```
Watch for updates to the action details, yielding each update until the action is done.



| Parameter | Type | Description |
|-|-|-|
| `cache_data_on_done` | `bool` | If True, cache inputs and outputs when the action completes. |

