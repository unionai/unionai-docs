---
title: Provision your GCP resources
description: Create the GKE cluster, Cloud Storage bucket, Artifact Registry repository, and service accounts that a GCP cluster pool needs.
icon: google
weight: 5
variants: -flyte +union
---

# Provision your GCP resources

Union.ai installs the data plane into your cluster for you, but the Google Cloud resources it runs on must exist first. This page creates them with the Google Cloud CLI:

- a regional GKE Standard cluster with private nodes, Cloud NAT for outbound traffic, Workload Identity, and node auto-provisioning
- one Cloud Storage bucket, the cluster pool's object store
- a private Artifact Registry Docker repository
- separate node, system, and task service accounts

You supply two values: your Google Cloud project ID and the address of your Union.ai UI. The commands derive every resource name from the project. At the end you have the values you enter when you connect your cluster: three for the cluster pool, and four for registering the cluster.

These resources differ from the ones in the manual [GCP infrastructure](../selfmanaged/infrastructure-recommendations/gcp) guide for self-managed deployments: here Google Cloud Secret Manager holds runtime secrets, and the agent you install from the Union.ai UI installs the data plane chart. Use this page only for a cluster you connect from the Union.ai UI.

> [!NOTE] Already have these resources?
> This page is optional. You can use an existing GKE cluster, bucket, repository, and service accounts instead, as long as they meet the same requirements:
>
> - The GKE cluster is a Standard cluster, not Autopilot, with Workload Identity enabled. Its nodes can reach the internet ([step 3](#3-create-the-private-network)), it can add nodes as the data plane needs them, and its nodes have boot disks of at least 200 GB ([step 6](#6-create-the-gke-cluster)).
> - The bucket is private, with the CORS rule from [step 4](#4-create-the-bucket-and-image-repository).
> - The Artifact Registry repository is a private Docker repository.
> - The service accounts have the roles from [step 5](#5-create-the-service-accounts-and-grant-access) and the Workload Identity binding from [step 7](#7-bind-the-cluster-to-the-service-accounts).
>
> Then collect the values listed in [step 8](#8-collect-the-values-for-connecting-your-cluster), and go on to [step 9](#9-connect-your-cluster).

## Prerequisites

- The [Google Cloud CLI](https://cloud.google.com/sdk/docs/install), `kubectl`, and `gke-gcloud-auth-plugin`. `kubectl` uses the plugin to authenticate to GKE, and fails without it. Install both with `gcloud components install kubectl gke-gcloud-auth-plugin`.
- A billing-enabled Google Cloud project, and an account that can enable APIs, create the resources below, and grant IAM roles in it. `roles/owner` covers all of it. Otherwise you need:

  | Role | For |
  |---|---|
  | `roles/serviceusage.serviceUsageAdmin` | Enabling the APIs |
  | `roles/compute.networkAdmin` | The VPC, subnet, Cloud Router, and Cloud NAT |
  | `roles/container.admin` | The GKE cluster |
  | `roles/storage.admin` | The bucket and its IAM |
  | `roles/artifactregistry.admin` | The repository and its IAM |
  | `roles/iam.serviceAccountAdmin` | The service accounts and their Workload Identity bindings |
  | `roles/iam.serviceAccountUser` | Creating the cluster with the node service account as its identity |
  | `roles/resourcemanager.projectIamAdmin` | The project-level roles the service accounts get |

- A Union.ai organization. See [Sign up for Union.ai](./sign-up).

The commands create billable resources, including a regional GKE control plane, its nodes, and Cloud NAT. They bill hourly whether or not anything runs. Use a project dedicated to the data plane: [step 5](#5-create-the-service-accounts-and-grant-access) grants Secret Manager roles on the whole project.

Run every step in the same shell session. Later steps use the variables that earlier steps export.

## 1. Set your project and names

Replace `<your-project-id>` with your project ID. Set `UNION_UI_ORIGIN` to the address of your Union.ai UI: copy the scheme and host from your browser's address bar while you are signed in, without a trailing slash, for example `https://acme.hosted.unionai.cloud`.

```bash
gcloud auth login
gcloud config set project <your-project-id>

export PROJECT_ID="$(gcloud config get-value project)"
export UNION_UI_ORIGIN="https://<your-org>.hosted.unionai.cloud"
export REGION="us-central1"
export CLUSTER_NAME="union-dataplane"
export BUCKET_NAME="$PROJECT_ID-$CLUSTER_NAME-data"
export NODE_SA="$CLUSTER_NAME-node@$PROJECT_ID.iam.gserviceaccount.com"
export SYSTEM_SA="$CLUSTER_NAME-system@$PROJECT_ID.iam.gserviceaccount.com"
export TASK_SA="$CLUSTER_NAME-task@$PROJECT_ID.iam.gserviceaccount.com"
export IMAGE_REGISTRY="$REGION-docker.pkg.dev/$PROJECT_ID/$CLUSTER_NAME"

gcloud auth list --filter=status:ACTIVE
gcloud config get-value project
```

Check that the active account and project are the ones you intend to use.

The defaults create one data plane per project. For a second data plane in the same project, change `CLUSTER_NAME`. It names the network, the cluster, the repository, and the service accounts, so it must be at most 23 characters of lowercase letters, digits, and hyphens, starting with a letter. Change `REGION` only if you need another region.

## 2. Enable the APIs

```bash
gcloud services enable \
  artifactregistry.googleapis.com \
  cloudresourcemanager.googleapis.com \
  compute.googleapis.com \
  container.googleapis.com \
  iam.googleapis.com \
  iamcredentials.googleapis.com \
  logging.googleapis.com \
  secretmanager.googleapis.com \
  storage.googleapis.com \
  --project="$PROJECT_ID"
```

If this fails with a `serviceusage.services.list` permission error, get permission to list and enable services in the project before you continue.

## 3. Create the private network

The cluster's nodes have private addresses only. Cloud NAT gives them outbound access to image registries and to Union.ai, and Private Google Access lets them reach Cloud Storage and Artifact Registry without going through NAT.

Choose ranges that do not conflict with networks you already have, and run:

```bash
gcloud compute networks create "$CLUSTER_NAME" \
  --subnet-mode=custom --project="$PROJECT_ID"

gcloud compute networks subnets create "$CLUSTER_NAME-private" \
  --network="$CLUSTER_NAME" --region="$REGION" \
  --range=10.232.0.0/19 \
  --secondary-range=pods=10.232.32.0/19,services=10.232.64.0/20 \
  --enable-private-ip-google-access --project="$PROJECT_ID"

gcloud compute routers create "$CLUSTER_NAME-router" \
  --network="$CLUSTER_NAME" --region="$REGION" --project="$PROJECT_ID"

gcloud compute routers nats create "$CLUSTER_NAME-nat" \
  --router="$CLUSTER_NAME-router" --region="$REGION" \
  --auto-allocate-nat-external-ips \
  --nat-custom-subnet-ip-ranges="$CLUSTER_NAME-private:ALL" \
  --enable-dynamic-port-allocation --min-ports-per-vm=32 \
  --project="$PROJECT_ID"
```

Check that this command succeeds:

```bash
gcloud compute routers nats describe "$CLUSTER_NAME-nat" \
  --router="$CLUSTER_NAME-router" --region="$REGION" --project="$PROJECT_ID"
```

To use a network you already have instead, it needs non-overlapping primary, Pod, and Service ranges, Private Google Access, and Cloud NAT. See the [Cloud NAT reference](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create).

## 4. Create the bucket and image repository

The bucket stores workflow metadata, task inputs and outputs, and fast-registration code bundles. It is the object store you enter in the cluster-pool form. Union.ai uses it for both metadata and fast registration, so you do not need a second bucket.

```bash
gcloud storage buckets create "gs://$BUCKET_NAME" \
  --location="$REGION" --uniform-bucket-level-access \
  --public-access-prevention --project="$PROJECT_ID"

gcloud artifacts repositories create "$CLUSTER_NAME" \
  --repository-format=docker --location="$REGION" \
  --project="$PROJECT_ID"
```

Check that both of these succeed:

```bash
gcloud storage buckets describe "gs://$BUCKET_NAME"
gcloud artifacts repositories describe "$CLUSTER_NAME" \
  --location="$REGION" --project="$PROJECT_ID"
```

Add a CORS rule to the bucket. The Union.ai UI downloads code and artifacts straight from the bucket with presigned URLs, and the browser refuses them without a rule that names the UI's origin. Without the rule, the UI reports that code download is blocked by your storage bucket's configuration.

```bash
printf '[{"origin":["%s"],"method":["GET","PUT","POST","DELETE","HEAD"],"responseHeader":["*"],"maxAgeSeconds":3600}]\n' \
  "$UNION_UI_ORIGIN" > union-gcs-cors.json

gcloud storage buckets update "gs://$BUCKET_NAME" \
  --cors-file=union-gcs-cors.json
```

Cloud Storage matches an origin exactly. Unlike S3, it does not accept a wildcard subdomain such as `https://*.unionai.cloud`, so the rule must name the UI's exact origin. Do not use the `*` wildcard origin for production. See [Configure CORS](https://cloud.google.com/storage/docs/configuring-cors).

## 5. Create the service accounts and grant access

The three service accounts have separate jobs:

- The **node** service account is the identity of the cluster's nodes. It pulls images.
- The **system** service account is the identity of Union.ai's system pods. It reads and writes the bucket, manages runtime secrets, and reads task logs back for the Union.ai UI.
- The **task** service account is the identity of your task pods. It reads and writes the bucket, reads runtime secrets, and pushes the images Union.ai builds.

Create them, and grant access to the repository:

```bash
gcloud iam service-accounts create "$CLUSTER_NAME-node" --project="$PROJECT_ID"
gcloud iam service-accounts create "$CLUSTER_NAME-system" --project="$PROJECT_ID"
gcloud iam service-accounts create "$CLUSTER_NAME-task" --project="$PROJECT_ID"

for SA in "$NODE_SA" "$SYSTEM_SA"
do
  gcloud artifacts repositories add-iam-policy-binding "$CLUSTER_NAME" \
    --location="$REGION" --project="$PROJECT_ID" \
    --member="serviceAccount:$SA" --role=roles/artifactregistry.reader
done

gcloud artifacts repositories add-iam-policy-binding "$CLUSTER_NAME" \
  --location="$REGION" --project="$PROJECT_ID" \
  --member="serviceAccount:$TASK_SA" \
  --role=roles/artifactregistry.writer
```

Give the system and task service accounts access to the bucket, and permission to sign requests as themselves. Both sign the URLs that uploads and downloads use. `roles/storage.bucketViewer` is needed as well as `roles/storage.objectAdmin`, because the data plane reads the bucket's own metadata when it starts.

```bash
for SA in "$SYSTEM_SA" "$TASK_SA"
do
  for ROLE in roles/storage.objectAdmin roles/storage.bucketViewer
  do
    gcloud storage buckets add-iam-policy-binding "gs://$BUCKET_NAME" \
      --member="serviceAccount:$SA" --role="$ROLE"
  done

  gcloud iam service-accounts add-iam-policy-binding "$SA" \
    --member="serviceAccount:$SA" \
    --role=roles/iam.serviceAccountTokenCreator \
    --project="$PROJECT_ID"
done
```

Grant the project roles for logging, monitoring, and Secret Manager:

```bash
for ROLE in roles/logging.logWriter roles/monitoring.metricWriter \
  roles/monitoring.viewer roles/stackdriver.resourceMetadata.writer
do
  gcloud projects add-iam-policy-binding "$PROJECT_ID" \
    --member="serviceAccount:$NODE_SA" --role="$ROLE"
done

for ROLE in roles/logging.viewer roles/secretmanager.admin
do
  gcloud projects add-iam-policy-binding "$PROJECT_ID" \
    --member="serviceAccount:$SYSTEM_SA" --role="$ROLE"
done

for ROLE in roles/secretmanager.secretAccessor roles/secretmanager.viewer
do
  gcloud projects add-iam-policy-binding "$PROJECT_ID" \
    --member="serviceAccount:$TASK_SA" --role="$ROLE"
done
```

The system service account creates and manages runtime secrets, such as the `EAGER_API_KEY` secret the data plane creates for itself. Without Secret Manager access, pods can fail admission. The Secret Manager roles are granted on the project because a secret does not exist until the data plane creates it, so there is nothing narrower to grant them on. This is why the project should be dedicated to the data plane.

## 6. Create the GKE cluster

Use GKE Standard, not Autopilot: Union.ai's image builder runs privileged pods, which Autopilot does not allow.

The command creates a small, autoscaled base node pool, and turns on [node auto-provisioning](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning), so GKE creates more node pools when pending workloads need other machine types or more capacity. The base pool's maximum of 10 nodes applies to that pool only, not to the whole cluster.

Node auto-provisioning needs cluster-wide ceilings. This example sets 64 vCPUs and 256 GiB of memory across all node pools, the base pool included. They are maximums, not capacity that is provisioned or billed at setup. Raise them if your workloads need more, within your project's quotas.

All nodes get 200 GB boot disks. The image builder requests 50 GiB of ephemeral storage, and GKE reserves part of each boot disk, so on smaller disks image builds stay pending and never run.

The first command finds your current public IP address, and the cluster allows access to its Kubernetes API from that address only. If you use a VPN or a proxy, check that the address printed is the one `kubectl` connects from.

```bash
export ADMIN_CIDR="$(curl -fsS https://api.ipify.org)/32"
printf 'Allowing Kubernetes API access from %s\n' "$ADMIN_CIDR"

gcloud container clusters create "$CLUSTER_NAME" \
  --region="$REGION" --project="$PROJECT_ID" \
  --network="$CLUSTER_NAME" --subnetwork="$CLUSTER_NAME-private" \
  --enable-ip-alias \
  --cluster-secondary-range-name=pods \
  --services-secondary-range-name=services \
  --enable-private-nodes \
  --master-ipv4-cidr=172.16.0.0/28 \
  --enable-master-authorized-networks \
  --master-authorized-networks="$ADMIN_CIDR" \
  --workload-pool="$PROJECT_ID.svc.id.goog" \
  --workload-metadata=GKE_METADATA \
  --release-channel=stable \
  --addons=HttpLoadBalancing,HorizontalPodAutoscaling,GcsFuseCsiDriver \
  --logging=SYSTEM,WORKLOAD \
  --machine-type=e2-standard-4 \
  --disk-type=pd-balanced --disk-size=200 \
  --image-type=COS_CONTAINERD \
  --service-account="$NODE_SA" \
  --scopes=https://www.googleapis.com/auth/cloud-platform \
  --enable-shielded-nodes --shielded-secure-boot \
  --shielded-integrity-monitoring \
  --enable-autoscaling \
  --total-min-nodes=2 --total-max-nodes=10 \
  --location-policy=BALANCED --num-nodes=1 \
  --enable-autoprovisioning \
  --autoprovisioning-config-file=- \
  --quiet <<EOF
resourceLimits:
  - resourceType: cpu
    maximum: 64
  - resourceType: memory
    maximum: 256
serviceAccount: $NODE_SA
scopes:
  - https://www.googleapis.com/auth/cloud-platform
diskSizeGb: 200
diskType: pd-balanced
management:
  autoRepair: true
  autoUpgrade: true
EOF
```

The node auto-provisioning configuration is read from standard input, so no file is created. Because `EOF` is unquoted, the shell fills in `$NODE_SA`. If `172.16.0.0/28` conflicts with your network, use another unused `/28` range. See the [cluster creation reference](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create).

Configure `kubectl` and check the cluster:

```bash
gcloud container clusters get-credentials "$CLUSTER_NAME" \
  --region="$REGION" --project="$PROJECT_ID"

kubectl get nodes

gcloud container clusters describe "$CLUSTER_NAME" \
  --region="$REGION" --project="$PROJECT_ID" \
  --format='yaml(autoscaling)'
```

Check that the initial nodes become `Ready`, and that the cluster description shows node auto-provisioning with the CPU and memory ceilings. GKE creates more node pools only when pending pods need them. If `kubectl` cannot connect, check the authorized network address and your VPN or proxy.

This example provisions CPU capacity only. To run GPU tasks, add GPU resource limits to the node auto-provisioning configuration, and check your GPU quota and driver requirements. See [Run GPUs in GKE Standard node pools](https://cloud.google.com/kubernetes-engine/docs/how-to/gpus).

## 7. Bind the cluster to the service accounts

Let workloads in the cluster use the system and task service accounts through Workload Identity, without static keys:

```bash
export PROJECT_NUMBER="$(gcloud projects describe "$PROJECT_ID" \
  --format='value(projectNumber)')"

export CLUSTER_PRINCIPAL="principalSet://iam.googleapis.com/projects/$PROJECT_NUMBER/locations/global/workloadIdentityPools/$PROJECT_ID.svc.id.goog/kubernetes.cluster/https://container.googleapis.com/v1/projects/$PROJECT_ID/locations/$REGION/clusters/$CLUSTER_NAME"

for SA in "$SYSTEM_SA" "$TASK_SA"
do
  gcloud iam service-accounts add-iam-policy-binding "$SA" \
    --member="$CLUSTER_PRINCIPAL" \
    --role=roles/iam.workloadIdentityUser \
    --project="$PROJECT_ID"
done
```

This binding covers the whole cluster, so the data plane works in whatever namespace you register it with. It also lets every workload in the cluster use both service accounts, which is right for a cluster dedicated to Union.ai.

If the cluster also runs other workloads, bind only Union.ai's Kubernetes service accounts instead. Choose the namespace you will enter when you register the cluster, and bind `serviceAccount:$PROJECT_ID.svc.id.goog[<namespace>/union-system]` and `serviceAccount:$PROJECT_ID.svc.id.goog[<namespace>/flytepropeller-system]` to the system service account, and `serviceAccount:$PROJECT_ID.svc.id.goog[<namespace>/union]` to the task service account. A pod in any other namespace then has no Google Cloud identity. See [Workload Identity Federation for GKE](https://cloud.google.com/kubernetes-engine/docs/concepts/workload-identity).

## 8. Collect the values for connecting your cluster

Print the values you enter in the Union.ai UI, labeled with the fields they go in:

```bash
printf '%s\n' \
  "Cluster pool form (GCP):" \
  "  GCS bucket                   = gs://$BUCKET_NAME" \
  "  Project ID                   = $PROJECT_ID" \
  "  Image registry               = $IMAGE_REGISTRY" \
  "Register cluster dialog:" \
  "  Project ID                   = $PROJECT_ID" \
  "  Region                       = $REGION" \
  "  System service account email = $SYSTEM_SA" \
  "  Task service account email   = $TASK_SA" \
  "kubeconfig command: gcloud container clusters get-credentials $CLUSTER_NAME --region $REGION --project $PROJECT_ID"
```

Keep this output, and keep the shell where `kubectl` can reach the cluster: you run the agent install from it.

## 9. Connect your cluster

1. In the Union.ai UI, select **Connect your cluster**, on the home page or in the sidebar. If your organization has no cluster pool yet, select **Create cluster pool**.
2. Select **GCP**, and fill in the form:

   | Field | Value |
   |---|---|
   | **GCS bucket** | The bucket URI, `gs://` followed by the bucket name, with no path after it |
   | **Project ID** | The project that holds Secret Manager. On this page it is the same project as the cluster's. |
   | **Image registry** | The repository address, in the form `<region>-docker.pkg.dev/<project-id>/<repository>` |

   Your first pool is always named `default`, so the **Pool name** field is already filled in. Select **Create cluster pool**.

3. When the pool is created, the dialog moves on to **Register a cluster**, with the new pool already selected. Fill in:

   | Field | Value |
   |---|---|
   | **Name** | A name for the cluster in Union.ai, for example `my-cluster`. You cannot change it once the cluster is registered. |
   | **Cluster pool** | Already set to the pool you just created. |
   | **Namespace** | Leave it empty to use `union`. The binding from [step 7](#7-bind-the-cluster-to-the-service-accounts) covers every namespace in the cluster. If you bound only specific service accounts instead, enter the namespace you bound them in. |
   | **Project ID** | The project the GKE cluster runs in |
   | **Region** | The cluster's region, for example `us-central1`, not a zone |
   | **System service account email** | The system service account's email |
   | **Task service account email** | The task service account's email |

4. Select **Register cluster**. The cluster's page, **Install Union on your GCP cluster**, shows the install command for this cluster.

Install the agent and wait for the data plane as described in steps 3 and 4 of [Connect your cluster](./connect-a-cluster#3-install-the-agent).

## Important behavior and cleanup

- The pool uses one bucket for both metadata and fast registration. Do not create or configure a second bucket.
- The Workload Identity binding from step 7 covers the whole cluster. Keep the cluster dedicated to Union.ai, or bind only Union.ai's service accounts.
- The Secret Manager roles cover the whole project. Keep the project dedicated to the data plane.
- This guide does not set data-retention or image-cleanup policies. Add Cloud Storage and Artifact Registry lifecycle rules before production use.
- To remove the environment, delete the GKE cluster, the bucket and its contents, the Artifact Registry repository, the three service accounts with the project-level IAM bindings they hold, and the Cloud NAT, Cloud Router, subnet, and VPC. Review every target before deletion.

## Next steps

**[Run a workload on the cluster](./connect-a-cluster#5-run-a-workload-on-the-cluster).** Once the cluster shows as **Healthy**, run a workflow on it.
