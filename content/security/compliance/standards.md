---
title: Standards compliance
description: How the private data plane architecture aligns with the ISO 27001 and CIS control frameworks.
icon: journal-text
weight: 4
variants: -flyte +union
---

# Standards compliance

Union.ai's private data plane architecture is designed to align with the ISO 27001 and CIS control frameworks. When a BYOC cluster on EKS or GKE is configured with a private endpoint, the private connectivity model described in [Private connectivity](../architecture/private-connectivity) addresses the management interface controls in both frameworks. Without a private endpoint, which is the default, the cluster's Kubernetes API endpoint is public.

| Framework | Control | Description |
|---|---|---|
| ISO 27001 A.5.15 | Access control | Restricts access to network services and management interfaces; management endpoints not exposed to the public internet |
| ISO 27001 A.5.23 | Information security for use of cloud services | Cloud services configured securely with mitigated public exposure risks |
| ISO 27001 A.8.20 | Networks security | Segregation and protection of networks; management interfaces on dedicated private channels |
| ISO 27001 A.8.22 | Segregation of networks | Management plane separated from public networks |
| ISO 27001 A.8.24 | Use of cryptography | TLS encryption with minimized exposure of sensitive channels |
| CIS Controls v8, Control 12 | Network infrastructure management | Administrative interfaces not exposed to the public internet; management endpoints behind network segmentation |
| CIS Controls v8, Control 13 | Network monitoring and defense | Traffic filtering between network segments; boundary protections on management plane endpoints |

Union.ai also holds CIS 1.4 AWS certification and is pursuing CIS 3.0.

## Verification

### Standards compliance

**Reviewer focus:** For a BYOC cluster on EKS or GKE configured with a private endpoint, confirm that the private connectivity architecture satisfies the referenced ISO 27001 and CIS management-interface controls.

**How to verify:**

1. For a BYOC cluster configured with a private endpoint (EKS or GKE only), the private connectivity architecture described in [Private connectivity](../architecture/private-connectivity) is the demonstration of these controls: the Kubernetes API isn't reachable from the public internet. Follow the verification steps on that page to confirm it. By default, a BYOC cluster has no private endpoint, and its Kubernetes API endpoint is public.

2. The [Trust Center](https://trust.union.ai) covers continuous monitoring of compliance status.

3. Apart from the private-endpoint checks in step 1, this is architectural and audit-only verification.
