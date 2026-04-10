---
title: Network architecture overview
weight: 2
variants: -flyte +union
---

# Network architecture overview

Network security is enforced through multiple layers:

![Network security](../../_static/images/security/network-security.png)

> [!NOTE]
> In BYOC deployments, Union.ai additionally maintains a private management connection to the customer's K8s cluster. See [Private connectivity (BYOC)](../network/private-connectivity) for details.

## Cloudflare Tunnel (outbound-only)

The data plane connects to the control plane via a Cloudflare Tunnel -- an outbound-only encrypted connection initiated from the customer's cluster.
This architecture provides several critical security benefits:

* No inbound firewall rules are required on the customer's network
* All traffic through the tunnel uses mutual TLS (mTLS) encryption
* The Tunnel Service performs periodic health checks and state reconciliation
* Connection is initiated outward to Cloudflare's edge network, from the data plane, which then connects to the control plane

For detailed Cloudflare Tunnel specifications, see [Cloudflare Tunnel](../network/cloudflare-tunnel).

## Communication paths

| Communication Path | Protocol | Encryption |
| --- | --- | --- |
| Client -> Control Plane | ConnectRPC (gRPC-Web) over HTTPS | TLS 1.2+ |
| Control Plane <-> Data Plane | Cloudflare Tunnel (outbound-initiated) | mTLS |
| Client -> Object Store (presigned URL) | HTTPS | TLS 1.2+ (cloud provider enforced) |
| Fluent Bit -> Log Aggregator | Cloud provider SDK | TLS (cloud-native) |
| Task Pods -> Object Store | Cloud provider SDK | TLS (cloud-native) |

> [!NOTE]
> BYOC deployments add a PrivateLink/PSC management path between Union.ai and the customer's K8s API. See [Private connectivity (BYOC)](../network/private-connectivity).

For the complete communication paths reference, see [Communication paths and protocols](../network/communication-paths).
