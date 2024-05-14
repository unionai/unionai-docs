from flytekit import task, workflow, LaunchPlan, FixedRate
from datetime import timedelta

@task
def my_task(a: int, b: int, c: int) -> int:
    return a + b + c

@workflow
def my_workflow(a: int, b: int, c: int) -> int:
    return my_task(a=a, b=b, c=c)

LaunchPlan.get_or_create(
    workflow=my_workflow,
    name="my_workflow_custom_lp",
    fixed_inputs={"a": 3},
    default_inputs={"b": 4, "c": 5},
    schedule=FixedRate(
        duration=timedelta(minutes=10)
    )
)
