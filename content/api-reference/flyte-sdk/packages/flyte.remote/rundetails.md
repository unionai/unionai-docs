---
title: RunDetails
version: 2.5.12
variants: +flyte +union
layout: py_api
---

# RunDetails

**Package:** `flyte.remote`

A class representing a run of a task. It is used to manage the run of a task and its state on the remote
Union API.


## Parameters

```python
class RunDetails(
    pb2: run_definition_pb2.RunDetails,
    _preserve_original_types: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `run_definition_pb2.RunDetails` | |
| `_preserve_original_types` | `bool` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `action_id` | `identifier_pb2.ActionIdentifier` | Get the action ID. |
| `name` | `str` | Get the name of the action. |
| `task_name` | `str \| None` | Get the name of the task. |

## Methods

| Method | Description |
|-|-|
| [`done()`](#done) | Check if the run is in a terminal state (completed or failed). |
| [`get()`](#get) | Get a run by its ID or name. |
| [`get_details()`](#get_details) | Get the details of the run. |
| [`input_literals()`](#input_literals) | Raw input literals without reconstructing types. |
| [`inputs()`](#inputs) | Placeholder for inputs. |
| [`output_literals()`](#output_literals) | Raw output literals without reconstructing types. |
| [`outputs()`](#outputs) | Placeholder for outputs. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`typed_inputs()`](#typed_inputs) | Re-hydrate requested inputs into caller-supplied types. |
| [`typed_outputs()`](#typed_outputs) | Re-hydrate requested outputs into caller-supplied types. |


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

### input_literals()

```python
def input_literals()
```
Raw input literals without reconstructing types. See :meth:`ActionDetails.input_literals`.


### inputs()

```python
def inputs()
```
Placeholder for inputs. This can be extended to handle inputs from the run context.


### output_literals()

```python
def output_literals()
```
Raw output literals without reconstructing types. See :meth:`ActionDetails.output_literals`.


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



**Returns:** dict: A dictionary representation of the object.

### to_json()

```python
def to_json()
```
Convert the object to a JSON string.



**Returns:** str: A JSON string representation of the object.

### typed_inputs()

```python
def typed_inputs(
    types: Dict[str, type],
    deserializers: Dict[type, Callable[[Any], Any]] | None,
) -> Dict[str, Any]
```
Re-hydrate requested inputs into caller-supplied types. See :meth:`ActionDetails.typed_inputs`.


| Parameter | Type | Description |
|-|-|-|
| `types` | `Dict[str, type]` | |
| `deserializers` | `Dict[type, Callable[[Any], Any]] \| None` | |

### typed_outputs()

```python
def typed_outputs(
    types: Dict[str, type],
    deserializers: Dict[type, Callable[[Any], Any]] | None,
) -> Dict[str, Any]
```
Re-hydrate requested outputs into caller-supplied types. See :meth:`ActionDetails.typed_outputs`.


| Parameter | Type | Description |
|-|-|-|
| `types` | `Dict[str, type]` | |
| `deserializers` | `Dict[type, Callable[[Any], Any]] \| None` | |

