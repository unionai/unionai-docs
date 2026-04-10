---
title: Secret lifecycle and scoping
weight: 2
variants: -flyte +union
---

# Secret lifecycle and scoping

## Creation

When a user creates a secret via the UI or CLI, the request is relayed through the Cloudflare tunnel to the data plane's secrets backend.
The secret value transits the control plane in-memory during this relay but is never written to disk or database on the control plane.

## Consumption

When a task pod is created, the Executor configures it to mount the requested secrets from the secrets backend (as environment variables or files).
The secret value is read by the data plane's secrets backend and injected into the pod -- it never leaves the customer's infrastructure during this process.

## Write-only API

> [!NOTE]
> **Security by design:** There is no API to read back secret values. The GetSecret RPC returns only the secret's metadata (name, scope, creation time, cluster presence status) -- never the value itself. Secret values can only be consumed by task pods at runtime. This eliminates an entire class of secret exfiltration attacks.

## Secret scoping

Secrets can be scoped at multiple levels (organization, project, domain) to provide granular access control.
Only task pods running within the appropriate scope can access the corresponding secrets.
