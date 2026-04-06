---
title: Data residency summary
weight: 16
variants: -flyte +union
---

# Data residency summary

| Data | Stored In | Accessed Via | Transits Control Plane? |
| --- | --- | --- | --- |
| Task definitions (spec metadata) | Control plane DB | ConnectRPC | Yes — metadata only |
| Run metadata (phase, timestamps) | Control plane DB | ConnectRPC | Yes |
| Action metadata (phase, attempts) | Control plane DB | ConnectRPC | Yes |
| Task inputs/outputs | Customer object store | Presigned URL | No — direct client ↔ object store |
| Code bundles | Customer object store | Presigned URL | No — direct client ↔ object store |
| Reports (HTML) | Customer object store | Presigned URL | No — direct client ↔ object store |
| Container images | Customer container registry | Pulled by K8s | No — stays in customer infra |
| Task logs | Customer log aggregator | Direct-to-DataPlane tunnel | No — served directly from data plane |
| Secrets | Customer secrets backend | Injected at runtime | Relayed during create (not stored)* |
| Observability metrics | Customer ClickHouse | Direct-to-DataPlane tunnel | No — served directly from data plane |
| User identity / RBAC | Control plane DB | ConnectRPC | Yes |
| Cluster state | Control plane DB | Internal | Yes |

> [!NOTE] Information needed
> *The zero-trust architecture eliminates all data transit through the control plane for visualization and retrieval. Whether the secret creation relay is also changing under the zero-trust model has not yet been confirmed.
