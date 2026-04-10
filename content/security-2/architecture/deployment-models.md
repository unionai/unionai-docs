---
title: Deployment models and BYOC differences
weight: 5
variants: -flyte +union
---

# Deployment models and BYOC differences

Union.ai's BYOC (Bring Your Own Cloud) deployment shares the same control plane / data plane architecture, encryption, RBAC, tenant isolation, and audit logging as the self-managed deployment. The key difference is that **Union.ai manages the Kubernetes cluster** in the customer's cloud account, rather than the customer managing it independently.

This page consolidates all security-relevant differences between BYOC and self-managed deployments.

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

In addition to the Cloudflare Tunnel (which operates identically in both models), Union.ai maintains a **private management connection** to the customer's Kubernetes cluster in BYOC deployments. For details, see [Private connectivity (BYOC)](../network/private-connectivity).

## Human access to customer environments

In self-managed deployments, Union.ai personnel access only the customer's control plane tenant. They have zero access to the customer's data plane infrastructure.

In BYOC deployments, Union.ai support and engineering personnel additionally have **authenticated access to the customer's Kubernetes cluster** for operational purposes:

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

For complete details on human access controls, see [Human access controls](../auth/human-access-controls).

## Secrets management

The default secrets backend differs by deployment model:

* **Self-managed:** Kubernetes Secrets (K8s etcd) is the default
* **BYOC:** A cloud-native secrets backend (AWS Secrets Manager, GCP Secret Manager, or Azure Key Vault) is the default, for managed integration with the provisioning workflow

All four backends remain available as options in both models. The security properties (write-only API, runtime-only consumption, in-memory relay) are identical.

For more on secrets backends, see [Secrets backends](../secrets/secrets-backends).

## Infrastructure management

In self-managed deployments, the customer manages their own Kubernetes clusters, including provisioning, configuration, version management, node pools, and security patching.

In BYOC deployments, Union.ai manages the Kubernetes cluster in the customer's cloud account:

* **Cluster provisioning and configuration**
* **Kubernetes version management and upgrades**
* **Node pool health and autoscaler configuration**
* **Helm chart updates for platform components**
* **Monitoring stack deployment and maintenance** (Prometheus, Grafana, Fluent Bit)
* **Serving infrastructure lifecycle** (Kourier gateway, Knative, Union Operator)

The customer retains responsibility for their cloud account's underlying infrastructure (VPC, IAM policies, object storage configuration).

### IAM role provisioning

The same two IAM roles (`adminflyterole` and `userflyterole`) exist in both models. In self-managed, the customer provisions them using Union.ai's documentation and templates. In BYOC, Union.ai provisions these roles as part of cluster setup.

### Data plane patching

In self-managed, the customer is responsible for all data plane patching (K8s version, platform components, monitoring stack). In BYOC, Union.ai manages data plane updates, including Kubernetes version, helm charts, and platform components. The control plane is updated independently in both models.

## Availability and resilience

Control plane availability is identical across both models (AWS multi-AZ, managed PostgreSQL with automated failover, SOC 2 Type II coverage).

The difference is in data plane availability:

* **Self-managed:** The customer is solely responsible for data plane availability, including Kubernetes cluster operations, node pool management, upgrades, and monitoring. Union.ai's availability commitment covers only the control plane.
* **BYOC:** Union.ai is responsible for data plane cluster availability, including Kubernetes version management, node pool health, autoscaler configuration, and monitoring stack uptime. The customer retains responsibility for their cloud account's underlying availability (VPC, IAM, object storage SLAs). Union.ai's operational SLA for BYOC cluster management is defined in the customer contract.

In both models, in-flight workflows continue executing during control plane outages. The operational difference is that in BYOC, Union.ai's monitoring detects control plane connectivity issues; in self-managed, the customer must detect these independently.

## Third-party dependency risk

In self-managed, the customer owns all data plane dependencies. Union.ai's dependency risk scope is limited to the control plane and Cloudflare tunnel.

In BYOC, Union.ai assumes operational responsibility for cluster-level dependencies and their associated risk mitigation:

* Kubernetes version
* Helm charts
* Monitoring stack (Prometheus, Grafana, Fluent Bit)
* Serving infrastructure (Kourier, Knative)

Union.ai's vendor management program, covered under the SOC 2 Type II audit, includes periodic evaluation of these dependencies.

## Shared responsibility model

The shared responsibility model shifts in BYOC for data plane operations:

| Responsibility Area | Self-Managed | BYOC |
| --- | --- | --- |
| Control plane security | Union.ai | Union.ai |
| Data plane K8s cluster | Customer | Union.ai |
| Cloud account (VPC, IAM) | Customer | Customer |
| Data encryption at rest | Customer (CMK optional) | Customer (CMK optional) |
| Network security (tunnel) | Union.ai (tunnel) + Customer (firewall/VPC) | Union.ai (tunnel + PrivateLink) + Customer (VPC) |
| IAM role provisioning | Customer | Union.ai |
| Secrets management | Customer (backend selection + values) | Union.ai (default backend) + Customer (values) |
| Application-level access control | Customer (role assignment) | Customer (role assignment) |
| Compliance documentation | Union.ai (SOC 2, Trust Center) + Customer | Union.ai (SOC 2, Trust Center) + Customer |

For the self-managed shared responsibility model, see [Shared responsibility model](../compliance/shared-responsibility-model).

## HIPAA and compliance

Union.ai's HIPAA compliance support applies equally to both deployment models. The architecture ensures that all customer data -- including any PHI -- remains exclusively in the customer's own cloud infrastructure regardless of who manages the K8s cluster. The control plane stores only orchestration metadata and never persists PHI.

## Contact and resources

* Trust Center: [trust.union.ai](https://trust.union.ai)
* SOC 2 Type II Report: Available upon request
* Security Inquiries: Contact your Union.ai account representative or visit [trust.union.ai](https://trust.union.ai)
