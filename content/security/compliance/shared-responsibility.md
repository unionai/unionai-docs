---
title: Shared responsibility model
weight: 5
variants: -flyte +union
---

# Shared responsibility model

## Self-managed

In self-managed deployments, the customer owns and operates the data plane infrastructure, while Union.ai manages the control plane. The following table defines the responsibility boundary.

| Area | Union.ai | Customer |
|---|---|---|
| Control plane security | Full ownership | N/A |
| Data plane infrastructure | Guidance and tooling | Provisioning and maintenance |
| Data encryption at rest | Default cloud encryption | Optional CMK configuration |
| Network security (tunnel) | Tunnel management | Firewall and VPC configuration |
| IAM roles and policies | Role templates and documentation | Role creation and binding |
| Secrets management | API and relay infrastructure | Backend selection and secret values |
| Access control | RBAC framework | Role assignment and policy |
| Compliance documentation | SOC 2 report, Trust Center | Customer-specific attestations |

## BYOC shifts

In BYOC deployments, Union.ai assumes additional operational responsibility for the data plane Kubernetes cluster while the customer retains ownership of the cloud account.

| Area | Self-managed | BYOC |
|---|---|---|
| Data plane K8s cluster | Customer | Union.ai |
| Cloud account (VPC, IAM) | Customer | Customer |
| IAM role provisioning | Customer | Union.ai |
| Secrets management | Customer (backend + values) | Union.ai (default backend) + Customer (values) |
| Network security | Union.ai (tunnel) + Customer (firewall/VPC) | Union.ai (tunnel + PrivateLink) + Customer (VPC) |

For details on how the deployment model affects security controls, see [Deployment models](../architecture/deployment-models).

## Verification

### Shared responsibility model

**Reviewer focus:** Confirm that the responsibility boundaries are clearly defined and that the BYOC model correctly reflects the shifted responsibilities.

**How to verify:**

This is a reference table for risk assessment, not a claim requiring active proof. Use it to map security questions to the responsible party for each deployment model.
