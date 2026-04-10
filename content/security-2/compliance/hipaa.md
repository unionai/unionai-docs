---
title: HIPAA compliance
weight: 3
variants: -flyte +union
---

# HIPAA compliance

Union.ai supports HIPAA compliance for organizations processing protected health information (PHI).

## Architectural support for HIPAA

All customer data -- including PHI -- remains in the customer's own cloud infrastructure:

* **Data residency:** PHI is stored and processed only in the customer's data plane (object store, secrets backend, container registry, log aggregator)
* **Control plane isolation:** The control plane stores only orchestration metadata and never persists PHI
* **Encryption:** All data is encrypted at rest and in transit (see [Encryption at rest](../keys/encryption-at-rest) and [Encryption in transit](../keys/encryption-in-transit))
* **Access controls:** RBAC policies restrict access to authorized users (see [Role-based access control](../auth/rbac))
* **Audit trail:** All API requests are authenticated and logged with identity, operation, and timestamp

These guarantees apply equally to self-managed and BYOC deployments.
