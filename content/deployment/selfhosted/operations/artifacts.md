---
title: Artifacts
weight: 4
variants: -flyte +union
---

# Artifacts

Artifacts let tasks publish and consume **versioned, named** outputs — models, datasets, feature tables — with lineage back to the run that produced them, and let runs be **triggered** when a new version of an artifact appears. For how to use them, see [Artifacts](../../../user-guide/artifacts/_index) in the user guide.

On a {{< key product_name >}} self-hosted deployment the Artifacts service is **enabled by default** and needs nothing provisioned: no dedicated bucket, no object-store credentials, no workload-identity binding.

## How it stores data

The Artifacts service is a **metadata layer** backed by the control plane's existing database. An artifact is a named, versioned **pointer** to data that already lives in your data bucket, plus metadata: partitions, source run, and cards (stored as URI references). The artifact bytes stay in the **same data bucket** used for task outputs and offloaded metadata. The service itself does no object-store I/O. It only needs the shared control-plane database, where it creates its own `artifacts_v2` tables on first start.

## Disabling Artifacts

A single value, `services.artifacts.enabled` (default `true`), controls the Artifacts pod, the v2 `ArtifactService` ingress route, the **Artifacts** console nav, and replication of run-produced artifacts. To turn Artifacts off for an environment, set it to `false` in your `values.yaml` overrides:

```yaml
services:
  artifacts:
    enabled: false
```

## Verify

After the control-plane chart rolls out:

1. The `artifacts` pod is `Running` and its `migrate` init container completed:

   ```bash
   kubectl -n <control-plane-namespace> get pods -l app.kubernetes.io/name=artifacts
   ```

2. The **Artifacts** tab appears in the console left navigation.
3. Run a task that returns an artifact and confirm it appears in the console with its source-run lineage (see [Task outputs as artifacts](../../../user-guide/artifacts/task-outputs)). The task needs `produces_artifacts=True`, and its return value (a `flyte.io.File`, `flyte.io.Dir`, or `flyte.io.DataFrame`) must be wrapped with `flyte.artifacts.new()`:

   ```python
   @env.task(produces_artifacts=True)
   async def publish() -> File:
       f = await File.from_local("model.pt")
       return artifacts.new(f, artifacts.Metadata(name="smoke-test"))
   ```

> [!NOTE]
> Artifacts are registered only while the service is enabled. If the Artifacts pod is temporarily unavailable, registration is retried until it succeeds. Runs that complete while `services.artifacts.enabled` is `false` are not registered after you turn it back on.
