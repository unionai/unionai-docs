---
title: Task routing
weight: 3
variants: -flyte +union
---

# Task routing

After installing a {{< key product_name >}} self-hosted deployment, the control plane still needs to be told **which data plane runs a given project's tasks**. Until that routing exists, a submitted run has no queue to land on, and control-plane bootstrap jobs that build images fail with `no enabled cluster in pool`.

This guide covers the queue model and the one-time steps to configure routing for each data plane. Perform them after the control plane and data plane are installed and healthy, and after the data plane has registered with the control plane.

## The queue model

Routing a task requires three constructs, created in order:

1. A **cluster pool** — carries the object store, secret store, and image registry contract that tasks in the pool use.
2. A **cluster** subscribed to that pool. Subscribing a cluster implicitly creates a **queue** of the same name.
3. A **`run.default_queue`** setting on each `(project, domain)` pair, pointing at a queue.

A run submitted for a `(project, domain)` resolves to its default queue, which resolves to the pool the queue is bound to, which resolves to an enabled, healthy cluster in that pool.

The simplest topology — and the recommended default — is **one pool, one cluster, one queue per data plane, all sharing the data plane's name.** You then point each project's `run.default_queue` at the data plane that should run its tasks.

> [!NOTE]
> Configuration is **create-only and additive.** At present there is no supported way to rename, delete, or repoint a cluster pool, cluster, or queue — draining is gated server-side. Choose data plane and pool names deliberately, and treat every step below as adding routing, never reconciling it. See [Changing existing routing](#changing-existing-routing) for the operational escape hatch when you must repoint an already-configured environment.

## Prerequisites

- The `flyte` CLI is installed (`pip install flyte` or `uv pip install flyte`) and authenticated against your control plane. In CI, set `FLYTE_API_KEY` — see [CI/CD integration](./cicd).
- The projects you intend to route already exist. The three base projects (`flytesnacks`, `system`, and `union-health-monitoring`) are always registered by the control plane. Register any additional project **before** routing it — routing an unregistered project fails.

## Step 1: Create a cluster pool

Describe the pool in a `cluster-pool.yaml`. `name` is the pool name (use the data plane's name); `config` binds the pool to the data plane's object store, secret store, and image registry.

{{< tabs >}}
{{< tab "AWS" >}}
{{< markdown >}}

```yaml
name: my-data-plane
config:
  object_store_ref:
    uri: s3://my-metadata-bucket
    endpoint: ""
  secret_store:
    type: AWS_SECRETS_MANAGER
    locator: us-east-2          # region
  image_registry:
    locator: <account>.dkr.ecr.us-east-2.amazonaws.com/my-images
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "GCP" >}}
{{< markdown >}}

```yaml
name: my-data-plane
config:
  object_store_ref:
    uri: gs://my-metadata-bucket
    endpoint: ""
  secret_store:
    type: GCP_SECRET_MANAGER
    locator: my-gcp-project     # control plane project ID
  image_registry:
    locator: us-central1-docker.pkg.dev/my-gcp-project/my-images
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

Create the pool:

```shell
flyte create cluster-pool my-data-plane --file cluster-pool.yaml
```

## Step 2: Create a cluster

Subscribe a cluster to the pool. Use the same name for the cluster, the pool, and the resulting queue so routing is easy to reason about. Subscribing the cluster implicitly creates a queue of that name.

```shell
flyte create cluster my-data-plane --pool my-data-plane
```

## Step 3: Route projects to a queue

Set `run.default_queue` for each `(project, domain)` pair. Put the target queue in a settings file and apply it per project and domain:

```shell
cat > settings.yaml <<'EOF'
run.default_queue: my-data-plane
EOF

flyte edit settings --project flytesnacks --domain development --from-file settings.yaml
```

Repeat for every project and domain you want to route. A common baseline is to route the three base projects (`flytesnacks`, `system`, `union-health-monitoring`) across all three domains (`development`, `staging`, `production`) to your first data plane — that is enough for image-build bootstrap and end-to-end tests to run. Route additional projects to whichever data plane should run their tasks.

Once routing is in place, submit a run and confirm it lands on the expected cluster.

## Changing existing routing

A cluster's pool binding and a queue's pool binding are **immutable through the API**. This is deliberate: it prevents work from being silently re-routed out from under running executions. Because configuration is create-only for the same reason, you cannot repoint an existing binding by re-running the steps above.

You will hit this only on an environment that already accumulated a *different* pool topology — for example, a cluster or queue previously subscribed to a differently-named pool. The symptoms are:

- On `flyte create cluster <name> --pool <name>`:
  `cannot change cluster pool from "<old-pool>" to "<new-pool>"`.
- On task routing or test runs:
  `no enabled, healthy cluster in pool "<old-pool>"` — the queue still points at the old pool, which is now empty because the cluster moved.

A fresh environment never hits this.

### Repoint the bindings in the control-plane database

Until a day-2 update command is available, repoint the bindings directly in the control-plane Postgres database. This bypasses the immutability guard on purpose — only do it on an environment you own, and only for clusters and queues with no in-flight work.

The control-plane database is typically a private-network managed Postgres instance, so run a throwaway `psql` client **inside the cluster**. The connection host, database name, and user come from any control-plane pod that talks to the database (its mounted `config.yaml`); the password comes from the mounted database-password secret.

```shell
NS=<controlplane-namespace>

kubectl -n "$NS" run pgclient --rm -i --restart=Never \
  --image=postgres:16 \
  --env="PGPASSWORD=$(kubectl -n "$NS" exec deploy/cluster -- cat /etc/db/pass.txt)" \
  --command -- psql -h "<DB_HOST>" -U "<DB_USER>" -d "<DB_NAME>"
```

1. **Inspect** the current bindings (replace `<org>` with your organization / tenant):

   ```sql
   SELECT organization, name, cluster_pool_name, state, health
     FROM clusters WHERE organization = '<org>' ORDER BY name;
   SELECT organization, name, cluster_pool_name
     FROM queues   WHERE organization = '<org>' ORDER BY name;
   ```

2. **Unpin the clusters.** Setting the existing pool to `NULL` skips the immutability check, so the next `flyte create cluster <name> --pool <name>` assigns the intended pool and runs its normal side effects:

   ```sql
   UPDATE clusters SET cluster_pool_name = NULL
     WHERE organization = '<org>' AND name IN ('<cluster-a>', '<cluster-b>');
   ```

3. **Repoint the queues** to the intended pool (each data plane's queue → its own pool):

   ```sql
   UPDATE queues SET cluster_pool_name = '<data-plane>'
     WHERE organization = '<org>' AND name = '<data-plane>';
   ```

4. **Flush the data proxy cache.** The data proxy caches the `(project, domain) → cluster pool` resolution for up to 30 minutes, so after fixing the database it keeps resolving the old (now-empty) pool until the cache expires. Restart it to re-resolve immediately:

   ```shell
   kubectl -n "$NS" rollout restart deploy/dataproxy
   ```

5. **Re-run** the configuration steps above. Pools, clusters, and queues that are already correct are tolerated; the previously failing create now succeeds.

Stale pools and queues from the old topology are left in place — they are harmless once nothing routes to them.
