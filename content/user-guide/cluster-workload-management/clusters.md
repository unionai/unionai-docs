---
title: Clusters
weight: 2
variants: -flyte +union
---

# Clusters

> [!NOTE] Requires the `flyteplugins-union` plugin
> The `flyte` cluster commands on this page are provided by the
> `flyteplugins-union` package. Install it with `pip install flyteplugins-union`.

A **cluster** is an execution cluster registered with {{< key product_name >}}.
Every cluster subscribes to exactly one [cluster pool](./cluster-pools), which
determines the data plane (object store, secrets, registry) the cluster uses.

## Register a cluster

Register a cluster into the `default` pool by omitting the pool flag:

```bash
flyte create cluster my-cluster
```

Or register it into a specific pool:

```bash
flyte create cluster prod-us-east-1 --pool prod
```

When a cluster registers, its declared object store, secret store, and container
registry are validated against the target pool's data plane contract. A cluster
whose configuration doesn't match the pool is rejected — this is what guarantees
that any workload routed to the pool can run on any of its clusters.

## Inspect clusters

```bash
# List all clusters (grouped by enabled / disabled)
flyte get cluster

# Inspect one cluster — cloud config, state, capacity, and bound queues
flyte get cluster prod-us-east-1

# Cap the number of results
flyte get cluster --limit 50
```

The detailed view shows the cluster's pool, current state, available capacity, and
which queues are bound to it — useful when deciding where to route or pin a queue.

## Move a cluster to a different pool

A cluster's pool membership is managed from the pool side. Edit the target (or
current) pool's `member_clusters` list:

```bash
flyte update cluster-pool prod
```

Because pools share a data plane contract, only move a cluster into a pool whose
object store, secrets, and registry match the cluster's configuration.

## Delete a cluster

```bash
flyte delete cluster prod-us-east-1
flyte delete cluster prod-us-east-1 --yes   # skip the confirmation prompt
```

Drain or repoint any queues bound to a cluster before removing it.

## Next

Once your clusters are registered and healthy, [create queues](./queues) to route
and govern the workloads that run on them.
