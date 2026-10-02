---
title: Human gates and approvals
description: Put a person in the loop with a durable condition — and avoid the failure mode where the run waits forever.
icon: person-check
weight: 3
variants: +flyte +union
---

# Human gates and approvals

Some decisions should not be automated: a production deploy, a schema migration, a model that will touch customers, an agent action with real consequences. Flyte's answer is the [external condition](../tasks/task-programming/conditions) — a first-class action that pauses a run until a signal arrives.

The reason it is worth using rather than hand-rolling is narrow and important: **the waiting is durable.** The condition is state on the backend, not a held-open process. The run survives restarts, redeploys, and node failures while it waits, and it can wait for days without consuming anything. A script that blocks on an HTTP long-poll has none of those properties, and loses the decision when the pod is rescheduled.

## Three ways to ask

| Approach | The person answers in | Reach for it when |
|---|---|---|
| A bare [condition](../tasks/task-programming/conditions) | The Flyte UI | The approver already works in Flyte, or the decision needs run context to make |
| [Slack approval](../../integrations/software-development-tools/slack) | Slack, by clicking a button | The approver lives in chat and should not have to go find a UI |
| [GitHub review gate](../../integrations/software-development-tools/github) | The Flyte UI, with the PR's metadata inlined | The decision is about a specific pull request |

These are not exclusive. A Slack approval *is* a condition underneath, which has a consequence worth knowing: an approval that nobody clicks in Slack is not a stuck run, because the same condition is answerable from the Flyte UI. Either path resolves it.

## Asking in Slack

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/slack/slack_tasks.py" fragment=approval lang=python >}}

The task half posts Block Kit buttons and parks the run. The webhook half signals the condition when a button is clicked, then replaces the buttons with a "decided by" line so nobody clicks twice. The button's `value` carries the run, action, and condition names, so the receiver needs no configuration to answer — which is what one line switches on:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/slack/slack_webhooks.py" fragment=app lang=python >}}

## Design the waiting, not just the asking

Most problems with human gates are not about posting the prompt. They are about what happens when nobody answers.

### Always set a timeout

A condition with no timeout waits indefinitely. That is occasionally what you want and usually not — the common outcome is a run that has been "in progress" for three weeks and that nobody is accountable for.

`approval.request` defaults to one hour, which is a reasonable default precisely because it is short enough to notice. On expiry, `wait()` raises `flyte.errors.ConditionTimedoutError`, so decide what that means:

- **Timeout means no.** The right default for anything with consequences. Catch it and take the safe branch.
- **Timeout means escalate.** Re-ask in a different channel, or page someone.
- **Timeout means yes.** Almost never defensible for a gate worth having. If a silent hour is as good as an approval, the gate is theater.

### Make the prompt decidable

The person answering is usually not the person who wrote the change, and often not at a desk. A prompt that says "Approve deploy?" forces them to go and find out what is in it — so they either approve blindly or ignore it.

Put the decision-relevant facts in the prompt: what is changing, against what it was measured, what the measurement said, and what happens if they say no. `review_pr` does this by construction, inlining the pull request's metadata. `approval.blocks(...)` is exposed so you can build a richer Block Kit message — context, fields, a link to the report — and still have it answered by the registered handler.

### Be explicit about who may answer

A Slack button is answerable by anyone who can see the channel. For a low-stakes deploy that is fine and is most of the value. For anything else, post it to a channel whose membership *is* the authorization, or use a Flyte condition where access is governed by the platform's own permissions.

{{< variant union >}}
{{< markdown >}}
See [Resource management](../project-patterns/resource-management) for the RBAC primitives.
{{< /markdown >}}
{{< /variant >}}

### Do not put a human in a loop that runs often

A gate on every merge trains people to click without reading within about a week, and then you have the latency of a human gate with the assurance of none.

Gate on the things that are rare and consequential — a production promotion, a migration, a first rollout to real traffic. Let measurement gate the rest. If a human gate fires more than a few times a day, it has become a rubber stamp and should be replaced by an [evaluation gate](./evaluation-gates) with an alert.

## Human review of AI output

There is a distinct case worth separating: not "approve this change", but "is this *output* acceptable" — a generated summary, an agent's proposed action, a low-confidence classification.

The difference is volume. Change approvals are rare by nature; output reviews scale with traffic, so routing all of them to a person does not work. The usable pattern is to review **by exception**:

1. Get a typed answer with a confidence score, rather than free text. [TypeSafe AI](../../integrations/typesafe-ai/_index) does this; [System one types](../system-one-types/_index) covers the pattern.
2. Act automatically on confident answers.
3. Park only the uncertain ones on a condition.
4. Record the human's answer — it is labelled data, and it is the best source you will get for your next [evaluation set](./evaluation-gates).

That last step is the one most often skipped, and it is the one that compounds.

## Next

- [External conditions](../tasks/task-programming/conditions) — the mechanism, in full.
- [Evaluation gates](./evaluation-gates) — what to measure so fewer decisions need a person.
- [Slack integration](../../integrations/software-development-tools/slack) — approvals, sends, and the receiver.
