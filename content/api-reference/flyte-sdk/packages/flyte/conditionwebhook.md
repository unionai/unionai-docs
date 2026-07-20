---
title: ConditionWebhook
version: 2.5.11
variants: +flyte +union
layout: py_api
---

# ConditionWebhook

**Package:** `flyte`

Webhook configuration for a condition notification.

When specified, the backend will POST to the given URL when the condition is created.
The ``payload`` dict may contain the template variable ``{callback_uri}`` in any
string value — the backend replaces it with the actual URI that can be used to
signal the condition.



## Parameters

```python
class ConditionWebhook(
    url: str,
    payload: typing.Optional[typing.Dict[str, typing.Any]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `url` | `str` | |
| `payload` | `typing.Optional[typing.Dict[str, typing.Any]]` | |

