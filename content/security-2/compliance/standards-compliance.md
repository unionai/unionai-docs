---
title: Standards compliance (ISO 27001, CIS)
weight: 5
variants: -flyte +union
---

# Standards compliance (ISO 27001, CIS)

In addition to certifications, Union.ai complies with the following standard control frameworks through its private data plane architecture:

| Framework | Control | Description |
| --- | --- | --- |
| ISO 27001 A.5.15 | Access control | Restricts access to network services and management interfaces; management endpoints not exposed to public Internet |
| ISO 27001 A.8.20 | Network security | Segregation and protection of networks; management interfaces on dedicated, private channels |
| ISO 27001 A.8.28 | Secure configuration | Minimizes public exposure of management plane by default |
| ISO 27001 A.8.21 | Cryptography | TLS encryption with minimized exposure of sensitive channels |
| ISO 27001 A.5.23 | Cloud service security | Cloud services configured securely with mitigated public exposure risks |
| CIS v8 4.4 | Administrative access | Administrative interfaces not exposed to Internet; VPN/bastion required |
| CIS v8 12.11 | Segment admin interfaces | Separation of administrative interfaces from public access |
| CIS v8 13.2 | Boundary protections | Management plane endpoints behind strong network segmentation |

Union.ai also holds CIS 1.4 AWS certification (restricted access benchmark) and is pursuing CIS 3.0 certification.
