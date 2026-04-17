---
title: Data flow
weight: 2
variants: -flyte +union
---

Union.ai uses two distinct patterns to move data between the data plane and clients: presigned URLs for stored objects and streaming relays for live data. Both patterns are designed to keep customer data out of the control plane.

## Presigned URL pattern

For task inputs, outputs, code bundles, and reports, the control plane proxies signing requests to the data plane, which generates time-limited presigned URLs using customer-managed IAM credentials. The client then fetches or uploads data directly to the customer's object store -- the data never transits the control plane. This model eliminates the need for the control plane to hold persistent cloud IAM credentials.

The following controls are applied to every presigned URL:

- **TTL enforcement** -- each URL expires after a default of 1 hour, configurable to shorter durations.
- **Single-object scope** -- each URL grants access to exactly one object.
- **Operation specificity** -- each URL is locked to a single operation (GET or PUT).
- **Transport encryption** -- URLs are transmitted only over TLS.
- **No URL logging** -- presigned URLs are not persisted in control plane logs or databases.

Because presigned URLs are bearer tokens -- possession alone grants access -- Union.ai recommends treating them with the same care as short-lived credentials and configuring the shortest practical TTL for your use case.

## Streaming relay pattern

For logs and observability metrics, the control plane acts as a stateless relay. It streams data from the data plane through the Cloudflare Tunnel to the client in real time. The data passes through the control plane's memory as a TLS-encrypted stream but is never written to disk, cached, or stored. Once the stream completes, no trace of the data remains in the control plane.

## Data in the UI

The Union.ai web console displays information from multiple sources. The following table shows where each UI field originates, where that data is stored, and how the browser retrieves it:

| Field | Source | Access method |
|---|---|---|
| Task names (function/module names) | Control Plane | CP API |
| User names | IDP (cached in CP memory) | IDP / CP |
| Inputs/outputs | Data plane S3 | Cloudflare Tunnel |
| Logs (live) | Data plane K8s | Cloudflare Tunnel |
| Logs (persisted) | Data plane S3/CloudWatch/Stackdriver | Cloudflare Tunnel |
| K8s events | Data plane K8s | Cloudflare Tunnel |
| Reports (HTML) | Data plane S3 | Signed URL, rendered in browser iframe |
| Code explorer | Data plane S3 | Signed URL, JS downloads and unzips bundle |
| Timeline timestamps | Control Plane | CP API |
| Errors | Control Plane | CP API |

Fields sourced from the control plane contain only orchestration metadata. Fields sourced from the data plane contain customer data and are accessed either through presigned URLs or the streaming relay -- in both cases, the data flows directly between the client and the customer's infrastructure.

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
