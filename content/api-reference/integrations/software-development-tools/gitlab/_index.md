---
title: GitLab
description: "GitLab webhooks for Flyte."
icon: book
version: 2.12.2
variants: +flyte +union
layout: py_api
---

# GitLab



GitLab webhooks for Flyte.

Hand a `GitLabProvider()` to a `WebhookAppEnvironment` and register handlers with the
typed constants in `events`:

```python
import flyte
from flyte.extras.webhooks import WebhookAppEnvironment, run_once
from flyteplugins.gitlab import GitLabProvider, events

# GitLabProvider.default_secret_env (GITLAB_WEBHOOK_TOKEN) is mounted for you.
app_env = WebhookAppEnvironment(name="gitlab-webhooks", providers=[GitLabProvider()])


@app_env.on_event(events.MergeRequest.OPEN)
async def triage(event):
    import flyte.remote as remote

    task = remote.Task.get(name="gitlab-triage.triage_mr", auto_version="latest")
    result = await run_once.aio(task, key=event.dedupe_key(), repo=event.scope)
    if not result.created:
        return {"skipped": result.run.name, "url": result.run.url}
    return {"run": result.run.name}
```

Note GitLab does not sign its webhooks; it authenticates with a shared token
sent verbatim in `X-Gitlab-Token` (the legacy *Secret token* mode — its newer
Standard-Webhooks *Signing token* mode, with `webhook-signature` /
`webhook-id` / `webhook-timestamp` headers, is not covered). See `_provider`
for what this plugin does with that. Calling the GitLab API (opening MRs, commenting, approving) is not
this plugin's job — use the `python-gitlab` package from your tasks, installed
via `flyteplugins-gitlab[gitlab]`. See `examples/external_saas_integrations`.
## Directory

### Classes

| Class | Description |
|-|-|
| [`GitLabProvider`](./gitlabprovider) | GitLab's webhook provider, with its defaults pre-wired. |

### Methods

| Method | Description |
|-|-|
| [`parse()`](#parse) | Normalize a GitLab delivery into a `WebhookEvent`. |
| [`verify()`](#verify) | Compare the `X-Gitlab-Token` header against the shared secret token. |


### Variables

| Property | Type | Description |
|-|-|-|
| `SAMPLE_DELIVERY` | `tuple` |  |

## Methods

#### parse()

```python
def parse(
    headers: Mapping[str, str],
    body: bytes,
) -> WebhookEvent
```
Normalize a GitLab delivery into a `WebhookEvent`.


| Parameter | Type | Description |
|-|-|-|
| `headers` | `Mapping[str, str]` | |
| `body` | `bytes` | |

#### verify()

```python
def verify(
    body: bytes,
    headers: Mapping[str, str],
    secret: str,
) -> bool
```
Compare the `X-Gitlab-Token` header against the shared secret token.


| Parameter | Type | Description |
|-|-|-|
| `body` | `bytes` | |
| `headers` | `Mapping[str, str]` | |
| `secret` | `str` | |

