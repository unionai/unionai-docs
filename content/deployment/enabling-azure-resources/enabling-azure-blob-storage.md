---
title: Enabling Azure Blob Storage
weight: 1
variants: -flyte -serverless +byoc -selfmanaged
---

# Enabling Azure Blob Storage

For {{< key product_name >}} customers whose data plane is in Azure, we walk through setting up access to your own Azure Blob Storage container.

> [!NOTE] Azure Blob Storage in the {{< key product_name >}} environment
> Your data plane is set up with a Kubernetes cluster and other resources.
> Among these are a number of Azure Storage containers used internally by the {{< key product_name >}} operator running in the cluster (see [Platform architecture](../platform-architecture)) to store things like workflow metadata.
>
> **These are not the Azure Blob Storage containers we are talking about in this section.**
>
> **We are discussing the case where you have **_**your own Azure Blob Storage container**_**that you set up to store input and output data used by your workflows.**

## Providing permissions to Azure Blob Storage container

{{< key product_name >}} data plane tasks employ Azure Workload Identity Federation to access Azure resources using an Azure user-assigned identity. Access to Azure Blob Storage containers requires updating permissions to permit this {{< key product_name >}}-managed user-assigned identity.

### {{< key product_name >}}-managed permissions

The simplest, most flexible approach is to provide {{< key product_name >}} the ability to add roles assignments against the blob storage container. [Create a role assignment](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal) to allow {{< key product_name >}} to assign roles to the blob storage container. These permissions should be scoped to the target container. Follow these steps to set up the required access:

1. Navigate to the Azure portal and locate the target storage container.
2. In the storage container's access control (IAM) section, create a new role assignment.
3. For the 'Assigned to' field, select the {{< key product_name >}} application's service principal.
4. For the 'Role' field, you have two options:
  * Simplest approach: Assign the built-in Azure role `User Access Administrator`.
  * Advanced approach: Create a custom role with the following specific permissions:
    * `Microsoft.Authorization/roleAssignments/write`
    * `Microsoft.Authorization/roleAssignments/delete`
    * `Microsoft.Authorization/roleAssignments/read`
    * `Microsoft.Authorization/roleDefinitions/read`
5. Ensure the 'Scope' is set to the target blob storage container.
6. Complete the role assignment process.
7. Provide the blob storage container [resource ID](https://learn.microsoft.com/en-us/dotnet/api/microsoft.azure.management.storage.models.resource.id) to {{< key product_name >}} support.

### Manage permissions directly

Managing permissions directly is required if it is not desirable to grant role assigning permissions to {{< key product_name >}}. [Create a role assignment](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal)) assigning the `Storage Blob Data Contributor` role to the `userflyterole` user assigned identity scoped the blob storage container.

> [!NOTE] {{< key product_name >}} managed user-assigned identities
> Refer to [Azure portal&#39;s user assigned managed identitites](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.ManagedIdentity%2FuserAssignedIdentities) if assistance is required identifying the `userflyterole` user assigned managed identity within the same resource group as the {{< key product_name >}} data plane.
