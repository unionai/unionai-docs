---
title: Interruptible task scheduling
weight: 1
variants: -flyte +union
---

# Interruptible task scheduling

Interruptible tasks are allowed to run on spot (also called preemptible) instances, which cloud
providers offer at a lower price but can be reclaimed at any time. A task left non-interruptible should
stay on on-demand instances so that it is not evicted while it runs.

On a self-managed cluster, Union has no way to tell which of your nodes are spot and which are
on-demand unless you configure it. If you skip this configuration, the `interruptible` setting has no
effect on placement. Both kinds of task can land on either kind of node, and a non-interruptible task
may be evicted when a spot node is reclaimed.

To make the `interruptible` setting take effect, tell Union how to recognize your spot and on-demand
nodes using the keys described below. For how to mark a task or task environment as interruptible in
your workflow code, see [Interruptible tasks](../../../user-guide/task-configuration/interruptible-tasks-and-queues)
in the user guide.

## Scheduling mechanisms

Union separates spot and on-demand work using two mechanisms, and we recommend configuring both. Each
one closes a gap that the other leaves open, and together they match how Union runs its own managed
clusters.

Node affinity uses a label on your nodes to pin pods to a capacity type. Union gives a non-interruptible
pod a required node affinity that only matches on-demand nodes, and pins an interruptible pod to spot
nodes.

Taints and tolerations work from the other direction. You taint your spot nodes so they reject any pod
that does not tolerate the taint, and Union hands out the matching toleration only to interruptible
pods. Non-interruptible pods never receive the toleration, so they are kept off spot nodes.

Node affinity is applied to each pod as Union builds it, so on its own it only protects pods that go
through Union's normal task path. Taints are enforced by the Kubernetes scheduler no matter how a pod
is created, so they also cover pods that do not receive the affinity, such as the Ray job submitter
pod. Because neither mechanism covers every case by itself, set up both.

## Configuration keys

Union translates the `interruptible` flag into scheduling constraints using three keys under
`config.k8s.plugins.k8s` in your data plane values file:

`interruptible-node-selector-requirement` adds a required node affinity term to interruptible pods so
that they target your spot nodes.

`non-interruptible-node-selector-requirement` adds a required node affinity term to non-interruptible
pods so that they target your on-demand nodes. This is the key that keeps non-interruptible tasks off
spot.

`interruptible-tolerations` adds one or more tolerations to interruptible pods so they can schedule
onto tainted spot nodes.

When a key is left unset, Union skips that constraint. If `non-interruptible-node-selector-requirement`
is unset, for example, non-interruptible pods receive no affinity and rely entirely on taints to stay
off spot.

## Pinning tasks with node affinity

The node affinity keys match against a label that identifies the capacity type of each node. The label
to use depends on how your nodes are provisioned. Set both keys so that interruptible tasks target spot
nodes and non-interruptible tasks target on-demand nodes.

### AWS (EKS)

EKS managed node groups apply the `eks.amazonaws.com/capacityType` label automatically, with a value of
`SPOT` or `ON_DEMAND`.

```yaml
config:
  k8s:
    plugins:
      k8s:
        interruptible-node-selector-requirement:
          key: eks.amazonaws.com/capacityType
          operator: In
          values:
          - SPOT
        non-interruptible-node-selector-requirement:
          key: eks.amazonaws.com/capacityType
          operator: In
          values:
          - ON_DEMAND
```

If your nodes are provisioned by Karpenter rather than by managed node groups, use the
`karpenter.sh/capacity-type` label instead, with the values `spot` and `on-demand`.

### GCP (GKE)

GKE labels Spot VM nodes with `cloud.google.com/gke-spot` set to `"true"`. Standard nodes do not carry
this label, so non-interruptible pods can match on its absence using the `DoesNotExist` operator.

```yaml
config:
  k8s:
    plugins:
      k8s:
        interruptible-node-selector-requirement:
          key: cloud.google.com/gke-spot
          operator: In
          values:
          - "true"
        non-interruptible-node-selector-requirement:
          key: cloud.google.com/gke-spot
          operator: DoesNotExist
```

### Azure (AKS)

AKS labels spot nodes with `kubernetes.azure.com/scalesetpriority` set to `spot`. Regular priority
nodes do not carry this label.

```yaml
config:
  k8s:
    plugins:
      k8s:
        interruptible-node-selector-requirement:
          key: kubernetes.azure.com/scalesetpriority
          operator: In
          values:
          - spot
        non-interruptible-node-selector-requirement:
          key: kubernetes.azure.com/scalesetpriority
          operator: DoesNotExist
```

When the operator is `DoesNotExist`, omit the `values` field.

### Other providers

If you provision nodes yourself, or your provider does not apply a capacity-type label, you can use any
label that tells your spot nodes apart from your on-demand nodes. To see what labels your nodes already
carry, run:

```bash
kubectl get nodes --show-labels
```

Look for a label that your provisioner sets on spot nodes and reference its key in both node selector
requirements. If no such label exists, add your own to each pool, for example
`union.ai/capacity-type=interruptible` on the spot pool and `union.ai/capacity-type=on-demand` on the
on-demand pool, then point both keys at that label.

## Keeping tasks off spot with taints

Node affinity covers the pods that Union builds through its standard task path. To also cover pods
created outside that path, such as the Ray job submitter pod, taint your spot nodes and give the
matching toleration only to interruptible tasks.

Taint each spot node:

```bash
kubectl taint nodes <node-name> union.ai/capacity-type=interruptible:NoSchedule
```

Provisioning tools and node pool configuration can usually apply this taint automatically.

Then add the matching toleration for interruptible tasks in your values file:

```yaml
config:
  k8s:
    plugins:
      k8s:
        interruptible-tolerations:
          - effect: NoSchedule
            key: union.ai/capacity-type
            operator: Equal
            value: interruptible
```

Apply the taint and the toleration together. If you taint your spot nodes without setting
`interruptible-tolerations`, interruptible tasks can no longer schedule onto spot at all, because
nothing tolerates the taint.

## On-demand capacity

Once non-interruptible tasks are pinned to on-demand nodes, confirm that your on-demand node pool can
scale to cover all of your non-interruptible work. Any task that is not marked interruptible needs
on-demand capacity to run.
