---
title: Threat model
weight: 4
variants: -flyte +union
---

# Threat model

This page enumerates the principal threat scenarios considered in Union.ai's security architecture, with pointers to the canonical pages where each scenario's controls and verification live.

## Control plane compromise

Under Zero Trust, a compromised control plane would expose orchestration metadata only: task definitions, run IDs, schedules, phase transitions, error messages, and the RBAC graph. It would not expose customer data of any kind -- workflow inputs and outputs, code bundles, log streams, secrets, and auxiliary UI traffic are all served directly from the data plane through the Direct-to-DataPlane tunnel and never enter the control plane in any form. The architectural properties that limit this blast radius are described in [Two-plane separation](./architecture/two-plane-separation#blast-radius), and the full classification of what does and does not reside in the control plane is in [Data classification and residency](./data-protection/classification-and-residency).

## Cross-plane network interception

Cross-plane traffic uses two outbound-only encrypted channels: the Direct-to-DataPlane tunnel (TLS 1.3 + mTLS + Cloudflare Access tokens) for client-to-data-plane requests, and a direct gRPC connection (TLS 1.2+) for orchestration metadata. All payloads are encrypted in transit, and no intermediate caching or storage occurs on either channel. See [Network architecture](./architecture/network) for the channel design and [Encryption](./data-protection/encryption) for the per-data-type encryption matrix.

## Presigned URL leakage

A leaked presigned URL exposes a single object for the duration of its TTL (1 hour by default, configurable shorter) and is locked to a single operation (GET or PUT). It cannot enumerate other objects or be replayed beyond its scope. The full enumeration of presigned URL controls is in [Data flow](./data-protection/data-flow#presigned-url-pattern). Customer-managed encryption keys provide an additional kill-switch -- see [Customer-managed key authority](./data-protection/encryption#customer-managed-key-authority).

## Secret exfiltration

The secrets API is write-only by design: there is no API endpoint that returns a secret value, regardless of the caller's privileges. Compromising the control plane API or a privileged user account does not yield secret values. See [Secrets management](./data-protection/secrets) for the lifecycle and write-only design.

## Cross-tenant data access

Tenant isolation is enforced at multiple layers: org-scoped primary keys in the control plane databases, service-layer query gating before any data access, and physically separate data planes in different cloud accounts. See [Tenant isolation](./identity-and-access/tenant-isolation).
