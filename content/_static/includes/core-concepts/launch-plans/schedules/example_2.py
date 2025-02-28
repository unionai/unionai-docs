import union
from flytekit import CronSchedule


@union.task
def my_task(a: int, b: int, c: int) -> int:
    return a + b + c

@union.workflow
def my_workflow(a: int, b: int, c: int) -> int:
    return my_task(a=a, b=b, c=c)

union.LaunchPlan.get_or_create(
    workflow=my_workflow,
    name="my_workflow_custom_lp",
    fixed_inputs={"a": 3},
    default_inputs={"b": 4, "c": 5},
    schedule=CronSchedule(
        schedule="*/10 * * * *"
    )
)
