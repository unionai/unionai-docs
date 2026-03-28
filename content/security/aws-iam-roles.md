---
title: AWS IAM roles
weight: 18
variants: -flyte +union
---

# AWS IAM roles

In self-managed deployments, the customer provisions these roles using Union.ai's documentation and templates. In BYOC deployments, [Union.ai provisions them](./byoc-differences#iam-role-provisioning).

| Plane | Service Account | Purpose | K8s Namespace | IAM Role ARN Pattern | Bound To | S3 Access |
| --- | --- | --- | --- | --- | --- | --- |
| Control Plane | `flyteadmin` | Orchestration metadata management, namespace provisioning, presigned URL generation for code upload/download | union | `arn:aws:iam::<account-id>:role/adminflyterole` | FlyteAdmin (workflow admin service) | Generates presigned URLs for customer S3 buckets (does not directly read/write data) |
| Data Plane | `clustersync-system` | Synchronizes K8s namespaces, RBAC roles, service accounts, resource quotas, and config across the cluster | union | `adminflyterole` (data plane admin) | ClusterResourceSync controller | No direct S3 access |
| Data Plane | `executor` | Receives task assignments via tunnel, creates task pods, manages pod lifecycle, reports status back to control plane | union | `adminflyterole` (data plane admin) | Node Executor (TaskAction controller) | R/W to metadata bucket and fast-registration bucket for staging task inputs/outputs |
| Data Plane | `proxy-system` | Monitors events, Flyte workflows, pod logs; streams data back to control plane via tunnel | union | `adminflyterole` (data plane admin) | Proxy Service | Read-only access to metadata bucket for proxying presigned URL requests |
| Data Plane | `operator-system` | Cluster operations, health monitoring, config management, image builder orchestration, tunnel management | union | `adminflyterole` (data plane admin) | Union Operator | R/W to metadata bucket for operator state and config |
| Data Plane | `flytepropeller-system` | K8s operator managing FlyteWorkflow CRDs, pod creation, workflow lifecycle execution | union | `adminflyterole` (data plane admin) | FlytePropeller (workflow engine) | R/W to metadata bucket for workflow data (inputs, outputs, offloaded data) |
| Data Plane | `flytepropeller-webhook-system` | Mutating admission webhook that injects secrets into task pods at creation time | union | `adminflyterole` (data plane admin) | FlytePropeller Webhook | No direct S3 access (handles secrets injection only) |
| Data Plane | `clusterresource-template` (per-namespace) | Executes user workflow tasks; reads inputs, writes outputs to S3 | Per-workspace namespace | `userflyterole` (data plane user) | Task Pods (user workloads) | R/W to metadata bucket for task inputs/outputs, code bundles, artifacts |

For BYOC-specific deployment concerns, see [BYOC deployment differences](./byoc-differences).
