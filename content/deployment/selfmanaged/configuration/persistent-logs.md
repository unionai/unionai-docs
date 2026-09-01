---
title: Persistent logs
description: How FluentBit collects container logs from every node and ships them for retention.
icon: journal-text
weight: 4
variants: -flyte +union
---

# Persistent logs

Persistent logging is enabled by default. The data plane deploys [FluentBit](https://fluentbit.io/) as a DaemonSet that collects container logs from every node and writes them to the `persisted-logs/` path in the object store configured for your data plane.

FluentBit runs under the `fluentbit-system` Kubernetes service account. This service account must have write access to the storage bucket so FluentBit can push logs. The sections below describe how to grant that access on each cloud provider.

> [!NOTE] **Azure works differently.** On AKS, persisted logs come from Azure Log Analytics and
> the chart ships with FluentBit disabled. See [Azure](#azure) below.

## AWS (IRSA)

On EKS, use [IAM Roles for Service Accounts (IRSA)](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) to grant the FluentBit service account permission to write to S3.

### 1. Create an IAM policy

Create an IAM policy that allows writing to your metadata S3 bucket:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:PutObjectAcl",
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::<BUCKET_NAME>",
        "arn:aws:s3:::<BUCKET_NAME>/persisted-logs/*"
      ]
    }
  ]
}
```

Replace `<BUCKET_NAME>` with the name of your data plane metadata bucket.

### 2. Create an IAM role with a trust policy

Create an IAM role that trusts the EKS OIDC provider and is scoped to the `fluentbit-system` service account:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::<ACCOUNT_ID>:oidc-provider/<OIDC_PROVIDER>"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "<OIDC_PROVIDER>:sub": "system:serviceaccount:<NAMESPACE>:fluentbit-system",
          "<OIDC_PROVIDER>:aud": "sts.amazonaws.com"
        }
      }
    }
  ]
}
```

Replace:

- `<ACCOUNT_ID>` with your AWS account ID
- `<OIDC_PROVIDER>` with your EKS cluster's OIDC provider (e.g. `oidc.eks.us-east-1.amazonaws.com/id/EXAMPLE`)
- `<NAMESPACE>` with the namespace where the data plane is installed (default: `union`)

You can retrieve the OIDC provider URL with:

```bash
aws eks describe-cluster --name <CLUSTER_NAME> --region <REGION> \
  --query "cluster.identity.oidc.issuer" --output text
```

Attach the IAM policy from step 1 to this role.

### 3. Configure the Helm values

Set the IRSA annotation on the FluentBit service account in your data plane Helm values:

```yaml
fluentbit:
  serviceAccount:
    annotations:
      eks.amazonaws.com/role-arn: "arn:aws:iam::<ACCOUNT_ID>:role/<FLUENTBIT_ROLE_NAME>"
```

## Azure

On Azure, persisted logs come from the AKS
[Container Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/containers/container-insights-overview)
add-on, which ships container logs into an Azure Log Analytics workspace that the Union operator
queries directly.

The data plane chart's `values.azure.yaml` therefore sets `fluentbit.enabled: false` from chart
version 2026.8.0; on earlier charts set it yourself. FluentBit's
`azure_blob` output cannot authenticate with Workload Identity, so a DaemonSet left enabled
without a shared key lands in `CrashLoopBackOff`.

### 1. Point the operator at the workspace

```yaml
config:
  proxy:
    persistedLogs:
      sourceType: AzureLogAnalytics
      azureLogAnalytics:
        logAnalyticsWorkspaceResourceIdTemplate: "/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<WORKSPACE_RESOURCE_GROUP>/providers/Microsoft.OperationalInsights/workspaces/<WORKSPACE_NAME>"
```

Nest this under `config.proxy`; a top-level `proxy:` block configures the proxy deployment
instead and leaves the workspace unchanged.

Find the workspace Container Insights is actually shipping to with:

```bash
az aks show --resource-group <RESOURCE_GROUP> --name <CLUSTER_NAME> \
  --query "addonProfiles.omsagent.config.logAnalyticsWorkspaceResourceID" --output tsv
```

It is frequently a shared workspace in a different resource group than the cluster.

### 2. Grant the backend identity Log Analytics Reader

The backend managed identity, the one annotated with `azure.workload.identity/client-id` in
`additionalServiceAccountAnnotations`, needs the **Log Analytics Reader** role on that workspace:

```bash
az role assignment create \
  --assignee-object-id <BACKEND_PRINCIPAL_ID> \
  --assignee-principal-type ServicePrincipal \
  --role "Log Analytics Reader" \
  --scope "/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<WORKSPACE_RESOURCE_GROUP>/providers/Microsoft.OperationalInsights/workspaces/<WORKSPACE_NAME>"
```

Without this role the pane stays empty and the operator logs an authorization error. The scope is
the workspace, so whoever administers the resource group that owns it may have to create the
assignment for you.

See [Persisted task logs](../selfmanaged-azure/prepare-infra#8-persisted-task-logs-log-analytics)
for the full Azure setup, including enabling Container Insights and verifying ingestion.

### Alternative: writing to Blob Storage

If you need logs in your own storage account rather than in Log Analytics, FluentBit can write to
Azure Blob Storage, but only with a storage account shared key, since `azure_blob` has no Workload
Identity support. Create a Kubernetes secret holding the key in the data plane namespace:

```bash
STORAGE_ACCOUNT_KEY=$(az storage account keys list \
  --account-name <STORAGE_ACCOUNT> \
  --resource-group <RESOURCE_GROUP> \
  --query "[0].value" --output tsv)

kubectl create secret generic fluentbit-azure-key \
  --namespace <NAMESPACE> \
  --from-literal=shared_key="$STORAGE_ACCOUNT_KEY"

unset STORAGE_ACCOUNT_KEY
```

Then point the log source back at the object store, enable FluentBit, and reference the secret so
the key never lands in the rendered ConfigMap:

```yaml
config:
  proxy:
    persistedLogs:
      sourceType: ObjectStore
fluentbit:
  enabled: true
  azureBlobSharedKey: "${AZURE_STORAGE_SHARED_KEY}"
  env:
    - name: AZURE_STORAGE_SHARED_KEY
      valueFrom:
        secretKeyRef:
          name: fluentbit-azure-key
          key: shared_key
```

> [!NOTE] The storage account key grants full access to the account. Rotate it on your normal
> schedule; after rotation, update the secret (`kubectl create secret ... --dry-run=client -o yaml
> | kubectl apply -f -`) and restart the FluentBit DaemonSet.

## GCP (Workload Identity)

On GKE, use [GKE Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to grant the FluentBit service account access to GCS.

### GCP prerequisites

- [Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable) must be enabled on your GKE cluster

### 1. Create or reuse a GCP service account

Create a GCP service account (or reuse an existing one):

```bash
gcloud iam service-accounts create fluentbit-gsa \
  --display-name "FluentBit logging service account" \
  --project <PROJECT_ID>
```

### 2. Grant storage permissions

Grant the service account write access to the metadata bucket:

```bash
gcloud storage buckets add-iam-policy-binding gs://<BUCKET_NAME> \
  --member "serviceAccount:fluentbit-gsa@<PROJECT_ID>.iam.gserviceaccount.com" \
  --role "roles/storage.objectAdmin"
```

### 3. Bind the Kubernetes service account to the GCP service account

Allow the `fluentbit-system` Kubernetes service account to impersonate the GCP service account:

```bash
gcloud iam service-accounts add-iam-policy-binding \
  fluentbit-gsa@<PROJECT_ID>.iam.gserviceaccount.com \
  --role "roles/iam.workloadIdentityUser" \
  --member "serviceAccount:<PROJECT_ID>.svc.id.goog[<NAMESPACE>/fluentbit-system]"
```

Replace:

- `<PROJECT_ID>` with your GCP project ID
- `<BUCKET_NAME>` with the name of your data plane metadata bucket
- `<NAMESPACE>` with the namespace where the data plane is installed (default: `union`)

### 4. Configure the GCP Helm values

Set the Workload Identity annotation on the FluentBit service account in your data plane Helm values:

```yaml
fluentbit:
  serviceAccount:
    annotations:
      iam.gke.io/gcp-service-account: "fluentbit-gsa@<PROJECT_ID>.iam.gserviceaccount.com"
```

## Disabling persistent logs

To disable persistent logging entirely, set the following in your Helm values:

```yaml
fluentbit:
  enabled: false
```
