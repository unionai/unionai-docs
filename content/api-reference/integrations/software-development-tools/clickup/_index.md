---
title: ClickUp
description: "ClickUp webhooks for Flyte."
icon: book
version: 2.11.2
variants: +flyte +union
layout: py_api
---

# ClickUp



ClickUp webhooks for Flyte.

Hand a `ClickUpProvider()` to a `WebhookAppEnvironment` and register handlers with the
typed constants in `events`. Calling the ClickUp API is not this plugin's job —
it is a handful of REST calls, so use `httpx` from your tasks. See
`examples/external_saas_integrations`.
## Directory

### Classes

| Class | Description |
|-|-|
| [`ClickUpProvider`](./clickupprovider) | ClickUp's webhook provider, with its defaults pre-wired. |

### Methods

| Method | Description |
|-|-|
| [`parse()`](#parse) | Normalize a ClickUp delivery into a `WebhookEvent`. |
| [`verify()`](#verify) | Verify the `X-Signature` HMAC over the raw body. |


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
Normalize a ClickUp delivery into a `WebhookEvent`.


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
Verify the `X-Signature` HMAC over the raw body.


| Parameter | Type | Description |
|-|-|-|
| `body` | `bytes` | |
| `headers` | `Mapping[str, str]` | |
| `secret` | `str` | |

