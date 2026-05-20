---
title: GDPR alignment
weight: 3
variants: -flyte +union
---

# GDPR alignment

Union.ai's architecture inherently supports GDPR through its data residency model. For EU-region data planes, all customer data remains within the European Union. Union.ai operates control plane endpoints in EU West-1 (Ireland), EU West-2 (London), and EU Central (Frankfurt), ensuring organizations can deploy with full EU data residency.

The control plane stores orchestration metadata and task definitions (encrypted at rest), which may include fields such as environment variables and default input values. No customer data payloads are stored in or transit the control plane. Structured task I/O, secret values, and log streams are served directly from the customer's data plane through the Direct-to-DataPlane tunnel and never enter the control plane region. Only orchestration metadata (run IDs, schedules, phase transitions, RBAC graph) resides in the control plane region; customers should select a control plane region consistent with their metadata residency requirements. When both planes are in EU regions (EU West-1, EU West-2, or EU Central), all data and metadata (both at rest and in transit) stay within the EU.

For details on how data residency is enforced architecturally, see [Data classification and residency](../data-protection/classification-and-residency) and [Two-plane separation](../architecture/two-plane-separation).

## Verification

### GDPR alignment

**Reviewer focus:** Confirm that all customer data remains within the EU for EU-region deployments and that the control plane does not store data payloads.

**How to verify:**

1. Follow the data residency verification steps described in [Data classification and residency](../data-protection/classification-and-residency#data-residency). All data resides in EU-region infrastructure.

2. Confirm that the control plane endpoints are deployed in EU regions (EU West-1, EU West-2, EU Central).

3. This is architectural verification. The [two-plane separation](../architecture/two-plane-separation) ensures data never leaves the customer's cloud account.
