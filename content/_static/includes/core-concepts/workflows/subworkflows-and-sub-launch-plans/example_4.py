import union
from typing import List


@union.task
def my_task(a: int, b: int, c: int) -> int:
    return a + b + c


@union.workflow
def my_workflow(a: int, b: int, c: int) -> int:
    return my_task(a=a, b=b, c=c)


my_workflow_lp = union.LaunchPlan.get_or_create(my_workflow)


@union.workflow
def wf() -> List[int]:
    return [my_workflow_lp(a=i, b=i, c=i) for i in [1, 2, 3]]
