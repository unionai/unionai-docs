---
title: Multi-cluster and multi-cloud
description: Run several Union-Managed clusters, in different cloud accounts or clouds, and choose which one runs your work.
icon: diagram-3
weight: 9
variants: -flyte +union
---

# Multi-cluster and multi-cloud

You can run more than one Union-Managed cluster: for example, separate clusters for development and production.
Create each one with the **Add a cluster** wizard, as on the setup page for [AWS](./data-plane-setup-on-aws), [GCP](./data-plane-setup-on-gcp), or [Azure](./data-plane-setup-on-azure).

- The wizard builds one cluster at a time in an organization. Start the next once the previous build ends.
- Each cluster can be in a different account, in any region the console offers. Clusters in more than one region or cloud need the Enterprise plan.
- The Team plan allows two active clusters. See [Product tiers](../product-tiers).

## Each cluster has its own pool

The wizard puts every cluster in a [cluster pool](../../user-guide/clusters-and-queues/cluster-pools) of its own, with its own object store and container registry in the cluster's cloud account.
Secrets are stored in the account's Secrets Manager in the cluster's region (AWS), in the project's Secret Manager (GCP), or in the cluster's own key vault (Azure).

The pool is named `default-<cloud>-<account>-<region>-<cluster>`, for example `default-aws-123456789012-us-east-2-prod`.
The name is lowercased and, past 63 characters, shortened with a hash. `flyte get cluster-pool` lists the exact names.

A run's code bundle, inputs, and outputs stay in the object store of the cluster that runs it.
Work can't move from one pool to another. See [Crossing a pool boundary](../../user-guide/clusters-and-queues/_index#crossing-a-pool-boundary).

## Choose which cluster runs your work

Every cluster has a queue with the same name as the cluster, which routes only to that cluster.
To run on a particular cluster, submit to its queue:

```bash
flyte run --queue <cluster-name> hello.py main
```

From Python, use `flyte.with_runcontext(queue=...)`.
To send a task's runs to the same cluster every time, set the queue on its task environment. See [Queues](../../user-guide/tasks/task-configuration/queues).

Sending a run's code bundle and inputs to its queue's cluster requires `flyte` 2.12.2 or later.
With `flyte run`, local `File`, `Dir`, and `DataFrame` inputs need `flyte` 2.15.0 or later.

A run that names no queue goes to the `run.default_queue` setting of its project and domain or, if that isn't set, to the `default` queue, which is in your first cluster's pool.
To send all of a project's or domain's work to one cluster, set its `run.default_queue` to that cluster's queue.
See [Route work to the right cluster pool](../../user-guide/project-patterns/resource-management#route-work-to-the-right-cluster-pool-in-multi-cluster-deployments).

For queue limits and resource caps, see [Clusters and queues](../../user-guide/clusters-and-queues/_index).
