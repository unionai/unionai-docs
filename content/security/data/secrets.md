---
title: Secrets management
weight: 4
variants: -flyte +union
---

Union.ai's secrets management system stores secret values exclusively within the customer's infrastructure, with a write-only API design that eliminates an entire class of exfiltration attacks.

## Core design

Secret values are stored exclusively within the customer's infrastructure. The secrets API is write-only by design -- there is no API to read back secret values. The `GetSecret` RPC returns only the secret's metadata (name, scope, creation time, cluster presence status) -- never the value itself. This means that even if an attacker compromises a user account or the control plane API, they cannot retrieve secret values through the API. The value simply is not available through any API endpoint.

## Backends

| Backend | Storage Location | Default |
|---|---|---|
| Kubernetes Secrets | K8s etcd on customer cluster | Self-managed default |
| AWS Secrets Manager | AWS-managed service | BYOC default (AWS) |
| GCP Secret Manager | GCP-managed service | BYOC default (GCP) |
| Azure Key Vault | Azure-managed service | BYOC default (Azure) |

All four backends are available regardless of deployment model. The choice of backend is a deployment configuration on the data plane operator. Each backend integrates with its cloud provider's native encryption and access control mechanisms.

## Secret lifecycle

**Creation:** When a user creates a secret via the UI or CLI, the request is relayed through the Cloudflare Tunnel to the data plane's secrets backend. The secret value transits the control plane in-memory during this relay but is never written to disk or database on the control plane. Once the relay completes, no trace of the value remains in the control plane.

**Consumption:** When a task pod is created, the Executor configures it to mount the requested secrets from the backend as environment variables or files. The value is read by the data plane's secrets backend and injected into the pod -- it never leaves the customer's infrastructure during this process. The control plane is not involved in secret consumption at runtime.

**Scoping:** Secrets can be scoped at organization, project, or domain level. Only task pods running within the appropriate scope can access the corresponding secrets. This ensures that teams working in different projects cannot access each other's secrets, even within the same data plane cluster.

For details on how secrets flow during workflow execution, see [Workflow data flow](./workflow-data-flow).

## Verification

### Write-only API (Critical)

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

3. Try every API endpoint that touches secrets -- none should return the value.

4. Check the protobuf definition in the open-source Flyte repository -- `GetSecretResponse` has no value field. The write-only design is enforced at the protocol level.

5. Verify the secret exists in the customer's secrets backend by checking the cloud secrets manager console directly -- the value should be present there.

6. For comparison: some competing platforms document that workspace admins can read secrets via API. Union.ai's API structurally cannot return secret values, regardless of the caller's privilege level.

This verification is fully self-service and works immediately.

### Secret lifecycle (High)

**Reviewer focus:** Confirm that secret values transit the control plane only in-memory during creation and are consumed entirely within the data plane at runtime.

**How to verify:**

- **Creation path:** Inspect DataProxy pod logs during secret creation:

  ```bash
  kubectl logs <dataproxy-pod> -n <control-plane-namespace>
  ```

  The logs should show the relay operation but not the secret value.

- **Consumption path:** Inspect the task pod configuration:

  ```bash
  kubectl describe pod <task-pod> -n <workspace-namespace>
  ```

  The pod should show secrets mounted from the customer's backend (e.g., AWS Secrets Manager volume mounts or environment variable references).

- **Scoping:** Create a secret in project A, then run a task in project B that attempts to access it -- the task should fail. Run the same task in project A -- it should succeed.
