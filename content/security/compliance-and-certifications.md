---
title: Compliance and certifications
weight: 8
variants: -flyte +byoc +selfmanaged
---

# Compliance and certifications

## Certifications overview

Union.ai maintains a rigorous certification program validated by independent third-party auditors.
Full details at the [Union.ai Trust Center](https://trust.union.ai/).

| Standard | Certification | Status |
| --- | --- | --- |
| SOC 2 Type II | Security, Availability, Integrity | Certified |
| SOC 2 Type I | Security, Availability, Integrity |  Certified |
| HIPAA | Health data privacy and security |  Compliant* |
| CIS 1.4 AWS | Restricted access benchmark |  Certified |
| CIS 3.0 | Security benchmark | In progress |

- * Union is designed to meet HIPAA compliance requirements for handling Protected Health Information (PHI).
- The SOC 2 Type II audit was conducted over a 12-week period and is available upon request.
Key areas covered include protection against unauthorized access (Security), system availability commitments and disaster recovery (Availability), and complete, valid, accurate, and timely processing (Processing Integrity).
- Union.ai uses Vanta for continuous compliance monitoring and automated control assessments.

## Standards compliance

In addition to certifications, Union.ai complies with the following standard control frameworks through its private compute plane architecture:

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

## HIPAA compliance

Union.ai is HIPAA certified, enabling healthcare and life sciences organizations to process protected health information (PHI) within their BYOC compute planes.
Because all customer data—including any PHI—remains exclusively in the customer’s own cloud infrastructure, Union.ai’s architecture inherently supports HIPAA’s data protection requirements.
The control plane stores only orchestration metadata and never persists PHI.

## GDPR alignment

Union.ai’s architecture inherently supports GDPR through its data residency model.
For EU-region compute planes, all customer data remains within the European Union.
The control plane stores only orchestration metadata, and where error messages may contain user-generated content, this is documented and scoped.

## Trust Center

Union.ai maintains a public Trust Center at trust.union.ai (powered by Vanta), providing real-time transparency into the company’s security controls, compliance status, and security practices.
The Trust Center provides up-to-date information on certifications, downloadable resources (SOC 2 reports upon request), and over 70 verified security controls organized across five categories:

| Control Category | Controls | Key Controls Include |
| --- | --- | --- |
| Infrastructure Security | 17 controls | Encryption key access restricted, unique account authentication enforced, production application/database/OS/network access restricted, intrusion detection, log management, network segmentation, firewalls reviewed and utilized, network hardening standards |
| Organizational Security | 13 controls | Asset disposal procedures, production inventory, portable media encryption, anti-malware, code of conduct, confidentiality agreements, password policy, MDM, security awareness training |
| Product Security | 5 controls | Data encryption at rest, control self-assessments, penetration testing, data transmission encryption, vulnerability/system monitoring |
| Internal Security Procedures | 35 controls | BC/DR plans established and tested, cybersecurity insurance, change management, SDLC, incident response tested, risk assessments, vendor management, board oversight, whistleblower policy |
| Data and Privacy | 3 controls | Data retention procedures, customer data deleted upon leaving, data classification policy |

## Shared responsibility model

Union.ai operates under a shared responsibility model:

| Responsibility Area | Union.ai | Customer |
| --- | --- | --- |
| Control plane security | Full ownership | N/A |
| Compute plane infrastructure | Guidance and tooling | Provisioning and maintenance |
| Data encryption at rest | Default cloud encryption | Optional CMK configuration |
| Network security (tunnel) | Tunnel management | Firewall and VPC configuration |
| IAM roles and policies | Role templates and documentation | Role creation and binding |
| Secrets management | API and relay infrastructure | Backend selection and secret values |
| Application-level access control | RBAC framework | Role assignment and policy |
| Compliance documentation | SOC 2 report, Trust Center | Customer-specific attestations |
