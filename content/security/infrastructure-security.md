---
title: Infrastructure security
weight: 6
variants: -flyte +byoc +selfmanaged
---

# Infrastructure security

## Kubernetes security

The compute plane runs on customer or Union-managed Kubernetes clusters. Union supports the following security measures:

* Workload identity federation for pod-level IAM role binding (no static credentials)
* Kubernetes RBAC for service account permissions within the cluster
* Network policies for pod-to-pod communication isolation
* Resource quotas and limit ranges to prevent resource abuse
* Pod security contexts enforcing non-root execution where applicable

A complete list of compute plane permissions appears in **[Appendix D](./appendix#d-kubernetes-rbac---compute-plane)**

## Container security

Union.ai’s container security model ensures that code execution is isolated and controlled:

* Image Builder runs on the customer’s cluster using Buildkit, ensuring source code and built images never leave customer infrastructure
* Base images are pulled from customer-approved registries (public or private)
* Built images are pushed to the customer’s container registry (ECR/GCR/ACR)
* Task pods mount code bundles via presigned URLs with limited TTL
* Container images follow customer-defined tagging and scanning policies

## IAM and workload identity

On Union-managed compute planes (BYOC), two IAM roles are provisioned per compute plane, each with narrowly scoped permissions:

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
