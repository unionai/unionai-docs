---
title: Authentication
weight: 1
variants: +flyte -serverless -byoc -selfmanaged
mermaid: true
---

# Configuring authentication

The Flyte platform consists of multiple components. Securing communication between each component is crucial to ensure
the integrity of the overall system.

Flyte supports most of the [OAuth2.0](https://tools.ietf.org/html/rfc6749) authorization grants and use them to control access to workflow and task executions as the main protected resources.

Additionally, Flyte implements the [OIDC1.0](https://openid.net/specs/openid-connect-core-1_0.html) standard to attach user identity to the autorization flow. This feature requires integration with an external Identity Provider.

The following diagram illustrates how the elements of the OAuth2.0 protocol map to the Flyte components involved in the authentication process:

```mermaid
sequenceDiagram
  participant Client (CLI/UI/system) as Client (CLI/UI/system)
  participant flytepropeller as Resource Server + Owner<br>(flytepropeller)
  participant flyteadmin/external IdP as Authorization Server<br>(flyteadmin/external IdP)

  Client (CLI/UI/system) ->>+ flytepropeller: Authorization request
  flytepropeller ->>+ flyteadmin/external IdP: Request authorization grant
  flyteadmin/external IdP ->> flytepropeller: Issue authorization grant
  flytepropeller ->> Client (CLI/UI/system): Authorization grant
  Client (CLI/UI/system) ->> flyteadmin/external IdP: Authorization grant
  flyteadmin/external IdP ->> Client (CLI/UI/system): Access token
  Client (CLI/UI/system) ->> flytepropeller: Access token
  flytepropeller ->> Client (CLI/UI/system): Protected resource
```

There are two main dependencies required for a complete auth flow in Flyte:

* **OIDC (Identity Layer) configuration** The OIDC protocol allows clients (such as Flyte) to confirm the identity of a user, based on authentication done by an Authorization Server.
  To enable this, you first need to register Flyte as an app (client) with your chosen Identity Provider (IdP).

* **An authorization server** The authorization server job is to issue access tokens to clients for them to access the protected resources.
  Flyte ships with two options for the authorization server:
  * **Internal authorization server**: It's part of `flyteadmin` and is a suitable choice for quick start or testing purposes.
  * **External (custom) authorization server**: This a service provided by one of the supported IdPs and is the recommended option if your organization needs to retain control over scope definitions, token expiration policies and other advanced security controls.

> [!NOTE]
> Regardless of the type of authorization server to use, you will still need an IdP to provide identity through OIDC.

## Configuring the identity layer

### Prerequisites

* A public domain name (e.g. example.foobar.com)
* A DNS entry mapping the Fully Qualified Domain Name to the Ingress `host`.

> [!NOTE]
> Checkout this [community-maintained guide](https://github.com/davidmirror-ops/flyte-the-hard-way/blob/main/docs/06-intro-to-ingress.md) for more information about setting up Flyte in production, including Ingress.

### Configuring your IdP for OIDC

In this section, you can find canonical examples of how to set up OIDC on some of the supported IdPs; enabling users to authenticate in the
browser.

> [!NOTE]
> Using the following configurations as a reference, the community has succesfully configured auth with other IdPs as Flyte implements open standards.

#### Google

1. Create an OAuth2 Client Credential following the [official documentation](https://developers.google.com/identity/protocols/oauth2/openid-connect) and take note of the `client_id` and `client_secret`

2. In the **Authorized redirect URIs** field, add `http://localhost:30081/callback` for **sandbox** deployments or `https://<your-Ingress-host>/callback` for other deployment methods.

#### Okta

1. If you don't already have an Okta account, [sign up for one](https://developer.okta.com/signup/).
2. Create an app integration, with `OIDC - OpenID Connect` as the sign-on method and `Web Application` as the app type.
3. Add sign-in redirect URIs: `http://localhost:30081/callback` for sandbox or `https://<your-Ingress-host>/callback` for other Flyte deployment types.
4. *Optional* - Add logout redirect URIs: `http://localhost:30081/logout` for sandbox, `https://<your-Ingress-host>/callback` for other Flyte deployment methods.
5. Take note of the Client ID and Client Secret.

#### Keycloak

1. Create a realm using the [admin console](https://wjw465150.gitbooks.io/keycloak-documentation/content/server_admin/topics/realms/create.html).
2. [Create an OIDC client with client secret](https://wjw465150.gitbooks.io/keycloak-documentation/content/server_admin/topics/clients/client-oidc.html) and note them down.
3. Add Login redirect URIs: `http://localhost:30081/callback` for sandbox or `https://<your-Ingress-host>/callback` for other Flyte deployment methods.

#### Microsoft Entra ID

1. In the Azure portal, open Microsoft Entra ID from the left-hand menu.
2. From the Overview section, navigate to **App registrations** > **+ New registration**.
   *  Under Supported account types, select the option based on your organization's needs.
3. Configure Redirect URIs
   * In the Redirect URI section, choose **Web** from the **Platform** dropdown and enter the following URIs based on your environment:
     * Sandbox: `http://localhost:30081/callback`
     * Production: `https://<your-Ingress-URL>/callback`
4. Obtain Tenant and Client Information
   * After registration, go to the app's Overview page.
   * Take note of the Application (client) ID and Directory (tenant) ID. You’ll need these in your Flyte configuration.
5. Create a Client Secret
   * From the Certificates & Secrets tab, click + New client secret.
   * Add a Description and set an Expiration period (e.g., 6 months or 12 months).
   * Click Add and copy the Value of the client secret; it will be used in the Helm values.
6. If the Flyte deployment will be dealing with user data, set API permissions:
   * Navigate to **API Permissions > + Add a permission**, select **Microsoft Graph > Delegated permissions**, and add the following permissions:
     * `email`
     * `openid`
     * `profile`
     * `offline_access`
     * `User.Read`
7. Expose an API (for Custom Scopes). In the Expose an API tab:
   * Click + Add a scope, and set the Scope name (e.g., access_flyte).
   * Provide a Consent description and enable Admin consent required and Save.
   * Then, click + Add a client application and enter the Client ID of your Flyte application.

8. Configure Mobile/Desktop Flow (for flytectl):
   * Go to the Authentication tab, and click + Add a platform.
   * Select Mobile and desktop applications.
   * Add following URI: `http://localhost:53593/callback`
   * Scroll down to Advanced settings and enable Allow public client flows.

For further reference, check out the official [Entra ID Docs](https://docs.microsoft.com/en-us/power-apps/maker/portals/configure/configure-openid-settings) on how to configure the IdP for OpenIDConnect.

> Make sure the app is registered without [additional claims](https://docs.microsoft.com/en-us/power-apps/maker/portals/configure/configure-openid-settings#configure-additional-claims).
> **The OpenIDConnect authentication will not work otherwise**.
> Please refer to [this GitHub Issue](https://github.com/coreos/go-oidc/issues/215) and [Entra ID Docs](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-protocols-oidc#sample-response) for more information.

### Apply the OIDC configuration to the Flyte backend

Select the Helm chart you used to install Flyte:

#### flyte-binary

1. Generate a random password to be used internally by `flytepropeller`
2. Use the following command to hash the password:
   ```shell
   $ pip install bcrypt && python -c 'import bcrypt; import base64; print(base64.b64encode(bcrypt.hashpw("<your-random-password>".encode("utf-8"), bcrypt.gensalt(6))))'
   ```
3. Go to your values file and locate the `auth` section and replace values accordingly:
   ```yaml
   auth:
     enabled: true
     oidc:
       # baseUrl: https://accounts.google.com # Uncomment for Google
       # baseUrl: https://<keycloak-url>/auth/realms/<keycloak-realm> # Uncomment for Keycloak and update with your installation host and realm name
       # baseUrl: https://login.microsoftonline.com/<tenant-id>/v2.0 # Uncomment for Azure AD
       # For Okta use the Issuer URI from Okta's default auth server
       baseUrl: https://dev-<org-id>.okta.com/oauth2/default
       # Replace with the client ID and secret created for Flyte in your IdP
       clientId: <client_ID>
       clientSecret: <client_secret>
     internal:
       clientSecret: '<your-random-password>'
       # Use the output of step #2 (only the content inside of '')
       clientSecretHash: <your-hashed-password>
     authorizedUris:
     - https://<your-flyte-deployment-URL>
   ```
4. Save your changes
5. Upgrade your Helm release with the new values:

```shell
$ helm upgrade <release-name> flyteorg/flyte-binary -n <your-namespace> --values <your-values-file>.yaml
```
Where `<release-name>` is the name of your Helm release, typically `flyte-backend`. You can find it using `helm ls -n <your-namespace>`

6. Verify that your Flyte deployment now requires successful login to your IdP to access the UI (`https://<your domain>/console`)

#### flyte-core

1. Generate a random password to be used internally by `flytepropeller`
2. Use the following command to hash the password:
   ```shell
   $ pip install bcrypt && python -c 'import bcrypt; import base64; print(base64.b64encode(bcrypt.hashpw("<your-random-password>".encode("utf-8"), bcrypt.gensalt(6))))'
   ```
   Take note of the output (only the contents inside `''`).
3. Go to your Helm values file and add the client_secret provided by your IdP to the configuration:
   ```yaml
   flyteadmin:
     secrets:
       oidc_client_secret:  <your_client_secret>
   ```
4. Verify that the `configmap` section include the following, replacing the content where indicated:
   ```yaml
   configmap:
     adminServer:
       server:
         httpPort: 8088
         grpc:
           port: 8089
         security:
           secure: false
           useAuth: true
           allowCors: true
           allowedOrigins:
     # Accepting all domains for Sandbox installation
             - "*"
           allowedHeaders:
             - "Content-Type"
       auth:
         appAuth:
           thirdPartyConfig:
             flyteClient:
               clientId: flytectl
               redirectUri: http://localhost:53593/callback
               scopes:
                 - offline
                 - all
           selfAuthServer:
             staticClients:
               flyte-cli:
                 id: flyte-cli
                 redirect_uris:
                 - http://localhost:53593/callback
                 - http://localhost:12345/callback
                 grant_types:
                   - refresh_token
                   - authorization_code
                 response_types:
                   - code
                   - token
                 scopes:
                   - all
                   - offline
                   - access_token
                 public: true
               flytectl:
                 id: flytectl
                 redirect_uris:
                   - http://localhost:53593/callback
                   - http://localhost:12345/callback
                 grant_types:
                   - refresh_token
                   - authorization_code
                 response_types:
                   - code
                   - token
                 scopes:
                   - all
                   - offline
                   - access_token
                 public: true
               flytepropeller:
                 id: flytepropeller
       # Use the bcrypt hash generated for your random password
                 client_secret: "<YOUR_PASSWORD_HASH>"
                 redirect_uris:
                   - http://localhost:3846/callback
                 grant_types:
                   - refresh_token
                   - client_credentials
                 response_types:
                   - token
                 scopes:
                   - all
                   - offline
                   - access_token
                 public: false

         authorizedUris:
         # Use the public URL of flyteadmin (a DNS record pointing to your Ingress resource)
           - https://<your-flyte-deployment-URL>
           - http://flyteadmin:80
           - http://flyteadmin.flyte.svc.cluster.local:80
         userAuth:
           openId:
         # baseUrl: https://accounts.google.com # Uncomment for Google
         # baseUrl: https://login.microsoftonline.com/<tenant-id>/v2.0 # Uncomment for Azure AD
           # For Okta, use the Issuer URI of the default auth server
           baseUrl: https://dev-<org-id>.okta.com/oauth2/default
           # Use the client ID generated by your IdP
           clientId: <client_ID>
           scopes:
             - profile
             - openid
   ```
5. Additionally, at the root of the values file, add the following block and replace the necessary information:
   ```yaml
   secrets:
     adminOauthClientCredentials:
     # If enabled is true, and `clientSecret` is specified, helm will create and mount `flyte-secret-auth`.
     # If enabled is true, and `clientSecret` is null, it's up to the user to create `flyte-secret-auth` as described in
     # https://docs.flyte.org/en/latest/deployment/cluster_config/auth_setup.html#oauth2-authorization-server
     # and helm will mount `flyte-secret-auth`.
     # If enabled is false, auth is not turned on.
     # Note: Unsupported combination: enabled.false and clientSecret.someValue
       enabled: true
     # Use the non-encoded version of the random password
       clientSecret: "<your-random-password>"
       clientId: flytepropeller
   ```
   > For [multi-cluster deployments](../multi-cluster.md) you must add this Secret definition block to the `values-dataplane.yaml` file. If you are not running `flytepropeller` in the control plane cluster, you do not need to create this secret there.
6. Save and exit your editor.
7. Upgrade your Helm release with the new configuration:
   ```shell
   $ helm upgrade <release-name> flyteorg/flyte-binary -n <your-namespace> --values <your-values-file>.yaml
   ```
8. Verify that the `flytepropeller`, `flytescheduler` and `flyteadmin` Pods are restarted and running:
   ```bash
   kubectl get pods -n flyte
   ```

**Congratulations!**

It should now be possible to go to Flyte UI and be prompted for authentication with the default `PKCE` auth flow. Flytectl should automatically pickup the change and start prompting for authentication as well.

The following sections guide you to configure an external auth server (optional for most authorization flows) and describe the client-side configuration for all the auth flows supported by Flyte.

## Configuring your IdP as an External Authorization Server

In this section, you will find instructions on how to setup an OAuth2 Authorization Server in the different IdPs supported by Flyte:

### Okta

Okta's custom authorization servers are available through an add-on license. The free developer accounts do include access, which you can use to test before rolling out the configuration more broadly.

1. From the left-hand menu, go to **Security** > **API**
2. Click on **Add Authorization Server**.
3. Assign an informative name and set the audience to the public URL of FlyteAdmin (e.g. https://example.foobar.com). The audience must exactly match one of the URIs in the `authorizedUris` section above.
4. Note down the **Issuer URI**; this will be used for all the `baseUrl` settings in the Flyte config.
5. Go to **Scopes** and click **Add Scope**.
6. Set the name to `all` (required) and check `Required` under the **User consent** option.
7. Uncheck the **Block services from requesting this scope** option and save your changes.
8. Add another scope, named `offline`. Check both the **Required** and **Include in public metadata** options.
9. Uncheck the **Block services from requesting this scope** option.
10. Click **Save**.
11. Go to  **Access Policies**, click **Add New Access Policy**. Enter a name and description and enable **Assign to** -  `All clients`.
12. Add a rule to the policy with the default settings (you can fine-tune these later).
13. Navigate back to the **Applications** section.
14. Create an integration for `flytectl`; it should be created with the **OIDC - OpenID Connect** sign-on method, and the **Native Application** type.
15. Add `http://localhost:53593/callback` to the sign-in redirect URIs. The other options can remain as default.
16. Assign this integration to any Okta users or groups who should be able to use the `flytectl` tool.
17. Note down the **Client ID**; there will not be a secret.
18. Create an integration for `flytepropeller`; it should be created with the **OIDC - OpenID Connect** sign-on method and **Web Application** type.
19. Check the `Client Credentials` option under **Client acting on behalf of itself**.
20. This app does not need a specific redirect URI; nor does it need to be assigned to any users.
21. Note down the **Client ID** and **Client secret**; you will need these later.
22. Take note of the **Issuer URI** for your Authorization Server. It will be used as the baseURL parameter in the Helm chart

You should have three integrations total - one for the web interface (`flyteconsole`), one for `flytectl`, and one for `flytepropeller`.

### Keycloak

1. Create a realm in keycloak installation using its [admin console](https://wjw465150.gitbooks.io/keycloak-documentation/content/server_admin/topics/realms/create.html).
2. Under `Client Scopes`, click `Add Create` inside the admin console.
3. Create two clients (for `flytectl` and `flytepropeller`) to enable these clients to communicate with the service.
4. `flytectl` should be created with `Access Type Public` and standard flow enabled.
5. `flytePropeller` should be created as an `Access Type Confidential`, enabling the standard flow
6. Take note of the client ID and client Secrets provided.

### Microsoft Entra ID

1. Navigate to tab **Overview**, obtain `<client id>` and `<tenant id>`
2. Navigate to tab **Authentication**, click `+Add a platform`
3. Add **Web** for flyteconsole and flytepropeller, **Mobile and desktop applications** for flytectl.
4. Add URL `https://<console-url>/callback` as the callback for Web
5. Add URL `http://localhost:53593/callback` as the callback for flytectl
6. In **Advanced settings**, set `Enable the following mobile and desktop flows` to **Yes** to enable deviceflow
7. Navigate to tab **Certificates & secrets**, click `+New client secret` to create `<client secret>`
8. Navigate to tab **Token configuration**, click `+Add optional claim` and create email claims for both ID and Access Token
9.  Navigate to tab **API permissions**, add `email`, `offline_access`, `openid`, `profile`, `User.Read`
10. Navigate to tab **Expose an API**, Click `+Add a scope` and `+Add a client application` to create `<custom scope>`.

### Apply the external auth server configuration to Flyte

Follow the steps in this section to configure `flyteadmin` to use an external auth server. This section assumes that you have already completed and applied the configuration for the OIDC Identity Layer.

#### flyte-binary

1. Go to the values YAML file you used to install Flyte
2. Find the `auth` section and follow the inline comments to insert your configuration:

```yaml

auth:
  enabled: true
  oidc:
# baseUrl: https://<keycloak-url>/auth/realms/<keycloak-realm> # Uncomment for Keycloak and update with your installation host and realm name
# baseUrl: https://login.microsoftonline.com/<tenant-id>/v2.0 # Uncomment for Azure AD
# For Okta, use the Issuer URI of the custom auth server:
    baseUrl: https://dev-<org-id>.okta.com/oauth2/<auth-server-id>
# Use the client ID and secret generated by your IdP for the first OIDC registration in the "Identity Management layer : OIDC" section of this guide
    clientId: <oidc-clientId>
    clientSecret: <oidc-clientSecret>
  internal:
# Use the clientID generated by your IdP for the flytepropeller app registration
    clientId: <flytepropeller-client-id>
#Use the secret generated by your IdP for flytepropeller
    clientSecret: '<flytepropeller-client-secret-non-encoded>'
# Use the bcrypt hash for the clientSecret
    clientSecretHash: <-flytepropeller-secret-bcrypt-hash>
  authorizedUris:
# Use here the exact same value used for 'audience' when the Authorization server was configured
  - https://<your-flyte-deployment-URL>
```

3. Find the `inline` section of the values file and add the following content, replacing where needed:

```yaml

inline:
  auth:
    appAuth:
      authServerType: External
      externalAuthServer:
      # baseUrl: https://<keycloak-url>/auth/realms/<keycloak-realm> # Uncomment for Keycloak and update with your installation host and realm name
      # baseUrl: https://login.microsoftonline.com/<tenant-id>/v2.0 # Uncomment for Azure AD
      # For Okta, use the Issuer URI of the custom auth server:
        baseUrl: https://dev-<org-id>.okta.com/oauth2/<auth-server-id>
        metadataUrl: .well-known/oauth-authorization-server
      thirdPartyConfig:
        flyteClient:
          # Use the clientID generated by your IdP for the `flytectl` app registration
          clientId: <flytectl-client-id>
          redirectUri: http://localhost:53593/callback
          scopes:
          - offline
          - all
    userAuth:
      openId:
      # baseUrl: https://<keycloak-url>/auth/realms/<keycloak-realm> # Uncomment for Keycloak and update with your installation host and realm name
      # baseUrl: https://login.microsoftonline.com/<tenant-id>/v2.0 # Uncomment for Azure AD
      # For Okta, use the Issuer URI of the custom auth server:
        baseUrl: https://dev-<org-id>.okta.com/oauth2/<auth-server-id>
        scopes:
        - profile
        - openid
      # - offline_access # Uncomment if your IdP supports issuing refresh tokens (optional)
      # Use the client ID and secret generated by your IdP for the first OIDC registration in the "Identity Management layer : OIDC" section of this guide
        clientId: <oidc-clientId>
```

4. Save your changes
5. Upgrade your Helm release with the new configuration:

```bash

    helm upgrade  <release-name> flyteorg/flyte-core -n <your-namespace> --values <your-updated-values-filel>.yaml
```

#### flyte-core

1. Find the `auth` section in your Helm values file, and replace the necessary data:

> If you were previously using the internal auth server, make sure to delete all the `selfAuthServer` section from your values file

```yaml

configmap:
  adminServer:
    auth:
      appAuth:
        authServerType: External
      # 2. Optional: Set external auth server baseUrl if different from OpenId baseUrl.
      externalAuthServer:
      # Replace this with your deployment URL.  It will be used by flyteadmin to validate the token audience
        allowedAudience: https://<your-flyte-deployment-URL>
      # baseUrl: https://<keycloak-url>/auth/realms/<keycloak-realm> # Uncomment for Keycloak and update with your installation host and realm name
      # baseUrl: https://login.microsoftonline.com/<tenant-id>/v2.0 # Uncomment for Azure AD
      # For Okta, use the Issuer URI of the custom auth server:
        baseUrl: https://dev-<org-id>.okta.com/oauth2/<auth-server-id>

        metadataUrl: .well-known/openid-configuration

    userAuth:
      openId:
      # baseUrl: https://<keycloak-url>/auth/realms/<keycloak-realm> # Uncomment for Keycloak and update with your installation host and realm name
      # baseUrl: https://login.microsoftonline.com/<tenant-id>/v2.0 # Uncomment for Azure AD
      # For Okta, use the Issuer URI of the custom auth server:
        baseUrl: https://dev-<org-id>.okta.com/oauth2/<auth-server-id>
        scopes:
        - profile
        - openid
        # - offline_access # Uncomment if OIdC supports issuing refresh tokens.
        clientId: <client id>

secrets:
  adminOauthClientCredentials:
    enabled: true # see the section "Disable Helm secret management" if you require to do so
    # Replace with the client_secret provided by your IdP for flytepropeller.
    clientSecret: <client_secret>
    # Replace with the client_id provided by provided by your IdP for flytepropeller.
    clientId: <client_id>
```
2. Save your changes
3. Upgrade your Helm release with the new configuration:

```bash

helm upgrade  <release-name> flyteorg/flyte-core -n <your-namespace> --values <your-updated-values-file>.yaml
```
#### flyte-core with Entra ID

```yaml

secrets:
  adminOauthClientCredentials:
    enabled: true
    clientSecret: <client secret>
    clientId: <client id>
---
configmap:
  admin:
    admin:
      endpoint: <admin endpoint>
      insecure: true
      clientId: <client id>
      clientSecretLocation: /etc/secrets/client_secret
      scopes:
      - api://<client id>/.default
      useAudienceFromAdmin: true
---
configmap:
  adminServer:
    auth:
      appAuth:
        authServerType: External
        externalAuthServer:
          baseUrl: https://login.microsoftonline.com/<tenant id>/v2.0/
          metadataUrl: .well-known/openid-configuration
          AllowedAudience:
          - api://<client id>
        thirdPartyConfig:
          flyteClient:
            clientId: <client id>
            redirectUri: http://localhost:53593/callback
            scopes:
            - api://<client id>/<custom-scope>

      userAuth:
        openId:
        baseUrl: https://login.microsoftonline.com/<tenant id>/v2.0
        scopes:
        - openid
        - profile
        clientId: <client id>
```

**Congratulations**

At this point, every interaction with Flyte components -be it in the UI or CLI- should require a successful login to your IdP, where your security policies are maintained and enforced.

## Configuring supported authorization flows

### PKCE

The Proof of Key Code Exchange protocol ([RFC 7636](https://tools.ietf.org/html/rfc7636)) is the default auth flow in Flyte and was designed to mitigate security risks in the communication between the authorization server and the resource server.

- **Good for**: user-to-system interaction with a web browser
- **Supported IdPs**: Google, Okta, Microsoft Entra ID, Keycloak.
- **Supported authorization servers**: internal(`flyteadmin`) or external

#### Client configuration

As this is the default flow, just verify that your `$HOME/.flyte/config.yaml` contains the following configuration:

```yaml
admin:
  authType: Pkce
```

### Client Credentials

- **Good for**: system-to-system communication where the client can securely store credentials (e.g. CI/CD).
- **Supported IdPs**: Google, Okta, Microsoft Entra ID, Keycloak.
- **Supported authorization servers**: internal(`flyteadmin`) or external

#### Client configuration

Verify that your `$HOME/.flyte/config.yaml` includes the following configuration:

```yaml
admin:
  endpoint: <your_flyteadmin_endpoint>
  authType: ClientSecret
  clientId: <your_clientID> #provided by your IdP
  clientSecretLocation: /etc/secrets/client_secret
```
`client_secret` is a file in the local filesystem that just contains the client secret provided by your IdP in plain text.

### Device Code

- **Good for**: “headless” devices or apps where the user cannot directly interact with a browser
- **Supported IdPs**: Google, Okta, Microsoft Entra ID, Keycloak.
- **Supported authorization servers**: external auth server **ONLY**

#### Client configuration

Verify that your `$HOME/.flyte/config.yaml` includes the following configuration:

```yaml
admin:
  endpoint: <your_flyteadmin_endpoint>
  authType: DeviceFlow
  clientId: <your_clientID> #provided by your IdP
```
A succesful response here it's a link with an authorization code you can use in a system with a browser to complete the auth flow.

## Disable Helm secret management

You can instruct Helm not to create and manage the secret for `flytepropeller`. In that case, you'll have to create it following these steps:


1. Disable Helm secrets management in your values file

```yaml

   secrets:
     adminOauthClientCredentials:
       enabled: true # enable mounting the flyte-secret-auth secret to the flytepropeller.
       clientSecret: null # disable Helm from creating the flyte-secret-auth secret.
       # Replace with the client_id provided by provided by your IdP for flytepropeller.
       clientId: <client_id>
```
2. Create a secret declaratively:

```yaml

   apiVersion: v1
   kind: Secret
   metadata:
    name: flyte-secret-auth
    namespace: flyte
   type: Opaque
   stringData:
  # Replace with the client_secret provided by your IdP for flytepropeller.
     client_secret: <client_secret>
```
`flytepropeller` then will mount this secret.

## Continuous Integration - CI


If your organization does any automated registration, then you'll need to authenticate using the [Client Credentials](#client-credentials) flow.

### Flytekit / pyflyte

Flytekit configuration variables are automatically designed to look up values from relevant environment variables.


However, to aid with continuous integration use-cases, Flytekit configuration can also reference other environment variables.

For instance, if your CI system is not capable of setting custom environment variables like
`FLYTE_CREDENTIALS_CLIENT_SECRET` but does set the necessary settings under a different variable, you may use
`export FLYTE_CREDENTIALS_CLIENT_SECRET_FROM_ENV_VAR=OTHER_ENV_VARIABLE` to redirect the lookup.
Also, `FLYTE_CREDENTIALS_CLIENT_SECRET_FROM_FILE` redirect is available as well, where the value should be the full path to the file containing the value for the configuration setting, in this case, the client secret.

The following is a list of flytekit configuration values the community has used in CI, along with a brief explanation:

```bash

# When using OAuth2 service auth, this is the username and password.
export FLYTE_CREDENTIALS_CLIENT_ID=<client_id>
export FLYTE_CREDENTIALS_CLIENT_SECRET=<client_secret>

# This tells the SDK to use basic authentication. If not set, Flytekit will assume you want to use the standard PKCE flow.
export FLYTE_CREDENTIALS_AUTH_MODE=basic

# This value should be set to conform to this
# `header config <https://github.com/flyteorg/flyteadmin/blob/12d6aa0a419ccec81b4c8289fd172e70a2ded525/auth/config/config.go#L124-L128>`_
# on the Admin side.
export FLYTE_CREDENTIALS_AUTHORIZATION_METADATA_KEY=<header name>

# When using basic authentication, you'll need to specify a scope to the IDP (instead of `openid`, which is
# only for OAuth). Set that here.
export FLYTE_CREDENTIALS_OAUTH_SCOPES=<idp defined scopes>

# Set this to force Flytekit to use authentication, even if not required by Admin. This is useful as you're
# rolling out the requirement.
export FLYTE_PLATFORM_AUTH=True
```


