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
The system is divided into a control plane hosted by Union.ai and a data plane hosted on the customer's infrastructure.
The only connections between the two planes are outbound-only routes from the customer data plane to the control plane.
Consequently, no inbound firewall rules are required on the customer's network.

**[Data protection](./data-protection/_index)**
Bulk customer data items (files, DataFrames, code bundles, container images) are stored in the customer's data plane and never enter the control plane.
Smaller inline data items (structured task inputs/outputs, secret values during creation, log streams) pass through the control plane memory only transiently. They are not persisted there.
The control plane does persist orchestration and task metadata, but these are always encrypted at rest.

**[Identity and access](./identity-and-access/_index)**
Authentication is done via OIDC/SSO, API keys, and service accounts.
Role-based access control enforces least-privilege.
Union.ai personnel cannot access customer data or secrets.

**[Threat model](./threat-model)**
An analysis of potential threats and how they are mitigated is provided.
Control plane compromise, tunnel interception, and presigned URL leakage scenarios are examined,
and the architectural design and security controls that mitigate these risks are described.
The goal is to demonstrate that even in worst-case scenarios, customer data remains protected.

**[Compliance and governance](./compliance/_index)**
Union.ai is SOC 2 Type II certified for Security, Availability, and Processing Integrity, with practices aligned to ISO 27001 and CIS benchmarks.
The platform is designed to meet HIPAA requirements.
Details are available in the Public Trust Center at [trust.union.ai](https://trust.union.ai).
This includes organizational security practices, vulnerability management, and a shared responsibility model.

## Deployment models

Union.ai offers two deployment models, both sharing the same control plane / data plane architecture and security controls described in this section.

In **BYOC** deployments, Union.ai manages the data plane in the customer's cloud account via private connectivity (PrivateLink/PSC).
Union.ai handles upgrades, monitoring, and provisioning, while maintaining strict separation from customer data, secrets, and logs.

In **Self-managed** deployments, the customer operates their data plane independently.
The customer is responsible for all aspects of data plane management, including upgrades, monitoring, and provisioning.
Union.ai has no access to the customer's infrastructure, with the Cloudflare Tunnel and GRPC connections being the only pathways between Union.ai and the customer's network
(and even then, only outbound from the customer to Union.ai).

For details, see [Deployment models](./architecture/deployment-models).
