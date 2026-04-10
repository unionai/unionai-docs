---
title: Cloudflare Tunnel
weight: 2
variants: -flyte +union
---

# Cloudflare Tunnel

The data plane connects to the control plane via a Cloudflare Tunnel -- an outbound-only encrypted connection initiated from the customer's cluster.

## How it works

The Tunnel Service on the data plane initiates and maintains an outbound-only encrypted connection to Cloudflare's edge network, which then connects to the Union.ai control plane. This architecture provides:

* **Outbound-only connection** -- no inbound firewall rules required on the customer's network
* **Mutual TLS (mTLS) encryption** -- all traffic through the tunnel is encrypted and both ends are authenticated
* **Periodic health checks and heartbeats** -- the Tunnel Service monitors connection health
* **Automatic reconnection** -- connection is restored automatically in case of network disruption
* **State reconciliation** -- the Cluster Service on the control plane performs periodic reconciliation to ensure tunnel health and DNS records are current

## Regional endpoints

Union.ai operates regional control plane endpoints:

| Area | Region | Endpoint |
| --- | --- | --- |
| US | us-east-2 | hosted.unionai.cloud |
| US | us-west-2 | us-west-2.unionai.cloud |
| Europe | eu-west-1 | eu-west-1.unionai.cloud |
| Europe | eu-west-2 | eu-west-2.unionai.cloud |
| Europe | eu-central-1 | eu-central-1.unionai.cloud |

## Egress CIDR configuration

In locked-down environments, networking teams can limit egress access to published Cloudflare CIDR blocks, and further restrict to specific regions in coordination with the Union networking team.

## What flows through the tunnel

The Cloudflare Tunnel carries all cross-plane communication:

* **Orchestration instructions** -- TaskAction custom resources from Queue Service to Executor
* **State transitions** -- phase changes from Executor back to State Service
* **Log streams** -- relayed in-memory from Log Provider through DataProxy (never persisted)
* **Presigned URL signing requests** -- proxied from control plane to Object Store Service
* **Health checks** -- from Cluster Service to Tunnel Service
* **Secret creation requests** -- relayed in-memory during secret creation (values never persisted)

Customer data payloads (task inputs/outputs, code bundles, reports) do **not** flow through the tunnel -- they are accessed directly via presigned URLs between the client and the customer's object store.
