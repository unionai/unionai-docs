---
title: TriggerDetails
icon: braces
version: 2.7.1
variants: +flyte +union
layout: py_api
---

# TriggerDetails

**Package:** `flyte.remote`

## Parameters

```python
class TriggerDetails(
    pb2: trigger_definition_pb2.TriggerDetails,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `trigger_definition_pb2.TriggerDetails` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `automation_spec` | `common_pb2.TriggerAutomationSpec` | Get the automation specification for the trigger (e.g., schedule, event). |
| `id` | `identifier_pb2.TriggerIdentifier` | Identifier for the trigger. |
| `is_active` | `bool` | Check if the trigger is currently active. |
| `metadata` | `trigger_definition_pb2.TriggerMetadata` | Get the metadata for the trigger. |
| `name` | `str` | Name of the trigger. |
| `status` | `trigger_definition_pb2.TriggerStatus` | Get the current status of the trigger. |
| `task_name` | `str` | Name of the associated task |
| `trigger` | `trigger_definition_pb2.Trigger` | Get the trigger protobuf object constructed from the details. |

## Methods

| Method | Description |
|-|-|
| [`get()`](#get) | Retrieve detailed information about a specific trigger by its name. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await TriggerDetails.get.aio()`.
```python
def get(
    cls,
    name: str,
    task_name: str,
) -> TriggerDetails
```
Retrieve detailed information about a specific trigger by its name.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `task_name` | `str` | |

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

