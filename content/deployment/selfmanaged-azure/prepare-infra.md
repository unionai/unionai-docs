---
title: Prepare infrastructure
weight: 1
variants: -flyte -byoc +selfmanaged
---

# Prepare infrastructure

This page walks you through creating the Azure resources needed for a Union data plane. If you already have these resources, skip to [Deploy the dataplane](../selfmanaged-azure/deploy-dataplane).

## AKS Cluster

You need an AKS cluster running one of the most recent three minor Kubernetes versions. See [Cluster Recommendations](../cluster-recommendations) for networking and node pool guidance.

If you don't already have a cluster, create one with the Azure CLI:

```bash
export RESOURCE_GROUP=union-rg
export REGION=eastus2
export CLUSTER_NAME=union-dataplane

az aks create \
  --resource-group ${RESOURCE_GROUP} \
  --name ${CLUSTER_NAME} \
  --location ${REGION} \
  --kubernetes-version 1.31 \
  --node-count 3 \
  --node-vm-size Standard_D4s_v3 \
  --enable-oidc-issuer \
  --enable-workload-identity \
  --generate-ssh-keys
```

> [!NOTE] The `--enable-oidc-issuer` and `--enable-workload-identity` flags are required for [Workload Identity](#workload-identity) below.

Get the OIDC issuer URL (you will need it when creating federated credentials):

```bash
export AKS_OIDC_ISSUER=$(az aks show \
  --resource-group ${RESOURCE_GROUP} \
  --name ${CLUSTER_NAME} \
  --query "oidcIssuerProfile.issuerUrl" \
  --output tsv)
```

Union supports autoscaling and the use of spot (interruptible) instances.

### Resource Requirements

By default, the Union installation requests the following resources:

|          | CPU (vCPUs)| Memory (GiB) |
|----------|------------|--------------|
| Requests |          14|          27.1|
| Limits   |          17|            32|

For GPU access, Union injects tolerations and label selectors to execution Pods.

## Azure Blob Storage

Each data plane uses Azure Blob Storage containers to store data used in workflow execution.
Union recommends the use of two containers within a Storage Account:

1. **Metadata container**: contains workflow execution data such as task inputs and outputs.
2. **Fast registration container**: contains local code artifacts copied into the Flyte task container at runtime when using `union register` or `union run --remote --copy-all`.

You can also choose to use a single container.

Create the Storage Account and containers:

```bash
export STORAGE_ACCOUNT=uniondataplane   # must be globally unique, lowercase alphanumeric
export SUBSCRIPTION_ID=$(az account show --query id --output tsv)

az storage account create \
  --name ${STORAGE_ACCOUNT} \
  --resource-group ${RESOURCE_GROUP} \
  --location ${REGION} \
  --sku Standard_LRS \
  --kind StorageV2

az storage container create \
  --name metadata \
  --account-name ${STORAGE_ACCOUNT}

az storage container create \
  --name fast-reg \
  --account-name ${STORAGE_ACCOUNT}
```

### CORS Configuration

To enable the [Code Viewer](../configuration/code-viewer) in the Union UI, configure a CORS rule on your Storage Account. This allows the UI to securely fetch code bundles directly from blob storage:

```bash
az storage cors add \
  --services b \
  --methods GET HEAD \
  --origins "https://*.unionai.cloud" \
  --allowed-headers "*" \
  --exposed-headers "ETag" \
  --max-age 3600 \
  --account-name ${STORAGE_ACCOUNT}
```

For more details, see the [Azure Storage CORS documentation](https://learn.microsoft.com/en-us/rest/api/storageservices/cross-origin-resource-sharing--cors--support-for-the-azure-storage-services).

### Data Retention

Union recommends using lifecycle management policies on your Storage Account to manage storage costs. See [Data retention policy](../configuration/data-retention) for more information.

## Azure Container Registry

Create an Azure Container Registry for Image Builder to push and pull container images:

```bash
export ACR_NAME=uniondataplane   # must be globally unique, lowercase alphanumeric

az acr create \
  --name ${ACR_NAME} \
  --resource-group ${RESOURCE_GROUP} \
  --location ${REGION} \
  --sku Basic
```

Note the registry login server (e.g. `${ACR_NAME}.azurecr.io`) -- you will reference it when configuring Workload Identity permissions below.

## Workload Identity

Union uses [Microsoft Entra Workload ID](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview) to securely access Azure resources.

### 1. Create the platform identity

Create a User Assigned Managed Identity for the Union platform services:

```bash
export UNION_NAMESPACE=union   # namespace where you will install the Union operator

az identity create \
  --name union-system-identity \
  --resource-group ${RESOURCE_GROUP} \
  --location ${REGION}

export SYSTEM_IDENTITY_CLIENT_ID=$(az identity show \
  --name union-system-identity \
  --resource-group ${RESOURCE_GROUP} \
  --query clientId \
  --output tsv)

export SYSTEM_IDENTITY_PRINCIPAL_ID=$(az identity show \
  --name union-system-identity \
  --resource-group ${RESOURCE_GROUP} \
  --query principalId \
  --output tsv)
```

### 2. Create the federated credential for the platform identity

Create a federated credential that maps to the `union-system` Kubernetes service account:

```bash
az identity federated-credential create \
  --name union-system-fedcred \
  --identity-name union-system-identity \
  --resource-group ${RESOURCE_GROUP} \
  --issuer ${AKS_OIDC_ISSUER} \
  --subject system:serviceaccount:${UNION_NAMESPACE}:union-system \
  --audiences api://AzureADTokenExchange
```

### 3. Assign roles to the platform identity

Grant `Storage Blob Data Owner` on the Storage Account and `AcrPush` on the Container Registry:

```bash
az role assignment create \
  --assignee-object-id ${SYSTEM_IDENTITY_PRINCIPAL_ID} \
  --assignee-principal-type ServicePrincipal \
  --role "Storage Blob Data Owner" \
  --scope /subscriptions/${SUBSCRIPTION_ID}/resourceGroups/${RESOURCE_GROUP}/providers/Microsoft.Storage/storageAccounts/${STORAGE_ACCOUNT}

az role assignment create \
  --assignee-object-id ${SYSTEM_IDENTITY_PRINCIPAL_ID} \
  --assignee-principal-type ServicePrincipal \
  --role "AcrPush" \
  --scope /subscriptions/${SUBSCRIPTION_ID}/resourceGroups/${RESOURCE_GROUP}/providers/Microsoft.ContainerRegistry/registries/${ACR_NAME}
```

### 4. Configure the service account annotation

In your Helm values, annotate the `union-system` service account with the managed identity client ID:

```yaml
commonServiceAccount:
  annotations:
    azure.workload.identity/client-id: "<SYSTEM_IDENTITY_CLIENT_ID>"
```

### Workers

This is the identity that the Pods created for each execution will use to access Azure resources. Those Pods use the `default` Kubernetes service account on each project-domain namespace, unless otherwise specified.

Create a User Assigned Managed Identity for worker pods:

```bash
az identity create \
  --name union-worker-identity \
  --resource-group ${RESOURCE_GROUP} \
  --location ${REGION}

export WORKER_IDENTITY_CLIENT_ID=$(az identity show \
  --name union-worker-identity \
  --resource-group ${RESOURCE_GROUP} \
  --query clientId \
  --output tsv)

export WORKER_IDENTITY_PRINCIPAL_ID=$(az identity show \
  --name union-worker-identity \
  --resource-group ${RESOURCE_GROUP} \
  --query principalId \
  --output tsv)
```

Create federated credentials for each project-domain namespace:

```bash
for NS in development staging production; do
  az identity federated-credential create \
    --name union-worker-fedcred-${NS} \
    --identity-name union-worker-identity \
    --resource-group ${RESOURCE_GROUP} \
    --issuer ${AKS_OIDC_ISSUER} \
    --subject system:serviceaccount:${NS}:default \
    --audiences api://AzureADTokenExchange
done
```

Assign the `Storage Blob Data Owner` role to the worker identity:

```bash
az role assignment create \
  --assignee-object-id ${WORKER_IDENTITY_PRINCIPAL_ID} \
  --assignee-principal-type ServicePrincipal \
  --role "Storage Blob Data Owner" \
  --scope /subscriptions/${SUBSCRIPTION_ID}/resourceGroups/${RESOURCE_GROUP}/providers/Microsoft.Storage/storageAccounts/${STORAGE_ACCOUNT}
```

## Azure Key Vault (optional)

Union ships with an embedded secrets manager. Alternatively, you can enable Union to consume secrets from Azure Key Vault adding the following to your Helm values file:

```yaml
config:

  ## Optional integration with Azure Key Vault secrets manager
  core:
    webhook:
      embeddedSecretManagerConfig:
        enabled: true
        type: Azure
        azureConfig:
          vaultURI: ""https://kv-myorg-prod.vault.azure.net/" #full key vault URI
      secretManagerTypes:
        - Azure
        - Embedded

```
