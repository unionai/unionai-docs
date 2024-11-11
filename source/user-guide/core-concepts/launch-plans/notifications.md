# Notifications

A launch plan may be associated with one or more notifications, which are triggered when the launch plan's workflow is completed.

There are three types of notifications:
* `Email`: Sends an email to the specified recipients.
* `PagerDuty`: Sends a PagerDuty notification to the PagerDuty service (with recipients specified).
  PagerDuty then forwards the notification as per your PagerDuty configuration.
* `Slack`: Sends a Slack notification to the email address of a specified channel. This requires that you configure your Slack account to accept notifications.

Separate notifications can be sent depending on the specific end state of the workflow. The options are:
* `WorkflowExecutionPhase.ABORTED`
* `WorkflowExecutionPhase.FAILED`
* `WorkflowExecutionPhase.SUCCEEDED`
* `WorkflowExecutionPhase.TIMED_OUT`

For example:
```{literalinclude} ../../../_static/includes/core-concepts/launch-plans/notifications/example_1.py
:language: python
```
