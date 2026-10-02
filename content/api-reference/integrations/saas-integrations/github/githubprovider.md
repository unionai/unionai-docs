---
title: GitHubProvider
description: "GitHub's webhook provider, with its defaults pre-wired."
icon: braces
version: 2.10.6
variants: +flyte +union
layout: py_api
---

# GitHubProvider

**Package:** `flyteplugins.github`

GitHub's webhook provider, with its defaults pre-wired.

```python
from flyte.extras.webhooks import WebhookAppEnvironment
from flyteplugins.github import GitHubProvider

app_env = WebhookAppEnvironment(name="webhooks", providers=[GitHubProvider()])
```

Either content type in GitHub's *Add webhook* form works: `application/json`
and the default `application/x-www-form-urlencoded` normalize identically.

`WebhookAppEnvironment` mounts `default_secret_env` for you, so it does not
need naming again in `secrets=`.



## Parameters

```python
class GitHubProvider(
    secret_env: str | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `secret_env` | `str \| None` | Environment variable holding the secret. Pass one only to point this provider at a secret stored under a different name; otherwise `default_secret_env` applies. |

