---
title: Identity
weight: 7
variants: -flyte +union
---

# Identity

The {{< key product_name >}} identity service provides **user and application management** for self-hosted deployments. It powers the **User Management** page in the console, enabling administrators to view, invite, and manage users and service accounts.

The identity service integrates with your identity provider to fetch user and application data. Without it, the User Management page displays a limited view based only on locally-cached authorization data.

## Prerequisites

Before configuring the identity service:

1. **Authentication is configured and working** — see the [authentication guide]({{< relref "authentication" >}})
2. **Authorization is configured** — see the [authorization guide]({{< relref "authorization" >}}). The User Management page is most useful with Union authorization mode enabled.

## Overview

The identity service acts as a bridge between your identity provider and the {{< key product_name >}} console:

| Feature | Without identity service | With identity service |
|---------|--------------------------|----------------------|
| View users | Only users who have logged in | All users from your IdP directory |
| View applications | Only bootstrapped service accounts | All registered OAuth applications |
| Invite users | Not available | Invite by email (creates authorization record) |
| User search | Limited to cached data | Search your IdP directory |

## Identity providers

The identity service supports multiple backend providers:

| Provider | Value | Description |
|----------|-------|-------------|
| **Noop** | `noop` | Identity service disabled. User Management shows only locally-cached authorization data. This is the default. |
| **Azure** | `azure` | Microsoft Entra ID (Azure AD). Fetches users and applications via Microsoft Graph API. |

> [!NOTE]
> Additional providers (Okta, Google Workspace) may be added in future releases. If you need a provider not listed here, contact {{< key product_name >}} support.

## Configuring the Azure provider (Entra ID)

The Azure provider uses the [Microsoft Graph API](https://learn.microsoft.com/en-us/graph/overview) to fetch users and applications from your Entra ID tenant.

### Step 1: Create an Entra ID app registration for Graph API

Create a **separate app registration** in Entra ID for the identity service. This app is distinct from the five OAuth apps used for authentication — it only needs Graph API permissions, not OIDC flows.

1. In the Azure portal, go to **Microsoft Entra ID** → **App registrations** → **New registration**
2. **Name**: `<your-org>-identity-service` (or similar)
3. **Supported account types**: Single tenant (this directory only)
4. **Redirect URI**: Leave blank (not needed for client_credentials)
5. Click **Register**

### Step 2: Configure API permissions

The identity service needs **Application permissions** (not Delegated) to manage users, groups, and applications:

1. Go to **API permissions** → **Add a permission** → **Microsoft Graph** → **Application permissions**
2. Add the following permissions:
   - `User.Read.All` — read all user profiles for the User Management page
   - `GroupMember.ReadWrite.All` — list and manage group members (required when `groupId` is configured)
   - `Application.ReadWrite.All` — create, update, and delete OAuth application registrations
3. Click **Grant admin consent for \<your-tenant\>**

> [!WARNING]
> These are high-privilege permissions that include write access. The identity service uses these permissions to:
> - Read user profiles for display in User Management
> - Manage group memberships when group-based access is configured
> - Create and manage OAuth application registrations for new service accounts
>
> Review your organization's security policies before granting admin consent. If your organization cannot grant write permissions, the identity service will have reduced functionality.

### Step 3: Create a client secret

1. Go to **Certificates & secrets** → **Client secrets** → **New client secret**
2. **Description**: `identity-service`
3. **Expires**: Choose an appropriate expiration (e.g., 24 months)
4. Click **Add** and **copy the secret value immediately** — you cannot retrieve it later

Store the secret in your secret management system (AWS Secrets Manager, GCP Secret Manager, HashiCorp Vault, etc.).

### Step 4: Note the required values

You'll need these values for Helm configuration. All values are found on the identity service app registration's **Overview** page in the Azure portal (**Microsoft Entra ID** → **App registrations** → **\<your-org\>-identity-service**):

| Value | Azure portal location |
|-------|----------------------|
| **Tenant ID** | **Directory (tenant) ID** field on the Overview page |
| **Client ID** | **Application (client) ID** field on the Overview page |
| **Client Secret** | The secret value you copied in Step 3 (not visible after creation) |

## Control plane Helm configuration

Configure the identity service in your controlplane Helm values:

```yaml
services:
  identity:
    configMap:
      identity:
        app:
          identityProviderConfig:
            provider: "azure"
            azure:
              tenantId: "<your-entra-tenant-id>"
              clientId: "<identity-service-app-client-id>"
              clientSecretName: "azure_client_secret"
              groupId: ""    # Optional: limit to users in a specific Entra group
```

### Configuration reference

| Field | Description |
|-------|-------------|
| `provider` | Identity provider backend. Set to `"azure"` for Entra ID, or `"noop"` to disable. |
| `azure.tenantId` | Your Microsoft Entra ID tenant ID (directory ID). |
| `azure.clientId` | The Application (client) ID of the identity service app registration. |
| `azure.clientSecretName` | The key name in the Kubernetes secret where the client secret is stored. The secret file is mounted at `/etc/secrets/union/`. |
| `azure.groupId` | _(Optional)_ Limit User Management to members of a specific Entra group. Leave empty to show all users in the tenant. |

### Secret delivery

The identity service reads the Graph API client secret from a file mounted at `/etc/secrets/union/<clientSecretName>`. Deliver this secret using External Secrets Operator or your preferred secret management approach.

#### External Secrets Operator (recommended)

Create an `ExternalSecret` that syncs the Graph API client secret into the controlplane service secret:

```yaml
apiVersion: external-secrets.io/v1
kind: ExternalSecret
metadata:
  name: identity-azure-secret
  namespace: union-cp
spec:
  secretStoreRef:
    name: default
    kind: SecretStore
  refreshInterval: 1h
  target:
    name: service-shared-secret    # The shared controlplane secret
    creationPolicy: Merge
    deletionPolicy: Retain
  data:
    - secretKey: azure_client_secret
      remoteRef:
        key: "<your-secret-store-path>"    # e.g., "staging/entraid/identity-service-client-secret"
```

> [!NOTE]
> `creationPolicy: Merge` adds the `azure_client_secret` key to the existing `service-shared-secret` Kubernetes secret without overwriting other keys.

#### Direct Kubernetes secret

If you manage secrets directly:

```bash
kubectl patch secret service-shared-secret -n union-cp \
  --type='json' \
  -p='[{"op": "add", "path": "/data/azure_client_secret", "value": "'$(echo -n '<YOUR_SECRET>' | base64)'"}]'
```

## Verifying the configuration

After deploying with the identity service configured:

1. **Check the identity pod is running**:
   ```bash
   kubectl get pods -n union-cp -l app.kubernetes.io/name=identity
   ```

2. **Check for configuration errors in logs**:
   ```bash
   kubectl logs -n union-cp deploy/identity --tail=50 | grep -i "error\|provider\|azure"
   ```

3. **Verify User Management in the console**:
   - Navigate to **Settings** → **Users** in the {{< key product_name >}} console
   - You should see users from your Entra ID tenant (not just users who have logged in)
   - The user count should match your Entra directory (or group, if `groupId` is configured)

## Troubleshooting

### User Management page shows "Unable to load users"

1. **Check identity pod logs** for Graph API errors:
   ```bash
   kubectl logs -n union-cp deploy/identity --tail=100 | grep -i "graph\|error\|unauthorized"
   ```

2. **Verify the client secret** is correctly mounted:
   ```bash
   kubectl exec -n union-cp deploy/identity -- cat /etc/secrets/union/azure_client_secret
   ```

3. **Verify API permissions** — ensure `User.Read.All` and `Application.Read.All` have admin consent in the Azure portal.

### Users appear but some are missing

1. **Check `groupId` configuration** — if set, only members of that group appear.

2. **Check Entra ID user status** — disabled or deleted users may be filtered out.

3. **Check pagination** — for large directories (>1000 users), verify the identity service handles Graph API pagination correctly by checking logs for pagination-related errors.

### Identity pod fails to start

1. **Check secret mount**:
   ```bash
   kubectl describe pod -n union-cp -l app.kubernetes.io/name=identity | grep -A5 "Mounts:"
   ```

2. **Check ExternalSecret sync status**:
   ```bash
   kubectl get externalsecret -n union-cp
   ```
   All ExternalSecrets should show `SecretSynced` status.

### "Unauthorized" errors in identity logs

The Graph API client secret may be expired or invalid:

1. **Check secret expiration** in the Azure portal under the app registration's **Certificates & secrets**.
2. **Rotate the secret** and update your secret store.
3. **Restart the identity pod** to pick up the new secret:
   ```bash
   kubectl rollout restart deployment/identity -n union-cp
   ```
