---
title: Threat modeling
weight: 3
variants: -flyte +union
---

## Control plane compromise

A control plane compromise exposes orchestration metadata only. An attacker would not obtain customer data payloads, secret values, code bundles, container images, or log content. The attacker could not initiate connections to customer data planes because the tunnel is outbound-only from the customer's network. Presigned URLs are generated on the data plane, so the attacker could not generate data access URLs. See [Two-plane separation](../architecture/two-plane-separation) and [Network architecture](../architecture/network) for details on how these properties are enforced.

## Tunnel interception

The Cloudflare Tunnel uses mTLS, making man-in-the-middle attacks infeasible. Even if tunnel traffic were intercepted, data flowing through it (logs, secret creation requests) is encrypted in transit and not cached or stored at any intermediate point. The tunnel carries only orchestration traffic -- customer data payloads travel directly between clients and the customer's object store via presigned URLs, bypassing the tunnel entirely.

## Presigned URL leakage

A leaked presigned URL exposes a single object for a maximum of one hour (default). The URL grants only the specific operation requested (GET or PUT) and cannot enumerate or access other objects. Organizations can configure shorter expiration times. Because presigned URLs are bearer tokens, Union.ai recommends treating them with the same care as short-lived credentials and configuring the shortest practical TTL.

## Verification

### Threat scenarios (High)

**Reviewer focus:** Confirm that the impact of each threat scenario is limited by the architectural properties described above.

**How to verify:**

These scenarios are validated by demonstrations from other sections:

- **Control plane compromise:** The data classification and workflow data flow verifications in [Two-plane separation](../architecture/two-plane-separation) prove that the control plane holds no customer data.
- **Presigned URL leakage:** The presigned URL verification in [Data plane](../architecture/data-plane) proves TTL and scope limits.
- **Tunnel interception:** The network architecture verifications in [Network architecture](../architecture/network) prove encryption.

No additional demonstrations are needed beyond those already identified in the referenced sections.
