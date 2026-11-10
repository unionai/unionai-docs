---
title: Authentication
description: Configure OIDC user authentication and OAuth 2.0 service authorization.
icon: shield-lock
weight: 2
variants: -flyte -union
mermaid: true
---

# Authentication

Union.ai uses [OpenID Connect (OIDC)](https://openid.net/specs/openid-connect-core-1_0.html) for user authentication and [OAuth 2.0](https://tools.ietf.org/html/rfc6749) for service-to-service authorization.

## Prerequisites

- The client ID and client secret Union.ai provides for your cluster, from `uctl selfserve provision-dataplane-resources` (see [Deploy the data plane](../../deploy)).
- A secret management solution for delivering client secrets to pods (e.g., External Secrets Operator with AWS Secrets Manager, HashiCorp Vault, or native Kubernetes secrets).

## Dataplane Helm configuration

All data plane services authenticate with the same client credentials: the client ID and secret Union.ai provides for your cluster. Use the client ID as `AUTH_CLIENT_ID` and store the secret in the `union-secret-auth` Kubernetes secret (see [Secret delivery](#secret-delivery)).

### Dataplane global variables

```yaml
global:
  AUTH_CLIENT_ID: "<service-client-id>"
```

### Cluster resource sync

```yaml
clusterresourcesync:
  config:
    union:
      auth:
        enable: true
        type: ClientSecret
        clientId: "<service-client-id>"
        clientSecretLocation: "/etc/union/secret/client_secret"
        authorizationMetadataKey: flyte-authorization
        tokenRefreshWindow: 5m
```

### Operator (union service auth)

```yaml
config:
  union:
    auth:
      enable: true
      type: ClientSecret
      clientId: "<service-client-id>"
      clientSecretLocation: "/etc/union/secret/client_secret"
      authorizationMetadataKey: flyte-authorization
      tokenRefreshWindow: 5m
```

### Propeller admin client

```yaml
config:
  admin:
    admin:
      clientId: "<service-client-id>"
      clientSecretLocation: "/etc/union/secret/client_secret"
```

### In-pod control plane authentication (EAGER_API_KEY)

Flyte task pods may need to call back into the Union.ai control plane during execution: to launch sub-tasks, fetch remote references, run apps that make programmatic API calls, and similar. The `EAGER_API_KEY` secret holds the OAuth2 client credentials used to authenticate those calls. (The "eager" prefix is a Flyte 1.x holdover; the key is needed for every task pod that may reach the control plane, not just eager workflows. There is no separate eager-mode toggle in Flyte 2.x.)

The executor injects the secret into task pods via:

```yaml
executor:
  config:
    unionAuth:
      injectSecret: true
      secretName: EAGER_API_KEY
```

#### Provisioning

The Union.ai operator provisions this key for you: no manual step and no support request are needed. On each reconciliation tick the operator checks whether the key already exists; if it does not, the operator mints one on the control plane and writes it into the cluster through the local operator proxy. Once the key is in place the check is a no-op, so the loop is safe to run continuously and re-provisions the key automatically if it is ever removed.

Self-provisioning is active when secret management is enabled, which is the chart default:

```yaml
proxy:
  secretManager:
    enabled: true
```

If you disable secret management, the operator cannot store the key and you must deliver the `EAGER_API_KEY` secret yourself, following the same [External Secrets Operator](#option-a-external-secrets-operator-recommended) pattern used for the client secrets below.

### Data plane secrets

Enable the `union-secret-auth` Kubernetes secret mount for data plane pods:

```yaml
secrets:
  admin:
    enable: true
    create: false
    clientId: "<service-client-id>"
    clientSecret: "placeholder"
```

> [!NOTE]
> `create: false` means the chart does not create the `union-secret-auth` Kubernetes Secret. You must provision it externally (see [Secret delivery](#secret-delivery)). Setting `clientSecret: "placeholder"` with `create: true` is also supported if you want the chart to create the secret and then overwrite it via External Secrets Operator.

## Secret delivery

Client secrets must be delivered to pods as files mounted into the container filesystem. The table below lists the required Kubernetes secret, its mount path, and which components use it:

| Kubernetes Secret | Mount Path | Components | Namespace |
| --- | --- | --- | --- |
| `union-secret-auth` | `/etc/union/secret/` | operator, propeller, CRS | `union` |

The secret must contain a key named `client_secret` with the client secret value.

### Option A: External Secrets Operator (recommended)

If you use [External Secrets Operator (ESO)](https://external-secrets.io/) with a cloud secret store, create an `ExternalSecret` resource that syncs the client secret into the Kubernetes secret:

```yaml
apiVersion: external-secrets.io/v1
kind: ExternalSecret
metadata:
  name: union-secret-auth
  namespace: union
spec:
  secretStoreRef:
    name: default
    kind: SecretStore
  refreshInterval: 1h
  target:
    name: union-secret-auth
    creationPolicy: Merge
    deletionPolicy: Retain
  data:
    - secretKey: client_secret
      remoteRef:
        key: "<your-secret-store-key>"
```

> [!NOTE]
> `creationPolicy: Merge` ensures the ExternalSecret adds the `client_secret` key alongside any existing keys in the target secret.

### Option B: Direct Kubernetes secrets

If you manage secrets directly:

```bash
# Dataplane — operator, propeller, CRS
kubectl create secret generic union-secret-auth \
  --from-literal=client_secret='<SERVICE_CLIENT_SECRET>' \
  -n union
```

## SDK and CLI authentication

The SDK and CLI use PKCE (Proof Key for Code Exchange) for interactive authentication:

1. The SDK calls `AuthMetadataService/GetPublicClientConfig` (an unprotected endpoint) to discover the `flytectl` client ID and redirect URI.
2. The SDK opens a browser to the IdP's authorize endpoint with a PKCE challenge.
3. The user authenticates in the browser.
4. The IdP redirects to `localhost:53593/callback` with an authorization code.
5. The SDK exchanges the code for tokens and stores them locally.
6. Subsequent requests include the token in the `flyte-authorization` header.

No additional SDK configuration is required beyond the standard `flyte` connection config:

```yaml
admin:
  endpoint: dns:///<your-domain>
  authType: Pkce
  insecure: false
```

For headless environments (CI/CD), use the [Client Credentials](#client-credentials-for-cicd) flow instead.

### Client credentials for CI/CD

For automated pipelines, create a service app in your IdP and configure:

```yaml
admin:
  endpoint: dns:///<your-domain>
  authType: ClientSecret
  clientId: "<your-ci-client-id>"
  clientSecretLocation: "/path/to/client_secret"
```

Or set them with environment variables, which override the values in the config file. The SDK reads them only when it finds a config file, so keep one that sets at least `admin.endpoint`:

```bash
export FLYTE_ADMIN_CLIENTID="<your-ci-client-id>"
export FLYTE_ADMIN_CLIENTSECRETENVVAR=CI_CLIENT_SECRET  # name of the variable that holds the secret
export CI_CLIENT_SECRET="<your-ci-client-secret>"
export FLYTE_AUTH_TYPE=ClientSecret
```

## Troubleshooting

### Operator or propeller cannot authenticate

1. Verify `union-secret-auth` exists in the data plane namespace and contains `client_secret`.
2. Check operator logs for auth errors: `kubectl logs -n union -l app.kubernetes.io/name=operator --tail=50 | grep -i auth`.
3. Verify that `AUTH_CLIENT_ID` and `client_secret` match the client ID and secret from `uctl selfserve provision-dataplane-resources`.
