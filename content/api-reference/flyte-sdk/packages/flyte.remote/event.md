---
title: Event
version: 2.4.4
variants: +flyte +union
layout: py_api
---

# Event

**Package:** `flyte.remote`

A remote Event registered within an action of a run.

Events pause a run until an external signal is delivered. On the backend an event is
backed by a *condition action*, so an ``Event`` simply wraps the condition
:class:`~flyteidl2.workflow.run_definition_pb2.Action` it represents.

Use :meth:`listall` to discover the events of a run, :meth:`get` to look one up by
name, and :meth:`signal` to resolve one with a typed payload.


## Parameters

```python
class Event(
    pb2: run_definition_pb2.Action,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `run_definition_pb2.Action` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `action_name` | `str` | The name of the condition action backing this event. |
| `expected_type` | `type \| None` | Python type the condition expects for its payload, derived from ``metadata.condition.type`` populated by the backend. Returns ``None`` if the underlying action is not a condition or the backend has not yet exposed the type (older deployments / older ``flyteidl2`` stubs). |
| `name` | `str` | The event name (the condition action's declared name). |
| `phase` | `str` | The current phase of the underlying condition action (e.g. ``RUNNING``). |
| `run_name` | `str` | The name of the run this event belongs to. |

## Methods

| Method | Description |
|-|-|
| [`get()`](#get) | Retrieve an existing Event by name within a run. |
| [`listall()`](#listall) | List all Events for a run, optionally filtered to a specific parent action. |
| [`signal()`](#signal) | Signal the event with the provided payload. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Event.get.aio()`.
```python
def get(
    cls,
    name: str,
    run_name: str,
    action_name: str | None,
) -> Event | None
```
Retrieve an existing Event by name within a run.

There is no dedicated get-event RPC, so this scans the run's condition actions
and returns the first whose name matches.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | The name of the Event. |
| `run_name` | `str` | The name of the Run the event belongs to. |
| `action_name` | `str \| None` | Optionally narrow to a specific parent action within the run. |

**Returns:** An Event instance if found, otherwise None.

### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Event.listall.aio()`.
```python
def listall(
    cls,
    run_name: str,
    action_name: str | None,
    limit: int,
) -> AsyncIterator[Event]
```
List all Events for a run, optionally filtered to a specific parent action.

Events are condition actions, so this lists the run's actions filtered (server
side) to ``ACTION_TYPE_CONDITION``.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `run_name` | `str` | The name of the Run to list events for (required). |
| `action_name` | `str \| None` | Optionally narrow to events whose parent is this action. |
| `limit` | `int` | The maximum number of events to fetch per page. |

**Returns:** An async iterator of Event instances.

### signal()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <Event instance>.signal.aio()`.
```python
def signal(
    payload: EventPayload,
)
```
Signal the event with the provided payload.

The payload must be one of: ``bool``, ``int``, ``float``, or ``str``.



| Parameter | Type | Description |
|-|-|-|
| `payload` | `EventPayload` | The value to signal the event with. |

**Raises**

| Exception | Description |
|-|-|
| `TypeError` | If the payload is not a supported type. |

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

