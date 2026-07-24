---
title: Managing queues
weight: 3
variants: -flyte +union
mermaid: true
---

# Managing queues

> [!NOTE] Requires the `flyteplugins-union` plugin
> The queue CLI commands and Python objects on this page are provided by the
> `flyteplugins-union` package. Install it with `pip install flyteplugins-union`.

A **queue** is a named scheduling lane. It does two jobs at once: it **routes**
work to a [cluster pool](./cluster-pools) (and, optionally, specific clusters
within it), and it **governs** that work with concurrency, depth, priority, and
fairness limits.

This page covers creating and managing queues administratively, from either the
CLI or Python. For how workflow authors *target* a queue from task code, see
[Queues in Configure tasks](../task-configuration/queues).

## How a queue routes

A queue lives inside one **cluster pool** and routes work to one or more clusters
*within that pool*. By default (the `*` selector) it spreads across the pool's
healthy, enabled clusters; you can also pin it to specific clusters. It can never
reach a cluster in another pool: pools are isolation boundaries.

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

- **`default`** spreads across the eligible clusters in the `default` pool.
- **`prod-queue`** spreads across the eligible clusters in the `prod` pool.
- **`gpu-queue`** lives in the same `prod` pool but is pinned to a single cluster.

> [!NOTE] Wildcard routing skips unhealthy and disabled clusters
> A `*` selector does not mean *every* cluster in the pool — it means every
> cluster that is both **healthy** and **enabled**, evaluated against the pool's
> current state. Say a pool holds two clusters and the second goes unhealthy for
> any reason, including a
> [config mismatch with the pool](./cluster-pools#how-a-pools-config-is-established):
> the queue routes new runs and actions to the first cluster only, and sends
> nothing to the second until it becomes healthy again. This governs the placement
> of new work; it does not move work that has already been dispatched. Check with
> `flyte get cluster <name>`, which reports each cluster's state, health, and
> unhealthy reasons.

### Queues you get for free

You don't have to create a queue to have one. Two exist without any action on
your part:

- The org-wide **`default`** queue, in the `default` pool with the `*` selector.
  Anything that doesn't explicitly target a queue goes here.
- A **co-named queue** for every cluster: registering a cluster creates a queue
  with the *same name as the cluster*, in that cluster's pool, whose selector
  names that one cluster explicitly rather than using `*`. Register
  `prod-us-east-1` and you get a `prod-us-east-1` queue that routes only to
  `prod-us-east-1` — so any cluster can be targeted by name immediately, without
  setting up a queue for it. See
  [The co-named queue](./clusters#the-co-named-queue).

Both are ordinary queues: they show up in `flyte get queue` and take the same
settings and updates as queues you create yourself.

The selector (which clusters within the pool) is mutable. The pool a queue lives
in is **fixed at creation**: an update that changes it is rejected, because
moving a queue to another pool would cross an isolation boundary. To move
workloads to another pool, see [Move work to another pool](#move-work-to-another-pool).

There is one exception, and it isn't a queue update: a cluster's co-named queue
follows that cluster if the cluster is
[reassigned to another pool](./clusters#move-a-cluster-to-a-different-pool). Any
other queue pinned to that cluster must be repointed first, or the reassignment
is rejected.

> [!NOTE] Queues are organization-scoped
> Every queue is visible to the whole organization; a queue cannot yet be scoped
> to a project or a domain. Some CLI and Python surfaces already expose `project`
> and `domain` parameters, but project/domain-scoped queue creation is not
> implemented yet and is rejected. Support is coming soon.

## Create a queue

`run_concurrency` and `action_concurrency` are required; everything else has a
sensible default. With no cluster selector, a queue spreads work across **all**
healthy clusters in its pool.

{{< tabs "create-queue" >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte create queue my-queue \
  --run-concurrency 100 \
  --action-concurrency 1000
```

Create a higher-priority queue in a specific pool:

```bash
flyte create queue gpu-queue \
  --cluster-pool prod \
  --cluster prod-us-east-1 \
  --run-concurrency 50 \
  --action-concurrency 500 \
  --depth 5000 \
  --priority max \
  --fairness round_robin
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
from flyteplugins.union.remote import Queue

queue = Queue.create(
    "my-queue",
    run_concurrency=100,
    action_concurrency=1000,
)

print(queue.to_dict())
```

Create a higher-priority queue in a specific pool:

```python
queue = Queue.create(
    "gpu-queue",
    cluster_pool="prod",
    clusters=["prod-us-east-1"],
    run_concurrency=50,
    action_concurrency=500,
    depth=5000,
    priority="max",
    fairness="round_robin",
)
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

> [!NOTE] Queues are bound to a cluster pool
> Every queue is bound to a cluster pool, chosen at creation time with
> `cluster_pool` in Python or `--cluster-pool` in the CLI. If you omit it, the
> queue is bound to the `default` cluster pool.

### What each setting controls

- **`cluster_pool` / `--cluster-pool`**: the pool this queue lives in. A queue can
  only route to clusters in its own pool. Omit to bind the queue to the `default`
  pool.
- **`clusters` / `--cluster`**: pin the queue to one or more clusters in the pool.
  Omit to use all clusters in the pool. In the API, `["*"]` means all enabled and
  healthy clusters in the pool (see
  [Wildcard routing](#how-a-queue-routes)), and `*` must be the only entry if
  used.
- **`run_concurrency` / `--run-concurrency`**: maximum number of *runs* active on
  the queue at once. Children of an active run aren't counted; use this to stop a
  job from overlapping with a previous invocation of itself. `0` means no limit.
- **`action_concurrency` / `--action-concurrency`**: maximum number of *actions*
  (tasks) running at once. A cap of 1 serializes the queue; higher values bound
  the burst rate. `0` means no limit.
- **`depth` / `--depth`**: total in-flight plus waiting items the queue will hold
  (default `10000`). `0` means no limit.
- **`priority` / `--priority`**: `min`, `medium` (default), or `max`. Among queues
  contending for the same pool's capacity, higher-priority work is scheduled
  first. Under the hood these map to enum values 1, 50, and 100; use `max` for a
  priority higher than 50. Priority controls ordering, not preemption.
- **`fairness` / `--fairness`**: `round_robin` (default) or `shuffle_interleave`.
  This controls how actions from different projects sharing the queue are
  interleaved.

## Inspect queues

{{< tabs "inspect-queue" >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
# List all queues
flyte get queue

# Inspect one queue's settings and status
flyte get queue gpu-queue

# Stream live metrics — runs in-flight, actions in-flight, queue depth
flyte get queue gpu-queue --watch
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
from flyteplugins.union.remote import Queue

for queue in Queue.listall(limit=100):
    print(queue.name, queue.status, queue.priority, queue.cluster_pool, queue.clusters)

queue = Queue.get("gpu-queue")
print(queue.to_dict())

metrics = Queue.details("gpu-queue")
print(metrics)
```

To stream metrics:

```python
for metrics in Queue.watch("gpu-queue"):
    print(metrics)
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

`--watch` renders live progress bars for run concurrency, action concurrency, and
depth, so you can see a queue filling up or draining in real time.

## Change a queue's settings

You can update limits, priority, fairness, or cluster pinning. The update API
replaces the full queue spec; the Python wrapper handles this by reading the
current queue first, changing only the fields you pass, and writing the complete
spec back.

{{< tabs "update-queue" >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte update queue gpu-queue --edit
```

This opens the queue in your `$EDITOR` so you can adjust the mutable settings.
{{< /markdown >}}
{{< /tab >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
from flyteplugins.union.remote import Queue

Queue.update(
    "gpu-queue",
    run_concurrency=75,
    action_concurrency=750,
    priority="max",
    clusters=["prod-us-east-1"],
)
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

Changing the **cluster selector within the same pool** (which clusters the queue
pins to) takes effect immediately because every cluster in the pool shares the
same data plane.

## Drain and reactivate a queue

**Draining** takes a queue out of rotation without losing in-flight work: the
queue stops admitting new submissions, work already in flight runs to
completion, and once nothing is left the queue settles into the `drained` state.
Draining is how you quiesce a queue: before deleting the cluster behind it,
before maintenance, or as part of
[moving work to another pool](#move-work-to-another-pool).

A queue is in one of three states:

```
active --[drain]--> draining --[in-flight work completes]--> drained
  ^                    |                                        |
  +----[activate]------+----------------[activate]-------------+
```

> [!WARNING] Draining is not yet available
> The drain operation is currently disabled: the control plane rejects drain
> requests. Support is coming in a future release.

{{< tabs "drain-queue" >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte update queue gpu-queue --drain      # stop new submissions; let in-flight work finish
flyte update queue gpu-queue --activate   # put the queue back in rotation
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
from flyteplugins.union.remote import Queue

Queue.drain("gpu-queue")     # stop new submissions; let in-flight work finish
Queue.activate("gpu-queue")  # put the queue back in rotation
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

The `default` queue is always active; its state cannot be changed. Note also
that queues cannot be deleted: draining is how a queue is retired, and an idle
queue costs nothing.

## Move work to another pool

Moving work to a different **pool** crosses an isolation boundary. In-flight runs
have already landed their data, containers, code, and secrets in the old pool's
data plane, and a different pool's clusters cannot read them. So a queue can
never change pools in place; moving work is a drain-and-replace migration:

1. Create a new queue in the destination pool.
2. Update workflows, launch plans, triggers, or run overrides to target the new
   queue.
3. Let in-flight work finish on the old queue. Once
   [draining](#drain-and-reactivate-a-queue) is available, drain it to also
   shut out any straggler submissions.
4. Leave the old queue idle. Queues cannot be deleted; an idle queue costs
   nothing.

> [!NOTE] Queue overrides stay within a pool
> A task can override its queue at runtime
> ([`task.override(queue=...)`](../task-configuration/queues#overriding-a-queue-at-runtime)),
> but only to another queue in the **same pool** as the run's original queue. A
> cross-pool override is rejected, for the same data plane reason that moving
> work between pools requires a drain-and-replace migration.

## See also

- [Queues in Configure tasks](../task-configuration/queues): routing work to a
  queue from task code, triggers, and per-run context.
- [Cluster pools](./cluster-pools) and [Clusters](./clusters): the routing
  targets a queue points at.
