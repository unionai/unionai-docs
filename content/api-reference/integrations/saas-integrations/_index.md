---
title: SaaS integrations
variants: +flyte +union
weight: 2
---

# SaaS integrations

API reference for the SaaS webhook provider plugins — one package per product, each contributing a single `Provider` to the receiver that ships with Flyte.

The shared machinery is not here. `WebhookAppEnvironment`, `WebhookEvent`, `Provider`, and `run_once` live in the SDK, documented under [`flyte.extras.webhooks`](../../flyte-sdk/flyte.extras.webhooks/_index). What each package below adds is only what is specific to its product: which environment variable holds its secret, how to verify a delivery, how to parse one into a `WebhookEvent`, and the typed constants for its events.

Two packages carry more than that, in the places where Flyte can do something a vendor SDK cannot:

- `flyteplugins-slack` adds `approval` (post buttons, park the run on a condition, resume on the click) and `notify` (post, update, delete, respond).
- `flyteplugins-github` adds `review_pr` (park a run on a human review condition, get a typed decision back) and `mint_installation_token` (short-lived GitHub App tokens instead of a stored PAT).

For setup, patterns, and per-product examples, see the [SaaS integrations](../../../integrations/saas-integrations/_index) guide.

| Package | API reference | Guide | Verification |
| --- | --- | --- | --- |
| `flyteplugins-github` | [GitHub](./github/_index) | [GitHub](../../../integrations/saas-integrations/github) | HMAC-SHA256 (`X-Hub-Signature-256`) |
| `flyteplugins-slack` | [Slack](./slack/_index) | [Slack](../../../integrations/saas-integrations/slack) | HMAC-SHA256 with a replay window (`X-Slack-Signature`) |
| `flyteplugins-linear` | [Linear](./linear/_index) | [Linear](../../../integrations/saas-integrations/linear) | HMAC-SHA256 (`X-Linear-Signature`) |
| `flyteplugins-clickup` | [ClickUp](./clickup/_index) | [ClickUp](../../../integrations/saas-integrations/clickup) | HMAC-SHA256 (`X-Clickup-Signature`) |
| `flyteplugins-jira` | [Jira](./jira/_index) | [Jira](../../../integrations/saas-integrations/jira) | none — Jira does not sign; a shared token stands in |

> [!NOTE] Event constants are not in the generated reference
> Each package exports an `events` module of typed constants (`events.PullRequest.OPENED`, `events.Task.STATUS_UPDATED`). The generator documents classes and functions, not modules, so the constants are listed on each product's guide page instead.
