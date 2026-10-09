---
title: Slack
description: "Slack webhooks for Flyte: the Events API, interactivity, and slash commands."
icon: book
version: 2.11.2
variants: +flyte +union
layout: py_api
---

# Slack



Slack webhooks for Flyte: the Events API, interactivity, and slash commands.

Hand a `SlackProvider()` to a `WebhookAppEnvironment` and register handlers with the
typed constants in `events`. All three of Slack's delivery shapes arrive on the
same `/webhook/slack` route. Calling the Slack API is not this plugin's job —
use `slack_sdk` from your tasks. See `examples/external_saas_integrations`.
## Directory

### Classes

| Class | Description |
|-|-|
| [`SlackProvider`](./slackprovider) | Slack's webhook provider, with its defaults pre-wired. |

### Methods

| Method | Description |
|-|-|
| [`handshake()`](#handshake) | Answer Slack's reachability probes, sent before events flow. |
| [`parse()`](#parse) | Normalize any Slack delivery — event callback, interaction, or slash command. |
| [`verify()`](#verify) | Verify the `X-Slack-Signature` v0 HMAC, within the replay window. |


### Variables

| Property | Type | Description |
|-|-|-|
| `MAX_REQUEST_AGE_SECONDS` | `int` |  |
| `SAMPLE_DELIVERY` | `tuple` |  |

## Methods

#### handshake()

```python
def handshake(
    headers: Mapping[str, str],
    body: bytes,
) -> dict[str, Any] | None
```
Answer Slack's reachability probes, sent before events flow.

Two exist: the `url_verification` challenge on the Events API URL, and the
form-encoded `ssl_check` probe on interactivity and slash-command URLs.
Ordinary deliveries return None and proceed to verification.


| Parameter | Type | Description |
|-|-|-|
| `headers` | `Mapping[str, str]` | |
| `body` | `bytes` | |

#### parse()

```python
def parse(
    headers: Mapping[str, str],
    body: bytes,
) -> WebhookEvent
```
Normalize any Slack delivery — event callback, interaction, or slash command.


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
Verify the `X-Slack-Signature` v0 HMAC, within the replay window.


| Parameter | Type | Description |
|-|-|-|
| `body` | `bytes` | |
| `headers` | `Mapping[str, str]` | |
| `secret` | `str` | |

