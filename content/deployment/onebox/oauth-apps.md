---
title: OAuth apps
description: Give scripts and CI their own credentials, either created in your identity provider or registered by onebox through OAuth 2.0 Dynamic Client Registration.
icon: key
weight: 10
variants: -flyte +union
---

# OAuth apps

An OAuth app is a client ID and secret that scripts and CI use instead of a person's sign-in. It gets a token with the client credentials grant, and onebox treats requests with that token as the app: the app has its own role, and runs it starts are attributed to it.

Choose who creates apps with `apps.provider`:

| `apps.provider` | Apps are created | Use when |
|---|---|---|
| `none` (default) | In your identity provider, by its admins | Your IdP doesn't support Dynamic Client Registration, or you manage clients there anyway. |
| `dcr` | By users, through onebox, at your IdP's Dynamic Client Registration endpoint (RFC 7591), and managed with RFC 7592 | Your IdP supports both RFCs, such as Keycloak. |

Either way, the proxy in front of onebox must accept the apps' tokens. See [Authentication](./authentication).

## Apps created in your IdP (`none`)

Create a client with the client credentials grant in your IdP, and use its ID and secret. Every app call through onebox, from the CLI or the UI, fails with `FAILED_PRECONDITION` and says apps are managed in your identity provider.

With authorization on, an app is identified by the subject its tokens carry, and gets `authz.defaultRole` the first time it makes a request.

## Apps registered by onebox (`dcr`)

Onebox registers the client at your IdP and returns its secret once. Onebox keeps each app's ID, name, creator, and the per-client management credentials RFC 7592 requires, in its database. It doesn't keep the secret. Deleting an app deletes the client at the IdP.

### Keycloak

1. Make every token carry the audience your proxy checks. Create a client scope with an audience mapper (for example audience `onebox`) and add it to the realm's default client scopes, so dynamically registered clients get it too.
2. Create an initial access token for client registration (Realm settings → Client registration → Initial access token, or `kcadm.sh create clients-initial-access -r <realm> -s count=1000 -s expiration=0`), and store it:

   ```shell
   kubectl -n union create secret generic onebox-dcr --from-literal=token='<initial access token>'
   ```

3. Configure onebox:

   ```yaml
   apps:
     provider: dcr
     dcr:
       registrationEndpoint: https://<keycloak>/realms/<realm>/clients-registrations/openid-connect
       initialAccessToken:
         existingSecret: onebox-dcr
   ```

   Leave `apps.dcr.scope` unset on Keycloak. Keycloak then gives each registered client the realm's default client scopes, including the audience scope from step 1. A scope set here becomes the client's only scope, and Keycloak adds it to a token only when the token request asks for it, so the SDK's app sign-ins would get tokens without the audience.

4. Let oauth2-proxy accept the apps' tokens: `--oidc-extra-audience=<audience>` and `--insecure-oidc-allow-unverified-email=true`, since client-credentials tokens have no email.

### Use an app

Create it as a user who may manage apps (an admin with authorization on). The response carries the secret, once. Then run with it:

```python
import flyte

flyte.init(
    endpoint="dns:///<host>",
    auth_type="ClientSecret",
    client_id="<client id>",
    client_credentials_secret="<client secret>",
    org="onebox", project="default", domain="development",
)
```

Requests with the app's token act as the app. The proxy verifies the token and tells onebox who the caller is, and onebox recognizes a registered app by what the proxy reports: a subject that is the app's client ID (Okta; Auth0's `<client id>@clients`), or Keycloak's `service-account-<client id>` username. Onebox doesn't read the token itself.

## Gotchas

| Symptom | Cause and fix |
|---|---|
| Creating an app fails with `PERMISSION_DENIED` from the identity provider | The initial access token is missing, expired, or used up. Create a new one. |
| An app's token is redirected to the IdP | The proxy doesn't accept it. See the oauth2-proxy troubleshooting in [Authentication](./authentication#troubleshooting). |
| Runs by an app show as a user | The proxy reports an identity onebox doesn't recognize as the app, or an email (users have one, apps don't). Check the headers the proxy sets: the subject should be the client ID, or on Keycloak the preferred username `service-account-<client id>` (oauth2-proxy sends it in `X-Forwarded-Preferred-Username` with `--pass-user-headers`). |
