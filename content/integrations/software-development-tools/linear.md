---
title: Linear
description: Receive Linear issue, comment, and project webhooks as Flyte runs.
icon: list-check
weight: 3
variants: +flyte +union
---

# Linear

Receive [Linear](https://developers.linear.app/docs/graphql/webhooks) webhooks in Flyte and turn them into runs.

## Installation

```bash
pip install "flyteplugins-linear[app]"
```

Requires `flyteplugins-linear` 2.10.7 or later and Python 3.10 or later. Earlier releases read the wrong signature header and reject every delivery. The `app` extra adds `fastapi` and `uvicorn` for serving the receiver.

## The receiver

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/linear/linear_webhooks.py" fragment=app lang=python >}}

The provider reads its secret from `LINEAR_WEBHOOK_SECRET`, which the app mounts automatically. It verifies an HMAC-SHA256 signature in the `Linear-Signature` header. The header name has no `X-` prefix.

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/linear/linear_webhooks.py" fragment=handler lang=python >}}

### Set up the webhook in Linear

Go to **Settings → API → Webhooks → New webhook** and set:

1. **URL**: the `/webhook/linear` URL from the app's dashboard.
2. **Resource types**: the entities your handlers match.

Linear generates a signing secret for the webhook. Store it as the `linear-webhook-secret` Flyte secret.

## Events

Linear separates type and action, so `qualified_type` has the form `Issue.create`. Constants live in `flyteplugins.linear.events`. Every class has `ANY`, `CREATE`, `UPDATE`, and `REMOVE`.

| Class | Covers |
|---|---|
| `Issue` | Issues |
| `Comment` | Comments on issues |
| `IssueLabel` | Labels |
| `Project` | Projects |
| `ProjectUpdate` | Project updates |
| `Cycle` | Cycles |
| `Reaction` | Reactions |
| `Attachment` | Attachments |

### Scope and deduplication

`scope` is the team ID. Comment and Reaction payloads have no top-level team ID, so the provider reads it from the issue the comment or reaction belongs to.

`resource_id` is the entity's UUID. `occurred_at` is the entity's `updatedAt`, or the payload's `createdAt` for entities without one, so each edit to an issue gets its own dedupe key.

## The task it launches

Linear's API is a single GraphQL endpoint. The example calls it with the `gql` client:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/linear/linear_tasks.py" fragment=task lang=python >}}

Pass the API key in the `Authorization` header without a `Bearer` prefix. Create a key under **Settings → API → Personal API keys**.

## Test without a Linear workspace

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/linear/linear_tasks.py" fragment=replay lang=python >}}

```bash
flyte run --local linear_tasks.py replay_sample_delivery
```

The replay also asserts that the signature arrives in `Linear-Signature`. A sign-and-verify round trip alone can't detect a wrong header name, because the sample's headers come from the same plugin. If you write your own provider, add the same check.

## Examples

Both files are in [`v2/integrations/flyte-plugins/linear`](https://github.com/unionai/unionai-examples/tree/main/v2/integrations/flyte-plugins/linear):

- `linear_webhooks.py`: the receiver and an issue-created handler.
- `linear_tasks.py`: commenting over GraphQL, and the offline replay.

## See also

- [Software development tools](./_index) for the event model, `run_once`, and scopes.
- [Linear API reference](../../api-reference/integrations/software-development-tools/linear/_index).
