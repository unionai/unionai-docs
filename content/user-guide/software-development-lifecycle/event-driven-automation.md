---
title: Event-driven automation
description: Choose what starts a run, and launch once per event rather than once per delivery.
icon: broadcast
weight: 1
variants: +flyte +union
---

# Event-driven automation

Every automation starts with a cause. The cause determines whether the automation runs on time, whether it fires twice, and whether anyone can later tell why it ran.

## Choose the cause

| The cause is | Use |
|---|---|
| A person acted in GitHub, Slack, Linear, ClickUp, or Jira | A [software development tool webhook](../../integrations/software-development-tools/_index). It fires when the action happens and carries who did what. |
| Time | A [schedule](../triggers/schedules). |
| Another external system calls you | A [custom provider](../../integrations/software-development-tools/_index) or a [FastAPI app](../apps/native-app-integrations/fastapi-app). |
| An outside system needs to drive Flyte itself | A [Flyte webhook](../apps/native-app-integrations/flyte-webhook), which exposes Flyte's own operations over HTTP. |

Use a schedule only when time is the cause, such as a weekly report or a nightly compaction. A nightly job that rebuilds a dataset "after the upstream load finishes" runs late when the load is early, and on stale data when the load is late. Neither failure raises an error.

{{< variant union >}}
{{< markdown >}}
When the cause is new data, use an [artifact trigger](../triggers/artifact-triggers). Register the upstream output as an artifact, and the downstream run starts when a new version is published.
{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}
When the cause is new data, start the downstream work at the end of the run that produces the data, rather than on a schedule.
{{< /markdown >}}
{{< /variant >}}

## Receive a webhook

A webhook receiver is an app that verifies each inbound delivery with the sending product's own scheme, normalizes it, and launches a run. One app can serve any combination of the five supported products:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_webhooks.py" fragment=app lang=python >}}

Each provider's secret is mounted automatically. The dashboard at `/` shows the payload URL to paste into the product's webhook settings.

## Launch once per event

Webhook senders retry on any non-2xx response, pollers overlap their windows, and operators re-trigger by hand. Without protection, one pull request can launch four triage runs and leave four comments.

`run_once` deduplicates on the event rather than the delivery:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_webhooks.py" fragment=handler lang=python >}}

How it behaves:

- Every run launched this way carries the label `dedupe=<key>`. A launch is refused if a run with that label is live or has succeeded.
- Failed, aborted, and timed-out runs don't block a new launch, so re-triggering after a failure retries the work.
- `dedupe_key()` includes the provider's timestamp, so a later change to the same resource gets a new key and launches a new run.
- The key is a string. Build your own for a different scope, such as one run per thread instead of one per message.

> [!WARNING] Make side effects idempotent
> `run_once` guarantees one run per event, not one side effect. Two deliveries that arrive at the same moment can both launch, because the label check is a read followed by a launch.
>
> Where a duplicate would be visible or harmful, such as a second comment or a second charge, make the task idempotent as well. The [ClickUp example](../../integrations/software-development-tools/clickup) reads the current state and does nothing if it is already correct.

## Keep the receiver thin

The receiver should verify, decide, and launch. Do the work in the launched task.

The receiver is an app with a request deadline: GitHub waits 10 seconds for a response. Work done in the handler isn't retried and doesn't appear as a run. Work done in the launched task is retried, observable, and recorded.

- Call `await run_once.aio(...)` in handlers. The blocking form stalls the app's event loop, and under load the receiver stops responding.
- Keep the app and the tasks in separate files. Importing a module that constructs a `WebhookAppEnvironment` requires `fastapi`, so a shared file puts `fastapi` in every task image.

## Restrict scopes

`scopes` is an allowlist of repositories, channels, teams, lists, or project keys. Events from anywhere else are acknowledged, so the sender stops retrying, but they are not dispatched.

Always set `scopes`. Without it, the receiver acts on any repository whose webhook points at it. The webhook secret authenticates the sender, not the repository.

Events that carry no scope are also not dispatched. If a webhook seems not to fire, check the product page for where that provider reads its scope from.

## Test in stages

When nothing happens, the cause could be credentials, parsing, or networking. Test in this order to separate them:

1. Run the task directly with `flyte run <file> <task>`. This tests the credentials and the logic without a webhook.
2. Replay the plugin's `SAMPLE_DELIVERY`. Every provider plugin ships one, so this tests verification and parsing without a product account.
3. Deploy the receiver and send a real delivery. This tests the remaining wiring.

## See also

- [Review and release gates](./review-and-release-gates) for what the launched run can do.
- [Software development tools](../../integrations/software-development-tools/_index) for each provider's events and setup.
- [Triggers](../triggers/_index) for schedules.
