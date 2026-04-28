---
title: Slack
version: 2.2.0
variants: +flyte +union
layout: py_api
---

# Slack

**Package:** `flyte.notify`

Send Slack notifications with optional Block Kit formatting.

    Example:
        ```python
        Slack(
            on_phase=ActionPhase.FAILED,
            webhook_url="https://hooks.slack.com/services/YOUR/WEBHOOK/URL",
            message="🚨 Task {task.name} failed: {run.error}
{run.url}",
        )
        ```

    Args:
        on_phase:ActionPhase(s) to trigger notification
        webhook_url: Slack webhook URL
        message: Simple text message (supports template variables)
        blocks: Optional Slack Block Kit blocks for rich formatting
            (if provided, message is ignored). See: https://api.slack.com/block-kit
    


## Parameters

```python
class Slack(
    on_phase: typing.Union[flyte.models.ActionPhase, typing.Tuple[flyte.models.ActionPhase, ...]],
    webhook_url: str,
    message: typing.Optional[str],
    blocks: typing.Optional[typing.Tuple[typing.Dict[str, typing.Any], ...]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `on_phase` | `typing.Union[flyte.models.ActionPhase, typing.Tuple[flyte.models.ActionPhase, ...]]` | |
| `webhook_url` | `str` | |
| `message` | `typing.Optional[str]` | |
| `blocks` | `typing.Optional[typing.Tuple[typing.Dict[str, typing.Any], ...]]` | |

