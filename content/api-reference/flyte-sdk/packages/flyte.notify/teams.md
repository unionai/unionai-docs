---
title: Teams
version: 2.5.9
variants: +flyte +union
layout: py_api
---

# Teams

**Package:** `flyte.notify`

Send Microsoft Teams notifications with optional Adaptive Cards.



## Parameters

```python
class Teams(
    on_phase: typing.Union[flyte.models.ActionPhase, typing.Tuple[flyte.models.ActionPhase, ...]],
    webhook_url: str,
    title: str,
    message: typing.Optional[str],
    card: typing.Optional[typing.Dict[str, typing.Any]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `on_phase` | `typing.Union[flyte.models.ActionPhase, typing.Tuple[flyte.models.ActionPhase, ...]]` | ActionPhase(s) to trigger notification |
| `webhook_url` | `str` | Microsoft Teams webhook URL |
| `title` | `str` | Message card title (supports template variables) |
| `message` | `typing.Optional[str]` | Simple text message (supports template variables) |
| `card` | `typing.Optional[typing.Dict[str, typing.Any]]` | Optional Adaptive Card for rich formatting (if provided, title and message are ignored). See: https://adaptivecards.io/designer/ |

