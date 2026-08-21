---
title: ActionInputs
version: 2.6.5
variants: +flyte +union
layout: py_api
---

# ActionInputs

**Package:** `flyte.remote`

A class representing the inputs of an action. It is used to manage the inputs of a task and its state on the
remote Union API.

ActionInputs extends from a `UserDict` and hence is accessible like a dictionary

Example Usage:
```python
action = Action.get(...)
print(action.inputs())
```
Output:
```bash
{
  "x": ...,
  "y": ...,
}
```


## Parameters

```python
class ActionInputs(
    pb2: common_pb2.Inputs,
    data: Dict[str, Any],
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `common_pb2.Inputs` | |
| `data` | `Dict[str, Any]` | |

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



**Returns:** dict: A dictionary representation of the object.

### to_json()

```python
def to_json()
```
Convert the object to a JSON string.



**Returns:** str: A JSON string representation of the object.

