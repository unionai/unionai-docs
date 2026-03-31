---
title: Data plane setup on Azure
weight: 5
variants: -flyte -byoc +selfmanaged
---

# Data plane setup on Azure

{{< key product_name >}}'s modular architecture allows for great flexibility and control.
The customer can decide how many clusters to have, their shape, and who has access to what.
All communication is encrypted.  The Union architecture is described on the [Architecture](./architecture/_index) page.

## Azure Blob Storage

Each data plane uses Azure Blob Storage containers to store data used in workflow execution.
Union recommends the use of two containers within a Storage Account:

1. **Metadata container**: contains workflow execution data such as task inputs and outputs.
2. **Fast registration container**: contains local code artifacts copied into the Flyte task container at runtime when using `union register` or `union run --remote --copy-all`.

You can also choose to use a single container.

Create an [Azure Storage Account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create) with Blob containers for your data plane.

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
  --account-name <STORAGE_ACCOUNT_NAME>
```

For more details, see the [Azure Storage CORS documentation](https://learn.microsoft.com/en-us/rest/api/storageservices/cross-origin-resource-sharing--cors--support-for-the-azure-storage-services).

### Data Retention

Union recommends using lifecycle management policies on your Storage Account to manage storage costs. See [Data retention policy](./configuration/data-retention) for more information.

## Azure Container Registry

Create an [Azure Container Registry](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-portal) for Image Builder to push and pull container images. Note the registry login server (e.g. `<REGISTRY_NAME>.azurecr.io`) — you will reference it when configuring Workload Identity permissions below.

## Workload Identity

Union recommends using [Microsoft Entra Workload ID](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview) to securely access Azure resources.

Ensure your AKS cluster is [enabled as OIDC Issuer](https://learn.microsoft.com/en-us/azure/aks/use-oidc-issuer).

Create a User Assigned Managed Identity with a Federated Credential that maps to the `union-system` Kubernetes service account:

**Subject Identifier**

- `system:serviceaccount:<NAMESPACE>:union-system`

Where `<NAMESPACE>` is where you plan to install the Union operator (`union` by default).

Assign the following roles to this Identity:

- `Storage Blob Data Owner` at the Storage Account level
- `AcrPush` on the Azure Container Registry used by Image Builder

Annotate the `union-system` service account with the managed identity client ID in your Helm values:

```yaml
commonServiceAccount:
  annotations:
    azure.workload.identity/client-id: "<MANAGED_IDENTITY_CLIENT_ID>"
```

### Workers

This is the Identity that the Pods created for each execution will use to access Azure resources. Those Pods use the `default` K8s Service Account on each project-domain namespace, unless otherwise specified.

Create a User Assigned Managed Identity with Federated Credentials that map to the `default` K8s Service Account:

**Subject Identifier**

- `system:serviceaccount:development:default`
- `system:serviceaccount:staging:default`
- `system:serviceaccount:production:default`

Assign the `Storage Blob Data Owner` role to this Identity at the Storage Account level.

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

## AKS Configuration

By default, the Union installation requests the following resources:

|          | CPU (vCPUs)| Memory (GiB) |
|----------|------------|--------------|
| Requests |          14|          27.1|
| Limits   |          17|            32|

For GPU access, Union injects tolerations and label selectors to execution Pods.

## Assumptions

* You have a {{< key product_name >}} organization, and you know the control plane URL for your organization.
* You have a cluster name provided by or coordinated with Union.
* You have a Kubernetes cluster, running one of the most recent three minor K8s versions.
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
