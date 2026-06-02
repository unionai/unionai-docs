---
title: Secrets management
weight: 4
variants: -flyte +union
---

# Secrets management

Union.ai's secrets management system stores secret values exclusively within the customer's infrastructure and exposes them through a write-only API: there is no endpoint that returns a secret value. The `GetSecret` RPC returns only metadata (name, scope, creation time, cluster presence status); Get, List, and Delete operations never expose the value. Secret writes go directly to the data plane through the Direct-to-DataPlane tunnel, so secret values never transit the control plane. Compromising a user account or the control plane API yields no path to read secret values back.

## Backends

| Backend | Storage Location | Default |
|---|---|---|
| Kubernetes Secrets | K8s etcd on customer cluster | Self-managed default |
| AWS Secrets Manager | AWS-managed service | BYOC default (AWS) |
| GCP Secret Manager | GCP-managed service | BYOC default (GCP) |
| Azure Key Vault | Azure-managed service | BYOC default (Azure) |

All four backends are available regardless of deployment model. The choice of backend is a deployment configuration on the data plane operator. Each backend integrates with its cloud provider's native encryption and access control mechanisms.

## Secret lifecycle

**Creation:** When a user creates a secret via the UI or CLI, the value is sent directly to the data plane's secrets backend through the Direct-to-DataPlane tunnel and stored encrypted at rest in the customer's secret manager (AWS Secrets Manager, GCP Secret Manager, Azure Key Vault, or K8s Secrets). The value never enters Union.ai's control plane in any form. The tunnel's Envoy router authenticates the request against Union identity and enforces RBAC before the value reaches the secrets backend.

| Phase | Encrypted? | Details |
|-------|------------|---------|
| Client → Cloudflare edge | **Yes** | TLS 1.3 (default tier only) |
| Cloudflare edge → Data Plane (tunnel) | **Yes** | mTLS + Cloudflare Tunnel (default tier only) |
| Client → Internal load balancer | **Yes** | TLS, customer-managed certificate ([Sovereign Data Plane](../architecture/sovereign-data-plane) tier only) |
| At Envoy router (data plane) | **Plaintext in memory** | AuthN + RBAC check; not persisted, cached, or logged |
| In Data Plane (operator) | **Plaintext in memory** | Briefly held before writing to secret backend |
| At rest (secret backend) | **Yes** | AWS Secrets Manager (AES-256/KMS), GCP Secret Manager (Google-managed or CMEK), Azure Key Vault (HSM-backed), or K8s etcd encryption |

**Consumption:** When a task pod is created, the Executor configures it to mount the requested secrets from the backend as environment variables or files. The value is read by the data plane's secrets backend and injected into the pod. It never leaves the customer's infrastructure during this process. The control plane is not involved in secret consumption at runtime.

**Scoping:** Secrets can be scoped at organization, project, or domain level. Only task pods running within the appropriate scope can access the corresponding secrets. This ensures that teams working in different projects cannot access each other's secrets, even within the same data plane cluster.

For details on how secrets flow during workflow execution, see [Data flow](./data-flow).

## Verification

### Write-only API

**Reviewer focus:** Confirm that no API endpoint returns secret values and that the write-only design holds.

**How to verify:**

1. Create a test secret:

   ```bash
   uctl create secret --name test-secret --value "s3cr3t-value" --project myproject
   ```

2. Attempt to read it back:

   ```bash
   uctl get secret --name test-secret --project myproject
   ```

   The output should show name, scope, creation time, and cluster status. There should be **no value field** in the response.

3. Try every API endpoint that touches secrets. None should return the value.

4. Check the protobuf definition in the open-source Flyte repository. `GetSecretResponse` has no value field. The write-only design is enforced at the protocol level.

5. Verify the secret exists in the customer's secrets backend by checking the cloud secrets manager console directly. The value should be present there.

This verification is fully self-service and works immediately. Note that the write-only design is enforced at the protocol level: Union.ai's API structurally cannot return secret values, regardless of the caller's privilege level.

### Secret lifecycle

**Reviewer focus:** Confirm that secret values are written directly to the data plane backend through the Direct-to-DataPlane tunnel without traversing the control plane, and are consumed entirely within the data plane at runtime.

**How to verify:**

- **Creation path:** Inspect Cloudflare Access logs for the tunnel during a secret create operation. Each request should show the authenticated Union identity, the data-plane endpoint, and a 2xx status. Control plane API logs over the same window should show no payload-bearing requests for the secret.

- **Consumption path:** Inspect the task pod configuration:

  ```bash
  kubectl describe pod <task-pod> -n <workspace-namespace>
  ```

  The pod should show secrets mounted from the customer's backend (e.g., AWS Secrets Manager volume mounts or environment variable references).

- **Scoping:** Create a secret in project A, then run a task in project B that attempts to access it. The task should fail. Run the same task in project A, and it should succeed.
