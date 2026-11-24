---
title: Multi-cluster and multi-cloud
description: Run several Union-Managed clusters, in different cloud accounts or clouds, and choose which one runs your work.
icon: diagram-3
weight: 9
variants: -flyte +union
---

# Multi-cluster and multi-cloud

You can run more than one Union-Managed cluster: for example, separate clusters for development and production, or clusters on both AWS and GCP.
Create each one with the **Add a cluster** wizard, as on the setup page for [AWS](./data-plane-setup-on-aws), [GCP](./data-plane-setup-on-gcp), or [Azure](./data-plane-setup-on-azure).
Each cluster can be in a different cloud, account, and region.

## Each cluster has its own pool

The wizard puts every cluster in a [cluster pool](../../user-guide/clusters-and-queues/cluster-pools) of its own, with its own object store, secret store, and container registry in the cluster's cloud account.
The pool is named `default-<cloud>-<account>-<region>-<cluster>`, for example `default-aws-123456789012-us-east-2-prod`.

Because each cluster has its own pool, a run's code bundle, inputs, and outputs stay in the object store of the cluster that runs it.
Work can't move from one pool to another. See [Crossing a pool boundary](../../user-guide/clusters-and-queues/_index#crossing-a-pool-boundary).

## Choose which cluster runs your work

Every cluster has a queue with the same name as the cluster, which routes only to that cluster.
To run on a particular cluster, submit to its queue:

```bash
flyte run --queue <cluster-name> hello.py main
```

From Python, use `flyte.with_runcontext(queue=...)`. Both require `flyte` 2.12.2 or later.
To send a task's runs to the same cluster every time, set the queue on its task environment. See [Queues](../../user-guide/tasks/task-configuration/queues).

For queues that route to several clusters in a pool, or cap what each team can use, see [Clusters and queues](../../user-guide/clusters-and-queues/_index).
