---
title: Artifacts
weight: 4
variants: -flyte +union
---

# Artifacts

Artifacts let tasks publish and consume **versioned, named** outputs — models, datasets, feature tables — with lineage back to the run that produced them, and let runs be **triggered** when a new version of an artifact appears.

On a {{< key product_name >}} self-hosted deployment the Artifacts service is **off by default** and is enabled per environment. It needs one new piece of infrastructure — a **dedicated object-store bucket** — plus a small set of Helm values. This guide covers the generalized setup; the cloud-specific bucket, lifecycle, and permission examples live in the sub-pages.

> [!NOTE]
> Enable Artifacts **after** the control plane is installed and healthy — see [Getting started](../../getting-started). Turning it on is additive: it deploys one pod and wires the console, with no change to existing services.

## Required infrastructure

Artifacts reuses the control plane's existing Postgres database (it creates its own `artifacts_v2` tables on first start — no new database is required). The only new substrate you provision is a bucket and the permission to reach it.

### Dedicated bucket

Provision a **separate** object-store bucket for Artifacts — do not reuse the metadata / offloaded-data bucket (`BUCKET_NAME`). The Artifacts service writes to it through the `ARTIFACTS_BUCKET_NAME` value.

A dedicated bucket exists so that artifacts can carry a **different retention lifecycle** from Flyte's offloaded task data. Offloaded inputs/outputs are short-lived and are typically expired aggressively to control cost; artifacts are long-lived, referenceable objects (a model you may promote or roll back to months later). Sharing one bucket would force a single lifecycle policy on both.

### Lenient lifecycle policy

Apply a **lenient** lifecycle policy to the artifacts bucket:

- **No object expiration** (or a long horizon that matches how long you retain models/datasets). An artifact whose backing object is deleted can no longer be materialized by a run.
- Keep noncurrent-version cleanup conservative if you enable bucket versioning — each artifact version references a specific object.
- It is safe (and recommended) to abort **incomplete multipart uploads** after a few days; that reclaims orphaned upload parts without touching committed artifacts.

The dedicated bucket is what makes this possible: you can keep an aggressive expiration policy on the data bucket while the artifacts bucket retains objects indefinitely.

### Artifacts service permissions

The Artifacts pod needs **read/write** access (object get, put, list, delete) scoped to the dedicated bucket, bound through the cloud's workload-identity mechanism (AWS IAM Roles for Service Accounts, or GCP Workload Identity) rather than long-lived node credentials. The `ARTIFACT_IAM_ROLE_ARN` value carries the role/service-account identity, which the chart annotates onto the Artifacts pod's Kubernetes service account.

See [Infrastructure requirements → Object storage](../../infrastructure-requirements) for the general object-store and workload-identity substrate this builds on.

## Enable Artifacts

Set the bucket and identity as **dedicated keys on the artifacts service** and flip the single toggle in your environment's `values.yaml` overrides:

```yaml
services:
  artifacts:
    disabled: false
    serviceAccount:
      annotations:
        # Cloud-specific identity annotation — the role/service account the
        # artifacts pod assumes to reach the bucket. See the cloud sub-pages:
        #   AWS: <pod-identity-prefix>/role-arn: "<irsa-role-arn>"
        #   GCP: iam.gke.io/gcp-service-account: "<service-account-email>"
    configMap:
      artifactsConfig:
        app:
          artifactBlobStoreConfig:
            # Dedicated bucket for artifacts — NOT the metadata/offloaded-data bucket.
            container: "my-union-artifacts"
```

`services.artifacts.disabled: false` is the **single switch** for the feature. It:

- deploys the Artifacts pod,
- exposes the v2 `ArtifactService` route on the control-plane ingress,
- enables the **Artifacts** navigation entry in the console, and
- turns on replication of run-produced artifacts into the service.

All four derive from this one value, so they cannot drift out of sync. The deprecated v1 artifact service is permanently disabled and is not configurable.

Layer the cloud-specific object-store backend and service-account wiring on top with the chart's `values.{aws,gcp}.yaml` overlay (already included in the standard install) — the per-cloud sub-pages below show exactly what those set.

## Cloud-specific setup

{{< grid >}}

{{< link-card target="./aws" icon="cloud" title="AWS" >}}
S3 bucket, lifecycle policy, and the IAM (IRSA) policy for the artifacts service
{{< /link-card >}}

{{< link-card target="./gcp" icon="cloud" title="GCP" >}}
GCS bucket, lifecycle policy, and the Workload Identity service account
{{< /link-card >}}

{{< /grid >}}

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
