---
title: Security
weight: 6
variants: -flyte +union
top_menu: true
sidebar_expanded: true
---

# Security

Union.ai provides a production-grade workflow orchestration platform built on Flyte, designed for AI/ML and data-intensive workloads.
Security is foundational to Union.ai's architecture, not an afterthought.
Union.ai's zero-trust architecture ensures that no customer data ever transits the control plane: all data visualization, logs, and metrics are served directly from the customer's data plane.
This document provides a comprehensive overview of Union.ai's security practices, architecture, and compliance posture for enterprise security professionals evaluating the platform.

Union.ai's security model is built on several core principles:

* **Zero-trust data isolation:** No customer data, operational metadata, or logs ever transit through Union.ai's control plane. All data visualization---including logs, task inputs and outputs, metrics, and dashboards---is served directly from the customer's data plane via the Direct-to-DataPlane tunnel. The `dataproxy` service runs entirely within the data plane, ensuring that data requests are fulfilled without leaving the customer's VPC. This zero-trust data isolation guarantee is contractual.
* **Data residency:** Customer data is stored and computed only within the customer's data plane. The Union.ai control plane never sees or relays customer data. It stores only orchestration metadata---task definitions, run identifiers, phase timestamps, and typed interface references---and holds no task inputs, outputs, code, logs, secrets, or container images.
* **Architectural isolation:** A strict separation between the Union-hosted control plane and the customer-hosted data plane ensures that the blast radius of any control plane compromise does not extend to customer data. The zero-trust model further reduces this blast radius: because no customer data flows through the control plane at any point, a control plane compromise exposes only orchestration metadata, never customer data.
* **Outbound-only connectivity:** The Cloudflare Tunnel connecting the control plane to the data plane is outbound-only from the customer's network, requiring no inbound firewall rules. All communication uses mutual TLS (mTLS) and is authenticated using the customer's Auth / SSO.
* **Compliance:** Union.ai is SOC 2 Type II certified for Security, Availability, and Integrity, with practices aligned to ISO 27001 and GDPR standards. Union is designed to meet HIPAA compliance requirements for handling Protected Health Information (PHI) and maintains CIS 1.4 AWS certification while pursuing CIS 3.0 certification (in progress). The Union.ai trust portal can be found at [trust.union.ai](https://trust.union.ai).
* **Defense in depth:** Multiple layers of encryption, authentication, authorization, and network segmentation protect data throughout its lifecycle.
* **Human / operational isolation:** In the default deployment, Union.ai personnel cannot see customer data even through the Union UI, because all data is served directly from the data plane via the Direct-to-DataPlane tunnel. Personnel do not have IAM credentials for customer cloud accounts and cannot directly access customer data stores, secrets, or compute infrastructure. In the Enterprise 1 security tier, data plane access is further restricted to VPN-connected users only, eliminating any external access path. In BYOC deployments, Union.ai additionally has [K8s cluster management access](./byoc-differences#human-access-to-customer-environments).

## Deployment models

Union.ai's deployment model has two independent dimensions: a **security tier** that determines data access controls, and an **operational model** that determines who manages the data plane infrastructure.

### Security tiers

Union.ai offers two security tiers that control how data flows between the data plane and end users:

* **Default** (all plans): All data visualization is served directly from the customer's data plane via the Direct-to-DataPlane tunnel. No customer data transits the control plane. The `dataproxy` service runs within the data plane, handling presigned URL generation and data streaming entirely within the customer's VPC.
* **Enterprise 1** (VPN-restricted): In addition to all Default tier guarantees, data plane access is restricted to users connected through the customer's VPN. The customer manages their own load balancer, and no Union.ai employee has access to the data plane. This tier is designed for organizations with the strictest data access requirements.

> [!NOTE] Information needed
> A dedicated deployment models page with detailed comparison of security tiers is planned. Link will be added here when available.

### Operational models

Independently of the security tier, customers choose how their data plane infrastructure is managed:

* **Self-Managed:** The customer operates their data plane independently. Union.ai has zero access to the customer's infrastructure, with the Cloudflare tunnel as the only connection between the control plane and data plane.
* **BYOC (Bring Your Own Cloud):** Union.ai manages the Kubernetes cluster in the customer's cloud account via private connectivity (PrivateLink/PSC), handling upgrades, monitoring, and provisioning while maintaining strict separation from customer data, secrets, and logs.

The core security architecture---encryption, RBAC, tenant isolation, presigned URL data access, and audit logging---is identical across both operational models and both security tiers. Sections where operational responsibilities differ are noted inline. [BYOC deployment differences](./byoc-differences) provides a detailed comparison of the operational models.
