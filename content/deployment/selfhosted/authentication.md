---
title: Authentication
weight: 5
variants: -flyte +union
---

# Authentication

{{< key product_name >}} self-hosted deployments use [OpenID Connect (OIDC)](https://openid.net/specs/openid-connect-core-1_0.html) for user authentication and [OAuth 2.0](https://tools.ietf.org/html/rfc6749) for service-to-service authorization.

Unlike serverless and BYOC deployments where {{< key product_name >}} manages authentication for you, **self-hosted deployments require you to create and manage OAuth applications in your own identity provider** (e.g. Okta, Microsoft Entra ID, Google Workspace, or any OIDC-compliant provider). {{< key product_name >}} does not provision or manage these applications — you are responsible for their lifecycle, credential rotation, and access policies.

> [!NOTE]
> This guide covers authentication for **self-hosted** deployments where you manage both the control plane and data plane. For **self-managed** deployments ({{< key product_name >}}-hosted control plane), authentication is handled automatically via `uctl selfserve provision-dataplane-resources` and `uctl create apikey`.

## Overview

Self-hosted authentication requires creating **five OAuth2 client applications** in your own identity provider. Each application serves a different authentication flow:

| # | Application | Type | Grant types | Purpose |
|---|-------------|------|-------------|---------|
| 1 | Browser login | Confidential (web) | `authorization_code`, `refresh_token`, `client_credentials` | Console/web UI login |
| 2 | CLI | Public (native) | `authorization_code`, `refresh_token`, `device_code` | `uctl` / `flytectl` CLI authentication via PKCE |
| 3 | Service-to-service | Confidential (service) | `client_credentials` | Control plane inter-service communication through NGINX |
| 4 | Operator | Confidential (service) | `client_credentials` | Data plane operator, propeller, and cluster-resource-sync authentication to control plane |
| 5 | EAGER | Confidential (service) | `client_credentials` | Task pod authentication (EAGER_API_KEY) |

## Identity provider requirements

You must use an OIDC-compliant identity provider that you manage outside of {{< key product_name >}}. Any standards-compliant provider will work. {{< key product_name >}} uses [Okta](https://www.okta.com/) for its internal deployments, but you can use whichever provider your organization already uses.

Your identity provider must support:

1. **OpenID Connect Discovery** — `/.well-known/openid-configuration` or `/.well-known/oauth-authorization-server` endpoint
2. **Authorization Code flow** — for browser and CLI login
3. **Client Credentials flow** — for service-to-service tokens
4. **PKCE** (Proof Key for Code Exchange) — for the CLI public client
5. **Custom scopes** — ability to create an `all` scope (or equivalent)
6. **Custom claims** — ability to emit `sub` and `preferred_username` claims in access tokens. An identity type claim (`identitytype` or equivalent) is recommended for authorization.

### Authorization server setup

Create a custom authorization server (or equivalent) in your identity provider. The setup differs by provider:

{{< tabs >}}
{{< tab "Okta" >}}
{{< markdown >}}
Create a **Custom Authorization Server** in Okta:

- **Audience**: `https://<your-domain>` (the control plane ingress domain)
- **Default scope**: `all`
- **Metadata URL**: `.well-known/oauth-authorization-server` (Okta-specific, not the standard `openid-configuration`)
- **Claims** (add as access token claims):
  - `sub` — Okta populates this natively. For client_credentials tokens, `sub` equals the app's Client ID.
  - `identitytype` — set to `"user"` for user tokens, `"app"` for client_credentials tokens
  - `preferred_username` — set to the user's login for user tokens, or the app's Client ID for app tokens
{{< /markdown >}}
{{< /tab >}}
{{< tab "Entra ID" >}}
{{< markdown >}}
Register an **App Registration** in Microsoft Entra ID:

- **App ID URI**: `api://<app-name>` (this becomes the audience)
- **Metadata URL**: `.well-known/openid-configuration` (standard OIDC)
- **Scopes**: Create two custom scopes on the app registration:
  - `all` — delegated scope for browser login (authorization_code flow)
  - `/.default` — used automatically for client_credentials flow
- **Claims** — configure via the app manifest's `optionalClaims`:
  - `sub` — Entra populates this natively. For client_credentials tokens, `sub` equals the **Service Principal Object ID** (not the Client ID).
  - `idtyp` — add as an optional access token claim. Emits `"app"` for client_credentials tokens (maps to the `identitytype` concept).
  - `preferred_username` — included by default for user tokens

> [!WARNING]
> Entra ID uses `sub` = Service Principal Object ID for client_credentials tokens, not the Client ID. When configuring trusted identities for service-to-service auth, use the SP Object ID (found in Enterprise Applications, not App Registrations).

> [!NOTE]
> Entra ID requires different scopes for different flows:
> - **Browser login** (authorization_code): `api://<app-name>/all` — Entra rejects `/.default` for same-app auth_code flows (error `AADSTS90009`)
> - **CLI** (authorization_code + PKCE): `api://<app-name>/.default`
> - **Service-to-service** (client_credentials): `api://<app-name>/.default`
{{< /markdown >}}
{{< /tab >}}
{{< tab "Generic OIDC" >}}
{{< markdown >}}
For other OIDC providers (Keycloak, Authentik, Auth0, etc.):

- **Audience**: `https://<your-domain>` or a custom resource identifier
- **Metadata URL**: Usually `.well-known/openid-configuration`
- **Scopes**: Create an `all` scope (or use your provider's default scope)
- **Claims**: Ensure access tokens include:
  - `sub` — a stable identifier for the authenticated principal
  - `preferred_username` — display name for identity injection
  - An identity type claim is optional but recommended for authorization

If your IdP cannot emit an `identitytype` claim, see the [identity type claim requirements](#identity-type-claim-requirements) section below.

If your IdP's client_credentials tokens omit the `sub` claim, configure `subjectClaimNames` to specify a fallback chain (e.g., `["sub", "client_id", "azp"]`).
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

### Identity type claim requirements

{{< key product_name >}} uses an identity type claim to distinguish human users from service applications. This distinction is **required for Union (built-in RBAC) authorization** and affects how access control decisions are made.

Your IdP must emit a claim that maps to the `identitytype` concept, with values that distinguish user tokens from application tokens. The claim name and values are configurable:

| Provider | Claim name | User value | App value | Configuration |
|----------|-----------|------------|-----------|---------------|
| Okta | `identitytype` | `"user"` | `"app"` | Custom access token claim on authorization server |
| Entra ID | `idtyp` | (not emitted) | `"app"` | Enable via optional claims in app manifest. Map with `identityTypeClaimsForApps: {idtyp: ["app"]}` |
| Generic | varies | varies | varies | Configure `identityTypeClaimsForApps` to map your claim name and values |

> [!WARNING]
> **Union authorization mode requires identity type resolution.** If your IdP cannot emit any claim that distinguishes users from applications, you must either:
> 1. Set `global.USE_EXTERNAL_IDENTITY: true` — the platform will infer identity type from the authentication context (e.g., whether the token was issued via authorization_code or client_credentials flow). This works for basic cases but may not cover all scenarios.
> 2. Use **External authorization mode** instead of Union mode — your external authorization server can determine identity type from the JWT payload, `sub` claim, or any other token attribute directly, without relying on the platform's identity type resolution.
>
> Without identity type resolution, Union authorization cannot distinguish user requests from service account requests, which may result in incorrect access control decisions.

### Subject claim requirements

{{< key product_name >}} uses the JWT `sub` claim as the **primary identifier** for all callers — users and service accounts alike. This value is used for:

- **Authorization decisions** — matching callers to roles and permissions
- **Trusted identity validation** — verifying internal service-to-service callers
- **Audit logging** — recording who performed each action
- **Resource ownership** — the "Owned By" relationship in the console

> [!WARNING]
> The `sub` claim value must be **stable and unique** per principal. If your IdP returns different `sub` values for the same user across token refreshes, authorization and ownership tracking will break.

**Your IdP must emit a `sub` claim in all access tokens.** If your IdP's client_credentials tokens use a different claim for the caller identity (or omit `sub` entirely), configure `subjectClaimNames` to specify a fallback chain:

```yaml
# In flyte.configmap.adminServer.auth.appAuth.externalAuthServer:
subjectClaimNames:
  - sub          # Standard OIDC subject (tried first)
  - client_id    # OAuth2 client ID (common fallback)
  - azp          # Authorized party (alternative)
```

The platform tries each claim in order and uses the first non-empty value as the caller's identity.

> [!NOTE]
> **Provider-specific `sub` values:**
> - **Okta**: `sub` equals the Client ID for client_credentials tokens and the user's Okta ID for user tokens.
> - **Entra ID**: `sub` equals the **Service Principal Object ID** for client_credentials tokens (not the Client ID). Find this in Entra ID > Enterprise Applications > your app > Object ID.
> - When configuring trusted identities for internal services (e.g., `INTERNAL_SUBJECT_ID`), use the value that your IdP places in the `sub` claim — not necessarily the Client ID.

## Step 1: Create OAuth2 applications

### Application 1: Browser login (Confidential)

Used by the web console for user authentication.

| Property | Value |
|----------|-------|
| Type | Web (confidential client) |
| Grant types | `authorization_code`, `refresh_token`, `client_credentials` |
| Redirect URI | `https://<your-domain>/callback` |
| Post-logout redirect URI | `https://<your-domain>/logout` |
| Scopes | `openid`, `profile`, `offline_access` |

Note the **Client ID** (used as `OIDC_CLIENT_ID`) and the **Client Secret** (stored in Kubernetes secrets).

### Application 2: CLI (Public)

Used by `uctl` and `flytectl` for CLI-based authentication with PKCE.

| Property | Value |
|----------|-------|
| Type | Native (public client) |
| Grant types | `authorization_code`, `refresh_token`, `device_code` |
| Redirect URIs | `http://localhost:53593/callback`, `http://localhost:12345/callback` |
| PKCE | Required |
| Client authentication | None (PKCE only, no client secret) |

Note the **Client ID** (used as `CLI_CLIENT_ID`).

### Application 3: Service-to-service (Confidential)

Used by control plane services (executions, cluster, identity, etc.) to authenticate with each other through NGINX when OIDC is enabled.

| Property | Value |
|----------|-------|
| Type | Service (confidential client) |
| Grant types | `client_credentials` |

Note the **Client ID** (used as `INTERNAL_CLIENT_ID`) and the **Client Secret** (stored in Kubernetes secrets).

### Application 4: Operator (Confidential)

Used by data plane services (operator, propeller, cluster-resource-sync) to authenticate to the control plane.

| Property | Value |
|----------|-------|
| Type | Service (confidential client) |
| Grant types | `client_credentials` |

Note the **Client ID** (used as `AUTH_CLIENT_ID` in data plane configuration) and the **Client Secret** (stored in Kubernetes secrets).

### Application 5: EAGER (Confidential)

Used for task pod authentication. The encoded credentials form the `EAGER_API_KEY`.

| Property | Value |
|----------|-------|
| Type | Service (confidential client) |
| Grant types | `client_credentials` |

Note the **Client ID** and **Client Secret** — these are encoded into the EAGER_API_KEY.

## Step 2: Configure control plane

Authentication is configured in the `flyte.configmap.adminServer.auth` block in your control plane Helm values. This block defines how the admin service validates tokens, which clients are trusted, and how browser login works.

You also need to set a few global variables for service-to-service authentication:

```yaml
global:
  INTERNAL_CLIENT_ID: "<service-to-service-client-id>"  # App 3
  AUTH_TOKEN_URL: "<token-endpoint-url>"                 # OAuth2 token endpoint
  OIDC_S2S_SCOPE: ""                                    # Leave empty for Okta, set to "api://<app>/.default" for Entra ID
```

Then configure the auth block. Select your identity provider below:

{{< tabs >}}
{{< tab "Okta" >}}
{{< markdown >}}
```yaml
flyte:
  configmap:
    adminServer:
      server:
        security:
          useAuth: true
      auth:
        appAuth:
          authServerType: External
          externalAuthServer:
            baseUrl: "https://dev-123456.okta.com/oauth2/default"
            metadataUrl: ".well-known/oauth-authorization-server"
            allowedAudience:
              - "https://<your-domain>"
          thirdPartyConfig:
            flyteClient:
              clientId: "<cli-client-id>"           # App 2
              redirectUri: "http://localhost:53593/callback"
              scopes:
                - all
        userAuth:
          openId:
            baseUrl: "https://dev-123456.okta.com/oauth2/default"
            clientId: "<browser-login-client-id>"   # App 1
            scopes:
              - profile
              - openid
              - offline_access
          cookieSetting:
            sameSitePolicy: LaxMode
            domain: "<your-domain>"
```

Set globals:
```yaml
global:
  INTERNAL_CLIENT_ID: "<service-to-service-client-id>"
  AUTH_TOKEN_URL: "https://dev-123456.okta.com/oauth2/default/v1/token"
  OIDC_S2S_SCOPE: ""   # Okta defaults to "all"
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Entra ID" >}}
{{< markdown >}}
```yaml
flyte:
  configmap:
    adminServer:
      server:
        security:
          useAuth: true
      auth:
        appAuth:
          authServerType: External
          externalAuthServer:
            baseUrl: "https://login.microsoftonline.com/<tenant-id>/v2.0"
            metadataUrl: ".well-known/openid-configuration"
            allowedAudience:
              - "api://<app-name>"
            # Entra client_credentials tokens use SP Object ID as sub, not client_id.
            # Configure fallback chain:
            subjectClaimNames:
              - sub
              - client_id
            # Map Entra's idtyp claim to internal identitytype:
            identityTypeClaimsForApps:
              idtyp:
                - app
          thirdPartyConfig:
            flyteClient:
              clientId: "<cli-client-id>"           # App 2
              redirectUri: "http://localhost:53593/callback"
              scopes:
                - "api://<app-name>/.default"
              audience: "api://<app-name>"
        userAuth:
          openId:
            baseUrl: "https://login.microsoftonline.com/<tenant-id>/v2.0"
            clientId: "<browser-login-client-id>"   # App 1
            scopes:
              - profile
              - openid
              - offline_access
              - "api://<app-name>/all"
          cookieSetting:
            sameSitePolicy: LaxMode
            domain: "<your-domain>"
```

Set globals:
```yaml
global:
  INTERNAL_CLIENT_ID: "<service-to-service-client-id>"
  AUTH_TOKEN_URL: "https://login.microsoftonline.com/<tenant-id>/oauth2/v2.0/token"
  OIDC_S2S_SCOPE: "api://<app-name>/.default"
```

> [!NOTE]
> `INTERNAL_SUBJECT_ID` defaults to `INTERNAL_CLIENT_ID` for backward compatibility. For Entra ID, where the token `sub` claim is the Service Principal Object ID (not the Client ID), set `INTERNAL_SUBJECT_ID` to the SP Object ID. Find this in **Entra ID > Enterprise Applications > your app > Object ID**.
{{< /markdown >}}
{{< /tab >}}
{{< tab "Generic OIDC" >}}
{{< markdown >}}
```yaml
flyte:
  configmap:
    adminServer:
      server:
        security:
          useAuth: true
      auth:
        appAuth:
          authServerType: External
          externalAuthServer:
            baseUrl: "<issuer-url>"
            metadataUrl: ".well-known/openid-configuration"
            allowedAudience:
              - "<audience>"
          thirdPartyConfig:
            flyteClient:
              clientId: "<cli-client-id>"           # App 2
              redirectUri: "http://localhost:53593/callback"
              scopes:
                - all
        userAuth:
          openId:
            baseUrl: "<issuer-url>"
            clientId: "<browser-login-client-id>"   # App 1
            scopes:
              - profile
              - openid
              - offline_access
          cookieSetting:
            sameSitePolicy: LaxMode
            domain: "<your-domain>"
```

Set globals:
```yaml
global:
  INTERNAL_CLIENT_ID: "<service-to-service-client-id>"
  AUTH_TOKEN_URL: "<issuer-url>/token"      # Your IdP's token endpoint
  OIDC_S2S_SCOPE: ""                        # Set if your IdP requires a specific scope for client_credentials
```

If your IdP's client_credentials tokens don't include a `sub` claim, add:
```yaml
            subjectClaimNames:
              - sub
              - client_id
              - azp
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

> [!NOTE]
> Setting `useAuth: true` is required for the `/login`, `/callback`, and `/me` endpoints to register. Without this, auth endpoints will return 404.

> [!NOTE]
> **Deprecated globals:** `OIDC_BASE_URL`, `OIDC_CLIENT_ID`, and `CLI_CLIENT_ID` are deprecated but still functional. New deployments should use the `auth` block directly as shown above. Existing deployments using these globals will continue to work.

## Step 3: Create Kubernetes secrets (control plane)

The control plane needs secrets for the browser login app (App 1) and the service-to-service app (App 3):

```shell
# Secret for admin service (mounted at /etc/secrets/)
# Note: "flyte-admin-secrets" is the default name expected by the Helm chart
kubectl create secret generic flyte-admin-secrets \
  --from-literal=client_secret='<BROWSER_LOGIN_CLIENT_SECRET>' \
  -n <controlplane-namespace>

# Secret for scheduler (mounted at /etc/secrets/)
# Note: "flyte-secret-auth" is the default name expected by the Helm chart
kubectl create secret generic flyte-secret-auth \
  --from-literal=client_secret='<BROWSER_LOGIN_CLIENT_SECRET>' \
  -n <controlplane-namespace>

# Add service-to-service client secret to the controlplane secrets
kubectl create secret generic <controlplane-secrets> \
  --from-literal=pass.txt='<DB_PASSWORD>' \
  --from-literal=client_secret='<SERVICE_TO_SERVICE_CLIENT_SECRET>' \
  -n <controlplane-namespace> --dry-run=client -o yaml | kubectl apply -f -
```

> [!NOTE]
> For production, use External Secrets Operator or a similar tool to sync secrets from your cloud provider's secret manager (AWS Secrets Manager, GCP Secret Manager, Azure Key Vault).

## Step 4: Configure data plane

Add the operator client ID to your data plane overrides file:

```yaml
global:
  AUTH_CLIENT_ID: "<operator-client-id>"  # App 4
```

Create the data plane auth secret:

```shell
kubectl create secret generic union-secret-auth \
  --from-literal=client_secret='<OPERATOR_CLIENT_SECRET>' \
  -n <dataplane-namespace>
```

## Step 5: Configure EAGER_API_KEY

The EAGER_API_KEY is a base64-encoded string containing the EAGER app credentials. It enables task pods to authenticate to the control plane.

Generate the key:

```shell
# Format: base64("<domain>:<eager-client-id>:<eager-client-secret>:")
echo -n "<your-domain>:<eager-client-id>:<eager-client-secret>:" | base64
```

Create the Kubernetes secret in the data plane namespace:

```shell
kubectl create secret generic <eager-secret-name> \
  --from-literal=<eager-secret-key>='<BASE64_ENCODED_EAGER_API_KEY>' \
  -n <dataplane-namespace>
```

> [!NOTE]
> The exact secret name and key depend on your deployment's embedded K8s secret manager configuration. The secret name is typically an MD5 hash of a logical identifier. Contact {{< key product_name >}} support for the exact values for your organization.

## Step 6: Deploy

Deploy or upgrade both the control plane and data plane with the updated configurations:

```shell
# Upgrade control plane
helm upgrade unionai-controlplane unionai/controlplane \
  --namespace <controlplane-namespace> \
  -f values.<cloud>.selfhosted-intracluster.yaml \
  -f values.registry.yaml \
  -f values.<cloud>.selfhosted-overrides.yaml \
  --timeout 15m --wait

# Upgrade data plane
helm upgrade unionai-dataplane unionai/dataplane \
  --namespace <dataplane-namespace> \
  -f values.<cloud>.selfhosted-intracluster.yaml \
  -f values.<cloud>.selfhosted-overrides.yaml \
  --timeout 10m --wait
```

## Verification

```shell
# Check admin service logs for auth initialization
kubectl logs -n <controlplane-namespace> deploy/<admin-service> | grep -i auth

# Test the /me endpoint (should return 401 without a token)
kubectl exec -n <controlplane-namespace> deploy/<admin-service> -- \
  curl -s -o /dev/null -w "%{http_code}" \
  https://<controlplane-ingress>.<controlplane-namespace>.svc.cluster.local/me -k

# Test CLI login
uctl config init --host https://<your-domain>
uctl get project

# Check data plane operator auth
kubectl logs -n <dataplane-namespace> -l app.kubernetes.io/name=operator --tail=50 | grep -i "token\|auth"
```

## Summary of secrets

| Secret name | Namespace | Keys | Source |
|-------------|-----------|------|--------|
| `flyte-admin-secrets` (Helm chart default) | `<controlplane-namespace>` | `client_secret` | Browser login app (App 1) secret |
| `flyte-secret-auth` (Helm chart default) | `<controlplane-namespace>` | `client_secret` | Browser login app (App 1) secret |
| `<controlplane-secrets>` | `<controlplane-namespace>` | `pass.txt`, `client_secret` | DB password, Service-to-service app (App 3) secret |
| `union-secret-auth` | `<dataplane-namespace>` | `client_secret` | Operator app (App 4) secret |
| EAGER secret | `<dataplane-namespace>` | varies | EAGER app (App 5) encoded key |

## Self-hosted vs. self-managed authentication

| Aspect | Self-hosted | Self-managed |
|--------|------------|--------------|
| OAuth app creation | Manual — create all 5 apps | Automatic — `uctl selfserve provision-dataplane-resources` creates apps 1-3 |
| EAGER_API_KEY | Manual — encode and create secret | Automatic — `uctl create apikey` generates and provisions |
| Control plane auth | Configure via Helm values | Managed by {{< key product_name >}} |
| Data plane auth | Configure `AUTH_CLIENT_ID` and secret | Provisioned by `uctl selfserve` |

## Troubleshooting

### Admin service auth endpoints return 404

Ensure `useAuth: true` is set under `flyte.configmap.adminServer.server.security`. Without this, the `/login`, `/callback`, and `/me` endpoints are not registered.

### Token validation fails with "audience mismatch"

The `allowedAudience` in the admin service configuration must include `https://<your-domain>`. This should match the audience configured on your authorization server.

### Data plane cannot authenticate to control plane

```shell
# Verify AUTH_CLIENT_ID is set
kubectl get configmap -n <dataplane-namespace> -o yaml | grep -i auth_client

# Check that union-secret-auth exists
kubectl get secret union-secret-auth -n <dataplane-namespace> \
  -o jsonpath='{.data.client_secret}' | base64 -d

# Check operator logs
kubectl logs -n <dataplane-namespace> -l app.kubernetes.io/name=operator --tail=50 \
  | grep -i "auth\|token\|401"
```

### CLI login fails

Ensure the CLI app (App 2) redirect URIs include `http://localhost:53593/callback` and PKCE is enabled. Test with:

```shell
uctl config init --host https://<your-domain>
uctl get project
```

### Entra ID: `AADSTS90009` on browser login

This error occurs when using the `/.default` scope with an authorization_code flow on the same app. Entra ID requires a named delegated scope (e.g., `api://<app-name>/all`) for browser login. Check that `userAuth.openId.scopes` includes `api://<app-name>/all` and not `/.default`.

### Entra ID: `AADSTS1002012` invalid_scope for service-to-service

Client_credentials flows in Entra ID require the `/.default` scope. Ensure `OIDC_S2S_SCOPE` is set to `api://<app-name>/.default` in your globals.

### Subject not found in token

If flyteadmin logs show `subject claim not found`, your IdP's client_credentials tokens may not include a `sub` claim. Configure `subjectClaimNames` in the auth block to specify a fallback chain (e.g., `["sub", "client_id"]`).
