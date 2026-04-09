---
title: NamedDelivery
version: 2.1.5
variants: +flyte +union
layout: py_api
---

# NamedDelivery

**Package:** `flyte.notify`

Use a pre-configured delivery channel by name.

Use this when your Flyte admin has configured a named delivery config
(e.g., a shared Slack webhook or email list) that you want to reference
without specifying the delivery details inline.



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

