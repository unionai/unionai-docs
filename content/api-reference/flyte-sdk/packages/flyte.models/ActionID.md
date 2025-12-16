---
title: ActionID
version: 2.0.0b38
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ActionID

**Package:** `flyte.models`

A class representing the ID of an Action, nested within a Run. This is used to identify a specific action on a task.


```python
class ActionID(
    name: str,
    run_name: str | None,
    project: str | None,
    domain: str | None,
    org: str | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `run_name` | `str \| None` | |
| `project` | `str \| None` | |
| `domain` | `str \| None` | |
| `org` | `str \| None` | |

## Methods

| Method | Description |
|-|-|
| [`create_random()`](#create_random) |  |
| [`new_sub_action()`](#new_sub_action) | Create a new sub-run with the given name. |
| [`new_sub_action_from()`](#new_sub_action_from) | Make a deterministic name. |


### create_random()

```python
def create_random()
```
### new_sub_action()

```python
def new_sub_action(
    name: str | None,
) -> ActionID
```
Create a new sub-run with the given name. If  name is None, a random name will be generated.


| Parameter | Type | Description |
|-|-|-|
| `name` | `str \| None` | |

### new_sub_action_from()

```python
def new_sub_action_from(
    task_call_seq: int,
    task_hash: str,
    input_hash: str,
    group: str | None,
) -> ActionID
```
Make a deterministic name


| Parameter | Type | Description |
|-|-|-|
| `task_call_seq` | `int` | |
| `task_hash` | `str` | |
| `input_hash` | `str` | |
| `group` | `str \| None` | |

