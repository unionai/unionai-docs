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
{{< /tabs >}}

When a cluster registers, its declared object store, secret store, and container
registry are validated against the target pool's data plane contract. A cluster
whose configuration doesn't match the pool is marked unhealthy or rejected,
depending on where the mismatch is detected. This is what guarantees that any
workload routed to the pool can run on any of its healthy clusters.

Registering a cluster also ensures two **implicit queues** exist: the org-wide
`default` queue (in the `default` pool, routing to all of its clusters), and a
queue named after the cluster, pinned to it, in the cluster's pool — so every
cluster can be targeted by name from day one. Both are ordinary queues; manage
them like any other on the [Queues](./queues) page.

## Inspect clusters

{{< tabs "inspect-cluster" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}
```python
from flyteplugins.union.remote import Cluster

for cluster in Cluster.listall(limit=100):
    print(cluster.name, cluster.pools, cluster.state, cluster.health, cluster.capacity)

cluster = Cluster.get("prod-us-east-1")
print(cluster.name)
print(cluster.pools)
print(cluster.queues)
print(cluster.config_drift)
```
{{< /markdown >}}
{{< /tab >}}
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
{{< /tabs >}}

The detailed view shows the cluster's pool, current state, available capacity, and
which queues are bound to it — useful when deciding where to route or pin a queue.

## Move a cluster to a different pool

A cluster's pool assignment is fixed for the life of the cluster record — a
registration that names a different pool for an existing cluster is rejected,
because the cluster may already have reported status, synced configuration, and
served workloads against the old pool's data plane. Moving a cluster is
therefore a delete-and-re-register:

1. [Drain](./queues#drain-and-reactivate-a-queue) the queues that pin the
   cluster, so in-flight work finishes without new submissions landing. (While
   draining is disabled, stop submissions and watch the queues empty with
   `flyte get queue <name> --watch`.)
2. Delete the cluster record. This automatically removes the cluster from the
   selector of every queue that pinned it.
3. Register the cluster in the destination pool — under a **new name**.
4. Point queues at the new cluster: create new queues in the destination pool,
   or add the new cluster to the selectors of existing queues in that pool.

Use a new name for the re-registered cluster. Registration creates an implicit
queue named after the cluster, and a queue's pool can never change — so if you
reuse the old name, the existing same-named queue stays bound to the **old**
pool with an empty selector, and anything still targeting that queue by name
silently routes nowhere.

## Delete a cluster

[Drain](./queues#drain-and-reactivate-a-queue) or repoint any queues bound to a
cluster before removing it, so in-flight work isn't lost when the cluster goes
away. (While draining is disabled, stop submissions and let in-flight work
finish first.)

Deleting a cluster automatically removes it from the selector of every queue
that pins it explicitly; wildcard (`*`) queues are unaffected. A queue whose
selector becomes empty stops routing work anywhere until you point it at
another cluster.

{{< tabs "delete-cluster" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}
```python
from flyteplugins.union.remote import Cluster

Cluster.delete("prod-us-east-1")
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}
```bash
flyte delete cluster prod-us-east-1
flyte delete cluster prod-us-east-1 --yes   # skip the confirmation prompt
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## Next

Once your clusters are registered and healthy, [create queues](./queues) to route
and govern the workloads that run on them.
