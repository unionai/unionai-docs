---
title: Data protection
weight: 2
variants: -flyte +union
---

# Data protection

> [!TIP] Updated for zero-trust architecture
> This page has been updated to reflect the zero-trust security architecture. Tabbed comparisons below highlight key changes.

## Data classification

Union.ai maintains a rigorous data classification framework.
Every data type handled by the platform is classified by residency and access pattern:

{{< tabs >}}
{{< tab "Zero-trust (current)" >}}
{{< markdown >}}
| Data Type | Classification | Residency | Transits Control Plane? |
| --- | --- | --- | --- |
| Task inputs/outputs | Customer Data | Customer object store | No — direct via presigned URL |
| Code bundles | Customer Data | Customer object store | No — direct via presigned URL |
| Container images | Customer Data | Customer registry | No — stays in customer infra |
| Reports (HTML) | Customer Data | Customer object store | No — direct via presigned URL |
| Task logs | Customer Data | Customer log aggregator | No — served directly from data plane |
| Secrets | Customer Data | Customer secrets backend | Relayed during create (not stored) |
| Observability metrics | Customer Data | Customer data plane | No — served directly from data plane |
| Task definitions | Orchestration Metadata | Control plane DB | Yes — metadata only |
| Run/action metadata | Orchestration Metadata | Control plane DB | Yes |
| User identity/RBAC | Platform Metadata | Control plane DB | Yes |
| Cluster records | Platform Metadata | Control plane DB | Yes |
{{< /markdown >}}
{{< /tab >}}
{{< tab "Previous architecture" >}}
{{< markdown >}}
| Data Type | Classification | Residency | Transits Control Plane? |
| --- | --- | --- | --- |
| Task inputs/outputs | Customer Data | Customer object store | No — direct via presigned URL |
| Code bundles | Customer Data | Customer object store | No — direct via presigned URL |
| Container images | Customer Data | Customer registry | No — stays in customer infra |
| Reports (HTML) | Customer Data | Customer object store | No — direct via presigned URL |
| Task logs | Customer Data | Customer log aggregator | Relayed in-memory (not stored) |
| Secrets | Customer Data | Customer secrets backend | Relayed during create (not stored) |
| Observability metrics | Customer Data | Customer data plane | Relayed in-memory (not stored) |
| Task definitions | Orchestration Metadata | Control plane DB | Yes — metadata only |
| Run/action metadata | Orchestration Metadata | Control plane DB | Yes |
| User identity/RBAC | Platform Metadata | Control plane DB | Yes |
| Cluster records | Platform Metadata | Control plane DB | Yes |
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

> [!NOTE] Information needed
> The zero-trust architecture eliminates all data transit through the control plane for visualization and retrieval. Whether the secret creation relay is also being changed is not yet confirmed.

## Zero-trust data guarantees

Union.ai's zero-trust architecture ensures that no customer data, operational metadata, or logs ever transit through the control plane.
This guarantee applies to all data retrieval and visualization operations:

* **Task inputs and outputs** are accessed via presigned URLs generated entirely on the data plane
* **Logs** are served directly from the data plane via the [Direct-to-DataPlane tunnel](./network-security#direct-to-dataplane-tunnel)
* **Observability metrics** are served directly from the data plane
* **Reports and code bundles** are accessed via presigned URLs generated on the data plane
* **Apps and auxiliary UIs** (Ray dashboard, Spark history server) are served from the data plane

The control plane handles only orchestration metadata: task definitions, run/action state, user identity, and cluster records.

This zero-trust guarantee is contractual.
See [Deployment models and security tiers](./deployment-models) for details on the Default and Enterprise 1 configurations.

## Encryption at rest

All data at rest is encrypted using cloud-provider native encryption:

| Storage | Encryption Standard | Key Management |
| --- | --- | --- |
| Object Store (S3/GCS/Azure Blob) | Cloud-provider default (SSE-S3, Google-managed, Azure SSE) | Cloud provider managed; CMK supported |
| Container Registry | Cloud-provider encryption | Cloud provider managed |
| Secrets Backend (cloud) | Cloud-provider encryption | Cloud secrets manager |
| Secrets Backend (K8s) | `etcd` encryption | K8s cluster-level encryption |
| ClickHouse | Encrypted EBS/persistent disk | Cloud provider managed |
| Control Plane PostgreSQL | AWS RDS encryption | AES-256; AWS KMS managed |

## Encryption in transit

Union.ai enforces encryption for all data in transit.
No unencrypted communication paths exist in the platform architecture.

- All client-to-control-plane communication uses TLS 1.2 or higher.
- All control-plane-to-data-plane communication uses mutual TLS via Cloudflare Tunnel.
- All client-to-data-plane communication (via the Direct-to-DataPlane tunnel) uses TLS 1.2 or higher, with authentication enforced by the Envoy router.
- All client-to-object-store communication (via presigned URLs) uses HTTPS, enforced by cloud providers.
- All internal data plane communication uses cloud-native TLS.

## Data residency and sovereignty

Union.ai's architecture provides strong data residency guarantees:

### Data plane

* All customer data resides exclusively in the customer's own cloud account and region. Under the zero-trust architecture, customer data never leaves the customer's infrastructure — not even temporarily for visualization.
* Customers choose the region for their data plane deployment

### Control plane

* Union.ai hosts your control plane in these supported regions: US West, US East, EU West-1 (Ireland), EU West-2 (London), EU Central, with more being added
* No customer data is stored, relayed, or cached in Union.ai infrastructure. See [Data classification](#data-classification) for more detail on data classification and handling.

For organizations operating under GDPR or other data residency regulations, Union.ai's EU-region data planes ensure all customer data remains within the European Union.
