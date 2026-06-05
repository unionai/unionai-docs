---
title: HIPAA compliance
weight: 2
variants: -flyte +union
---

# HIPAA compliance

Union.ai supports HIPAA compliance for organizations processing protected health information (PHI). The architectural separation between control plane and data plane described in [Two-plane separation](../architecture/two-plane-separation) is the foundation of HIPAA compliance.

No PHI ever transits Union.ai's control plane. Bulk PHI (files, DataFrames), structured task inputs and outputs, secret values, log streams, and reports are all served directly from the customer's data plane through the Direct-to-DataPlane tunnel; the control plane is not on the data path. PHI written to stdout/stderr flows through the tunnel to the requesting client without traversing Union.ai infrastructure.

To request a Business Associate Agreement (BAA), submit the request through Union.ai's [Trust Center](https://app.vanta.com/c/union/trust-center).

All data is encrypted at rest and in transit. RBAC policies restrict access to authorized users. All API requests are authenticated and logged with identity, operation, and timestamp. These guarantees apply equally to self-managed and BYOC deployments.

## Verification

### HIPAA compliance

**Reviewer focus:** Confirm that PHI remains exclusively in the customer's infrastructure and that appropriate safeguards are in place.

**How to verify:**

1. All data residency demonstrations apply. PHI stays in the customer's infrastructure. Run the verification steps described in [Data classification and residency](../data-protection/classification-and-residency) to confirm data residency.

2. Confirm Business Associate Agreement (BAA) availability via the [Trust Center](https://app.vanta.com/c/union/trust-center).

3. Map Union.ai's controls to HIPAA safeguard categories (Administrative, Physical, Technical) to validate coverage.
