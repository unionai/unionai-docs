---
title: GDPR alignment
weight: 4
variants: -flyte +union
---

# GDPR alignment

Union.ai's architecture inherently supports GDPR through its data residency model.

## EU data residency

For EU-region data planes, all customer data remains within the European Union.
Union.ai operates control plane endpoints in EU West-1 (Ireland), EU West-2 (London), and EU Central, ensuring that organizations can deploy with full EU data residency.

## Data handling

* The control plane stores only orchestration metadata -- no customer data payloads
* Customer data (task inputs/outputs, code, images, logs, secrets) resides exclusively in the customer's own cloud account and region
* Where error messages may contain user-generated content, this is documented and scoped

For details on what data resides where, see [Data classification and residency](../keys/data-classification-and-residency).
