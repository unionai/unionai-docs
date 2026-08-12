---
title: Clusters
weight: 2
variants: -flyte +union
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
custom pool, create that pool first.

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

Registration additionally ensures the org-wide `default` queue exists. The
`default` queue lives in the `default` pool with the `*` selector, so it routes
to every healthy, enabled cluster in the `default` pool: a cluster registered
there joins it automatically, while a cluster in any other pool never does.

Both are ordinary queues — they appear in `flyte get queue`, carry the same
concurrency, depth, priority, and fairness settings as any other, and are managed
the same way on the [Managing queues](./queues) page. What sets the co-named
queue apart is that its cluster selector and pool are managed by its cluster and
cannot be edited directly: it follows its cluster if the cluster is
[reassigned to another pool](#move-a-cluster-to-a-different-pool), and it is
deleted along with the cluster if the cluster is [deleted](#delete-a-cluster).

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
    print(cluster.name, cluster.pool, cluster.state, cluster.health, cluster.capacity)

cluster = Cluster.get("prod-us-east-1")
print(cluster.name)
print(cluster.pool)
print(cluster.queues)
print(cluster.health, cluster.unhealthy_reasons)
print(cluster.capacity)
print(cluster.config_drift)
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

The detailed view shows the cluster's pool, current state, available capacity, and
which queues are bound to it, useful when deciding where to route or pin a queue.

## Move a cluster to a different pool

A cluster can be reassigned to another pool in place, without deleting and
re-registering it. This is a **disruptive** operation: read the warning below
before you run it.

> [!WARNING] Moving a cluster does not stop in-flight work
> Reassigning a cluster's pool does **not** wait for running work or reschedule
> anything: the change takes effect immediately, switches the cluster's workloads
> to the new pool's object store and secret store, and can break whatever is
> currently running on the cluster. The control plane checks queue state only
> (see the preconditions below) — it does not check for running runs, apps, or
> v1 executions. Ensuring that no {{< key product_name >}} workload is running
> on the cluster is **your responsibility**. Treat this as a maintenance-window
> operation.

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

1. **Drain the co-named queue.** The cluster's [co-named queue](#the-co-named-queue)
   must be in the `drained` state, or the move is rejected.
   [Drain it](./queues#drain-and-reactivate-a-queue) and let its in-flight work
   finish, watching with `flyte get queue <name> --watch`. The drained queue
   moves to the destination pool with the cluster automatically; reactivate it
   after the move.
2. **Repoint other queues.** Any other queue that pins the cluster explicitly
   must have the cluster removed from its selector first, or the move is
   rejected. Wildcard (`*`) queues never block the move — but they also keep
   routing work to the cluster right up to the moment it leaves the pool, which
   is what the warning above is about. `flyte get cluster <name>` lists the
   queues bound to the cluster.
3. **Check for apps and v1 executions.** A cluster does not only serve runs: it
   can also be hosting [apps](../serve-and-deploy-apps/_index) and legacy v1
   executions, which {{< key product_name >}} still supports today. There is
   currently **no way to see how many apps or v1 executions are running on a
   given cluster**, and the queue preconditions above do not account for them,
   so nothing will block the move. If any are running when you reassign the
   cluster, the cluster can be marked unhealthy and drop out of scheduling until
   the mismatch is resolved. Confirm out-of-band that the cluster is idle before
   moving it.
4. **Make sure the configs match.** The destination pool's config must match
   what the cluster reports, or the cluster goes unhealthy shortly after the
   move — see below.

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

Deleting a cluster requires the same quiescing as a
[pool move](#move-a-cluster-to-a-different-pool):

- The cluster's [co-named queue](#the-co-named-queue) must be **drained** first —
  [draining it](./queues#drain-and-reactivate-a-queue) is also what lets
  in-flight work finish before the cluster goes away. The co-named queue is then
  deleted together with the cluster.
- Any other queue that pins the cluster explicitly **blocks** the delete: remove
  the cluster from those selectors first. Wildcard (`*`) queues never block a
  delete.

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

Deletion is a **soft delete**: the cluster disappears from listings and can no
longer report status or heartbeat, but its record is kept and its name stays
reserved — registering a new cluster under the same name is rejected. Restore it
with `flyte undelete cluster <name>`, which also restores the co-named queue;
the restored queue comes back drained, so
[reactivate it](./queues#drain-and-reactivate-a-queue) to resume routing to the
cluster.

## Next

Once your clusters are registered and healthy, [create queues](./queues) to route
and govern the workloads that run on them.
