---
title: GCP
weight: 2
variants: -flyte +union
---

# GCP infrastructure

This page walks you through creating the GCP resources needed for a Union data plane. If you already have these resources, skip to [Deploy the dataplane](../deploy/_index).

## Environment variables

Set these variables before running the commands below. Customize the names if you are deploying multiple data planes in the same GCP project.

```bash
export PROJECT_ID=my-project            # your GCP project ID
export REGION=us-central1               # GCP region for all resources
export CLUSTER_NAME=union-dataplane     # GKE cluster name
export BUCKET_PREFIX=union-dataplane    # prefix for GCS buckets (must be globally unique)
export AR_REPOSITORY=union-dataplane    # Artifact Registry repository name
export GSA_NAME=union-system            # Google Service Account name
```

## GKE cluster

You need a GKE cluster running one of the most recent three minor Kubernetes versions. See [Infrastructure recommendations](../infrastructure-recommendations/_index) for networking and node pool guidance.

If you don't already have a cluster, create one with `gcloud`:

First, enable the required APIs:

```bash
gcloud services enable container.googleapis.com --project ${PROJECT_ID}
```

> [!NOTE] If the project has no default VPC network, create one before proceeding:
>
> ```bash
> gcloud compute networks create default --project ${PROJECT_ID} --subnet-mode=auto
> ```

```bash
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

> [!NOTE] Plan `max-pods-per-node` before you scale
> The create command above uses GKE's default of 110 pods per node, which reserves a `/24`
> per node and caps a `/19` pod range at ~32 nodes. If you expect to scale, set
> `--max-pods-per-node 32` and size the pods secondary range accordingly — the cluster-wide
> value cannot be changed after creation. See [Networking and IP capacity](#networking-and-ip-capacity)
> below for the math.

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

## Networking and IP capacity

GKE **preallocates** a pod CIDR block per node sized by `max_pods_per_node`, so the pod
secondary range — not the node subnet — is what caps the cluster's node count. Size it
greedily up front: changing a nodepool's pod range forces nodepool recreation, and the
cluster-wide `max_pods_per_node` cannot be changed after cluster creation.

Suggested defaults for a production-scale data plane:

| Component | Setting |
| --- | --- |
| VPC subnet (nodes) | `/19` (8,192 IPs) per cluster |
| Pods secondary range | `/19` (8,192 IPs) — with `max_pods_per_node = 32` supports 128 nodes |
| Services secondary range | `/20` (4,096 IPs) |
| Cloud NAT | Dynamic Port Allocation enabled |

If you expect a single cluster to scale beyond a few hundred nodes, enlarge the pods secondary
range to `/14` (200,000 IPs) **up front**.

### Per-node CIDR math

Per [Google's published formula](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr),
each node's block is the smallest subnet that holds at least `2 × max_pods_per_node` IPs:

| `max_pods_per_node` (range) | Per-node block | IPs reserved |
| --- | --- | --- |
| 8 | /28 | 16 |
| 9–16 | /27 | 32 |
| 17–32 | /26 | 64 |
| 33–64 | /25 | 128 |
| 65–128 | /24 | 256 |
| 129–256 | /23 | 512 |

The Standard-cluster default of 110 falls in the 65–128 band, so every node consumes a `/24`
(256 IPs). The cluster-wide node ceiling is `pods_cidr_size / per_node_block`:

| Pod CIDR | `max_pods_per_node` | Node ceiling |
| --- | --- | --- |
| `/19` (8,192 IPs) | 110 (default) | **32 nodes** |
| `/19` (8,192 IPs) | 32 (recommended) | 128 nodes |
| `/16` (65,536 IPs) | 32 | 1,024 nodes |
| `/14` (262,144 IPs) | 32 | 4,096 nodes |

Setting `max_pods_per_node = 32` yields a 4× headroom improvement over the Standard default
while filling the `/26` block (no wasted IPs).

### Pool-aware tuning

`max_pods_per_node` is set per nodepool. Picking the smallest power-of-2 band that comfortably
fits each pool's realistic pod count maximizes total node count on a given pods CIDR:

| Pool | Realistic pod density | `max_pods_per_node` | Per-node block |
| --- | --- | --- | --- |
| System pool (operator, ingress-nginx, cert-manager, external-dns) | 10–20 fixed | **16** | /27 (32 IPs) |
| Worker pool (general task pods) | 5–20 typical, bursts to 30+ | **32** | /26 (64 IPs) |
| Dedicated monitoring (Prometheus) | 10–15 stable | **16** | /27 (32 IPs) |
| GPU pool (1–8 GPUs/node, typically 1 pod/node) | 1–4 | **8** | /28 (16 IPs) |

Set the cluster-wide `max_pods_per_node` to match the worker pool (the heaviest user), then
override per-nodepool for system / monitoring / GPU pools. Combined with a `/14` pods CIDR,
this lifts the practical node ceiling beyond what a single cluster-wide value can deliver.

For the full set of per-cluster scaling ceilings (vCPU quotas, image pull rate, conntrack,
etcd), see [Scaling constraints](../infrastructure-recommendations/scaling-constraints).

## GCS

Each data plane uses GCS buckets to store data used in workflow execution.
Union recommends the use of two buckets:

1. **Metadata bucket**: contains workflow execution data such as task inputs and outputs.
2. **Fast registration bucket**: contains local code artifacts copied into the Flyte task container at runtime when using `flyte deploy` or `flyte run --copy-style all`.

You can also choose to use a single bucket.

Create the buckets:

```bash
gcloud storage buckets create gs://${BUCKET_PREFIX}-metadata \
  --project ${PROJECT_ID} \
  --location ${REGION}

gcloud storage buckets create gs://${BUCKET_PREFIX}-fast-reg \
  --project ${PROJECT_ID} \
  --location ${REGION}
```

### CORS configuration

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

### Data retention

Union recommends using Lifecycle Policy on these buckets to manage storage costs. See [Data retention policy](../configuration/data-retention) for more information.

## Artifact Registry

Create an [Artifact Registry Docker repository](https://cloud.google.com/artifact-registry/docs/docker/store-docker-container-images#create) for Image Builder to push and pull container images:

```bash
gcloud artifacts repositories create ${AR_REPOSITORY} \
  --project ${PROJECT_ID} \
  --location ${REGION} \
  --repository-format docker \
  --description "Union Image Builder repository"
```

Note the repository path (`${REGION}-docker.pkg.dev/${PROJECT_ID}/${AR_REPOSITORY}`) -- you will reference it when configuring Workload Identity permissions below.

> [!NOTE] Node service account and image pulls
> Kubelet pulls task images using the **node's** service account, not the pod's Workload
> Identity binding. The default Compute Engine node SA can read Artifact Registry in the same
> project. If you configure the node pool with a **custom** service account, grant it
> `roles/artifactregistry.reader` on this repository or task pods fail `ErrImagePull` with
> `403 Forbidden` — even though the `union-system` GSA below has access.

## Workload Identity

Union recommends using [GKE Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to securely access GCP resources.

### 1. Create a Google service account

```bash
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

Once your infrastructure is ready, proceed to [Deploy the dataplane](../deploy/_index).

## Deploy configuration

When you [deploy the data plane](../deploy/_index), download the GCP values file and set the GCP-specific keys below. The shared `global` keys (`UNION_CONTROL_PLANE_HOST`, `CLUSTER_NAME`, `ORG_NAME`) are covered in the deploy walkthrough.

```bash
curl -O https://raw.githubusercontent.com/unionai/helm-charts/main/charts/dataplane/values.gcp.yaml
```

Using the [environment variables](#environment-variables) from above, set the following keys under `global`. The rest of the file (storage, service account annotations, Workload Identity) is templated from these values, so you do not need to edit it:

- Set `global.GOOGLE_PROJECT_ID` to `${PROJECT_ID}`.
- Set `global.GCP_REGION` to `${REGION}`.
- Set `global.METADATA_BUCKET` to `${BUCKET_PREFIX}-metadata`.
- Set `global.FAST_REGISTRATION_BUCKET` to `${BUCKET_PREFIX}-fast-reg`.
- Set `global.BACKEND_IAM_ROLE_ARN` to `${GSA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com`.
- Set `global.WORKER_IAM_ROLE_ARN` to the same value (or a separate GSA if you use distinct worker permissions).
- Optionally set `imageBuilder.registryName` to `${AR_REPOSITORY}` (defaults to `union-dataplane`; the chart auto-generates the full Artifact Registry URL from the project ID and region).
