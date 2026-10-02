---
title: Linear
description: "Linear webhooks for Flyte."
icon: book
version: 2.10.6
variants: +flyte +union
layout: py_api
---

# Linear



Linear webhooks for Flyte.

Hand a `LinearProvider()` to a `WebhookAppEnvironment` and register handlers with the
typed constants in `events`. Calling the Linear API is not this plugin's job —
Linear's API is a single GraphQL endpoint, so use `gql` from your tasks. See
`examples/external_saas_integrations`.
## Directory

### Classes

| Class | Description |
|-|-|
| [`LinearProvider`](./linearprovider) | Linear's webhook provider, with its defaults pre-wired. |

### Methods

| Method | Description |
|-|-|
| [`parse()`](#parse) | Normalize a Linear delivery into a `WebhookEvent`. |
| [`verify()`](#verify) | Verify the `X-Linear-Signature` HMAC over the raw body. |


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
Normalize a Linear delivery into a `WebhookEvent`.


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
Verify the `X-Linear-Signature` HMAC over the raw body.


| Parameter | Type | Description |
|-|-|-|
| `body` | `bytes` | |
| `headers` | `Mapping[str, str]` | |
| `secret` | `str` | |

