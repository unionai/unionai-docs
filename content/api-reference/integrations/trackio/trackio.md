---
title: Trackio
description: "Generates a Trackio dashboard link for Flyte."
icon: braces
version: 2.11.0
variants: +flyte +union
layout: py_api
---

# Trackio

**Package:** `flyteplugins.trackio`

Generates a Trackio dashboard link for Flyte.

The link resolution order is:

    1. Explicit server_url (self or context)
    2. Hugging Face Space (space_id)
    3. Hugging Face Trackio documentation



## Parameters

```python
class Trackio(
    host: str = 'https://huggingface.co',
    project: Optional[str] = None,
    server_url: Optional[str] = None,
    space_id: Optional[str] = None,
    name: str = 'Trackio',
)
```
| Parameter | Type | Description |
|-|-|-|
| `host` | `str` | Base Hugging Face host. |
| `project` | `Optional[str]` | Trackio project name. |
| `server_url` | `Optional[str]` | Base URL of a self-hosted Trackio instance. |
| `space_id` | `Optional[str]` | Hugging Face Space hosting the Trackio dashboard. |
| `name` | `str` | Display name in the Flyte UI. |

## Methods

| Method | Description |
|-|-|
| [`get_link()`](#get_link) | Resolve the Trackio dashboard URL. |


### get_link()

```python
def get_link(
    run_name: str,
    project: str,
    domain: str,
    context: Dict[str, str],
    parent_action_name: str,
    action_name: str,
    pod_name: str,
    **kwargs,
) -> str
```
Resolve the Trackio dashboard URL.


| Parameter | Type | Description |
|-|-|-|
| `run_name` | `str` | |
| `project` | `str` | |
| `domain` | `str` | |
| `context` | `Dict[str, str]` | |
| `parent_action_name` | `str` | |
| `action_name` | `str` | |
| `pod_name` | `str` | |
| `**kwargs` |  | |

