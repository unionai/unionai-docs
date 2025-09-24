---
title: Retries and timeouts
weight: 8
variants: +flyte +serverless +byoc +selfmanaged
---

# Retries and timeouts

Flyte provides robust error handling through configurable retry strategies and timeout controls.
These parameters help ensure task reliability and prevent resource waste from runaway processes.

## Retries

The `retries` parameter controls how many times a failed task should be retried before giving up.
A "retry" is any attempt after the initial attempt.
In other words, `retries=3` means the task may be attempted up to 4 times in total (1 initial + 3 retries).

The `retries` parameter can be configured in either the `@env.task` decorator or using `override` when invoking the task.
It cannot be configured in the `TaskEnvironment` definition.

The code for the examples below can be found on [GitHub](https://github.com/unionai/unionai-examples/blob/main/user-guide-v2/task-configuration/retries-and-timeouts/retries.py).

### Retry example

First we import the required modules and set up a task environment:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/retries-and-timeouts/retries.py" fragment="import-and-env" lang="python" >}}

Then we configure our task to retry up to 3 times if it fails (for a total of 4 attempts). We also define the driver task `main` that calls the `retry` task:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/retries-and-timeouts/retries.py" fragment="retry" lang="python" >}}

Note that we call `retry` twice: first without any `override`, and then with an `override` to increase the retries to 5 (for a total of 6 attempts).

Finally, we configure flyte and invoke the `main` task:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/retries-and-timeouts/retries.py" fragment="run" lang="python" >}}

## Timeouts

The `timeout` parameter sets limits on how long a task can run, preventing resource waste from stuck processes.
It supports multiple formats for different use cases.

The `timeout` parameter can be configured in either the `@env.task` decorator or using `override` when invoking the task.
It cannot be configured in the `TaskEnvironment` definition.

The code for the example below can be found on [GitHub](https://github.com/unionai/unionai-examples/blob/main/user-guide-v2/task-configuration/retries-and-timeouts/timeouts.py).

### Timeout example

First, we import the required modules and set up a task environment:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/retries-and-timeouts/timeouts.py" fragment="import-and-env" lang="python" >}}

Our first task sets a timeout using seconds as an integer:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/retries-and-timeouts/timeouts.py" fragment="timeout-seconds" lang="python" >}}

We can also set a timeout using a `timedelta` object for more readable durations:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/retries-and-timeouts/timeouts.py" fragment="timeout-timedelta" lang="python" >}}

You can also set separate timeouts for maximum execution time and maximum queue time using the `Timeout` class:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/retries-and-timeouts/timeouts.py" fragment="timeout-advanced" lang="python" >}}

You can also combine retries and timeouts for resilience and resource control:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/retries-and-timeouts/timeouts.py" fragment="timeout-with-retry" lang="python" >}}

Here we specify:
- Up to 3 retry attempts.
- Each attempt times out after 1 minute.
- Task fails if queued for more than 1 minute.
- Total possible runtime: 1 minute queue + (1 minute × 3 attempts).

We define the `main` driver task that calls all the timeout tasks concurrently and returns their outputs as a list. The return value for failed tasks will indicate failure:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/retries-and-timeouts/timeouts.py" fragment="main" lang="python" >}}

Note that we also demonstrate overriding the timeout for `timeout_seconds` to 120 seconds when calling it.

Finally, we configure Flyte and invoke the `main` task:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/retries-and-timeouts/timeouts.py" fragment="run" lang="python" >}}

Proper retry and timeout configuration ensures your Flyte workflows are both reliable and efficient, handling transient failures gracefully while preventing resource waste.