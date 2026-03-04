---
title: Organizational security practices
weight: 11
variants: -flyte +byoc +selfmanaged
---

# Organizational security practices

Union.ai maintains organizational security controls independently verified through SOC 2 Type II audits and continuously monitored via the Vanta Trust Center (trust.union.ai).

## Employee security lifecycle

**Verified controls*** (source: Trust Center, SOC 2 Type II audit)*

| Control | Description | Verification |
| --- | --- | --- |
| Background checks | All employees with access to production systems undergo background checks prior to onboarding | SOC 2 Type II |
| Security awareness training | Required within 30 days of hire and annually thereafter for all employees | Trust Center (passing) |
| Confidentiality agreements | Signed by all employees and contractors during onboarding | Trust Center (passing) |
| Code of conduct | Acknowledged by all employees and contractors; violations subject to disciplinary action | Trust Center (passing) |
| Access provisioning | Documented procedures for granting, modifying, and revoking user access | Trust Center (passing) |
| Termination checklists | Access revoked for terminated employees via formal checklist process | Trust Center (passing) |
| Performance evaluations | Managers complete evaluations for direct reports at least annually | Trust Center (passing) |
| Least-privilege access | Internal systems follow least-privilege; regular access reviews conducted | SOC 2 Type II |

## Governance and organizational controls

| Control | Description | Verification |
| --- | --- | --- |
| Defined security roles | Formal roles and responsibilities for design, implementation, and monitoring of security controls | Trust Center (passing) |
| Organizational structure | Documented org chart with reporting relationships | Trust Center (passing) |
| Board-level oversight | Board or relevant subcommittee briefed by senior management on security and risk at least annually | Trust Center (passing) |
| Information security policies | Policies and procedures documented and reviewed at least annually | Trust Center (passing) |
| Whistleblower policy | Formalized policy with anonymous communication channel for reporting violations | Trust Center (passing) |
| Vendor management | Third-party vendors and sub-processors evaluated and monitored; sub-processor list available via Trust Center | SOC 2 Type II |
| Business continuity | BC/DR plans aligned with SOC 2; BYOC architecture provides natural resilience since customer data resides in customer infrastructure | SOC 2 Type II |

## Security development lifecycle

* **Secure coding:** Guidelines enforced through mandatory code review processes
* **Automated security testing:** Integrated into CI/CD pipelines
* **Dependency scanning:** Vulnerability scanning and management for all software dependencies
* **Infrastructure-as-code:** Version-controlled security configurations
* **Penetration testing:** Regular third-party security assessments
* **Incident response:** Documented procedures aligned with SOC 2 Type II, including defined escalation paths and post-incident review

*All controls marked as “passing” are continuously monitored via Vanta and verified through the Union.ai Trust Center at trust.union.ai.
The SOC 2 Type II audit report is available upon request.*
