---
title: Condition
description: "A remote Condition registered within an action of a run."
icon: braces
version: 2.14.0
variants: +flyte +union
layout: py_api
---

# Condition

**Package:** `flyte.remote`

A remote Condition registered within an action of a run.

Conditions pause a run until an external signal is delivered. On the backend a condition is
backed by a *condition action*, so a `Condition` simply wraps the condition
`flyteidl2.workflow.run_definition_pb2.Action` it represents.

Use `Condition.listall` to discover the conditions of a run, `Condition.get` to look one up by
name, and `Condition.signal` to resolve one with a typed payload.

What the condition asks for (`prompt`, `prompt_type`, `description`, `timeout`) is not part of
the action listing; it is only returned by the action-details RPC. Call `Condition.fetch_details`
to load it, until then those properties are `None`.



## Parameters

```python
class Condition(
    pb2: run_definition_pb2.Action,
    details_pb2: run_definition_pb2.ActionDetails | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `run_definition_pb2.Action` | |
| `details_pb2` | `run_definition_pb2.ActionDetails \| None` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `action_name` | `str` | The name of the condition action backing this condition. |
| `description` | `str \| None` | The condition's description, or `None` if it has none or details are not loaded. |
| `expected_type` | `type \| None` | Python type the condition expects for its payload, derived from `metadata.condition.type` populated by the backend, falling back to the loaded details (see `fetch_details`). Returns `None` if the underlying action is not a condition or the backend has not exposed the type (older deployments / older `flyteidl2` stubs). |
| `name` | `str` | The condition name (the condition action's declared name). |
| `phase` | `str` | The current phase of the underlying condition action (e.g. `RUNNING`). |
| `prompt` | `str \| None` | The prompt text the condition shows whoever signals it, or `None` if details are not loaded. |
| `prompt_type` | `str \| None` | How `prompt` should be rendered: `"text"` or `"markdown"`, or `None` if unknown. |
| `run_name` | `str` | The name of the run this condition belongs to. |
| `timeout` | `timedelta \| None` | How long the condition waits for a signal before timing out, or `None` if it waits forever or details are not loaded. |

## Methods

| Method | Description |
|-|-|
| [`fetch_details()`](#fetch_details) | Load what the condition is asking for: its prompt, description and timeout. |
| [`get()`](#get) | Retrieve an existing Condition by name within a run. |
| [`listall()`](#listall) | List all Conditions for a run, optionally filtered to a specific parent action. |
| [`signal()`](#signal) | Signal the condition with the provided payload. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


### fetch_details()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <Condition instance>.fetch_details.aio()`.
```python
def fetch_details()
```
Load what the condition is asking for: its prompt, description and timeout.

This is one action-details RPC for the condition action. The current object is left
unchanged; a new `Condition` carrying the details is returned.



**Returns:** A Condition whose `prompt`, `prompt_type`, `description` and `timeout` are populated.

### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Condition.get.aio()`.
```python
def get(
    cls,
    name: str,
    run_name: str,
    action_name: str | None = None,
) -> Condition | None
```
Retrieve an existing Condition by name within a run.

There is no dedicated get-condition RPC, so this scans the run's condition actions
and returns the first whose name matches.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | The name of the Condition. |
| `run_name` | `str` | The name of the Run the condition belongs to. |
| `action_name` | `str \| None` | Optionally narrow to a specific parent action within the run. |

**Returns:** A Condition instance if found, otherwise None.

### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Condition.listall.aio()`.
```python
def listall(
    cls,
    run_name: str,
    action_name: str | None = None,
    limit: int = 100,
) -> AsyncIterator[Condition]
```
List all Conditions for a run, optionally filtered to a specific parent action.

Conditions are condition actions, so this lists the run's actions filtered (server
side) to `ACTION_TYPE_CONDITION`.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `run_name` | `str` | The name of the Run to list conditions for (required). |
| `action_name` | `str \| None` | Optionally narrow to conditions whose parent is this action. |
| `limit` | `int` | The maximum number of conditions to fetch per page. |

**Returns:** An async iterator of Condition instances.

### signal()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <Condition instance>.signal.aio()`.
```python
def signal(
    payload: ConditionPayload,
)
```
Signal the condition with the provided payload.

The payload must be one of: `bool`, `int`, `float`, or `str`.



| Parameter | Type | Description |
|-|-|-|
| `payload` | `ConditionPayload` | The value to signal the condition with. |

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

