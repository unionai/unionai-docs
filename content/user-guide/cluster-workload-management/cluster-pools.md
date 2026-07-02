---
title: Cluster pools
weight: 1
variants: -flyte +union
---

# Cluster pools

> [!NOTE] Requires the `flyteplugins-union` plugin
> The cluster-pool CLI commands and Python objects on this page are provided by
> the `flyteplugins-union` package. Install it with
> `pip install flyteplugins-union`.

A **cluster pool** is a named group of clusters that share one **data plane
configuration** — the same object store, secret store, and container registry.
Because every cluster in a pool reads and writes the same data plane, a workload
can run on any healthy cluster in the pool and still find its inputs, code, and
secrets.

## When you need more than one pool

Most deployments need exactly one pool. Every organization is provisioned with a
`default` pool, and clusters join it when no custom pool is specified. If your
clusters share a bucket, secret store, and registry, leave them in `default` and
move on to [Clusters](./clusters).

Create additional pools when you have clusters with **distinct** data planes —
for example, separate development and production cloud accounts, each with its own
bucket, secrets vault, and registry. Each such environment becomes its own pool.

## Create a pool

A pool is defined by its shared data plane contract: object store, secret store,
and optional image registry.

{{< tabs "create-cluster-pool" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}
```python
from flyteplugins.union.remote import ClusterPool

ClusterPool.create(
    "prod",
    object_store_uri="s3://my-prod-bucket/prefix",
    secret_store_type="AWS_SECRETS_MANAGER",
    secret_store_locator="us-east-1",
    image_registry="123456789012.dkr.ecr.us-east-1.amazonaws.com/union",
)
```

```
{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}
Create one interactively with an editor, or from a file:

```bash
# Open an editor pre-filled with a template
flyte create cluster-pool prod --edit

# ...or create from a manifest you've prepared
flyte create cluster-pool prod --file prod-pool.yaml
```

The manifest declares the shared data plane contract:

```yaml
name: prod
config:
  object_store_ref:
    uri: s3://my-prod-bucket/prefix
    endpoint: ""
  secret_store:
    type: AWS_SECRETS_MANAGER  # or KUBERNETES, GCP_SECRET_MANAGER, VAULT
    locator: us-east-1
  image_registry:
    locator: 123456789012.dkr.ecr.us-east-1.amazonaws.com/union
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

Supported `secret_store_type` values are `AWS_SECRETS_MANAGER`,
`GCP_SECRET_MANAGER`, `AZURE_KEY_VAULT`, `KUBERNETES`, `VAULT`, and
`OCI_VAULT`.

## Inspect pools

{{< tabs "inspect-cluster-pool" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}
```python
from flyteplugins.union.remote import ClusterPool

for pool in ClusterPool.listall(limit=100):
    print(pool.name, pool.member_clusters, pool.object_store_uri, pool.secret_store_type)

pool = ClusterPool.get("prod")
print(pool.name)
print(pool.member_clusters)
print(pool.object_store_uri)
print(pool.secret_store_type)
print(pool.image_registry)
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}
```bash
# List all pools
flyte get cluster-pool

# Inspect a specific pool — its config and member clusters
flyte get cluster-pool prod
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

`member_clusters` is derived from clusters that were registered into the pool.
Assign clusters when you register them; see [Clusters](./clusters).

## Manage membership

Cluster pool membership is set when clusters are registered:

{{< tabs "cluster-pool-membership" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}
```python
from flyteplugins.union.remote import Cluster

Cluster.create("prod-us-east-1", cluster_pool_name="prod")
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}
```bash
flyte create cluster prod-us-east-1 --pool prod
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

Existing clusters cannot be moved between pools in place. To change the pool for
a cluster, register a replacement cluster in the destination pool, move queues or
workload routing, and remove the old cluster record when it is no longer used.

## Delete a pool

The `default` pool cannot be deleted. A non-default pool can only be deleted after
all clusters and queues stop referencing it.

{{< tabs "delete-cluster-pool" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}
```python
from flyteplugins.union.remote import ClusterPool

ClusterPool.delete("prod")
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}
```bash
flyte delete cluster-pool prod
flyte delete cluster-pool prod --yes   # skip the confirmation prompt
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## Next

With your pools defined, [register clusters](./clusters) into them, then
[create queues](./queues) to route workloads.
