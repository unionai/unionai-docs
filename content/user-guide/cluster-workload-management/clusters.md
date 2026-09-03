---
title: Clusters
description: Register execution clusters into a pool and inspect their state, capacity, and bound queues.
icon: cloud
weight: 2
variants: -flyte +union
mermaid: true
---

# Clusters

> [!NOTE] Requires the `flyteplugins-union` plugin
> The cluster CLI commands and Python objects on this page are provided by the
> `flyteplugins-union` package. Install it with `pip install flyteplugins-union`.

A **cluster** is an execution cluster registered with {{< key product_name >}}.
Every cluster subscribes to exactly one [cluster pool](./cluster-pools), which
determines the data plane configuration (object store, secret store, container
registry) the cluster uses.

Creating a cluster record registers the cluster in the control plane. It does not
install Kubernetes resources or deploy the data plane itself. For self-managed
deployments, first provision and install the data plane using the appropriate
[Self-managed deployment](../../deployment/selfmanaged/_index) guide, then use
the commands or Python calls here to manage the control-plane record.

## Register a cluster

If you omit the pool, the cluster is registered into the `default` pool. To use a
custom pool, create that pool first. One edge case: if the `default` pool has
been [deleted](./cluster-pools#delete-a-pool), registering without a pool is
rejected rather than falling back to it — name a pool explicitly, or undelete
`default`.

{{< tabs "register-cluster" >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
# Register in the default pool.
flyte create cluster my-cluster

# Register in a specific pool.
flyte create cluster prod-us-east-1 --pool prod
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
from flyteplugins.union.remote import Cluster

# Register in the default pool.
Cluster.create("my-cluster")

# Register in a specific pool.
Cluster.create("prod-us-east-1", cluster_pool_name="prod")
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

Registration itself does not validate the cluster against the pool: any cluster
is allowed to join. Validation happens asynchronously, once the cluster starts
reporting its real object store, secret store, and container registry to the
control plane. The control plane compares each reported value against the pool's
config and marks the cluster **unhealthy** on a mismatch. An unhealthy cluster
stops receiving new work from every queue that
[routes](./queues#how-a-queue-routes) to it, until it recovers. See
[How a pool's config is enforced](./cluster-pools#how-a-pools-config-is-enforced)
for the full mechanism.

This is what guarantees that any workload routed to the pool can run on any of
its healthy clusters — so after registering into a custom pool, confirm with
`flyte get cluster <name>` that the cluster settles healthy.

The name `default` is reserved and cannot be used for a cluster (it collides
with the org-wide `default` queue), and a cluster cannot share a name with an
existing queue — registration creates a queue named after the cluster, described
next.

### The co-named queue

Registering a cluster also creates an implicit **co-named queue**: a queue with
the same name as the cluster, in the cluster's pool, whose selector names that
one cluster explicitly — not the `*` wildcard. So `flyte create cluster
prod-us-east-1` also gives you a `prod-us-east-1` queue that routes only to
`prod-us-east-1`, and every cluster can be targeted by name from day one, with no
queue setup:

```python
flyte.with_runcontext(queue="prod-us-east-1").run(main)
```

Registration additionally ensures the org-wide `default` queue exists — unless
that queue has been deliberately [deleted](./queues#delete-a-queue): nothing
re-creates a soft-deleted `default` queue (or pool) implicitly; `flyte undelete`
is the only way back. The `default` queue lives in the `default` pool with the
`*` selector, so it routes to every healthy, enabled cluster in the `default`
pool: a cluster registered there joins it automatically, while a cluster in any
other pool never does.

Both are ordinary queues — they appear in `flyte get queue` (a co-named queue is
flagged there as **cluster-managed**), carry the same
concurrency, depth, priority, and fairness settings as any other, and are managed
the same way on the [Managing queues](./queues) page. What sets the co-named
queue apart is that its cluster selector and pool are managed by its cluster and
cannot be edited directly: it follows its cluster if the cluster is
[reassigned to another pool](#move-a-cluster-to-a-different-pool). It also
follows the cluster through drain, activate, and delete transitions unless it
was already deleted on its own. The system confirms the cluster and queue
transitions separately, so they may finish at slightly different times.

## Inspect clusters

{{< tabs "inspect-cluster" >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
# List all clusters (grouped by enabled / disabled)
flyte get cluster

# Inspect one cluster — cloud config, state, capacity, and bound queues
flyte get cluster prod-us-east-1

# Cap the number of results
flyte get cluster --limit 50
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
from flyteplugins.union.remote import Cluster

for cluster in Cluster.listall(limit=100):
    print(cluster.name, cluster.pool, cluster.drain_state, cluster.health, cluster.capacity)

cluster = Cluster.get("prod-us-east-1")
print(cluster.name)
print(cluster.pool)
print(cluster.drain_state)
print(cluster.queues)
print(cluster.health, cluster.unhealthy_reasons)
print(cluster.capacity)
print(cluster.config_drift)
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

The detailed view shows the cluster's pool, lifecycle state, drain progress,
available capacity, and bound queues.

## Drain and reactivate a cluster

Draining is the graceful way to take a cluster out of service. It stops new work
from reaching the cluster while work already there finishes. The cluster becomes
`drained` after the system confirms that no run or cleanup work remains. You can
reactivate it while it is `draining` or after it becomes `drained`.

Draining a cluster also drains its [co-named queue](#the-co-named-queue), and
reactivating the cluster reactivates that queue when it is draining or drained.
The cluster and queue finish draining separately, so one can briefly be
`drained` before the other. Any other live queue that explicitly names the
cluster blocks the drain; remove the cluster from that queue first. Wildcard
(`*`) queues do not block it.

```mermaid
stateDiagram-v2
    [*] --> Active
    Active --> Draining: drain
    Draining --> Active: activate
    Draining --> Drained: work completes
    Drained --> Active: activate
    Active --> Deleting: delete
    Draining --> Deleting: delete
    Drained --> Deleted: delete
    Deleting --> Deleted: cleanup completes
    Deleted --> Drained: undelete
```

{{< tabs "drain-cluster" >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte update cluster prod-us-east-1 --drain
flyte get cluster prod-us-east-1              # wait for drain: drained
flyte update cluster prod-us-east-1 --activate
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
from flyteplugins.union.remote import Cluster

cluster = Cluster.drain("prod-us-east-1")
print(cluster.drain_state)

Cluster.activate("prod-us-east-1")
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

A `deleting` or `deleted` cluster cannot be drained or activated. To remove a
cluster without waiting for its work to finish, [delete it](#delete-a-cluster).

## Move a cluster to a different pool

A cluster can be reassigned to another pool in place, without deleting and
re-registering it, but the cluster must be `drained` first. It remains drained
after the move so that you can verify its new pool configuration before
reactivating it.

> [!WARNING] A pool move changes the cluster's data plane
> The destination pool can use a different object store, secret store, and
> container registry. Make the required data, images, and secrets available in
> that data plane before moving the cluster.

{{< tabs "move-cluster" >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte update cluster prod-us-east-1 --pool prod
flyte update cluster prod-us-east-1 --pool prod --yes   # skip the confirmation prompt
```

Without `--yes`, the CLI warns that the operation is unsafe and asks you to
confirm.

{{< /markdown >}}
{{< /tab >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
from flyteplugins.union.remote import Cluster

Cluster.update("prod-us-east-1", cluster_pool_name="prod")
```

There is no confirmation prompt on this path.

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

The destination pool must already exist — the move never creates one — and must
differ from the cluster's current pool.

### Before you move a cluster

1. **Repoint other queues.** Any queue other than the
   [co-named queue](#the-co-named-queue) that explicitly names the cluster must
   have it removed from its selector. Such a queue blocks both the cluster drain
   and the pool move. Wildcard (`*`) queues do not block either operation.
   `flyte get cluster <name>` lists the queues bound to the cluster.
2. **Check for apps and v1 executions.** A cluster does not only serve runs: it
   can also be hosting [apps](../apps/serve-and-deploy-apps/_index) and legacy v1
   executions, which {{< key product_name >}} still supports today. There is
   currently **no way to see how many apps or v1 executions are running on a
   given cluster**. Confirm out-of-band that they have stopped before continuing.
3. **Drain the cluster.** Run `flyte update cluster <name> --drain`. This also
   drains its co-named queue. Wait until `flyte get cluster <name>` reports the
   cluster as `drained` and `flyte get queue <name>` reports the queue as
   `drained`. The move is rejected until draining finishes.
4. **Make sure the configs match.** The destination pool's config must match
   what the cluster reports, or the cluster goes unhealthy shortly after the
   move — see below.

After the move, confirm the cluster is healthy, then run
`flyte update cluster <name> --activate`. Its co-named queue is activated with it.

### If the cluster goes unhealthy after the move

Pool config is validated asynchronously against what the cluster reports (see
[How a pool's config is enforced](./cluster-pools#how-a-pools-config-is-enforced)),
so a mismatch surfaces only after the move, as an unhealthy cluster that
[queues](./queues#how-a-queue-routes) will no longer route new work to.
`flyte get cluster <name>` shows the state, health, and unhealthy reasons. Fix
whichever side is wrong:

- **The cluster's config**: the reported values come from the deployed data
  plane, so change them where that deployment is defined (Terraform, Helm values,
  and so on) and redeploy the cluster. The control plane picks up the new values
  on the cluster's next status report.
- **The pool's config**: run `flyte update cluster-pool <pool>`, which opens the
  pool in your `$EDITOR`. See [Update a pool](./cluster-pools#update-a-pool).

## Delete a cluster

You can delete a cluster from any live state. What happens next depends on its
lifecycle state:

- A `drained` cluster becomes `deleted` immediately.
- An `active` or `draining` cluster becomes `deleting` while the system
  disconnects its workers, makes its running work available to other clusters,
  and drops cluster-specific cleanup work. It becomes `deleted` when that
  teardown finishes.

Deletion does not wait for running work and cannot be canceled. It also does not
remove Kubernetes pods that remain on the data plane. **You are responsible for
cleaning up those pods.** To let work finish normally, first
[drain the cluster](#drain-and-reactivate-a-cluster) and wait for `drained`, then
delete it.

The cluster's [co-named queue](#the-co-named-queue) enters deletion with the
cluster. A drained queue becomes `deleted` immediately; an active or draining
queue becomes `deleting` until its cleanup finishes. The cluster and queue reach
`deleted` independently and may finish in either order. Any other live queue
that explicitly names the cluster blocks deletion; remove the cluster from its
selector first. Wildcard (`*`) queues do not block deletion.

A queue whose selector you empty this way stops routing work anywhere until you
point it at another cluster **in its pool** (or
[move it to another pool](./queues#move-work-to-another-pool) once drained).

{{< tabs "delete-cluster" >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte delete cluster prod-us-east-1
flyte delete cluster prod-us-east-1 --yes   # skip the confirmation prompt

# List deleted clusters, restore one
flyte get cluster --deleted
flyte undelete cluster prod-us-east-1
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
from flyteplugins.union.remote import Cluster

Cluster.delete("prod-us-east-1")
Cluster.undelete("prod-us-east-1")   # restore a deleted cluster
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

The command returns after the cluster becomes either `deleting` or `deleted`.
A `deleting` cluster remains visible in normal listings while teardown runs.
Once `deleted`, it disappears from normal listings and stops accepting status
reports and heartbeats. The record is retained and its name stays reserved, so
registering another cluster with the same name is rejected.

A `deleting` cluster cannot be restored; wait for deletion to finish. Then use
`flyte undelete cluster <name>`. The cluster and its co-named queue both return
in the `drained` state. Run `flyte update cluster <name> --activate` to reactivate
both.

## Next

Once your clusters are registered and healthy, [create queues](./queues) to route
and govern the workloads that run on them.
