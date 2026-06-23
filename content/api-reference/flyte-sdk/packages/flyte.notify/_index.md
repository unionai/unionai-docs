---
title: flyte.notify
version: 2.5.2
variants: +flyte +union
layout: py_api
---

# flyte.notify

Task Notifications API for Flyte 2.0

Send notifications when tasks reach specific execution phases.
Supports Email, Slack, Teams, and custom Webhooks.

Quick Start:
    ```python
    import flyte
    import flyte.models
    from flyte import notify

    @flyte.task(
        trigger=flyte.Trigger(
            name="daily_report",
            automation=flyte.Cron("0 0 * * *"),
            notifications=[
                notify.Email(
                    on_phase=flyte.models.ActionPhase.FAILED,
                    recipients=["oncall@example.com"]
                ),
                notify.Slack(
                    on_phase=flyte.models.ActionPhase.SUCCEEDED,
                    webhook_url="https://hooks.slack.com/...",
                    message="Daily report completed! {{.Run.Name}}"
                )
            ]
        )
    )
    def daily_report():
        # Your task logic here
        pass
    ```

Available Notification Types:
    - Email: Send email notifications
    - Slack: Send Slack messages (with optional Block Kit)
    - Teams: Send Microsoft Teams messages (with optional Adaptive Cards)
    - Webhook: Send custom HTTP requests (most flexible)

Supported Phases:
    - SUCCEEDED: Task completed successfully
    - FAILED: Task failed
    - TIMED_OUT: Task timed out
    - ABORTED: Task was aborted

Template Variables:
    All notification messages support template variables:
    - {{.Run.Project}}: Run project name
    - {{.Run.Domain}}: Run domain name
    - {{.Run.Name}}: Run ID/name
    - {{.Phase}}: Terminal run phase
    - {{.Error}}: Error message (if failed)
## Directory

### Classes

| Class | Description |
|-|-|
| [`Email`](../flyte.notify/email) | Send email notifications. |
| [`NamedDelivery`](../flyte.notify/nameddelivery) | Use a pre-configured delivery channel by name. |
| [`NamedRule`](../flyte.notify/namedrule) | Reference a pre-defined notification rule by name. |
| [`Notification`](../flyte.notify/notification) | Base notification class. |
| [`Slack`](../flyte.notify/slack) | Send Slack notifications with optional Block Kit formatting. |
| [`Teams`](../flyte.notify/teams) | Send Microsoft Teams notifications with optional Adaptive Cards. |
| [`Webhook`](../flyte.notify/webhook) | Send custom HTTP webhook notifications (most flexible option). |

