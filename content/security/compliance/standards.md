---
title: Standards compliance
weight: 4
variants: -flyte +union
---



# Standards compliance

Union.ai aligns with ISO 27001 and CIS control frameworks through its private data plane architecture. The private connectivity model described in [Private connectivity](../architecture/private-connectivity) directly addresses the management interface controls in both frameworks.

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

**Reviewer focus:** Confirm that the private connectivity architecture satisfies the referenced ISO 27001 and CIS controls.

**How to verify:**

1. The private connectivity architecture described in [Private connectivity](../architecture/private-connectivity) IS the demonstration of these controls: management interfaces are not exposed to the public Internet.

2. The [Trust Center](https://trust.union.ai) covers continuous monitoring of compliance status.

3. This is architectural and audit-only verification.
