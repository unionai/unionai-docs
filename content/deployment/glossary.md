---
title: Deployment glossary
weight: 99
variants: -flyte +union
---

# Deployment glossary

## Deployment models

**Self-managed deployment**
: {{< key product_name >}} hosts the control plane. You manage the data plane in your own cloud account. Data plane provisioning is handled via `uctl selfserve`. See [Platform deployment](./_index).

**Self-hosted deployment**
: You host both the control plane and data plane in the same Kubernetes cluster. All communication stays within your infrastructure via Kubernetes internal networking. See [Self-hosted deployment](./selfhosted/_index).

## Architecture components

**Control plane**
: The orchestration layer that manages workflow execution state. Includes FlyteAdmin, scheduler, queue service, cache service, and supporting services. In self-managed deployments, the control plane is hosted by {{< key product_name >}}. In self-hosted deployments, you deploy it in the `union-cp` namespace.

**Data plane**
: The execution layer where your code and data reside. Includes the operator, propeller, and worker pods that run your tasks. Deployed in the `union` namespace.

**Intra-cluster**
: A deployment topology where the control plane and data plane run in the same Kubernetes cluster and communicate via internal DNS (e.g., `controlplane-nginx-controller.union-cp.svc.cluster.local`) rather than external networking.

## Cloud provider concepts

**IRSA** (IAM Roles for Service Accounts)
: AWS mechanism that allows Kubernetes service accounts to assume IAM roles. Used by control plane and data plane pods to access AWS resources (S3, RDS) without static credentials.

**Workload Identity**
: GCP mechanism that allows Kubernetes service accounts to impersonate GCP service accounts. The GCP equivalent of IRSA.
