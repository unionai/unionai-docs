---
title: flytekit.core.notification
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.notification


Notifications are primarily used when defining Launch Plans (also can be used when launching executions) and will trigger
the Flyte platform to send emails when a workflow run reaches certain stages (fails or succeeds, etc.).

Each notification type takes a list of {{< py_class_ref flytekit.models.core.execution.WorkflowExecutionPhase >}} and a list of
emails. Even though there are different notification classes in this module, they all just send email. The differentiation
offers semantic meaning to the end-user but do not functionally behave differently. Successful integration with Slack
and Pagerduty is incumbent on those email API being set-up correctly.

## Directory

### Classes

| Class | Description |
|-|-|
| [`Email`](../flytekit.core.notification/email) | This notification should be used when sending regular emails to people. |
| [`Notification`](../flytekit.core.notification/notification) |  |
| [`PagerDuty`](../flytekit.core.notification/pagerduty) | This notification should be used when sending emails to the PagerDuty service. |
| [`Slack`](../flytekit.core.notification/slack) | This notification should be used when sending emails to the Slack. |

