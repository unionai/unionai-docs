---
title: flytekit.remote.backfill
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.remote.backfill

## Directory

### Methods

| Method | Description |
|-|-|
| [`create_backfill_workflow()`](#create_backfill_workflow) | Generates a new imperative workflow for the launchplan that can be used to backfill the given launchplan. |


## Methods

#### create_backfill_workflow()

```python
def create_backfill_workflow(
    start_date: datetime.datetime,
    end_date: datetime.datetime,
    for_lp: typing.Union[flytekit.core.launch_plan.LaunchPlan, flytekit.remote.entities.FlyteLaunchPlan],
    parallel: bool,
    per_node_timeout: datetime.timedelta,
    per_node_retries: int,
    failure_policy: typing.Optional[flytekit.core.workflow.WorkflowFailurePolicy],
) -> n: WorkflowBase, datetime datetime -> New generated workflow, datetime for first instance of backfill, datetime for last instance of backfill
```
Generates a new imperative workflow for the launchplan that can be used to backfill the given launchplan.
This can only be used to generate  backfilling workflow only for schedulable launchplans

the Backfill plan is generated as (start_date - exclusive, end_date inclusive)

> [!NOTE]
> Correct usage for dates example

```python
lp = Launchplan.get_or_create(...)
start_date = datetime.datetime(2023, 1, 1)
end_date =  start_date + datetime.timedelta(days=10)
wf = create_backfill_workflow(start_date, end_date, for_lp=lp)
```
> [!WARNING]
> Incorrect date example

```python
wf = create_backfill_workflow(end_date, start_date, for_lp=lp) # end_date is before start_date
# OR
wf = create_backfill_workflow(start_date, start_date, for_lp=lp) # start and end date are same
```



| Parameter | Type |
|-|-|
| `start_date` | `datetime.datetime` |
| `end_date` | `datetime.datetime` |
| `for_lp` | `typing.Union[flytekit.core.launch_plan.LaunchPlan, flytekit.remote.entities.FlyteLaunchPlan]` |
| `parallel` | `bool` |
| `per_node_timeout` | `datetime.timedelta` |
| `per_node_retries` | `int` |
| `failure_policy` | `typing.Optional[flytekit.core.workflow.WorkflowFailurePolicy]` |

