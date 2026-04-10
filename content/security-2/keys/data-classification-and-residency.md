---
title: Data classification and residency
weight: 3
variants: -flyte +union
---

# Data classification and residency

## Data classification

Union.ai maintains a rigorous data classification framework.
Every data type handled by the platform is classified by residency and access pattern:

| Data Type | Classification | Residency | Transits Control Plane? |
| --- | --- | --- | --- |
| Task inputs/outputs | Customer Data | Customer object store | No -- direct via presigned URL |
| Code bundles | Customer Data | Customer object store | No -- direct via presigned URL |
| Container images | Customer Data | Customer registry | No -- stays in customer infra |
| Reports (HTML) | Customer Data | Customer object store | No -- direct via presigned URL |
| Task logs | Customer Data | Customer log aggregator | Relayed in-memory (not stored) |
| Secrets | Customer Data | Customer secrets backend | Relayed during create (not stored) |
| Observability metrics | Customer Data | Customer data plane | Relayed in-memory (not stored) |
| Task definitions | Orchestration Metadata | Control plane DB | Yes -- metadata only |
| Run/action metadata | Orchestration Metadata | Control plane DB | Yes |
| User identity/RBAC | Platform Metadata | Control plane DB | Yes |
| Cluster records | Platform Metadata | Control plane DB | Yes |

## Data residency and sovereignty

Union.ai's architecture provides strong data residency guarantees.

### Data plane

* All customer data resides in the customer's own cloud account and region
* Customers choose the region for their data plane deployment

### Control plane

* Union.ai hosts your control plane in these supported regions: US West, US East, EU West-1 (Ireland), EU West-2 (London), EU Central, with more being added
* No customer data is replicated to or cached in Union.ai infrastructure. See [Data classification](#data-classification) for more detail on data classification and handling.

For organizations operating under GDPR or other data residency regulations, Union.ai's EU-region data planes ensure all customer data remains within the European Union.

## Supported cloud providers

| Cloud Provider | Object Store | Secrets Backend | Log Aggregator | Container Registry |
| --- | --- | --- | --- | --- |
| AWS | S3 | K8s Secrets / AWS Secrets Manager | CloudWatch Logs | ECR |
| GCP | GCS | K8s Secrets / GCP Secret Manager | Cloud Logging | GCR / Artifact Registry |
| Azure | Azure Blob Storage | K8s Secrets / Azure Key Vault | Azure Monitor | ACR |

Union Implementation Services supports additional cloud providers and on-premises deployments through a case-by-case engagement.

## Consistent security across clouds

Regardless of the cloud provider selected, Union.ai enforces consistent security guarantees through its architecture: the same control plane/data plane separation, the same presigned URL model, the same tunnel-based connectivity, the same RBAC framework, and the same encryption standards.
Cloud-specific implementations (IAM roles, encryption services, log aggregators) are abstracted by the platform while maintaining native integration with each provider's security services.

For the full multi-cloud reference, see [Multi-cloud and region support](../reference/multi-cloud-support).
