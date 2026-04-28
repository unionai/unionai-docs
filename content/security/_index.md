---
title: Security
weight: 6
variants: -flyte +union
top_menu: true
---

# Security

This section provides a comprehensive overview of Union.ai's security architecture, practices, and compliance posture for enterprise security professionals evaluating the platform.
Beyond describing the security model, it provides concrete verification steps so that reviewers can independently confirm each claim against a running system.

## Overview

**[Architecture](./architecture/_index)**
The system is divided into a control plane hosted by Union.ai and a data plane hosted on the customer's infrastructure. The two planes are connected solely by Cloudflare Tunnel that is outbound-only from the customer data plane. No inbound firewall rules are required on the customer's network.

**[Data protection](./data-protection/_index)**
Bulk customer data (files, DataFrames, code bundles, container images) is stored in the customer's data plane and never enters the control plane. Smaller inline data (structured task inputs/outputs, secret values during creation, log streams) transits control plane memory transiently but is not persisted there. The control plane database stores orchestration metadata and task definitions (encrypted at rest), which include fields such as environment variables and default input values.

**[Identity and access](./identity-and-access/_index)**
Authentication via OIDC/SSO, API keys, and service accounts. Role-based access control enforces least privilege. Tenants are isolated at the database layer. Union.ai personnel cannot access customer data or secrets.

**[Threat model](./threat-model)**
Analysis of control plane compromise, tunnel interception, and presigned URL leakage scenarios, with the blast radius limited by the architectural separation described above.

**[Compliance and governance](./compliance/_index)**
SOC 2 Type II certified for Security, Availability, and Processing Integrity. Practices aligned to ISO 27001 and CIS benchmarks. Designed to meet HIPAA requirements. Public Trust Center at [trust.union.ai](https://trust.union.ai). Organizational security practices, vulnerability management, and shared responsibility model.

## Deployment models

Union.ai offers two deployment models, both sharing the same control plane / data plane architecture and security controls described in this section.

In **Self-Managed** deployments, the customer operates their data plane independently.
Union.ai has zero access to the customer's infrastructure, with the Cloudflare Tunnel as the only connection between Union.ai and the customer's network.

In **BYOC** deployments, Union.ai manages the Kubernetes cluster in the customer's cloud account via private connectivity (PrivateLink/PSC), handling upgrades, monitoring, and provisioning while maintaining strict separation from customer data, secrets, and logs.

For details, see [Deployment models](./architecture/deployment-models).
