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

* **Data residency:** Customer data is stored and computed only within the customer's data plane. The Union.ai control plane stores only orchestration metadata—no task inputs, outputs, code, logs, secrets, or container images.
* **Architectural isolation:** A strict separation between the Union-hosted control plane and the customer-hosted data plane ensures that the blast radius of any control plane compromise does not extend to customer data.
* **Outbound only connectivity:** The Cloudflare Tunnel connecting the control plane to the data plane is outbound-only from the customer’s network, requiring no inbound firewall rules. All communication uses mutual TLS (mTLS) and is authenticated using the customer's Auth / SSO.
* **Compliance:** Union.ai is SOC 2 Type II certified for Security, Availability, and Integrity, with practices aligned to ISO 27001 and GDPR standards. Union is designed to meet HIPAA compliance requirements for handling Protected Health Information (PHI) and maintains CIS 1.4 AWS certification while pursuing CIS 3.0 certification (in progress). The Union.ai trust portal can be found at [trust.union.ai](https://trust.union.ai)
* **Defense in depth:** Multiple layers of encryption, authentication, authorization, and network segmentation protect data throughout its lifecycle.
* **Human / operational isolation:** Union.ai personnel access the customer's control plane UI only through authenticated, RBAC-controlled channels. Personnel do not have IAM credentials for customer cloud accounts and cannot directly access customer data stores, secrets, or compute infrastructure. In BYOC deployments, Union.ai additionally has [K8s cluster management access](./byoc-differences#human-access-to-customer-environments).

## Deployment models

Union.ai offers two deployment models, both sharing the same control plane / data plane architecture and security controls described in this document.

In **Self-Managed** deployments, the customer operates their data plane independently; Union.ai has zero access to the customer’s infrastructure, with the Cloudflare tunnel as the only connection.

In **BYOC** deployments, Union.ai manages the Kubernetes cluster in the customer’s cloud account via private connectivity (PrivateLink/PSC), handling upgrades, monitoring, and provisioning while maintaining strict separation from customer data, secrets, and logs.

The core security architecture—encryption, RBAC, tenant isolation, presigned URL data access, and audit logging—is identical across both models. Sections where operational responsibilities differ are noted inline. [BYOC deployment differences](./byoc-differences) provides a detailed comparison.
