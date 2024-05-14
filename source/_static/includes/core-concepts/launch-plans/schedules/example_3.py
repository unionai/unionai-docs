from flytekit import task, workflow, LaunchPlan, FixedRate
from datetime import datetime, timedelta

@task
def my_task(a: int, b: int, c: int) -> int:
    return a + b + c

@workflow
def my_workflow(a: int, b: int, c: int, kickoff_time: datetime ) -> str:
    return f"sum: {my_task(a=a, b=b, c=c)} at {kickoff_time}"

LaunchPlan.get_or_create(
    workflow=my_workflow,
    name="my_workflow_custom_lp",
    fixed_inputs={"a": 3},
    default_inputs={"b": 4, "c": 5},
    schedule=FixedRate(
        duration=timedelta(minutes=10),
        kickoff_time_input_arg="kickoff_time"
    )
)
