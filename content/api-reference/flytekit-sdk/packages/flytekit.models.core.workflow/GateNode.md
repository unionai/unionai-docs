---
title: GateNode
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# GateNode

**Package:** `flytekit.models.core.workflow`

```python
class GateNode(
    signal: typing.Optional[flytekit.models.core.workflow.SignalCondition],
    sleep: typing.Optional[flytekit.models.core.workflow.SleepCondition],
    approve: typing.Optional[flytekit.models.core.workflow.ApproveCondition],
)
```
| Parameter | Type | Description |
|-|-|-|
| `signal` | `typing.Optional[flytekit.models.core.workflow.SignalCondition]` | |
| `sleep` | `typing.Optional[flytekit.models.core.workflow.SleepCondition]` | |
| `approve` | `typing.Optional[flytekit.models.core.workflow.ApproveCondition]` | |

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
    pb2_object: flyteidl.core.workflow_pb2.GateNode,
) -> GateNode
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.workflow_pb2.GateNode` | |

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
| `approve` |  |  |
| `condition` |  |  |
| `is_empty` |  |  |
| `signal` |  |  |
| `sleep` |  |  |

