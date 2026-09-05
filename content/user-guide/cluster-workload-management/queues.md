---
title: Managing queues
description: Create and manage the scheduling lanes that route workloads to a pool and enforce concurrency, priority, and fairness.
icon: list-task
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
[Queues in Configure tasks](../tasks/task-configuration/queues).

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

> [!NOTE] Routing skips unhealthy and disabled clusters
> A `*` selector does not mean *every* cluster in the pool — it means every
> cluster that is both **healthy** and **enabled**, evaluated against the pool's
> current state. Pinned selectors are filtered the same way: an unhealthy or
> disabled cluster receives no new work from *any* queue, wildcard or pinned.
> Say a pool holds two clusters and the second goes unhealthy for any reason,
> including a
> [config mismatch with the pool](./cluster-pools#how-a-pools-config-is-enforced):
> the queue routes new runs and actions to the first cluster only, and sends
> nothing to the second until it becomes healthy again. This governs the placement
> of new work; it does not move work that has already been dispatched. Check with
> `flyte get cluster <name>`, which reports each cluster's state, health, and
> unhealthy reasons.

### Queues you get for free

You don't have to create a queue to have one. Two exist without any action on
your part:

- The org-wide **`default`** queue, in the `default` pool with the `*` selector.
  Anything that doesn't explicitly target a queue goes here. (If the `default`
  queue is [drained](#drain-and-reactivate-a-queue) or
  [deleted](#delete-a-queue), untargeted submissions are rejected until it is
  active again — a restored queue comes back `drained`, so after an undelete it
  must also be reactivated.)
- A **co-named queue** for every cluster: registering a cluster creates a queue
  with the *same name as the cluster*, in that cluster's pool, whose selector
  names that one cluster explicitly rather than using `*`. Register
  `prod-us-east-1` and you get a `prod-us-east-1` queue that routes only to
  `prod-us-east-1` — so any cluster can be targeted by name immediately, without
  setting up a queue for it. See
  [The co-named queue](./clusters#the-co-named-queue).

Both are ordinary queues: they show up in `flyte get queue` and take the same
settings and updates as queues you create yourself — with one exception. A
co-named queue's cluster selector and pool are managed by its cluster and cannot
be edited directly: the queue follows its cluster if the cluster is
[reassigned to another pool](./clusters#move-a-cluster-to-a-different-pool). It
also follows the cluster through drain, activate, and delete transitions, and
it cannot be activated on its own while its cluster is `draining` or `drained`
(see
[How the co-named queue follows its cluster](./clusters#how-the-co-named-queue-follows-its-cluster)).
The cluster and queue finish their transitions separately, so they may reach
their final states at slightly different times. Its other settings (concurrency,
depth, priority, fairness) stay editable like any queue's. Listings make the
distinction visible: cluster-managed queues are flagged in the `flyte get queue`
table (`cluster_managed`, exposed as `Queue.cluster_managed` in Python), and
`flyte update queue --edit` says so at the top of the edit buffer.

The selector (which clusters within the pool) is mutable and can be changed at
any time. The pool a queue lives in can only change once the queue is fully
**drained**: a pool move on an `active` or `draining` queue is rejected, because
moving a queue that still holds work would cross an isolation boundary. See
[Move work to another pool](#move-work-to-another-pool).

> [!NOTE] Queues are organization-scoped
> Every queue is visible to the whole organization; a queue cannot yet be scoped
> to a project or a domain. Some CLI and Python surfaces already expose `project`
> and `domain` parameters, but project/domain-scoped queue creation is not
> implemented yet and is rejected. Support is coming soon.

## Create a queue

`run_concurrency` and `action_concurrency` are required; everything else has a
sensible default. With no cluster selector, a queue spreads work across **all**
healthy clusters in its pool. The name `default` is reserved, and a queue cannot
share a name with a cluster — every cluster already owns its
[co-named queue](./clusters#the-co-named-queue).

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
{{< tab "Console" >}}
{{< markdown >}}

In the console, go to **Settings > Queues** and click **New Queue**. Fill in the
**New queue** form and click **Create queue**. The fields map to the same settings
the CLI and Python expose:

![The New queue form in the console](../../_static/images/user-guide/cluster-workload-management/queues/queues-new-form.png)

| Form field | Setting |
|---|---|
| **Name** | the queue name |
| **Priority** | `priority` (shown as Low / Medium / High, see below) |
| **Cluster pool** | `cluster_pool` / `--cluster-pool` |
| **Clusters** | `clusters` / `--cluster` ("All available clusters (default behavior)" routes to every cluster in the pool) |
| **Depth** | `depth` / `--depth` |
| **Run concurrency** | `run_concurrency` / `--run-concurrency` |
| **Action concurrency** | `action_concurrency` / `--action-concurrency` |

The console labels priority **Low**, **Medium**, and **High**; these are the same
levels the CLI and Python call `min`, `medium`, and `max`. **Fairness** is not in
the form, so set it from the CLI or Python if you need a value other than the
default.

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

# List live queues in one state: active, draining, drained, or deleting
flyte get queue --state draining

# Inspect one queue's settings and status
flyte get queue gpu-queue

# Stream live metrics — runs in-flight, actions in-flight, queue depth
flyte get queue gpu-queue --watch

# List soft-deleted queues (hidden from the plain listing)
flyte get queue --deleted
```

`--watch` renders live progress bars for run concurrency, action concurrency, and
depth, so you can see a queue filling up or draining in real time. Metrics are
available while a queue is `active`, `draining`, `drained`, or `deleting`.
Watching a `draining` queue shows work finishing normally; watching a `deleting`
queue shows its cleanup progress. A [deleted](#delete-a-queue) queue cannot be
watched until you restore it.

Fetching a queue **by name** works even after it has been
[deleted](#delete-a-queue): `flyte get queue <name>` returns the soft-deleted
queue carrying its deletion time instead of failing, so a queue that an old run
once targeted stays inspectable. Only the listing hides deleted queues, unless
you pass `--deleted`; `--state deleted` without `--deleted` returns nothing for
the same reason.

{{< /markdown >}}
{{< /tab >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
from flyteplugins.union.remote import Queue

for queue in Queue.listall(limit=100):
    print(queue.name, queue.status, queue.priority, queue.cluster_pool, queue.clusters)

# Narrow the live listing to one lifecycle state: "active", "draining",
# "drained", or "deleting"
for queue in Queue.listall(state="draining"):
    print(queue.name)

# Deleted queues are hidden from the listing unless you ask for them
for queue in Queue.listall(deleted=True):
    print(queue.name)

queue = Queue.get("gpu-queue")
print(queue.to_dict())
```

`Queue.get` works even on a [deleted](#delete-a-queue) queue: it returns the
soft-deleted queue carrying its deletion time instead of failing, while
`Queue.listall` hides deleted queues.

```python
metrics = Queue.details("gpu-queue")
print(metrics)
```

To stream metrics:

```python
for metrics in Queue.watch("gpu-queue"):
    print(metrics)
```

`Queue.details` and `Queue.watch` work on live queues, including `draining`,
`drained`, and `deleting` queues. Unlike `Queue.get`, neither works on a
[deleted](#delete-a-queue) queue.

{{< /markdown >}}
{{< /tab >}}
{{< tab "Console" >}}
{{< markdown >}}

Go to **Settings > Queues** to see all your queues.

![The console Queues list, grouped by cluster pool](../../_static/images/user-guide/cluster-workload-management/queues/queues-list.png)

Queues are grouped by cluster pool (the **View by Pool** toggle), and each row
shows its status, priority, and live **Queued**, **Runs**, and **Actions** counts.
Use the **Status** filter or the search box to narrow the list.

Click a queue to open its detail view, which has three tabs.

**Overview** shows the queue's live state: its cluster pool, the clusters it is
connected to and their CPU, GPU, and memory capacity, and the in-flight **Queued**,
**Runs**, and **Actions** counts.

![The Overview tab of a queue's detail view in the console](../../_static/images/user-guide/cluster-workload-management/queues/queues-detail-overview.png)

**Usage** gives ready-to-copy snippets for routing work to this queue, at run level
and per task, with the queue's name already filled in. These are the same routing
methods described in [Queues in Configure tasks](../tasks/task-configuration/queues).

![The Usage tab of a queue's detail view, showing run-level and task-level routing snippets](../../_static/images/user-guide/cluster-workload-management/queues/queues-detail-usage.png)

**Settings** lists the queue's current configuration: its pool, connected clusters,
and scope, plus its priority, depth, and run and action concurrency limits.

![The Settings tab of a queue's detail view, listing its configuration](../../_static/images/user-guide/cluster-workload-management/queues/queues-detail-settings.png)

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

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

Changing the queue's **pool** (`cluster_pool` in the YAML or Python) is allowed
only when the queue is [drained](#drain-and-reactivate-a-queue), the destination
pool exists, and every cluster in the queue's selector is a member of the
destination pool — see [Move work to another pool](#move-work-to-another-pool).
A cluster's [co-named queue](./clusters#the-co-named-queue) rejects selector and
pool changes entirely: those are managed by its cluster.

## Queue lifecycle

A queue is in one of five lifecycle states. The `drain`, `activate`, `delete`,
and `undelete` transitions are requested by you; the moves into `drained` and
`deleted` are written by the system once the leasor confirms the queue holds
nothing.

```mermaid
stateDiagram-v2
    [*] --> active: create
    active --> draining: drain
    draining --> active: activate
    draining --> drained: no work left (system)
    drained --> active: activate
    draining --> deleting: delete
    drained --> deleted: delete
    active --> deleting: cluster deleted (co-named queue only)
    deleting --> deleted: cleanup done (system)
    deleted --> drained: undelete
```

- **`active`**: accepting new submissions.
- **`draining`**: no new submissions; in-flight work runs to completion. The
  system moves the queue to `drained` once the leasor reports it holds no run
  or cleanup work.
- **`drained`**: confirmed empty. The only state from which a delete completes
  in one step, the only state in which the queue can change pools, and the
  state a restored queue comes back in.
- **`deleting`**: deletion requested while the queue may still hold work. The
  leasor terminates the queue's remaining run leases, waits for cleanup work,
  and then reports the queue `deleted`. The queue stays listed meanwhile.
- **`deleted`**: soft-deleted. Hidden from listings and never scheduled on; the
  name stays reserved and `flyte get queue <name>` still returns it.

What each operation does from each state:

| Current state | `--drain` | `--activate` | `flyte delete queue` | `flyte undelete queue` | Pool change |
|---|---|---|---|---|---|
| `active` | → `draining` | no change | rejected (drain first) | rejected | rejected |
| `draining` | no change | → `active` | → `deleting` | rejected | rejected |
| `drained` | rejected (already drained) | → `active` | → `deleted` | rejected | allowed |
| `deleting` | rejected | rejected | rejected | rejected | rejected |
| `deleted` | rejected | rejected | rejected | → `drained` | rejected |

A cluster's co-named queue is the one exception in the `--activate` column:
while its cluster is `draining` or `drained`, the queue cannot be activated on
its own. Activating the cluster activates it.

Three rules follow from the table:

- **Deleting a queue is a safe archive operation.** A queue must always be
  drained before it can be deleted: there is no path from `active` into
  deletion that you can request on a queue, so deleting a queue that is
  accepting work always takes two calls, a drain and then a delete. A single
  misdirected command can never take a serving queue away, and the delete
  itself only archives the record. The one indirect path is
  [deleting a cluster](./clusters#delete-a-cluster), which takes the cluster's
  co-named queue into deletion whatever state it is in; that path is only as
  safe as the cluster delete that triggers it.
- Deletion cannot be canceled: a `deleting` queue can only become `deleted`,
  and only then can it be undeleted.
- `drained` and `deleted` are never requested directly; the leasor writes them
  once it has confirmed the queue holds nothing.

Draining a cluster drains its co-named queue and activating the cluster
activates it; see
[How the co-named queue follows its cluster](./clusters#how-the-co-named-queue-follows-its-cluster).

## Drain and reactivate a queue

**Draining** takes a queue out of rotation without losing in-flight work: the
queue stops admitting new submissions, work already in flight runs to
completion, and once nothing is left the queue settles into the `drained` state.
Use it before maintenance, deletion, or as part of
[moving work to another pool](#move-work-to-another-pool).

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

To see where things stand across the organization, filter listings by state:
`flyte get queue --state draining` shows the queues still finishing in-flight
work, `--state drained` the ones that are done, and `--state deleting` the ones
being removed.

An active queue must start draining before it can be [deleted](#delete-a-queue),
but you do not have to wait for `drained`: deleting a `draining` queue begins its
cleanup immediately. A [pool move](#move-work-to-another-pool) does require the
queue to be fully `drained`. Deleting a cluster automatically takes its co-named
queue into deletion, whatever state that queue is in.

Any queue can be drained, including the `default` queue and a queue configured
as the default run queue (`run.default_queue`) in your organization's settings
at any scope — draining is how you stop scheduling on it, and the prerequisite
for [deleting it](#delete-a-queue). A draining or drained queue still resolves
as the default: runs that land on it are rejected with an error saying the
queue is not accepting work. Only [deleting](#delete-a-queue) a queue
referenced in settings is refused.

## Delete a queue

A queue must always be drained before it is deleted: an `active` queue is
rejected, so start draining it first. This is what makes deleting a queue a
safe archive operation, in contrast to
[deleting a cluster](./clusters#delete-a-cluster), which can interrupt work.
Once the queue is draining you can choose whether to wait:

- Deleting a `draining` queue moves it to `deleting`. The leasor terminates the
  queue's remaining run leases, so queued and running actions on it are
  aborted rather than finished; cleanup work already in progress is allowed to
  complete. The queue becomes `deleted` when the leasor holds nothing more for
  it.
- Deleting a `drained` queue moves it directly to `deleted`, because the leasor
  has already confirmed that no work or cleanup remains.

Deletion cannot be canceled. A `deleting` queue rejects every further request:
it cannot be drained, activated, deleted again, or undeleted. Wait until it
becomes `deleted` before undeleting it.

A queue referenced as the default run queue (`run.default_queue`) in settings at
any scope can be drained but not deleted: update or unset those settings first.
A cluster's [co-named queue](./clusters#the-co-named-queue) can be deleted on its
own while the cluster lives. Deleting the cluster also deletes its co-named queue
and is the only operation that can take that queue directly from `active` to
`deleting`.

The `default` queue is no exception: drain it, then delete it, like any other
queue — deleting it is also how the `default` pool is emptied of live queues so
that [the pool itself can be deleted](./cluster-pools#delete-a-pool). While the
`default` queue is deleted, submissions that name no queue and have no
`run.default_queue` setting to fall back on are rejected at creation. Nothing
re-creates it implicitly; `flyte undelete queue default` brings it back.

{{< tabs "delete-queue" >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte delete queue gpu-queue
flyte delete queue gpu-queue --yes   # skip the confirmation prompt

# List deleted queues, restore one
flyte get queue --deleted
flyte undelete queue gpu-queue
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
from flyteplugins.union.remote import Queue

queue = Queue.delete("gpu-queue")
print(queue.status)           # deleting or deleted
Queue.undelete("gpu-queue")   # restore a deleted queue
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

A `deleting` queue remains visible in normal listings while cleanup runs, and it
can still be inspected or watched. Once `deleted`, it is soft-deleted: it
disappears from normal listings and is no longer scheduled on, but its name stays
reserved. Fetching it by name still works — `flyte get queue <name>` and
`Queue.get` return the queue with its deletion time. Use
`flyte get queue --deleted` to list deleted queues.

Restore it with `flyte undelete queue <name>`. The queue's pool and pinned
clusters must still be live. A cluster's co-named queue undeletes like any other
queue while its cluster is live; while the cluster is deleted, the undelete is
refused and [undeleting the cluster](./clusters#delete-a-cluster) brings the
queue back with it. The restored queue comes back `drained`; reactivate it to
resume routing.

## Move work to another pool

Moving work to a different **pool** crosses an isolation boundary. In-flight runs
have already landed their data, containers, code, and secrets in the old pool's
data plane, and a different pool's clusters cannot read them. So work in flight
never moves: the migration is always drain-first, in one of two shapes.

**Move the queue itself.** A queue can change pools once it holds no work:

1. [Drain](#drain-and-reactivate-a-queue) the queue and wait for it to reach the
   `drained` state.
2. Update the queue's pool — `flyte update queue <name> --edit` and change
   `cluster_pool` in the YAML, or `Queue.update(name, cluster_pool=...)` — and
   set its cluster selector to clusters that are members of the destination pool
   (or `*`).
3. [Reactivate](#drain-and-reactivate-a-queue) the queue.

Anything targeting the queue by name follows it to the new pool. New submissions
made while it is drained are rejected, so coordinate the window with the queue's
users.

**Replace the queue.** Alternatively, keep the old queue's pool binding and
shift traffic over:

1. Create a new queue in the destination pool.
2. Update workflows, launch plans, triggers, or run overrides to target the new
   queue.
3. [Drain](#drain-and-reactivate-a-queue) the old queue to shut out straggler
   submissions and let in-flight work finish.
4. [Delete](#delete-a-queue) the drained queue, or leave it idle — an idle queue
   costs nothing.

> [!NOTE] Queue overrides stay within a pool
> A task can override its queue at runtime
> ([`task.override(queue=...)`](../tasks/task-configuration/queues#overriding-a-queue-at-runtime)),
> but only to another queue in the **same pool** as the run's original queue. A
> cross-pool override is rejected, for the same data plane reason that moving
> work between pools requires a drain-and-replace migration.

## See also

- [Queues in Configure tasks](../tasks/task-configuration/queues): routing work to a
  queue from task code, triggers, and per-run context.
- [Cluster pools](./cluster-pools) and [Clusters](./clusters): the routing
  targets a queue points at.
