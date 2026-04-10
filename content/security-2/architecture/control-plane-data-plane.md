---
title: Control plane and data plane separation
weight: 1
variants: -flyte +union
---

# Control plane and data plane separation

Union.ai's security architecture is founded on the principle of strict separation between orchestration (control plane) and execution (data plane).
This architectural decision ensures that customer data remains within the customer's own cloud infrastructure at all times.

The control plane and data plane serve fundamentally different purposes and handle different types of data:

## Control plane (Union.ai hosted)

The control plane is responsible for workflow orchestration, user management, and providing the web interface.
It runs within Union.ai's AWS account and stores only orchestration metadata in a managed PostgreSQL database.
This metadata includes task definitions (image references, resource requirements, typed interfaces), run and action metadata (identifiers, phase, timestamps, error information), user identity and RBAC records, cluster configuration and health records, and trigger/schedule definitions.
The control plane never stores customer data payloads.
It stores only references (URIs) to data in the customer's object store, no data.
When data must be surfaced to a client, the control plane either proxies a signing request to generate a presigned URL or relays a data stream from the data plane without persisting it.

**See comprehensive list of control plane roles and permissions in [Kubernetes RBAC: control plane](../reference/kubernetes-rbac-control-plane).**

### Control plane infrastructure

The Union.ai control plane is hosted on AWS with enterprise-grade infrastructure security:

* Managed PostgreSQL (AWS RDS) with AES-256 encryption at rest
* Network isolation via VPC with restricted security groups
* TLS termination at the edge for all incoming connections
* Automated backups and disaster recovery procedures
* Infrastructure-as-code deployment with version-controlled configurations
* Automated patch management and security updates

## Data plane (customer hosted)

The data plane runs inside the customer's own cloud account on their own Kubernetes cluster.
All customer data resides here, including:

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

**See comprehensive list of data plane roles and permissions in [Kubernetes RBAC: data plane](../reference/kubernetes-rbac-data-plane).**

### Kubernetes security

The data plane runs on customer-managed Kubernetes clusters (or Union.ai-managed clusters in [BYOC deployments](./deployment-models)). Union supports the following security measures:

* Workload identity federation for pod-level IAM role binding (no static credentials)
* Kubernetes RBAC for service account permissions within the cluster
* Network policies for pod-to-pod communication isolation
* Resource quotas and limit ranges to prevent resource abuse
* Pod security contexts enforcing non-root execution where applicable

### Container security

Union.ai's container security model ensures that code execution is isolated and controlled:

* Image Builder runs on the customer's cluster using Buildkit, ensuring source code and built images never leave customer infrastructure
* Base images are pulled from customer-approved registries (public or private)
* Built images are pushed to the customer's container registry (ECR/GCR/ACR)
* Task pods mount code bundles via presigned URLs with limited TTL
* Container images follow customer-defined tagging and scanning policies

### IAM and workload identity

Two IAM roles are provisioned per data plane, each with narrowly scoped permissions. In BYOC deployments, [Union.ai provisions these roles](./deployment-models#iam-role-provisioning); in self-managed, the customer provisions them.

| Role | Permissions | Assumed By | Mechanism |
| --- | --- | --- | --- |
| Admin Role (`adminflyterole`) | R/W to object store buckets, secrets manager access, persisted logs read | Platform services: Executor, Object Store Service, DataProxy | Workload identity federation |
| User Role (`userflyterole`) | R/W to object store buckets | Task pods (user workloads) | Workload identity via K8s service account annotation |

These roles use cloud-native workload identity federation (IAM Roles for Service Accounts on AWS, Workload Identity on GCP, Azure Workload Identity on Azure), eliminating the need for static credential storage.

For the full IAM role mapping, see [AWS IAM roles](../reference/aws-iam-roles).

## Availability, response time, and resilience

Union.ai's architecture separates the availability characteristics of the control plane and data plane, providing resilience even during partial outages.

### Control plane availability

The Union.ai control plane runs on AWS with multi-AZ redundancy, managed PostgreSQL (RDS) with automated failover, and continuous monitoring. Union.ai's SOC 2 Type II audit covers availability as a trust service criterion. The control plane is designed for high availability, with automated recovery and health monitoring. Specific SLA targets are defined in customer contracts and are available upon request.

### Data plane resilience during control plane outages

Because the data plane runs entirely within the customer's Kubernetes cluster, in-flight workflows continue executing even if the control plane becomes temporarily unavailable. The Executor, which manages pod lifecycle, operates as a Kubernetes controller on the customer's cluster and does not require real-time connectivity to the control plane to continue running pods that have already been scheduled. State transitions will be reconciled when connectivity is restored. However, new workflow submissions and scheduling operations require control plane availability.

The customer is solely responsible for data plane availability, including Kubernetes cluster operations, node pool management, upgrades, and monitoring. Union.ai's availability commitment covers only the control plane.

> [!NOTE]
> In BYOC deployments, availability responsibilities shift -- Union.ai manages data plane cluster availability. See [Deployment models and BYOC differences: Availability and resilience](./deployment-models#availability-and-resilience).
