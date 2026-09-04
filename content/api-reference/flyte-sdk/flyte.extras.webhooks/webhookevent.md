---
title: WebhookEvent
description: "One inbound webhook, normalized across providers."
icon: braces
version: 2.7.0
variants: +flyte +union
layout: py_api
---

# WebhookEvent

**Package:** `flyte.extras.webhooks`

One inbound webhook, normalized across providers.



## Parameters

```python
class WebhookEvent(
    provider: str,
    event_type: str,
    action: str | None = None,
    delivery_id: str = '',
    resource_id: str | None = None,
    occurred_at: str | None = None,
    scope: str | None = None,
    title: str | None = None,
    url: str | None = None,
    actor: str | None = None,
    received_at: datetime.datetime = <lambda>(),
    payload: dict[str, typing.Any] = dict(),
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type | Description |
|-|-|-|
| `provider` | `str` | Which integration delivered this (`github`, `slack`, ...). |
| `event_type` | `str` | The provider's event type (`pull_request`, `Issue`, ...). |
| `action` | `str \| None` | The provider's action within that type (`opened`, `create`, ...), when it splits the two. None for providers that do not. |
| `delivery_id` | `str` | The provider's own id for this delivery, where it sends one. |
| `resource_id` | `str \| None` | The thing the event is about — issue key, task id, message timestamp. Used for dedupe and shown on the dashboard. |
| `occurred_at` | `str \| None` | The provider's timestamp for the change, when it sends one. Folded into the dedupe key so a *later* change to the same resource gets its own key. |
| `scope` | `str \| None` | The container the resource lives in — repository, channel, team, list, project. Matched against the app's allowlist. |
| `title` | `str \| None` | Human-readable summary, for the dashboard. |
| `url` | `str \| None` | Link back to the resource in the provider's UI. |
| `actor` | `str \| None` | Who caused the event. |
| `received_at` | `datetime.datetime` | |
| `payload` | `dict[str, typing.Any]` | The provider's original JSON, verbatim. |

## Properties

| Property | Type | Description |
|-|-|-|
| `qualified_type` | `str` | `type.action` when the provider splits the two, else `type`.  This is what handlers register against, and what the `events` constants spell out. A computed field rather than a plain property, so it appears in `/api/events` — a consumer of that endpoint should not have to reassemble it from `event_type` and `action`. |

## Methods

| Method | Description |
|-|-|
| [`dedupe_key()`](#dedupe_key) | A stable key for `flyte.extras.webhooks.run_once`. |


### dedupe_key()

```python
def dedupe_key()
```
A stable key for `flyte.extras.webhooks.run_once`.

Keyed on provider + qualified type + resource + the provider's own
timestamp. The timestamp is what makes this usable for `update`-shaped
events: without it, every later change to one resource would collapse
onto the first one's key and never launch. Events with no resource fall
back to the delivery id, which is unique per delivery.

The key is just a string — build your own and pass it to
`run_once` directly when you want a different scope, such as one
run per thread rather than one per message.


