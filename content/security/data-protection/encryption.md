---
title: Encryption
weight: 3
variants: -flyte +union
---

# Encryption

Union.ai encrypts all data at rest and in transit across every storage and communication path in the platform. Transit encryption uses TLS 1.2+ for all communication paths, with mutual TLS (mTLS) layered through the Direct-to-DataPlane tunnel for client-to-data-plane traffic. At-rest encryption is provided by cloud provider services (S3 SSE, GCS encryption, Azure SSE) for customer-side storage, and by managed cloud database services (AES-256/KMS) for the control plane. Under Zero Trust, customer data never enters control plane memory in any form -- it is served directly from the data plane through the tunnel.

## Encryption at rest

| Storage | Standard | Key Management |
|---|---|---|
| Object Store (S3/GCS/Azure Blob) | Cloud-provider default (SSE-S3, Google-managed, Azure SSE) | Cloud provider managed; CMK supported |
| Container Registry | Cloud-provider encryption | Cloud provider managed |
| Secrets Backend (cloud) | Cloud-provider encryption | Cloud secrets manager |
| Secrets Backend (K8s) | etcd encryption | K8s cluster-level |
| Observability metrics store (per-cluster) | Encrypted persistent disk | Cloud provider managed |
| Control plane databases | Managed cloud database service | AES-256; cloud KMS managed |

All data at rest is encrypted using cloud-provider native encryption. Each storage backend uses the default encryption mechanism provided by the underlying cloud service, ensuring that encryption is always active without requiring additional configuration. For object stores (S3, GCS, Azure Blob Storage), customers can bring their own customer-managed keys (CMK) to gain full control over key rotation, access policies, and revocation. Control plane databases use AES-256 encryption managed through the cloud KMS, consistent with Union.ai's SOC 2 Type II controls.

## Encryption in transit

All communication paths in the Union.ai platform are encrypted using TLS:

- **Client to control plane**: orchestration API and UI metadata traffic uses TLS 1.2+.
- **Client to data plane**: customer-data requests resolve to the per-cluster Direct-to-DataPlane tunnel domain. TLS 1.3 from the client to the Cloudflare edge; mTLS plus Cloudflare Tunnel encryption from the edge to the data plane.
- **Data plane to control plane**: outbound-only direct gRPC over TLS 1.2+ for orchestration RPCs (action lifecycle, events, registration). No customer data on this channel. See [Network architecture](../architecture/network).
- **Client to object store**: presigned URLs always use HTTPS, enforced by the cloud provider.
- **Internal data plane communication**: uses cloud-native TLS for inter-service traffic.

No unencrypted communication paths exist in the platform. Data content is never logged at any log level.

For details on the cross-plane channels, see [Network architecture](../architecture/network).

## Data protection summary

The following table summarizes the encryption state for each data category across all phases:

| Data category | In transit | At rest | Enters control plane memory? | Persisted in control plane? |
|---|---|---|---|---|
| **Files, directories, DataFrames** | HTTPS (presigned URL) | S3 SSE / GCS / Azure SSE | No | No |
| **Code bundles** | HTTPS (presigned URL) | S3 SSE / GCS / Azure SSE | No | No |
| **Container images** | HTTPS (registry pull) | ECR/GCR/ACR encryption | No | No |
| **Inter-task I/O** (in-cluster) | Cloud SDK TLS | S3 SSE / GCS / Azure SSE | No | No |
| **Structured task inputs** (run submission) | TLS 1.3 + mTLS tunnel | S3 SSE / GCS / Azure SSE | No | No |
| **Structured task I/O** (retrieval) | TLS 1.3 + mTLS tunnel | S3 SSE / GCS / Azure SSE | No | No |
| **Secret values** (create/update) | TLS 1.3 + mTLS tunnel | ASM/GCP SM/AKV/etcd encryption | No | No |
| **Secret values** (get/list/delete) | TLS | ASM/GCP SM/AKV/etcd encryption | No (metadata only) | No |
| **Secret values** (runtime injection) | Linkerd mTLS / Kubernetes API | Secret backend encryption | No (data plane only) | No |
| **Execution logs** (live & persisted) | TLS 1.3 + mTLS tunnel | CloudWatch / Cloud Logging / Azure Monitor | No | No |
| **Task definitions** (TaskSpec) | TLS | Control plane database (AES-256/KMS) | Yes (read from DB) | **Yes** (encrypted at rest) |
| **Run/trigger specs** | TLS | Control plane database (AES-256/KMS) | Yes (read from DB) | **Yes** (encrypted at rest) |
| **Error messages** | TLS (gRPC) | Control plane database (storage-level) | Yes (read from DB) | **Yes** |
| **Execution metadata** (phase, timestamps) | TLS (gRPC) | Control plane database (AES-256/KMS) | Yes (read from DB) | **Yes** (encrypted at rest) |

Customer-data categories (everything above the task-definition row) route from the client directly to the data plane. Under the default tier this is the Direct-to-DataPlane tunnel: TLS 1.3 from the client to the Cloudflare edge, then mTLS plus Cloudflare Tunnel encryption from the edge to the data plane. Under the [Sovereign Data Plane](../architecture/sovereign-data-plane) tier this is a single TLS hop from the client (on the corporate VPN) to a customer-managed internal load balancer. In both cases, authentication and RBAC are enforced by the Envoy router inside the customer's cluster, and the control plane is not on the path. For details, see [Data flow](./data-flow).

## Verification

### Encryption at rest

**Reviewer focus:** Confirm that all storage backends are encrypted and verify key management configuration.

**How to verify:**

1. Check object store encryption:

   ```bash
   aws s3api get-bucket-encryption --bucket <customer-bucket>
   ```

   The output should show SSE configuration (SSE-S3, SSE-KMS, or SSE-C depending on configuration).

2. Check Kubernetes storage classes for ClickHouse volumes:

   ```bash
   kubectl get sc -o yaml
   ```

   Encrypted storage classes should be configured for ClickHouse persistent volumes.

3. For customer-managed keys, verify key configuration:

   ```bash
   aws kms describe-key --key-id <key-id>
   ```

This verification is fully self-service.

### Customer-managed key authority

**Reviewer focus:** Confirm that bulk data is unreadable without the customer's encryption keys, regardless of who holds a presigned URL.

**How to verify:**

1. From a successful workflow run, capture a presigned URL for an output artifact (Union.ai UI, browser developer tools → Network tab, or via `uctl`).

2. Confirm the URL fetches the artifact:

   ```bash
   curl -o /tmp/output "<presigned-url>"
   ```

3. Disable the customer-managed key that encrypts the bucket:

   ```bash
   aws kms disable-key --key-id <bucket-kms-key-id>
   ```

   On GCP, disable the CMEK key version protecting the bucket. On Azure, disable the customer-managed key in Key Vault.

4. Re-fetch the same URL (or issue a fresh one). The request should fail with `KMS.DisabledException` (AWS) or the equivalent. Re-enable the key to restore access.

The presigned URL itself is unchanged and still authentic. The data behind it is opaque without the customer's key -- proof that customer-controlled keys are the final gate on bulk data access, independent of who can issue URLs.

### Encryption in transit

**Reviewer focus:** Confirm that all communication paths use TLS and that no plaintext channels exist.

**How to verify:**

1. Verify TLS on the control plane endpoint:

   ```bash
   openssl s_client -connect <cp-endpoint>:443
   ```

   Confirm TLS version (1.2 or higher) and cipher suite in the output.

2. Check the browser lock icon when accessing the Union.ai UI for certificate details.

3. Confirm that all presigned URLs use HTTPS by inspecting any presigned URL generated by the platform.

4. Check the Cloudflare Tunnel pod logs for TLS handshake confirmation:

   ```bash
   kubectl logs <tunnel-pod> -n <control-plane-namespace>
   ```

This verification is fully self-service.
