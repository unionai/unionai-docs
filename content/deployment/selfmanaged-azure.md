---
title: Data plane setup on Azure
weight: 5
variants: -flyte -byoc +selfmanaged
---

# Data plane setup on Azure

{{< key product_name >}}'s modular architecture allows for great flexibility and control.
The customer can decide how many clusters to have, their shape, and who has access to what.
All communication is encrypted.  The Union architecture is described on the [Architecture](./architecture/_index) page.

## AKS Cluster

You need an AKS cluster running one of the most recent three minor Kubernetes versions. See [Cluster Recommendations](./cluster-recommendations) for networking and node pool guidance.

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

To enable the [Code Viewer](./configuration/code-viewer) in the Union UI, configure a CORS rule on your Storage Account. This allows the UI to securely fetch code bundles directly from blob storage:

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

Union recommends using lifecycle management policies on your Storage Account to manage storage costs. See [Data retention policy](./configuration/data-retention) for more information.

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

## Assumptions

* You have a {{< key product_name >}} organization, and you know the control plane URL for your organization.
* You have a cluster name provided by or coordinated with Union.
* You have an AKS cluster with OIDC issuer and Workload Identity enabled, running one of the most recent three minor K8s versions.
  [Learn more](https://kubernetes.io/releases/version-skew-policy/).
* You have configured a Storage Account, Container Registry, and Workload Identity as described above.

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
   uctl selfserve provision-dataplane-resources --clusterName <YOUR_SELECTED_CLUSTERNAME>  --provider azure
   ```

   * The command will output the ID, name, and a secret that will be used by the Union services to communicate with your control plane.
     It will also generate a YAML file specific to the provider that you specify, in this case `azure`.

   * Save the secret that is displayed. Union does not store the credentials; rerunning the same command can be used to retrieve the secret later.

3. Update the generated values file with your infrastructure details:

   - Set `azure.tenantId`, `azure.subscriptionId`, and `azure.resourceGroupName` to your Azure environment values.
   - Set `storage.custom.container` to your Azure Storage container name.
   - Set `storage.custom.stow.config.account` to your Storage Account name and `storage.custom.stow.config.key` to the Storage Account key.
   - Replace `<SERVICE_CLIENT_ID>` in `additionalServiceAccountAnnotations` with the Managed Identity client ID for the `union-system` service account (from the [Workload Identity](#workload-identity) section).
   - Replace `<WORKER_CLIENT_ID>` in `userRoleAnnotationValue` with the Managed Identity client ID for worker pods (from the [Workers](#workers) section).

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
