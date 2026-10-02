---
title: JiraProvider
description: "Jira's webhook provider, with its defaults pre-wired."
icon: braces
version: 2.10.6
variants: +flyte +union
layout: py_api
---

# JiraProvider

**Package:** `flyteplugins.jira`

Jira's webhook provider, with its defaults pre-wired.

```python
from flyte.extras.webhooks import WebhookAppEnvironment
from flyteplugins.jira import JiraProvider

app_env = WebhookAppEnvironment(name="webhooks", providers=[JiraProvider()])
```

Jira does not sign its webhooks, so this provider authenticates with a
shared token instead and reports `signed=False` — which is what makes the
dashboard say so rather than implying a guarantee that is absent.

`WebhookAppEnvironment` mounts `default_secret_env` for you, so it does not
need naming again in `secrets=`.



## Parameters

```python
class JiraProvider(
    secret_env: str | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `secret_env` | `str \| None` | Environment variable holding the secret. Pass one only to point this provider at a secret stored under a different name; otherwise `default_secret_env` applies. |

