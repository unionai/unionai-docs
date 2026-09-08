---
title: Notification
description: "Base notification class."
icon: braces
version: 2.7.1
variants: +flyte +union
layout: py_api
---

# Notification

**Package:** `flyte.notify`

Base notification class.

All notification types must specify phases when they should trigger.


## Parameters

```python
class Notification(
    on_phase: typing.Union[flyte.models.ActionPhase, typing.Tuple[flyte.models.ActionPhase, ...]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `on_phase` | `typing.Union[flyte.models.ActionPhase, typing.Tuple[flyte.models.ActionPhase, ...]]` | |

