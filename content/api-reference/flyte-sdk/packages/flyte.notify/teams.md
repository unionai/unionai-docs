---
title: Teams
version: 2.2.2
variants: +flyte +union
layout: py_api
---

# Teams

**Package:** `flyte.notify`

Send Microsoft Teams notifications with optional Adaptive Cards.

    Example:
        ```python
        Teams(
            on_phase=ActionPhase.SUCCEEDED,
            webhook_url="https://outlook.office.com/webhook/YOUR_WEBHOOK_URL",
            title="✅ Task Complete",
            message="Task {task.name} completed in {run.duration}
[View Details]({run.url})"
        )
        ```

    Args:
        on_phase:ActionPhase(s) to trigger notification
        webhook_url: Microsoft Teams webhook URL
        title: Message card title (supports template variables)
        message: Simple text message (supports template variables)
        card: Optional Adaptive Card for rich formatting
            (if provided, title and message are ignored).
            See: https://adaptivecards.io/designer/
    


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
| `on_phase` | `typing.Union[flyte.models.ActionPhase, typing.Tuple[flyte.models.ActionPhase, ...]]` | |
| `webhook_url` | `str` | |
| `title` | `str` | |
| `message` | `typing.Optional[str]` | |
| `card` | `typing.Optional[typing.Dict[str, typing.Any]]` | |

