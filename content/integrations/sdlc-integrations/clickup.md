---
title: ClickUp
description: Receive ClickUp task, list, and goal webhooks as Flyte runs.
icon: kanban
weight: 4
variants: +flyte +union
---

# ClickUp

Receive [ClickUp](https://developer.clickup.com/docs/webhooks) webhooks in Flyte and turn them into runs. See [SDLC integrations](./_index) for the shared model this builds on.

## Installation

```bash
pip install "flyteplugins-clickup[app]"
```

Requires Python 3.10 or later. The `app` extra pulls in `fastapi` and `uvicorn` for serving the receiver.

## The receiver

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/clickup/clickup_webhooks.py" fragment=app lang=python >}}

`CLICKUP_WEBHOOK_SECRET` is mounted for you from the provider's `default_secret_env`. Deliveries are verified against an HMAC-SHA256 in `X-Signature` — ClickUp's signature header is unprefixed by its own name, so it is `X-Signature` and not `X-Clickup-Signature`.

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/clickup/clickup_webhooks.py" fragment=handler lang=python >}}

### Setting up the webhook in ClickUp

**Space Settings → Integrations → Webhooks**:

1. **Endpoint** — the `/webhook/clickup` URL from the app's dashboard.
2. **Secret** — ClickUp generates it; store that value as the `clickup-webhook-secret` Flyte secret.
3. **Events** — select the events your handlers match.

## Events

ClickUp does **not** split type and action. The event name is one camelCase string, so `qualified_type` is `taskStatusUpdated` and `action` is `None`. Constants live in `flyteplugins.clickup.events`.

| Class | Members |
|---|---|
| `Task` | `CREATED`, `UPDATED`, `DELETED`, `PRIORITY_UPDATED`, `STATUS_UPDATED`, `ASSIGNEE_UPDATED`, `DUE_DATE_UPDATED`, `TAG_UPDATED`, `MOVED`, `COMMENT_POSTED`, `COMMENT_UPDATED`, `TIME_ESTIMATE_UPDATED`, `TIME_TRACKED_UPDATED` |
| `List` | `CREATED`, `UPDATED`, `DELETED` |
| `Folder` | `CREATED`, `UPDATED`, `DELETED` |
| `Space` | `CREATED`, `UPDATED`, `DELETED` |
| `Goal` | `CREATED`, `UPDATED`, `DELETED` |
| `KeyResult` | `CREATED`, `UPDATED`, `DELETED` |

### How events are scoped and deduped

`scope` is the **list id**, which is what `scopes=` matches. ClickUp puts the list id at the top level on list-scoped events and only on the nested task for task-scoped ones; the provider reads both, so a single allowlist attributes either kind.

`resource_id` is the task id, and `occurred_at` is the delivery timestamp — so each successive status change on one ticket gets its own dedupe key.

## The task it launches

ClickUp ships no official Python SDK, and its API is a handful of REST calls, so `httpx` directly beats a thin third-party wrapper.

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/clickup/clickup_tasks.py" fragment=task lang=python >}}

The pre-check is the interesting part, and generalizes beyond ClickUp. `run_once` guarantees one *run* per event; it does not make the run's side effects idempotent. ClickUp accepts a redundant status write, so without reading first, a redelivered webhook would leave a second, misleading entry in the ticket's audit log. Where a duplicate write would be visible or harmful, make the task idempotent too.

Mint an API token under **Settings → Apps → API Token**.

## Try it without a ClickUp workspace

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/clickup/clickup_tasks.py" fragment=replay lang=python >}}

```bash
flyte run --local clickup_tasks.py replay_sample_delivery
```

> [!NOTE] Why the replay asserts the header *name*
> `verify` and `SAMPLE_DELIVERY` agree with each other whatever the signature header is called, so a round trip is self-consistent for any name — and cannot catch a wrong one. That is exactly how ClickUp's header shipped as `X-Clickup-Signature` in releases before 2.10.7: conformance was green while every genuine delivery got a 401.
>
> Asserting the literal header a real delivery carries is the one check the round trip cannot make. It is worth copying into your own tests for any provider you add.

## Examples

Both files live in [`v2/integrations/flyte-plugins/clickup`](https://github.com/unionai/unionai-examples/tree/main/v2/integrations/flyte-plugins/clickup):

- `clickup_webhooks.py` — the receiver and a status-change handler.
- `clickup_tasks.py` — the idempotent close, and the offline replay.

## See also

- [SDLC integrations](./_index) for the shared model: the normalized event, `run_once`, and scoping.
- [ClickUp API reference](../../api-reference/integrations/sdlc-integrations/clickup/_index).
