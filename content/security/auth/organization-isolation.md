---
title: Organization and tenant isolation
weight: 4
variants: -flyte +union
---

# Organization and tenant isolation

Union.ai enforces tenant isolation at multiple architectural layers to ensure that no customer can access another customer's data or metadata, even within the shared control plane.

## Database-layer isolation

Every record in the control plane PostgreSQL database is scoped by organization (org). The org identifier is part of the primary key or unique index on all tenant-scoped tables (actions, tasks, runs, executions, RBAC bindings). All database queries are gated by the org context extracted from the caller's authenticated token at the service layer, before any SQL is executed. A query can only return records belonging to the caller's organization.

Cross-organization access is explicitly denied: there is no API or internal path that permits querying across org boundaries. Union.ai does not currently use PostgreSQL row-level security (RLS) policies, but the application-layer enforcement is uniform and independently verifiable through the SOC 2 Type II audit.

## Data plane isolation

Each customer's data plane runs in a dedicated Kubernetes cluster within the customer's own cloud account. There is no shared compute infrastructure between customers. Customer workloads, data, secrets, container images, and logs are physically isolated in separate cloud accounts with separate IAM boundaries. No other customer's workloads can execute on or access another customer's cluster.

## Control plane service isolation

Within the control plane, all service-to-service calls carry the authenticated org context. The identity service extracts org membership from the OIDC token, and this context is propagated through every downstream service call via request headers. Kubernetes namespaces on the data plane are provisioned per-project within each org, providing namespace-level resource isolation (resource quotas, RBAC bindings, network policies) even within a single customer's cluster.

## Isolation verification

Tenant isolation controls are covered by Union.ai's SOC 2 Type II audit scope. The combination of org-scoped primary keys, service-layer query gating, and physically separate data planes provides defense-in-depth against cross-tenant data access.
