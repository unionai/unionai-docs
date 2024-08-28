# Data plane setup on Azure

To set up your data plane on Azure, you must allow Union to provision and maintain compute resources under your Azure Subscription. To do this, you will need to provision a user managed identity with sufficient permissions to an Azure resource group.

## Selecting Azure Tenant and Subscription

* Select the Tenant ID for your organization. Refer to [Microsoft Entra ID service page](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/Overview) from the Azure portal.
* We highly recommend creating a new Subscription for Union-specific services. This helps isolate Service Quotas and Azure costs from your other Azure resources.
  * Ensure the Subscription is tied to an active Billing account.
* Provide the Tenant and Suscription ID to Union.

<!-- TODO(MIKE) ### Azure CLI Steps -->

## Create a Microsoft Entra Application Registration

Union uses [Microsoft Entra for AKS authentication and Kubernetes RBAC for authorization](https://learn.microsoft.com/en-us/azure/aks/azure-ad-rbac?tabs=portal). This step involves
creating a Union specific App and granting it sufficient permission to managed the dataplane.

1. Navigate to the [Application Registrations](https://entra.microsoft.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade/quickStartType~/null/sourceType/Microsoft_AAD_IAM) page.
2. Create a new registration.
3. Create a new application. The name is your choice, but we recommend `union`. Leave it at the "Single Tenant" account type and do not add any registration URIs.
4. Select "API Permissions" from the application details page after creating it.
5. Select "Add a permission".
6. Select "Microsoft Graph" from the "Microsofts APIs" tab.
7. Select "Application permissions".
8. Add the following permissions:

* Application.Read.All
* Group.ReadWrite.All

9. Navigate to your target [Azure Subscription](https://portal.azure.com/#view/Microsoft_Azure_Billing/SubscriptionsBladeV2).
10. Within the Subscription page select Access Control (IAM). Select Add Role Assignment and add the following roles:

<!-- TODO(PE-1123) The below roles will change in favor of minimal set of permissions -->

* Contributor
* Storage Blob Data Owner
* Role Based Access Control Administrator
* Azure Kubernetes Service Cluster User Role

11. Provide the Application Client ID to Union.

<!-- TODO(MIKE) ### Azure CLI Steps -->

## Create workload identity federation credentials for Union

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

Provide the group `Object ID` to Union.

## Setting up and managing your own VNet (optional)

If you decide to manage your own VNet instead of leaving it to Union, you will need to set it up yourself.

### Required Union VNet permissions

Union requires permissions to read Azure network resources and assign the `Network Contributor` role to the underlying Union Kubernetes cluster.

Therefore, the Union application requires the following RBAC permissions scoped to the target VNet. [Creating a role assignment](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal) will be required `scope`d to the VNet with the Union app service principal as the granted principal (`Members` through the Azure portal). For roles, the simplest option is to use Azure provided roles `Reader` and `User Access Administrator`. Alternatively, a custom role can be used with the following permissions:

* `Microsoft.Network/*/read`
* `Microsoft.Authorization/roleAssignments/write`
* `Microsoft.Authorization/roleAssignments/delete`
* `Microsoft.Authorization/roleAssignments/read`
* `Microsoft.Authorization/roleDefinitions/read`

### Required VNet Properties

The VNet should be configured with the following characteristics:

* We recommend using a VNet within the same Azure tenant as your Union data plane
* A single subnet with an address prefix with /19 CIDR mask. This is used for Kubernetes nodes
* One to five subnets with an address prefix with /14 to /18 CIDR mask. This is used for Kubernetes pods. /14 is preferrable to mitigate IP exhaustion. It is common to start with one subnet for initial clusters and add more subnets as workloads scale.
* An non-allocated (I.E. no subnet) /19 CIDR range that will be retained for Service CIDRs.
* Within the CIDR range choose a single IP address that will be used for internal DNS. This IP address should not be the first address within the CIDR range.
* (Recommended): Enable [Virtual network service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview) `Microsoft.Storage`, `Microsoft.ContainerRegistry`, and `Microsoft.KeyVault`.
* (Recommended) Create a [NAT gateway for Virtual network](https://learn.microsoft.com/en-us/azure/nat-gateway/quickstart-create-nat-gateway-portal) egress traffic. This allows scaling out public IP addresses and limit potential external rate limitting scenarios.

Once your VPC is set up, provide the following to Union:

* The Virtual Network's subscription ID.
* The Virtual Network's name.
* The Virtual Network's resource group name.
* The Virtual Network's subnet name used for Kubernetes nodes.
* The Virtual Network's subnet names used for Kubernetes pods.
* The CIDR range intended to use for Kubernetes services.
* The IP address to be used for internal DNS.

### Example VPC CIDR Block allocation

* 10.0.0.0/8 for the VPC CIDR block.
* 10.0.0.0/19 for the Kubernetes node specific subnet.
* 10.4.0.0/14 for the initial Kubernetes pods specific subnet.
  * 10.8.0.0/14, 10.12.0.0/14, 10.16.0.0/14, 10.20.0.0/14 for any future Kubernetes pod specific subnets.
* 10.0.96.0/19 unallocated for Kubernetes services.
* 10.0.96.10 for internal DNS.
