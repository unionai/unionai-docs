---
title: SlackProvider
description: "Slack's webhook provider, with its defaults pre-wired."
icon: braces
version: 2.11.1
variants: +flyte +union
layout: py_api
---

# SlackProvider

**Package:** `flyteplugins.slack`

Slack's webhook provider, with its defaults pre-wired.

```python
from flyte.extras.webhooks import WebhookAppEnvironment
from flyteplugins.slack import SlackProvider

app_env = WebhookAppEnvironment(name="webhooks", providers=[SlackProvider()])
```

One route serves all three of Slack's delivery shapes, so point Event
Subscriptions, Interactivity & Shortcuts, and every slash command at the
same `/webhook/slack` URL.

`WebhookAppEnvironment` mounts `default_secret_env` for you, so it does not
need naming again in `secrets=`.



## Parameters

```python
class SlackProvider(
    secret_env: str | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `secret_env` | `str \| None` | Environment variable holding the secret. Pass one only to point this provider at a secret stored under a different name; otherwise `default_secret_env` applies. |

