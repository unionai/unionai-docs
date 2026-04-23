---
title: Controlling parallel execution
weight: 14
variants: +flyte +union
---

# Controlling parallel execution

When you [fan out](./fanout) to many tasks, you often need to limit how many run at the same time.
Common reasons include rate-limited APIs, GPU quotas, database connection limits, or simply avoiding overwhelming a downstream service.

Flyte 2 provides two ways to control concurrency:
[`asyncio.Semaphore`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Semaphore) for fine-grained control,
and `flyte.map` with a built-in `concurrency` parameter for simpler cases.

## The problem: unbounded parallelism

A straightforward `asyncio.gather` launches every task at once.
If you are calling an external API that allows only a few concurrent requests, this can cause throttling or errors:

{{< code file="/unionai-examples/v2/user-guide/task-programming/controlling-parallelism/controlling_parallelism.py" fragment="setup" lang="python" >}}

{{< code file="/unionai-examples/v2/user-guide/task-programming/controlling-parallelism/controlling_parallelism.py" fragment="unbounded" lang="python" >}}

With eight prompts, this fires eight concurrent API calls.
That works fine when there are no limits, but will fail when the API enforces a concurrency cap.

## Using asyncio.Semaphore

An `asyncio.Semaphore` acts as a gate: only a fixed number of tasks can pass through at a time.
The rest wait until a slot opens up.

{{< code file="/unionai-examples/v2/user-guide/task-programming/controlling-parallelism/controlling_parallelism.py" fragment="semaphore" lang="python" >}}

The pattern is:

1. Create a semaphore with the desired limit.
2. Wrap each task call in an inner async function that acquires the semaphore before calling and releases it after.
3. Pass all wrapped calls to `asyncio.gather`.

All eight tasks are submitted immediately, but the Flyte orchestrator only allows three to run in parallel.
As each one completes, the next waiting task starts.

> [!NOTE]
> The semaphore controls how many tasks execute concurrently on the Flyte cluster.
> Each task still runs in its own container with its own resources — the semaphore simply limits how many containers are active at a time.

## Using flyte.map with concurrency

For uniform work — applying the same task to a list of inputs — `flyte.map` with the `concurrency` parameter is simpler:

{{< code file="/unionai-examples/v2/user-guide/task-programming/controlling-parallelism/controlling_parallelism.py" fragment="map-concurrency" lang="python" >}}

This achieves the same concurrency limit with less boilerplate.

## Running the example

{{< code file="/unionai-examples/v2/user-guide/task-programming/controlling-parallelism/controlling_parallelism.py" fragment="run" lang="python" >}}

## When to use each approach

Use **`flyte.map(concurrency=N)`** when:

- Every item goes through the same task.
- You want the simplest possible code.

Use **`asyncio.Semaphore`** when:

- You need different concurrency limits for different task types within the same workflow.
- You want to combine concurrency control with error handling (e.g., `asyncio.gather(*tasks, return_exceptions=True)`).
- You are calling multiple different tasks in one parallel batch.
