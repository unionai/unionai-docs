---
title: Enabling Azure Container Registry (ACR)
weight: 2
variants: -flyte -serverless +byoc -selfmanaged
---

# Enabling Azure Container Registry (ACR)

ACR can be used to store container images within Azure and accessed within your Azure-based Data Plane.

{{< key product_name >}} leverages Azure Kubernetes Service (AKS) managed identities to authenticate with ACR.

Refer to [Azure documentation for more details](https://learn.microsoft.com/en-us/azure/container-registry/authenticate-kubernetes-options)

## Creating a container registry

### Creating a container registry outside of {{< key product_name >}}

ACR instances that allow anonymous (I.E., public) access doesn't require additional configuration. Otherwise, the underlying AKS cluster must be granted permissions to pull from the container registry.

Private ACR for {{< key product_name >}} images is only supported for ACRs within the same tenant as the {{< key product_name >}} data plane. Refer to [Azure documentation](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-portal?tabs=azure-cli) for creating Container Registries.

### Creating a {{< key product_name >}}-managed container registry

Upon request, {{< key product_name >}} can create a container registry within your data plane.

By default this {{< key product_name >}}-managed ACR instance:

* Will be created within the same subscription and resource group of the Azure Kubernetes cluster instance.
* {{< key product_name >}} will create necessary permissions for the Azure Kubernetes cluster to pull images from the container registry.
* Container registry will be created with **Basic** service tier.
* In order to mitigate excessive storage costs, {{< key product_name >}} creates a weekly [scheduled container registry task](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-tasks-scheduled) to [purge](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-auto-purge#use-the-purge-command) **all** images with last modified dates older then 7 days. As a symptom, some 7 day old images will be rebuilt.

Upon request, {{< key product_name >}} can:

* Configure the [Container Registry service tier](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-skus).
* Disable the purge task to prevent automated image delettion.
* Configure the purge task to run daily, weekly, and monthly deleting tasks with last modified dates older then 1, 7, and 30 days respectively.
* Configure a [regexp2 with RE2 compatiblity](https://github.com/dlclark/regexp2) regular expression to filter for which repository to purge. For example, `^(?!keep-repo).*` will keep all images with repositories prefixed with keep-repo, E.G., `<CONTAINER_REGISTRY_NAME>/keep-repo/my-image:my-tag>`.

{{< key product_name >}} will provide the created container registry Name and Login server for Docker authentication.

## Enable access to ACR in a different subscription within the same Azure tenant

{{< key product_name >}} data plane resources will require permissions to pull images from your container registry.

### Allow {{< key product_name >}} to manage permissions

The simplest, most flexible approach is to provide {{< key product_name >}} the ability to add roles assignments against the container registry. [Create a role assignment](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal) to allow {{< key product_name >}} to assign roles to the container registry. These permissions should be scoped to the target container registry. Follow these steps to set up the required access:

1. Navigate to the Azure portal and locate the target container registry.
2. In the container registry's access control (IAM) section, create a new role assignment.
3. For the 'Assigned to' field, select the {{< key product_name >}} application's service principal.
4. For the 'Role' field, you have two options:
    * Simplest approach: Assign the built-in Azure role `User Access Administrator`.
    * Advanced approach: Create a custom role with the following specific permissions:
      * `Microsoft.Authorization/roleAssignments/write`
      * `Microsoft.Authorization/roleAssignments/delete`
      * `Microsoft.Authorization/roleAssignments/read`
      * `Microsoft.Authorization/roleDefinitions/read`
5. Ensure the 'Scope' is set to the target container registry.
6. Complete the role assignment process.
7. Provide the container registry [resource ID](https://learn.microsoft.com/en-us/dotnet/api/microsoft.azure.management.storage.models.resource.id) to {{< key product_name >}} support.

### Manage permissions directly

Managing permissions directly is required if it is not desirable to grant role assigning permissions to {{< key product_name >}}. [Create a role assignment](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal) assigning the `AcrPull` role to the underlying AKS cluster kubelet service principal ID. The service principal ID can be provided by {{< key product_name >}} support.

Note, this process needs to be repeated every time the underlying Kubernetes cluster is changed or a new cluster is added.

## Enable access to ACR in a different Azure tenant

Please contact and work directly with {{< key product_name >}} support.

## References

* [Azure - Authenticate with Azure Container Registry (ACR) from Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/cluster-container-registry-integration?toc=%2Fazure%2Fcontainer-registry%2Ftoc.json&bc=%2Fazure%2Fcontainer-registry%2Fbreadcrumb%2Ftoc.json&tabs=azure-cli)
* [Azure - Pull images from a container registry to an AKS cluster in a different Microsoft Entra tenant](https://learn.microsoft.com/en-us/azure/container-registry/authenticate-aks-cross-tenant)
