---
title: Data flow
weight: 2
variants: -flyte +union
---

# Data flow

Union.ai uses three distinct patterns to move data between the data plane and clients: presigned URLs for bulk data, an inline proxy for structured task I/O, and streaming relays for live data. All three patterns encrypt data in transit. The patterns differ in whether data enters control plane memory.

```
Presigned URL pattern (bulk data — never enters control plane):
  SDK/UI ──HTTPS──→ Object Store (direct, encrypted at rest)

Inline proxy pattern (structured I/O — transits control plane):
  SDK/UI ──TLS──→ Control Plane ──(plaintext in memory)──→ ──TLS+mTLS+tunnel──→ Operator → Object Store (encrypted at rest)

Streaming relay pattern (logs — transits control plane):
  DP ──TLS+mTLS+tunnel──→ Control Plane ──(plaintext in memory)──→ ──TLS──→ Client
```

## Presigned URL pattern

For bulk data -- files (`flyte.io.File`), directories (`flyte.io.Dir`), DataFrames, code bundles, and reports -- the control plane proxies signing requests to the data plane, which generates time-limited presigned URLs using customer-managed IAM credentials. The client then uploads or downloads data directly to the customer's object store. The data content never enters the control plane; only the signing metadata passes through. This model eliminates the need for the control plane to hold persistent cloud IAM credentials.

| Phase | Encrypted? | Details |
|-------|------------|---------|
| Client → Object Store | **Yes** | HTTPS via presigned URL, direct to customer storage |
| At rest | **Yes** | S3 SSE / GCS encryption / Azure SSE |
| Control plane involvement | **None** | CP generates/relays the signed URL only; data content never enters CP |

## Inline proxy pattern

For structured task inputs and outputs (protobuf literals such as ints, strings, lists, dicts, and small serialized objects), the control plane acts as a proxy. On run submission, the SDK sends structured inputs to the control plane (up to 10 MiB). The control plane proxies the full payload through its memory to the data plane object store via the Cloudflare Tunnel. On result retrieval, the control plane fetches both inputs and outputs from the data plane object store and returns them to the client (up to 20 MiB). The data is encrypted in transit (TLS on both sides), exists as plaintext in control plane memory for the duration of each request, and is not persisted, cached, or logged. The same pattern applies to secret values during create/update operations, which are relayed through the control plane to the data plane's secrets backend.

The distinction between presigned URLs and the inline proxy is by data type, not by size: binary artifacts always use presigned URLs; structured protobuf literals always use the inline proxy.

**Encryption at each phase (run submission):**

| Phase | Encrypted? | Details |
|-------|------------|---------|
| Client → Control Plane | **Yes** | TLS 1.2+. Wire format: protobuf binary |
| In Control Plane | **Plaintext in memory** | Deserialized protobuf, hashed for cache key, then re-serialized. Not persisted, cached, or logged |
| Control Plane → Data Plane | **Yes** | TLS + mTLS + Cloudflare Tunnel. Wire format: protobuf JSON |
| At rest (data plane object store) | **Yes** | S3 SSE / GCS encryption / Azure SSE |

**Encryption at each phase (result retrieval):**

| Phase | Encrypted? | Details |
|-------|------------|---------|
| At rest (data plane object store) | **Yes** | S3 SSE / GCS encryption / Azure SSE |
| Data Plane → Control Plane | **Yes** | TLS + mTLS + Cloudflare Tunnel |
| In Control Plane | **Plaintext in memory** | Full inputs and outputs deserialized. Not persisted, cached, or logged |
| Control Plane → Client | **Yes** | TLS 1.2+ |

The following controls are applied to every presigned URL:

- **TTL enforcement**: each URL expires after a default of 1 hour, configurable to shorter durations.
- **Single-object scope**: each URL grants access to exactly one object.
- **Operation specificity**: each URL is locked to a single operation (GET or PUT).
- **Transport encryption**: URLs are transmitted only over TLS.
- **No URL logging**: presigned URLs are not persisted in control plane logs or databases.

Because presigned URLs are bearer tokens (possession alone grants access), Union.ai recommends treating them with the same care as short-lived credentials and configuring the shortest practical TTL for your use case.

## Streaming relay pattern

For logs and observability metrics, the control plane acts as a stateless relay. It streams data from the data plane through the Cloudflare Tunnel to the client in real time. The data passes through the control plane's memory as plaintext, encrypted in transit on both network hops. It is never written to disk, cached, or stored. Once the stream completes, no trace of the data remains in the control plane. There is no content filtering or redaction in the log streaming pipeline. Any sensitive data (secrets, PII, credentials) that user code writes to stdout/stderr will flow through control plane memory unmodified.

| Phase | Encrypted? | Details |
|-------|------------|---------|
| Data plane log source → DP operator | **Yes** | Linkerd mTLS (pod-to-pod) or cloud SDK TLS (CloudWatch / Cloud Logging / Azure Monitor) |
| Data Plane → Control Plane | **Yes** | TLS + mTLS + Cloudflare Tunnel. Wire format: protobuf streaming |
| In Control Plane | **Plaintext in memory** | Each log message deserialized for byte counting. Not persisted, cached, or logged. No content filtering |
| Control Plane → Client | **Yes** | TLS 1.2+ (streaming) |
| At rest (data plane log backend) | **Yes** | CloudWatch (AES-256/KMS), Cloud Logging (Google-managed), or Azure Monitor (Microsoft-managed) |

## Data in the UI

The Union.ai web console displays information from multiple sources. The following table shows where each UI field originates, where that data is stored, and how the browser retrieves it:

| Field | Source | Access method |
|---|---|---|
| Task names (function/module names) | Control Plane | CP API |
| User names | IDP (cached in CP memory) | IDP / CP |
| Inputs/outputs (structured) | Data plane object store via CP proxy | Cloudflare Tunnel (transits CP memory) |
| Logs (live) | Data plane K8s | Cloudflare Tunnel |
| Logs (persisted) | Data plane log aggregator (CloudWatch / Cloud Logging / Azure Monitor) | Cloudflare Tunnel |
| K8s events | Data plane K8s | Cloudflare Tunnel |
| Reports (HTML) | Data plane object store | Signed URL, rendered in browser iframe |
| Code explorer | Data plane object store | Signed URL, JS downloads and unzips bundle |
| Timeline timestamps | Control Plane | CP API |
| Errors | Control Plane | CP API |

Fields sourced from the control plane include orchestration metadata and task definitions, which may contain potentially sensitive fields such as environment variables and default values (see [Data classification and residency](./classification-and-residency) for the full enumeration). Structured inputs/outputs are proxied through control plane memory via the inline proxy pattern before reaching the client. Fields sourced directly from the data plane via presigned URLs (reports, code bundles) bypass the control plane entirely. Error messages served from the control plane database may contain customer data from Python tracebacks.

For details on the underlying network architecture, see [Network architecture](../architecture/network).

## Verification

### Presigned URLs

**Reviewer focus:** Confirm that presigned URLs point to the customer's object store, expire as documented, and are scoped to a single object.

**How to verify (browser-based):**

1. Open the Union.ai UI and navigate to a completed task's outputs.
2. Open browser developer tools (Network tab) and observe the request when viewing output data.
3. The presigned URL should resolve to the customer's S3/GCS/Azure Blob domain (not a Union.ai domain), contain an expiry parameter, and reference a single object key.
4. Copy the presigned URL and wait 1 hour. Paste it into the browser. It should return a 403 (TTL expired).
5. Modify the object key in the URL and retry immediately. It should return a 403 (signature invalid, confirming single-object scope).

### Streaming relay

**Reviewer focus:** Confirm that logs and metrics streamed through the control plane are not persisted.

**How to verify:**

Proving non-persistence is inherently difficult. The best available evidence:

1. Inspect the control plane proxy pod configuration:

   ```bash
   kubectl describe pod <control-plane-proxy-pod> -n <control-plane-namespace>
   ```

   The pod should have no persistent volumes mounted and no database connection environment variables.

2. The SOC 2 Type II audit covers the non-persistence control for streaming relays. Request the current report from Union.ai.

3. (Advanced) Compare log content flowing through the tunnel against control plane state before and after streaming. There should be no delta in stored data.

### UI data sources

**Reviewer focus:** Confirm that the UI retrieves customer data exclusively through presigned URLs or tunnel relays, not from the control plane.

**How to verify:**

Walk through each panel of the Union.ai UI with browser developer tools open. For each data element, the Network tab shows whether the request goes to the CP API (metadata) or to a presigned URL / tunnel relay endpoint (customer data). Every field in the table above should match its documented access method. This verification is fully self-service.
