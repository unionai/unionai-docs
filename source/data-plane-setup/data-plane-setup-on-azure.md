# Data plane setup on Azure

To set up your data plane on Azure, you must allow Union to provision and maintain compute resources under your Azure Subscription. To do this, you will need to provision a user managed identity with sufficient permissions to an Azure resource group.

## Selecting Azure Tenant and Subscription

* Select the Tenant ID for your organization. Refer to [Microsoft Entra ID service page](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/Overview) from the Azure portal.
* We highly recommend creating a new Subscription for Union-specific services. This helps isolate Service Quotas and Azure costs from your other Azure resources.
  * Ensure the Subscription is tied to an active Billing account.
* Provide the Tenant and Suscription ID to Union.

<!-- TODO(MIKE) ### Azure CLI Steps -->

## Create a Microsoft Entra Application Registration

1. Navigate to the [Application Registrations](https://entra.microsoft.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade/quickStartType~/null/sourceType/Microsoft_AAD_IAM) page.
2. Create a new registration.
3. Create a new Application the name. The name is your choice but we recommend `union`. Leave at Single Tenant account type and do not add and registration URIs.
4. Navigate to your target Azure [Subscription](https://portal.azure.com/#view/Microsoft_Azure_Billing/SubscriptionsBladeV2).
5. Within the Subscription page select Access Control (IAM). Select Add Role Assignment and add the following roles:

  * Contributor

6. Provide the Application Client ID to Union.

<!-- TODO(MIKE) ### Azure CLI Steps -->

## Create a Workload Federation Identity Credentials for Union.

Creating an Azure [Workload identity federation](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation) to establish a trust relationship with Union's
AWS environment. This allows Union to manage Azure resources within your subscription.

1. Go the application registration page for the app you created.
2. Select "Certificates & secrets."
3. Select "the Federated Credentials" tab, select "Add credential", and choose "Other issuer"
4. Set `Issuer` to `https://cognito-identity.amazonaws.com`
5. Set `Subject identifier` to `us-east-2:6f9a6050-887a-c4cc-0625-120a4805bc34`
6. `Name` is your choice but would recommend `union-access`
7. Set `Audience` to `us-east-2:ad71bce5-161b-4430-85a5-7ea84a941e6a`
