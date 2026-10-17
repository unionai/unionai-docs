---
title: Provision your Azure resources
description: Create the AKS cluster, storage account, container registry, Key Vault, and managed identities that an Azure cluster pool needs.
icon: microsoft
weight: 6
variants: -flyte +union
---

# Provision your Azure resources

Union.ai installs the data plane into your cluster for you, but the Azure resources it runs on must exist first. This page creates them with the Azure CLI:

- an AKS cluster with Azure CNI overlay, the OIDC issuer, Workload Identity, and one autoscaled node pool
- a Data Lake Storage Gen2 account with one private `metadata` container, the cluster pool's object store
- an Azure Container Registry
- a Key Vault, where the data plane keeps runtime secrets
- separate system and task managed identities, each federated to specific Kubernetes service accounts
- a Log Analytics workspace with Container Insights, from which the Union.ai UI reads task logs after the pods are gone

At the end you have the values you enter when you connect your cluster: three for the cluster pool, and seven for registering the cluster.

These resources differ from the ones in the manual [Azure infrastructure](../selfmanaged/infrastructure-recommendations/azure) guide for self-managed deployments: here Key Vault is required and holds runtime secrets, and the agent you install from the Union.ai UI installs the data plane chart. Use this page only for a cluster you connect from the Union.ai UI.

> [!WARNING] Choose the namespace before you start
> The managed identities trust Kubernetes service accounts in one namespace, which you choose in [step 1](#1-sign-in-and-choose-names). When you register the cluster, you must enter exactly that namespace. Azure federated credentials accept no wildcard, so a mismatch is not reported anywhere: the data plane's pods run with no Azure identity, and the cluster never finishes registering.

> [!NOTE] Already have these resources?
> This page is optional. You can use existing resources instead, as long as they meet the same requirements:
>
> - The AKS cluster has the OIDC issuer and Workload Identity enabled, can add nodes as the data plane needs them, and its nodes have OS disks of at least 200 GiB ([step 7](#7-create-the-aks-cluster)).
> - The storage account has the hierarchical namespace (Data Lake Storage Gen2) enabled, and the CORS rule from [step 4](#4-create-the-storage-account-and-container).
> - The Key Vault uses Azure RBAC for access.
> - The two managed identities have the federated credentials from [step 8](#8-federate-the-identities-to-the-kubernetes-service-accounts), and the roles from [step 9](#9-grant-access).
>
> Then collect the values listed in [step 10](#10-check-the-resources-and-collect-the-values), and go on to [step 11](#11-connect-your-cluster).

## Prerequisites

- The [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) and `kubectl`. If you don't have `kubectl`, install it with `az aks install-cli`.
- An account that can create resource groups and role assignments in the subscription: Owner, or Contributor together with User Access Administrator. Contributor alone cannot create role assignments, so with it the setup fails as soon as it assigns a role.
- A Union.ai organization. See [Sign up for Union.ai](./sign-up).

The commands create billable resources, including the AKS cluster, its nodes, a standard load balancer, and the Log Analytics workspace, which bills per GB of logs it ingests. The cluster's API server is reachable from the internet, and its outbound traffic goes through the AKS-managed load balancer. The setup does not create a private cluster or a NAT gateway.

Run every step in the same shell session. Later steps use the variables that earlier steps export.

## 1. Sign in and choose names

Replace `<your-subscription-id>` with the subscription to create the resources in, and `<your-prefix>` with the name prefix described below. Set `UNION_UI_ORIGIN` to the address of your Union.ai UI: copy the scheme and host from your browser's address bar while you are signed in, without a trailing slash, for example `https://acme.hosted.unionai.cloud`.

`AZURE_NAME_PREFIX` names every resource. The storage account, the registry, and the Key Vault take their names from it, and those names must be globally unique across Azure, so include something specific to your organization, for example `acme-union-dp`. The prefix must be 5 to 24 characters of lowercase letters, digits, and single hyphens, start with a letter, end with a letter or digit, and contain at least 5 letters or digits.

```bash
az login
az account set --subscription <your-subscription-id>

export AZURE_SUBSCRIPTION_ID="$(az account show --query id -o tsv)"
export AZURE_TENANT_ID="$(az account show --query tenantId -o tsv)"
export AZURE_LOCATION="eastus2"
export AZURE_NAME_PREFIX="<your-prefix>"
export UNION_UI_ORIGIN="https://<your-org>.hosted.unionai.cloud"
export UNION_DATAPLANE_NAMESPACE="union"

export AZURE_RESOURCE_GROUP_NAME="$AZURE_NAME_PREFIX"
export AZURE_CLUSTER_NAME="$AZURE_NAME_PREFIX"
export AZURE_VNET_NAME="$AZURE_NAME_PREFIX"
export AZURE_NODE_SUBNET_NAME="${AZURE_NAME_PREFIX}-nodes"
export AZURE_LOG_ANALYTICS_WORKSPACE_NAME="${AZURE_NAME_PREFIX}-logs"
export AZURE_SYSTEM_IDENTITY_NAME="${AZURE_NAME_PREFIX}-system"
export AZURE_TASK_IDENTITY_NAME="${AZURE_NAME_PREFIX}-task"
export AZURE_KEY_VAULT_NAME="$AZURE_NAME_PREFIX"
export AZURE_WORK_DIR="$(mktemp -d)"

# Storage account and registry names cannot contain hyphens.
export AZURE_ALPHANUMERIC_PREFIX="${AZURE_NAME_PREFIX//-/}"
export AZURE_STORAGE_ACCOUNT_NAME="$AZURE_ALPHANUMERIC_PREFIX"
export AZURE_CONTAINER_REGISTRY_NAME="$AZURE_ALPHANUMERIC_PREFIX"

az account show --query '{name:name,id:id,tenant:tenantId}' -o table
az group exists --name "$AZURE_RESOURCE_GROUP_NAME"
az storage account check-name --name "$AZURE_STORAGE_ACCOUNT_NAME" --query nameAvailable
az acr check-name --name "$AZURE_CONTAINER_REGISTRY_NAME" --query nameAvailable
```

Check that the subscription is the one you intend to use, that `az group exists` prints `false`, and that both `check-name` commands print `true`. Otherwise choose another prefix.

If your account can see more than one tenant, sign in with `az login --tenant <tenant-id>`. Signing in to the wrong tenant succeeds, and the next command then reports that the subscription is not found.

`UNION_DATAPLANE_NAMESPACE` is the namespace the data plane is installed into, and the one you enter when you register the cluster. `union` is the default the Union.ai UI uses when the field is left empty. If you choose another name, it must be a valid Kubernetes namespace name, and not `default`, `dataplane-agent`, or one that starts with `kube-`.

## 2. Register the resource providers

Azure registers resource providers per subscription, and a subscription that has never run AKS may not have them yet. Providers that are already registered are left as they are.

```bash
for provider in Microsoft.ContainerService Microsoft.ContainerRegistry \
                Microsoft.KeyVault Microsoft.Storage Microsoft.Network \
                Microsoft.OperationalInsights Microsoft.Insights \
                Microsoft.ManagedIdentity Microsoft.Monitor; do
  az provider register --namespace "$provider" --wait
done
```

## 3. Create the resource group and network

The node subnet has a `Microsoft.Storage` service endpoint, so the cluster reaches the storage account over the Azure network rather than through its outbound address. Pods and services get addresses from ranges outside the virtual network.

```bash
az group create --name "$AZURE_RESOURCE_GROUP_NAME" --location "$AZURE_LOCATION" \
  --tags "cluster-name=$AZURE_CLUSTER_NAME" union-component=selfserve-dataplane

az network vnet create --resource-group "$AZURE_RESOURCE_GROUP_NAME" --name "$AZURE_VNET_NAME" \
  --location "$AZURE_LOCATION" --address-prefixes 10.232.0.0/16 \
  --tags "cluster-name=$AZURE_CLUSTER_NAME" union-component=selfserve-dataplane

az network vnet subnet create --resource-group "$AZURE_RESOURCE_GROUP_NAME" --vnet-name "$AZURE_VNET_NAME" \
  --name "$AZURE_NODE_SUBNET_NAME" --address-prefixes 10.232.0.0/20 \
  --service-endpoints Microsoft.Storage

export AZURE_NODE_SUBNET_ID="$(az network vnet subnet show --resource-group "$AZURE_RESOURCE_GROUP_NAME" \
  --vnet-name "$AZURE_VNET_NAME" --name "$AZURE_NODE_SUBNET_NAME" --query id -o tsv)"
```

## 4. Create the storage account and container

The storage account stores workflow metadata, task inputs and outputs, and fast-registration code bundles, in one `metadata` container. Union.ai uses the container for both metadata and fast registration, so you do not need a second one.

The account has the hierarchical namespace that Data Lake Storage Gen2 needs. Shared-key access is off, so the data plane reaches the account only through Workload Identity, and holds no storage key.

```bash
az storage account create --resource-group "$AZURE_RESOURCE_GROUP_NAME" --name "$AZURE_STORAGE_ACCOUNT_NAME" \
  --location "$AZURE_LOCATION" --kind StorageV2 --sku Standard_LRS \
  --enable-hierarchical-namespace true --allow-shared-key-access false \
  --allow-blob-public-access false --min-tls-version TLS1_2 \
  --https-only true --default-action Allow --bypass AzureServices \
  --tags "cluster-name=$AZURE_CLUSTER_NAME" union-component=selfserve-dataplane

az storage account network-rule add --resource-group "$AZURE_RESOURCE_GROUP_NAME" \
  --account-name "$AZURE_STORAGE_ACCOUNT_NAME" --subnet "$AZURE_NODE_SUBNET_ID"

# This command uses the management API, so it needs no storage account key.
az storage container-rm create --resource-group "$AZURE_RESOURCE_GROUP_NAME" \
  --storage-account "$AZURE_STORAGE_ACCOUNT_NAME" --name metadata --public-access off

export AZURE_STORAGE_ACCOUNT_ID="$(az storage account show --resource-group "$AZURE_RESOURCE_GROUP_NAME" \
  --name "$AZURE_STORAGE_ACCOUNT_NAME" --query id -o tsv)"
```

Add a CORS rule to the account. The Union.ai UI downloads code and artifacts straight from the storage account with presigned URLs, and the browser refuses them without a rule that names the UI's origin.

```bash
az storage account blob-service-properties cors-rule add \
  --resource-group "$AZURE_RESOURCE_GROUP_NAME" --account-name "$AZURE_STORAGE_ACCOUNT_NAME" \
  --allowed-origins "$UNION_UI_ORIGIN" \
  --allowed-methods GET PUT POST DELETE HEAD OPTIONS \
  --allowed-headers '*' --exposed-headers '*' --max-age 3600
```

Azure matches an origin exactly. Unlike S3, it does not accept a wildcard subdomain such as `https://*.unionai.cloud`, so the rule must name the UI's exact origin.

Because shared-key access is off, `az storage` commands that read the account's contents need `--auth-mode login`, for example `az storage blob list --account-name "$AZURE_STORAGE_ACCOUNT_NAME" --container-name metadata --auth-mode login`.

## 5. Create the container registry and Key Vault

The registry is where image-building tasks push images and where the cluster pulls them from. The Key Vault is where the data plane keeps runtime secrets, and uses Azure RBAC for access.

```bash
az acr create --resource-group "$AZURE_RESOURCE_GROUP_NAME" --name "$AZURE_CONTAINER_REGISTRY_NAME" \
  --location "$AZURE_LOCATION" --sku Standard --admin-enabled false \
  --role-assignment-mode rbac \
  --tags "cluster-name=$AZURE_CLUSTER_NAME" union-component=selfserve-dataplane

az keyvault create --resource-group "$AZURE_RESOURCE_GROUP_NAME" --name "$AZURE_KEY_VAULT_NAME" \
  --location "$AZURE_LOCATION" --sku standard --retention-days 7 \
  --enable-rbac-authorization true --enable-purge-protection true \
  --tags "cluster-name=$AZURE_CLUSTER_NAME" union-component=selfserve-dataplane

export AZURE_CONTAINER_REGISTRY_ID="$(az acr show --resource-group "$AZURE_RESOURCE_GROUP_NAME" \
  --name "$AZURE_CONTAINER_REGISTRY_NAME" --query id -o tsv)"
export AZURE_KEY_VAULT_ID="$(az keyvault show --resource-group "$AZURE_RESOURCE_GROUP_NAME" \
  --name "$AZURE_KEY_VAULT_NAME" --query id -o tsv)"
```

If `az keyvault create` reports that the name is already in use, another vault has it, possibly a deleted one that Azure still holds. Set `AZURE_KEY_VAULT_NAME` to another name, of 3 to 24 letters, digits, and single hyphens, and run the step again.

The vault starts empty. The data plane writes its runtime secrets into it once it is installed.

## 6. Create the managed identities and Log Analytics workspace

Create one managed identity for Union.ai's system pods and one for your task pods, and a workspace that keeps container logs for 30 days.

```bash
az identity create --resource-group "$AZURE_RESOURCE_GROUP_NAME" --name "$AZURE_SYSTEM_IDENTITY_NAME" \
  --location "$AZURE_LOCATION" \
  --tags "cluster-name=$AZURE_CLUSTER_NAME" union-component=selfserve-dataplane

az identity create --resource-group "$AZURE_RESOURCE_GROUP_NAME" --name "$AZURE_TASK_IDENTITY_NAME" \
  --location "$AZURE_LOCATION" \
  --tags "cluster-name=$AZURE_CLUSTER_NAME" union-component=selfserve-dataplane

export AZURE_SYSTEM_CLIENT_ID="$(az identity show --resource-group "$AZURE_RESOURCE_GROUP_NAME" \
  --name "$AZURE_SYSTEM_IDENTITY_NAME" --query clientId -o tsv)"
export AZURE_SYSTEM_PRINCIPAL_ID="$(az identity show --resource-group "$AZURE_RESOURCE_GROUP_NAME" \
  --name "$AZURE_SYSTEM_IDENTITY_NAME" --query principalId -o tsv)"
export AZURE_TASK_CLIENT_ID="$(az identity show --resource-group "$AZURE_RESOURCE_GROUP_NAME" \
  --name "$AZURE_TASK_IDENTITY_NAME" --query clientId -o tsv)"
export AZURE_TASK_PRINCIPAL_ID="$(az identity show --resource-group "$AZURE_RESOURCE_GROUP_NAME" \
  --name "$AZURE_TASK_IDENTITY_NAME" --query principalId -o tsv)"

az monitor log-analytics workspace create --resource-group "$AZURE_RESOURCE_GROUP_NAME" \
  --workspace-name "$AZURE_LOG_ANALYTICS_WORKSPACE_NAME" --location "$AZURE_LOCATION" \
  --sku PerGB2018 --retention-time 30 \
  --tags "cluster-name=$AZURE_CLUSTER_NAME" union-component=selfserve-dataplane

export AZURE_LOG_ANALYTICS_WORKSPACE_ID="$(az monitor log-analytics workspace show \
  --resource-group "$AZURE_RESOURCE_GROUP_NAME" --workspace-name "$AZURE_LOG_ANALYTICS_WORKSPACE_NAME" \
  --query id -o tsv)"
```

Each managed identity has two IDs. The **client ID** is what you enter in the Union.ai UI. The **principal ID**, also called the object ID, is what role assignments use, in [step 9](#9-grant-access). Both are GUIDs, so they are easy to swap: an identity given the wrong one authenticates as nothing, with no error until the first storage read.

## 7. Create the AKS cluster

The cluster has the OIDC issuer and Workload Identity turned on, which the federated credentials in [step 8](#8-federate-the-identities-to-the-kubernetes-service-accounts) rely on. It has one node pool of 2 to 10 `Standard_D4s_v5` nodes with 200 GiB OS disks. The image builder requests 50 GiB of ephemeral storage, which comes from the OS disk, so on smaller disks image builds stay pending and never run.

The Container Insights add-on sends the logs of every namespace to the Log Analytics workspace. Enabling it also creates the data collection rule it needs.

```bash
cat > "$AZURE_WORK_DIR/data-collection-settings.json" <<'JSON'
{
  "interval": "1m",
  "namespaceFilteringMode": "Off",
  "enableContainerLogV2": true,
  "streams": ["Microsoft-ContainerInsights-Group-Default"]
}
JSON

az aks create --resource-group "$AZURE_RESOURCE_GROUP_NAME" --name "$AZURE_CLUSTER_NAME" \
  --location "$AZURE_LOCATION" --dns-name-prefix "$AZURE_CLUSTER_NAME" \
  --enable-managed-identity --enable-oidc-issuer --enable-workload-identity \
  --nodepool-name default --node-count 2 --node-vm-size Standard_D4s_v5 \
  --node-osdisk-type Managed --node-osdisk-size 200 \
  --enable-cluster-autoscaler --min-count 2 --max-count 10 \
  --node-provisioning-mode Manual \
  --vnet-subnet-id "$AZURE_NODE_SUBNET_ID" \
  --network-plugin azure --network-plugin-mode overlay \
  --pod-cidr 10.244.0.0/16 --service-cidr 10.0.0.0/19 \
  --dns-service-ip 10.0.0.10 \
  --load-balancer-sku standard --outbound-type loadBalancer \
  --enable-addons monitoring --workspace-resource-id "$AZURE_LOG_ANALYTICS_WORKSPACE_ID" \
  --enable-msi-auth-for-monitoring \
  --data-collection-settings "$AZURE_WORK_DIR/data-collection-settings.json" \
  --generate-ssh-keys \
  --tags "cluster-name=$AZURE_CLUSTER_NAME" union-component=selfserve-dataplane

export AZURE_CLUSTER_ID="$(az aks show --resource-group "$AZURE_RESOURCE_GROUP_NAME" \
  --name "$AZURE_CLUSTER_NAME" --query id -o tsv)"
export AZURE_OIDC_ISSUER_URL="$(az aks show --resource-group "$AZURE_RESOURCE_GROUP_NAME" \
  --name "$AZURE_CLUSTER_NAME" --query oidcIssuerProfile.issuerUrl -o tsv)"
export AZURE_KUBELET_PRINCIPAL_ID="$(az aks show --resource-group "$AZURE_RESOURCE_GROUP_NAME" \
  --name "$AZURE_CLUSTER_NAME" --query identityProfile.kubeletidentity.objectId -o tsv)"
```

Check that `AZURE_OIDC_ISSUER_URL` and `AZURE_KUBELET_PRINCIPAL_ID` are not empty:

```bash
printf 'OIDC issuer: %s\nKubelet principal: %s\n' "$AZURE_OIDC_ISSUER_URL" "$AZURE_KUBELET_PRINCIPAL_ID"
```

## 8. Federate the identities to the Kubernetes service accounts

Each federated credential trusts one Kubernetes service account in one namespace:

- The system identity trusts `union-system`, the service account Union.ai's system pods run as.
- The task identity trusts `union`, the service account task pods run as, and `default`, so that a pod created without a service account still gets an identity.

```bash
az identity federated-credential create --resource-group "$AZURE_RESOURCE_GROUP_NAME" \
  --identity-name "$AZURE_SYSTEM_IDENTITY_NAME" \
  --name "${AZURE_CLUSTER_NAME}-system-${UNION_DATAPLANE_NAMESPACE}-union-system" \
  --issuer "$AZURE_OIDC_ISSUER_URL" \
  --subject "system:serviceaccount:${UNION_DATAPLANE_NAMESPACE}:union-system" \
  --audiences api://AzureADTokenExchange

az identity federated-credential create --resource-group "$AZURE_RESOURCE_GROUP_NAME" \
  --identity-name "$AZURE_TASK_IDENTITY_NAME" \
  --name "${AZURE_CLUSTER_NAME}-task-${UNION_DATAPLANE_NAMESPACE}-union" \
  --issuer "$AZURE_OIDC_ISSUER_URL" \
  --subject "system:serviceaccount:${UNION_DATAPLANE_NAMESPACE}:union" \
  --audiences api://AzureADTokenExchange

az identity federated-credential create --resource-group "$AZURE_RESOURCE_GROUP_NAME" \
  --identity-name "$AZURE_TASK_IDENTITY_NAME" \
  --name "${AZURE_CLUSTER_NAME}-task-${UNION_DATAPLANE_NAMESPACE}-default" \
  --issuer "$AZURE_OIDC_ISSUER_URL" \
  --subject "system:serviceaccount:${UNION_DATAPLANE_NAMESPACE}:default" \
  --audiences api://AzureADTokenExchange
```

## 9. Grant access

Assign the roles each identity needs:

| Identity | Roles | For |
|---|---|---|
| System | Storage Blob Data Contributor, Key Vault Secrets Officer, AcrPull, Log Analytics Reader | Reading and writing the container, managing runtime secrets, pulling images, and reading task logs back for the Union.ai UI |
| Task | Storage Blob Data Contributor, Key Vault Secrets User, AcrPush | Reading and writing the container, reading runtime secrets, and pushing the images Union.ai builds |
| AKS kubelet | AcrPull, Monitoring Metrics Publisher | Pulling images onto the nodes, and publishing metrics |

```bash
# New managed identities are service principals. Naming the principal type
# avoids role-assignment failures while Microsoft Entra ID replicates them.
assign_service_role() {
  az role assignment create --assignee-object-id "$1" \
    --assignee-principal-type ServicePrincipal --role "$2" --scope "$3" \
    --output none
}

assign_service_role "$AZURE_SYSTEM_PRINCIPAL_ID" "Storage Blob Data Contributor" "$AZURE_STORAGE_ACCOUNT_ID"
assign_service_role "$AZURE_TASK_PRINCIPAL_ID" "Storage Blob Data Contributor" "$AZURE_STORAGE_ACCOUNT_ID"
assign_service_role "$AZURE_SYSTEM_PRINCIPAL_ID" "Key Vault Secrets Officer" "$AZURE_KEY_VAULT_ID"
assign_service_role "$AZURE_TASK_PRINCIPAL_ID" "Key Vault Secrets User" "$AZURE_KEY_VAULT_ID"
assign_service_role "$AZURE_TASK_PRINCIPAL_ID" "AcrPush" "$AZURE_CONTAINER_REGISTRY_ID"
assign_service_role "$AZURE_SYSTEM_PRINCIPAL_ID" "AcrPull" "$AZURE_CONTAINER_REGISTRY_ID"
assign_service_role "$AZURE_KUBELET_PRINCIPAL_ID" "AcrPull" "$AZURE_CONTAINER_REGISTRY_ID"
assign_service_role "$AZURE_KUBELET_PRINCIPAL_ID" "Monitoring Metrics Publisher" "$AZURE_CLUSTER_ID"
assign_service_role "$AZURE_SYSTEM_PRINCIPAL_ID" "Log Analytics Reader" "$AZURE_LOG_ANALYTICS_WORKSPACE_ID"
```

Optionally, give your own account access to the container and the vault, so you can inspect them. Creating a storage account or a vault grants its creator no access to the data in it.

```bash
export AZURE_SIGNED_IN_USER_OBJECT_ID="$(az ad signed-in-user show --query id -o tsv)"

az role assignment create --assignee-object-id "$AZURE_SIGNED_IN_USER_OBJECT_ID" \
  --assignee-principal-type User --role "Storage Blob Data Contributor" \
  --scope "$AZURE_STORAGE_ACCOUNT_ID" --output none

az role assignment create --assignee-object-id "$AZURE_SIGNED_IN_USER_OBJECT_ID" \
  --assignee-principal-type User --role "Key Vault Secrets Officer" \
  --scope "$AZURE_KEY_VAULT_ID" --output none
```

Role assignments can take a few minutes to take effect.

## 10. Check the resources and collect the values

Configure `kubectl`, and check the cluster, the storage account, and the federated credentials:

```bash
az aks get-credentials --resource-group "$AZURE_RESOURCE_GROUP_NAME" --name "$AZURE_CLUSTER_NAME" \
  --subscription "$AZURE_SUBSCRIPTION_ID"
kubectl get nodes

az storage account show --resource-group "$AZURE_RESOURCE_GROUP_NAME" --name "$AZURE_STORAGE_ACCOUNT_NAME" \
  --query '{hns:isHnsEnabled,sharedKeys:allowSharedKeyAccess,publicBlobs:allowBlobPublicAccess}'
az storage container-rm show --resource-group "$AZURE_RESOURCE_GROUP_NAME" \
  --storage-account "$AZURE_STORAGE_ACCOUNT_NAME" --name metadata --query name -o tsv
az identity federated-credential list --resource-group "$AZURE_RESOURCE_GROUP_NAME" \
  --identity-name "$AZURE_SYSTEM_IDENTITY_NAME" --query '[].subject' -o tsv
az identity federated-credential list --resource-group "$AZURE_RESOURCE_GROUP_NAME" \
  --identity-name "$AZURE_TASK_IDENTITY_NAME" --query '[].subject' -o tsv
```

Check that the nodes are `Ready`, that the storage account shows `hns` as `true` and both `sharedKeys` and `publicBlobs` as `false`, and that the subjects all name the namespace you chose in step 1.

Print the values you enter in the Union.ai UI, labeled with the fields they go in:

```bash
export UNION_STORAGE_URI="abfs://metadata@${AZURE_STORAGE_ACCOUNT_NAME}.dfs.core.windows.net"
export UNION_KEY_VAULT_URI="$(az keyvault show --resource-group "$AZURE_RESOURCE_GROUP_NAME" \
  --name "$AZURE_KEY_VAULT_NAME" --query properties.vaultUri -o tsv)"
export UNION_IMAGE_REGISTRY="$(az acr show --resource-group "$AZURE_RESOURCE_GROUP_NAME" \
  --name "$AZURE_CONTAINER_REGISTRY_NAME" --query loginServer -o tsv)"

printf '%s\n' \
  "Cluster pool form (Azure):" \
  "  Storage container          = $UNION_STORAGE_URI" \
  "  Key Vault URI              = $UNION_KEY_VAULT_URI" \
  "  Image registry             = $UNION_IMAGE_REGISTRY" \
  "Register cluster dialog:" \
  "  Namespace                  = $UNION_DATAPLANE_NAMESPACE" \
  "  Subscription ID            = $AZURE_SUBSCRIPTION_ID" \
  "  Tenant ID                  = $AZURE_TENANT_ID" \
  "  Resource group             = $AZURE_RESOURCE_GROUP_NAME" \
  "  System client ID           = $AZURE_SYSTEM_CLIENT_ID" \
  "  Task client ID             = $AZURE_TASK_CLIENT_ID" \
  "  Log Analytics workspace ID = $AZURE_LOG_ANALYTICS_WORKSPACE_ID"
```

Keep this output, and keep the shell where `kubectl` can reach the cluster: you run the agent install from it.

## 11. Connect your cluster

1. In the Union.ai UI, select **Connect your cluster**, on the home page or in the sidebar. If your organization has no cluster pool yet, select **Create cluster pool**.
2. Select **Azure**, and fill in the form:

   | Field | Value |
   |---|---|
   | **Storage container** | The container's Data Lake Storage URI, in the form `abfs://metadata@<storage-account>.dfs.core.windows.net`, with no path after it |
   | **Key Vault URI** | The vault's URI, in the form `https://<vault-name>.vault.azure.net/` |
   | **Image registry** | The registry's login server, in the form `<registry-name>.azurecr.io`. You do not need a repository path: Union.ai adds its own. |

   Your first pool is always named `default`, so the **Pool name** field is already filled in. Select **Create cluster pool**.

3. When the pool is created, the dialog moves on to **Register a cluster**, with the new pool already selected. Fill in:

   | Field | Value |
   |---|---|
   | **Name** | A name for the cluster in Union.ai, for example `my-cluster`. You cannot change it once the cluster is registered. |
   | **Cluster pool** | Already set to the pool you just created. |
   | **Namespace** | Exactly the namespace from step 1. If you kept `union`, you can also leave the field empty. |
   | **Subscription ID** | The subscription the AKS cluster is in |
   | **Tenant ID** | The Microsoft Entra ID tenant the subscription belongs to |
   | **Resource group** | The resource group the AKS cluster is in. Union.ai uses it to link to your task logs in the Azure portal. |
   | **System client ID** | The system identity's client ID, not its principal ID |
   | **Task client ID** | The task identity's client ID, not its principal ID |
   | **Log Analytics workspace ID (optional)** | The workspace's resource ID, which starts with `/subscriptions/`. Without it, the Union.ai UI shows task logs only while the pods exist. |

4. Select **Register cluster**. The cluster's page, **Install Union on your Azure cluster**, shows the install command for this cluster.

Install the agent and wait for the data plane as described in steps 3 and 4 of [Connect your cluster](./connect-a-cluster#3-install-the-agent).

Once the data plane is installed, check that its service accounts carry the right client IDs:

```bash
kubectl -n "$UNION_DATAPLANE_NAMESPACE" get sa union-system union \
  -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.metadata.annotations.azure\.workload\.identity/client-id}{"\n"}{end}'
```

`union-system` must show `AZURE_SYSTEM_CLIENT_ID`, and `union` must show `AZURE_TASK_CLIENT_ID`. If the namespace has no such service accounts, the data plane was installed into a different namespace from the one the federated credentials trust.

## Important behavior and cleanup

- The federated credentials trust one namespace. To install the data plane into another namespace, create federated credentials for that namespace first.
- The pool uses one container for both metadata and fast registration. Do not create or configure a second one.
- The cluster has one on-demand node pool, and no GPUs. Tasks that request interruptible capacity stay pending until you add a Spot node pool, for example with `az aks nodepool add --priority Spot`.
- This guide does not set data-retention or image-cleanup policies. Add a storage lifecycle management policy and registry cleanup before production use.
- To remove the environment, review the resource group's contents, then delete the group with `az group delete --name "$AZURE_RESOURCE_GROUP_NAME"`. That removes everything this page created, including the role assignments on those resources. The Key Vault has purge protection, so after deletion Azure keeps it in a deleted state, and its name stays reserved for the 7-day retention period. The resource providers stay registered.

## Next steps

**[Run a workload on the cluster](./connect-a-cluster#5-run-a-workload-on-the-cluster).** Once the cluster shows as **Healthy**, run a workflow on it.
