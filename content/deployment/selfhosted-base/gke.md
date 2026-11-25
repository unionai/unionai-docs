---
title: Deploy on Google GKE
description: Install Self-Hosted Base on Google Kubernetes Engine with a Cloud SQL for PostgreSQL database and a Cloud Storage bucket, using Workload Identity.
icon: google
weight: 3
variants: -flyte +union
---

# Deploy on Google GKE

This guide installs Self-Hosted Base on an existing GKE cluster, with a Cloud SQL for PostgreSQL database and a Cloud Storage bucket. Self-Hosted Base and its task pods reach the bucket through Workload Identity, so no service account keys are stored in the cluster.

## Prerequisites

- A GKE Standard cluster with Workload Identity enabled on the cluster and its node pools. Autopilot isn't supported: Self-Hosted Base's node agent (`selfhosted-base-node-agent`) needs privileged containers and `hostPath` mounts, which Autopilot refuses.
- `gcloud`, `kubectl` configured for the cluster, and [Helm](https://helm.sh) 3.

Set these for the commands below:

```shell
export PROJECT_ID=<project>
export REGION=<region>
export BUCKET=<globally unique bucket name>
export NAMESPACE=union
export GSA=selfhosted-base@${PROJECT_ID}.iam.gserviceaccount.com
```

## Create the database

Create a Cloud SQL for PostgreSQL instance with a **private IP** in the cluster's VPC network, so pods can reach it directly. Then create a database and a user:

```shell
gcloud sql databases create union --instance=<instance>
gcloud sql users create union --instance=<instance> --password='<password>'
```

Use the instance's private IP address as `database.host`. Self-Hosted Base connects with TLS (`database.sslMode: require`).

For thousands of tasks at once, give the instance a `max_connections` of at least 300. Cloud SQL's default limit depends on the instance's memory and is lower on small instances; set it with the `max_connections` database flag. See [Sizing](./_index#sizing).

## Create the bucket

```shell
gcloud storage buckets create gs://${BUCKET} --project ${PROJECT_ID} --location ${REGION} \
  --uniform-bucket-level-access
```

Let the UI read objects from it (see [Bucket CORS](./_index#bucket-cors)), with the address your users open:

```shell
cat > cors.json <<EOF
[{"origin": ["https://<host>"], "method": ["GET", "HEAD"], "responseHeader": ["*"], "maxAgeSeconds": 3600}]
EOF
gcloud storage buckets update gs://${BUCKET} --cors-file=cors.json
```

## Create the Google service account

Self-Hosted Base and the task pods both need the bucket. Self-Hosted Base runs as the `selfhosted-base` Kubernetes service account; task pods run as the namespace's `default` service account unless a task asks for another one. Map both to one Google service account:

```shell
gcloud iam service-accounts create selfhosted-base --project ${PROJECT_ID}

for ksa in selfhosted-base default; do
  gcloud iam service-accounts add-iam-policy-binding ${GSA} --project ${PROJECT_ID} \
    --role roles/iam.workloadIdentityUser \
    --member "serviceAccount:${PROJECT_ID}.svc.id.goog[${NAMESPACE}/${ksa}]"
done
```

Give it the bucket:

```shell
gcloud storage buckets add-iam-policy-binding gs://${BUCKET} \
  --member "serviceAccount:${GSA}" --role roles/storage.objectAdmin
gcloud storage buckets add-iam-policy-binding gs://${BUCKET} \
  --member "serviceAccount:${GSA}" --role roles/storage.legacyBucketReader
```

Let it sign URLs. The SDK uploads code and downloads outputs through signed URLs, and without a key file, Self-Hosted Base signs them with the IAM `signBlob` API:

```shell
gcloud iam service-accounts add-iam-policy-binding ${GSA} --project ${PROJECT_ID} \
  --member "serviceAccount:${GSA}" --role roles/iam.serviceAccountTokenCreator
```

## Install Self-Hosted Base

Create the namespace and the database password Secret, and map the task pods' service account:

```shell
kubectl create namespace ${NAMESPACE}
kubectl -n ${NAMESPACE} create secret generic selfhosted-base-db --from-literal=password='<password>'
kubectl -n ${NAMESPACE} annotate serviceaccount default iam.gke.io/gcp-service-account=${GSA}
```

Save this as `values.yaml`:

```yaml
database:
  host: <cloud-sql-private-ip>
  name: union
  user: union
  existingSecret: selfhosted-base-db
storage:
  type: gcs
  bucket: <bucket>
  gcpProjectId: <project>
serviceAccount:
  annotations:
    iam.gke.io/gcp-service-account: selfhosted-base@<project>.iam.gserviceaccount.com
```

Install the chart:

```shell
helm repo add unionai https://unionai.github.io/helm-charts
helm repo update
helm install selfhosted-base unionai/selfhosted-base -n ${NAMESPACE} -f values.yaml --wait --timeout 10m
```

Install Self-Hosted Base in a namespace of its own: task pods, their secrets, and the other Kubernetes objects created for tasks all live in it.

## Check it

```shell
kubectl -n ${NAMESPACE} port-forward svc/selfhosted-base 8080:80
```

Open [http://localhost:8080/v2](http://localhost:8080/v2), and run a workflow as in [Install the chart on k3d](./local-k3d#run-a-workflow).

Anyone who can reach port `80` can use Self-Hosted Base until you put an authenticating proxy in front of it. See [Authentication](./authentication#oauth2-proxy).

## Troubleshooting

| Symptom | Cause and fix |
|---|---|
| The Self-Hosted Base pod restarts with a timeout to the database | The pods can't reach the Cloud SQL private IP. Check that the instance has a private IP in the cluster's VPC network. |
| `403` from Cloud Storage in Self-Hosted Base's logs | The `selfhosted-base` service account isn't mapped to the Google service account. Check the annotation and the `workloadIdentityUser` binding for `[<namespace>/selfhosted-base]`. |
| `flyte run` fails while uploading the code bundle, and Self-Hosted Base logs `signBlob` permission errors | The Google service account can't sign URLs. Grant it `roles/iam.serviceAccountTokenCreator` on itself. |
| Tasks fail reading their inputs with `403` | The namespace's `default` service account isn't annotated, or isn't bound with `workloadIdentityUser`. |
| The Self-Hosted Base pod restarts with `OOMKilled` | Its memory limit is too small for the actions in flight; 2 GiB holds about 13,000. Raise `resources`; see [Sizing](./_index#sizing). Self-Hosted Base before 2026.11.14 needs about 1 GiB plus 1 MiB for each action queued or running. |
| Tasks stay queued while the cluster has room for them | Self-Hosted Base runs at most 500 tasks at once. Raise `extraConfig.leaseworker.capacity`; see [Sizing](./_index#sizing). |
