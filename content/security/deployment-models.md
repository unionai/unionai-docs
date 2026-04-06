---
title: Deployment models and security tiers
weight: 13
variants: -flyte +union
---

# Deployment models and security tiers

## Overview

Union.ai deployments have two independent dimensions:

* **Security tier** determines how data is accessed and who can see it.
* **Operational model** determines who manages the data plane infrastructure.

These dimensions are orthogonal: any security tier can be combined with any operational model.
This page describes the security tiers in detail.
For operational model differences, see [BYOC deployment differences](./byoc-differences).

## Security tiers

Union.ai offers two security tiers that control how data flows between the data plane and end users.
Both tiers enforce the same zero-trust guarantee: no customer data, metadata, or logs ever transit through the Union.ai control plane.
The tiers differ in how clients connect to the data plane and who can access data through the UI.

### Default

The Default tier uses the Direct-to-DataPlane tunnel via Cloudflare to serve all data directly from the customer's VPC.
This is the standard configuration for all Union.ai plans (Starter, Team, and Enterprise).

Key characteristics:

* All data visualization, logs, metrics, and task inputs/outputs are served from the data plane via the Cloudflare tunnel.
* No customer data transits the control plane. This is a contractual guarantee.
* The `dataproxy` service runs entirely within the customer's VPC, handling presigned URL generation and data streaming.
* An Envoy router within the data plane handles authentication and RBAC enforcement.
* No additional infrastructure is required from the customer beyond the standard data plane setup.

### Enterprise 1: Enhanced security

The Enterprise 1 tier adds VPN-restricted access on top of all Default tier guarantees.
The customer's SRE/DevOps team provisions a load balancer within their VPC that is routable only from within their corporate VPN.
This ensures that only VPN-connected users in the customer's organization can access data plane endpoints.

Key characteristics:

* No Union.ai employee can ever see customer data, because data plane access requires VPN connectivity.
* Union.ai RBAC and SSO continue to work as in the Default tier.
* Recommended for organizations with the strictest data access requirements and for high-scale model serving within their cloud.
* Available on Enterprise plans only.

> [!NOTE] Information needed
> The exact load balancer configuration requirements, supported types, and DNS setup steps are not yet documented.

> [!NOTE] Information needed
> "Enterprise 1" is an internal codename. The final product name for this tier has not been confirmed.

## Comparison matrix

| Feature | Default | Enterprise 1 |
| --- | --- | --- |
| Data transit through control plane | No | No |
| Who can see data in UI | Authenticated users via SSO | VPN-connected users only |
| Union employee data visibility | No -- data served from data plane | No -- VPN restricts all access |
| Network requirements | Cloudflare egress | Customer-managed LB + VPN |
| Available plans | All (Starter, Team, Enterprise) | Enterprise only |
| Configuration complexity | None -- default setup | Customer provisions LB |

## Operational models

The operational model is an independent dimension from the security tier.
It determines who manages the data plane infrastructure:

* **BYOC (Bring Your Own Cloud):** Union.ai manages the Kubernetes cluster in the customer's cloud account via private connectivity (PrivateLink/PSC). Union.ai handles upgrades, monitoring, and provisioning while maintaining strict separation from customer data, secrets, and logs.
* **Self-Managed:** The customer operates their data plane independently. Union.ai has zero access to the customer's infrastructure, with the Cloudflare tunnel as the only connection between the control plane and data plane.

Both operational models work with either security tier.
The core security architecture -- encryption, RBAC, tenant isolation, presigned URL data access, and audit logging -- is identical across all combinations.

For a detailed comparison of operational models, see [BYOC deployment differences](./byoc-differences).
