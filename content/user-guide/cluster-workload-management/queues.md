---
title: Queues
weight: 3
variants: -flyte +union
mermaid: true
---

# Queues

> [!NOTE] Requires the `flyteplugins-union` plugin
> The `flyte` queue commands on this page are provided by the
> `flyteplugins-union` package. Install it with `pip install flyteplugins-union`.

A **queue** is a named scheduling lane. It does two jobs at once: it **routes**
work to a [cluster pool](./cluster-pools) (and, optionally, specific clusters
within it), and it **governs** that work with concurrency, depth, priority, and
fairness limits.

This page covers creating and managing queues from the CLI — the administrative
side. For how workflow authors *target* a queue from task code, see
[Queues in Configure tasks](../task-configuration/queues).

## How a queue routes

A queue lives inside one **cluster pool** and routes work to one or more clusters
*within that pool*. By default (the `*` selector) it spreads across every healthy
cluster in the pool; you can also pin it to specific clusters. It can never reach a
cluster in another pool — pools are isolation boundaries.

```mermaid
flowchart TD
    R(["Runs &amp; actions"])

    subgraph Pdef["Cluster pool: default"]
        direction TB
        QD["Queue: default<br/>selector: *"]
        CA["Cluster A"]
        CB["Cluster B"]
        QD --> CA
        QD --> CB
    end

    subgraph Pprod["Cluster pool: prod"]
        direction TB
        QP["Queue: prod-queue<br/>selector: *"]
        QG["Queue: gpu-queue<br/>pinned: Cluster C"]
        CC["Cluster C"]
        CD["Cluster D"]
        QP --> CC
        QP --> CD
        QG --> CC
    end

    R --> QD
    R --> QP
    R --> QG
```

Users submit to a **queue**, never to a pool or a cluster directly. Each queue sits
inside exactly one pool:

- **`default`** spreads across all clusters in the `default` pool.
- **`prod-queue`** spreads across all clusters in the `prod` pool.
- **`gpu-queue`** lives in the same `prod` pool but is pinned to a single cluster.

The selector (which clusters within the pool) is freely mutable; the pool a queue
lives in is not — moving a queue to another pool means crossing an isolation
boundary, so it [requires a drain](#change-a-queues-pool--drain-first).

## Create a queue

```bash
flyte create queue my-queue \
  --run-concurrency 100 \
  --action-concurrency 1000
```

`--run-concurrency` and `--action-concurrency` are required; everything else has a
sensible default. With no `--cluster` a queue spreads work across **all** healthy
clusters in its pool.

> [!NOTE] Queues are bound to a cluster pool
> Every queue is bound to a cluster pool, chosen at creation time with
> `--cluster-pool`. In the absence of `--cluster-pool`, the queue is bound to the
> `default` cluster pool.

Pin a queue to specific clusters within its pool, scope it to a project/domain, and
tune its limits:

```bash
flyte create queue gpu-queue \
  --cluster-pool prod \
  --cluster prod-us-east-1 \
  --run-concurrency 50 \
  --action-concurrency 500 \
  --depth 5000 \
  --priority max \
  --fairness round_robin \
  --project myproj \
  --domain production
```

### What each setting controls

- **`--cluster-pool`** — the pool this queue lives in. A queue can only route to
  clusters in its own pool. Omit to bind the queue to the `default` pool. The pool
  is fixed at creation time; moving a queue to another pool later
  [requires a drain](#change-a-queues-pool--drain-first).
- **`--cluster`** — pin the queue to one or more clusters in the pool (repeat the
  flag for several). Omit to use all clusters in the pool.
- **`--run-concurrency`** — maximum number of *runs* active on the queue at once.
  Children of an active run aren't counted; use this to stop a job from overlapping
  with a previous invocation of itself.
- **`--action-concurrency`** — maximum number of *actions* (tasks) running at once.
  A cap of 1 serializes the queue; higher values bound the burst rate.
- **`--depth`** — total in-flight plus waiting items the queue will hold (default
  `10000`). When full, new submissions are rejected with `RESOURCE_EXHAUSTED` —
  back-pressure, not an unbounded backlog.
- **`--priority`** — `min`, `medium` (default), or `max`. Among queues contending
  for the same pool's capacity, higher-priority work is scheduled first. Priority
  controls ordering, not preemption.
- **`--fairness`** — `round_robin` (default) or `shuffle_interleave`. How actions
  from different projects sharing the queue are interleaved.
- **`--project` / `--domain`** — scope the queue so only that project/domain can
  route to it. Pools are org-level; queue *scope* is independent of the pool it
  targets.

## Inspect queues

```bash
# List all queues
flyte get queue

# Inspect one queue's settings and status
flyte get queue gpu-queue

# Stream live metrics — runs in-flight, actions in-flight, queue depth
flyte get queue gpu-queue --watch
```

`--watch` renders live progress bars for run concurrency, action concurrency, and
depth, so you can see a queue filling up or draining in real time.

## Change a queue's settings

Edit a queue's limits, priority, fairness, or cluster pinning interactively:

```bash
flyte update queue gpu-queue --edit
```

Changing the **cluster selector within the same pool** (which clusters the queue
pins to) takes effect immediately — no drain required, because every cluster in the
pool shares the same data plane.

## Change a queue's pool — drain first

Moving a queue to a different **pool** is different — it crosses an isolation
boundary. In-flight runs have already landed their data, containers, code, and
secrets in the old pool's data plane, and a different pool's clusters cannot read
them. So you must drain the queue first:

```bash
# 1. Stop accepting new submissions; let in-flight work finish
flyte update queue gpu-queue --drain

# 2. Once drained, repoint the queue to the new pool
flyte update queue gpu-queue --edit   # set cluster_pool to the new pool

# 3. Start accepting work again
flyte update queue gpu-queue --activate
```

> [!NOTE] Queue overrides stay within a pool
> A task can override its queue at runtime
> ([`task.override(queue=...)`](../task-configuration/queues#overriding-a-queue-at-runtime)),
> but only to another queue in the **same pool** as the run's original queue. A
> cross-pool override is rejected, for the same data-plane reason that pool changes
> require a drain.

## Draining and reactivating

Draining is also how you take a queue out of rotation without losing in-flight work
— for maintenance, or before deleting the clusters behind it:

```bash
flyte update queue gpu-queue --drain      # stop new submissions, let current work finish
flyte update queue gpu-queue --activate   # accept work again
```

## See also

- [Queues in Configure tasks](../task-configuration/queues) — routing work to a
  queue from task code, triggers, and per-run context.
- [Cluster pools](./cluster-pools) and [Clusters](./clusters) — the routing
  targets a queue points at.
