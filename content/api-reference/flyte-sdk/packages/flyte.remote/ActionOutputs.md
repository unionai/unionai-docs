---
title: ActionOutputs
version: 2.0.0b38
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ActionOutputs

**Package:** `flyte.remote`

A class representing the outputs of an action. It is used to manage the outputs of a task and its state on the
remote Union API.


```python
class ActionOutputs(
    pb2: common_pb2.Outputs,
    data: Tuple[Any, ...],
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `common_pb2.Outputs` | |
| `data` | `Tuple[Any, ...]` | |

## Methods

| Method | Description |
|-|-|
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


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


