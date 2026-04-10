---
title: Communication paths and protocols
weight: 4
variants: -flyte +union
---

# Communication paths and protocols

This page provides a complete reference of all communication paths in the Union.ai platform, their protocols, and encryption standards.

## Standard communication paths (all deployments)

| Communication Path | Protocol | Encryption |
| --- | --- | --- |
| Client -> Control Plane | ConnectRPC (gRPC-Web) over HTTPS | TLS 1.2+ |
| Control Plane <-> Data Plane | Cloudflare Tunnel (outbound-initiated) | mTLS |
| Client -> Object Store (presigned URL) | HTTPS | TLS 1.2+ (cloud provider enforced) |
| Fluent Bit -> Log Aggregator | Cloud provider SDK | TLS (cloud-native) |
| Task Pods -> Object Store | Cloud provider SDK | TLS (cloud-native) |

## Additional BYOC communication path

BYOC deployments add a private management path:

| Communication Path | Protocol | Encryption |
| --- | --- | --- |
| Union.ai -> Customer K8s API | PrivateLink / PSC | TLS (private connectivity) |

This path is used exclusively for cluster management operations and does not carry customer data. See [Private connectivity (BYOC)](./private-connectivity).

## Encryption summary

No unencrypted communication paths exist in the platform architecture:

* All client-to-control-plane communication uses **TLS 1.2 or higher**
* All control-plane-to-data-plane communication uses **mutual TLS** via Cloudflare Tunnel
* All client-to-object-store communication (via presigned URLs) uses **HTTPS**, enforced by cloud providers
* All internal data plane communication uses **cloud-native TLS**
* The BYOC management path uses **TLS over private connectivity** (PrivateLink/PSC)
