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

The node pool configuration is held by Union for each cluster and is not set in the data plane
values. Until a cluster has it, the scheduler treats the cluster as able to run anything and places
work on any healthy cluster the queue routes to. Resource caps and the scheduling policy apply either
way. Two things are configured on the data plane: reporting observed node capacity, and, on a
self-hosted control plane, the scheduling strategy.

> [!NOTE] Data planes connected from the Union.ai UI
> The Helm values on this page are for a data plane installed with Helm. On a data plane connected from
> the Union.ai UI, the agent manages the chart values, so change them through Union.ai rather than with
> `helm upgrade`.

## What the scheduler uses

The scheduler reads two kinds of information about a cluster. Only the first one affects placement.

| Information | Source | Used for |
| --- | --- | --- |
| Node pool configuration | Held by Union for the cluster | Which clusters can run an action, how much room a cluster has at full scale, and which cluster is least loaded |
| Observed node capacity | Reported by the data plane operator when `nodeCapacity` is on | The **Node pools** tab on the cluster page: nodes, pods, CPU, memory, and accelerators in use per pool |

A queue's resource caps are a third limit, set on the queue itself. The scheduler applies them with or
without the node pool configuration.

## Prerequisites

- Resource-aware scheduling enabled for your organization.
- Data plane chart 2026.11.0 or later, to report observed node capacity.
- `flyteplugins-union` 0.16.0 or later, for the `flyte create queue` and `flyte update queue` commands
  that set resource caps.

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
- With resource-aware scheduling enabled for your organization, a task that requests an accelerator no
  node pool in the cluster's configuration offers fails within seconds with error code `INFEASIBLE`,
  and the message names what each pool offers instead.

## See also

- [Resource caps and scheduling](../../../user-guide/clusters-and-queues/resource-caps-and-scheduling): caps, scheduling policies, and infeasible requests.
- [Interruptible task scheduling](./interruptible-scheduling): labeling spot and on-demand nodes.
- [Node pools](./node-pools): separating Union services from worker pods.
- [Data plane Helm chart reference](../helm-chart-reference/dataplane): `config.operator.clusterHealth.nodeCapacity`.
