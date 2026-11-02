---
title: NamedDelivery
description: "Use a pre-configured delivery channel by name."
icon: braces
version: 2.12.2
variants: +flyte +union
layout: py_api
---

# NamedDelivery

**Package:** `flyte.notify`

Use a pre-configured delivery channel by name.

Not yet supported: no backend resolves named delivery configs, and there is
no way to create one yet. A run or trigger that references a named delivery
config is rejected, or sends no notification. Use an inline notification
such as `Slack` or `Email` instead.

A named delivery config will hold the delivery details (e.g., a shared
Slack webhook or email list), so you can reference it without specifying
them inline.



## Parameters

```python
class NamedDelivery(
    on_phase: typing.Union[flyte.models.ActionPhase, typing.Tuple[flyte.models.ActionPhase, ...]],
    name: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `on_phase` | `typing.Union[flyte.models.ActionPhase, typing.Tuple[flyte.models.ActionPhase, ...]]` | ActionPhase(s) to trigger notification. |
| `name` | `str` | The name of the pre-configured delivery config (scoped to project/domain). |

