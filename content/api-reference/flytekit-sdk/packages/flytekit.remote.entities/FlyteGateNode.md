---
title: FlyteGateNode
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteGateNode

**Package:** `flytekit.remote.entities`

```python
class FlyteGateNode(
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
| [`promote_from_model()`](#promote_from_model) |  |
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

### promote_from_model()

```python
def promote_from_model(
    model: _workflow_model.GateNode,
)
```
| Parameter | Type | Description |
|-|-|-|
| `model` | `_workflow_model.GateNode` | |

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

