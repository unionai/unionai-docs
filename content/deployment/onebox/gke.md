---
title: Deploy on Google GKE
description: Install onebox on Google Kubernetes Engine with a Cloud SQL for PostgreSQL database and a Cloud Storage bucket, using Workload Identity.
icon: google
weight: 3
variants: -flyte +union
---

# Deploy on Google GKE

This guide installs onebox on an existing GKE cluster, with a Cloud SQL for PostgreSQL database and a Cloud Storage bucket. Onebox and its task pods reach the bucket through Workload Identity, so no service account keys are stored in the cluster.

## Prerequisites

- A GKE cluster with Workload Identity enabled. Autopilot clusters have it; on a Standard cluster, enable it on the cluster and its node pools.
- `gcloud`, `kubectl` configured for the cluster, and [Helm](https://helm.sh) 3.

Set these for the commands below:

```shell
export PROJECT_ID=<project>
export REGION=<region>
export BUCKET=<globally unique bucket name>
export NAMESPACE=union
export GSA=onebox@${PROJECT_ID}.iam.gserviceaccount.com
```

## Create the database

Create a Cloud SQL for PostgreSQL instance with a **private IP** in the cluster's VPC network, so pods can reach it directly. Then create a database and a user:

```shell
gcloud sql databases create union --instance=<instance>
gcloud sql users create union --instance=<instance> --password='<password>'
```

Use the instance's private IP address as `database.host`. Onebox connects with TLS (`database.sslMode: require`).

## Create the bucket

```shell
gcloud storage buckets create gs://${BUCKET} --project ${PROJECT_ID} --location ${REGION} \
  --uniform-bucket-level-access
```

## Create the Google service account

Onebox and the task pods both need the bucket. Onebox runs as the `onebox` Kubernetes service account; task pods run as the namespace's `default` service account unless a task asks for another one. Map both to one Google service account:

```shell
gcloud iam service-accounts create onebox --project ${PROJECT_ID}

for ksa in onebox default; do
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

Let it sign URLs. The SDK uploads code and downloads outputs through signed URLs, and without a key file, onebox signs them with the IAM `signBlob` API:

```shell
gcloud iam service-accounts add-iam-policy-binding ${GSA} --project ${PROJECT_ID} \
  --member "serviceAccount:${GSA}" --role roles/iam.serviceAccountTokenCreator
```

## Install onebox

Create the namespace and the database password Secret, and map the task pods' service account:

```shell
kubectl create namespace ${NAMESPACE}
kubectl -n ${NAMESPACE} create secret generic onebox-db --from-literal=password='<password>'
kubectl -n ${NAMESPACE} annotate serviceaccount default iam.gke.io/gcp-service-account=${GSA}
```

Save this as `values.yaml`:

```yaml
database:
  host: <cloud-sql-private-ip>
  name: union
  user: union
  existingSecret: onebox-db
storage:
  type: gcs
  bucket: <bucket>
  gcpProjectId: <project>
serviceAccount:
  annotations:
    iam.gke.io/gcp-service-account: onebox@<project>.iam.gserviceaccount.com
```

Install the chart:

```shell
helm repo add unionai https://unionai.github.io/helm-charts
helm repo update
helm install onebox unionai/onebox -n ${NAMESPACE} -f values.yaml --wait --timeout 10m
```

Install onebox in a namespace of its own: task pods, their secrets, and the objects plugins create all live in it.

## Check it

```shell
kubectl -n ${NAMESPACE} port-forward svc/onebox 8080:80
```

Open [http://localhost:8080/v2](http://localhost:8080/v2), and run a workflow as in [Try onebox on k3d](./local-k3d#run-a-workflow).

Anyone who can reach port `80` can use onebox until you put an authenticating proxy in front of it. See [Authentication](./authentication#oauth2-proxy).

## Troubleshooting

| Symptom | Cause and fix |
|---|---|
| The onebox pod restarts with a timeout to the database | The pods can't reach the Cloud SQL private IP. Check that the instance has a private IP in the cluster's VPC network. |
| `403` from Cloud Storage in onebox's logs | The `onebox` service account isn't mapped to the Google service account. Check the annotation and the `workloadIdentityUser` binding for `[<namespace>/onebox]`. |
| `flyte run` fails while uploading the code bundle, and onebox logs `signBlob` permission errors | The Google service account can't sign URLs. Grant it `roles/iam.serviceAccountTokenCreator` on itself. |
| Tasks fail reading their inputs with `403` | The namespace's `default` service account isn't annotated, or isn't bound with `workloadIdentityUser`. |
