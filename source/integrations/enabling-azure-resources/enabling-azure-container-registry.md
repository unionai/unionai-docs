# Enabling Azure Container Registry (ACR)

Union leverages Azure Kubernetes Service (AKS) managed identities to authentication to ACR.
The following instructions apply if ACR is configured to disallow anonomous access.

Refer to [Azure documentation for more details](https://learn.microsoft.com/en-us/azure/container-registry/authenticate-kubernetes-options)

## Setting up a container registry

### Union managed ACR

Union, by default, will create a container registry for image storage.

By default this ACR instance:

* Will be created within the same Subscription and Resource group of the Azure Kubernetes Cluster instance.
* Union will create necessary permissions for the Azure Kubernetes Cluster to pull images from the container registry.
* Container registry will be created with "Basic" service tier.
* In order to mitigate excessive storage costs, Union creates a weekly [scheduled container registry task](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-tasks-scheduled) to [purge](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-auto-purge#use-the-purge-command) **all** images with last modified dates older then 7 days. As a symptom, some 7 day old images will be rebuilt.z

Upon request, Union can:

* Not create a ACR instance.
* Configure the [Container Registry service tier](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-skus).
* Configure the purge task to run daily, weekly, and monthly deleting tasks with last modified dates older then 1, 7, and 30 days respectively.
* Configure a [regexp2 with RE2 compatiblity](https://github.com/dlclark/regexp2) regular expression to filter for which repository to purge. For example, `^(?!keep-repo).*` will keep all images with repositories prefixed with keep-repo, E.G., `<CONTAINER_REGISTRY_NAME/keep-repo/my-image:my-tag>`.

Union will provide the created container registry Name and Login server for Docker authentication.

### BYO-ACR

Private ACR for Union images is only supported for ACRs within the same tenant as the Union dataplane. Refer to [Azure documenation](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-portal?tabs=azure-cli) for creating Container Registries.

If you are using ACR, you will need to provide pull access to the underlying Kubernetes cluster within your Union dataplane. Union will provide you the Kubernetes service principal ID. Use [Azure Role Assignment](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal) to assign `AcrPull` role to Kubernetes service principal provided by Union.

## Enable access to ACR within the same Azure Subscription

Given Union was [setup with appropriate permissions](../../data-plane-setup/data-plane-setup-on-azure.md), Union can create and manage the permissions required to provide the dataplane's AKS cluster.Provide your ACR container ID to Union Support if Union managed permissions is desired. Otherwise refer to [Enable access to ACR within the same Azure Tenant but different Azure Subscription](#enable-access-to-acr-within-the-same-azure-tenant-but-different-azure-subscription)

## Enable access to ACR within the same Azure Tenant but different Azure Subscription

Union will not have permissions to assign roles to AKS managed identities scoped to the ACR instance unless special permission accomodations have been made. This will require you to add `AcrPull` permissions for the AKS service principal object id provided by Union.

## Enable access to ACR in a different Azure Tenant

Please contact Union support and work directly.

## References

* [Azure - Authenticate with Azure Container Registry (ACR) from Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/cluster-container-registry-integration?toc=%2Fazure%2Fcontainer-registry%2Ftoc.json&bc=%2Fazure%2Fcontainer-registry%2Fbreadcrumb%2Ftoc.json&tabs=azure-cli)
* [Azure - Pull images from a container registry to an AKS cluster in a different Microsoft Entra tenant](https://learn.microsoft.com/en-us/azure/container-registry/authenticate-aks-cross-tenant)
