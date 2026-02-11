---
title: Action
version: 2.0.0b56
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Action

**Package:** `flyte.remote`

A class representing an action. It is used to manage the "execution" of a task and its state on the remote API.

From a datamodel perspective, a Run consists of actions. All actions are linearly nested under a parent action.
 Actions have unique auto-generated identifiers, that are unique within a parent action.

 &lt;pre&gt;
 run
  - a0
    - action1 under a0
    - action2 under a0
        - action1 under action2 under a0
        - action2 under action1 under action2 under a0
        - ...
    - ...
&lt;/pre&gt;



```python
class Action(
    pb2: run_definition_pb2.Action,
    _details: ActionDetails | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `run_definition_pb2.Action` | |
| `_details` | `ActionDetails \| None` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `action_id` | `None` | Get the action ID. |
| `name` | `None` | Get the name of the action. |
| `phase` | `None` | Get the phase of the action.  Returns:     The current execution phase as an ActionPhase enum |
| `raw_phase` | `None` | Get the raw phase of the action. |
| `run_name` | `None` | Get the name of the run. |
| `start_time` | `None` | Get the start time of the action. |
| `task_name` | `None` | Get the name of the task. |

## Methods

| Method | Description |
|-|-|
| [`abort()`](#abort) | Aborts / Terminates the action. |
| [`details()`](#details) | Get the details of the action. |
| [`done()`](#done) | Check if the action is done. |
| [`get()`](#get) | Get a run by its ID or name. |
| [`listall()`](#listall) | Get all actions for a given run. |
| [`show_logs()`](#show_logs) | Display logs for the action. |
| [`sync()`](#sync) | Sync the action with the remote server. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`wait()`](#wait) | Wait for the run to complete, displaying a rich progress panel with status transitions,. |
| [`watch()`](#watch) | Watch the action for updates, updating the internal Action state with latest details. |


### abort()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <Action instance>.abort.aio()`.
```python
def abort(
    reason: str,
)
```
Aborts / Terminates the action.


| Parameter | Type | Description |
|-|-|-|
| `reason` | `str` | |

### details()

```python
def details()
```
Get the details of the action. This is a placeholder for getting the action details.


### done()

```python
def done()
```
Check if the action is done.


### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Action.get.aio()`.
```python
def get(
    cls,
    uri: str | None,
    run_name: str | None,
    name: str | None,
) -> Action
```
Get a run by its ID or name. If both are provided, the ID will take precedence.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `uri` | `str \| None` | The URI of the action. |
| `run_name` | `str \| None` | The name of the action. |
| `name` | `str \| None` | The name of the action. |

### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Action.listall.aio()`.
```python
def listall(
    cls,
    for_run_name: str,
    in_phase: Tuple[ActionPhase | str, ...] | None,
    filters: str | None,
    sort_by: Tuple[str, Literal['asc', 'desc']] | None,
) -> Union[Iterator[Action], AsyncIterator[Action]]
```
Get all actions for a given run.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `for_run_name` | `str` | The name of the run. |
| `in_phase` | `Tuple[ActionPhase \| str, ...] \| None` | Filter actions by one or more phases. |
| `filters` | `str \| None` | The filters to apply to the project list. |
| `sort_by` | `Tuple[str, Literal['asc', 'desc']] \| None` | The sorting criteria for the project list, in the format (field, order). :return: An iterator of actions. |

### show_logs()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <Action instance>.show_logs.aio()`.
```python
def show_logs(
    attempt: int | None,
    max_lines: int,
    show_ts: bool,
    raw: bool,
    filter_system: bool,
)
```
Display logs for the action.



| Parameter | Type | Description |
|-|-|-|
| `attempt` | `int \| None` | The attempt number to show logs for (defaults to latest attempt). |
| `max_lines` | `int` | Maximum number of log lines to display in the viewer. |
| `show_ts` | `bool` | Whether to show timestamps with each log line. |
| `raw` | `bool` | If True, print logs directly without the interactive viewer. |
| `filter_system` | `bool` | If True, filter out system-generated log lines. |

### sync()

```python
def sync()
```
Sync the action with the remote server. This is a placeholder for syncing the action.


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


### wait()

```python
def wait(
    quiet: bool,
    wait_for: WaitFor,
)
```
Wait for the run to complete, displaying a rich progress panel with status transitions,
time elapsed, and error details in case of failure.


| Parameter | Type | Description |
|-|-|-|
| `quiet` | `bool` | |
| `wait_for` | `WaitFor` | |

### watch()

```python
def watch(
    cache_data_on_done: bool,
    wait_for: WaitFor,
) -> AsyncGenerator[ActionDetails, None]
```
Watch the action for updates, updating the internal Action state with latest details.

This method updates both the cached details and the protobuf representation,
ensuring that properties like `phase` reflect the current state.


| Parameter | Type | Description |
|-|-|-|
| `cache_data_on_done` | `bool` | |
| `wait_for` | `WaitFor` | |

