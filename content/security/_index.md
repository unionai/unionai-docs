---
title: Security
weight: 8
variants: -flyte +byoc +selfmanaged
top_menu: true
sidebar_expanded: true
---

# Security

Union.ai provides a production-grade workflow orchestration platform built on Flyte, designed for AI/ML and data-intensive workloads.
Security is foundational to Union.ai’s architecture, not an afterthought.
This document provides a comprehensive overview of Union.ai’s security practices, architecture, and compliance posture for enterprise security professionals evaluating the platform.

Union.ai’s security model is built on several core principles:

* **Data residency:** Customer data is stored and computed only within the customer's compute plane. The Union.ai control plane stores only orchestration metadata—no task inputs, outputs, code, logs, secrets, or container images.
* **Architectural isolation:** A strict separation between the Union-hosted control plane and the customer-hosted compute plane ensures that the blast radius of any control plane compromise does not extend to customer data.
* **Outbound only connectivity:** The Cloudflare Tunnel connecting the control plane to the compute plane is outbound-only from the customer’s network, requiring no inbound firewall rules. All communication uses mutual TLS (mTLS) and is authenticated using the customer's Auth / SSO.
* **Compliance:** Union.ai is SOC 2 Type II certified for Security, Availability, and Integrity, with practices aligned to ISO 27001 and GDPR standards. Union is certified HIPAA-compliant and maintains CIS 1.4 AWS and CIS 3.0 certifications. The Union.ai trust portal can be found at [trust.union.ai](https://trust.union.ai)
* **Defense in depth:** Multiple layers of encryption, authentication, authorization, and network segmentation protect data throughout its lifecycle.
* **Human / operational isolation:** Your data is protected by least privileged access, comprehensive auditing, and detailed logging. Union AI personnel cannot view it without customer authorization.

> [!NOTE]
> In Union.ai’s BYOC architecture, all customer data—including task inputs/outputs, code bundles, container images, logs, secrets, and observability metrics—resides exclusively in the customer’s own cloud infrastructure.
