---
title: Operations
weight: 5
variants: -flyte +union
sidebar_expanded: true
---

# Operations

Union.ai implements comprehensive operational security controls covering logging, monitoring, audit trails, vulnerability management, threat modeling, and organizational practices.

## Security architecture benefits

The following table summarizes how Union.ai's architectural decisions translate into concrete security benefits:

| Decision | Benefit |
| --- | --- |
| Control plane stores no customer data | Minimizes blast radius of control plane compromise |
| Outbound-only tunnel | No inbound attack surface on customer network |
| Presigned URLs for data access | No persistent data access credentials |
| Write-only secrets API | Cannot exfiltrate secrets via API |
| Workload identity federation | No static credentials on data plane |
| Per-org database scoping | Enforces tenant isolation at data layer |
| Cloud-native encryption | Leverages provider-managed encryption |

## Sections

* [Logging and audit](./logging-and-audit): Task logging, observability metrics, audit trails, and incident response.
* [Vulnerability management](./vulnerability-management): Vulnerability assessment, patch management, incident response, and third-party dependency risk.
* [Threat modeling](./threat-modeling): Analysis of control plane compromise, tunnel interception, and presigned URL leakage scenarios.
* [Organizational security](./organizational-security): Employee security lifecycle, governance controls, and the security development lifecycle.
