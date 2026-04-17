---
title: Authentication
weight: 1
variants: -flyte +union
---

# Authentication

## Authentication methods

Union.ai supports three authentication methods, each designed for a different use case.

| Method | Identity Type | Credentials | Use Case |
|---|---|---|---|
| OIDC (Okta) | Human user | Browser SSO | UI access, initial CLI login |
| API Keys | Human user (delegated) | Static bearer token | CI/CD scripts, simple automation |
| Service Accounts | Application identity | OAuth2 client_id + client_secret -> short-lived token | Production pipelines, multi-service systems |

API keys are issued per user and inherit the user's RBAC permissions. They can be created and revoked via the UI or CLI.

Service accounts are provisioned through the Identity Service, creating OAuth2 applications with distinct, auditable identities independent of any human user.

## Single sign-on

Union.ai uses OAuth2 with Okta as its identity provider, supporting any OIDC or SAML 2.0 compliant provider (Google Workspace, Microsoft Entra ID, Okta, others). SSO provides centralized identity management where the user lifecycle is managed in the customer's IdP. MFA enforcement is delegated to the customer's IdP -- the customer's existing MFA policies apply without additional configuration. Session management is inherited from the IdP configuration, and all authentication events are logged with caller identity.

## Verification

### SSO and credential lifecycle (High)

**Reviewer focus:** Confirm that SSO redirects to the customer's IdP, that MFA is enforced when configured, and that API keys and service accounts can be created, used, and revoked.

**How to verify:**

1. SSO: Log in -- the browser redirects to the customer's IdP, and a MFA prompt appears if configured.

2. API key: Create a key, use it in a script, then revoke it:

   ```bash
   uctl create api-key
   # Use the key in a script to authenticate
   uctl delete api-key <key-id>
   # Confirm the revoked key is rejected
   ```

3. Service account: Create a service account and confirm it has a distinct identity:

   ```bash
   uctl create service-account
   ```

   Show the OAuth2 token exchange and confirm the service account appears as a distinct identity in the audit log.

All verification steps are self-service using existing features.
