# Enabling Azure Blob Storage

For Union customers whose data plane is in Azure and have a Blob Storage Container within the same Azure tenant.

:::{admonition} Azure Blob Storage in the Union environment

Your data plane is set up with a Kubernetes cluster and other resources.
Among these are a number of Azure Storage contaiers used internally by the Union operator running in the cluster (see [Platform architecture](/platform-architecture)) to store things like workflow metadata.

**These are not the Azure Storage containers we are talking about in this section.**

**We are discussing the case where you have **_**your own Azure Storage Container**_**that you set up to store input and output data used by your workflows.**

:::

## Providing permissions to Azure Blob Storage container

Union data plane tasks utilizes Azure Workload Identity Federation to access Azure resources as an Azure user assigned identity. Access Azure Blob Storage containers requires updating permissions to permit this Union managed user assigned identity.

### Union managed permissions

The simplest, most flexible approach is to provide Union the ability to add roles assignments against the Azure storage account or storage container.

Assign the union Entra app registration created during data plane setup the Azure provided role `User Access Administrator` or create a custom role, scoped to the ACR instance, with the following permissions:

* `Microsoft.Authorization/roleAssignments/write`
* `Microsoft.Authorization/roleAssignments/delete`
* `Microsoft.Authorization/roleAssignments/read`
* `Microsoft.Authorization/roleDefinitions/read`

With either approach, [creating a role assignment](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal) `scope`d to the storage account or storage container. Assign the union app as member / principal of the role assignment.

Provide blob storage container resource ID to Union.

### Manage permissions directly

Managing permissions directly is required if it is not desirable to grant role assigning permissions to Union.

[Create a role assignment](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal) assigning the `Storage Blob Data Contributor` role to the `unionrunner` user assigned identity scoped the blob storage container.

Refer to [Azure portal's user assigned managed identitites](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.ManagedIdentity%2FuserAssignedIdentities) if assistance is required identifying the `unionrunner` user assigned managed identity within the same resource group as the Union data plane.
