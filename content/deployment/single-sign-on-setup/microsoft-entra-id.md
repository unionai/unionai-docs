---
title: Microsoft Entra ID (formerly Azure AD)
weight: 3
variants: "+flyte +serverless +byoc +byok"
---

# Microsoft Entra ID (formerly Azure AD)

To set up your Union instance to use Microsoft Entra ID as the identity provider, follow the directions below.

{{< note "Microsoft documentation" >}}
In this article, we cover the same steps as the [Quickstart: Register an application with the Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app) Microsoft documentation, but with additional directions specific to Union.
{{< /note >}}

## Register an Entra ID application

1. Log into your Azure account as a cloud application administrator or higher permission level.

1. In the identity drop down on the top right of the page (indicated by the email you are currently logged in as) select **Switch directory**, then select the directory yin which you want to register this application.

1. Browse to **Identity > Applications > App registrations** and select **New registration**.

1. Under **Name**, enter an appropriate display name. For example, `Union Production`.

1. Under **Supported account types**, select **Accounts in this organizational directory only**.

1. Under **Redirect URI (optional)**, select **Web** and enter the following URI:

   `https://signin.hosted.unionai.cloud/oauth2/v1/authorize/callback`

1. Click **Register**.

{{< note "Make the app visible to users" >}}
New app registrations are hidden to users by default. You must enable the app when you are ready for users to see the app on their **My Apps** page.
To enable the app, in the Microsoft Entra admin center, navigate to **Identity > Applications > Enterprise applications** and select the app.
Then, on the **Properties** page, toggle **Visible to users?** to **Yes**.
{{< /note >}}

## Copy the values needed by the Union team

When registration finishes, the Microsoft Entra admin center will display the app registration's **Overview** page, from which you can copy the Application (client) ID, Directory (tenant) ID, and client secret needed by the Union team.

### Application (client) ID and directory (tenant) ID

Copy the **Application (client) ID** and **Directory (tenant) ID** from the overview page to a text file on your computer.

![Application and directory ID](/_static/images/user-guide/data-plane-setup/single-sign-on-setup/microsoft-entra-id/entra-id-application-and-directory-id.png)

### Client secret

To get the **client secret**, on the overview page, go to **Client credentials** and click **Add a certificate or secret**.

![Client credentials](/_static/images/user-guide/data-plane-setup/single-sign-on-setup/microsoft-entra-id/entra-id-client-credentials.png)

On the subsequent page, under **Client secrets**, click **New client secret** to generate a new secret.
Copy the **Value** of this secret to a plain text file on your computer.

![Client secret](/_static/images/user-guide/data-plane-setup/single-sign-on-setup/microsoft-entra-id/entra-id-client-secret.png)

## Share the client secret securely with Union

1. Copy the public key provided by Union here: [**public-key.txt**](/_static/public/public-key.txt)

1. Go to [https://pgptool.org](https://pgptool.org/).

1. Click the **Encrypt** tab.

1. Upload the public key provided by Union under **Receiver's public key**.

1. Skip the **Signer’s Private Key** section.

1. Enter the **client secret** in plain text and encrypt it.

1. Download the encrypted text and share it with the Union team over Slack.

1. Delete the **client secret** from the text file on your computer.

## Share the IDs with Union

Share the **application (client) ID** and **directory (tenant) ID** with the Union team over Slack.
These values do not have to be encrypted.
