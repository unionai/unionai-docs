---
title: GDPR alignment
weight: 3
variants: -flyte +union
---

# GDPR alignment

Union.ai's architecture inherently supports GDPR through its data residency model. For EU-region data planes, all customer data remains within the European Union. Union.ai operates control plane endpoints in EU West-1 (Ireland), EU West-2 (London), and EU Central, ensuring organizations can deploy with full EU data residency.

The control plane stores orchestration metadata and task definitions (encrypted at rest), which may include fields such as environment variables and default input values. No bulk customer data payloads are stored in the control plane. Inline data -- structured task I/O, secret values during creation, and log streams -- transits control plane memory during request processing but is not persisted. This transit occurs through the control plane region, so customers should select a control plane region consistent with their data residency requirements. When both planes are in EU regions (EU West-1, EU West-2, or EU Central), all data -- both at rest and in transit -- stays within the EU.

For details on how data residency is enforced architecturally, see [Two-plane separation](../architecture/two-plane-separation) and [Data plane](../architecture/data-plane).

## Verification

### GDPR alignment (Critical for EU, Low otherwise)

**Reviewer focus:** Confirm that all customer data remains within the EU for EU-region deployments and that the control plane does not store data payloads.

**How to verify:**

1. Follow the same data residency verification steps described in [Two-plane separation](../architecture/two-plane-separation) -- all data resides in EU-region infrastructure.

2. Confirm that the control plane endpoints are deployed in EU regions (EU West-1, EU West-2, EU Central).

3. This is architectural verification -- the [two-plane separation](../architecture/two-plane-separation) ensures data never leaves the customer's cloud account.
