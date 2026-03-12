---
title: ActionInputs
version: 2.0.6
variants: +flyte +byoc +selfmanaged
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

