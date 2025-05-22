---
title: Data plane setup on Azure
weight: 7
variants: -flyte -serverless +byoc -selfmanaged
---

# Data plane setup on Azure

To set up your data plane on Azure, you must allow {{< key product_name >}} to provision and maintain compute resources under your Azure subscription. To do this, you will need to provision an Azure app registration with sufficient permissions to an Azure subscription.

## Selecting Azure tenant and subscription

- Select the tenant ID for your organization. Refer to [Microsoft Entra ID service page](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/Overview) from the Azure portal.
- We highly recommend creating a new subscription for {{< key product_name >}}-specific services. This helps isolate service quotas and Azure costs from your other Azure resources.
  - Ensure the subscription is tied to an active billing account.
- Provide the Tenant and Subscription ID to {{< key product_name >}}.

## Create a Microsoft Entra Application Registration

{{< key product_name >}} uses [Microsoft Entra for AKS authentication and Kubernetes RBAC for authorization](https://learn.microsoft.com/en-us/azure/aks/azure-ad-rbac?tabs=portal). This step involves
creating a {{< key product_name >}} specific App and granting it sufficient permission to manage the dataplane.

1. Navigate to the [Application Registrations](https://entra.microsoft.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade/quickStartType~/null/sourceType/Microsoft_AAD_IAM) page.
2. Create a new registration.
3. Create a new application. The name is your choice, but we recommend `union`. Leave it at the "Single Tenant" account type and do not add any registration URIs.
4. Select "API Permissions" from the application details page after creating it.
5. Select "Add a permission".
6. Select "Microsoft Graph" from the "Microsofts APIs" tab.
7. Select "Application permissions".
8. Add the following permissions:

- Application.Read.All
- Group.ReadWrite.All

9. Navigate to your target [Azure Subscription](https://portal.azure.com/#view/Microsoft_Azure_Billing/SubscriptionsBladeV2).
10. Within the Subscription page select Access Control (IAM). Select Add Role Assignment and add the following roles:

- Contributor
- Role Based Access Control Administrator

11. Provide the Application Client ID to {{< key product_name >}}.

## Create workload identity federation credentials for {{< key product_name >}}

1. Go the application registration page for the app you created.
2. Select "Certificates & secrets."
3. Select the "Federated Credentials" tab, then select "Add credential", and choose "Other issuer".
4. Set "Issuer" to `https://cognito-identity.amazonaws.com`
5. Set "Subject identifier" to `us-east-2:6f9a6050-887a-c4cc-0625-120a4805bc34`
6. "Name" is your choice, but we recommend `union-access`
7. Set "Audience" to `us-east-2:ad71bce5-161b-4430-85a5-7ea84a941e6a`

## (Recommended) Create a Microsoft Entra group for cluster administration

We recommend [creating a Microsoft Entra group](https://learn.microsoft.com/en-us/training/modules/create-users-and-groups-in-azure-active-directory/) for AKS cluster admin access.
AKS Cluster admin access is commonly provided to individuals that need direct (e.g. `kubectl`) access to the cluster.

Provide the group `Object ID` to {{< key product_name >}}.

## (Optional) Setting up and managing your own VNet

If you decide to manage your own VNet instead of leaving it to {{< key product_name >}}, you will need to set it up yourself.

### Required {{< key product_name >}} VNet permissions

{{< key product_name >}} requires permissions to read Azure network resources and assign the `Network Contributor` role to the underlying {{< key product_name >}} Kubernetes cluster.

[Create a role assignment](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal) to allow {{< key product_name >}} to read VNet resources and assign roles. These permissions should be scoped to the target Virtual Network (VNet). Follow these steps to set up the required access:

1. Navigate to the Azure portal and locate the target VNet.
2. In the VNet's access control (IAM) section, create a new role assignment.
3. For the 'Assigned to' field, select the {{< key product_name >}} application's service principal.
4. For the 'Role' field, you have two options:
   - Simplest approach: Assign the built-in Azure roles `Reader` and `User Access Administrator`.
   - Advanced approach: Create a custom role with the following specific permissions:
     - `Microsoft.Network/*/read`
     - `Microsoft.Authorization/roleAssignments/write`
     - `Microsoft.Authorization/roleAssignments/delete`
     - `Microsoft.Authorization/roleAssignments/read`
     - `Microsoft.Authorization/roleDefinitions/read`
5. Ensure the 'Scope' is set to the target VNet.
6. Complete the role assignment process.

This configuration will provide the {{< key product_name >}} application with the necessary permissions to interact with and manage resources within the specified VNet.

> [!NOTE] Creating Azure role assignments
>
> For more detailed instructions on creating role assignments, refer to the
> [official Azure documentation](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal).

### Required VNet properties

We recommend using a VNet within the same Azure tenant as your {{< key product_name >}} data plane. It should be configured with the following characteristics:

- A single subnet with an address prefix with `/19` CIDR mask. This is used for Kubernetes nodes.
- One to five subnets with an address prefix with `/14` to `/18` CIDR mask. This is used for Kubernetes pods. `/14` is preferable to mitigate IP exhaustion. It is common to start with one subnet for initial clusters and add more subnets as workloads scale.
- An non-allocated (i.e., no subnet) `/19` CIDR range that will be retained for service CIDRs.
- Within the CIDR range, choose a single IP address that will be used for internal DNS. This IP address should not be the first address within the CIDR range.
- (Recommended): Enable [virtual network service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview) `Microsoft.Storage`, `Microsoft.ContainerRegistry`, and `Microsoft.KeyVault`.
- (Recommended) Create a [NAT gateway for virtual network](https://learn.microsoft.com/en-us/azure/nat-gateway/quickstart-create-nat-gateway-portal) egress traffic. This allows scaling out public IP addresses and limit potential external rate limiting scenarios.

Once your VPC is set up, provide the following to {{< key product_name >}}:

- The Virtual Network's subscription ID.
- The Virtual Network's name.
- The Virtual Network's resource group name.
- The Virtual Network's subnet name used for Kubernetes nodes.
- The Virtual Network's subnet names used for Kubernetes pods.
- The CIDR range intended to use for Kubernetes services.
- The IP address to be used for internal DNS.

### Example VPC CIDR Block allocation

- `10.0.0.0/8` for the VPC CIDR block.
- `10.0.0.0/19` for the Kubernetes node specific subnet.
- `10.4.0.0/14` for the initial Kubernetes pods specific subnet.
  - `10.8.0.0/14`, `10.12.0.0/14`, `10.16.0.0/14`, `10.20.0.0/14` for any future Kubernetes pod specific subnets.
- `10.0.96.0/19` unallocated for Kubernetes services.
- `10.0.96.10` for internal DNS.

## {{< key product_name >}} Maintenance Windows

{{< key product_name >}} configures a four hour maintainence window to run monthly on the first Sunday at 3AM with respect to the Azure location's timezone.

> [!NOTE] Setting up Tasks for Fault Tolerance
> During this time window Flyte execution pods could be potentially interrupted.
> We recommend leveraging
> [Flyte fault tolerance](https://docs.flyte.org/en/latest/concepts/tasks.html#fault-tolerance) and
> [checkpointing](https://docs.flyte.org/en/latest/user_guide/advanced_composition/intratask_checkpoints.html)
> to efficiently minimize failed executions.
