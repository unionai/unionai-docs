---
title: Multiple Clusters
description: Attach several Kubernetes clusters to one control plane with cluster pools.
icon: diagram-3
weight: 3
variants: -flyte +union
---

# Multiple clusters

Union enables you to integrate multiple Kubernetes clusters into a single Union control plane using cluster pools.

You create and manage cluster pools yourself with the `flyte create cluster-pool` command from the `flyteplugins-union` plugin. Each cluster belongs to exactly one pool. Create the pool first, then name it with `--pool` when you register the cluster with `flyte create cluster`. Without `--pool`, the cluster joins the `default` pool. If you created your organization by signing up, create `default` with `flyte create cluster-pool` first; if Union.ai set up your organization, `default` is created when its first cluster is registered. Register each cluster under the name you set as `global.CLUSTER_NAME` when you install the `unionai/dataplane` Helm chart. You can have as many cluster pools as needed. See [Cluster pools](../../../user-guide/clusters-and-queues/cluster-pools) for how to create pools, manage membership and move a cluster to another pool.

## Routing work to a cluster pool

Work reaches a cluster pool through a queue. A queue lives in one cluster pool and routes runs to the clusters in it; users submit to a queue, never to a pool or a cluster directly. See [Cluster pools](../../../user-guide/clusters-and-queues/cluster-pools) and [Managing queues](../../../user-guide/clusters-and-queues/queues) for the full model.

These examples assume pools named `development-cp` and `production-cp`, created with `flyte create cluster-pool`.

> [!NOTE] Requires the `flyteplugins-union` plugin
> The `flyte create queue` and related commands are provided by the `flyteplugins-union` package. Install it with `pip install flyteplugins-union`.

### Route a project or domain to a pool

Create a queue in the target pool, then set it as the default queue for the project-domain scope through the [settings](../../../user-guide/get-started/core-concepts/settings) hierarchy.

1. Create a queue in the pool the work should land in:

```bash
flyte create queue development-queue \
  --cluster-pool development-cp \
  --run-concurrency 100 \
  --action-concurrency 1000
```

2. Set that queue as the default for the project-domain scope:

```bash
flyte edit settings --domain development --project flytesnacks
```

   Uncomment and set `run.default_queue` in the editor:

```yaml
run.default_queue: development-queue
```

New runs in `flytesnacks-development` are submitted to `development-queue`, which routes them to the clusters in `development-cp`.

### Route a specific workflow to a pool

Routing is per task environment rather than per matchable attribute. To send one workflow to a different pool, target a queue in that pool with the `queue` parameter on the workflow's `flyte.TaskEnvironment` (or on an individual task):

```python
import flyte

env = flyte.TaskEnvironment(
    name="critical",
    queue="production-queue",  # a queue that lives in production-cp
)
```

You can also choose a queue when you launch a run, or from a trigger, without touching task code. See [Queues](../../../user-guide/tasks/task-configuration/queues) for every way to target a queue.

## Data sharing between cluster pools

The sharing of metadata is controlled by the cluster pool to which a cluster belongs. If two clusters are in the same cluster pool, then they must share the same metadata bucket, defined in the Helm values as `storage.bucketName`.

If they are in different cluster pools, then they **must** have different metadata buckets. You could, for example, have a single metadata bucket for all your development clusters, and a separate one for all your production clusters, by grouping the clusters into cluster pools accordingly.

 Alternatively you could have a separate metadata bucket for each cluster, by putting each cluster in its own cluster pool.
