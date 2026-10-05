---
title: Notifications and observability
description: Get a run's outcome to the people who need it, and see what production is doing without reading logs.
icon: bell
weight: 5
variants: +flyte +union
---

# Notifications and observability

Notifications tell a person that a specific run finished or failed. Observability lets someone investigate what the system is doing across runs. Keep them separate: if every run posts to a channel, people mute the channel and miss the message that mattered.

| | Notification | Observability |
|---|---|---|
| Answers | "This run finished, or failed" | "What is the system doing" |
| Audience | Whoever must act | Whoever is investigating |
| Destination | Slack, email, or a webhook | Traces and metrics in your own backend |
| Volume | Low | High, and queried rather than read |

## Notify on a terminal state

Start with the built-in notifications, which need no plugin. [Run with notifications](../tasks/task-deployment/run-with-notifications) sends a message when a run reaches a terminal state, through email, Slack, Teams, or a generic webhook. [Trigger notifications](../triggers/trigger-notifications) does the same for triggered runs.

They are declarative, need no code, and fire even if the task itself crashed.

## Post from inside a run

When the message needs results the run computed, such as which model won or which rows failed, post from inside the run with the [Slack integration](../../integrations/software-development-tools/slack):

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/slack/slack_tasks.py" fragment=task lang=python >}}

`post` returns the message's `ts`, which serves as both the thread anchor and the ID that `update` edits. To report progress, post once when work starts and edit the message as it proceeds, instead of posting a new message at each step.

To limit which tasks hold the bot token, deploy the ready-made task environment in `notify` once, with `flyte.deploy(notify.env)`. Only that environment mounts the token. Other runs post by calling its `send` task, without mounting the secret.

## Reply to the person who asked

When a person started the run, with a slash command, a button, or a mention, reply where they are:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/slack/slack_webhooks.py" fragment=handler lang=python >}}

`respond` needs no token. It posts to the `response_url` that every interaction and slash command carries, which Slack accepts for 30 minutes and up to five times.

Acknowledge from the handler and let the run post the answer. Slack shows a synchronous reply only if it arrives within 3 seconds.

## Observe across runs

For a single failed run, the run itself is usually enough: it records inputs, outputs, logs, and task reports.

For questions that span runs and services, export telemetry. [OpenTelemetry](../../integrations/opentelemetry/_index) sends task and agent telemetry to any OTLP backend, and [Grafana Agent](../../integrations/grafana-agent-observability/_index) sends it to Grafana Cloud. Flyte spans then join your application's traces, so a request that calls into a Flyte run stays one trace. This is most useful for agents, where the question is often about the whole trajectory, such as why an answer took nine turns.

## Track what produced an output

Every run records its inputs, outputs, code version, and image. Deploy with `--version <commit-sha>`, as described in [CI/CD deployments](../project-patterns/cicd), to tie each run to a commit.

{{< variant union >}}
{{< markdown >}}
To trace an output to the data and model behind it, register datasets and models as [artifacts](../artifacts/_index). Artifacts record lineage across runs: which model version came from which training run, on which dataset version.
{{< /markdown >}}
{{< /variant >}}

[MLflow](../../integrations/mlflow/_index) and [Weights & Biases](../../integrations/wandb/_index) keep metric history, so you can tell whether a score is unusual compared with previous weeks.

## Investigate a failure

Work through these in order, cheapest first:

1. **Read the failed run:** its inputs, outputs, logs, and report.
2. **Check the inputs.** A [Pandera](../../integrations/pandera/_index) report shows whether the data changed. If you have no data contract yet, add one.
3. **Compare against history** to see whether the score is unusual.
4. **Re-run it.** If a [retry](../tasks/task-configuration/retries-and-timeouts) succeeds, the failure was transient.
5. **Open the trace** when the question spans services.

Two things set up in advance make this faster: typed task signatures, so a malformed input fails at the task boundary, and [error handling](../tasks/task-programming/error-handling) that separates recoverable failures from ones that should stop the run.

## File the result in your tracker

A run that finds something to act on can file it:

- Open or update a ticket in [Linear](../../integrations/software-development-tools/linear), [Jira](../../integrations/software-development-tools/jira), or [ClickUp](../../integrations/software-development-tools/clickup).
- Comment on a pull request or publish a check run in [GitHub](../../integrations/software-development-tools/github).

Make these tasks idempotent, so a retried run doesn't file a duplicate ticket. Launch with `run_once`, and have the task check whether the ticket exists before creating it. The [ClickUp example](../../integrations/software-development-tools/clickup) shows this.

## See also

- [Event-driven automation](./event-driven-automation) for what starts a run.
- [Run with notifications](../tasks/task-deployment/run-with-notifications) for declarative notifications.
- [Slack integration](../../integrations/software-development-tools/slack) for messages, approvals, and the receiver.
