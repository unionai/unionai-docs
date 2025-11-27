---
title: ActionDetails
version: 2.0.0b34.dev10+g162555e05
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

## Methods

| Method | Description |
|-|-|
| [`done()`](#done) | Check if the action is in a terminal state (completed or failed). |
| [`get()`](#get) | Get a run by its ID or name. |
| [`get_details()`](#get_details) | Get the details of the action. |
| [`inputs()`](#inputs) | Placeholder for inputs. |
| [`logs_available()`](#logs_available) | Check if logs are available for the action, optionally for a specific attempt. |
| [`outputs()`](#outputs) | Placeholder for outputs. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`watch()`](#watch) | Watch the action for updates. |
| [`watch_updates()`](#watch_updates) |  |


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
Placeholder for inputs. This can be extended to handle inputs from the run context.


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
Placeholder for outputs. This can be extended to handle outputs from the run context.


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
| Parameter | Type | Description |
|-|-|-|
| `cache_data_on_done` | `bool` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `abort_info` | `None` |  |
| `action_id` | `None` | Get the action ID. |
| `attempts` | `None` | Get the number of attempts of the action. |
| `error_info` | `None` |  |
| `is_running` | `None` | Check if the action is currently running. |
| `metadata` | `None` |  |
| `name` | `None` | Get the name of the action. |
| `phase` | `None` | Get the phase of the action. |
| `raw_phase` | `None` | Get the raw phase of the action. |
| `run_name` | `None` | Get the name of the run. |
| `runtime` | `None` | Get the runtime of the action. |
| `status` | `None` |  |
| `task_name` | `None` | Get the name of the task. |

