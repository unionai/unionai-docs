---
title: GDPR alignment
weight: 3
variants: -flyte +union
---

Union.ai's architecture inherently supports GDPR through its data residency model. For EU-region data planes, all customer data remains within the European Union. Union.ai operates control plane endpoints in EU West-1 (Ireland), EU West-2 (London), and EU Central, ensuring organizations can deploy with full EU data residency.

The control plane stores only orchestration metadata -- no customer data payloads. Customer data resides exclusively in the customer's own cloud account and region. Where error messages may contain user-generated content, this is documented and scoped.

For details on how data residency is enforced architecturally, see [Two-plane separation](../architecture/two-plane-separation) and [Data plane](../architecture/data-plane).

## Verification

### GDPR alignment (Critical for EU, Low otherwise)

**Reviewer focus:** Confirm that all customer data remains within the EU for EU-region deployments and that the control plane does not store data payloads.

**How to verify:**

1. Follow the same data residency verification steps described in [Two-plane separation](../architecture/two-plane-separation) -- all data resides in EU-region infrastructure.

2. Confirm that the control plane endpoints are deployed in EU regions (EU West-1, EU West-2, EU Central).

3. This is architectural verification -- the [two-plane separation](../architecture/two-plane-separation) ensures data never leaves the customer's cloud account.
