---
title: Enabling Azure resources
weight: 1
variants: +flyte +serverless +byoc +byok
---

# Enabling Azure resources

Components of your Union data plane will need to connect to and communicate with other resources in your Azure cloud environment, such as Azure [Blob Storage](https://azure.microsoft.com/en-ca/products/storage/blobs/) and [Container Registry](https://azure.microsoft.com/en-us/products/container-registry).

[Data plane setup on Azure](../../data-plane-setup/data-plane-setup-on-azure.md) provides Union with the necessary permissions to manage underlying Azure resources within your data plane. Access to non-Union Azure resources is subject to Azure limitations and will require additional configuration.

As your projects evolve, your needs may change.
You can always contact the Union team for help enabling additional resources as required.

## Types of access

There are two categories of access that you are likely to have to deal with:

* **Infrastructure access**:
  Enabling access to a resource for your data plane infrastructure.
  The most common case occurs when using your container registry task container images.
  In that case, refer to [Enabling Azure Container Registry](./enabling-azure-container-registry.md) to configure the Union data plane to access that registry.
* **Task code access**:
  Enabling access to a resource for your task code.
  For example, your task code might need to access Azure Blob Storage at runtime.
  This involves granting permission to the [User-assigned managed identity](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview) attached to the Kubernetes cluster within which your task code runs.

## Infrastructure-level access

Infrastructure access with non-Union-managed Azure resources will require additional configuration. Refer to [Enabling Azure Container Registry](./enabling-azure-container-registry.md) if you need access to images within an existing or non-Union-managed container registry.

## Task code access

Union tasks run within a Union-managed Kubernetes pod in your data plane. Union uses [Microsoft Entra Workload ID](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview?tabs=dotnet) to create user-assigned managed identities and access Union-managed Azure resources. Additional permissions can be granted to the user-assigned managed identity to access Azure resources within the same Tenant.

Union on Azure has two types of access arrangements:

* **Domain-scoped access**: With this arrangement, you define permissions you want to grant to your tasks, which are applied only to a specific Union domain.
* **Global access**: With this arrangement, you define permissions you want to grant to your tasks, which are applied to an entire Azure subscription or resource group.

> [!NOTE] Azure only supports scoping by domain
> In AWS-based data planes, scoping by both project _and_ domain is supported.
> However, due to intrinsic architectural constraints, Azure-based data planes only support scoping by domain.

Global access is recommended for most use cases since it is simpler. Still, if you have a compelling reason to restrict access, then the subscription/resource group-domain-scoped access is available at the cost of additional complexity in setup.

> [!NOTE] Relationship with RBAC
> The permissions being discussed here are attached to a domain.
> This is independent of the permissions granted to users and machine applications through Union's role-based access control (see [User management](../../administration/user-management.md)).
> But, the two types of permissions are related.
>
> For example, for a user (or machine application) to have read access to a blob storage container, two things are required:
>
> * The user (or machine application) must have **execute** permission for the project and domain where the code that does the reading resides.
> * The domain must have read permission for the blob storage container.

## Domain-scoped access

**Because of the way that Azure works internally, domain-scoped access can only be configured by the Union team.**

Please work directly with the Union team if you have requirements that involve domain-scoped access to cloud resources.

## Globally-scoped access

Union creates a managed identity prefixed with `flyteuser` within the resource group that contains the other Union-managed data plane Azure resources. Navigate to [Azure portal Managed Identities](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.ManagedIdentity%2FuserAssignedIdentities) to find respective managed identity details.

Follow [Azure's official assigned roles documentation](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal) to assign an appropriate role to scope.
