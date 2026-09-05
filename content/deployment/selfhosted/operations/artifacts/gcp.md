---
title: Artifacts on GCP
weight: 2
variants: -flyte +union
---

# Artifacts on GCP

Concrete example of the [generalized Artifacts setup](./_index) on GCP: a dedicated GCS bucket, a lenient lifecycle policy, and a Workload Identity service account bound to the Artifacts pod.

> [!NOTE]
> Binding a Google service account via Workload Identity is **one option** for granting the pod bucket access. The chart does not impose a service-account annotation; you set `services.artifacts.serviceAccount.annotations` directly.

Replace the placeholders — `ARTIFACTS_BUCKET`, `PROJECT_ID`, `REGION`, `CP_NAMESPACE` — with your values.

## 1. Create the GCS bucket

```bash
gcloud storage buckets create gs://ARTIFACTS_BUCKET \
  --project=PROJECT_ID \
  --location=REGION \
  --uniform-bucket-level-access
```

Uniform bucket-level access keeps permissions on IAM (no per-object ACLs) — the Artifacts service reaches the bucket through Workload Identity.

## 2. Apply a lenient lifecycle policy

Artifacts are long-lived, so the bucket should have **no deletion rule**. At most, clean up abandoned multipart uploads:

```json
{
  "rule": [
    {
      "action": { "type": "AbortIncompleteMultipartUpload" },
      "condition": { "age": 7 }
    }
  ]
}
```

```bash
gcloud storage buckets update gs://ARTIFACTS_BUCKET --lifecycle-file=artifacts-lifecycle.json
```

> [!NOTE]
> Do not add a `Delete` action here. The metadata / offloaded-data bucket is where aggressive expiration belongs; the artifacts bucket is separate precisely so it can retain objects indefinitely.

## 3. Workload Identity service account

Create a Google service account, grant it object admin **on the bucket only**, and bind it to the Artifacts pod's Kubernetes service account:

```bash
# Service account the artifacts pod will impersonate
gcloud iam service-accounts create union-artifacts --project=PROJECT_ID

# Object read/write on the dedicated bucket only
gcloud storage buckets add-iam-policy-binding gs://ARTIFACTS_BUCKET \
  --member="serviceAccount:union-artifacts@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/storage.objectAdmin"

# Workload Identity binding to the control-plane 'artifacts' KSA
gcloud iam service-accounts add-iam-policy-binding \
  union-artifacts@PROJECT_ID.iam.gserviceaccount.com \
  --project=PROJECT_ID \
  --role="roles/iam.workloadIdentityUser" \
  --member="serviceAccount:PROJECT_ID.svc.id.goog[CP_NAMESPACE/artifacts]"
```

## 4. Values

The chart's `values.gcp.yaml` overlay selects the GCS (`stow` `google`) object-store backend and reads the shared `global.GOOGLE_PROJECT_ID`. Set the bucket and the Google service account as **dedicated keys on the artifacts service**, plus the enable toggle, in your environment overrides:

```yaml
services:
  artifacts:
    disabled: false
    serviceAccount:
      annotations:
        iam.gke.io/gcp-service-account: "union-artifacts@PROJECT_ID.iam.gserviceaccount.com"
    configMap:
      artifactsConfig:
        app:
          artifactBlobStoreConfig:
            container: "ARTIFACTS_BUCKET"
```

Return to the [generalized guide](./_index) for verification steps.
