---
title: GDPR alignment
description: How the data residency model keeps EU customer data in the EU, and which control plane endpoints serve it.
icon: flag
weight: 3
variants: -flyte +union
---

# GDPR alignment

Union.ai's architecture inherently supports GDPR through its data residency model. On this page, an EU region is a cloud region located in an EU member state. EU West-2 (London) is in the United Kingdom, which is outside the EU, so it is not an EU region. For EU-region data planes, all customer data remains within the European Union. At signup, an organization's control plane can be placed in two European regions: EU West-2 (London) and EU Central (Frankfurt). Full EU data residency requires the EU Central control plane.

The control plane stores orchestration metadata (including task definitions), encrypted at rest. When the data plane is in an EU region and the control plane is in EU Central, all data and metadata (both at rest and in transit) stay within the EU.

For details on how data residency is enforced architecturally, see [Data classification and residency](../data-protection/classification-and-residency) and [Two-plane separation](../architecture/two-plane-separation).

## Verification

### GDPR alignment

**Reviewer focus:** Confirm that all customer data remains within the EU for EU-region deployments and that the control plane does not store data payloads.

**How to verify:**

1. Follow the data residency verification steps described in [Data classification and residency](../data-protection/classification-and-residency#data-residency). All data resides in EU-region infrastructure.

2. Confirm that the organization's control plane endpoint is deployed in EU Central (eu-central-1).

3. This is architectural verification. The [two-plane separation](../architecture/two-plane-separation) ensures data never leaves the customer's cloud account.
