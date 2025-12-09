---
title: RunDetails
version: 2.0.0b35
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# RunDetails

**Package:** `flyte.remote`

A class representing a run of a task. It is used to manage the run of a task and its state on the remote
Union API.


```python
class RunDetails(
    pb2: run_definition_pb2.RunDetails,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `run_definition_pb2.RunDetails` | |

## Methods

| Method | Description |
|-|-|
| [`done()`](#done) | Check if the run is in a terminal state (completed or failed). |
| [`get()`](#get) | Get a run by its ID or name. |
| [`get_details()`](#get_details) | Get the details of the run. |
| [`inputs()`](#inputs) | Placeholder for inputs. |
| [`outputs()`](#outputs) | Placeholder for outputs. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


### done()

```python
def done()
```
Check if the run is in a terminal state (completed or failed). This is a placeholder for checking the
run state.


### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await RunDetails.get.aio()`.
```python
def get(
    cls,
    name: str | None,
) -> RunDetails
```
Get a run by its ID or name. If both are provided, the ID will take precedence.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str \| None` | The name of the run. |

### get_details()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await RunDetails.get_details.aio()`.
```python
def get_details(
    cls,
    run_id: identifier_pb2.RunIdentifier,
) -> RunDetails
```
Get the details of the run. This is a placeholder for getting the run details.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `run_id` | `identifier_pb2.RunIdentifier` | |

### inputs()

```python
def inputs()
```
Placeholder for inputs. This can be extended to handle inputs from the run context.


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


## Properties

| Property | Type | Description |
|-|-|-|
| `action_id` | `None` | Get the action ID. |
| `name` | `None` | Get the name of the action. |
| `task_name` | `None` | Get the name of the task. |

