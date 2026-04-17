---
title: Security
weight: 6
variants: -flyte +union
top_menu: true
sidebar_expanded: true
---

# Security

This section provides a comprehensive overview of Union.ai's security architecture, practices, and compliance posture for enterprise security professionals evaluating the platform. Beyond describing the security model, it provides concrete verification steps so that reviewers can independently confirm each claim against a running system.

## Core principles

Union.ai's security model is built on several core principles:

**Architectural isolation.** The system is divided into two parts: the control plane, which runs on Union.ai's infrastructure, and the data plane, which runs on the customer's infrastructure. The control plane stores only orchestration metadata. Customer data -- task inputs, outputs, code, logs, secrets, and container images -- never leaves the customer's cloud account.

**Outbound-only connectivity.** The connection between the data plane and the control plane is a Cloudflare Tunnel initiated outbound from the customer's network. No inbound firewall rules are required.

**Defense in depth.** Multiple layers of encryption, authentication, authorization, and network segmentation protect data throughout its lifecycle.

**Operational isolation.** In self-managed deployments, the customer has sole control of their data plane and Union.ai has no access to it. In BYOC deployments, Union.ai manages the customer's Kubernetes cluster but still cannot access customer data, secrets, or logs.

**Compliance.** Union.ai is SOC 2 Type II certified for Security, Availability, and Processing Integrity, with practices aligned to ISO 27001 and CIS benchmarks. Union.ai is designed to meet HIPAA compliance requirements and maintains a public Trust Center at [trust.union.ai](https://trust.union.ai).

## Deployment models

Union.ai offers two deployment models, both sharing the same control plane / data plane architecture and security controls described in this section.

In **self-managed** deployments, the customer operates their data plane independently. Union.ai has zero access to the customer's infrastructure, with the Cloudflare Tunnel as the only connection between Union.ai and the customer's network.

In **BYOC** deployments, Union.ai manages the Kubernetes cluster in the customer's cloud account via private connectivity (PrivateLink/PSC), handling upgrades, monitoring, and provisioning while maintaining strict separation from customer data, secrets, and logs.

For details, see [Deployment models](./architecture/deployment-models).

## Documentation overview

* **[Architecture](./architecture/):** Control plane / data plane separation, network architecture, deployment model differences.
* **[Data](./data/):** Data classification and residency, data flow patterns, encryption, secrets management.
* **[Access control](./access/):** Authentication, RBAC, tenant isolation, human access controls.
* **[Compliance](./compliance/):** Certifications, HIPAA, GDPR, standards compliance, shared responsibility model.
* **[Operations](./operations/):** Logging, audit trails, vulnerability management, threat modeling, organizational security.
