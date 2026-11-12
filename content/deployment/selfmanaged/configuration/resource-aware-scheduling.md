---
title: Resource-aware scheduling
description: Give the scheduler your cluster's node pool configuration so it places work only where it fits, and report live node capacity to the console.
icon: cpu
weight: 2
variants: -flyte +union
---

# Resource-aware scheduling

With resource-aware scheduling, a queue places an action only on a cluster that can run it, waits when
a cluster is full, and fails up front an action that no cluster could ever run. The scheduler decides
this from your cluster's **node pool configuration**: the node pools, the size of a node in each pool,
the accelerators on it, and how far the pool can scale. For how queues, resource caps, and scheduling
policies work, see [Resource caps and scheduling](../../../user-guide/clusters-and-queues/resource-caps-and-scheduling)
in the user guide. This page covers what a self-managed data plane contributes and what you configure.

You declare the node pool configuration for each cluster with `flyte update node-groups`; the
scheduler reads only what is declared, not what the operator observes. Until a cluster has a
declaration, the scheduler treats it as able to run anything and places work on any healthy cluster
the queue routes to. Resource caps and the scheduling policy apply either way. This page covers the
declaration, the optional reporting of observed capacity, and, on a self-hosted control plane, the
scheduling strategy.

> [!NOTE] Data planes connected from the Union.ai UI
> The Helm values on this page are for a data plane installed with Helm. On a data plane connected from
> the Union.ai UI, the agent manages the chart values, so change them through Union.ai rather than with
> `helm upgrade`.

## What the scheduler uses

The scheduler reads two kinds of information about a cluster. Only the first one affects placement.

| Information | Source | Used for |
| --- | --- | --- |
| Node pool configuration | Declared by you with `flyte update node-groups` | Which clusters can run an action, how much room a cluster has at full scale, and which cluster is least loaded |
| Observed node capacity | Reported by the data plane operator when `nodeCapacity` is on; never used for placement | The **Node pools** tab on the cluster page: nodes, pods, CPU, memory, and accelerators in use per pool |

A queue's resource caps are a third limit, set on the queue itself. The scheduler applies them with or
without the node pool configuration.

## Version requirements

| What | Needs |
| --- | --- |
| Resource-aware scheduling for your organization | Enabled by Union.ai per organization |
| `flyte get node-groups` and `flyte update node-groups`, and `NodeGroups` in Python | `flyteplugins-union` 0.20.2 or later, which runs with `flyte` 2.10.1 through 2.12.x |
| Queue resource caps from the CLI or Python | `flyteplugins-union` 0.16.0 or later (covered by the line above) |
| Writing node groups | Permission to manage the cluster (the `MANAGE_CLUSTER` action on it) |
| A managed-cluster record for the cluster | Created by the **Connect your cluster** flow, which only organizations created through self-serve sign-up have in the Union.ai UI, and which installs the agent-managed data plane. Every other registration path (**Create cluster** in Settings > Clusters, `flyte create cluster`) creates none; Union.ai creates the record for those clusters. See the note under *Declare your node pools* |
| Observed node capacity on the **Node pools** tab | Data plane chart 2026.11.0 or later for the `nodeCapacity` switch. On a self-hosted control plane, also controlplane chart 2026.11.0 or later for the tab itself |
| Scheduling strategy on a self-hosted control plane | Controlplane chart `2026.9.7` or later |

On a self-managed deployment the control plane is Union.ai's and always current, so only the plugin,
permission, and data plane chart rows apply.

## Declare your node pools

The declaration is the list of node pools that task pods can land on, with what one node in each pool
offers and how far the pool can scale. The scheduler decides from it which clusters can run an action,
how much room a cluster has at full scale, and which cluster is least loaded.

Export the current declaration, edit it, and apply it back. `update` replaces the whole set, so always
work from the complete list:

```bash
flyte get node-groups <cluster> --export > node-groups.yaml
# edit node-groups.yaml
flyte update node-groups <cluster> -f node-groups.yaml
```

Without `-f`, `flyte update node-groups <cluster>` opens the declaration in `$EDITOR`. Either way the
command prints which groups are added, removed, or changed, and asks before removing one.

> [!NOTE] The declaration attaches to the cluster's managed-cluster record
> The **Connect your cluster** flow creates that record along with the agent-managed data plane it
> installs. It appears on the home page and in Settings > Clusters only for organizations created
> through self-serve sign-up. For every other organization, Settings > Clusters offers **Create
> cluster**, which, like `flyte create cluster` and `Cluster.create()`, registers the cluster without a
> record. On such a cluster both node-groups commands fail with
> `cluster '<name>' not found: missing entity of type ManagedCluster` until Union.ai creates the record
> for it. The scheduler treats the cluster as able to run anything in the meantime, as described above.

A declaration with two pools, one on-demand CPU pool with a node-count ceiling and one GPU pool bounded
by Karpenter limits instead of a node count:

```yaml
node_groups:
- name: cpu-workers
  min_nodes: 1
  max_nodes: 20
  node_instance_types: [m6i.4xlarge]
  capacity_types: [CAPACITY_TYPE_ON_DEMAND]
  labels:
    union.ai/node-role: worker
- name: gpu-h100
  min_nodes: 0
  max_nodes: 0            # 0 means no node-count bound; `limits` is the ceiling
  node_instance_types: [p5.48xlarge]
  capacity_types: [CAPACITY_TYPE_ON_DEMAND, CAPACITY_TYPE_SPOT]
  limits:
    cpu: "3840"
    nvidia.com/gpu: "160"
  labels:
    union.ai/node-role: worker
    platform.union.ai/accelerator: nvidia-h100
```

The export shows every field the scheduler reads, in the format the server stores: allocatable
resources per node, accelerators with their partition size, taints, and CPU architecture. Fill them from
`kubectl describe node` on a node of the pool and from the pool's definition in your cloud provider or
autoscaler. Quantities in `limits` are strings. Leave out pools reserved for Union services or other
workloads: a declared pool is a pool the scheduler counts on.

> [!WARNING] Keep the declaration in sync with the cluster
> The scheduler decides from the declaration, not from the nodes that exist. Update it in the same
> change that adds, resizes, or removes a node pool. A GPU pool you added but did not declare is
> invisible to the scheduler: a task that asks for that GPU fails as `INFEASIBLE`, because no declared
> pool offers it. A pool you removed but left declared still counts as room, so work is placed on the
> cluster and then pends in Kubernetes. Turn on observed capacity (below) to see the declaration next to
> what the cluster is actually running on the cluster page's **Node pools** tab.

`NodeGroups.get` and `NodeGroups.set` in `flyteplugins.union.remote` do the same from Python; see the
[NodeGroups reference](../../../api-reference/union-plugin/flyteplugins.union.remote/nodegroups).

## Report observed node capacity

Turn on `nodeCapacity` to have the operator report each node pool's nodes, pods, CPU, memory, and
accelerators into cluster health. The cluster page's **Node pools** tab then shows your declaration
next to what the cluster is doing. The report is for you to read; the scheduler does not use it.

```yaml
config:
  operator:
    clusterHealth:
      nodeCapacity:
        enabled: true
        clusterWidePods: true
```

The setting renders a read-only `ClusterRole` that lets the operator list and watch nodes, and pods
when `clusterWidePods` is set. It is independent of `low_privilege`: a low-privilege data plane can
report capacity without the broad operator `ClusterRole`.

Set `clusterWidePods: true` on a data plane with `low_privilege: true`. Without it, a low-privilege
operator is limited to its own namespace, so it reports node counts and allocatable capacity but not
usage or accelerators.

A data plane that leaves `nodeCapacity` off reports no capacity rather than partial capacity, and the
heartbeat's namespace `ResourceQuota` totals are what the cluster page shows.

## Set resource caps on your queues

Caps need nothing from the data plane. Set them per queue with the CLI, Python, or the console, as
described in [Set caps on a queue](../../../user-guide/clusters-and-queues/resource-caps-and-scheduling#set-caps-on-a-queue).
Size each queue's `max_resources` and `max_accelerators` to the share of the cluster that queue may
hold, and choose `greedy_capacity` unless the queue runs gang-style jobs.

## Self-hosted control planes

If you run the control plane chart yourself, set the scheduling strategy in your control plane
values:

```yaml
services:
  leasor:
    configMap:
      leasor:
        runtime:
          scheduler:
            strategy: v2
```

With `v2`, queue resource caps and scheduling policies are enforced. A self-hosted control plane has no
managed-cluster record for its data planes and no way to create one, so `flyte update node-groups`
fails with `missing entity of type ManagedCluster` there and the checks that need a declaration (which clusters can run an action, room at full scale, and
cluster-level infeasibility) are not active; `v3` behaves the same as `v2`. Observed node capacity still
shows on the **Node pools** tab when `nodeCapacity` is on.

The console's resource cap fields are hidden on a self-hosted control plane. Set caps with
`flyte create queue` and `flyte update queue`, or with `Queue.create` and `Queue.update` in Python.

## Verify

- `flyte get queue <name> --watch` shows each cap with its usage.
- The cluster page's **Node pools** tab lists your pools with live counts once `nodeCapacity` is on
  and the operator has pushed a snapshot.
- `flyte get node-groups <cluster>` shows the declaration the scheduler reads.
- With resource-aware scheduling enabled for your organization, a task that requests an accelerator no
  declared pool offers fails within seconds with error code `INFEASIBLE`, and the message names what
  each pool offers instead.

## See also

- [Resource caps and scheduling](../../../user-guide/clusters-and-queues/resource-caps-and-scheduling): caps, scheduling policies, and infeasible requests.
- [Clusters](../../../user-guide/clusters-and-queues/clusters): registering and inspecting clusters.
- [Interruptible task scheduling](./interruptible-scheduling): labeling spot and on-demand nodes.
- [Node pools](./node-pools): separating Union services from worker pods.
- [Data plane Helm chart reference](../helm-chart-reference/dataplane): `config.operator.clusterHealth.nodeCapacity`.
