# Enabling Azure Container Registry (ACR)

Union leverages Azure Kubernetes Service (AKS) managed identities to authentication to ACR.
The following instructions apply if ACR is configured to disallow anonomous access.

Refer to [Azure documentation for more details](https://learn.microsoft.com/en-us/azure/container-registry/authenticate-kubernetes-options)

## Setting up a container registry

Union requires that you setup your own ACR instance. ACR instances that allow anonoymous (I.E. public) acces don't require additional configuration. Otherwise, pull permissions need to be granted to the underlying AKS cluster.

Private ACR for Union images is only supported for ACRs within the same tenant as the Union dataplane. Refer to [Azure documenation](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-portal?tabs=azure-cli) for creating Container Registries.

## Enable access to ACR within the same Azure Subscription

Given Union was [setup with appropriate permissions](../../data-plane-setup/data-plane-setup-on-azure.md), Union can create and manage the permissions required to provide the dataplane's AKS cluster.Provide your ACR container ID to Union Support if Union managed permissions is desired. Otherwise refer to [Enable access to ACR within the same Azure Tenant but different Azure Subscription](#enable-access-to-acr-within-the-same-azure-tenant-but-different-azure-subscription)

## Enable access to ACR within the same Azure Tenant but different Azure Subscription

Union will not have permissions to assign roles to AKS managed identities scoped to the ACR instance unless special permission accomodations have been made. This will require you to use [Azure Role Assignment](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal) to assign `AcrPull` role to Kubernetes service principal provided by Union.

## Enable access to ACR in a different Azure Tenant

Please contact Union support and work directly.

## References

* [Azure - Authenticate with Azure Container Registry (ACR) from Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/cluster-container-registry-integration?toc=%2Fazure%2Fcontainer-registry%2Ftoc.json&bc=%2Fazure%2Fcontainer-registry%2Fbreadcrumb%2Ftoc.json&tabs=azure-cli)
* [Azure - Pull images from a container registry to an AKS cluster in a different Microsoft Entra tenant](https://learn.microsoft.com/en-us/azure/container-registry/authenticate-aks-cross-tenant)
