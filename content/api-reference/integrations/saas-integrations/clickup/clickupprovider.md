---
title: ClickUpProvider
description: "ClickUp's webhook provider, with its defaults pre-wired."
icon: braces
version: 2.10.6
variants: +flyte +union
layout: py_api
---

# ClickUpProvider

**Package:** `flyteplugins.clickup`

ClickUp's webhook provider, with its defaults pre-wired.

```python
from flyte.extras.webhooks import WebhookAppEnvironment
from flyteplugins.clickup import ClickUpProvider

app_env = WebhookAppEnvironment(name="webhooks", providers=[ClickUpProvider()])
```

`WebhookAppEnvironment` mounts `default_secret_env` for you, so it does not
need naming again in `secrets=`.



## Parameters

```python
class ClickUpProvider(
    secret_env: str | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `secret_env` | `str \| None` | Environment variable holding the secret. Pass one only to point this provider at a secret stored under a different name; otherwise `default_secret_env` applies. |

