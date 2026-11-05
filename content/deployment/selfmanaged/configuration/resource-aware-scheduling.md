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

On a self-managed cluster, Union does not discover your node pool configuration. You provide it, and
Union records it on your cluster. Until it is recorded, the scheduler treats the cluster as able to run
anything and places work on any healthy cluster the queue routes to. Resource caps and the scheduling
policy apply either way.

> [!NOTE] Data planes connected from the Union.ai UI
> The Helm values on this page are for a data plane installed with Helm. On a data plane connected from
> the Union.ai UI, the agent manages the chart values, so change them through Union.ai rather than with
> `helm upgrade`. Providing your node pool configuration applies either way.

## What the scheduler uses

The scheduler reads two kinds of information about a cluster. Only the first one affects placement.

| Information | Source | Used for |
| --- | --- | --- |
| Node pool configuration | Provided by you, recorded by Union on the cluster | Which clusters can run an action, how much room a cluster has at full scale, and which cluster is least loaded |
| Observed node capacity | Reported by the data plane operator when `nodeCapacity` is on | The **Node pools** tab on the cluster page: nodes, pods, CPU, memory, and accelerators in use per pool |

A queue's resource caps are a third limit, set on the queue itself. The scheduler applies them with or
without the node pool configuration.

## Prerequisites

- Resource-aware scheduling turned on for your organization. Ask the Union team.
- Data plane chart 2026.11.0 or later, to report observed node capacity.
- `flyteplugins-union` 0.16.0 or later, for the `flyte create queue` and `flyte update queue` commands
  that set resource caps.

## Provide your node pool configuration

Send the Union team one entry per node pool that task pods can land on. Leave out pools reserved for
Union services or other workloads: a pool that is listed is a pool the scheduler counts on.

| Field | What to provide | Where to find it |
| --- | --- | --- |
| Name | The pool's name in your cloud provider or autoscaler | EKS node group, GKE node pool, AKS node pool, or Karpenter `NodePool` name |
| Instance types | The instance types the pool launches | The pool definition. A Karpenter pool that selects by requirements can list several |
| Allocatable CPU, memory, and ephemeral storage per node | What one node offers to pods, not the instance's nominal size | `kubectl describe node <node>` under **Allocatable** |
| Accelerators per node | Device model and count, and the MIG partition size if the pool is partitioned | The instance type, or `kubectl describe node <node>` under **Allocatable** and the node's accelerator label |
| Labels | Labels every node in the pool carries | The pool definition. Include the label a task's node selector would match |
| Taints | Taints every node in the pool carries | The pool definition |
| Scaling limit | The maximum node count, or the autoscaler's resource limits | EKS, GKE, and AKS pools have a maximum node count. A Karpenter pool has `spec.limits` (for example `cpu: 1000`, `nvidia.com/gpu: 8`) and no node count |
| Capacity type | On-demand, spot, or both when the pool falls back from spot to on-demand | The pool definition. See [Interruptible task scheduling](./interruptible-scheduling) for how spot nodes are labeled |
| CPU architecture | `amd64` or `arm64` | The instance type |

If you automate cluster changes, the same record is readable and writable through the managed cluster
API: `GET /managed_cluster/api/v1/{organization}/{cluster}/node_groups` returns the pools and a
generation, and `POST` to the same path with the generation replaces the whole set. A write replaces
every pool, so send the complete list.

> [!WARNING] Keep the configuration in sync with the cluster
> The scheduler decides from the recorded configuration, not from the nodes that exist. When you add,
> resize, or remove a node pool, send the change to the Union team (or write it through the API) in the
> same change. A GPU pool you added but did not record is invisible to the scheduler: a task that asks
> for that GPU fails as `INFEASIBLE`, because no recorded pool offers it. A pool you removed but left
> recorded is still counted as room, so work is placed on the cluster and then pends in Kubernetes.

## Report observed node capacity

Turn on `nodeCapacity` to have the operator report each node pool's nodes, pods, CPU, memory, and
accelerators into cluster health. The cluster page's **Node pools** tab then shows the recorded
configuration next to what the cluster is doing.

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

If you run the control plane chart yourself, the scheduling strategy is set in your control plane
values rather than by the Union team:

```yaml
services:
  leasor:
    configMap:
      leasor:
        runtime:
          scheduler:
            strategy: v2
```

With `v2`, queue resource caps and scheduling policies are enforced. The node pool configuration is
not available on a self-hosted control plane, so the checks that need it (which clusters can run an
action, room at full scale, and cluster-level infeasibility) are not active; `v3` behaves the same as
`v2` there. Observed node capacity still shows on the **Node pools** tab when `nodeCapacity` is on.

The console's resource cap fields are hidden on a self-hosted control plane. Set caps with
`flyte create queue` and `flyte update queue`, or with `Queue.create` and `Queue.update` in Python.

## Verify

- `flyte get queue <name> --watch` shows each cap with its usage.
- The cluster page's **Node pools** tab lists your pools with live counts once `nodeCapacity` is on
  and the operator has pushed a snapshot.
- With resource-aware scheduling on for your organization, a task that requests an accelerator none of
  your recorded pools offers fails within seconds with error code `INFEASIBLE`, and the message names
  what each pool offers instead.

## See also

- [Resource caps and scheduling](../../../user-guide/clusters-and-queues/resource-caps-and-scheduling): caps, scheduling policies, and infeasible requests.
- [Interruptible task scheduling](./interruptible-scheduling): labeling spot and on-demand nodes.
- [Node pools](./node-pools): separating Union services from worker pods.
- [Data plane Helm chart reference](../helm-chart-reference/dataplane): `config.operator.clusterHealth.nodeCapacity`.
