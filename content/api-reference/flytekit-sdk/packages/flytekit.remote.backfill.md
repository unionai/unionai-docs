---
title: flytekit.remote.backfill
version: 1.16.10
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
) -> typing.Tuple[flytekit.core.workflow.WorkflowBase, datetime.datetime, datetime.datetime]
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



| Parameter | Type | Description |
|-|-|-|
| `start_date` | `datetime.datetime` | datetime generate a backfill starting at this datetime (exclusive) |
| `end_date` | `datetime.datetime` | datetime generate a backfill ending at this datetime (inclusive) |
| `for_lp` | `typing.Union[flytekit.core.launch_plan.LaunchPlan, flytekit.remote.entities.FlyteLaunchPlan]` | typing.Union[LaunchPlan, FlyteLaunchPlan] the backfill is generated for this launchplan |
| `parallel` | `bool` | if the backfill should be run in parallel. False (default) will run each bacfill sequentially |
| `per_node_timeout` | `datetime.timedelta` | timedelta Timeout to use per node |
| `per_node_retries` | `int` | int Retries to user per node |
| `failure_policy` | `typing.Optional[flytekit.core.workflow.WorkflowFailurePolicy]` | WorkflowFailurePolicy Failure policy to use for the backfill workflow :return: WorkflowBase, datetime datetime -&gt; New generated workflow, datetime for first instance of backfill, datetime for last instance of backfill |

