---
title: Multiple Clusters
weight: 3
variants: -flyte -serverless -byoc +selfmanaged
---

# Multiple Clusters

Union enables you to integrate multiple Kubernetes clusters into a single Union control plane using the `clusterPool` abstraction.

Currently, the clusterPool configuration is performed by Union in the control plane when you provide the mapping between clusterPool name and clusterNames using the following structure:

```yaml
clusterPoolname:
  - clusterName
```
With `clusterName` matching the name you used to install the Union operator Helm chart.

You can have as many cluster pools as needed:

**Example**

```yaml
default: # this is the clusterPool where executions will run, unless another mapping specified
  - my-dev-cluster
development-cp:
  - my-dev-cluster
staging-cp:
  - my-staging-cluster
production-cp:
  - production-cluster-1
  - production-cluster-2
dr-region:
  - dr-site-cluster
```

## Using cluster pools

Once the Union team configures the clusterPools in the control plane, you can proceed to configure mappings:

### project-domain-clusterPool mapping

1. Create a YAML file that includes the project, domain, and clusterPool:

**Example: cpa-dev.yaml**

```yaml
domain: development
project: flytesnacks
clusterPoolName: development-cp
```

2. Update the control plane with this mapping:

```bash
uctl update cluster-pool-attributes --attrFile cpa-dev.yaml
```
3. New executions in `flytesnacks-development` should now run in the `my-dev-cluster`

### project-domain-workflow-clusterPool mapping

1. Create a YAML file that includes the project, domain, and clusterPool:

**Example: cpa-dev.yaml**

```yaml
domain: production
project: flytesnacks
workflow: my_critical_wf
clusterPoolName: production-cp
```

2. Update the control plane with this mapping:

```bash
uctl update cluster-pool-attributes --attrFile cpa-prod.yaml
```
3. New executions of the `my_critical_wf` workflow in `flytesnacks-production` should now run in any of the clusters under `production-cp`

## Data sharing between cluster pools

The sharing of metadata is controlled by the cluster pool to which a cluster belongs. If two clusters are in the same cluster pool, then they must share the same metadata bucket, defined in the Helm values as `storage.bucketName`.

If they are in different cluster pools, then they **must** have different metadata buckets. You could, for example, have a single metadata bucket for all your development clusters, and a separate one for all your production clusters, by grouping the clusters into cluster pools accordingly.

 Alternatively you could have a separate metadata bucket for each cluster, by putting each cluster in its own cluster pool.