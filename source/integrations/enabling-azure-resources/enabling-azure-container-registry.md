# Enabling Azure Container Registry (ACR)

ACR can be used to store container images within Azure and accessed within your Azure-based Data Plane.

Union leverages Azure Kubernetes Service (AKS) managed identities to authenticate with ACR.

Refer to [Azure documentation for more details](https://learn.microsoft.com/en-us/azure/container-registry/authenticate-kubernetes-options)

## Creating a container registry

### Creating a container registry outside of Union

ACR instances that allow anonymous (I.E., public) access doesn't require additional configuration. Otherwise, the underlying AKS cluster must be granted permissions to pull from the container registry.

Private ACR for Union images is only supported for ACRs within the same tenant as the Union data plane. Refer to [Azure documentation](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-portal?tabs=azure-cli) for creating Container Registries.

### Using Union-managed container registry

Upon request, Union can create a container registry within your data plane.

By default this Union-managed ACR instance:

* Will be created within the same Subscription and Resource group of the Azure Kubernetes Cluster instance.
* Union will create necessary permissions for the Azure Kubernetes Cluster to pull images from the container registry.
* Container registry will be created with "Basic" service tier.
* In order to mitigate excessive storage costs, Union creates a weekly [scheduled container registry task](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-tasks-scheduled) to [purge](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-auto-purge#use-the-purge-command) **all** images with last modified dates older then 7 days. As a symptom, some 7 day old images will be rebuilt.

Upon request, Union can:

* Configure the [Container Registry service tier](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-skus).
* Disable the purge task to prevent automated image delettion.
* Configure the purge task to run daily, weekly, and monthly deleting tasks with last modified dates older then 1, 7, and 30 days respectively.
* Configure a [regexp2 with RE2 compatiblity](https://github.com/dlclark/regexp2) regular expression to filter for which repository to purge. For example, `^(?!keep-repo).*` will keep all images with repositories prefixed with keep-repo, E.G., `<CONTAINER_REGISTRY_NAME>/keep-repo/my-image:my-tag>`.

Union will provide the created container registry Name and Login server for Docker authentication.

## Enable access to ACR in a different subscription within the same Azure Tenant

Union data plane resources will require permissions to pull images from you ACR instance.

### Allow Union to manage permissions

The simplest, most flexible approach is to provide Union the ability to add roles assignments against the ACR instance.

Assign the union Entra app registration created during data plane setup the Azure provided role `User Access Administrator` or create a custom role, scoped to the ACR instance, with the following permissions:

* `Microsoft.Authorization/roleAssignments/write`
* `Microsoft.Authorization/roleAssignments/delete`
* `Microsoft.Authorization/roleAssignments/read`
* `Microsoft.Authorization/roleDefinitions/read`

With either approach, [creating a role assignment](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal) `scope`d to the ACR instance and granted to the union app.

Provide union the resource ID of the ACR instance.

### Manage permissions directly

Managing permissions directly is required if it is not desirable to grant role assigning permissions to Union.

Retrieve the underlying kubelet principal ID from Union. [Create a role assignment]((https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal)) assigning the `AcrPull` role to the provided principal ID.

Note, this process need to be done everytime the Underlying Kubernetes cluster is changed or new clusters are added.

## Enable access to ACR in a different Azure Tenant

Please contact and work directly with Union support.

## References

* [Azure - Authenticate with Azure Container Registry (ACR) from Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/cluster-container-registry-integration?toc=%2Fazure%2Fcontainer-registry%2Ftoc.json&bc=%2Fazure%2Fcontainer-registry%2Fbreadcrumb%2Ftoc.json&tabs=azure-cli)
* [Azure - Pull images from a container registry to an AKS cluster in a different Microsoft Entra tenant](https://learn.microsoft.com/en-us/azure/container-registry/authenticate-aks-cross-tenant)
