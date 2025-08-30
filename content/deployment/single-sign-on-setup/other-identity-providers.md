---
title: Other identity providers
weight: 4
variants: -flyte -serverless +byoc -selfmanaged
---

# Other identity providers

Depending on the type of identity provider you are using, open the appropriate directions below on the Okta site:

- [Okta-to-Okta](https://developer.okta.com/docs/guides/add-an-external-idp/oktatookta/main/)

- [OpenID Connect (OIDC)](https://developer.okta.com/docs/guides/add-an-external-idp/openidconnect/main/)

- [SAML 2.0](https://developer.okta.com/docs/guides/add-an-external-idp/saml2/main/)

Now, referencing those directions, follow the steps below:

1. Navigate to the section with the heading **Create an app at the Identify Provider**.

1. Complete all the steps in that section and make a note of the **application (client) ID**.

1. Where a callback URI needs to be specified, use `https://signin.hosted.unionai.cloud/oauth2/v1/authorize/callback`.

1. The last step in the setup will generate the **client secret**. Copy this value to a text file on your computer.
   Make a copy of this value.

## Share the client secret securely with the {{< key product_name >}} team

1. Copy the public key provided by {{< key product_name >}} here: {{< download "/_static/public/public-key.txt" >}}

2. Go to [https://pgptool.net](https://pgptool.net/).

3. Click the **Encrypt (+Sign)** tab.

4. Enter public key in **Public Key (For Verification)** section.

5. Skip the **Private Key** section.

6. Enter the **client secret** in plain text and encrypt it.

7. Save encypted text to a file and share with the {{< key product_name >}} team over Slack.

8. Delete the client secret from the text file on your computer.

## Share the application (client) ID with {{< key product_name >}}

Share the **application (client) ID** with the {{< key product_name >}} team over Slack.
This value does not have to be encrypted.
