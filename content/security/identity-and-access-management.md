---
title: Identity and access management
weight: 3
variants: -flyte +byoc +selfmanaged
---

# Identity and access management

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
Users have the ability to create custom policies to further refine access control.

## Organization isolation

Union.ai enforces tenant isolation at multiple architectural layers to ensure that no customer can access another customer's data or metadata, even within the shared control plane.

### Database-layer isolation

Every record in the control plane PostgreSQL database is scoped by organization (org). The org identifier is part of the primary key or unique index on all tenant-scoped tables, including actions, tasks, runs, executions, and RBAC bindings. All database queries are gated by the org context extracted from the caller's authenticated token at the service layer, before any SQL is executed. This ensures that a query can only return records belonging to the caller's organization. Cross-organization access is explicitly denied: there is no API or internal path that permits querying across org boundaries. While Union.ai does not currently use PostgreSQL row-level security (RLS) policies, the application-layer enforcement is uniform and independently verifiable through the SOC 2 Type II audit.

### Compute plane isolation

Each customer's compute plane runs in a dedicated Kubernetes cluster within the customer's own cloud account. There is no shared compute infrastructure between customers. Customer workloads, data, secrets, container images, and logs are physically isolated in separate cloud accounts with separate IAM boundaries. No other customer's workloads can execute on or access another customer's cluster.

### Control plane service isolation

Within the control plane, all service-to-service calls carry the authenticated org context. The identity service extracts org membership from the OIDC token, and this context is propagated through every downstream service call via request headers. Kubernetes namespaces on the compute plane are provisioned per-project within each org, providing namespace-level resource isolation (resource quotas, RBAC bindings, network policies) even within a single customer's cluster.

### Isolation verification

Tenant isolation controls are covered by Union.ai's SOC 2 Type II audit scope. The combination of org-scoped primary keys, service-layer query gating, and physically separate compute planes provides defense-in-depth against cross-tenant data access.

## Human access to customer environments

Union.ai maintains controls governing how its personnel interact with customer environments.

### Current access model

Union.ai support and engineering personnel may access a customer's Union.ai tenant (the control plane UI and API for that organization) for the purposes of onboarding, troubleshooting, and operational support. This access is authenticated through the same OIDC/SSO mechanisms as customer users and is subject to RBAC policies. Personnel access the customer's tenant, not the customer's compute plane infrastructure directly. Union.ai personnel do not have IAM credentials for the customer's cloud account and cannot directly access the customer's object stores, secrets backends, or container registries.

> [!NOTE]
> In BYOC deployments, Union.ai personnel additionally have K8s cluster management access. See [BYOC deployment differences: Human access](./byoc-differences#human-access-to-customer-environments) for details.

### Access scope and limitations

When Union.ai personnel access a customer's tenant, they can view orchestration metadata (workflow definitions, run status, scheduling configuration), view logs relayed through the tunnel (but cannot access the customer's log aggregator directly), and perform administrative operations (cluster configuration, namespace provisioning) as authorized by the customer's RBAC policy. Personnel cannot read secret values (the API is write-only for values), cannot access raw data in the customer's object stores (presigned URLs are generated per-request and are not retained), and cannot access the customer's cloud account or IAM roles. In BYOC deployments, administrative operations [extend to direct K8s cluster management](./byoc-differences#human-access-to-customer-environments).

### Audit trail

All access by Union.ai personnel to customer tenants is authenticated and logged. API requests include the identity of the caller, the operation performed, and a timestamp.

> [!NOTE]
> In BYOC deployments, Union.ai personnel have additional K8s cluster access for operational management. See [BYOC deployment differences: Human access](./byoc-differences#human-access-to-customer-environments) for full details.

## Least privilege principle

Union.ai enforces the principle of least privilege across all system components:

* IAM roles on the compute plane are scoped to minimum required permissions
* Two IAM roles per compute plane: admin role (for platform services) and user role (for task pods)
* IAM roles are bound to Kubernetes service accounts via cloud-native workload identity federation
* Presigned URLs grant single-object, operation-specific, time-limited access
* Service accounts receive only the permissions needed for their specific function
