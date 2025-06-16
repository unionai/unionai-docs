---
title: Schedules
weight: 4
variants: +flyte +serverless +byoc +selfmanaged
---

# Schedules

Launch plans let you schedule the invocation of your workflows.
A launch plan can be associated with one or more schedules, where at most one schedule is active at any one time.
If a schedule is activated on a launch plan, the workflow will be invoked automatically by the system at the scheduled time with the inputs provided by the launch plan.

To add a schedule to a launch plan, add a schedule object to the launch plan, like this:

```python
from datetime import timedelta

import {{< key kit_import >}}
from flytekit import FixedRate

@{{< key kit_as >}}.task
def my_task(a: int, b: int, c: int) -> int:
    return a + b + c

@{{< key kit_as >}}.workflow
def my_workflow(a: int, b: int, c: int) -> int:
    return my_task(a=a, b=b, c=c)

{{< key kit_as >}}.LaunchPlan.get_or_create(
    workflow=my_workflow,
    name="my_workflow_custom_lp",
    fixed_inputs={"a": 3},
    default_inputs={"b": 4, "c": 5},
    schedule=FixedRate(
        duration=timedelta(minutes=10)
    )
)
```

Here we specify a [FixedRate]() schedule that will invoke the workflow every 10 minutes. Fixed rate schedules can also be defined using days or hours.
<!-- TODO: Add link to API -->


Alternatively, you can specify a [CronSchedule]():
<!-- TODO: Add link to API -->

```python
import {{< key kit_import >}}
from flytekit import CronSchedule


@{{< key kit_as >}}.task
def my_task(a: int, b: int, c: int) -> int:
    return a + b + c

@{{< key kit_as >}}.workflow
def my_workflow(a: int, b: int, c: int) -> int:
    return my_task(a=a, b=b, c=c)

{{< key kit_as >}}.LaunchPlan.get_or_create(
    workflow=my_workflow,
    name="my_workflow_custom_lp",
    fixed_inputs={"a": 3},
    default_inputs={"b": 4, "c": 5},
    schedule=CronSchedule(
        schedule="*/10 * * * *"
    )
)
```

## kickoff_time_input_arg

Both `FixedRate` and `CronSchedule` can take an optional parameter called `kickoff_time_input_arg`

This parameter is used to specify the name of a workflow input argument.
Each time the system invokes the workflow via this schedule, the time of the invocation will be passed to the workflow through the specified parameter.
For example:

```python
from datetime import datetime, timedelta

import {{< key kit_import >}}
from flytekit import FixedRate

@{{< key kit_as >}}.task
def my_task(a: int, b: int, c: int) -> int:
    return a + b + c

@{{< key kit_as >}}.workflow
def my_workflow(a: int, b: int, c: int, kickoff_time: datetime ) -> str:
    return f"sum: {my_task(a=a, b=b, c=c)} at {kickoff_time}"

{{< key kit_as >}}.LaunchPlan.get_or_create(
    workflow=my_workflow,
    name="my_workflow_custom_lp",
    fixed_inputs={"a": 3},
    default_inputs={"b": 4, "c": 5},
    schedule=FixedRate(
        duration=timedelta(minutes=10),
        kickoff_time_input_arg="kickoff_time"
    )
)
```

Here, each time the schedule calls `my_workflow`, the invocation time is passed in the `kickoff_time` argument.
