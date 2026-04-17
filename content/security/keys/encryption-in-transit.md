---
title: Encryption in transit
weight: 2
variants: -flyte +union
---

# Encryption in transit

Union.ai enforces encryption for all data in transit.
No unencrypted communication paths exist in the platform architecture.

- All client-to-control-plane communication uses TLS 1.2 or higher.
- All control-plane-to-data-plane communication uses mutual TLS via Cloudflare Tunnel.
- All client-to-object-store communication (via presigned URLs) uses HTTPS, enforced by cloud providers.
- All internal data plane communication uses cloud-native TLS.

For a complete list of all communication paths and their encryption standards, see [Communication paths and protocols](../network/communication-paths).
