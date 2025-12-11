---
title: Single sign on setup
weight: 12
variants: -flyte -serverless +byoc -selfmanaged
sidebar_expanded: true
---

# Single sign on setup

{{< key product_name >}} authentication uses OAuth2 with Okta and supports SAML and OIDC-compliant identity providers (IdP) to configure single sign on (SSO).

To enable SSO, create an app for your preferred identity provider and provide the associated secrets to the {{< key product_name >}} team.
The team will then complete the process.

## Google OpenID Connect

To configure Google OpenID Connect, see [Google OpenID Connect](./google-oidc).

## Microsoft Entra ID (formerly Azure AD)

To configure Entra ID (Azure AD), see [Microsoft Entra ID (formerly Azure ID)](./microsoft-entra-id).

## Other identity providers

To configure other identity providers, see [Other identity providers](./other-identity-providers).
