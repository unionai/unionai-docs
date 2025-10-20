---
title: Fanout
weight: 160
variants: +flyte +serverless +byoc +selfmanaged
---

# Fanout

Flyte is designed to scale effortlessly, allowing you to run workflows with large fan-outs.
When you need to execute many tasks in parallel—such as processing a large dataset or running hyperparameter sweeps—Flyte provides powerful patterns to implement these operations efficiently.

{{< variant byoc selfmanaged serverless >}}
{{< markdown >}}
> [!NOTE]
> By default fanouts in Union are limited to a maximum size.
> Adjustment can made to this maximum by consulting with the Union team.
> Full documentation of this aspect of fanout is coming soon.
{{< /markdown >}}
{{< /variant >}}

## Understanding fanout

A "fanout" pattern occurs when you spawn multiple tasks concurrently.
Each task runs in its own container and contributes an output that you later collect.
The most common way to implement this is using the [`asyncio.gather`](https://docs.python.org/3/library/asyncio-task.html#asyncio.gather) function.

In Flyte terminology, each individual task execution is called an "action"—this represents a specific invocation of a task with particular inputs. When you call a task multiple times in a loop, you create multiple actions.

## Settinng up our example

We start by importing our required packages, defining our Flyte environment, and creating a simple task that fetches user data from a mock API.

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/fanout/fanout.py" fragment="setup" lang="python" >}}

## Parallel execution

Next we implement the most common fanout pattern, which is to collect task invocations and execute them in parallel using `asyncio.gather()`:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/fanout/fanout.py" fragment="parallel" lang="python" >}}

When this pattern is used in a normal Python environment, the tasks would execute concurrently, but not necessrily in parallel.

However, **in Flyte, the orchestrator acts as the event loop**, running each task action in parallel in its own container.

This means that when you use `asyncio.gather()` in a Flyte task, each task invocation is scheduled to run simultaneously across the cluster, allowing for massive scalability.

## Running the example

To actually run our example, we create a main guard that intializes Flyte and runs our main driver task:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/fanout/fanout.py" fragment="run" lang="python" >}}