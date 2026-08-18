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
configuration**: the same object store, secret store, and container registry.
Because every cluster in a pool reads and writes the same data plane, a workload
can run on any healthy cluster in the pool and still find its inputs, code, and
secrets.

## When you need more than one pool

Most deployments need exactly one pool. Each cluster is assigned exactly one
pool, and if no custom pool is specified when the cluster is created, it joins
the `default` pool that every organization is provisioned with. If your clusters
share a bucket, secret store, and registry, leave them in `default` and move on
to [Clusters](./clusters).

Create additional pools when you have clusters with **distinct** data planes:
for example, separate development and production cloud accounts, each with its own
bucket, secrets vault, and registry. Each such environment becomes its own pool.

## Create a pool

A pool's config is the data plane contract its member clusters must satisfy:
object store, secret store, and image registry. The object store URI and secret
store type are required here; the image registry is optional to set, but member
clusters are still expected to match it — see
[How a pool's config is enforced](#how-a-pools-config-is-enforced) for how
that contract works.

{{< tabs "create-cluster-pool" >}}
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
    type: AWS_SECRETS_MANAGER
    locator: us-east-1
  image_registry:
    locator: 123456789012.dkr.ecr.us-east-1.amazonaws.com/union
```

{{< /markdown >}}
{{< /tab >}}
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

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

Supported `secret_store_type` values are `AWS_SECRETS_MANAGER`,
`GCP_SECRET_MANAGER`, `AZURE_KEY_VAULT`, `KUBERNETES`, `VAULT`, and
`OCI_VAULT`.

## How a pool's config is enforced

Pool config is **not** enforced at join time. Any cluster is allowed to join a
pool, and the check happens asynchronously afterwards:

1. A cluster joins the pool when its cluster record is created (see
   [Manage membership](#manage-membership)). The control plane accepts the
   membership without inspecting the cluster's actual data plane.
2. Once running, the cluster reports its real object store, secret store, and
   image registry to the control plane in periodic status updates.
3. The control plane compares each reported value against the pool's config. If
   they don't match, the cluster is marked **unhealthy**. An unhealthy cluster
   stops receiving new work from every queue that
   [routes](./queues#how-a-queue-routes) to it, until it recovers — the pool's
   other healthy clusters absorb the work.

Because the comparison rides on status reporting, a misconfigured cluster is
accepted first and only turns unhealthy a short time later. After registering a
cluster into a custom pool, check `flyte get cluster <name>` to confirm it
settles healthy rather than assuming the join succeeded.

Note that while the image registry is optional to *set*, it is still part of the
contract: a member cluster must report the same registry the pool declares — or
no registry at all, if the pool doesn't declare one — to stay healthy.

## Inspect pools

{{< tabs "inspect-cluster-pool" >}}
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
{{< /tabs >}}

`member_clusters` is derived from clusters that were registered into the pool.
Assign clusters when you register them; see [Clusters](./clusters).

## Update a pool

`flyte update cluster-pool` opens the pool in your `$EDITOR` as the same YAML
manifest used to create it. Save and close to apply.

{{< tabs "update-cluster-pool" >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte update cluster-pool prod
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
from flyteplugins.union.remote import ClusterPool

ClusterPool.update(
    "prod",
    object_store_uri="s3://my-prod-bucket/prefix",
    secret_store_type="AWS_SECRETS_MANAGER",
    secret_store_locator="us-east-1",
    image_registry="123456789012.dkr.ecr.us-east-1.amazonaws.com/union",
)
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

Editing the pool config changes the contract every member cluster is validated
against, so a change that no longer matches a member cluster will make that
cluster unhealthy on its next status report. This is also the fix for the
opposite case: when a cluster reports config the pool doesn't expect, correct
whichever side is wrong — the pool here, or the cluster in its own deployment.

## Manage membership

Cluster pool membership is normally set when clusters are registered:

{{< tabs "cluster-pool-membership" >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte create cluster prod-us-east-1 --pool prod
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
from flyteplugins.union.remote import Cluster

Cluster.create("prod-us-east-1", cluster_pool_name="prod")
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

You can also list clusters under `member_clusters` in the pool manifest to add
them to the pool. That route only adds: it cannot remove a cluster from a pool
or move one elsewhere.

An existing cluster can be reassigned to another pool with
`flyte update cluster <name> --pool <pool>`, but today the operation does not
stop in-flight work and carries real risk (a cluster-level drain that makes the
move safe is coming soon) — read
[Move a cluster to a different pool](./clusters#move-a-cluster-to-a-different-pool)
before running it.

## Delete a pool

A pool can be deleted only when it is **empty** — it contains no clusters and no
live queues; otherwise the request is rejected. (A queue that is itself
soft-deleted doesn't block the deletion, but it can only be restored once the
pool is.) Empty the pool first:

1. Delete the member [clusters](./clusters#delete-a-cluster). Deleting a cluster
   also deletes its [co-named queue](./clusters#the-co-named-queue), so the
   queues that came with the clusters go with them.
2. [Delete](./queues#delete-a-queue) any queue you created in the pool yourself.

The `default` pool follows the same rules: it can be deleted once emptied, which
additionally means [draining and deleting](./queues#delete-a-queue) the org-wide
`default` queue that lives in it — nothing is deleted on the pool's behalf.
While the `default` pool is deleted, registering a cluster without naming a pool
is rejected instead of falling back to it: name a pool explicitly, or undelete
`default` first.

{{< tabs "delete-cluster-pool" >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte delete cluster-pool prod
flyte delete cluster-pool prod --yes   # skip the confirmation prompt

# List deleted pools, restore one
flyte get cluster-pool --deleted
flyte undelete cluster-pool prod
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
from flyteplugins.union.remote import ClusterPool

ClusterPool.delete("prod")
ClusterPool.undelete("prod")   # restore a deleted pool
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

Deletion is a **soft delete**: the pool disappears from listings, but its name
stays reserved — creating a new pool under the same name is rejected — and it
can be restored with `flyte undelete cluster-pool <name>`.

## Next

With your pools defined, [register clusters](./clusters) into them, then
[create queues](./queues) to route workloads.
