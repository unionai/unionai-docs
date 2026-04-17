---
title: Standards compliance
weight: 4
variants: -flyte +union
---

# Standards compliance

Union.ai complies with ISO 27001 and CIS control frameworks through its private data plane architecture. The private connectivity model described in [Private connectivity](../architecture/private-connectivity) directly addresses the management interface controls required by both frameworks.

| Framework | Control | Description |
|---|---|---|
| ISO 27001 A.5.15 | Access control | Restricts access to network services and management interfaces; management endpoints not exposed to public Internet |
| ISO 27001 A.8.20 | Network security | Segregation and protection of networks; management interfaces on dedicated private channels |
| ISO 27001 A.8.28 | Secure configuration | Minimizes public exposure of management plane by default |
| ISO 27001 A.8.21 | Cryptography | TLS encryption with minimized exposure of sensitive channels |
| ISO 27001 A.5.23 | Cloud service security | Cloud services configured securely with mitigated public exposure risks |
| CIS v8 4.4 | Administrative access | Administrative interfaces not exposed to Internet; VPN/bastion required |
| CIS v8 12.11 | Segment admin interfaces | Separation of administrative interfaces from public access |
| CIS v8 13.2 | Boundary protections | Management plane endpoints behind strong network segmentation |

Union.ai also holds CIS 1.4 AWS certification and is pursuing CIS 3.0.

## Verification

### Standards compliance (Medium)

**Reviewer focus:** Confirm that the private connectivity architecture satisfies the referenced ISO 27001 and CIS controls.

**How to verify:**

1. The private connectivity architecture described in [Private connectivity](../architecture/private-connectivity) IS the demonstration of these controls -- management interfaces are not exposed to the public Internet.

2. The [Trust Center](https://trust.union.ai) covers continuous monitoring of compliance status.

3. This is architectural and audit-only verification.
