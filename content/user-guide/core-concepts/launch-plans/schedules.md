---
title: Schedules
weight: 4
variants: +flyte +serverless +byoc +selfmanaged
---

# Schedules

Launch plans let you schedule the invocation of your workflows.
A launch plan can be associated with one or more schedules, where at most one schedule is active at any one time.
If a schedule is activated on a launch plan, the workflow will be invoked automatically by the system at the scheduled time with the inputs provided by the launch plan. Schedules can be either fixed-rate or `cron`-based.

To set up a schedule, you can use the `schedule` parameter of the `LaunchPlan.get_or_create()` method.

## Fixed-rate schedules

In the following example we add a [FixedRate](../../../api-reference/flytekit-sdk/packages/flytekit.core.schedule#flytekitcoreschedulefixedrate) that will invoke the workflow every 10 minutes.

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
Above, we defined the duration of the `FixedRate` schedule using `minutes`.
Fixed rate schedules can also be defined using `days` or `hours`.

## Cron schedules

A [`CronSchedule`](../../../api-reference/flytekit-sdk/packages/flytekit.core.schedule#flytekitcoreschedulecronschedule) allows you to specify a schedule using a `cron` expression:

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

### Cron expression format

A `cron` expression is a string that defines a schedule using five space-separated fields, each representing a time unit. The format of the string is:

```
minutes hours day-of-month month day-of-week year
```

Where each field can contain specific values, wildcards, and special characters. The fields are defined as follows:

| Field | Values | Special characters |
| `minutes` | `0-59` | `, - * /` |
| `hours` | `0-23` | `, - * /` |
| `day-of-month` | `1-31` | `, - * / ?` |
| `month` | `1-12 or JAN-DEC` | `, - * /` |
| `day-of-week` | `0-6 or SUN-SAT` | `, - * ?` |


The `,` (comma) is used to specify multiple values.
For example, in the `month` field, `JAN,FEB,MAR` means every January, February, and March.

The `-` (dash) specifies a range of values.
For example, in the `day-of-month` field, `1-15` means every day from `1` through `15` of the specified month.

The `*` (asterisk) specifies all values of the field.
For example, in the `hours` field, `*` means every hour (on the hour), from `0` to `23`.
You cannot use `*` in both the `day-of-month` and `day-of-week` fields in the same `cron` expression.
If you use it in one, you must use `?` in the other.

The `/` (slash) specifies increments.
For example, in the `minutes` field, `1/10` means every tenth minute, starting from the first minute of the hour (that is, the 11th, 21st, and 31st minute, and so on).

The `?` (question mark) specifies any value of the field.
For example, in the `day-of-month` field you could enter `7` and, if any day of the week was acceptable, you would enter `?` in the `day-of-week` field.

### Cron expression examples

`0 0 * * *`: Midnight every day.
`0 12 * * MON-FRI`: Noon every weekday.
`0 0 1 * *`: Midnight on the first day of every month.
`0 0 * JAN,JUL *`: Midnight every day in January and July.
`*/5 * * * *`: Every five minutes.
`30 2 * * 1`: At 2:30 AM every Monday.
`0 0 15 * ?`: Midnight on the 15th of every month.

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
