---
title: Tenant isolation
weight: 3
variants: -flyte +union
---

# Tenant isolation

## Database-layer isolation

Every record in the control plane databases is scoped by organization. The org identifier is part of the primary key on all tenant-scoped tables. All database queries are gated by the org context extracted from the caller's authenticated token at the service layer, before any data access occurs. The primary org identity is derived from the request hostname subdomain (not user-supplied input). The standard `ResolveAuthorizationOrg` check blocks cross-org calls by default, and unrecognized services receive a default-deny response.

> [!NOTE]
> A source code audit identified areas where tenant isolation enforcement could be strengthened: certain internal proxy routes allow an org name from the request path to override the authenticated identity's organization, and the authorizer for these routes does not perform an active check. These routes are intended to be reachable only from internal services behind the service mesh. Additionally, some services (e.g., secret service) allow org override from the request body, relying on the authorization backend to deny cross-org access rather than using the standard `ResolveAuthorizationOrg` check.

Union.ai does not currently use PostgreSQL row-level security (RLS) policies, but the application-layer enforcement is uniform and independently verifiable through the SOC 2 Type II audit.

## Data plane isolation

Each customer's data plane runs in a dedicated Kubernetes cluster within the customer's own cloud account. There is no shared compute infrastructure between customers. Customer workloads, data, secrets, container images, and logs are physically isolated in separate cloud accounts with separate IAM boundaries.

## Control plane service isolation

All service-to-service calls within the control plane carry the authenticated org context. The identity service extracts org membership from the OIDC token, and this context is propagated through every downstream service call via request headers. Kubernetes namespaces on the data plane are provisioned per-project within each org, providing namespace-level resource isolation including resource quotas, RBAC bindings, and network policies.

## Isolation verification

Tenant isolation controls are covered by the SOC 2 Type II audit scope. The combination of org-scoped primary keys, service-layer query gating, and physically separate data planes provides defense-in-depth against cross-tenant data access.

## Verification

### Tenant isolation

**Reviewer focus:** Confirm that customers cannot access other tenants' data through any path, and that the isolation model is architecturally enforced rather than relying solely on application logic.

**How to verify:**

1. Data plane isolation is architectural: each customer has their own cluster in their own cloud account. This is verifiable by inspecting the infrastructure directly.

2. Database isolation: all API responses include org context. Confirm that only the customer's org is returned:

   ```bash
   uctl get executions -o json | jq '.org'
   ```

   This should always return only the customer's org identifier.

3. The SOC 2 Type II audit specifically covers tenant isolation controls.

4. The Protobuf definitions and SDK code are open source -- the org context enforcement path can be traced through the codebase.
