---
title: Notifications and observability
description: Close the loop — get a run's outcome to the people who need it, and know what production is doing without reading logs.
icon: bell
weight: 5
variants: +flyte +union
---

# Notifications and observability

An automation nobody hears about is only half built. This page covers getting an outcome to a person, and knowing what production is doing between outcomes.

## Two different jobs

Keep them apart, because conflating them is why alert channels get muted.

| | Notification | Observability |
|---|---|---|
| Answers | "This specific thing finished, or failed" | "What is the system doing in general" |
| Audience | Whoever must act | Whoever is investigating |
| Destination | Slack, email, a webhook | Traces and metrics in your own backend |
| Volume | Low, by design | High — queried, not read |

If every run posts to a channel, nobody reads the channel, and the one message that mattered is lost among the ones that did not.

## Notifying on a terminal state

The built-in path needs no plugin: [run with notifications](../tasks/task-deployment/run-with-notifications) fires when a run reaches a terminal state, and `flyte.notify` covers email, Slack, Teams, and a generic webhook. [Trigger notifications](../triggers/trigger-notifications) does the same for scheduled and artifact-triggered runs.

Reach for this first. It is declarative, it fires even when the task itself has died, and there is no code to maintain.

## Posting from inside a run

When the message needs content the run computed — which model won, what the evaluation said, which rows failed — post from inside it. The [Slack integration](../../integrations/software-development-tools/slack) covers the sends people otherwise hand-roll:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/slack/slack_tasks.py" fragment=task lang=python >}}

`post` returns the message's `ts`, which is both the thread anchor and the address `update` edits. That makes the progress-counter shape two calls rather than a stream of messages: post once when work starts, edit in place as it proceeds.

A long pipeline that posts one message and edits it is pleasant to follow. The same pipeline posting eleven messages is why the channel got muted.

> [!NOTE] One place can hold the bot token
> `notify` ships a ready-made task environment with a `send` task. Deploy it once and only it holds the token; every other run posts through `flyte.run(notify.send, ...)` without mounting a secret.
>
> This is worth doing for the blast radius alone: a bot token that can post anywhere the bot is invited should not be mounted on every task environment that happens to want to say something.

## Answering the person who asked

When a run was started by something a person did — a slash command, a button, an @-mention — the reply belongs where they are, not in a channel they would have to go and check.

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/slack/slack_webhooks.py" fragment=handler lang=python >}}

`respond` needs no token at all: it posts to the `response_url` every interaction and slash command carries, valid for 30 minutes and five uses. That makes it the zero-setup way for a launched run to answer the click that launched it.

Acknowledge from the handler and let the run post the real answer. Slack only shows a synchronous reply if it arrives within three seconds, and the work almost never does.

## Observability

Notifications tell you about one run. Observability answers questions you did not know to ask.

Flyte gives you run history, inputs and outputs, logs, and task reports out of the box, and for most debugging that is enough — the run that failed is right there with the inputs that failed it.

For questions spanning runs and services, export rather than scrape: [OpenTelemetry](../../integrations/opentelemetry/_index) sends task and agent telemetry to any OTLP backend, and [Grafana Agent](../../integrations/grafana-agent-observability/_index) is the pre-wired path to Grafana Cloud. Flyte spans then sit alongside your application's, so a slow request traced into a Flyte run stays one trace.

This matters most for agentic workloads, where the interesting question — why did it take nine turns — is about the shape of the trajectory rather than about any single step.

## Tracking what produced what

The question that recurs in a data or AI system is not "is it up" but **"which data and which model produced this output".**

{{< variant union >}}
{{< markdown >}}
[Artifacts](../artifacts/_index) answer it directly: register datasets and models as named, versioned artifacts and you get lineage across runs — which model version came from which training run, from which dataset version.
{{< /markdown >}}
{{< /variant >}}

Independently, [MLflow](../../integrations/mlflow/_index) and [Weights & Biases](../../integrations/wandb/_index) keep the metric history that tells you whether today's number is unusual. A single score is not interpretable; the same score against twenty weeks of history is.

And deploying with `--version <commit-sha>` (see [CI/CD deployments](../project-patterns/cicd)) is what ties a run back to a commit. It costs one flag, and it is the difference between "something changed" and "this changed".

## When production misbehaves

A rough order, cheapest first:

1. **Read the failed run.** Inputs, outputs, logs, report. Most failures are explained here, and the inputs that caused it are attached.
2. **Check whether the inputs are admissible.** If a [Pandera](../../integrations/pandera/_index) contract is in place, its report says whether the data moved. If one is not, this is the moment to add it — a surprising share of model regressions are upstream data problems.
3. **Compare against history.** Is this score unusual, or is it Tuesday?
4. **Re-run it.** A [retry](../tasks/task-configuration/retries-and-timeouts) that succeeds tells you the failure was transient — which is information, not a fix.
5. **Open the trace** when the question spans services.

Two things make this much faster, and both are set up before the incident rather than during it: typed task signatures, so a malformed input fails at the boundary rather than deep inside; and [error handling](../tasks/task-programming/error-handling) that distinguishes a recoverable failure from one that should stop the run.

## Closing the loop back to the tracker

The lifecycle closes where it started. A run that found something worth acting on can file it:

- [Linear](../../integrations/software-development-tools/linear), [Jira](../../integrations/software-development-tools/jira), or [ClickUp](../../integrations/software-development-tools/clickup) to open or update a ticket.
- [GitHub](../../integrations/software-development-tools/github) to comment on a pull request or publish a check run.

Make these idempotent. A retried run that files a second duplicate ticket is worse than one that files none — the duplicate costs someone a triage cycle every time, which is how an automation earns a reputation for noise and then gets switched off. Use `run_once` for the launch, and have the task check whether the ticket already exists before creating it; the [ClickUp example](../../integrations/software-development-tools/clickup) shows the shape.

## Next

- [Event-driven automation](./event-driven-automation) — where the loop starts.
- [Run with notifications](../tasks/task-deployment/run-with-notifications) — the declarative path.
- [Slack integration](../../integrations/software-development-tools/slack) — sends, approvals, and the receiver.
