---
title: Infrastructure security
weight: 6
variants: -flyte +byoc +selfmanaged
---

# Infrastructure security

## Kubernetes security

The compute plane runs on customer-managed Kubernetes clusters. Union supports the following security measures:

> [!NOTE]
> In BYOC deployments, Union.ai manages the K8s cluster. See [BYOC deployment differences: Infrastructure management](./byoc-differences#infrastructure-management).

* Workload identity federation for pod-level IAM role binding (no static credentials)
* Kubernetes RBAC for service account permissions within the cluster
* Network policies for pod-to-pod communication isolation
* Resource quotas and limit ranges to prevent resource abuse
* Pod security contexts enforcing non-root execution where applicable

A complete list of compute plane permissions appears in **[Kubernetes RBAC: compute plane](./kubernetes-rbac-compute-plane)**

## Container security

Union.ai’s container security model ensures that code execution is isolated and controlled:

* Image Builder runs on the customer’s cluster using Buildkit, ensuring source code and built images never leave customer infrastructure
* Base images are pulled from customer-approved registries (public or private)
* Built images are pushed to the customer’s container registry (ECR/GCR/ACR)
* Task pods mount code bundles via presigned URLs with limited TTL
* Container images follow customer-defined tagging and scanning policies

## IAM and workload identity

Two IAM roles are provisioned per compute plane, each with narrowly scoped permissions. In BYOC deployments, [Union.ai provisions these roles](./byoc-differences#iam-role-provisioning); in self-managed, the customer provisions them.

| Role | Permissions | Assumed By | Mechanism |
| --- | --- | --- | --- |
| Admin Role (`adminflyterole`) | R/W to object store buckets, secrets manager access, persisted logs read | Platform services: Executor, Object Store Service, DataProxy | Workload identity federation |
| User Role (`userflyterole`) | R/W to object store buckets | Task pods (user workloads) | Workload identity via K8s service account annotation |

These roles use cloud-native workload identity federation (IAM Roles for Service Accounts on AWS, Workload Identity on GCP, Azure Workload Identity on Azure), eliminating the need for static credential storage.

## Control plane infrastructure

The Union.ai control plane is hosted on AWS with enterprise-grade infrastructure security:

* Managed PostgreSQL (AWS RDS) with AES-256 encryption at rest
* Network isolation via VPC with restricted security groups
* TLS termination at the edge for all incoming connections
* Automated backups and disaster recovery procedures
* Infrastructure-as-code deployment with version-controlled configurations
* Automated patch management and security updates

## Availability, response time, and resilience

Union.ai's architecture separates the availability characteristics of the control plane and compute plane, providing resilience even during partial outages.

### Control plane availability

The Union.ai control plane runs on AWS with multi-AZ redundancy, managed PostgreSQL (RDS) with automated failover, and continuous monitoring. Union.ai's SOC 2 Type II audit covers availability as a trust service criterion. The control plane is designed for high availability, with automated recovery and health monitoring. Specific SLA targets are defined in customer contracts and are available upon request.

### Compute plane resilience during control plane outages

Because the compute plane runs entirely within the customer's Kubernetes cluster, in-flight workflows continue executing even if the control plane becomes temporarily unavailable. The Executor, which manages pod lifecycle, operates as a Kubernetes controller on the customer's cluster and does not require real-time connectivity to the control plane to continue running pods that have already been scheduled. State transitions will be reconciled when connectivity is restored. However, new workflow submissions and scheduling operations require control plane availability.

The customer is solely responsible for compute plane availability, including Kubernetes cluster operations, node pool management, upgrades, and monitoring. Union.ai's availability commitment covers only the control plane. In-flight workflows continue executing independently during control plane outages.

> [!NOTE]
> In BYOC deployments, availability responsibilities shift — Union.ai manages compute plane cluster availability. See [BYOC deployment differences: Availability and resilience](./byoc-differences#availability-and-resilience).
