---
title: Cluster pools
weight: 1
variants: -flyte +union
---

# Cluster pools

A **cluster pool** is a named group of clusters that share one **data-plane
configuration** — the same object store, secret store, and container registry.
Because every cluster in a pool reads and writes the same data plane, a workload
can run on any cluster in the pool and still find its inputs, code, and secrets.

## When you need more than one pool

Most deployments need exactly one pool. Every organization is provisioned with a
`default` pool, and every cluster joins it automatically. If your clusters share a
bucket, secret store, and registry, leave them in `default` and move on to
[Clusters](./clusters).

Create additional pools when you have clusters with **distinct** data planes —
for example, separate development and production cloud accounts, each with its own
bucket, secrets vault, and registry. Each such environment becomes its own pool.

## Create a pool

A pool is defined by a small YAML manifest. Create one interactively with an
editor, or from a file:

```bash
# Open an editor pre-filled with a template
flyte create cluster-pool prod --edit

# ...or create from a manifest you've prepared
flyte create cluster-pool prod --file prod-pool.yaml
```

The manifest declares the shared data-plane contract:

```yaml
name: prod
member_clusters: []          # clusters are added as they register into the pool
config:
  object_store_ref:
    uri: s3://my-prod-bucket/prefix
    endpoint: ""
  secret_store:
    type: AWS_SECRETS_MANAGER  # or KUBERNETES, GCP_SECRET_MANAGER, VAULT
    locator: ""
  image_registry:
    locator: ""
```

> [!WARNING] Pool configuration is immutable
> The data-plane `config` of a pool cannot be changed after it is created. This is
> deliberate: flipping the bucket or secret path under live workloads would leave
> in-flight runs unable to read data they already uploaded. To move to a different
> bucket, secrets vault, or registry, **create a new pool** and migrate clusters
> and queues to it.

## Inspect pools

```bash
# List all pools
flyte get cluster-pool

# Inspect a specific pool — its config and member clusters
flyte get cluster-pool prod
```

## Manage membership

A pool's configuration is fixed, but its **membership is dynamic**. Edit the
member cluster list interactively:

```bash
flyte update cluster-pool prod
```

This opens the pool in your `$EDITOR` so you can adjust `member_clusters`. (You can
also set a cluster's pool when you register it — see [Clusters](./clusters).)

## Delete a pool

```bash
flyte delete cluster-pool prod
flyte delete cluster-pool prod --yes   # skip the confirmation prompt
```

Move any clusters and queues off a pool before deleting it.

## Next

With your pools defined, [register clusters](./clusters) into them, then
[create queues](./queues) to route workloads.
