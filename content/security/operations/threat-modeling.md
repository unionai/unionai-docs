---
title: Threat modeling
weight: 3
variants: -flyte +union
---

# Threat modeling

## Control plane compromise

A control plane compromise exposes orchestration metadata only. An attacker would not obtain customer data payloads, secret values, code bundles, container images, or log content. The attacker could not initiate connections to customer data planes because the tunnel is outbound-only from the customer's network. Presigned URLs are generated on the data plane, so the attacker could not generate data access URLs. See [Two-plane separation](../architecture/two-plane-separation) and [Network architecture](../architecture/network) for details on how these properties are enforced.

> [!WARNING]
> **Audit finding (ref #3, #4, #5, #7):** "A control plane compromise exposes orchestration metadata only" significantly understates the impact. A compromised control plane could: (1) intercept structured task inputs on every run submission and inputs+outputs on every retrieval (up to 10-20 MiB per request), (2) intercept secret values during create/update relay, (3) intercept all log stream content (unredacted), and (4) access TaskSpec and RunSpec blobs in the databases containing environment variables, default values, SQL statements, K8s pod specs, plugin configuration, and OAuth2 client IDs. In v2, a full TaskSpec is stored for every run. The attacker could not access binary artifacts (files, DataFrames, code bundles) since those use presigned URLs generated on the data plane, and could not access secrets via the read API (write-only design validated). The outbound-only tunnel property is correctly stated.

## Tunnel interception

The Cloudflare Tunnel uses mTLS, making man-in-the-middle attacks infeasible. Even if tunnel traffic were intercepted, data flowing through it (logs, secret creation requests) is encrypted in transit and not cached or stored at any intermediate point. The tunnel carries only orchestration traffic -- customer data payloads travel directly between clients and the customer's object store via presigned URLs, bypassing the tunnel entirely.

> [!WARNING]
> **Audit finding (ref #3):** "The tunnel carries only orchestration traffic" is incorrect -- the tunnel also carries structured task I/O (up to 10-20 MiB per request). The statement that only presigned URL data bypasses the tunnel should be qualified: binary artifacts bypass the tunnel, but structured task I/O transits through it.

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
