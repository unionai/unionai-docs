---
title: Event
version: 2.1.0
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# Event

**Package:** `flyteplugins.hitl`

An event that waits for human input via an embedded FastAPI app.

This class encapsulates the entire HITL functionality:
- Creates and serves a FastAPI app for receiving human input
- Provides endpoints for form-based and JSON-based submission
- Polls object storage for responses using durable sleep (crash-resilient)

The app is automatically served when the Event is created via `Event.create()`.
All infrastructure details (AppEnvironment, deployment) are abstracted away.



## Parameters

```python
class Event(
    name: str,
    scope: EventScope,
    data_type: Type[T],
    prompt: str,
    request_id: str,
    endpoint: str,
    request_path: str,
    response_path: str,
    timeout_seconds: int,
    poll_interval_seconds: int,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `scope` | `EventScope` | |
| `data_type` | `Type[T]` | |
| `prompt` | `str` | |
| `request_id` | `str` | |
| `endpoint` | `str` | |
| `request_path` | `str` | |
| `response_path` | `str` | |
| `timeout_seconds` | `int` | |
| `poll_interval_seconds` | `int` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `api_url` | `None` | API endpoint for programmatic submission. |
| `endpoint` | `None` | Base endpoint of the HITL app. |
| `form_url` | `None` | URL where humans can submit input for this event. |

## Methods

| Method | Description |
|-|-|
| [`create()`](#create) | Create a new human-in-the-loop event and serve the app. |
| [`wait()`](#wait) | Wait for human input and return the result. |


### create()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Event.create.aio()`.
```python
def create(
    cls,
    name: str,
    data_type: Type[T],
    scope: EventScope,
    prompt: str,
    timeout_seconds: int,
    poll_interval_seconds: int,
) -> 'Event[T]'
```
Create a new human-in-the-loop event and serve the app.

This method creates an event that waits for human input via the FastAPI app.
The app is automatically served if not already running. All infrastructure
details are abstracted away - you just get an event to wait on.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | A descriptive name for the event (used in logs and UI) |
| `data_type` | `Type[T]` | The expected type of the input (int, float, str, bool) |
| `scope` | `EventScope` | The scope of the event. Currently only "run" is supported. |
| `prompt` | `str` | The prompt to display to the human |
| `timeout_seconds` | `int` | Maximum time to wait for human input (default: 1 hour) |
| `poll_interval_seconds` | `int` | How often to check for a response (default: 5 seconds) |

**Returns**

An Event object that can be used to wait for the human input


### wait()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <Event instance>.wait.aio()`.
```python
def wait()
```
Wait for human input and return the result.

This method polls object storage for a response using durable sleep,
making it crash-resilient. If the task crashes and restarts, it will
resume polling from where it left off.



**Returns**

The value provided by the human, converted to the event's data_type


**Raises**

| Exception | Description |
|-|-|
| `TimeoutError` | If no response is received within the timeout |

