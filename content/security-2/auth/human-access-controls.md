---
title: Human access controls
weight: 5
variants: -flyte +union
---

# Human access controls

Union.ai maintains controls governing how its personnel interact with customer environments.

## Current access model

Union.ai support and engineering personnel may access a customer's Union.ai tenant (the control plane UI and API for that organization) for the purposes of onboarding, troubleshooting, and operational support. This access is authenticated through the same OIDC/SSO mechanisms as customer users and is subject to RBAC policies. Personnel access the customer's tenant, not the customer's data plane infrastructure directly. Union.ai personnel do not have IAM credentials for the customer's cloud account and cannot directly access the customer's object stores, secrets backends, or container registries.

## BYOC: Additional K8s cluster access

In BYOC deployments, Union.ai personnel additionally have **authenticated access to the customer's Kubernetes cluster** for operational purposes:

* Cluster upgrades
* Node pool provisioning
* Helm chart updates
* Health monitoring and troubleshooting

This access is via cloud-native private connectivity (PrivateLink/PSC) and is scoped to K8s cluster management. Union.ai personnel still **cannot** access:

* Customer object stores
* Secrets backends
* Container registries
* Log aggregators

All cluster management actions are logged. Union.ai is implementing **just-in-time (JIT) access controls** to replace persistent support access with time-bound, customer-authorized grants.

The scope of "administrative operations" also differs: in self-managed, these are limited to control plane API calls (cluster configuration, namespace provisioning). In BYOC, they extend to direct K8s cluster management through the PrivateLink/PSC connection.

## Access scope and limitations

When Union.ai personnel access a customer's tenant, they can view orchestration metadata (workflow definitions, run status, scheduling configuration), view logs relayed through the tunnel (but cannot access the customer's log aggregator directly), and perform administrative operations (cluster configuration, namespace provisioning) as authorized by the customer's RBAC policy. Personnel cannot read secret values (the API is write-only for values), cannot access raw data in the customer's object stores (presigned URLs are generated per-request and are not retained), and cannot access the customer's cloud account or IAM roles. In BYOC deployments, administrative operations [extend to direct K8s cluster management](../architecture/deployment-models#human-access-to-customer-environments).

## Audit trail

All access by Union.ai personnel to customer tenants is authenticated and logged. API requests include the identity of the caller, the operation performed, and a timestamp.
