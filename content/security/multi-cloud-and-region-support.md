---
title: Multi-cloud and region support
weight: 9
variants: -flyte +union
---

# Multi-cloud and region support

Union.ai supports data plane deployments across multiple cloud providers and regions, ensuring that organizations can meet their specific infrastructure and regulatory requirements.

## Supported cloud providers

| Cloud Provider | Object Store | Secrets Backend | Log Aggregator | Container Registry |
| --- | --- | --- | --- | --- |
| AWS | S3 | K8s Secrets / AWS Secrets Manager | CloudWatch Logs | ECR |
| GCP | GCS | K8s Secrets / GCP Secret Manager | Cloud Logging | GCR / Artifact Registry |
| Azure | Azure Blob Storage | K8s Secrets / Azure Key Vault | Azure Monitor | ACR |

Union Implementation Services supports additional cloud providers and on-premises deployments through a case-by-case engagement.

## Supported regions

Union.ai currently operates control planes in the following regions, with additional regions being added: **US West, US East, EU West, and EU Central**.
Customers choose the region for their data plane deployment, ensuring that all customer data remains within the selected geographic region.

## Consistent security across clouds

Regardless of the cloud provider selected, Union.ai enforces consistent security guarantees through its architecture: the same control plane/data plane separation, the same zero-trust data isolation (no customer data transits the control plane), the same presigned URL model, the same Direct-to-DataPlane tunnel connectivity, the same RBAC framework, and the same encryption standards.
The [Default and Enterprise 1 security tiers](./deployment-models) are available across all supported cloud providers.
Cloud-specific implementations (IAM roles, encryption services, log aggregators) are abstracted by the platform while maintaining native integration with each provider’s security services.
