---
title: SessionStartup
description: "How long each step of starting a session took, in seconds (``sb.startup``)."
icon: braces
version: 0.21.1
variants: -flyte +union
layout: py_api
---

# SessionStartup

**Package:** `flyteplugins.union.sandbox`

How long each step of starting a session took, in seconds (``sb.startup``).


## Parameters

```python
class SessionStartup(
    submit: float,
    ready: float,
    connect: float = 0.0,
)
```
| Parameter | Type | Description |
|-|-|-|
| `submit` | `float` | |
| `ready` | `float` | |
| `connect` | `float` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `total` | `float` | From asking for the session until it was usable. |

