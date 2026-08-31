---
title: Prepare infrastructure
description: Create the AKS cluster, Storage Account, and managed identities the data plane needs.
icon: tools
weight: 1
variants: -flyte +union
---

# Prepare infrastructure

This page walks you through the Azure infrastructure required before deploying the Union dataplane on AKS. If you already have these resources, skip to [Deploy the dataplane](../selfmanaged-azure/deploy-dataplane).

> [!NOTE] **Deployment model**: This guide covers **Self-managed**: you run only the dataplane chart; Union hosts the control plane.

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

# --- Logging ---
export LOG_ANALYTICS_WORKSPACE=union-${ORG_NAME}   # Log Analytics workspace holding persisted task logs

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

A fourth add-on, Container Insights (`monitoring`), is required for historical task logs. It
needs a Log Analytics workspace to ship to, so it is enabled separately in
[Persisted task logs](#8-persisted-task-logs-log-analytics).

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

Save the OIDC issuer URL. You will need it when creating federated credentials:

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

Union stores workflow metadata and code bundle artifacts in Azure Blob Storage. The storage account **must have Data Lake Storage Gen2 enabled** (`--enable-hierarchical-namespace`). Union uses the `abfs://` protocol which requires this.

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

> [!NOTE] Union reads and writes this account through Workload Identity rather than the account
> key. `--allow-shared-key-access true` is only needed if you take the optional
> [FluentBit-to-Blob path](../configuration/persistent-logs#alternative-writing-to-blob-storage)
> for persisted logs; set it to `false` otherwise.

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

Azure Workload Identity lets Kubernetes pods authenticate to Azure services using a projected service account token: no credentials stored in secrets.

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

- Obtain the Storage Account ID:

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

## 8. Persisted task logs (Log Analytics)

Union reads historical task logs (the logs of a task pod that has already terminated) from an
Azure Log Analytics workspace. The AKS **Container Insights** add-on ships container logs into
that workspace, and the Union operator queries them back out using the backend managed identity.

> [!NOTE] **FluentBit is not used on Azure.** The chart's `values.azure.yaml` ships with
> `fluentbit.enabled: false`. FluentBit's `azure_blob` output cannot authenticate with Workload
> Identity, so the DaemonSet lands in `CrashLoopBackOff` unless you hand it a storage account
> shared key. See [Persistent logs](../configuration/persistent-logs) for that alternative and for
> the object store path used on AWS and GCP.

### Create the workspace and enable Container Insights

```bash
export LOG_ANALYTICS_WORKSPACE_ID=$(az monitor log-analytics workspace create \
  --resource-group $RESOURCE_GROUP \
  --workspace-name $LOG_ANALYTICS_WORKSPACE \
  --location $LOCATION \
  --query id --output tsv)

az aks enable-addons \
  --resource-group $RESOURCE_GROUP \
  --name $CLUSTER_NAME \
  --addons monitoring \
  --workspace-resource-id $LOG_ANALYTICS_WORKSPACE_ID
```

Container Insights is often already enabled, especially when a central platform team provisioned
the AKS cluster. In that case it is shipping to an existing workspace, frequently a shared one in
another resource group. Reuse that workspace instead of creating a second one, and save its
resource ID. You will need it to override the chart default when you
[deploy the dataplane](../selfmanaged-azure/deploy-dataplane).

```bash
export LOG_ANALYTICS_WORKSPACE_ID=$(az aks show \
  --resource-group $RESOURCE_GROUP \
  --name $CLUSTER_NAME \
  --query "addonProfiles.omsagent.config.logAnalyticsWorkspaceResourceID" --output tsv)
```

### Grant the backend identity read access

The backend managed identity needs the **Log Analytics Reader** role on the workspace. Without it,
the log pane in the UI stays empty and the operator logs an authorization error.

```bash
az role assignment create \
  --assignee-object-id $BACKEND_PRINCIPAL_ID \
  --assignee-principal-type ServicePrincipal \
  --role "Log Analytics Reader" \
  --scope $LOG_ANALYTICS_WORKSPACE_ID
```

> [!NOTE] The assignment is scoped to the workspace, which may sit in a different resource group
> under different ownership than the AKS cluster. Creating it requires
> `Microsoft.Authorization/roleAssignments/write` on that scope, so whoever administers that
> resource group may have to run this command for you.

### Verify

Confirm the workspace is actually receiving container logs from the dataplane namespace:

```bash
WORKSPACE_GUID=$(az monitor log-analytics workspace show \
  --ids $LOG_ANALYTICS_WORKSPACE_ID \
  --query customerId --output tsv)

az monitor log-analytics query \
  --workspace $WORKSPACE_GUID \
  --analytics-query "ContainerLogV2 | where TimeGenerated > ago(1h) | summarize count() by PodNamespace" \
  --output table
```

> [!NOTE] No rows means Container Insights is not ingesting, so fixing the Union configuration
> will not help. `az aks enable-addons` grants the cluster's Azure Monitor Agent identity the
> **Monitoring Metrics Publisher** role automatically; check that it is present if Container
> Insights was wired up by hand. Ingestion and query both use the public Azure Monitor endpoints.
> Azure supports no VNet service endpoints for them, so a cluster without egress needs an Azure
> Monitor Private Link Scope.

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
