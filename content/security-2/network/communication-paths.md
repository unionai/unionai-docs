---
title: Communication paths and protocols
weight: 4
variants: -flyte +union
---

# Communication paths and protocols

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

This path is used exclusively for cluster management and does not carry customer data. See [Private connectivity (BYOC)](./private-connectivity).

## Encryption summary

No unencrypted communication paths exist. All connections use TLS 1.2+ or mTLS.
