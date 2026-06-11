---
title: Prepare infrastructure
weight: 1
variants: -flyte +union
---

# Prepare infrastructure

This page walks you through the Azure infrastructure required before deploying the Union dataplane on AKS. If you already have these resources, skip to [Deploy the dataplane](../selfmanaged-azure/deploy-dataplane).

> [!NOTE] **Deployment model**: This guide covers **Self-managed** — you run only the dataplane chart; Union hosts the control plane.

## Prerequisites
- Azure CLI [installed](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) and [configured](https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli?view=azure-cli-latest#sign-in-to-azure)

## Environment variables

Set these once at the top of your terminal session. All commands below reference them. Customize the names if you are deploying multiple data planes in the same subscription.

```bash
# --- Your environment ---
export SUBSCRIPTION_ID=$(az account show --query id --output tsv)
export TENANT_ID=$(az account show --query tenantId --output tsv)
export RESOURCE_GROUP=union-rg
export LOCATION=eastus2
export CLUSTER_NAME=union-dataplane
export ORG_NAME=<your-union-org-name>       # provided by Union

# --- Storage ---
export STORAGE_ACCOUNT=uniondataplane       # 3-24 lowercase alphanumeric, globally unique
export METADATA_CONTAINER=union-metadata
export FLUENTBIT_SECRET_NAME=fluentbit-azure-key   # k8s secret holding the storage key for persisted logs

# --- Identities ---
export BACKEND_IDENTITY_NAME=union-backend
export WORKER_IDENTITY_NAME=union-executions

# --- AKS namespace (do not change) ---
export DATAPLANE_NAMESPACE=union
```

## 1. Subscription and resource group

All Union infrastructure lives in a dedicated resource group for access control and cost tracking.

```bash
az account set --subscription $SUBSCRIPTION_ID

az group create \
  --name $RESOURCE_GROUP \
  --location $LOCATION
```

## 2. AKS cluster

You need an AKS cluster running one of the most recent three minor Kubernetes versions. See [Cluster Recommendations](../cluster-recommendations) for networking and node pool guidance.

Three specific add-ons are required:

| Add-on | Why |
|--------|-----|
| `--enable-oidc-issuer` | Enables the OIDC token issuer AKS needs for Workload Identity |
| `--enable-workload-identity` | Allows pods to assume Azure Managed Identities without credentials |
| `--enable-managed-identity` | AKS control plane uses a managed identity (not service principal) |

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

Save the OIDC issuer URL — you will need it when creating federated credentials:

```bash
export AKS_OIDC_ISSUER=$(az aks show \
  --resource-group $RESOURCE_GROUP \
  --name $CLUSTER_NAME \
  --query "oidcIssuerProfile.issuerUrl" \
  --output tsv)
```

Get cluster credentials:

```bash
az aks get-credentials \
  --resource-group $RESOURCE_GROUP \
  --name $CLUSTER_NAME
```

## 3. Node pools

Union workloads run on dedicated node pools. Separating system, worker, and GPU nodes allows independent scaling and keeps system pods stable.

### System node pool

The system pool was created with the cluster above. Recommended minimum: `Standard_D4s_v3` (4 vCPU / 16 GB) x 2 nodes.

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

```bash
az aks nodepool add \
  --resource-group $RESOURCE_GROUP \
  --cluster-name $CLUSTER_NAME \
  --name gpuworkers \
  --node-count 1 \
  --node-vm-size Standard_NC6s_v3 \
  --node-taints sku=gpu:NoSchedule \
  --labels union.ai/node-role=worker
```

> [!NOTE] **Spot VMs**: Union supports interruptible workloads on Azure Spot. Spot nodes are identified by the label `kubernetes.azure.com/scalesetpriority: spot`, which AKS sets automatically when `--priority Spot` is used.

## 4. Storage account and container

Union stores workflow metadata and code bundle artifacts in Azure Blob Storage. The storage account **must have Data Lake Storage Gen2 enabled** (`--enable-hierarchical-namespace`) — Union uses the `abfs://` protocol which requires this.

```bash
az storage account create \
  --name $STORAGE_ACCOUNT \
  --resource-group $RESOURCE_GROUP \
  --location $LOCATION \
  --sku Standard_LRS \
  --kind StorageV2 \
  --enable-hierarchical-namespace true \
  --allow-blob-public-access false \
  --allow-shared-key-access true

az storage container create \
  --name $METADATA_CONTAINER \
  --account-name $STORAGE_ACCOUNT
```

### CORS configuration

To enable the [Code Viewer](../configuration/code-viewer) in the Union UI, configure a CORS rule on your Storage Account:

```bash
az storage cors add \
  --services b \
  --methods GET HEAD \
  --origins "https://*.unionai.cloud" "https://*.union.ai" \
  --allowed-headers "*" \
  --exposed-headers "ETag" \
  --max-age 3600 \
  --account-name $STORAGE_ACCOUNT
```

### Data retention

Union recommends using lifecycle management policies on your Storage Account to manage storage costs. See [Data retention policy](../configuration/data-retention) for more information.

## 5. Managed identities

Union separates infrastructure-level access from workload-level access using two identities:

| Identity | Used by | Needs access to |
|----------|---------|-----------------|
| `union-backend` | Operator, propeller, clusterresourcesync | Storage account, Key Vault |
| `union-executions` | Task execution pods (user workloads) | Storage account + any customer Azure services |

```bash
# Backend identity (for Union system components)
az identity create \
  --name $BACKEND_IDENTITY_NAME \
  --resource-group $RESOURCE_GROUP

# Worker identity (for task pods)
az identity create \
  --name $WORKER_IDENTITY_NAME \
  --resource-group $RESOURCE_GROUP

# Save client IDs and principal IDs
export BACKEND_CLIENT_ID=$(az identity show \
  --name $BACKEND_IDENTITY_NAME \
  --resource-group $RESOURCE_GROUP \
  --query clientId --output tsv)

export BACKEND_PRINCIPAL_ID=$(az identity show \
  --name $BACKEND_IDENTITY_NAME \
  --resource-group $RESOURCE_GROUP \
  --query principalId --output tsv)

export WORKER_CLIENT_ID=$(az identity show \
  --name $WORKER_IDENTITY_NAME \
  --resource-group $RESOURCE_GROUP \
  --query clientId --output tsv)

export WORKER_PRINCIPAL_ID=$(az identity show \
  --name $WORKER_IDENTITY_NAME \
  --resource-group $RESOURCE_GROUP \
  --query principalId --output tsv)
```

## 6. Workload Identity and federated credentials

Azure Workload Identity lets Kubernetes pods authenticate to Azure services using a projected service account token — no credentials stored in secrets.

### Backend identity (Union system components)

```bash
az identity federated-credential create \
  --name "union-backend-federated" \
  --identity-name $BACKEND_IDENTITY_NAME \
  --resource-group $RESOURCE_GROUP \
  --issuer $AKS_OIDC_ISSUER \
  --subject "system:serviceaccount:${DATAPLANE_NAMESPACE}:union-system" \
  --audiences api://AzureADTokenExchange
```

### Worker identity (task execution pods)

Task pods run under the `union` service account. In single-namespace mode (the default with `low_privilege: true`), create one federated credential for the release namespace:

```bash
az identity federated-credential create \
  --name "union-worker-single-ns" \
  --identity-name $WORKER_IDENTITY_NAME \
  --resource-group $RESOURCE_GROUP \
  --issuer $AKS_OIDC_ISSUER \
  --subject "system:serviceaccount:${DATAPLANE_NAMESPACE}:union" \
  --audiences api://AzureADTokenExchange
```

If using multi-namespace mode (`low_privilege: false`), also create credentials for each project-domain namespace:

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

## 7. Role assignments

The managed identities need explicit RBAC permissions on the storage account.

- Obtaine the Storage Account ID:

```bash
STORAGE_ACCOUNT_ID=$(az storage account show \
    --name $STORAGE_ACCOUNT \
    --resource-group $RESOURCE_GROUP \
    --query id -o tsv)
```

```bash
# Backend identity: read/write workflow metadata
az role assignment create \
  --assignee-object-id $BACKEND_PRINCIPAL_ID \
  --assignee-principal-type ServicePrincipal \
  --role "Storage Blob Data Contributor" \
  --scope $STORAGE_ACCOUNT_ID

# Worker identity: read/write artifacts
az role assignment create \
  --assignee-object-id $WORKER_PRINCIPAL_ID \
  --assignee-principal-type ServicePrincipal \
  --role "Storage Blob Data Contributor" \
  --scope $STORAGE_ACCOUNT_ID
```

## 8. Persisted logs storage key (FluentBit)

To display historical task logs in the Union UI, FluentBit ships container logs to your
storage account. Because its `azure_blob` output cannot use Workload Identity (see the note in
[Storage Account and Container](#4-storage-account-and-container)), you must provide the storage
account shared key as a Kubernetes secret. The dataplane chart references this secret to inject
the key into FluentBit at runtime, so the key never appears in the rendered ConfigMap.

> [!NOTE] This step requires cluster credentials from [AKS Cluster](#2-aks-cluster)
> (`az aks get-credentials`).

Retrieve the storage account key and create the secret in the dataplane namespace:

```bash
# Ensure the dataplane namespace exists
kubectl create namespace $DATAPLANE_NAMESPACE \
  --dry-run=client -o yaml | kubectl apply -f -

# Fetch the storage account key
STORAGE_ACCOUNT_KEY=$(az storage account keys list \
  --account-name $STORAGE_ACCOUNT \
  --resource-group $RESOURCE_GROUP \
  --query "[0].value" --output tsv)

# Create the secret FluentBit reads (key name must be 'shared_key')
kubectl create secret generic $FLUENTBIT_SECRET_NAME \
  --namespace $DATAPLANE_NAMESPACE \
  --from-literal=shared_key="$STORAGE_ACCOUNT_KEY"

unset STORAGE_ACCOUNT_KEY
```

You will wire this secret into the chart in [Deploy the dataplane](../selfmanaged-azure/deploy-dataplane)
via the `fluentbit` values, for example:

```yaml
fluentbit:
  # Placeholder is expanded by FluentBit at runtime from the env var below,
  # keeping the key out of the rendered ConfigMap.
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

## 9. Azure Key Vault (optional)

Union provides an embedded secrets management backend. If your organization needs to integrate with Azure Key Vault, create a vault and grant the backend identity access:

```bash
export KEY_VAULT_NAME=union-${ORG_NAME}

az keyvault create \
  --name $KEY_VAULT_NAME \
  --resource-group $RESOURCE_GROUP \
  --location $LOCATION \
  --enable-rbac-authorization true

KEY_VAULT_RESOURCE_ID=$(az keyvault show \
  --name $KEY_VAULT_NAME \
  --query id --output tsv)

az role assignment create \
  --assignee-object-id $BACKEND_PRINCIPAL_ID \
  --assignee-principal-type ServicePrincipal \
  --role "Key Vault Secrets Officer" \
  --scope $KEY_VAULT_RESOURCE_ID
```

The Key Vault URI (`https://${KEY_VAULT_NAME}.vault.azure.net/`) maps to `AZURE_KEY_VAULT_URI` in the chart values.

Once your infrastructure is ready, proceed to [Deploy the dataplane](../selfmanaged-azure/deploy-dataplane).
