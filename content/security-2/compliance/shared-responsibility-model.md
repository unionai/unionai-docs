---
title: Shared responsibility model
weight: 6
variants: -flyte +union
---

# Shared responsibility model

Union.ai operates under a shared responsibility model. The allocation of responsibilities differs between Self-Managed and BYOC deployment models.

## Self-managed deployments

| Responsibility Area | Union.ai | Customer |
| --- | --- | --- |
| Control plane security | Full ownership | N/A |
| Data plane infrastructure | Guidance and tooling | Provisioning and maintenance |
| Data encryption at rest | Default cloud encryption | Optional CMK configuration |
| Network security (tunnel) | Tunnel management | Firewall and VPC configuration |
| IAM roles and policies | Role templates and documentation | Role creation and binding |
| Secrets management | API and relay infrastructure | Backend selection and secret values |
| Application-level access control | RBAC framework | Role assignment and policy |
| Compliance documentation | SOC 2 report, Trust Center | Customer-specific attestations |

## BYOC deployments

In BYOC, responsibilities shift for data plane operations:

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

For a comprehensive comparison of BYOC and self-managed differences, see [Deployment models and BYOC differences](../architecture/deployment-models).
