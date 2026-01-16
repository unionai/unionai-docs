---
title: ActionOutputs
version: 2.0.0b48
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ActionOutputs

**Package:** `flyte.remote`

A class representing the outputs of an action. The outputs are by default represented as a Tuple. To access them,
you can simply read them as a tuple (assign to individual variables, use index to access) or you can use the
property `named_outputs` to retrieve a dictionary of outputs with keys that represent output names
which are usually auto-generated `o0, o1, o2, o3, ...`.

Example Usage:
```python
action = Action.get(...)
print(action.outputs())
```
Output:
```python
("val1", "val2", ...)
```
OR
```python
action = Action.get(...)
print(action.outputs().named_outputs)
```
Output:
```bash
{"o0": "val1", "o1": "val2", ...}
```


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

## Properties

| Property | Type | Description |
|-|-|-|
| `named_outputs` | `None` |  |

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


