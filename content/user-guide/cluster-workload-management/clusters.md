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

## Change a cluster's pool

A cluster's pool assignment is effectively fixed once the cluster exists. Repeating
cluster creation with a different pool is rejected, because the cluster may already
have reported status, synced configuration, and served workloads against the old
pool's data plane.

To use a different pool, register a new cluster in the destination pool and move
queues or workload routing to that new cluster. If you need to replace the
existing cluster with the same name, repoint any queues first, delete the old
cluster record, then register it again in the intended pool.

## Delete a cluster

Repoint any queues bound to a cluster before removing it.

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
