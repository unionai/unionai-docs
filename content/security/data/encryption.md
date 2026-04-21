---
title: Encryption
weight: 3
variants: -flyte +union
---

# Encryption

Union.ai encrypts all data at rest and in transit across every storage and communication path in the platform. Transit encryption uses TLS + mTLS + Cloudflare Tunnel for all cross-plane communication. At-rest encryption is provided by cloud provider services (S3 SSE, GCS encryption, Azure SSE, AWS RDS AES-256). Data that transits control plane memory (structured task I/O, secret values during creation, log streams) is encrypted on every network hop but exists as plaintext in process memory during request handling -- this is standard for any service that processes data.

## Encryption at rest

| Storage | Standard | Key Management |
|---|---|---|
| Object Store (S3/GCS/Azure Blob) | Cloud-provider default (SSE-S3, Google-managed, Azure SSE) | Cloud provider managed; CMK supported |
| Container Registry | Cloud-provider encryption | Cloud provider managed |
| Secrets Backend (cloud) | Cloud-provider encryption | Cloud secrets manager |
| Secrets Backend (K8s) | etcd encryption | K8s cluster-level |
| ClickHouse | Encrypted EBS/persistent disk | Cloud provider managed |
| Control Plane PostgreSQL | AWS RDS encryption | AES-256; AWS KMS managed |

All data at rest is encrypted using cloud-provider native encryption. Each storage backend uses the default encryption mechanism provided by the underlying cloud service, ensuring that encryption is always active without requiring additional configuration. For object stores (S3, GCS, Azure Blob Storage), customers can bring their own customer-managed keys (CMK) to gain full control over key rotation, access policies, and revocation. The control plane database uses AES-256 encryption managed through AWS KMS, consistent with Union.ai's SOC 2 Type II controls.

## Encryption in transit

All communication paths in the Union.ai platform are encrypted using TLS:

- **Client to control plane** -- all API and UI traffic uses TLS 1.2 or higher.
- **Control plane to data plane** -- all traffic flows through Cloudflare Tunnel, which enforces mutual TLS.
- **Client to object store** -- presigned URLs always use HTTPS, enforced by the cloud provider.
- **Internal data plane communication** -- uses cloud-native TLS for inter-service traffic.

No unencrypted communication paths exist in the platform. The combination of TLS at the edge, mutual TLS through the tunnel, and HTTPS for presigned URLs ensures end-to-end encryption for all data in transit. Data content is never logged at any log level. (Note: if debug logging is enabled in the control plane, authentication credentials -- not data content -- may be logged in plaintext by the header-propagation utility.)

For details on the tunnel architecture, see [Two-plane separation](../architecture/two-plane-separation).

## Data protection summary

The following table summarizes the encryption state for each data category across all phases:

| Data category | In transit | At rest | Enters CP memory? | Persisted in CP? |
|---|---|---|---|---|
| **Files, directories, DataFrames** | HTTPS (presigned URL) | S3 SSE / GCS / Azure SSE | No | No |
| **Code bundles** | HTTPS (presigned URL) | S3 SSE / GCS / Azure SSE | No | No |
| **Container images** | HTTPS (registry pull) | ECR/GCR/ACR encryption | No | No |
| **Inter-task I/O** (in-cluster) | Cloud SDK TLS | S3 SSE / GCS / Azure SSE | No | No |
| **Structured task inputs** (run submission) | TLS + TLS/mTLS/tunnel | S3 SSE / GCS / Azure SSE | Yes (plaintext, transient) | No |
| **Structured task I/O** (retrieval) | TLS + TLS/mTLS/tunnel | S3 SSE / GCS / Azure SSE | Yes (plaintext, transient) | No |
| **Secret values** (create/update) | TLS + TLS/mTLS/tunnel | ASM/GCP SM/AKV/etcd encryption | Yes (plaintext, transient) | No |
| **Secret values** (get/list/delete) | TLS | ASM/GCP SM/AKV/etcd encryption | No (metadata only) | No |
| **Secret values** (runtime injection) | Linkerd mTLS / K8s API | Secret backend encryption | No (data plane only) | No |
| **Execution logs** (streaming) | TLS + TLS/mTLS/tunnel | CloudWatch/Stackdriver/Azure Monitor | Yes (plaintext, transient) | No |
| **Task definitions** (TaskSpec) | TLS | PostgreSQL AES-256/KMS | Yes (read from DB) | **Yes** (encrypted at rest) |
| **Run/trigger specs** | TLS | PostgreSQL AES-256/KMS | Yes (read from DB) | **Yes** (encrypted at rest) |
| **Error messages** | TLS/mTLS/tunnel | Cassandra (storage-level) | Yes (read from DB) | **Yes** |
| **Execution metadata** (phase, timestamps) | TLS/mTLS/tunnel | PostgreSQL AES-256/KMS + Cassandra | Yes (read from DB) | **Yes** (encrypted at rest) |

"Transient" means the data exists in process memory only for the duration of a single request and is not written to disk, cache, or logs. For details on each data flow pattern, see [Data flow](./data-flow).

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

### Encryption in transit

**Reviewer focus:** Confirm that all communication paths use TLS and that no plaintext channels exist.

**How to verify:**

1. Verify TLS on the control plane endpoint:

   ```bash
   openssl s_client -connect <cp-endpoint>:443
   ```

   Confirm TLS version (1.2 or higher) and cipher suite in the output.

2. Check the browser lock icon when accessing the Union.ai UI for certificate details.

3. Confirm that all presigned URLs use HTTPS -- inspect any presigned URL generated by the platform.

4. Check the Cloudflare Tunnel pod logs for TLS handshake confirmation:

   ```bash
   kubectl logs <tunnel-pod> -n <control-plane-namespace>
   ```

This verification is fully self-service.
