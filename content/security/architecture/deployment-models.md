---
title: Deployment models and BYOC differences
weight: 5
variants: -flyte +union
---

# Deployment models and BYOC differences

Union.ai offers two deployment models that share the same control plane/data plane architecture, encryption, RBAC, tenant isolation, and audit logging. The difference: in BYOC, **Union.ai manages the Kubernetes cluster** in the customer's cloud account.

## Overview

| Aspect | Self-Managed | BYOC |
| --- | --- | --- |
| Data plane operator | Customer | Union.ai |
| K8s cluster management | Customer | Union.ai (via PrivateLink/PSC) |
| K8s API exposure | Customer-controlled | Private only (never public Internet) |
| Union.ai infrastructure access | None (Cloudflare tunnel only) | K8s cluster management only |
| Data/secrets/logs access by Union.ai | None | None |
| Upgrade responsibility | Customer | Union.ai |
| Monitoring responsibility | Customer | Union.ai + customer |

## Network architecture

In addition to the Cloudflare Tunnel (identical in both models), BYOC deployments use a **private management connection** to the customer's Kubernetes cluster. See [Private connectivity (BYOC)](../network/private-connectivity).

## Human access to customer environments

In self-managed deployments, Union.ai personnel access only the control plane tenant. They have zero access to data plane infrastructure.

In BYOC, personnel additionally have authenticated K8s cluster access for operational purposes (upgrades, provisioning, monitoring). This access is scoped to cluster management -- personnel still cannot access customer data, secrets, or logs.

For complete details, see [Human access controls](../auth/human-access-controls).

## Secrets management

The default secrets backend differs by deployment model:

* **Self-managed:** Kubernetes Secrets (K8s etcd)
* **BYOC:** Cloud-native secrets backend (AWS Secrets Manager, GCP Secret Manager, or Azure Key Vault)

All four backends remain available in both models. Security properties (write-only API, runtime-only consumption, in-memory relay) are identical. See [Secrets backends](../secrets/secrets-backends).

## Infrastructure management

In self-managed deployments, the customer manages their own Kubernetes clusters.

In BYOC, Union.ai manages the cluster in the customer's cloud account:

* Cluster provisioning and configuration
* Kubernetes version management and upgrades
* Node pool health and autoscaler configuration
* Helm chart updates for platform components
* Monitoring stack deployment and maintenance (Prometheus, Grafana, Fluent Bit)
* Serving infrastructure lifecycle (Kourier gateway, Knative, Union Operator)

The customer retains responsibility for their cloud account's underlying infrastructure (VPC, IAM policies, object storage configuration).

### IAM role provisioning

The same two IAM roles (`adminflyterole` and `userflyterole`) exist in both models. In self-managed, the customer provisions them. In BYOC, Union.ai provisions them during cluster setup.

### Data plane patching

In self-managed, the customer handles all data plane patching. In BYOC, Union.ai manages Kubernetes version, helm charts, and platform component updates. The control plane is updated independently in both models.

## Availability and resilience

Control plane availability is identical (AWS multi-AZ, managed PostgreSQL with automated failover, SOC 2 Type II coverage).

Data plane availability differs:

* **Self-managed:** Customer is solely responsible for data plane availability. Union.ai's availability commitment covers only the control plane.
* **BYOC:** Union.ai is responsible for cluster availability (K8s version, node pool health, autoscaler, monitoring stack). The customer retains responsibility for cloud account availability (VPC, IAM, object storage SLAs). Union.ai's operational SLA is defined in the customer contract.

In both models, in-flight workflows continue executing during control plane outages. In BYOC, Union.ai monitoring detects connectivity issues; in self-managed, the customer detects these independently.

## Third-party dependency risk

In self-managed, the customer owns all data plane dependencies. In BYOC, Union.ai assumes responsibility for cluster-level dependencies (Kubernetes, Helm charts, monitoring stack, serving infrastructure).

Union.ai's vendor management program, covered under SOC 2 Type II, includes periodic evaluation of these dependencies. See [Vulnerability management](../operations/vulnerability-management).

## Shared responsibility model

For the full responsibility breakdown by deployment model, see [Shared responsibility model](../compliance/shared-responsibility-model).

## HIPAA and compliance

Union.ai's HIPAA support applies equally to both deployment models. All customer data -- including any PHI -- remains in the customer's cloud infrastructure regardless of who manages the K8s cluster. The control plane stores only orchestration metadata.
