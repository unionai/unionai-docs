---
title: Queues
weight: 11
variants: +union
---

# Queues

> [!NOTE] Beta
> Queues are a beta feature. The set of queues available to you, and the limits
> each one enforces, are configured by your platform administrator. Talk to your
> platform admin about which queues exist in your environment, what they're
> intended for, and what limits they apply before pinning workloads to them.

A **queue** is a named scheduling lane for your work. Instead of every run and
action competing for whatever capacity happens to be free, a queue gives the
platform a place to apply policy: how many things run at once, how deep the
backlog can get, how this work is prioritized relative to everyone else's, and
which cluster it lands on.

Targeting a queue is a single parameter — you don't change your task code, you
just say *where* it should be scheduled. Anything you don't explicitly route
goes to the **default queue**.

## Routing work to a queue

The `queue` parameter can be set at three levels — on the `flyte.TaskEnvironment`,
on the `@env.task` decorator, and at invocation time via `task.override()`. The
more specific level always wins, exactly like the other task settings.

```python
import flyte

# Default every task in this environment to a queue...
env = flyte.TaskEnvironment(
    name="my_env",
    queue="default-pool",
)

# ...inherit the environment default...
@env.task
def preprocess(data: list) -> list:
    return [x * 2 for x in data]

# ...or override per task.
@env.task(queue="gpu-pool")
def train_model(data: list) -> dict:
    return {"accuracy": 0.95}
```

A common pattern is to leave the entry-point task on the default routing and pin
only the child steps that need capping to a queue, so the run as a whole goes
through the default pool and only the targeted workload is constrained.

### Per-run and per-trigger routing

You can also choose a queue when you launch a run, without touching the task
definition:

```python
flyte.with_runcontext(queue="my-queue").run(main, count=10)
```

And a [trigger](./triggers) can send its scheduled runs to a specific queue —
useful when you want scheduled or automated work to run under different limits
than ad-hoc runs:

```python
import flyte

trigger = flyte.Trigger(
    "nightly",
    flyte.Cron("0 2 * * *"),
    queue="batch",
)
```

### Overriding a queue at runtime

A running workflow can route a specific task invocation to a different queue —
for example to push one heavy step onto a dedicated lane:

```python
@env.task
async def main(queue_name: str):
    # Route this invocation of train_model to a queue chosen at runtime.
    train_model.override(queue=queue_name)(data=[1, 2, 3])
```

## What a queue controls

Queues are configured by your platform admin, but it helps to understand the
knobs so you can pick the right queue for a workload:

- **Action concurrency** — the maximum number of tasks routed to the queue that
  run at the same time. A queue with a cap of 1 serializes its work; a cap of 3
  lets at most three run concurrently and holds the rest until a slot frees up.
- **Run concurrency** — the maximum number of *runs* on the queue that are active
  at once. Children of an active run aren't capped by this; only the runs
  themselves are. Use this for a job that parallelizes well internally but must
  not overlap with a previous invocation of itself.
- **Depth** — the total number of in-flight plus waiting items the queue will
  hold. When a queue is full, new submissions are rejected immediately with a
  `RESOURCE_EXHAUSTED` error rather than queueing forever. That rejection is a
  back-pressure signal to your caller — catch it and slow down, rather than
  retrying in a tight loop.
- **Priority** — when several queues share the same cluster capacity, higher
  priority work is scheduled ahead of lower priority work. Priority controls
  *ordering*, not preemption: a lower-priority task that has already started is
  not interrupted when higher-priority work arrives.

## When to use queues

### Concurrency control for scheduled and automated runs

A run that updates a shared checkpoint or mutates global state must not overlap
with itself. Route it to a queue with **run concurrency of 1**: even if a
schedule fires again before the previous run finishes, the new run waits instead
of running concurrently. Inside each run, children still fan out freely.

```python
@env.task(queue="runs-1")  # run-concurrency 1
async def nightly_job(fan_out: int = 50) -> list[str]:
    # Hundreds of children can run in parallel within this run...
    return list(flyte.map(child, range(fan_out)))
    # ...but two nightly_job runs never overlap.
```

This pairs naturally with [triggers](./triggers) — give the trigger a serialized
queue and you get self-non-overlapping scheduled jobs for free.

### Backfill control

A backfill can produce thousands of actions in a burst and starve everything
else sharing the cluster. Send the backfill to a queue with a bounded **action
concurrency** (and optionally a **depth** limit) so it drains at a controlled
rate while leaving headroom for production traffic. The depth limit turns a flood
into explicit back-pressure: when the queue is full your submitter gets
`RESOURCE_EXHAUSTED` and can pause instead of piling on.

### Multi-cluster routing and prioritizing certain workloads

Because a queue can be bound to a specific cluster (or set of clusters) and given
a priority, queues are how you say "GPU training goes to the GPU cluster" or
"this customer-facing pipeline is high priority." Route latency-sensitive or
business-critical work to a high-priority queue and bulk or best-effort work to a
lower-priority one; when they contend for the same capacity, the important work
is scheduled first.

## Queues and timeouts

How long a task is willing to *wait* in a queue before it gives up is a separate,
per-task concern controlled by the timeout settings. If a queue is busy or
capped, an action sits in the **Queued** phase until a slot opens — set
[`max_queued_time`](./retries-and-timeouts#max_queued_time--fail-fast-when-capacity-isnt-available)
to fail fast when capacity isn't available within your window, and
[`deadline`](./retries-and-timeouts#deadline--bound-the-total-wall-clock) to put
an absolute ceiling on total wall-clock including queue wait. See
[Retries and timeouts](./retries-and-timeouts) for the full picture.
