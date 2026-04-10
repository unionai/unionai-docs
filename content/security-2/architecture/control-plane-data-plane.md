---
title: Control plane and data plane separation
weight: 1
variants: -flyte +union
---

# Control plane and data plane separation

Union.ai strictly separates orchestration (control plane) from execution (data plane), keeping all customer data in the customer's cloud.

## Control plane (Union.ai hosted)

The control plane handles workflow orchestration, user management, and the web interface. It runs in Union.ai's AWS account and stores only orchestration metadata in a managed PostgreSQL database:

* Task definitions (image references, resource requirements, typed interfaces)
* Run and action metadata (identifiers, phase, timestamps, error information)
* User identity and RBAC records
* Cluster configuration and health records
* Trigger/schedule definitions

The control plane never stores customer data payloads -- only references (URIs) to data in the customer's object store. When data must be surfaced to a client, the control plane either proxies a signing request to generate a presigned URL or relays a data stream without persisting it.

**See [Kubernetes RBAC: control plane](../reference/kubernetes-rbac-control-plane) for roles and permissions.**

### Control plane infrastructure

The control plane runs on AWS with:

* Managed PostgreSQL (AWS RDS) with AES-256 encryption at rest
* Network isolation via VPC with restricted security groups
* TLS termination at the edge for all incoming connections
* Automated backups and disaster recovery procedures
* Automated patch management and security updates

## Data plane (customer hosted)

The data plane runs in the customer's own cloud account on their Kubernetes cluster. All customer data resides here:

| Data Type | Storage Technology | Access Pattern |
| --- | --- | --- |
| Task inputs/outputs | Object Store | Read/write by task pods via IAM roles |
| Code bundles (TGZ) | Object Store (fast-registration bucket) | Write via presigned URL; read by task pods and presigned URL by the browser |
| Container images | Container Registry | Built on-cluster; pulled by K8s |
| Task logs | Cloud Log Aggregator + live K8s API | Streamed via tunnel (never stored in CP) |
| Secrets | K8s Secrets, Vault, or Cloud Secrets Manager | Injected into pods at runtime |
| Observability metrics | Prometheus (in-cluster / customer managed) | Proxied queries via DataProxy |
| Reports (HTML) | Object Store (S3/GCS/Azure Blob) | Accessed by the browser via presigned URL |
| Cluster events | K8s API (ephemeral) | Live from K8s API |

**See [Kubernetes RBAC: data plane](../reference/kubernetes-rbac-data-plane) for roles and permissions.**

### Kubernetes security

The data plane runs on customer-managed Kubernetes clusters (or Union.ai-managed in [BYOC](./deployment-models)):

* Workload identity federation for pod-level IAM role binding (no static credentials)
* Kubernetes RBAC for service account permissions
* Network policies for pod-to-pod communication isolation
* Resource quotas and limit ranges to prevent resource abuse
* Pod security contexts enforcing non-root execution where applicable

### Container security

* Image Builder runs on the customer's cluster using Buildkit -- source code and built images never leave customer infrastructure
* Base images pulled from customer-approved registries (public or private)
* Built images pushed to the customer's container registry (ECR/GCR/ACR)
* Task pods mount code bundles via presigned URLs with limited TTL
* Container images follow customer-defined tagging and scanning policies

### IAM and workload identity

Two IAM roles are provisioned per data plane with narrowly scoped permissions. In [BYOC, Union.ai provisions these roles](./deployment-models#iam-role-provisioning); in self-managed, the customer provisions them.

| Role | Permissions | Assumed By | Mechanism |
| --- | --- | --- | --- |
| Admin Role (`adminflyterole`) | R/W to object store buckets, secrets manager access, persisted logs read | Platform services: Executor, Object Store Service, DataProxy | Workload identity federation |
| User Role (`userflyterole`) | R/W to object store buckets | Task pods (user workloads) | Workload identity via K8s service account annotation |

These roles use cloud-native workload identity federation (IRSA on AWS, Workload Identity on GCP, Azure Workload Identity), eliminating static credential storage.

For the full IAM role mapping, see [AWS IAM roles](../reference/aws-iam-roles).

## Availability, response time, and resilience

### Control plane availability

The control plane runs on AWS with multi-AZ redundancy, managed PostgreSQL with automated failover, and continuous monitoring. SOC 2 Type II covers availability as a trust service criterion. Specific SLA targets are defined in customer contracts.

### Data plane resilience during control plane outages

In-flight workflows continue executing during control plane outages. The Executor operates as a Kubernetes controller on the customer's cluster and does not require real-time connectivity to continue running already-scheduled pods. State transitions reconcile when connectivity is restored. New workflow submissions require control plane availability.

The customer is responsible for data plane availability (cluster operations, node pool management, upgrades, monitoring). Union.ai's availability commitment covers only the control plane.

> [!NOTE]
> In BYOC deployments, availability responsibilities shift -- Union.ai manages data plane cluster availability. See [Deployment models: Availability and resilience](./deployment-models#availability-and-resilience).
