---
title: EventWebhook
version: 2.4.4
variants: +flyte +union
layout: py_api
---

# EventWebhook

**Package:** `flyte`

Webhook configuration for an event notification.

When specified, the backend will POST to the given URL when the event is created.
The ``payload`` dict may contain the template variable ``{callback_uri}`` in any
string value — the backend replaces it with the actual URI that can be used to
signal the event.



## Parameters

```python
class EventWebhook(
    url: str,
    payload: typing.Optional[typing.Dict[str, typing.Any]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `url` | `str` | |
| `payload` | `typing.Optional[typing.Dict[str, typing.Any]]` | |

