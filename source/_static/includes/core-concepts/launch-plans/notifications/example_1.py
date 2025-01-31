from datetime import datetime

import union

from flytekit import (
    WorkflowExecutionPhase,
    Email,
    PagerDuty,
    Slack
)

@union.task
def my_task(a: int, b: int, c: int) -> int:
    return a + b + c

@union.workflow
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
