---
title: Data protection
description: The classification framework, residency guarantees, and encryption that protect customer data.
icon: file-lock
weight: 2
variants: -flyte +union
sidebar_expanded: true
---

# Data protection

Union.ai protects customer data through a classification framework, residency guarantees, and cloud-native encryption. All customer data is encrypted both at rest and in transit.

Customer data never transits Union.ai's control plane. Every customer-data request -- bulk artifacts (via presigned URLs), structured task inputs and outputs, secret writes, logs, reports, and auxiliary UI traffic -- is served directly from the data plane through the Direct-to-Data-Plane tunnel, with authentication and RBAC enforced by an Envoy router inside the customer's cluster. The control plane is not on the data path.

This section covers:

{{< subpage-cards >}}
