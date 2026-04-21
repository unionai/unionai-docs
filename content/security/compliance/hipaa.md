---
title: HIPAA compliance
weight: 2
variants: -flyte +union
---

# HIPAA compliance

Union.ai supports HIPAA compliance for organizations processing protected health information (PHI). All customer data, including PHI, remains in the customer's own cloud infrastructure. PHI is stored and processed only in the customer's data plane -- object store, secrets backend, container registry, and log aggregator. The control plane stores only orchestration metadata and never persists PHI.

> [!WARNING]
> **Audit finding (ref #3, #5, #6, #7):** If task inputs/outputs or log output contain PHI, they will transit control plane memory (structured I/O via `UploadInputs`/`GetActionData`, logs via streaming relay). PHI is not persisted in the control plane, but it does exist transiently in Union.ai process memory. Additionally, TaskSpec blobs (containing default values, environment variables) and error messages are persisted in the CP databases -- if these contain PHI, it would reside in Union.ai infrastructure. A full TaskSpec is stored on every run submission. There is no log content filtering or redaction, so PHI written to stdout/stderr flows through control plane memory unredacted.

All data is encrypted at rest and in transit. RBAC policies restrict access to authorized users. All API requests are authenticated and logged with identity, operation, and timestamp. These guarantees apply equally to self-managed and BYOC deployments.

The architectural separation between control plane and data plane described in [Two-plane separation](../architecture/two-plane-separation) is the foundation of HIPAA compliance -- PHI never leaves the customer's infrastructure.

> [!NOTE]
> **Audit finding (ref #3, #5):** "PHI never leaves the customer's infrastructure" should be qualified to: "PHI is not persistently stored outside the customer's infrastructure." PHI may transit control plane memory transiently if present in structured task I/O or log streams. See the architecture section annotations for the complete "passes through" / "resides in" / "never touches" taxonomy.

## Verification

### HIPAA compliance (Critical for healthcare, Low otherwise)

**Reviewer focus:** Confirm that PHI remains exclusively in the customer's infrastructure and that appropriate safeguards are in place.

**How to verify:**

1. All data residency demonstrations apply -- PHI stays in the customer's infrastructure. Run the verification steps described in [Two-plane separation](../architecture/two-plane-separation) to confirm data residency.

2. Confirm Business Associate Agreement (BAA) availability with Union.ai sales.

3. Map Union.ai's controls to HIPAA safeguard categories (Administrative, Physical, Technical) to validate coverage.
