---
title: Prepare the Azure environment
weight: 2
variants: -flyte -byoc +selfmanaged
---

# Union Self Managed — Azure Prerequisites

This guide walks through the Azure infrastructure required before deploying the Union
dataplane on AKS. Each section explains **what** you need and **why Union needs it**, with
`az` CLI commands you can run directly.

> **Deployment model**: This guide covers **Self Managed (BYOK)** — you run only the
> dataplane chart; Union hosts the control plane. If you are running both charts yourself
> (Selfhosted), additional prerequisites apply for the control plane.

---

## Preparing your environment

Make sure your system has the Azure CLI [installed](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) and [configured](https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli?view=azure-cli-latest)

## Prerequisites Checklist

Work through these in order. Each item links to its section below.

- [ ] [Azure subscription and resource group](#1-subscription-and-resource-group)
- [ ] [AKS cluster with required add-ons](#2-aks-cluster)
- [ ] [Node pools (system, CPU workers, optional GPU)](#3-node-pools)
- [ ] [Storage account with Data Lake Gen2](#4-storage-account-and-containers)
- [ ] [Two user-assigned managed identities](#5-managed-identities)
- [ ] [Federated credentials for Workload Identity](#6-workload-identity-and-federated-credentials)
- [ ] [Role assignments for managed identities](#7-role-assignments)
- [ ] [Log Analytics workspace](#8-log-analytics-workspace)
---

## Variables Used in This Guide

Set these once at the top of your terminal session. All `az` commands below reference them.
> Most of these resources don't exist yet, you're picking the names or options you want to use for this environment

```bash
# --- Your environment ---
SUBSCRIPTION_ID="<your-subscription-id>"        # az account show --query id
TENANT_ID="<your-tenant-id>"          # az account show --query tenantId
RESOURCE_GROUP="<your-resource-group-name>"
LOCATION="eastus" #Regions list https://learn.microsoft.com/en-us/azure/reliability/regions-list?tabs=all#azure-regions-list-1
CLUSTER_NAME="<cluster-name>"
# you can pick a cluster name 
ORG_NAME="<your-union-org-name>"       # provided by Union

# --- Storage ---
STORAGE_ACCOUNT="union${ORG_NAME//-/}prod"      # 3-24 lowercase alphanumeric
METADATA_CONTAINER="union-metadata"

# --- Identities ---
BACKEND_IDENTITY_NAME="union-backend"
WORKER_IDENTITY_NAME="union-executions"


# --- Log Analytics ---
LOG_ANALYTICS_WORKSPACE="union-${ORG_NAME}"    # Union expects this exact naming convention

# --- AKS namespaces (do not change) ---
DATAPLANE_NAMESPACE="union"

```

---

## 1. Subscription and Resource Group

**Why Union needs this:** All Union infrastructure lives in a dedicated resource group for access control and cost tracking.

```bash
# Set active subscription
az account set --subscription $SUBSCRIPTION_ID

# Create resource group
az group create \
  --name $RESOURCE_GROUP \
  --location $LOCATION
```

---

## 2. AKS Cluster

**Why Union needs this:** The dataplane runs on AKS. Three specific add-ons are required:

| Add-on | Why |
|--------|-----|
| `--enable-oidc-issuer` | Enables the OIDC token issuer AKS needs for Workload Identity |
| `--enable-workload-identity` | Allows pods to assume Azure Managed Identities without credentials |
| `--enable-managed-identity` | AKS control plane uses a managed identity (not service principal) |

Without Workload Identity, the dataplane cannot authenticate to Azure Blob Storage or Key Vault.

```bash
az aks create \
  --resource-group $RESOURCE_GROUP \
  --name $CLUSTER_NAME \
  --location $LOCATION \
  --enable-oidc-issuer \
  --enable-workload-identity \
  --enable-managed-identity \
  --node-count 2 \
  --node-vm-size Standard_D4s_v3
```

**Save the OIDC issuer URL** — you'll need it when creating federated credentials:
```bash
AKS_OIDC_ISSUER=$(az aks show \
  --resource-group $RESOURCE_GROUP \
  --name $CLUSTER_NAME \
  --query "oidcIssuerProfile.issuerUrl" \
  --output tsv)
echo "OIDC Issuer: $AKS_OIDC_ISSUER"
```

**Get cluster credentials:**
```bash
az aks get-credentials \
  --resource-group $RESOURCE_GROUP \
  --name $CLUSTER_NAME
```

> **Reference:** [AKS Workload Identity overview](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview)

---

## 3. Node Pools

**Why Union needs this:** Union workloads run on dedicated node pools. Separating system,
worker, and GPU nodes allows independent scaling and keeps system pods stable.

### System node pool
The system pool was created with the cluster above. Recommended minimum: `Standard_D4s_v3`
(4 vCPU / 16 GB) × 2 nodes.

### CPU worker node pool

```bash

az aks nodepool add \
  --resource-group $RESOURCE_GROUP \
  --cluster-name $CLUSTER_NAME \
  --name workers \
  --node-count 2 \
  --node-vm-size Standard_B8as_v2 \
  --labels union.ai/node-role=worker
```

### GPU node pool (optional)

Add a GPU node pool to your cluster if you need to:
```bash
# TODO: confirm GPU SKU and driver add-on during testing
az aks nodepool add \
  --resource-group $RESOURCE_GROUP \
  --cluster-name $CLUSTER_NAME \
  --name gpuworkers \
  --node-count 1 \
  --node-vm-size Standard_NC6s_v3 \
  --node-taints sku=gpu:NoSchedule \
  --labels union.ai/node-role=worker
```

> **Spot VMs:** Union supports interruptible workloads on Azure Spot. Spot nodes are
> identified by the label `kubernetes.azure.com/scalesetpriority: spot`, which AKS sets
> automatically when `--priority Spot` is used. No manual labeling needed.
>
> ```bash
> # Spot worker pool example
> az aks nodepool add \
>   --resource-group $RESOURCE_GROUP \
>   --cluster-name $CLUSTER_NAME \
>   --name spotworkers \
>   --node-count 0 \
>   --min-count 0 \
>   --max-count 10 \
>   --enable-cluster-autoscaler \
>   --priority Spot \
>   --eviction-policy Delete \
>   --spot-max-price -1 \
>   --node-vm-size Standard_D8s_v3
> ```

---

## 4. Storage Account and Containers

**Why Union needs this:** Union stores workflow metadata and fast-registration artifacts in
Azure Blob Storage. The storage account **must have Data Lake Storage Gen2 enabled**
(`--enable-hierarchical-namespace`) — Union uses the `abfs://` protocol to access it,
which requires this.

```bash
# Create storage account with hierarchical namespace (Data Lake Gen2)
az storage account create \
  --name $STORAGE_ACCOUNT \
  --resource-group $RESOURCE_GROUP \
  --location $LOCATION \
  --sku Standard_LRS \
  --kind StorageV2 \
  --enable-hierarchical-namespace true \
  --allow-blob-public-access false

# Create the metadata container
az storage container create \
  --name $METADATA_CONTAINER \
  --account-name $STORAGE_ACCOUNT
```


> **Reference:** [Azure Data Lake Storage Gen2](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction)

---

## 5. Managed Identities

**Why Union needs two identities:** Union separates infra-level access from workload-level
access:

| Identity | Used by | Needs access to |
|----------|---------|-----------------|
| `union-backend` | Operator, propeller, clusterresourcesync | Storage account, Key Vault |
| `union-executions` | Task execution pods (user workloads) | Storage account + any customer Azure services |

```bash
# Backend identity (for Union system components)
az identity create \
  --name union-backend \
  --resource-group $RESOURCE_GROUP

# Worker identity (for task pods)
az identity create \
  --name union-executions \
  --resource-group $RESOURCE_GROUP

# Save client IDs — these map to AZURE_BACKEND_CLIENT_ID and AZURE_WORKER_CLIENT_ID
BACKEND_CLIENT_ID=$(az identity show \
  --name $BACKEND_IDENTITY_NAME \
  --resource-group $RESOURCE_GROUP \
  --query clientId --output tsv)

WORKER_CLIENT_ID=$(az identity show \
  --name $WORKER_IDENTITY_NAME \
  --resource-group $RESOURCE_GROUP \
  --query clientId --output tsv)

echo "Backend client ID: $BACKEND_CLIENT_ID"
echo "Worker client ID:  $WORKER_CLIENT_ID"
```

> **Reference:** [User-assigned managed identities](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/how-manage-user-assigned-managed-identities)

---

## 6. Workload Identity and Federated Credentials

**Why Union needs this:** Azure Workload Identity lets Kubernetes pods authenticate to
Azure services using a projected service account token — no credentials stored in secrets.
Each Kubernetes service account that needs Azure access gets a *federated credential* linking
it to a managed identity.

Union requires federated credentials for these Kubernetes service accounts:

| Kubernetes SA | Namespace | Managed Identity |
|---------------|-----------|-----------------|
| `union-system` | `union` | `union-backend` |
| `default` | one per project domain (e.g. `development`, `staging`, `production`) | `union-worker` |

**Backend identity (Union system components):**

```bash
az identity federated-credential create \
  --name "union-backend-federated" \
  --identity-name $BACKEND_IDENTITY_NAME \
  --resource-group $RESOURCE_GROUP \
  --issuer $AKS_OIDC_ISSUER \
  --subject "system:serviceaccount:${DATAPLANE_NAMESPACE}:union" \
  --audiences api://AzureADTokenExchange
```

**Worker identity (task execution pods):**

Task pods run under the `default` service account in the same namespace where the Union chart was deployed. This is known as the `single namespace mode` and is the default behavior.

Create the corresponding Federated Identity:

```
az identity federated-credential create \
--name "union-worker-single-ns" \
--identity-name $WORKER_IDENTITY_NAME \
--resource-group $RESOURCE_GROUP \
--issuer $AKS_OIDC_ISSUER \
>   --subject "system:serviceaccount:${DATAPLANE_NAMESPACE}:default" \
>   --audiences api://AzureADTokenExchange

```

each project domain namespace, created
automatically by `clusterresourcesync`. Each namespace needs its own federated credential.

```bash
for ns in development staging production; do
  az identity federated-credential create \
    --name "union-worker-${ns}" \
    --identity-name $WORKER_IDENTITY_NAME \
    --resource-group $RESOURCE_GROUP \
    --issuer $AKS_OIDC_ISSUER \
    --subject "system:serviceaccount:${ns}:default" \
    --audiences api://AzureADTokenExchange
done
```

> **Single-namespace mode:** If you deployed the chart with `namespaces.enabled: true`,
> workloads will run on namespaces, corresponding
>(default: `union`). In that
> case, create a single federated credential for the `default` SA in that namespace instead:
>
> ```bash
> az identity federated-credential create \
>   --name "union-worker-single-ns" \
>   --identity-name $WORKER_IDENTITY_NAME \
>   --resource-group $RESOURCE_GROUP \
>   --issuer $AKS_OIDC_ISSUER \
>   --subject "system:serviceaccount:${DATAPLANE_NAMESPACE}:default" \
>   --audiences api://AzureADTokenExchange
> ```

> **Reference:** [Workload Identity federation](https://learn.microsoft.com/en-us/azure/active-directory/workload-identities/workload-identity-federation)

---

## 7. Role Assignments

**Why Union needs this:** The managed identities need explicit RBAC permissions on the
storage account to read/write workflow data.

```bash
STORAGE_RESOURCE_ID=$(az storage account show \
  --name $STORAGE_ACCOUNT \
  --resource-group $RESOURCE_GROUP \
  --query id --output tsv)

BACKEND_PRINCIPAL_ID=$(az identity show \
  --name $BACKEND_IDENTITY_NAME \
  --resource-group $RESOURCE_GROUP \
  --query principalId --output tsv)

WORKER_PRINCIPAL_ID=$(az identity show \
  --name $WORKER_IDENTITY_NAME \
  --resource-group $RESOURCE_GROUP \
  --query principalId --output tsv)

# Backend identity: read/write workflow metadata
az role assignment create \
  --assignee-object-id $BACKEND_PRINCIPAL_ID \
  --assignee-principal-type ServicePrincipal \
  --role "Storage Blob Data Owner" \
  --scope "${STORAGE_RESOURCE_ID}/blobServices/default/containers/${METADATA_CONTAINER}"


# Worker identity: read/write artifacts
az role assignment create \
  --assignee-object-id $WORKER_PRINCIPAL_ID \
  --assignee-principal-type ServicePrincipal \
  --role "Storage Blob Data Owner" \
  --scope "${STORAGE_RESOURCE_ID}/blobServices/default/containers/${METADATA_CONTAINER}"
```

---

## 8. (Optional) Azure Key Vault

Union provides an embedded secrets management backend supported by Kubernetes secrets. If your organization needs to integrate with Azure Key Vault, complete the below steps:


### Create a key vault (skip if it already exists)


```bash
az keyvault create \
  --name $KEY_VAULT_NAME \
  --resource-group $RESOURCE_GROUP \
  --location $LOCATION \
  --enable-rbac-authorization true

KEY_VAULT_RESOURCE_ID=$(az keyvault show \
  --name $KEY_VAULT_NAME \
  --query id --output tsv)
```

### Configure backend identity access

This is needed for the Union backend to read and inject secrets:

```bash
az role assignment create \
  --assignee-object-id $BACKEND_PRINCIPAL_ID \
  --assignee-principal-type ServicePrincipal \
  --role "Key Vault Secrets Officer" \
  --scope $KEY_VAULT_RESOURCE_ID
```

The Key Vault URI follows the pattern `https://<vault-name>.vault.azure.net/` and maps
directly to `AZURE_KEY_VAULT_URI` in the chart values


> **Reference:** [Key Vault RBAC](https://learn.microsoft.com/en-us/azure/key-vault/general/rbac-guide)


---

With all the required configurations completed, you can [proceed to install Union](./installation.md)