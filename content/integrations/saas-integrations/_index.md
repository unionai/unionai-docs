---
title: SaaS integrations
description: Receive webhooks from GitHub, Slack, Linear, ClickUp, and Jira, and turn them into Flyte runs.
icon: broadcast
weight: 2
variants: +flyte +union
sidebar_expanded: false
---

# SaaS integrations

Most of what a team wants automated starts somewhere other than Flyte. A pull request opens, an issue is filed, someone types a slash command, a ticket changes status. The work that should follow is exactly the kind of thing Flyte is good at — typed, retried, observable, and auditable — but the trigger lives in GitHub or Linear or Slack.

These integrations close that gap. One app receives webhooks from any combination of five products, authenticates each delivery with that product's own scheme, normalizes it into a single event model, and launches a run **once per event** no matter how many times the delivery arrives.

## Supported products

| Product | Page | Package | Verification |
|---|---|---|---|
| [GitHub](https://docs.github.com/en/webhooks) | [GitHub](./github) | `flyteplugins-github` | HMAC-SHA256 (`X-Hub-Signature-256`) |
| [Slack](https://api.slack.com/apis/events-api) | [Slack](./slack) | `flyteplugins-slack` | HMAC-SHA256 with a replay window (`X-Slack-Signature`) |
| [Linear](https://developers.linear.app/docs/graphql/webhooks) | [Linear](./linear) | `flyteplugins-linear` | HMAC-SHA256 (`Linear-Signature`) |
| [ClickUp](https://developer.clickup.com/docs/webhooks) | [ClickUp](./clickup) | `flyteplugins-clickup` | HMAC-SHA256 (`X-Signature`) |
| [Jira](https://developer.atlassian.com/cloud/jira/platform/webhooks/) | [Jira](./jira) | `flyteplugins-jira` | **none** — Jira does not sign; a shared token stands in |

Install the packages for the products you wire up. The receiver itself ships with Flyte, so there is no core package to add:

```bash
pip install "flyteplugins-github[app]"
```

The `[app]` extra pulls in `fastapi` and `uvicorn`. They are needed to *serve* the app, not to import the plugin, which is why they are an extra rather than a dependency.

## The division of labor

This is the part worth understanding before reading any single product's page, because it explains what you will and will not find in these packages.

**Flyte owns the hard half.** `flyte.extras.webhooks` ships with the SDK and supplies the app, the setup dashboard, dispatch, the scope allowlist, idempotent launching, the normalized event, and the verification primitives — the parts that are easy to get subtly wrong and expensive to get wrong once per product.

**A provider plugin owns only what is specific to its product:** which environment variable holds its secret, how to verify a delivery, how to parse one into an event, and the typed constants for its events. That is usually under 150 lines.

**Calling the product's API is nobody's job here.** There is deliberately no Flyte client wrapper around the GitHub or Slack or Jira API. Each vendor already ships (or the community maintains) a Python client tested against the live API by people who get deprecation notices first — and a Flyte task is just a function, so calling `PyGithub` or `slack_sdk` from one needs nothing in between. A wrapper would only add a surface to keep in sync with someone else's release calendar.

> [!NOTE] Two exceptions, and why they are exceptions
> A plugin earns a helper when it does something the vendor SDK *cannot*. Two do:
>
> - [`review_pr`](./github#human-review-gates) parks a run on a human decision and returns a typed verdict. The condition is Flyte's, not GitHub's.
> - [`approval.request`](./slack#approvals) posts buttons, parks the run, and resumes on the click. Same reason.
>
> Forwarding arguments and reshaping JSON does not earn a helper. Returning a `flyte.io.File` instead of an inline megabyte diff, rendering into the task report, or participating in caching and fan-out would.

## One app, many products

Each provider gets a route at `/webhook/<name>`; anything not configured returns 404. The dashboard at `/` shows one row per provider with its payload URL, whether its secret is mounted, and how it is verified — which is the page you copy from when filling in the product's webhook form.

```python
import flyte
from flyte.extras.webhooks import WebhookAppEnvironment
from flyteplugins.github import GitHubProvider
from flyteplugins.github import events as github_events
from flyteplugins.slack import SlackProvider

app_env = WebhookAppEnvironment(
    name="saas-webhooks",
    providers=[GitHubProvider(), SlackProvider()],
    scopes=["octo/repo"],
)


@app_env.on_event(github_events.PullRequest.OPENED)
async def triage(event): ...
```

Each provider's secret is mounted for you from its `default_secret_env`, so it does not need naming again in `secrets=`. Declare it explicitly only to point a provider at a secret stored under a different key.

## The normalized event

Five products, five payload shapes, one model. Handlers match on `qualified_type` and read the fields they need; `payload` always carries the provider's original JSON for anything the model does not surface.

| Field | What it holds |
|---|---|
| `provider` | Which integration delivered this — `github`, `slack`, … |
| `event_type` | The provider's event type — `pull_request`, `Issue`, `taskCreated` |
| `action` | The action within that type — `opened`, `create` — or `None` for providers that do not split the two |
| `qualified_type` | `type.action` when the provider splits them, else `type`. **This is what handlers register against**, and what the `events` constants spell out |
| `resource_id` | The thing the event is about — issue key, task id, message timestamp |
| `scope` | The container it lives in — repository, channel, team, list, project key. Matched against the app's allowlist |
| `occurred_at` | The provider's timestamp for the change, when it sends one |
| `title`, `url`, `actor` | Human-readable summary, link back, and who caused it |
| `payload` | The provider's original JSON, verbatim |

## Launch once per event, not once per delivery

Webhook senders retry on any non-2xx response, pollers overlap their windows, and operators re-trigger by hand. `run_once` makes all of that safe: the same event may be delivered any number of times and still produce one run.

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_webhooks.py" fragment=handler lang=python >}}

Deduplication is keyed on a run **label**, not a run name. Every run launched this way carries `dedupe=<key>`, and a launch is refused when a run already carrying that key is live or has succeeded. Failed, aborted, and timed-out runs do **not** block — re-triggering after a failure is a retry, which is what an operator wants.

`event.dedupe_key()` folds in the provider's own timestamp, which is what makes it usable for `update`-shaped events: without it, every later change to one resource would collapse onto the first one's key and never launch again. The key is just a string, so build your own and pass it directly when you want a different scope — one run per thread rather than one per message, say.

> [!WARNING] Handlers must await `run_once.aio(...)`
> The blocking form stalls the app's event loop, and webhook senders time deliveries out in seconds — GitHub gives you ten.
>
> Two *simultaneous* deliveries of one event can still both launch: the label check is a read followed by a launch, and closing that window needs a compare-and-set the control plane does not currently expose. Redeliveries are seconds to minutes apart and dedupe reliably. Where a double launch would do real damage, make the task itself idempotent too.

## Scope the app to what it should act on

`scopes` is an allowlist of repositories, channels, teams, lists, or project keys. Events from anywhere else are acknowledged — so the sender stops retrying — but never dispatched.

Events carrying **no** scope at all are also not dispatched: an allowlist cannot vouch for an event it cannot attribute. That is worth knowing before you conclude a webhook is not firing.

## Try one without an account

Every provider plugin ships a `SAMPLE_DELIVERY` — a trimmed but real payload, plus a function that signs it. It is what each plugin's own conformance test replays in CI, so `parse` is exercised against a body the product actually sent rather than one written to match the parser.

Be precise about what that does and does not cover, because the gap bit us. The **body** is real, so field extraction is checked against reality. The **headers** are fabricated by the plugin, so for anything whose name the plugin chooses — the signature header above all — the sample agrees with `verify` whatever that name is. ClickUp and Linear both shipped reading a header no real delivery carries, with conformance green and every genuine webhook getting a 401. Asserting the literal header name is a separate check, and the product pages show it.

That makes it the fastest way to see the shape of an event before wiring anything up:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_tasks.py" fragment=replay lang=python >}}

```bash
flyte run --local github_tasks.py replay_sample_delivery
```

## Receiver and tasks, kept apart

In the examples the receiver and the tasks it launches are separate files, deliberately. The app authenticates and dispatches; the tasks do the work, and can be deployed, run, tested, and retried on their own.

There is a practical reason too: importing a module that constructs a `WebhookAppEnvironment` requires `fastapi`, so folding the app in with the tasks would put `fastapi` in every task image.

Task names are qualified by their environment once deployed — `triage_pr` in the `github-triage` environment becomes `github-triage.triage_pr`, which is the name the receiver looks up.

```bash
# 1. deploy the tasks the receiver will launch
flyte deploy github_tasks.py env

# 2. run one directly, to confirm credentials work before any webhook is involved
flyte run github_tasks.py triage_pr --repo octo/repo --number 1

# 3. deploy the receiver, then point the product at the URL its dashboard shows
python github_webhooks.py
```

Step 2 is the one people skip and then regret: it separates "my credentials are wrong" from "my webhook is not arriving", which otherwise present identically.

## Not to be confused with

**[Flyte webhook](../../user-guide/apps/native-app-integrations/flyte-webhook)** is the mirror image of this: a prebuilt app exposing *Flyte's own* operations over HTTP, for things outside Flyte to call. The integrations here receive calls *from* SaaS products. Similar names, opposite directions.

**[Triggers](../../user-guide/triggers/_index)** fire runs on a schedule or on an artifact changing — Flyte's own event sources. Reach for a trigger when the cause is time or data; reach for a webhook when the cause is something a person did in another product.

## Next steps

- Pick a product page above for its events, setup steps, and quirks.
- [API reference](../../api-reference/integrations/saas-integrations/_index) for the five packages, and [`flyte.extras.webhooks`](../../api-reference/flyte-sdk/flyte.extras.webhooks/_index) for the shared core.

{{< subpage-cards >}}
