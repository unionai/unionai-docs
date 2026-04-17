---
title: SSO configuration
weight: 2
variants: -flyte +union
---

# SSO configuration

Union.ai uses OAuth2 with Okta as its identity provider, supporting both OIDC and SAML-compliant identity providers for single sign-on.

## Supported identity providers

Union.ai integrates with any OIDC or SAML 2.0 compliant identity provider, including:

* **Google Workspace** (OIDC)
* **Microsoft Entra ID** (Azure AD) (OIDC/SAML)
* **Okta** (OIDC/SAML)
* **Other OIDC/SAML providers**

## Security properties

SSO provides several security benefits for Union.ai deployments:

* **Centralized identity management:** User lifecycle (provisioning, deprovisioning) is managed in your IdP, ensuring consistent access control across all systems.
* **Multi-factor authentication:** MFA enforcement is delegated to your IdP, applying your organization's existing MFA policies to Union.ai access without additional configuration.
* **Session management:** Session duration and idle timeout policies are inherited from your IdP configuration.
* **Audit trail:** All authentication events are logged with the identity of the caller, supporting compliance and forensic requirements.

## Setup guides

For step-by-step SSO configuration instructions, see the deployment documentation:

* [Single sign-on setup](/deployment/byoc/single-sign-on-setup/)
