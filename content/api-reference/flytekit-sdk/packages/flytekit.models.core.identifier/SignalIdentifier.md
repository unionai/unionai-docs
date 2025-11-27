---
title: SignalIdentifier
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SignalIdentifier

**Package:** `flytekit.models.core.identifier`

```python
class SignalIdentifier(
    signal_id: str,
    execution_id: flytekit.models.core.identifier.WorkflowExecutionIdentifier,
)
```
| Parameter | Type | Description |
|-|-|-|
| `signal_id` | `str` | User provided name for the gate node. |
| `execution_id` | `flytekit.models.core.identifier.WorkflowExecutionIdentifier` | The workflow execution id this signal is for. |

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
    proto: flyteidl.core.identifier_pb2.SignalIdentifier,
) -> SignalIdentifier
```
| Parameter | Type | Description |
|-|-|-|
| `proto` | `flyteidl.core.identifier_pb2.SignalIdentifier` | |

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
| `execution_id` |  |  |
| `is_empty` |  |  |
| `signal_id` |  |  |

