---
title: ClickUp
description: Receive ClickUp task, list, and goal webhooks as Flyte runs.
icon: kanban
weight: 4
variants: +flyte +union
---

# ClickUp

Receive [ClickUp](https://developer.clickup.com/docs/webhooks) webhooks in Flyte and turn them into runs.

## Installation

```bash
pip install "flyteplugins-clickup[app]"
```

Requires `flyteplugins-clickup` 2.10.7 or later and Python 3.10 or later. Earlier releases read the wrong signature header and reject every delivery. The `app` extra adds `fastapi` and `uvicorn` for serving the receiver.

## The receiver

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/clickup/clickup_webhooks.py" fragment=app lang=python >}}

The provider reads its secret from `CLICKUP_WEBHOOK_SECRET`, which the app mounts automatically. It verifies an HMAC-SHA256 signature in the `X-Signature` header (not `X-Clickup-Signature`).

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/clickup/clickup_webhooks.py" fragment=handler lang=python >}}

### Set up the webhook in ClickUp

Go to **Space Settings → Integrations → Webhooks** and set:

1. **Endpoint**: the `/webhook/clickup` URL from the app's dashboard.
2. **Events**: the events your handlers match.

ClickUp generates a secret for the webhook. Store it as the `clickup-webhook-secret` Flyte secret.

## Events

ClickUp doesn't separate type and action. Each event name is a single camelCase string, so `qualified_type` is, for example, `taskStatusUpdated`, and `action` is `None`. Constants live in `flyteplugins.clickup.events`.

| Class | Members |
|---|---|
| `Task` | `CREATED`, `UPDATED`, `DELETED`, `PRIORITY_UPDATED`, `STATUS_UPDATED`, `ASSIGNEE_UPDATED`, `DUE_DATE_UPDATED`, `TAG_UPDATED`, `MOVED`, `COMMENT_POSTED`, `COMMENT_UPDATED`, `TIME_ESTIMATE_UPDATED`, `TIME_TRACKED_UPDATED` |
| `List` | `CREATED`, `UPDATED`, `DELETED` |
| `Folder` | `CREATED`, `UPDATED`, `DELETED` |
| `Space` | `CREATED`, `UPDATED`, `DELETED` |
| `Goal` | `CREATED`, `UPDATED`, `DELETED` |
| `KeyResult` | `CREATED`, `UPDATED`, `DELETED` |

### Scope and deduplication

`scope` is the list ID. List events carry it at the top level, and task events carry it on the nested task; the provider reads both.

`resource_id` is the task ID, and `occurred_at` is the delivery's `timestamp`, so each status change on a task gets its own dedupe key.

## The task it launches

ClickUp has no official Python SDK. The example calls its REST API with `httpx`:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/clickup/clickup_tasks.py" fragment=task lang=python >}}

The task reads the current status before writing a new one. `run_once` prevents duplicate runs, not duplicate side effects within a run. Without the check, a retried run would write the same status again and add a redundant entry to the task's activity log.

Create an API token under **Settings → Apps → API Token**.

## Test without a ClickUp workspace

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/clickup/clickup_tasks.py" fragment=replay lang=python >}}

```bash
flyte run --local clickup_tasks.py replay_sample_delivery
```

The replay also asserts that the signature arrives in `X-Signature`. A sign-and-verify round trip alone can't detect a wrong header name, because the sample's headers come from the same plugin. If you write your own provider, add the same check.

## Examples

Both files are in [`v2/integrations/flyte-plugins/clickup`](https://github.com/unionai/unionai-examples/tree/main/v2/integrations/flyte-plugins/clickup):

- `clickup_webhooks.py`: the receiver and a status-change handler.
- `clickup_tasks.py`: the idempotent status update, and the offline replay.

## See also

- [Software development tools](./_index) for the event model, `run_once`, and scopes.
- [Event-driven automation](../../user-guide/software-development-lifecycle/event-driven-automation) for the pattern across Linear, Jira, and ClickUp.
- [ClickUp API reference](../../api-reference/integrations/software-development-tools/clickup/_index).
