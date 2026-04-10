---
title: Network architecture overview
weight: 2
variants: -flyte +union
---

# Network architecture overview

Network security is enforced through multiple layers:

![Network security](../../_static/images/security/network-security.png)

> [!NOTE]
> In BYOC deployments, Union.ai additionally maintains a private management connection to the customer's K8s cluster. See [Private connectivity (BYOC)](../network/private-connectivity).

## Cloudflare Tunnel (outbound-only)

The data plane connects to the control plane via a Cloudflare Tunnel -- an outbound-only encrypted connection initiated from the customer's cluster:

* No inbound firewall rules required on the customer's network
* All traffic uses mutual TLS (mTLS) encryption
* The Tunnel Service performs periodic health checks and state reconciliation
* The data plane initiates the connection outbound to Cloudflare's edge, which then connects to the control plane

For detailed specifications, see [Cloudflare Tunnel](../network/cloudflare-tunnel).

## Communication paths

For the complete reference of all communication paths, protocols, and encryption standards, see [Communication paths and protocols](../network/communication-paths).
