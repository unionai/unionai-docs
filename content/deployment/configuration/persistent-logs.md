---
title: Persistent logs
weight: 4
variants: -flyte -serverless -byoc +selfmanaged
---

# Persistent logs

Persistent logging is enabled by default. The data plane deploys [FluentBit](https://fluentbit.io/) as a DaemonSet that collects container logs from every node and writes them to the `persisted-logs/` path in the object store configured for your data plane.

FluentBit runs under the `fluentbit-system` Kubernetes service account. This service account must have write access to the storage bucket so FluentBit can push logs. The sections below describe how to grant that access on each cloud provider.

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
    name: fluentbit-system
    annotations:
      eks.amazonaws.com/role-arn: "arn:aws:iam::<ACCOUNT_ID>:role/<FLUENTBIT_ROLE_NAME>"
```

## Azure (Workload Identity Federation)

On AKS, use [Microsoft Entra Workload Identity](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview) to grant the FluentBit service account access to Azure Blob Storage.

### Azure prerequisites

- Your AKS cluster must be [enabled as an OIDC Issuer](https://learn.microsoft.com/en-us/azure/aks/use-oidc-issuer)
- The [Azure Workload Identity](https://learn.microsoft.com/en-us/azure/aks/workload-identity-deploy-cluster) mutating webhook must be installed on your cluster

### 1. Create or reuse a Managed Identity

Create a User Assigned Managed Identity (or reuse an existing one):

```bash
az identity create \
  --name fluentbit-identity \
  --resource-group <RESOURCE_GROUP> \
  --location <LOCATION>
```

Note the `clientId` from the output.

### 2. Add a federated credential

Create a federated credential that maps the `fluentbit-system` Kubernetes service account to the managed identity:

```bash
az identity federated-credential create \
  --name fluentbit-federated-credential \
  --identity-name fluentbit-identity \
  --resource-group <RESOURCE_GROUP> \
  --issuer <AKS_OIDC_ISSUER_URL> \
  --subject "system:serviceaccount:<NAMESPACE>:fluentbit-system" \
  --audiences "api://AzureADTokenExchange"
```

Replace:

- `<RESOURCE_GROUP>` with your Azure resource group
- `<AKS_OIDC_ISSUER_URL>` with the OIDC issuer URL of your AKS cluster
- `<NAMESPACE>` with the namespace where the data plane is installed (default: `union`)

You can retrieve the OIDC issuer URL with:

```bash
az aks show --name <CLUSTER_NAME> --resource-group <RESOURCE_GROUP> \
  --query "oidcIssuerProfile.issuerUrl" --output tsv
```

### 3. Assign a storage role

Assign the `Storage Blob Data Contributor` role to the managed identity at the storage account level:

```bash
az role assignment create \
  --assignee <CLIENT_ID> \
  --role "Storage Blob Data Contributor" \
  --scope "/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.Storage/storageAccounts/<STORAGE_ACCOUNT>"
```

### 4. Configure the Azure Helm values

Set the Workload Identity annotation on the FluentBit service account in your data plane Helm values:

```yaml
fluentbit:
  serviceAccount:
    name: fluentbit-system
    annotations:
      azure.workload.identity/client-id: "<CLIENT_ID>"
```

You must also ensure the FluentBit pods have the Workload Identity label. If you have already set `additionalPodLabels` for your data plane, confirm the following label is present:

```yaml
additionalPodLabels:
  azure.workload.identity/use: "true"
```

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
    name: fluentbit-system
    annotations:
      iam.gke.io/gcp-service-account: "fluentbit-gsa@<PROJECT_ID>.iam.gserviceaccount.com"
```

## Disabling persistent logs

To disable persistent logging entirely, set the following in your Helm values:

```yaml
fluentbit:
  enabled: false
```
