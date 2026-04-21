---
title: HIPAA compliance
weight: 2
variants: -flyte +union
---

# HIPAA compliance

Union.ai supports HIPAA compliance for organizations processing protected health information (PHI). Bulk PHI (files, DataFrames, container images) is stored and processed only in the customer's data plane and never enters the control plane. Structured task inputs/outputs and log streams that may contain PHI transit control plane memory during request processing (encrypted in transit, plaintext in memory, not persisted, cached, or logged). Task definitions stored in the control plane databases may contain fields such as environment variables and default input values -- if these contain PHI, it would be persisted (encrypted at rest) in Union.ai infrastructure. Error messages from task executions are also persisted in the control plane and may contain customer data from tracebacks. There is no log content filtering or redaction, so PHI written to stdout/stderr flows through control plane memory unmodified.

All data is encrypted at rest and in transit. RBAC policies restrict access to authorized users. All API requests are authenticated and logged with identity, operation, and timestamp. These guarantees apply equally to self-managed and BYOC deployments.

The architectural separation between control plane and data plane described in [Two-plane separation](../architecture/two-plane-separation) is the foundation of HIPAA compliance. Bulk PHI is not stored outside the customer's infrastructure. Inline PHI (if present in structured I/O or log streams) transits the control plane transiently but is not persisted there. Organizations should evaluate whether task definitions or error messages in their workflows could contain PHI and scope their BAA accordingly.

## Verification

### HIPAA compliance (Critical for healthcare, Low otherwise)

**Reviewer focus:** Confirm that PHI remains exclusively in the customer's infrastructure and that appropriate safeguards are in place.

**How to verify:**

1. All data residency demonstrations apply -- PHI stays in the customer's infrastructure. Run the verification steps described in [Two-plane separation](../architecture/two-plane-separation) to confirm data residency.

2. Confirm Business Associate Agreement (BAA) availability with Union.ai sales.

3. Map Union.ai's controls to HIPAA safeguard categories (Administrative, Physical, Technical) to validate coverage.
