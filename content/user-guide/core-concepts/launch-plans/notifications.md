---
title: Notifications
weight: 3
variants: +flyte +serverless +byoc +byok
---

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

```python
from datetime import datetime

import union

from flytekit import (
    WorkflowExecutionPhase,
    Email,
    PagerDuty,
    Slack
)

@{{< key kit_as >}}.task
def my_task(a: int, b: int, c: int) -> int:
    return a + b + c

@{{< key kit_as >}}.workflow
def my_workflow(a: int, b: int, c: int, kickoff_time: datetime ) -> str:
    return f"sum: {my_task(a=a, b=b, c=c)} at {kickoff_time}"

union.LaunchPlan.get_or_create(
    workflow=my_workflow,
    name="my_workflow_custom_lp",
    fixed_inputs={"a": 3},
    default_inputs={"b": 4, "c": 5},
    notifications=[
        Email(
            phases=[WorkflowExecutionPhase.FAILED],
            recipients_email=["me@example.com", "you@example.com"],
        ),
        PagerDuty(
            phases=[WorkflowExecutionPhase.SUCCEEDED],
            recipients_email=["myboss@example.com"],
        ),
        Slack(
            phases=[
                WorkflowExecutionPhase.SUCCEEDED,
                WorkflowExecutionPhase.ABORTED,
                WorkflowExecutionPhase.TIMED_OUT,
            ],
            recipients_email=["your_slack_channel_email"],
        ),
    ],
)
```
