---
title: Tenant isolation
weight: 3
variants: -flyte +union
---

## Database-layer isolation

Every record in the control plane PostgreSQL database is scoped by organization. The org identifier is part of the primary key or unique index on all tenant-scoped tables. All database queries are gated by the org context extracted from the caller's authenticated token at the service layer, before any SQL is executed. Cross-org access is explicitly denied -- there is no API or internal path that permits querying across org boundaries.

Union.ai does not currently use PostgreSQL row-level security (RLS) policies, but the application-layer enforcement is uniform and independently verifiable through the SOC 2 Type II audit.

## Data plane isolation

Each customer's data plane runs in a dedicated Kubernetes cluster within the customer's own cloud account. There is no shared compute infrastructure between customers. Customer workloads, data, secrets, container images, and logs are physically isolated in separate cloud accounts with separate IAM boundaries.

## Control plane service isolation

All service-to-service calls within the control plane carry the authenticated org context. The identity service extracts org membership from the OIDC token, and this context is propagated through every downstream service call via request headers. Kubernetes namespaces on the data plane are provisioned per-project within each org, providing namespace-level resource isolation including resource quotas, RBAC bindings, and network policies.

## Isolation verification

Tenant isolation controls are covered by the SOC 2 Type II audit scope. The combination of org-scoped primary keys, service-layer query gating, and physically separate data planes provides defense-in-depth against cross-tenant data access.

## Verification

### Tenant isolation (Critical)

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
