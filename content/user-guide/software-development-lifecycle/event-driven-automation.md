---
title: Event-driven automation
description: Choose between a webhook, a schedule, and an artifact trigger — and make an automation that fires once per event rather than once per delivery.
icon: broadcast
weight: 1
variants: +flyte +union
---

# Event-driven automation

Every automation starts with a cause. Getting the cause right is most of the design, because it determines whether the automation is timely, whether it double-fires, and whether anyone can later explain why it ran.

## Choosing the cause

Flyte has three ways in, and they are not interchangeable.

| The cause is | Use | Why |
|---|---|---|
| A person did something in one of your team's tools | A [software development tool webhook](../../integrations/software-development-tools/_index) | Fires when it happens, carries who did it and to what |
| Time | A [schedule](../triggers/schedules) | Nothing external to depend on |
| New data exists | An [artifact trigger](../triggers/_index) | Fires on the thing you actually care about, not on a guess about when it will be ready |
| An external system can call you, but is not one of the five | A [custom provider](../../integrations/software-development-tools/_index) or a plain [FastAPI app](../apps/native-app-integrations/fastapi-app) | |
| Something outside needs to drive *Flyte itself* | [Flyte webhook](../apps/native-app-integrations/flyte-webhook) | It exposes Flyte's own operations over HTTP — the opposite direction from the rest of this page |

The common mistake is reaching for a schedule because it is the easiest thing to set up. A nightly job that rebuilds a dataset "after the upstream load finishes" encodes a hope about timing; it runs late on a good day and on stale data on a bad one, and the failure is silent. If what you mean is "when the data is there", say that.

{{< variant union >}}
{{< markdown >}}
[Artifact triggers](../triggers/artifact-triggers) are the way to say it: register the upstream output as an artifact, and the downstream run starts when a new version lands.
{{< /markdown >}}
{{< /variant >}}

Schedules are the right answer when time genuinely is the cause — a weekly report, a nightly compaction, a retention sweep.

## Receiving a webhook

A [webhook receiver](../../integrations/software-development-tools/_index) is an app that verifies an inbound delivery with the sending product's own scheme, normalizes it, and launches a run. One app can serve any combination of the five supported products.

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_webhooks.py" fragment=app lang=python >}}

Each provider's secret is mounted automatically, and the dashboard at `/` shows the payload URL to paste into the product's webhook form.

## Launch once per event, not once per delivery

This is the part that bites. **Webhook senders retry on any non-2xx response**, pollers overlap their windows, and operators re-trigger by hand. Without protection, one pull request becomes four triage runs — and you usually find out from the four duplicate comments it left.

`run_once` keys on the event rather than the delivery:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_webhooks.py" fragment=handler lang=python >}}

Three properties worth knowing before you rely on it:

- **Deduplication is keyed on a run label, not a run name.** Every run launched this way carries `dedupe=<key>`, and a launch is refused when a run already carrying that key is live or has succeeded.
- **Failed, aborted, and timed-out runs do not block.** Re-triggering after a failure is a retry, which is what an operator wants. This is a deliberate asymmetry, not an oversight.
- **`dedupe_key()` folds in the provider's timestamp.** Without that, every later change to one resource would collapse onto the first one's key and never launch again — which matters for `update`-shaped events, where that is most of the traffic.

The key is just a string. Build your own when you want a different scope — one run per thread rather than per message, say.

> [!WARNING] Idempotent runs are not idempotent side effects
> `run_once` guarantees one *run* per event. It does not make that run's effects safe to repeat, and two genuinely simultaneous deliveries can still both launch, because the label check is a read followed by a launch.
>
> Where a duplicate would be visible or harmful — a second comment, a second audit entry, a second charge — make the task itself idempotent too. The [ClickUp example](../../integrations/software-development-tools/clickup) shows the shape: read the current state, and do nothing if it is already right.

## Keep the receiver thin

The receiver should verify, decide, and launch. Nothing else.

It is an app, so it is a long-lived process on a request deadline — GitHub gives you ten seconds. Work done inside the handler is work that is not retried, not observable as a run, and not visible to anyone debugging later. Work done in the launched task gets all three.

This is also why handlers must `await run_once.aio(...)`: the blocking form stalls the app's event loop and takes the whole receiver down with it under load.

A second, more practical reason to keep them in separate files: importing a module that constructs a `WebhookAppEnvironment` requires `fastapi`, so folding the app in with the tasks puts `fastapi` in every task image.

## Scope what the automation may act on

`scopes` is an allowlist of repositories, channels, teams, lists, or project keys. Events from anywhere else are acknowledged — so the sender stops retrying — but never dispatched.

Set it. A receiver with no allowlist will act on any repository whose webhook is pointed at it, and the secret that authenticates deliveries says nothing about which repository is allowed to use it.

> [!NOTE] Events with no scope are also not dispatched
> An allowlist cannot vouch for an event it cannot attribute. This is the right behavior and a confusing one: it presents as "my webhook isn't firing". If a provider's events arrive unattributed, check the product page for where that provider finds its scope.

## Test the pieces separately

The order matters, because two different failures look identical from the outside — "nothing happened".

1. **Run the task directly.** `flyte run <file> <task> --...`. This proves the credentials and the logic, with no webhook involved.
2. **Replay a sample delivery.** Every provider plugin ships a real `SAMPLE_DELIVERY`; replaying it proves verification and parsing with no account at all.
3. **Deploy the receiver and send a real delivery.** Now the only untested thing left is the wiring.

Skipping to step 3 means debugging credentials, parsing, and network reachability at the same time.

## Next

- [Review and release gates](./review-and-release-gates) — what to do with the run once the event has started it.
- [Software development tools](../../integrations/software-development-tools/_index) — the five providers, their events, and their quirks.
- [Triggers](../triggers/_index) — schedules and artifact events.
