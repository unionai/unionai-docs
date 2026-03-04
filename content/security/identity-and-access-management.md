---
title: Identity and access management
weight: 4
variants: -flyte +byoc +selfmanaged
---

## Authentication

Union.ai supports three authentication methods to accommodate different usage patterns:

| Method | Identity Type | Credentials | Use Case |
| --- | --- | --- | --- |
| OIDC (Okta) | Human user | Browser SSO | UI access, initial CLI login |
| API Keys | Human user (delegated) | Static bearer token | CI/CD scripts, simple automation |
| Service Accounts | Application identity | OAuth2 client_id + client_secret → short-lived token | Production pipelines, multi-service systems |

API keys are issued per user and inherit the user’s RBAC permissions.
They can be created and revoked via the UI or CLI.
Service accounts are provisioned through the Identity Service, creating OAuth2 applications with distinct, auditable identities independent of any human user.

## Authorization (RBAC)

Union.ai implements a policy-based Role-Based Access Control (RBAC) system with three built-in role types.

| Role | Capabilities | Typical Assignment |
| --- | --- | --- |
| Admin | Full access: manage users, clusters, secrets, projects, and all runs | Platform administrators, security team leads |
| Contributor | Create/abort runs, register tasks, manage secrets within assigned projects | ML engineers, data scientists, DevOps |
| Viewer | Read-only access to runs, actions, logs, reports | Stakeholders, auditors, read-only consumers |
| Custom Policies | Custom policies bind roles (built-in or custom) to resources scoped at org-wide, domain, or project+domain level using composable YAML bindings via `uctl` | Giving contributor access to a specific project's development and staging domains, but only viewer access in production |

RBAC policies are enforced at the service layer.
Every API request is authenticated and authorized against the user’s role assignments before any data access occurs.

## Organization isolation

Every record in the control plane database is scoped by organization (org).
The identity context, extracted from the authenticated token, gates all database queries.
The actions table uses org as part of its unique index, and the tasks table uses org as part of its primary key.
Cross-organization access is explicitly denied at the service layer, providing strong multi-tenant isolation.

## Least privilege principle

Union.ai enforces the principle of least privilege across all system components:

* IAM roles on the data plane are scoped to minimum required permissions
* Two IAM roles per data plane: admin role (for platform services) and user role (for task pods)
* IAM roles are bound to Kubernetes service accounts via cloud-native workload identity federation
* Presigned URLs grant single-object, operation-specific, time-limited access
* Service accounts receive only the permissions needed for their specific function
