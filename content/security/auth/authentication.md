---
title: Authentication methods
weight: 1
variants: -flyte +union
---

# Authentication methods

Union.ai supports three authentication methods to accommodate different usage patterns:

| Method | Identity Type | Credentials | Use Case |
| --- | --- | --- | --- |
| OIDC (Okta) | Human user | Browser SSO | UI access, initial CLI login |
| API Keys | Human user (delegated) | Static bearer token | CI/CD scripts, simple automation |
| Service Accounts | Application identity | OAuth2 client_id + client_secret -> short-lived token | Production pipelines, multi-service systems |

API keys are issued per user and inherit the user's RBAC permissions.
They can be created and revoked via the UI or CLI.
Service accounts are provisioned through the Identity Service, creating OAuth2 applications with distinct, auditable identities independent of any human user.
