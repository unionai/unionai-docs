---
title: ActionOutputs
version: 2.0.6
variants: +flyte +byoc +selfmanaged
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
    fields: List[str] | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `common_pb2.Outputs` | |
| `data` | `Tuple[Any, ...]` | |
| `fields` | `List[str] \| None` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `named_outputs` | `None` |  |

