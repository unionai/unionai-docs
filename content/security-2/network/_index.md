---
title: Network security
weight: 500
variants: -flyte +union
sidebar_expanded: true
---

# Network security

Union.ai's network security is built on an **outbound-only** connectivity model. The data plane initiates all connections to the control plane — no inbound firewall rules are required on the customer's network. This eliminates an entire class of network-based attacks.

This section covers:

* [Outbound-only network architecture](./outbound-only-architecture): The design principle, security benefits, and how it differs from traditional approaches.
* [Cloudflare Tunnel](./cloudflare-tunnel): The encrypted tunnel connecting data plane to control plane, including mTLS, health checks, and regional endpoints.
* [Private connectivity (BYOC)](./private-connectivity): PrivateLink and Private Service Connect for BYOC cluster management.
* [Communication paths and protocols](./communication-paths): All communication paths, protocols, and encryption standards used across the platform.
