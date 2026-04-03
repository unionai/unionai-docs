---
title: Prepare infrastructure
weight: 1
variants: -flyte +union
---

# Prepare infrastructure

This page walks you through creating the GCP resources needed for a Union data plane. If you already have these resources, skip to [Deploy the dataplane](../selfmanaged-gcp/deploy-dataplane).

## GKE Cluster

You need a GKE cluster running one of the most recent three minor Kubernetes versions. See [Cluster Recommendations](../cluster-recommendations) for networking and node pool guidance.

If you don't already have a cluster, create one with `gcloud`:

First, enable the required APIs:

```bash
gcloud services enable container.googleapis.com --project ${PROJECT_ID}
```

> [!NOTE] If the project has no default VPC network, create one before proceeding:
> ```bash
> gcloud compute networks create default --project ${PROJECT_ID} --subnet-mode=auto
> ```

```bash
export PROJECT_ID=my-project            # your GCP project ID
export REGION=us-central1
export CLUSTER_NAME=union-dataplane

gcloud container clusters create ${CLUSTER_NAME} \
  --project ${PROJECT_ID} \
  --region ${REGION} \
  --release-channel regular \
  --machine-type e2-standard-4 \
  --num-nodes 1 \
  --workload-pool ${PROJECT_ID}.svc.id.goog
```

> [!NOTE] The `--workload-pool` flag enables [GKE Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity), which is required for the [Workload Identity](#workload-identity) setup below.

The following GKE add-ons are required and come pre-installed on GKE clusters:
  - CoreDNS (kube-dns)
  - GKE networking (Dataplane V2 / Calico)
  - Kube-proxy

If you created your cluster through other means, verify that Workload Identity is enabled:

```bash
gcloud container clusters describe ${CLUSTER_NAME} \
  --region ${REGION} \
  --project ${PROJECT_ID} \
  --format="value(workloadIdentityConfig.workloadPool)"
```

Union supports Autoscaling and the use of preemptible (spot) instances.

### BuildKit node pool

Image Builder (BuildKit) requires 4 CPUs and 50Gi ephemeral storage, which can exceed what's allocatable on a standard `e2-standard-4` node when other pods are running. Add a dedicated node pool with a larger machine type and boot disk:

```bash
gcloud container node-pools create buildkit-pool \
  --cluster ${CLUSTER_NAME} \
  --region ${REGION} \
  --project ${PROJECT_ID} \
  --machine-type e2-standard-8 \
  --disk-size 200GB \
  --num-nodes 0 \
  --enable-autoscaling \
  --min-nodes 0 \
  --max-nodes 2
```

## GCS

Each data plane uses GCS buckets to store data used in workflow execution.
Union recommends the use of two buckets:

1. **Metadata bucket**: contains workflow execution data such as task inputs and outputs.
2. **Fast registration bucket**: contains local code artifacts copied into the Flyte task container at runtime when using `union register` or `union run --remote --copy-all`.

You can also choose to use a single bucket.

Create the buckets:

```bash
export BUCKET_PREFIX=union-dataplane   # choose a globally unique prefix

gcloud storage buckets create gs://${BUCKET_PREFIX}-metadata \
  --project ${PROJECT_ID} \
  --location ${REGION}

gcloud storage buckets create gs://${BUCKET_PREFIX}-fast-reg \
  --project ${PROJECT_ID} \
  --location ${REGION}
```

### CORS Configuration

To enable the [Code Viewer](../configuration/code-viewer) in the Union UI, configure a CORS policy on your buckets. This allows the UI to securely fetch code bundles directly from GCS.

Save the following as `cors.json`:

```json
[
    {
        "origin": ["https://*.unionai.cloud"],
        "method": ["HEAD", "GET"],
        "responseHeader": ["ETag"],
        "maxAgeSeconds": 3600
    }
]
```

Apply it to both buckets:

```bash
gcloud storage buckets update gs://${BUCKET_PREFIX}-metadata --cors-file=cors.json
gcloud storage buckets update gs://${BUCKET_PREFIX}-fast-reg --cors-file=cors.json
```

### Data Retention

Union recommends using Lifecycle Policy on these buckets to manage storage costs. See [Data retention policy](../configuration/data-retention) for more information.

## Artifact Registry

Create an [Artifact Registry Docker repository](https://cloud.google.com/artifact-registry/docs/docker/store-docker-container-images#create) for Image Builder to push and pull container images:

```bash
export AR_REPOSITORY=union-dataplane

gcloud artifacts repositories create ${AR_REPOSITORY} \
  --project ${PROJECT_ID} \
  --location ${REGION} \
  --repository-format docker \
  --description "Union Image Builder repository"
```

Note the repository path (`${REGION}-docker.pkg.dev/${PROJECT_ID}/${AR_REPOSITORY}`) -- you will reference it when configuring Workload Identity permissions below.

## Workload Identity

Union recommends using [GKE Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to securely access GCP resources.

### 1. Create a Google Service Account

```bash
export GSA_NAME=union-system

gcloud iam service-accounts create ${GSA_NAME} \
  --project ${PROJECT_ID} \
  --display-name "Union data plane service account"
```

### 2. Bind the GSA to the Kubernetes service account

Bind both the `union-system` and `union` Kubernetes service accounts in the `union` namespace to impersonate the Google Service Account:

```bash
gcloud iam service-accounts add-iam-policy-binding \
  ${GSA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com \
  --project ${PROJECT_ID} \
  --role roles/iam.workloadIdentityUser \
  --member "serviceAccount:${PROJECT_ID}.svc.id.goog[union/union-system]"

gcloud iam service-accounts add-iam-policy-binding \
  ${GSA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com \
  --project ${PROJECT_ID} \
  --role roles/iam.workloadIdentityUser \
  --member "serviceAccount:${PROJECT_ID}.svc.id.goog[union/union]"
```

> [!NOTE] Why bind both `union/union-system` and `union/union`?
> Union platform services run under `union-system`, while task pods in the `union` namespace run under the `union` service account. Both need Workload Identity access to GCS.

### 3. Grant GCS access

```bash
gcloud projects add-iam-policy-binding ${PROJECT_ID} \
  --member "serviceAccount:${GSA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role roles/storage.objectAdmin \
  --condition="expression=resource.name.startsWith('projects/_/buckets/${BUCKET_PREFIX}'),title=union-bucket-access"
```

Alternatively, grant the role on each bucket directly:

```bash
gcloud storage buckets add-iam-policy-binding gs://${BUCKET_PREFIX}-metadata \
  --member "serviceAccount:${GSA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role roles/storage.objectAdmin

gcloud storage buckets add-iam-policy-binding gs://${BUCKET_PREFIX}-fast-reg \
  --member "serviceAccount:${GSA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role roles/storage.objectAdmin
```

Also grant `legacyBucketReader` on each bucket. This is required for `storage.buckets.get` access, which the operator needs to verify the bucket exists at startup:

```bash
gcloud storage buckets add-iam-policy-binding gs://${BUCKET_PREFIX}-metadata \
  --member "serviceAccount:${GSA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role roles/storage.legacyBucketReader

gcloud storage buckets add-iam-policy-binding gs://${BUCKET_PREFIX}-fast-reg \
  --member "serviceAccount:${GSA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role roles/storage.legacyBucketReader
```

### 4. Grant Artifact Registry access

```bash
gcloud artifacts repositories add-iam-policy-binding ${AR_REPOSITORY} \
  --project ${PROJECT_ID} \
  --location ${REGION} \
  --member "serviceAccount:${GSA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role roles/artifactregistry.writer
```

### 5. Grant token creator access

This role includes `iam.serviceAccounts.signBlob`, which is required for Image Builder authentication:

```bash
gcloud projects add-iam-policy-binding ${PROJECT_ID} \
  --member "serviceAccount:${GSA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role roles/iam.serviceAccountTokenCreator
```

> [!NOTE] If prompted to specify a condition, select **None**. This role applies project-wide and does not require a condition. The prompt appears because the policy already contains other conditional bindings.

Once your infrastructure is ready, proceed to [Deploy the dataplane](../selfmanaged-gcp/deploy-dataplane).
