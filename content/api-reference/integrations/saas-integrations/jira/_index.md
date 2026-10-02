---
title: Jira
description: "Jira webhooks for Flyte."
icon: book
version: 2.10.6
variants: +flyte +union
layout: py_api
---

# Jira



Jira webhooks for Flyte.

Hand a `JiraProvider()` to a `WebhookAppEnvironment` and register handlers with the
typed constants in `events`. Calling the Jira API is not this plugin's job — use
the `jira` package from your tasks. See `examples/external_saas_integrations`.

Note Jira does not sign its webhooks; see `_provider` for what this plugin does
instead.
## Directory

### Classes

| Class | Description |
|-|-|
| [`JiraProvider`](./jiraprovider) | Jira's webhook provider, with its defaults pre-wired. |

### Methods

| Method | Description |
|-|-|
| [`parse()`](#parse) | Normalize a Jira delivery into a `WebhookEvent`. |
| [`verify()`](#verify) | Compare the `X-Webhook-Token` header against the shared token. |


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
Normalize a Jira delivery into a `WebhookEvent`.


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
Compare the `X-Webhook-Token` header against the shared token.


| Parameter | Type | Description |
|-|-|-|
| `body` | `bytes` | |
| `headers` | `Mapping[str, str]` | |
| `secret` | `str` | |

