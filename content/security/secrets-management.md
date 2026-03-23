---
title: Secrets management
weight: 5
variants: -flyte +byoc +selfmanaged
---

# Secrets management

Union.ai provides enterprise-grade secrets management with a security-first design that ensures secret values never leave the customer’s infrastructure during normal operations.

## Secrets architecture

The compute plane supports four configurable secrets backends:

| Backend | Storage Location | Default? |
| --- | --- | --- |
| Kubernetes Secrets | K8s `etcd` on the customer cluster | Yes (default for self-managed) |
| AWS Secrets Manager | AWS-managed service | Optional |
| GCP Secret Manager | GCP-managed service | Optional |
| Azure Key Vault | Azure-managed service | Optional |

In all cases, secrets are stored within the customer’s infrastructure.
The choice of backend is a deployment configuration on the compute plane operator.

{{< variant byoc >}}
{{< markdown >}}
BYOC deployments default to a cloud-native secrets backend (AWS Secrets Manager, GCP Secret Manager, or Azure Key Vault) for managed integration with the provisioning workflow.
{{< /markdown >}}
{{< /variant >}}

## Secret lifecycle

### Creation

When a user creates a secret via the UI or CLI, the request is relayed through the Cloudflare tunnel to the compute plane’s secrets backend.
The secret value transits the control plane in-memory during this relay but is never written to disk or database on the control plane.

### Consumption

When a task pod is created, the Executor configures it to mount the requested secrets from the secrets backend (as environment variables or files).
The secret value is read by the compute plane’s secrets backend and injected into the pod—it never leaves the customer’s infrastructure during this process.

### Write-only API

> [!NOTE]
> Security by Design: There is no API to read back secret values. The GetSecret RPC returns only the secret’s metadata (name, scope, creation time, cluster presence status)—never the value itself. Secret values can only be consumed by task pods at runtime. This eliminates an entire class of secret exfiltration attacks.

## Secret scoping

Secrets can be scoped at multiple levels (organization, project, domain) to provide granular access control.
Only task pods running within the appropriate scope can access the corresponding secrets.
