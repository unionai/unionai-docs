---
title: SignalCondition
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SignalCondition

**Package:** `flytekit.models.core.workflow`

```python
class SignalCondition(
    signal_id: str,
    type: flytekit.models.types.LiteralType,
    output_variable_name: str,
)
```
Represents a dependency on an signal from a user.



| Parameter | Type | Description |
|-|-|-|
| `signal_id` | `str` | The node id of the signal, also the signal name. |
| `type` | `flytekit.models.types.LiteralType` | |
| `output_variable_name` | `str` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `output_variable_name` | `None` |  |
| `signal_id` | `None` |  |
| `type` | `None` |  |

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
    pb2_object: flyteidl.core.workflow_pb2.SignalCondition,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.workflow_pb2.SignalCondition` | |

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
