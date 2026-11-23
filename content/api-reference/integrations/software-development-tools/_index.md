---
title: Software development tools
variants: +flyte +union
weight: 2
---

# Software development tools

API reference for the webhook provider plugins, one package per product. Each package contributes a `Provider` to the receiver in `flyte.extras.webhooks`.

The receiver itself (`WebhookAppEnvironment`, `WebhookEvent`, `Provider`, and `run_once`) is documented under [`flyte.extras.webhooks`](../../flyte-sdk/flyte.extras.webhooks/_index). Each package below adds its product's secret, verification, parsing, and event constants.

Two packages also provide task helpers:

- `flyteplugins-github`: `review_pr`, which pauses a run until a person reviews a pull request, and `mint_installation_token`, which creates short-lived GitHub App tokens.
- `flyteplugins-slack`: `approval`, which pauses a run until someone clicks a button, and `notify`, which posts, updates, and deletes messages.

For setup and examples, see the [Software development tools](../../../integrations/software-development-tools/_index) guide.

| Package | API reference | Guide | Verification |
| --- | --- | --- | --- |
| `flyteplugins-github` | [GitHub](./github/_index) | [GitHub](../../../integrations/software-development-tools/github) | HMAC-SHA256 (`X-Hub-Signature-256`) |
| `flyteplugins-slack` | [Slack](./slack/_index) | [Slack](../../../integrations/software-development-tools/slack) | HMAC-SHA256 with a five-minute replay window (`X-Slack-Signature`) |
| `flyteplugins-linear` | [Linear](./linear/_index) | [Linear](../../../integrations/software-development-tools/linear) | HMAC-SHA256 (`Linear-Signature`) |
| `flyteplugins-clickup` | [ClickUp](./clickup/_index) | [ClickUp](../../../integrations/software-development-tools/clickup) | HMAC-SHA256 (`X-Signature`) |
| `flyteplugins-jira` | [Jira](./jira/_index) | [Jira](../../../integrations/software-development-tools/jira) | Shared token (`X-Webhook-Token`) |

Each package's `events` module of constants, such as `events.PullRequest.OPENED`, isn't included in the generated reference. The constants are listed on each product's guide page.
