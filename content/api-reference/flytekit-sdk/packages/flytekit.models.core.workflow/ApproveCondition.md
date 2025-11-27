---
title: ApproveCondition
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ApproveCondition

**Package:** `flytekit.models.core.workflow`

```python
class ApproveCondition(
    signal_id: str,
)
```
Represents a dependency on an signal from a user.



| Parameter | Type | Description |
|-|-|-|
| `signal_id` | `str` | The node id of the signal, also the signal name. |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.workflow_pb2.ApproveCondition,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.workflow_pb2.ApproveCondition` | |

### serialize_to_string()

```python
def serialize_to_string()
```
### short_string()

```python
def short_string()
```
:rtype: Text


### to_flyte_idl()

```python
def to_flyte_idl()
```
## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `signal_id` |  |  |

