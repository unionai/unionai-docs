---
title: Human gates and approvals
description: Put a person in the loop with a durable condition, and decide what happens when nobody answers.
icon: person-check
weight: 3
variants: +flyte +union
---

# Human gates and approvals

Use a human gate for decisions that should not be automated, such as a production deploy, a schema migration, or an agent action with real consequences. The gate is an [external condition](../tasks/task-programming/conditions): an action that pauses a run until a signal arrives.

The wait is durable. The condition is stored on the backend, not held by a running process, so the run survives restarts, redeploys, and node failures, and can wait for days without using compute. A script that blocks on an HTTP long-poll loses the decision when its pod is rescheduled.

## Choose where the person answers

| Approach | The person answers in | Use it when |
|---|---|---|
| A [condition](../tasks/task-programming/conditions) | The {{< key product_name >}} UI | The approver works in {{< key product_name >}}, or needs the run's context to decide |
| A [Slack approval](../../integrations/software-development-tools/slack) | Slack, with a button | The approver works in chat |
| A [GitHub review gate](../../integrations/software-development-tools/github) | The {{< key product_name >}} UI, with the PR's metadata shown | The decision is about a specific pull request |

A Slack approval is a condition underneath. If nobody clicks the button in Slack, the same condition can still be answered in the {{< key product_name >}} UI.

## Ask in Slack

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/slack/slack_tasks.py" fragment=approval lang=python >}}

The task posts Block Kit buttons and pauses the run. When someone clicks a button, the receiver signals the condition and replaces the buttons with a "decided by" line. The button's `value` carries the run, action, and condition names, so the receiver needs only one setting to answer:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/slack/slack_webhooks.py" fragment=app lang=python >}}

## Set a timeout

A condition with no timeout waits indefinitely, and the run can sit "in progress" for weeks with nobody responsible for it.

`approval.request` times out after one hour by default. On expiry, `wait()` raises `flyte.errors.ConditionTimedoutError`. Catch it and decide what a timeout means:

- **No.** The right default for anything with consequences. Take the safe branch.
- **Escalate.** Ask again in another channel, or page someone.
- **Yes.** Rarely appropriate. If an unanswered hour counts as approval, the gate does not protect anything.

## Make the prompt decidable

The person answering is often not the author of the change, and may be on a phone. "Approve deploy?" sends them looking for context, so they approve without it or don't answer.

Put the facts needed to decide in the prompt: what is changing, what it was measured against, what the measurement showed, and what happens on "no". `review_pr` includes the pull request's metadata. For Slack, build a richer Block Kit message with `approval.blocks(...)`, including context, fields, and a link to the report. The registered handler still answers it.

## Control who can answer

Anyone who can see a Slack channel can click its buttons. For a low-stakes deploy, that is acceptable. Otherwise, post to a channel whose membership is the set of approvers, or use a condition answered in the {{< key product_name >}} UI, where platform permissions control access.

{{< variant union >}}
{{< markdown >}}
See [Resource management](../project-patterns/resource-management) for the RBAC primitives.
{{< /markdown >}}
{{< /variant >}}

## Keep human gates rare

A gate on every merge trains people to approve without reading. Gate on changes that are rare and consequential, such as a production promotion, a migration, or a first rollout to real traffic. If a human gate fires more than a few times a day, replace it with an [evaluation gate](./evaluation-gates) and an alert.

## Review AI output by exception

Reviewing AI output, such as a generated summary or an agent's proposed action, differs from approving a change because its volume grows with traffic. Send only the uncertain cases to a person:

1. Get a typed answer with a confidence score instead of free text. [TypeSafe AI](../../integrations/typesafe-ai/_index) does this, and [System one types](../system-one-types/_index) covers the pattern.
2. Act automatically on confident answers.
3. Pause the uncertain ones on a condition.
4. Record each human answer. These answers are labeled data for your next [evaluation set](./evaluation-gates).

## See also

- [External conditions](../tasks/task-programming/conditions) for the full condition API.
- [Evaluation gates](./evaluation-gates) for measurements that reduce how often a person must decide.
- [Slack integration](../../integrations/software-development-tools/slack) for approvals, messages, and the receiver.
