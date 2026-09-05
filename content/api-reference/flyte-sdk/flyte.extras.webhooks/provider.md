---
title: Provider
description: "Everything core needs to accept one product's webhooks."
icon: braces
version: 2.7.1
variants: +flyte +union
layout: py_api
---

# Provider

**Package:** `flyte.extras.webhooks`

Everything core needs to accept one product's webhooks.



## Parameters

```python
class Provider(
    name: str,
    secret_env: str,
    verify: VerifyFn,
    parse: ParseFn,
    handshake: HandshakeFn | None = None,
    signed: bool = True,
    setup_hint: str = '',
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | URL segment and `WebhookEvent.provider` value. Must match the plugin's module name, so `/webhook/github` maps to `flyteplugins.github`. |
| `secret_env` | `str` | Environment variable holding the signing secret or shared token. `WebhookAppEnvironment` mounts a `flyte.Secret` for it automatically, so it rarely needs naming twice. Defaults to the subclass's `default_secret_env`. |
| `verify` | `VerifyFn` | Returns True when a delivery is authentic. |
| `parse` | `ParseFn` | Turns a verified delivery into a `WebhookEvent`. |
| `handshake` | `HandshakeFn \| None` | Optional setup handshake, answered before verification. |
| `signed` | `bool` | False when the product does not sign its webhooks at all, so the dashboard can say so rather than implying a guarantee that is absent. |
| `setup_hint` | `str` | Where to configure the webhook, shown on the dashboard. |

