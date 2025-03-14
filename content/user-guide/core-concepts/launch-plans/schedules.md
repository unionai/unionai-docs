---
title: Schedules
weight: 5
variants: +flyte +serverless +byoc +byok
---

# Schedules

Launch plans let you schedule the invocation of your workflows.
A launch plan can be associated with one or more schedules, where at most one schedule is active at any one time.
If a schedule is activated on a launch plan, the workflow will be invoked automatically by the system at the scheduled time with the inputs provided by the launch plan.

To add a schedule to a launch plan, add a schedule object to the launch plan, like this:

{{< code file="/_static/includes/core-concepts/launch-plans/schedules/example_1.py" lang="python" >}}

Here we specify a [FixedRate](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.FixedRate.html#flytekit.FixedRate) schedule that will invoke the workflow every 10 minutes. Fixed rate schedules can also be defined using days or hours.

Alternatively, you can specify a [CronSchedule](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.CronSchedule.html#flytekit.CronSchedule) that uses the Unix standard [cron format](https://en.wikipedia.org/wiki/Cron)(See [crontab guru](https://crontab.guru/) for a handy helper for cron expressions):

{{< code file="/_static/includes/core-concepts/launch-plans/schedules/example_2.py" lang="python" >}}

## kickoff_time_input_arg

Both `FixedRate` and `CronSchedule` can take an optional parameter called `kickoff_time_input_arg`

This parameter is used to specify the name of a workflow input argument.
Each time the system invokes the workflow via this schedule, the time of the invocation will be passed to the workflow through the specified parameter.
For example:

{{< code file="/_static/includes/core-concepts/launch-plans/schedules/example_3.py" lang="python" >}}

Here, each time the schedule calls `my_workflow`, the invocation time is passed in the `kickoff_time` argument.
