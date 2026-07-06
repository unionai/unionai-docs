---
title: Slack
version: 2.5.7
variants: +flyte +union
layout: py_api
---

# Slack

**Package:** `flyte.notify`

Send Slack notifications with optional Block Kit formatting.



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
| `on_phase` | `typing.Union[flyte.models.ActionPhase, typing.Tuple[flyte.models.ActionPhase, ...]]` | ActionPhase(s) to trigger notification |
| `webhook_url` | `str` | Slack webhook URL |
| `message` | `typing.Optional[str]` | Simple text message (supports template variables) |
| `blocks` | `typing.Optional[typing.Tuple[typing.Dict[str, typing.Any], ...]]` | Optional Slack Block Kit blocks for rich formatting (if provided, message is ignored). See: https://api.slack.com/block-kit |

