---
title: Run with notifications
weight: 11
variants: +flyte +union
---

# Run with notifications

You can attach notifications to a single run by passing them to `flyte.with_runcontext()`.
Notifications fire when the run reaches the terminal execution phase — no trigger or persistent deployment is required.

```python
import os
import flyte
from flyte import notify
from flyte.models import ActionPhase

env = flyte.TaskEnvironment(name="notify_example")

SLACK_WEBHOOK_URL = os.environ["SLACK_WEBHOOK_URL"]
NOTIFICATION_EMAIL = os.environ["NOTIFICATION_EMAIL"]


@env.task
def compute(x: int, y: int) -> int:
    return x + y


if __name__ == "__main__":
    result = flyte.with_runcontext(
        notifications=(
            notify.Slack(
                on_phase=ActionPhase.SUCCEEDED,
                webhook_url=SLACK_WEBHOOK_URL,
                message="Run {{.Run.Name}} succeeded.",
            ),
            notify.Email(
                on_phase=ActionPhase.FAILED,
                recipients=[NOTIFICATION_EMAIL],
                subject="ALERT: Run {{.Run.Name}} failed",
                body="Run: {{.Run.Name}}\nError: {{.Error}}",
            ),
        ),
    ).run(compute, x=3, y=7)
    print(f"Result: {result}")
```

Pass a single notification or a tuple of notifications. All notification types from `flyte.notify` are supported: `Slack`, `Email`, `Teams`, `Webhook`, and `NamedDelivery`.

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

```python
notify.Slack(
    on_phase=ActionPhase.FAILED,
    webhook_url=SLACK_WEBHOOK_URL,
    message="Run {{.Run.Name}} failed in {{.Run.Project}}/{{.Run.Domain}}: {{.Error}}",
)
```

**Rich formatting with [Block Kit](https://api.slack.com/block-kit):**

Use `blocks` instead of `message` for structured layouts. When `blocks` is provided, `message` is ignored.

```python
notify.Slack(
    on_phase=ActionPhase.SUCCEEDED,
    webhook_url=SLACK_WEBHOOK_URL,
    blocks=[
        {
            "type": "header",
            "text": {"type": "plain_text", "text": "Task Succeeded"},
        },
        {
            "type": "section",
            "fields": [
                {"type": "mrkdwn", "text": "*Run:*\n{{.Run.Name}}"},
                {"type": "mrkdwn", "text": "*Phase:*\n{{.Phase}}"},
            ],
        },
        {"type": "divider"},
        {
            "type": "context",
            "elements": [
                {"type": "mrkdwn", "text": "{{.Run.Project}}/{{.Run.Domain}}"},
            ],
        },
    ],
)
```

## Email notifications

`notify.Email` sends an email notification. Provide `body` for plain text, `html_body` for HTML, or both (sent as multipart).

```python
notify.Email(
    on_phase=ActionPhase.FAILED,
    recipients=[NOTIFICATION_EMAIL],
    cc=["team-lead@example.com"],
    subject="ALERT: Run {{.Run.Name}} failed",
    body="Run: {{.Run.Name}}\nError: {{.Error}}",
    html_body="<b>Error:</b> {{.Error}}<br>",
)
```

To receive emails locally while developing, start a debug SMTP server before running your script:

```bash
# Python >= 3.12
pip install aiosmtpd
sudo python -m aiosmtpd -n -l localhost:25
```

The server prints received emails to stdout. Port 25 requires root; use port 1025 as an alternative (update the SMTP port in your configuration accordingly).
