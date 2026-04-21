---
title: Threat modeling
weight: 3
variants: -flyte +union
---

# Threat modeling

## Control plane compromise

A control plane compromise would expose: orchestration metadata and task definitions stored in the databases (including potentially sensitive fields such as environment variables, default input values, SQL statements, and K8s pod specs), structured task I/O transiting memory during active requests (up to 10-20 MiB per request), secret values being relayed during create/update operations, unredacted log stream content, and error messages. The attacker could not access bulk customer data (files, DataFrames, code bundles, container images) since those are stored in the customer's infrastructure and accessed via presigned URLs generated on the data plane. The attacker could not retrieve secret values via the API (write-only design). The attacker could not initiate connections to customer data planes because the tunnel is outbound-only from the customer's network. See [Two-plane separation](../architecture/two-plane-separation) and [Network architecture](../architecture/network) for details.

## Tunnel interception

The Cloudflare Tunnel uses layered encryption (TLS + mTLS + Cloudflare Access tokens), making man-in-the-middle attacks infeasible. Even if tunnel traffic were intercepted, all data is encrypted in transit and not cached or stored at any intermediate point. The tunnel carries orchestration traffic, structured task I/O (up to 10-20 MiB per request), secret values during creation, and log streams. Bulk customer data (files, DataFrames, code bundles) travels directly between clients and the customer's object store via presigned URLs, bypassing the tunnel entirely.

## Presigned URL leakage

A leaked presigned URL exposes a single object for a maximum of one hour (default). The URL grants only the specific operation requested (GET or PUT) and cannot enumerate or access other objects. Organizations can configure shorter expiration times. Because presigned URLs are bearer tokens, Union.ai recommends treating them with the same care as short-lived credentials and configuring the shortest practical TTL.

## Verification

### Threat scenarios

**Reviewer focus:** Confirm that the impact of each threat scenario is limited by the architectural properties described above.

**How to verify:**

These scenarios are validated by demonstrations from other sections:

- **Control plane compromise:** The data classification and workflow data flow verifications in [Two-plane separation](../architecture/two-plane-separation) demonstrate the blast radius limits described above -- bulk data is inaccessible, inline data is transient, and task definitions are enumerated.
- **Presigned URL leakage:** The presigned URL verification in [Data plane](../architecture/data-plane) proves TTL and scope limits.
- **Tunnel interception:** The network architecture verifications in [Network architecture](../architecture/network) prove encryption.

No additional demonstrations are needed beyond those already identified in the referenced sections.
