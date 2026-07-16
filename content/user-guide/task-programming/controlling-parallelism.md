---
title: Controlling parallel execution
weight: 18
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
> Each task still runs in its own container with its own resources: the semaphore simply limits how many containers are active at a time.

## Using flyte.map with concurrency

For uniform work (applying the same task to a list of inputs), `flyte.map` with the `concurrency` parameter is simpler:

{{< code file="/unionai-examples/v2/user-guide/task-programming/controlling-parallelism/controlling_parallelism.py" fragment="map-concurrency" lang="python" >}}

This achieves the same concurrency limit with less boilerplate.

{{< variant union >}}
{{< markdown >}}
For the full `flyte.map` treatment (signature, return order, error handling, partials, and use with
reusable environments), see [Mapping over inputs](./map).
{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}
For the full `flyte.map` treatment (signature, return order, error handling, and partials), see
[Mapping over inputs](./map).
{{< /markdown >}}
{{< /variant >}}

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

## Per-map concurrency vs. the run-level action cap

The `concurrency` parameter (and `asyncio.Semaphore`) throttle how many actions run **at the same
time**. They do **not** change how many actions your run creates in total. These are two separate
limits, and they compose:

- **Per-map `concurrency`** bounds the *in-flight* actions **within one map** — a moving window over
  the fan-out. `flyte.map(process, items, concurrency=10)` keeps at most ten actions running at once,
  but every item still becomes its own action; they are just submitted through a bounded worker pool
  as slots free up.
- **The run-level action cap** bounds the *total* number of actions in the whole run. A run currently
  supports up to **50k actions**, with a recommended target of **10k–20k**. This ceiling counts
  **every** action across the run — summed over all maps and all fan-out — not just the ones in flight
  at any instant. See [Scale your workflows](../run-scaling/scale-your-workflows).

Because these limits are independent, **lowering `concurrency` does not help you stay under the run
cap.** A `flyte.map` over 100,000 items creates 100,000 actions whether `concurrency` is `0` or `10` —
the throttle only slows how fast they are submitted, so such a run still exceeds the 50k ceiling. To
fit under the cap you must reduce the *total* action count by [**batching**](../run-scaling/scale-your-workflows):
have each action process a batch of items, so a large input maps to far fewer actions.

In practice, use the two controls for different jobs:

- **Batch to stay well under the run cap.** Size batches so the total number of mapped actions lands
  in the 10k–20k target range (comfortably below 50k), especially when a single run contains multiple
  maps or other fan-out — they all count against the same ceiling.
- **Set `concurrency` to protect downstream resources.** Independently of total count, cap in-flight
  actions to respect rate-limited APIs, GPU quotas, or connection limits, and to keep memory
  proportional to `concurrency` rather than to the full input size.

For the full run-scaling picture — task overhead, batch sizing, and fan-out control — see
[Scale your workflows](../run-scaling/scale-your-workflows).
