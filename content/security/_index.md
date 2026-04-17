---
title: Security (re-org)
weight: 6
variants: -flyte +union
top_menu: true
sidebar_expanded: true
---

# Security

This section provides a comprehensive overview of Union.ai's security architecture, practices, and compliance posture for enterprise security professionals evaluating the platform.

This includes not just a discussion of the security model itself, but also details on how to audit a running system to demonstrate that the claims made here are accurate.

## Core principles

Union.ai's security model is built on several core principles:

* **Architectural isolation:** The system is divided into two parts: the control plane, which runs on Union.ai's infrastructure, and the data plane, which runs on customer's infrastructure.

* **Data residency:** Customer data is stored and processed only within the customer's data plane. The Union.ai control plane stores only orchestration metadata. No task inputs, outputs, code, logs, secrets, or container images are ever stored in the control plane.

* **Outbound-only connectivity:** The connecting between the data plane and the control plane (a Cloudflare tunnel) is outbound-only from the customer's network, requiring no inbound firewall rules.

* **Defense in depth:** Multiple layers of encryption, authentication, authorization, and network segmentation protect data throughout its lifecycle.

* **Compliance:** Union.ai is SOC 2 Type II certified for Security, Availability, and Integrity, with practices aligned to ISO 27001 and GDPR standards. Union is designed to meet HIPAA compliance requirements for handling Protected Health Information (PHI) and maintains CIS 1.4 AWS certification while pursuing CIS 3.0 certification (in progress). The Union.ai trust portal can be found at [trust.union.ai](https://trust.union.ai).

* **Operational isolation:** In Self-managed deployments, the customer has sole control of, and management responsibility for, their data plane. Union.ai has no access to it. In BYOC deployments, Union.ai manages the customer's data plane for you on the customer's infrastructure. In these cases Union.ai has access, but only that required to perform the requiredmanagement functions. See [Kubernetess cluster management access](./architecture/deployment-models#human-access-to-customer-environments).

## Deployment models

Union.ai offers two deployment models, both sharing the same control plane / data plane architecture and security controls described in this section.

In **Self-Managed** deployments, the customer operates their data plane independently. Union.ai has zero access to the customer's infrastructure, with the Cloudflare tunnel as the only connection between Union.ai and the customer's network.

In **BYOC** deployments, Union.ai manages the Kubernetes cluster in the customer's cloud account via private connectivity (PrivateLink/PSC), handling upgrades, monitoring, and provisioning while maintaining strict separation from customer data, secrets, and logs.

For details on the differences between these models, see [Deployment models and BYOC differences](./architecture/deployment-models).

## Security documentation

This security documentation is organized into the following sections:

* **[Security architecture](./architecture/):** Control plane / data plane separation, network architecture, data flow patterns, component architecture, and deployment model differences.
* **[Authentication and access control](./auth/):** Authentication methods, SSO, role-based access control, organization isolation, and human access controls.
* **[Network security](./network/):** Outbound-only architecture, Cloudflare Tunnel, private connectivity for BYOC, and communication paths.
* **[Data protection and encryption](./keys/):** Encryption at rest and in transit, data classification, and data residency guarantees.
* **[Secrets management](./secrets/):** Secrets backends, secret lifecycle, write-only API, and scoping.
* **[Compliance and governance](./compliance/):** Certifications (SOC 2, HIPAA, GDPR), standards compliance, shared responsibility model, and the Trust Center.
* **[Operational security](./operations/):** Logging, monitoring, audit trails, vulnerability management, organizational security practices, and workflow execution security.
* **[Security reference](./reference/):** Detailed Kubernetes RBAC specifications, AWS IAM role mappings, and multi-cloud support details.