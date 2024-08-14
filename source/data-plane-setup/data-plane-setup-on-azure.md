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
5. Select "Add a permission"
6. Select "Microsoft Graph" from the "Microsofts APIs" tab
7. Select "Application permissions"
8. Add the following permissions

* Application.Read.All
* Group.ReadWrite.All

9. Navigate to your target Azure [Subscription](https://portal.azure.com/#view/Microsoft_Azure_Billing/SubscriptionsBladeV2).
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

It is recommended to [create a Microsoft Entra group](https://learn.microsoft.com/en-us/training/modules/create-users-and-groups-in-azure-active-directory/) for AKS cluster admin access.
AKS Cluster admin access is commonly provided to individuals that need direct (E.G. `kubectl`) access to the clustr.

Provide the group `Object ID` to Union.
