---
title: Security
weight: 6
variants: -flyte +union
top_menu: true
---

# Security

This section provides a comprehensive overview of Union.ai's security architecture, practices, and compliance posture for enterprise security professionals evaluating the platform.
Beyond describing the security model, it provides concrete verification steps so that reviewers can independently confirm each claim against a running system.

> **No customer data, code, or logs ever touch Union.ai's control plane. Not in flight. Not at rest. Not ever.**

## Overview

**[Architecture](./architecture/_index)**
The system is divided into a control plane hosted by Union.ai and a data plane hosted on the customer's infrastructure.
The only connection between the two planes is an outbound-only route from the data plane to the control plane that carries orchestration metadata.
Enterprise customers can further restrict the client-to-data-plane path with the [Sovereign Data Plane](./architecture/sovereign-data-plane) option.
No inbound firewall rules are required on the customer's external network perimeter under either configuration.

**[Data protection](./data-protection/_index)**
No customer data ever transits Union.ai's control plane. Workflow inputs and outputs, code bundles, secret values, logs, reports, and auxiliary UI traffic are served directly from the customer's data plane through the Direct-to-DataPlane tunnel, with authentication and RBAC enforced by an Envoy router inside the customer's cluster.
The control plane holds orchestration metadata only -- run IDs, schedules, phase transitions, task definitions, error messages, and the RBAC graph -- always encrypted at rest.

**[Identity and access](./identity-and-access/_index)**
Authentication is done via OIDC/SSO, API keys, and service accounts.
Role-based access control enforces least-privilege.
Union.ai personnel cannot access customer data or secrets.

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
Union.ai has no access to the customer's infrastructure: the only pathway between Union.ai and the customer's network is an outbound-initiated direct gRPC connection from the data plane carrying orchestration metadata.

Independently of deployment model, Enterprise customers can elect the [Sovereign Data Plane](./architecture/sovereign-data-plane) tier, under which the client-to-data-plane path runs through a customer-managed internal load balancer reachable only from the corporate VPN -- no third-party network on the path, and no Union.ai employee able to reach customer data even with full Union.ai credentials.
