---
title: Prepare infrastructure
weight: 1
variants: -flyte -byoc +selfmanaged
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

## Assumptions

* You have a {{< key product_name >}} organization, and you know the control plane URL for your organization (e.g. `https://your-org-name.us-east-2.unionai.cloud`).
* You have a cluster name provided by or coordinated with Union.
* You have a GKE cluster with Workload Identity enabled, running one of the most recent three minor Kubernetes versions.
  [Learn more](https://kubernetes.io/releases/version-skew-policy/)
* You have configured GCS bucket(s), Artifact Registry, and Workload Identity as described above.

## Prerequisites

* Install [Helm 3](https://helm.sh/docs/intro/install/).
* Install [uctl](../api-reference/uctl-cli/_index).

## Deploy the {{< key product_name >}} operator

1. Add the {{< key product_name >}} Helm repo:

   ```bash
   helm repo add unionai https://unionai.github.io/helm-charts/
   helm repo update
   ```

2. Use the `uctl selfserve provision-dataplane-resources` command to generate a new client and client secret for communicating with your Union control plane, provision authorization permissions for the app to operate on the Union cluster name you have selected, generate values file to install dataplane in your Kubernetes cluster and provide follow-up instructions:

   ```bash
   uctl config init --host=<YOUR_UNION_CONTROL_PLANE_URL>
   uctl selfserve provision-dataplane-resources --clusterName <YOUR_SELECTED_CLUSTERNAME>  --provider gcp
   ```

   * The command will output the ID, name, and a secret that will be used by the Union services to communicate with your control plane.
     It will also generate a YAML file specific to the provider that you specify, in this case `gcp`.

   * Save the secret that is displayed. Union does not store the credentials; rerunning the same command can be used to retrieve the secret later.

3. Update the generated values file with your infrastructure details:

   - Set `storage.bucketName` and `storage.fastRegistrationBucketName` to your GCS bucket name(s).
   - Set `storage.gcp.projectId` to your GCP project ID.
   - Replace all occurrences of `<GCP_SERVICE_ACCOUNT>` with the Google Service Account email created in the [Workload Identity](#workload-identity) section (e.g. `union-system@my-project.iam.gserviceaccount.com`). This appears in `additionalServiceAccountAnnotations`, `userRoleAnnotationValue`, and `fluentbit.serviceAccount.annotations`.
   - Annotate the `union-system` Kubernetes service account with the Google Service Account email so that Workload Identity is active for Union platform pods:

     ```yaml
     commonServiceAccount:
       annotations:
         iam.gke.io/gcp-service-account: "union-system@<PROJECT_ID>.iam.gserviceaccount.com"
     ```

4. Optionally configure the resource `limits` and `requests` for the different services.
   By default, these will be set minimally, will vary depending on usage, and follow the Kubernetes `ResourceRequirements` specification.

   * `operator.resources`
   * `executor.resources`
   * `proxy.resources`
   * `flytepropellerwebhook.resources`

5. Install the data plane Helm chart:

   ```bash
   helm upgrade --install union unionai/dataplane \
     -f <GENERATED_VALUES_FILE> \
     --namespace union \
     --create-namespace
   ```

6. Create an API key for your organization. This is required for v2 workflow executions on the data plane. If you have already created one, rerun the same command to propagate the key to the new cluster:

   ```bash
   uctl create apikey --keyName EAGER_API_KEY --org <YOUR_ORG_NAME>
   ```

7. Once deployed you can check to see if the cluster has been successfully registered to the control plane:

   ```bash
   uctl get cluster
    ----------- ------- --------------- -----------
   | NAME      | ORG   | STATE         | HEALTH    |
    ----------- ------- --------------- -----------
   | <cluster> | <org> | STATE_ENABLED | HEALTHY   |
    ----------- ------- --------------- -----------
   1 rows
   ```

8. You can then register and run some example workflows through your cluster to ensure that it is working correctly.

   ```bash
   uctl register examples --project=union-health-monitoring --domain=development
   uctl validate snacks --project=union-health-monitoring --domain=development
    ---------------------- ----------------------------------- ---------- -------------------------------- -------------- ----------- ---------------
   | NAME                 | LAUNCH PLAN NAME                  | VERSION  | STARTED AT                     | ELAPSED TIME | RESULT    | ERROR MESSAGE |
    ---------------------- ----------------------------------- ---------- -------------------------------- -------------- ----------- ---------------
   | alskkhcd6wx5m6cqjlwm | basics.hello_world.hello_world_wf | v0.3.341 | 2025-05-09T18:30:02.968183352Z | 4.452440953s | SUCCEEDED |               |
    ---------------------- ----------------------------------- ---------- -------------------------------- -------------- ----------- ---------------
   1 rows
   ```
