---
title: HIPAA compliance
weight: 3
variants: -flyte +union
---

# HIPAA compliance

Union.ai is designed to support HIPAA compliance requirements, enabling healthcare and life sciences organizations to process protected health information (PHI) within their data planes.

## Architectural support for HIPAA

Because all customer data -- including any PHI -- remains exclusively in the customer's own cloud infrastructure, Union.ai's architecture inherently supports HIPAA's data protection requirements:

* **Data residency:** PHI is stored and processed only in the customer's data plane (object store, secrets backend, container registry, log aggregator)
* **Control plane isolation:** The control plane stores only orchestration metadata and never persists PHI
* **Encryption:** All data is encrypted at rest and in transit (see [Encryption at rest](../keys/encryption-at-rest) and [Encryption in transit](../keys/encryption-in-transit))
* **Access controls:** RBAC policies restrict access to authorized users (see [Role-based access control](../auth/rbac))
* **Audit trail:** All API requests are authenticated and logged with identity, operation, and timestamp

## BYOC applicability

Union.ai's HIPAA compliance support applies equally to both Self-Managed and BYOC deployment models. The architecture ensures that all customer data -- including any PHI -- remains exclusively in the customer's own cloud infrastructure regardless of who manages the K8s cluster. The control plane stores only orchestration metadata and never persists PHI.
