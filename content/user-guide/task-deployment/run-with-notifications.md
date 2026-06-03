---
title: Run with notifications
weight: 13
variants: +flyte +union
---

# Run with notifications

You can attach notifications to a single run by passing them to `flyte.with_runcontext()`.
Notifications fire when the run reaches the terminal execution phase — no trigger or persistent deployment is required.

{{< code file="/unionai-examples/v2/user-guide/task-deployment/run-with-notifications/run_with_notifications.py" fragment="run-with-notifications" lang="python">}}

Pass a single notification or a tuple of notifications. The notification types in `flyte.notify` are `Slack`, `Email`, `Teams`, `Webhook`, and `NamedDelivery`.

> [!NOTE]
> To attach notifications to every run created by a scheduled trigger, set `notifications` on the `flyte.Trigger` object instead. See [Notifications](../task-configuration/triggers#notifications).

## Execution phases

The `on_phase` parameter accepts a single phase or a tuple of phases from `flyte.models.ActionPhase`:

| Phase | Description |
|-------|-------------|
| `ActionPhase.SUCCEEDED` | Run completed successfully |
| `ActionPhase.FAILED` | Run failed with an error |
| `ActionPhase.TIMED_OUT` | Run exceeded its timeout |
| `ActionPhase.ABORTED` | Run was manually aborted |

## Template variables

All message fields support template variables substituted at delivery time:

| Variable | Description |
|----------|-------------|
| `{{.Run.Project}}` | Project name |
| `{{.Run.Domain}}` | Domain name |
| `{{.Run.Name}}` | Run ID |
| `{{.Phase}}` | Execution phase |
| `{{.Error}}` | Error message (failed) or abort reason (aborted) |

## Slack notifications

`notify.Slack` sends a message to a Slack channel via an [incoming webhook](https://api.slack.com/messaging/webhooks).

**Simple message:**

{{< code file="/unionai-examples/v2/user-guide/task-configuration/notifications/notifications.py" fragment="slack-notification" lang="python">}}

**Rich formatting with [Block Kit](https://api.slack.com/block-kit):**

Use `blocks` instead of `message` for structured layouts. When `blocks` is provided, `message` is ignored.

{{< code file="/unionai-examples/v2/user-guide/task-configuration/notifications/notifications.py" fragment="notification-blocks" lang="python">}}

## Email notifications

`notify.Email` sends an email notification. Provide `body` for plain text, `html_body` for HTML, or both (sent as multipart).

{{< code file="/unionai-examples/v2/user-guide/task-configuration/notifications/notifications.py" fragment="email-extended-notification" lang="python">}}

To receive emails locally while developing, start a debug SMTP server before running your script:

```bash
# Python >= 3.12
pip install aiosmtpd
python -m aiosmtpd -n -l localhost:1025
```

The server prints received emails to stdout. Port 1025 needs no special privileges; to listen on the standard SMTP port 25 instead, run the command with `sudo`. Either way, set the SMTP port in your configuration to match.
