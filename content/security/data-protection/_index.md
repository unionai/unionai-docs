---
title: Data protection
weight: 2
variants: -flyte +union
sidebar_expanded: true
---

# Data protection

Union.ai protects customer data through a classification framework, residency guarantees, and cloud-native encryption. All customer data is encrypted both at rest and in transit.

Customer data never transits Union.ai's control plane. Every customer-data request, whether bulk artifacts (via presigned URLs), structured task inputs and outputs, secret values, logs, reports, or auxiliary UI traffic, is served directly from the data plane through the Direct-to-Data-Plane tunnel, with authentication and RBAC enforced by an Envoy router inside the customer's cluster. The control plane is not on the data path.

This section covers:

* [Data classification and residency](./classification-and-residency): How data is classified, where it resides, and multi-cloud region support.
* [Secrets management](./secrets): Write-only API design, backends, and secret lifecycle.
* [Logging and audit](./logging-and-audit): Task logging, observability metrics, and audit trails.
