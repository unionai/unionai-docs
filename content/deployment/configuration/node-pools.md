---
title: Node Pools
weight: 1
variants: -flyte -serverless -byoc +selfmanaged
---

# Configuring Service and Worker Node Pools

As a best practice, we recommend using separate node pools for the Union services and the Union worker pods. This allows
you to guard against resource contention between Union services and other tasks running in your cluster.

Start by creating two node pools in your cluster. One for the Union services and one for the Union worker pods.
Configure the node pool for the Union services with the `union.ai/node-role: services` label.  The worker pool will
be configured with the `union.ai/node-role: worker` label.  You will also need to taint the nodes in the service and
worker pools to ensure that only the appropriate pods are scheduled on them.

The nodes for Union services should be tainted with:

```shell
kubectl taint nodes <node-name> union.ai/node-role=services:NoSchedule
```
The nodes for execution workers should be tainted with:

```shell
kubectl taint nodes <node-name> union.ai/node-role=worker:NoSchedule
```

Vendor interfaces and provisioning tools may support tainting nodes automatically through configuration options.

Set the scheduling constraints for the Union services in your values file:

```yaml
scheduling:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: union.ai/node-role
            operator: In
            values:
            - services
  tolerations:
    - effect: NoSchedule
      key: union.ai/node-role
      operator: Equal
      value: services
```

To ensure that your worker processes are scheduled on the worker node pool, set the following for the Flyte kubernetes plugin:

```yaml
config:
  k8s:
    plugins:
      k8s:
        default-affinity:
          nodeAffinity:
            requiredDuringSchedulingIgnoredDuringExecution:
              nodeSelectorTerms:
              - matchExpressions:
                - key: union.ai/node-role
                  operator: In
                  values:
                  - worker
        default-tolerations:
          - effect: NoSchedule
            key: union.ai/node-role
            operator: Equal
            value: worker
```
