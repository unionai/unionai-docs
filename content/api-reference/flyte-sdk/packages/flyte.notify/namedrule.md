---
title: NamedRule
version: 2.0.11
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# NamedRule

**Package:** `flyte.notify`

Reference a pre-defined notification rule by name.

    Use this when your Flyte admin has configured a named notification rule
    that you want to apply to your runs. Named rules define both the phases
    to monitor and the delivery channels to use.

    Example:
        ```python
        # As a trigger notification
        flyte.Trigger(
            name="hourly",
            automation=flyte.Cron("0 * * * *"),
            notifications=flyte.notify.NamedRule("oncall-alerts"),
        )

        # In with_runcontext
        flyte.with_runcontext(
            notifications=flyte.notify.NamedRule("oncall-alerts"),
        ).run(my_task, x=1)
        ```

    Args:
        name: The name of the pre-defined rule (scoped to project/domain).
    


## Parameters

```python
class NamedRule(
    name: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |

