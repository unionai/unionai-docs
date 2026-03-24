---
title: NamedDelivery
version: 2.0.10
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# NamedDelivery

**Package:** `flyte.notify`

Use a pre-configured delivery channel by name.

    Use this when your Flyte admin has configured a named delivery config
    (e.g., a shared Slack webhook or email list) that you want to reference
    without specifying the delivery details inline.

    Example:
        ```python
        flyte.notify.NamedDelivery(
            on_phase=ActionPhase.FAILED,
            name="slack-oncall",
        )

        # Combine with inline notifications
        notifications=(
            flyte.notify.NamedDelivery(on_phase=ActionPhase.FAILED, name="slack-oncall"),
            flyte.notify.Email(
                on_phase=ActionPhase.SUCCEEDED,
                recipients=["team@example.com"],
            ),
        )
        ```

    Args:
        on_phase: ActionPhase(s) to trigger notification.
        name: The name of the pre-configured delivery config (scoped to project/domain).
    


## Parameters

```python
class NamedDelivery(
    on_phase: typing.Union[flyte.models.ActionPhase, typing.Tuple[flyte.models.ActionPhase, ...]],
    name: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `on_phase` | `typing.Union[flyte.models.ActionPhase, typing.Tuple[flyte.models.ActionPhase, ...]]` | |
| `name` | `str` | |

