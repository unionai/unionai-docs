---
title: SandboxRun
description: "One run of a sandbox: its first, or one a resume started."
icon: braces
version: 0.26.0
variants: -flyte +union
layout: py_api
---

# SandboxRun

**Package:** `flyteplugins.union.remote`

One run of a sandbox: its first, or one a resume started.


## Parameters

```python
class SandboxRun(
    run: str,
    generation: int,
    phase: str,
    started_at: Optional[datetime] = None,
    ended_at: Optional[datetime] = None,
    kept: str = '',
)
```
| Parameter | Type | Description |
|-|-|-|
| `run` | `str` | |
| `generation` | `int` | |
| `phase` | `str` | |
| `started_at` | `Optional[datetime]` | |
| `ended_at` | `Optional[datetime]` | |
| `kept` | `str` | |

## Methods

| Method | Description |
|-|-|
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


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

