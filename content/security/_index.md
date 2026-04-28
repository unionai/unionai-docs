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
The system is divided into a control plane hosted by Union.ai and a data plane hosted on the customer's infrastructure. The two planes are connected by two routes: a Cloudflare Tunnel and a GRPC connection. Both are outbound-only from the customer data plane to the control plane. Consequently, no inbound firewall rules are required on the customer's network.

**[Data protection](./data-protection/_index)**
Bulk customer data (files, DataFrames, code bundles, container images) is stored in the customer's data plane and never enters the control plane. Smaller inline data (structured task inputs/outputs, secret values during creation, log streams) transits control plane memory only temporarily and is not persisted there. The control plane database stores orchestration metadata and task definitions (encrypted at rest), which include fields such as environment variables and default input values.

**[Identity and access](./identity-and-access/_index)**
Authentication is done via OIDC/SSO, API keys, and service accounts. Role-based access control enforces least-privilege. Union.ai personnel cannot access customer data or secrets.

**[Threat model](./threat-model)**
An analysis of potential threats and how they are mitigated is provided. Control plane compromise, tunnel interception, and presigned URL leakage scenarios are examined, and the architectural design and security controls that mitigate these risks are described. The goal is to demonstrate that even in worst-case scenarios, customer data remains protected.

**[Compliance and governance](./compliance/_index)**
Union.ai is SOC 2 Type II certified for Security, Availability, and Processing Integrity, with practices aligned to ISO 27001 and CIS benchmarks. The platform is designed to meet HIPAA requirements. Details are available in the Public Trust Center at [trust.union.ai](https://trust.union.ai). This includes organizational security practices, vulnerability management, and a shared responsibility model.

## Deployment models

Union.ai offers two deployment models, both sharing the same control plane / data plane architecture and security controls described in this section.

In **BYOC** deployments, Union.ai manages the Kubernetes cluster in the customer's cloud account via private connectivity (PrivateLink/PSC), handling upgrades, monitoring, and provisioning while maintaining strict separation from customer data, secrets, and logs.

In **Self-managed** deployments, the customer operates their data plane independently.
Union.ai has zero access to the customer's infrastructure, with the Cloudflare Tunnel as the only connection between Union.ai and the customer's network.

For details, see [Deployment models](./architecture/deployment-models).
