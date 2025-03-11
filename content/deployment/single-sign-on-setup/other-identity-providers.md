---
title: Other identity providers
weight: 4
variants: "+flyte +serverless +byoc +byok"
---

# Other identity providers

Depending on the type of identity provider you are using, open the appropriate directions below on the Okta site:

* [Okta-to-Okta](https://developer.okta.com/docs/guides/add-an-external-idp/oktatookta/main/)

* [OpenID Connect (OIDC)](https://developer.okta.com/docs/guides/add-an-external-idp/openidconnect/main/)

* [SAML 2.0](https://developer.okta.com/docs/guides/add-an-external-idp/saml2/main/)

Now, referencing those directions, follow the steps below:

1. Navigate to the section with the heading **Create an app at the Identify Provider**.

1. Complete all the steps in that section and make a note of the **application (client) ID**.

1. Where a callback URI needs to be specified, use `https://signin.hosted.unionai.cloud/oauth2/v1/authorize/callback`.

1. The last step in the setup will generate the **client secret**. Copy this value to a text file on your computer.
   Make a copy of this value.

## Share the client secret securely with the Union team

1. Copy the public key provided by Union here: [**public-key.txt**](/_static/public/public-key.txt)

1. Go to [https://pgptool.org](https://pgptool.org/).

1. Click the **Encrypt** tab.

1. Upload the public key provided by Union under **Receiver's public key**.

1. Skip the **Signer’s Private Key** section.

1. Enter the **client secret** in plain text and encrypt it.

1. Download the encrypted text and share it with the Union team over Slack.

1. Delete the client secret from the text file on your computer.

## Share the application (client) ID with Union

Share the **application (client) ID** with the Union team over Slack.
This value does not have to be encrypted.
