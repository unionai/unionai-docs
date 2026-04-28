---
title: Multi-cloud support
weight: 6
variants: -flyte +union
---

# Multi-cloud support

Union.ai supports data plane deployments on AWS, GCP, and Azure. Each cloud provider uses its native services for storage, secrets, logging, and container registry, while the platform enforces consistent security guarantees across all three.

## Supported services

| Cloud | Object Store | Secrets Backend | Log Aggregator | Container Registry |
|---|---|---|---|---|
| AWS | S3 | K8s Secrets / AWS Secrets Manager | CloudWatch Logs | ECR |
| GCP | GCS | K8s Secrets / GCP Secret Manager | Cloud Logging | GCR / Artifact Registry |
| Azure | Azure Blob Storage | K8s Secrets / Azure Key Vault | Azure Monitor | ACR |

Union Implementation Services supports additional cloud providers and on-premises deployments through case-by-case engagement.

## Consistent security guarantees

Regardless of cloud provider, Union.ai enforces the same security model: control plane / data plane separation, presigned URLs for bulk data access (bypassing the control plane), inline proxying for structured task I/O (transiting control plane memory, not persisted), Cloudflare Tunnel-based connectivity between planes, RBAC-based access control, and encryption at rest and in transit. Cloud-specific implementations (IAM roles, encryption services, log aggregators, and secrets managers) are abstracted by the platform while maintaining native integration with each provider's security services. A workflow running on AWS receives the same separation guarantees as one running on GCP or Azure; only the underlying cloud primitives differ. Data residency at rest is maintained within the customer's chosen cloud and region.

For details on the data flow patterns that apply across all clouds, see [Data flow](./data-flow). For encryption specifics by storage type, see [Encryption](./encryption). For secrets backend options, see [Secrets management](./secrets).

## Verification

### Multi-cloud support

**Reviewer focus:** Confirm that the services listed for each cloud provider are accurate.

**How to verify:** This is a factual reference table, not a claim requiring active demonstration. Verify against the Union.ai deployment documentation and cloud provider configurations for each supported deployment.
