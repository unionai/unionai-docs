---
title: Secrets management
description: How secret values stay in customer infrastructure behind a write-only API that never returns them.
icon: safe
weight: 4
variants: -flyte +union
---

# Secrets management

Union.ai's secrets management system stores secret values exclusively within the customer's infrastructure and exposes them through a write-only API: there is no endpoint that returns a secret value. The `GetSecret` RPC returns only metadata (name, scope, creation time, cluster presence status); Get, List, and Delete operations never expose the value. Secret writes go directly to the data plane through the Direct-to-Data-Plane tunnel, so secret values never transit the control plane. Compromising a user account or the control plane API yields no path to read secret values back.

## Backends

| Backend | Storage Location | Default |
|---|---|---|
| Kubernetes Secrets | Kubernetes etcd on customer cluster | Self-managed default |
| AWS Secrets Manager | AWS-managed service | BYOC default (AWS) |
| GCP Secret Manager | GCP-managed service | BYOC default (GCP) |
| Azure Key Vault | Azure-managed service | BYOC default (Azure) |

All four backends are available regardless of deployment model. The choice of backend is a deployment configuration on the data plane operator. Each backend integrates with its cloud provider's native encryption and access control mechanisms.

## Secret lifecycle

**Creation:** When a user creates a secret via the UI or CLI, the value is sent directly to the data plane's secrets backend over the client-to-data-plane channel -- the Direct-to-Data-Plane tunnel under the default tier, or the customer-managed internal load balancer under the [Sovereign Data Plane](../architecture/sovereign-data-plane) tier -- and stored encrypted at rest in the customer's secret manager (AWS Secrets Manager, GCP Secret Manager, Azure Key Vault, or Kubernetes Secrets). The value never enters Union.ai's control plane in any form. The Envoy router inside the customer's cluster authenticates the request against Union.ai identity and enforces RBAC before the value reaches the secrets backend.

| Phase | Encrypted? | Details |
|-------|------------|---------|
| Client → Cloudflare edge | **Yes** | TLS 1.3 (default tier only) |
| Cloudflare edge → data plane (tunnel) | **Yes** | mTLS + Cloudflare Tunnel |
| Client → Internal load balancer | **Yes** | TLS, customer-managed certificate ([Sovereign Data Plane](../architecture/sovereign-data-plane) tier only) |
| At Envoy router (data plane) | **Plaintext in memory** | AuthN + RBAC check; not persisted, cached, or logged |
| In data plane (operator) | **Plaintext in memory** | Briefly held before writing to secret backend |
| At rest (secret backend) | **Yes** | AWS Secrets Manager (AES-256/KMS), GCP Secret Manager (Google-managed or CMEK), Azure Key Vault (HSM-backed), or Kubernetes etcd encryption |

**Consumption:** When a task pod is created, the data plane's secret injector reads each requested secret from the backend and adds it to the pod spec. For a secret mounted as a file, the injector writes the base64-encoded value into an init container's `SECRETS` environment variable. The init container decodes it into an in-memory volume that the task container mounts. Because the init container's environment is part of the pod spec, the encoded value is stored with the pod object. Anyone who can read pods in the namespace can decode it, so it is protected only by Kubernetes RBAC and etcd encryption. A secret mounted as an environment variable is a `secretKeyRef` to a Kubernetes Secret, so it requires the secret to be stored in Kubernetes Secrets. One exception applies on data planes that enable the AWS or Azure secret injector, as Union.ai's AWS and Azure data plane configurations do. There, a file secret that sets a `group` is not read by the injector or put in the pod spec. Instead, an init container receives the secret's location (on AWS, the ARN formed from the `group` and `key`; on Azure, the Key Vault secret URI given as the `group`), fetches the value from AWS Secrets Manager or Azure Key Vault when the pod starts, and writes it to a separate in-memory volume. The value never leaves the customer's infrastructure during this process. The control plane is not involved in secret consumption at runtime.

**Scoping:** Secrets can be scoped at the organization, domain, or project-domain level. Only task pods running within the appropriate scope can access the corresponding secrets. This ensures that teams working in different projects cannot access each other's secrets, even within the same data plane cluster.

## Verification

### Write-only API

**Reviewer focus:** Confirm that no API endpoint returns secret values and that the write-only design holds.

**How to verify:**

1. Create a test secret:

   ```bash
   flyte create secret --project myproject test-secret --value "s3cr3t-value"
   ```

2. Attempt to read it back:

   ```bash
   flyte get secret --project myproject test-secret
   ```

   The output should show name, scope, creation time, and cluster status. There should be **no value field** in the response.

3. Try every API endpoint that touches secrets. None should return the value.

4. Check the protobuf definition in the open-source Flyte repository. `GetSecretResponse` has no value field. The write-only design is enforced at the protocol level.

5. Verify the secret exists in the customer's secrets backend by checking the cloud secrets manager console directly. The value should be present there.

This verification is fully self-service and works immediately. Note that the write-only design is enforced at the protocol level: Union.ai's API structurally cannot return secret values, regardless of the caller's privilege level.

### Secret lifecycle

**Reviewer focus:** Confirm that secret values are written directly to the data plane backend through the Direct-to-Data-Plane tunnel without traversing the control plane, and are consumed entirely within the data plane at runtime.

**How to verify:**

- **Creation path:** Inspect Cloudflare Access logs for the tunnel during a secret create operation. Each request should show the authenticated Union identity, the data plane endpoint, and a 2xx status. Control plane API logs over the same window should show no payload-bearing requests for the secret.

- **Consumption path:** Inspect the task pod configuration:

  ```bash
  kubectl describe pod <task-pod> -n <workspace-namespace>
  ```

  For secrets without a `group`, the pod does not mount the backend. File secrets appear as an in-memory `emptyDir` volume named `embedded-secret-vol`, filled by an init container whose `SECRETS` environment variable holds the base64-encoded values. The command prints those values, so treat its output as secret. Environment-variable secrets appear in the container's environment as `<set to the key '…' in secret '…'>` entries, which are `secretKeyRef` references to a Kubernetes Secret (`kubectl get pod -o yaml` shows the `secretKeyRef` field itself). On data planes with the AWS secret injector, a file secret that sets a `group` appears instead as an in-memory volume named `aws-secret-vol`, filled by an `aws-pull-secret-<n>` init container whose `SECRET_ARN` environment variable holds the secret's ARN. On data planes with the Azure secret injector, it appears as an in-memory volume named `azure-secret-vol`, filled by an `azure-pull-secret-<n>` init container whose command holds the Key Vault secret URI.

- **Scoping:** Create a secret in project A, then run a task in project B that attempts to access it. The task should fail. Run the same task in project A, and it should succeed.
