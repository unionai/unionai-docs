---
title: ConditionWebhook
version: 2.6.5
variants: +flyte +union
layout: py_api
---

# ConditionWebhook

**Package:** `flyte`

Webhook configuration for a condition notification.

When specified, the backend will POST to the given URL when the condition is created.
The `payload` dict may contain the template variable `{callback_uri}` in any
string value — the backend replaces it with the actual URI that can be used to
signal the condition.

```python
ConditionWebhook(
    url="https://example.com/hook",
    payload={"callback": "{callback_uri}", "condition": "approval_needed"},
)
```


## Parameters

```python
class ConditionWebhook(
    url: str,
    payload: typing.Optional[typing.Dict[str, typing.Any]] = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `url` | `str` | |
| `payload` | `typing.Optional[typing.Dict[str, typing.Any]]` | |

