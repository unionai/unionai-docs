---
title: Data flow
weight: 2
variants: -flyte +union
---

# Data flow

Union.ai uses two distinct patterns to move data between the data plane and clients: presigned URLs for stored objects and streaming relays for live data. Both patterns are designed to keep customer data out of the control plane.

> [!WARNING]
> **Audit finding (ref #3):** There is a third data flow pattern not described here: structured task I/O (protobuf literals -- ints, strings, lists, dicts, small serialized objects) is proxied through control plane memory via `UploadInputs` (on every run submission, up to 10 MB) and `GetActionData` (on every result retrieval, up to 20 MiB). Only binary artifacts (files, directories, DataFrames, code bundles) use the presigned URL path. The distinction is by data type, not by size. This third pattern should be documented as a separate section.

## Presigned URL pattern

For task inputs, outputs, code bundles, and reports, the control plane proxies signing requests to the data plane, which generates time-limited presigned URLs using customer-managed IAM credentials. The client then fetches or uploads data directly to the customer's object store -- the data never transits the control plane. This model eliminates the need for the control plane to hold persistent cloud IAM credentials.

> [!WARNING]
> **Audit finding (ref #3):** "The data never transits the control plane" is true for the presigned URL path (binary artifacts like files, directories, DataFrames, code bundles, and reports). However, structured task inputs are uploaded through `UploadInputs` (which proxies the full payload through control plane memory), and structured task inputs+outputs are retrieved through `GetActionData` (same proxying pattern). The presigned URL pattern does not apply to structured task I/O.

The following controls are applied to every presigned URL:

- **TTL enforcement** -- each URL expires after a default of 1 hour, configurable to shorter durations.
- **Single-object scope** -- each URL grants access to exactly one object.
- **Operation specificity** -- each URL is locked to a single operation (GET or PUT).
- **Transport encryption** -- URLs are transmitted only over TLS.
- **No URL logging** -- presigned URLs are not persisted in control plane logs or databases.

Because presigned URLs are bearer tokens -- possession alone grants access -- Union.ai recommends treating them with the same care as short-lived credentials and configuring the shortest practical TTL for your use case.

## Streaming relay pattern

For logs and observability metrics, the control plane acts as a stateless relay. It streams data from the data plane through the Cloudflare Tunnel to the client in real time. The data passes through the control plane's memory as a TLS-encrypted stream but is never written to disk, cached, or stored. Once the stream completes, no trace of the data remains in the control plane.

> [!NOTE]
> **Audit finding (ref #6):** This description accurately characterizes the streaming relay as non-persisting. However, note that there is no content filtering or redaction in the log streaming pipeline. Any sensitive data (secrets, PII, credentials) that user code writes to stdout/stderr will flow through control plane memory unmodified.

## Data in the UI

The Union.ai web console displays information from multiple sources. The following table shows where each UI field originates, where that data is stored, and how the browser retrieves it:

| Field | Source | Access method |
|---|---|---|
| Task names (function/module names) | Control Plane | CP API |
| User names | IDP (cached in CP memory) | IDP / CP |
| Inputs/outputs (structured) | Data plane S3 via CP proxy | Cloudflare Tunnel (transits CP memory) |
| Logs (live) | Data plane K8s | Cloudflare Tunnel |
| Logs (persisted) | Data plane S3/CloudWatch/Stackdriver | Cloudflare Tunnel |
| K8s events | Data plane K8s | Cloudflare Tunnel |
| Reports (HTML) | Data plane S3 | Signed URL, rendered in browser iframe |
| Code explorer | Data plane S3 | Signed URL, JS downloads and unzips bundle |
| Timeline timestamps | Control Plane | CP API |
| Errors | Control Plane | CP API |

Fields sourced from the control plane contain only orchestration metadata. Fields sourced from the data plane contain customer data and are accessed either through presigned URLs or the streaming relay -- in both cases, the data flows directly between the client and the customer's infrastructure.

> [!NOTE]
> **Audit finding (ref #3, #7):** "Fields sourced from the control plane contain only orchestration metadata" -- TaskSpec blobs stored in the control plane databases contain potentially sensitive fields (env vars, default values, SQL statements, K8s pod specs, plugin configuration). Also, "Inputs/outputs" in the table above are proxied through control plane memory via `GetActionData`, not fetched directly by the client. The "Errors" row correctly shows these come from the control plane, but error messages can contain customer data from Python tracebacks.

For details on the underlying network architecture, see [Two-plane separation](../architecture/two-plane-separation).

## Verification

### Presigned URLs (Critical)

**Reviewer focus:** Confirm that presigned URLs point to the customer's object store, expire as documented, and are scoped to a single object.

**How to verify (browser-based):**

1. Open the Union.ai UI and navigate to a completed task's outputs.
2. Open browser developer tools (Network tab) and observe the request when viewing output data.
3. The presigned URL should resolve to the customer's S3/GCS/Azure Blob domain (not a Union.ai domain), contain an expiry parameter, and reference a single object key.
4. Copy the presigned URL and wait 1 hour. Paste it into the browser -- it should return a 403 (TTL expired).
5. Modify the object key in the URL and retry immediately -- it should return a 403 (signature invalid, confirming single-object scope).

### Streaming relay (High)

**Reviewer focus:** Confirm that logs and metrics streamed through the control plane are not persisted.

**How to verify:**

Proving non-persistence is inherently difficult. The best available evidence:

1. Inspect the DataProxy pod configuration:

   ```bash
   kubectl describe pod <dataproxy-pod> -n <control-plane-namespace>
   ```

   The pod should have no persistent volumes mounted and no database connection environment variables.

2. The SOC 2 Type II audit covers the non-persistence control for streaming relays. Request the current report from Union.ai.

3. (Advanced) Compare log content flowing through the tunnel against control plane state before and after streaming. There should be no delta in stored data.

### UI data sources (High)

**Reviewer focus:** Confirm that the UI retrieves customer data exclusively through presigned URLs or tunnel relays, not from the control plane.

**How to verify:**

Walk through each panel of the Union.ai UI with browser developer tools open. For each data element, the Network tab shows whether the request goes to the CP API (metadata) or to a presigned URL / tunnel relay endpoint (customer data). Every field in the table above should match its documented access method. This verification is fully self-service.
