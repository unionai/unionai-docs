from flytekit import task, workflow, LaunchPlan
from typing import List


@task
def my_task(a: int, b: int, c: int) -> int:
    return a + b + c


@workflow
def my_workflow(a: int, b: int, c: int) -> int:
    return my_task(a=a, b=b, c=c)


my_workflow_lp = LaunchPlan.get_or_create(my_workflow)


@workflow
def wf() -> List[int]:
    return [my_workflow_lp(a=i, b=i, c=i) for i in [1, 2, 3]]
