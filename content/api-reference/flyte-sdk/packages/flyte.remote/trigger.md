---
title: Trigger
version: 2.0.0b58
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Trigger

**Package:** `flyte.remote`

Represents a trigger in the Flyte platform.



```python
class Trigger(
    pb2: trigger_definition_pb2.Trigger,
    details: TriggerDetails | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `trigger_definition_pb2.Trigger` | |
| `details` | `TriggerDetails \| None` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `automation_spec` | `None` | Get the automation specification for the trigger. |
| `id` | `None` | Get the unique identifier for the trigger. |
| `is_active` | `None` | Check if the trigger is currently active. |
| `name` | `None` | Get the name of the trigger. |
| `task_name` | `None` | Get the name of the task associated with this trigger. |
| `url` | `None` | Get the console URL for viewing the trigger. |

## Methods

| Method | Description |
|-|-|
| [`create()`](#create) | Create a new trigger in the Flyte platform. |
| [`delete()`](#delete) | Delete a trigger by its name. |
| [`get()`](#get) | Retrieve a trigger by its name and associated task name. |
| [`get_details()`](#get_details) | Get detailed information about this trigger. |
| [`listall()`](#listall) | List all triggers associated with a specific task or all tasks if no task name is provided. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`update()`](#update) | Pause a trigger by its name and associated task name. |


### create()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Trigger.create.aio()`.
```python
def create(
    cls,
    trigger: flyte.Trigger,
    task_name: str,
    task_version: str | None,
) -> Trigger
```
Create a new trigger in the Flyte platform.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `trigger` | `flyte.Trigger` | The flyte.Trigger object containing the trigger definition. |
| `task_name` | `str` | Optional name of the task to associate with the trigger. |
| `task_version` | `str \| None` | |

### delete()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Trigger.delete.aio()`.
```python
def delete(
    cls,
    name: str,
    task_name: str,
    project: str | None,
    domain: str | None,
)
```
Delete a trigger by its name.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `task_name` | `str` | |
| `project` | `str \| None` | |
| `domain` | `str \| None` | |

### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Trigger.get.aio()`.
```python
def get(
    cls,
    name: str,
    task_name: str,
) -> TriggerDetails
```
Retrieve a trigger by its name and associated task name.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `task_name` | `str` | |

### get_details()

```python
def get_details()
```
Get detailed information about this trigger.


### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Trigger.listall.aio()`.
```python
def listall(
    cls,
    task_name: str | None,
    task_version: str | None,
    limit: int,
) -> AsyncIterator[Trigger]
```
List all triggers associated with a specific task or all tasks if no task name is provided.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `task_name` | `str \| None` | |
| `task_version` | `str \| None` | |
| `limit` | `int` | |

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


### update()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Trigger.update.aio()`.
```python
def update(
    cls,
    name: str,
    task_name: str,
    active: bool,
)
```
Pause a trigger by its name and associated task name.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `task_name` | `str` | |
| `active` | `bool` | |

