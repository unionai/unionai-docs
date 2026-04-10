---
title: Human access controls
weight: 5
variants: -flyte +union
---

# Human access controls

Union.ai controls how its personnel access customer environments.

## Current access model

Union.ai support and engineering personnel may access a customer's Union.ai tenant (control plane UI and API) for onboarding, troubleshooting, and operational support. This access uses the same OIDC/SSO mechanisms and RBAC policies as customer users. Personnel access the tenant, not the data plane infrastructure directly.

## BYOC: Additional K8s cluster access

In BYOC deployments, personnel additionally have **authenticated access to the customer's Kubernetes cluster** for operational purposes:

* Cluster upgrades
* Node pool provisioning
* Helm chart updates
* Health monitoring and troubleshooting

This access uses cloud-native private connectivity (PrivateLink/PSC) and is scoped to K8s cluster management.

All cluster management actions are logged. Union.ai is implementing **just-in-time (JIT) access controls** to replace persistent support access with time-bound, customer-authorized grants.

## Access scope

When accessing a customer's tenant, personnel **can**:

* View orchestration metadata (workflow definitions, run status, scheduling configuration)
* View logs relayed through the tunnel (not the customer's log aggregator directly)
* Perform administrative operations as authorized by the customer's RBAC policy
* In BYOC: manage the K8s cluster via the PrivateLink/PSC connection

Personnel **cannot**:

* Read secret values (the API is write-only)
* Access raw data in customer object stores (presigned URLs are per-request and not retained)
* Access the customer's cloud account or IAM roles
* Access customer object stores, secrets backends, container registries, or log aggregators

## Audit trail

All access by Union.ai personnel is authenticated and logged. API requests include caller identity, operation performed, and timestamp.
