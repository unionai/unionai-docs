---
title: Software development tools
description: Receive webhooks from GitHub, Slack, Linear, ClickUp, and Jira, and turn them into Flyte runs.
icon: broadcast
weight: 2
variants: +flyte +union
sidebar_expanded: false
---

# Software development tools

These integrations launch Flyte runs from events in GitHub, Slack, Linear, ClickUp, and Jira: a pull request opens, an issue is filed, someone types a slash command, a ticket changes status.

One app receives webhooks from any combination of the five products. It verifies each delivery with that product's authentication scheme, converts it to a common event model, and launches a run once per event, however many times the delivery arrives.

## Supported products

| Product | Package | Verification |
|---|---|---|
| [GitHub](./github) | `flyteplugins-github` | HMAC-SHA256 (`X-Hub-Signature-256`) |
| [Slack](./slack) | `flyteplugins-slack` | HMAC-SHA256 with a five-minute replay window (`X-Slack-Signature`) |
| [Linear](./linear) | `flyteplugins-linear` | HMAC-SHA256 (`Linear-Signature`) |
| [ClickUp](./clickup) | `flyteplugins-clickup` | HMAC-SHA256 (`X-Signature`) |
| [Jira](./jira) | `flyteplugins-jira` | Shared token (`X-Webhook-Token`). Jira does not sign deliveries. |

## Quick start

Install the package for each product you connect:

```bash
pip install "flyteplugins-github[app]" "flyteplugins-slack[app]"
```

The `[app]` extra adds `fastapi` and `uvicorn`, which you need to serve the receiver. The receiver itself, `flyte.extras.webhooks`, ships with Flyte.

Define the receiver with one provider per product, and register a handler for each event you want to act on:

```python
import flyte
from flyte.extras.webhooks import WebhookAppEnvironment
from flyteplugins.github import GitHubProvider
from flyteplugins.github import events as github_events
from flyteplugins.slack import SlackProvider

app_env = WebhookAppEnvironment(
    name="devtools-webhooks",
    providers=[GitHubProvider(), SlackProvider()],
    scopes=["octo/repo"],
)


@app_env.on_event(github_events.PullRequest.OPENED)
async def triage(event): ...
```

The app serves:

- `/webhook/<provider>`, one route per configured provider. Requests for any other provider return 404.
- `/`, a setup dashboard listing each provider's payload URL, whether its secret is mounted, and how it is verified. Copy the payload URL from here into the product's webhook settings.

Each provider's secret is mounted automatically from its `default_secret_env`. Pass `secrets=` only to read a provider's secret from a different key.

The product pages cover each product's setup, events, and the tasks it launches.

## The event model

Every provider parses its deliveries into the same `WebhookEvent`. Handlers match on `qualified_type` and read the fields they need. `payload` holds the original JSON for anything the model doesn't surface.

| Field | Contents |
|---|---|
| `provider` | The integration that delivered the event: `github`, `slack`, and so on |
| `event_type` | The provider's event type: `pull_request`, `Issue`, `taskCreated` |
| `action` | The action within that type, such as `opened` or `create`. `None` for providers that don't separate type and action |
| `qualified_type` | `type.action` when the provider separates them, otherwise `type`. Handlers register against this value, and the `events` constants spell it out |
| `resource_id` | The object the event is about: issue key, task ID, message timestamp |
| `scope` | The container the object belongs to: repository, channel, team, list, project key. Matched against `scopes` |
| `occurred_at` | The provider's timestamp for the change, when it sends one |
| `title`, `url`, `actor` | A summary, a link to the object, and who caused the event |
| `payload` | The provider's original JSON |

## Launch one run per event

Senders retry failed deliveries, and operators resend them by hand. Use `run_once` to launch a run so that repeated deliveries of one event produce one run:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_webhooks.py" fragment=handler lang=python >}}

`run_once` labels each run it launches with `dedupe=<key>`. It skips the launch when a run with the same label is running or has succeeded. Failed, aborted, and timed-out runs don't block a new launch, so resending a delivery after a failure retries it.

`event.dedupe_key()` includes the provider's timestamp, so each later change to the same object launches its own run. To deduplicate at a different granularity, such as one run per Slack thread instead of one per message, build your own key string and pass it as `key=`.

> [!WARNING]
> Call `await run_once.aio(...)` in handlers. The blocking form stalls the app's event loop, and senders time out deliveries quickly. GitHub waits ten seconds.

Two deliveries of one event that arrive at the same moment can both launch a run, because the label check and the launch are separate steps. Ordinary retries arrive seconds or minutes apart and are deduplicated. If a duplicate run would cause harm, make the task idempotent.

## Restrict which events launch runs

Set `scopes` to the repositories, channels, teams, lists, or project keys the app should act on. The app acknowledges events from any other scope, so the sender stops retrying, but doesn't dispatch them.

When `scopes` is set, the app also skips events that carry no scope at all. If a handler never fires, check that the provider sets `scope` for that event type. The [Linear](./linear) and [ClickUp](./clickup) pages describe where each provider reads it from.

## Test without an account

Each provider package ships a `SAMPLE_DELIVERY`: a recorded payload and a function that signs it. Pass it through `verify` and `parse` to see the event your handler will receive, without connecting the product. Each product page has a `replay_sample_delivery` task that does this:

```bash
flyte run --local github_tasks.py replay_sample_delivery
```

The sample's body is a real delivery, but its headers are generated by the plugin. A replay checks parsing, not that the plugin reads the header the product actually sends.

## Deploy

Keep the receiver and the tasks it launches in separate files. The receiver needs `fastapi`, and keeping it out of the task module keeps `fastapi` out of the task image. Tasks can then be deployed, run, and tested on their own.

Once deployed, a task's name is qualified by its environment: `triage_pr` in the `github-triage` environment is `github-triage.triage_pr`. That's the name the handler passes to `remote.Task.get`.

```bash
# 1. Deploy the tasks the receiver launches
flyte deploy github_tasks.py env

# 2. Run one directly to confirm its credentials work
flyte run github_tasks.py triage_pr --repo octo/repo --number 1

# 3. Deploy the receiver, then copy its payload URL from the dashboard into the product
python github_webhooks.py
```

Step 2 separates a credentials problem from a delivery problem. From the receiver, the two look the same.

## Calling the product's API

These packages don't wrap the products' APIs. To act on GitHub, Slack, Linear, ClickUp, or Jira from a task, call the vendor's client, such as `PyGithub` or `slack_sdk`, directly.

Two helpers are the exception, because each pauses a run until a person decides:

- [`review_pr`](./github#human-review-gates) in `flyteplugins-github` waits for a pull-request review decision in the Flyte UI.
- [`approval.request`](./slack#approvals) in `flyteplugins-slack` waits for a button click in Slack.

## Related features

- [Flyte webhook](../../user-guide/apps/native-app-integrations/flyte-webhook) works in the opposite direction: it exposes Flyte's own operations over HTTP for other systems to call.
- [Triggers](../../user-guide/triggers/_index) launch runs on a schedule or when an artifact changes. Use a trigger when the cause is time or data, and a webhook when the cause is an action in another product.

## Next steps

- [API reference](../../api-reference/integrations/software-development-tools/_index) for the five packages, and [`flyte.extras.webhooks`](../../api-reference/flyte-sdk/flyte.extras.webhooks/_index) for the shared receiver.

{{< subpage-cards >}}
