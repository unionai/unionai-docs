---
title: Artifacts
weight: 4
variants: -flyte +union
---

# Artifacts

Artifacts let tasks publish and consume **versioned, named** outputs — models, datasets, feature tables — with lineage back to the run that produced them, and let runs be **triggered** when a new version of an artifact appears.

On a {{< key product_name >}} self-hosted deployment the Artifacts service is **enabled by default**. It needs **no dedicated bucket** — artifact blobs reuse the existing data bucket, and the service itself holds no object-store credentials, so there is nothing to provision.

## No dedicated bucket required

The Artifacts service is a **metadata layer** backed by the control plane's existing database. An artifact is a named, versioned **pointer** to the literal a task already produced (plus metadata: partitions, source run, cards). The bytes stay at the producing task's output path — the **same data bucket** used for task outputs and offloaded metadata, not a separate artifacts bucket — and cards are stored as URI references. The service itself does no object-store I/O (pointers only), so it needs no bucket credentials or workload-identity binding of its own — just the shared control-plane database (it creates its own `artifacts_v2` tables on first start).

## Enabling and disabling

Artifacts is on by default (`services.artifacts.enabled: true`) — deploying the Artifacts pod, exposing the v2 `ArtifactService` route, enabling the **Artifacts** console nav, and turning on replication of run-produced artifacts, all from one value. To turn it off for an environment, set it false in your `values.yaml` overrides:

```yaml
services:
  artifacts:
    enabled: false
```

## Verify

After ArgoCD (or `helm upgrade`) rolls the change:

1. The `artifacts` pod is `Running` and its `migrate` init container completed:

   ```bash
   kubectl -n <control-plane-namespace> get pods -l app.kubernetes.io/name=artifacts
   ```

2. The **Artifacts** tab appears in the console left navigation.
3. Publish a test artifact from a task (`produces_artifacts=True` / `artifacts.new(...)`) and confirm it appears in the console with its source-run lineage.

> [!NOTE]
> If a run publishes an artifact **before** the Artifacts pod is `Running`, that version is not registered — re-run after the pod is healthy.
