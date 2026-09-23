---
title: When scheduled runs start
description: When the first run of a cron or fixed-rate trigger happens, depending on activation and `start_time`.
icon: hourglass-split
weight: 3
variants: +flyte +union
---

# When scheduled runs start

You deploy a trigger with `flyte.Cron("0 0 * * *")` at 17:00, and nothing runs for seven hours. That is expected: a schedule never fires on deploy. It waits for its next scheduled time.

The timing of the first run created by a trigger depends on the type of trigger used (Cron-based or Fixed-rate) and whether the trigger is active upon deployment.
A trigger with no automation never creates runs on its own; it only runs when [fired on demand](./manual-triggers#firing-a-trigger-on-demand).

## Cron-based triggers

For Cron-based triggers, the first run will be created at the next scheduled time according to the cron expression after trigger activation and similarly thereafter.

* `0 0 * * *` If deployed at 17:00 today, the trigger will first fire 7 hours later (0:00 of the following day) and then every day at 0:00 thereafter.

* `*/15 14 * * 1-5` if today is Tuesday at 17:00, the trigger will fire the next day (Wednesday) at 14:00, 14:15, 14:30, and 14:45 and then the same for every subsequent weekday thereafter.

## Fixed-rate triggers without `start_time`

If no `start_time` is specified, then the first run will be created after the specified interval from the time of activation. No run will be created immediately upon activation, but the activation time will be used as the reference point for future runs.

### No `start_time`, auto_activate: True

Let's say you define a fixed rate trigger with automatic activation like this:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="no-start-time-auto-activate-true" lang="python">}}

In this case, the first run will occur 60 minutes after the successful deployment of the trigger.
So, if you deployed this trigger at 13:15, the first run will occur at 14:15 and so on thereafter.

### No `start_time`, auto_activate: False

On the other hand, let's say you define a fixed rate trigger without automatic activation like this:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="no-start-time-auto-activate-false" lang="python">}}

Then you activate it after about 3 hours. In this case the first run will kick off 60 minutes after trigger activation.
If you deployed the trigger at 13:15 and activated it at 16:07, the first run will occur at 17:07.

## Fixed-rate triggers with `start_time`

If a `start_time` is specified, the timing of the first run depends on whether the trigger is active at `start_time` or not.

### Fixed-rate with `start_time` while active

If a `start_time` is specified, and the trigger is active at `start_time` then the first run will occur at `start_time` and then at the specified interval thereafter.
For example:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="fixed-rate-with-start-time-while-active" lang="python">}}

If you deploy this trigger on October 24th, 2025, the trigger will wait until October 26th 10:00am and will create the first run at exactly 10:00am.

### Fixed-rate with `start_time` while inactive

If a start time is specified, but the trigger is activated after `start_time`, then the first run will be created when the next time point occurs that aligns with the recurring trigger interval using `start_time` as the initial reference point.
For example:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="fixed-rate-with-start-time-while-inactive" lang="python">}}

If activated later than the `start_time`, say on October 28th 12:35pm for example, the first run will be created at October 28th at 1:00pm.
