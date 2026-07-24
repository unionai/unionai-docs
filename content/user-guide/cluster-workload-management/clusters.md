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
determines the data plane (object store, secrets, registry) the cluster uses.

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
config and marks the cluster **unhealthy** on a mismatch. An unhealthy cluster is
no longer eligible for
[wildcard routing](./queues#how-a-queue-routes), so queues with the `*` selector
stop sending new work to it until it recovers. If the pool has no config yet, the
first cluster to report instead *populates* it. See
[How a pool's config is established](./cluster-pools#how-a-pools-config-is-established)
for the full mechanism.

This is what guarantees that any workload routed to the pool can run on any of
its healthy clusters — so after registering into a custom pool, confirm with
`flyte get cluster <name>` that the cluster settles healthy.

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
the same way on the [Managing queues](./queues) page. Two behaviors are specific
to the co-named queue: it follows its cluster if the cluster is
[reassigned to another pool](#move-a-cluster-to-a-different-pool), and its
selector empties out if the cluster is [deleted](#delete-a-cluster).

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
> Reassigning a cluster's pool does **not** drain the cluster, wait for running
> work, or reschedule anything. The change takes effect immediately and can break
> whatever is currently running on that cluster. The control plane enforces
> exactly one precondition — that no custom-named queue in the current pool still
> points at the cluster — and checks nothing else. Ensuring that no
> {{< key product_name >}} workload is running on the cluster is **your
> responsibility**. Treat this as a maintenance-window operation.

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

### Before you move a cluster

1. **Repoint custom-named queues.** Any queue *other* than the one named after
   the cluster that pins it must be repointed or removed from the cluster first,
   or the move is rejected. The cluster's [co-named queue](#the-co-named-queue)
   moves to the destination pool with it, automatically.
   `flyte get cluster <name>` lists the queues bound to the cluster.
2. **Let runs finish.** [Draining](./queues#drain-and-reactivate-a-queue) is
   coming in a future release; until it ships, wait for in-flight work to finish,
   watching with `flyte get queue <name> --watch`.
3. **Check for apps and v1 executions.** A cluster does not only serve runs: it
   can also be hosting [apps](../serve-and-deploy-apps/_index) and legacy v1
   executions, which {{< key product_name >}} still supports today. There is
   currently **no way to see how many apps or v1 executions are running on a
   given cluster**, and the queue precondition above does not account for them,
   so nothing will block the move. If any are running when you reassign the
   cluster, the cluster can be marked unhealthy and drop out of scheduling until
   the mismatch is resolved. Confirm out-of-band that the cluster is idle before
   moving it.
4. **Make sure the configs match.** The destination pool's config must match
   what the cluster reports, or the cluster goes unhealthy shortly after the
   move — see below.

### If the cluster goes unhealthy after the move

Pool config is validated asynchronously against what the cluster reports (see
[How a pool's config is established](./cluster-pools#how-a-pools-config-is-established)),
so a mismatch surfaces only after the move, as an unhealthy cluster that
[wildcard queues](./queues#how-a-queue-routes) will no longer route to.
`flyte get cluster <name>` shows the state, health, and unhealthy reasons. Fix
whichever side is wrong:

- **The cluster's config**: the reported values come from the deployed data
  plane, so change them where that deployment is defined (Terraform, Helm values,
  and so on) and redeploy the cluster. The control plane picks up the new values
  on the cluster's next status report.
- **The pool's config**: run `flyte update cluster-pool <pool>`, which opens the
  pool in your `$EDITOR`. See [Update a pool](./cluster-pools#update-a-pool).

## Delete a cluster

[Drain](./queues#drain-and-reactivate-a-queue) or repoint any queues bound to a
cluster before removing it, so in-flight work isn't lost when the cluster goes
away. (Draining is coming in a future release; until it ships, repoint the queue
or wait for its in-flight work to finish.)

Deleting a cluster automatically removes it from the selector of every queue
that pins it explicitly; wildcard (`*`) queues are unaffected. A queue whose
selector becomes empty stops routing work anywhere until you point it at
another cluster **in its pool**. You cannot move a queue to another pool, so if
the replacement cluster lives in a different pool, create a new queue there
instead.

{{< tabs "delete-cluster" >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte delete cluster prod-us-east-1
flyte delete cluster prod-us-east-1 --yes   # skip the confirmation prompt
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
from flyteplugins.union.remote import Cluster

Cluster.delete("prod-us-east-1")
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## Next

Once your clusters are registered and healthy, [create queues](./queues) to route
and govern the workloads that run on them.
