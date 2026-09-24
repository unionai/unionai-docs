---
title: Notifications
description: Send Slack, email, Teams, or webhook notifications when a run started by a trigger ends.
icon: bell
weight: 7
variants: +flyte +union
---

# Notifications

A nightly job that fails at 2 AM should reach someone on Slack, instead of waiting for a person to notice in the UI. Attach notifications to the trigger and every run it starts reports its outcome.

You can attach notifications to a trigger using the `notifications` parameter of `flyte.Trigger`.
Notifications fire when a triggered run reaches a terminal execution phase.

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="trigger-with-notifications" lang="python">}}

## Execution phases

The `on_phase` parameter accepts a single phase or a tuple of terminal phases from `flyte.models.ActionPhase`:

| Phase | Description                |
|-------|----------------------------|
| `ActionPhase.SUCCEEDED` | Run completed successfully |
| `ActionPhase.FAILED` | Run failed with an error  |
| `ActionPhase.TIMED_OUT` | Run exceeded its timeout  |
| `ActionPhase.ABORTED` | Run was manually aborted  |

To notify on multiple phases with the same notification:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/notifications/notifications.py" fragment="email-short-notification" lang="python">}}

## Template variables

All message fields support template variables that are substituted at delivery time:

| Variable           | Description                                            |
|--------------------|--------------------------------------------------------|
| `{{.Run.Project}}` | Project name                                           |
| `{{.Run.Domain}}`  | Domain name                                            |
| `{{.Run.Name}}`    | Run ID                                                 |
| `{{.Phase}}`       | Execution phase                                        |
| `{{.Error}}`       | Error message when failed or abort reason when aborted |

## Slack notifications

`notify.Slack` sends a message to a Slack channel via an [incoming webhook](https://api.slack.com/messaging/webhooks).

**Simple message:**

{{< code file="/unionai-examples/v2/user-guide/task-configuration/notifications/notifications.py" fragment="slack-notification" lang="python">}}

**Rich formatting with [Block Kit](https://api.slack.com/block-kit):**

Use `blocks` instead of `message` for structured layouts. When `blocks` is provided, `message` is ignored.

{{< code file="/unionai-examples/v2/user-guide/task-configuration/notifications/notifications.py" fragment="notification-blocks" lang="python">}}

## Email notifications

`notify.Email` sends an email notification. You can provide a plain-text `body`, an `html_body`, or both (the email is sent as multipart when both are present).

{{< code file="/unionai-examples/v2/user-guide/task-configuration/notifications/notifications.py" fragment="email-extended-notification" lang="python">}}

## Microsoft Teams notifications

`notify.Teams` sends a message to a Teams channel via an incoming webhook. Use `card` for [Adaptive Card](https://adaptivecards.io/designer/) formatting; when `card` is set, `title` and `message` are ignored.

{{< code file="/unionai-examples/v2/user-guide/task-configuration/notifications/notifications.py" fragment="teams-notification" lang="python">}}

## Custom webhook notifications

`notify.Webhook` sends an HTTP request to any endpoint. All string values in `headers` and `body` support template variables.

{{< code file="/unionai-examples/v2/user-guide/task-configuration/notifications/notifications.py" fragment="webhook-notification" lang="python">}}

To attach notifications to a single run instead of a trigger, see [Run with notifications](../tasks/task-deployment/run-with-notifications).
