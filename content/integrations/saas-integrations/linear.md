---
title: Linear
description: Receive Linear issue, comment, and project webhooks as Flyte runs.
icon: list-check
weight: 3
variants: +flyte +union
---

# Linear

Receive [Linear](https://developers.linear.app/docs/graphql/webhooks) webhooks in Flyte and turn them into runs. See [SaaS integrations](./_index) for the shared model this builds on.

## Installation

```bash
pip install "flyteplugins-linear[app]"
```

Requires Python 3.10 or later. The `app` extra pulls in `fastapi` and `uvicorn` for serving the receiver.

## The receiver

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/linear/linear_webhooks.py" fragment=app lang=python >}}

`LINEAR_WEBHOOK_SECRET` is mounted for you from the provider's `default_secret_env`. Deliveries are verified against an HMAC-SHA256 in `Linear-Signature` — note there is no `X-` prefix, which is unusual enough to look like a typo and is not one.

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/linear/linear_webhooks.py" fragment=handler lang=python >}}

### Setting up the webhook in Linear

**Settings → API → Webhooks → New webhook**:

1. **URL** — the `/webhook/linear` URL from the app's dashboard.
2. **Signing secret** — Linear generates it; store that value as the `linear-webhook-secret` Flyte secret.
3. **Resource types** — select the entities your handlers match.

## Events

Linear splits type and action, so `qualified_type` reads `Issue.create`. Constants live in `flyteplugins.linear.events`; every class carries `ANY`, `CREATE`, `UPDATE`, and `REMOVE`.

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

### How events are scoped and deduped

`scope` is the **team id**, which is what `scopes=` matches. There is a subtlety here worth knowing in advance, because the failure mode looks like "my webhook is not firing":

> [!NOTE] Comment and Reaction payloads carry no top-level team id
> The provider falls back to the team id nested on the issue. Without that fallback, a `scopes` allowlist would silently drop every non-`Issue` event as unattributable — events with no scope are acknowledged but never dispatched.

`resource_id` is the entity's UUID. `occurred_at` is the entity's `updatedAt`, falling back to the payload's `createdAt` for entities that carry no timestamp of their own — which is what lets a later edit to one issue launch its own run rather than collapsing onto the first one's key.

## The task it launches

Linear ships no official Python SDK and does not need one: its API is a single GraphQL endpoint, so `gql` is the maintained client and the task calls it directly.

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/linear/linear_tasks.py" fragment=task lang=python >}}

Linear takes the API key raw in the `Authorization` header, with no `Bearer` prefix. Mint one under **Settings → API → Personal API keys**.

## Try it without a Linear workspace

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/linear/linear_tasks.py" fragment=replay lang=python >}}

```bash
flyte run --local linear_tasks.py replay_sample_delivery
```

> [!NOTE] Why the replay asserts the header *name*
> `verify` and `SAMPLE_DELIVERY` agree with each other whatever the signature header is called, so a round trip is self-consistent for any name — and cannot catch a wrong one. That is exactly how Linear's header shipped as `X-Linear-Signature` in releases before 2.10.7: conformance was green while every genuine delivery got a 401.
>
> Asserting the literal header a real delivery carries is the one check the round trip cannot make. It is worth copying into your own tests for any provider you add.

## Examples

Both files live in [`v2/integrations/flyte-plugins/linear`](https://github.com/unionai/unionai-examples/tree/main/v2/integrations/flyte-plugins/linear):

- `linear_webhooks.py` — the receiver and an issue-created handler.
- `linear_tasks.py` — commenting over GraphQL, and the offline replay.

## See also

- [SaaS integrations](./_index) for the shared model: the normalized event, `run_once`, and scoping.
- [Linear API reference](../../api-reference/integrations/saas-integrations/linear/_index).
