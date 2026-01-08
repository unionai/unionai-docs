---
title: Run
version: 2.0.0b46
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Run

**Package:** `flyte.remote`

A class representing a run of a task. It is used to manage the run of a task and its state on the remote
Union API.


```python
class Run(
    pb2: run_definition_pb2.Run,
    _details: RunDetails | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `run_definition_pb2.Run` | |
| `_details` | `RunDetails \| None` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `name` | `None` | Get the name of the run. |
| `phase` | `None` | Get the phase of the run. |
| `raw_phase` | `None` | Get the raw phase of the run. |
| `url` | `None` | Get the URL of the run. |

## Methods

| Method | Description |
|-|-|
| [`abort()`](#abort) | Aborts / Terminates the run. |
| [`details()`](#details) | Get the details of the run. |
| [`done()`](#done) | Check if the run is done. |
| [`get()`](#get) | Get the current run. |
| [`inputs()`](#inputs) | Get the inputs of the run. |
| [`listall()`](#listall) | Get all runs for the current project and domain. |
| [`outputs()`](#outputs) | Get the outputs of the run. |
| [`show_logs()`](#show_logs) |  |
| [`sync()`](#sync) | Sync the run with the remote server. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`wait()`](#wait) | Wait for the run to complete, displaying a rich progress panel with status transitions,. |
| [`watch()`](#watch) | Watch the run for updates, updating the internal Run state with latest details. |


### abort()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <Run instance>.abort.aio()`.
```python
def abort()
```
Aborts / Terminates the run.


### details()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <Run instance>.details.aio()`.
```python
def details()
```
Get the details of the run. This is a placeholder for getting the run details.


### done()

```python
def done()
```
Check if the run is done.


### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Run.get.aio()`.
```python
def get(
    cls,
    name: str,
) -> Run
```
Get the current run.

:return: The current run.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |

### inputs()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <Run instance>.inputs.aio()`.
```python
def inputs()
```
Get the inputs of the run. This is a placeholder for getting the run inputs.


### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Run.listall.aio()`.
```python
def listall(
    cls,
    in_phase: Tuple[ActionPhase | str, ...] | None,
    task_name: str | None,
    task_version: str | None,
    created_by_subject: str | None,
    sort_by: Tuple[str, Literal['asc', 'desc']] | None,
    limit: int,
) -> AsyncIterator[Run]
```
Get all runs for the current project and domain.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `in_phase` | `Tuple[ActionPhase \| str, ...] \| None` | Filter runs by one or more phases. |
| `task_name` | `str \| None` | Filter runs by task name. |
| `task_version` | `str \| None` | Filter runs by task version. |
| `created_by_subject` | `str \| None` | Filter runs by the subject that created them. (this is not username, but the subject) |
| `sort_by` | `Tuple[str, Literal['asc', 'desc']] \| None` | The sorting criteria for the Run list, in the format (field, order). |
| `limit` | `int` | The maximum number of runs to return. :return: An iterator of runs. |

### outputs()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <Run instance>.outputs.aio()`.
```python
def outputs()
```
Get the outputs of the run. This is a placeholder for getting the run outputs.


### show_logs()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <Run instance>.show_logs.aio()`.
```python
def show_logs(
    attempt: int | None,
    max_lines: int,
    show_ts: bool,
    raw: bool,
    filter_system: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `attempt` | `int \| None` | |
| `max_lines` | `int` | |
| `show_ts` | `bool` | |
| `raw` | `bool` | |
| `filter_system` | `bool` | |

### sync()

```python
def sync()
```
Sync the run with the remote server. This is a placeholder for syncing the run.


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


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <Run instance>.wait.aio()`.
```python
def wait(
    quiet: bool,
    wait_for: Literal['terminal', 'running'],
)
```
Wait for the run to complete, displaying a rich progress panel with status transitions,
time elapsed, and error details in case of failure.

This method updates the Run's internal state, ensuring that properties like
`run.action.phase` reflect the final state after waiting completes.


| Parameter | Type | Description |
|-|-|-|
| `quiet` | `bool` | |
| `wait_for` | `Literal['terminal', 'running']` | |

### watch()

```python
def watch(
    cache_data_on_done: bool,
) -> AsyncGenerator[ActionDetails, None]
```
Watch the run for updates, updating the internal Run state with latest details.

This method updates the Run's action state, ensuring that properties like
`run.action.phase` reflect the current state after watching.


| Parameter | Type | Description |
|-|-|-|
| `cache_data_on_done` | `bool` | |

