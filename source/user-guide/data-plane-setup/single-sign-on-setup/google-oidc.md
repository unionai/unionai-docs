# Google OpenID Connect

To set up your Union instance to use Google OpenID Connect as the identity provider, follow the directions below.

:::{admonition} Google documentation
In this article, we cover the same steps as in the [OpenID Connect](https://developers.google.com/identity/openid-connect/openid-connect) Google documentation, but with additional directions specific to Union.
:::

## Setting up OAuth 2.0

Before your Union tenant can use Google's OAuth 2.0 authentication system for user login, select an existing project or set up a new project in the [Google Cloud Console](https://console.cloud.google.com).

1. Maneuver to the Clients section for [Google Auth Platform](https://console.cloud.google.com/auth/).

2. Click **CREATE CLIENT**. If this is your first client you might need to provide additional App details. There is no special configuration needed from the Union side.

3. Under **Create OAuth client ID**, select **Web application** as Application type and assign a name.

4. Under **Authorized redirect URIs**, add an entry with the following callback URI: `https://signin.hosted.unionai.cloud/oauth2/v1/authorize/callback`.

5. Click **Create**.

## Obtain OAuth 2.0 credentials

Click on your configured client and copy the values for **Client ID** & **Client secret** to a text file on your computer.

![OAuth 2.0 credentials](/_static/images/user-guide/data-plane-setup/single-sign-on-setup/google-oidc/oauth-credentials.png)

## Share the Client ID & Client secret securely with Union

1. Copy the public key provided by Union here: [**public-key.txt**](/_static/public/public-key.txt)

2. Encrypt the given text file on your computer with a pgb tool of your choice.

3. Share the encrypted message with the Union team over Slack.

