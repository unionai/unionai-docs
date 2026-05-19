---
title: Data flow
weight: 2
variants: -flyte +union
---

# Data flow

Under Zero Trust, customer data never transits Union.ai's control plane. Every customer-data request -- bulk artifacts, structured task inputs and outputs, secret values, logs, reports, and auxiliary UI traffic -- is served directly from the data plane through the Direct-to-DataPlane tunnel. The control plane is not on the data path.

This page covers two complementary aspects of that model: the **single request pattern** that all customer-data traffic follows, and the **stage-by-stage data movement** during the workflow lifecycle.

## The Direct-to-DataPlane request pattern

Every request that touches customer data follows the same path:

```
Client (SDK / CLI / UI)
   │
   ▼
Cloudflare edge                   ─ TLS 1.3 termination  (default tier only;
   │                                 replaced by a customer-managed internal LB
   ▼                                 under the Sovereign Data Plane tier)
Direct-to-DataPlane tunnel        ─ mTLS, outbound-initiated from the data plane
   │
   ▼
Envoy router (data plane)         ★ AuthN against Union identity, RBAC enforced
   │
   ▼
Dataproxy service (data plane)
   │
   ▼
Object store · logs · secrets ·   ─ customer IAM / Workload Identity
auxiliary UIs                       customer-managed KMS
```

The tunnel (or internal load balancer, under the Sovereign Data Plane tier) terminates **inside the customer's cluster** at the Envoy router. Authentication and authorization run there, against the same Union.ai identity that gates the control plane API -- but the enforcement point is inside the customer's network. Union.ai's control plane never sees the request payload under either tier. See [Sovereign Data Plane](../architecture/sovereign-data-plane) for the Sovereign Data Plane topology.

| Phase | Encrypted? | Details |
|-------|------------|---------|
| Client → Cloudflare edge | **Yes** | TLS 1.3 (default tier only) |
| Cloudflare edge → Data Plane (tunnel) | **Yes** | mTLS + Cloudflare Tunnel (default tier only) |
| Client → Internal load balancer | **Yes** | TLS, customer-managed certificate (Sovereign Data Plane tier only) |
| At Envoy router (data plane) | **Plaintext in memory** | AuthN + RBAC check; not persisted, cached, or logged |
| Data Plane → Object store / log source / secret backend | **Yes** | Cloud-native TLS, signed URLs for object access |
| At rest (customer's storage) | **Yes** | S3 SSE / GCS / Azure SSE; CMK supported |

The Cloudflare-edge and tunnel rows apply under the default tier. Under the [Sovereign Data Plane](../architecture/sovereign-data-plane) tier, those two hops are replaced by the single internal-load-balancer hop shown above; the remaining hops are identical.

Bulk artifacts (files, directories, DataFrames, code bundles, reports) use **presigned URLs** so that the data content never even enters the dataproxy: the dataproxy issues the signed URL via the tunnel, and the client then transfers data directly between itself and the customer's object store. Structured task inputs and outputs, log streams, secret writes, and auxiliary UI traffic flow through the dataproxy itself within the customer's cluster.

### Presigned URL controls

Every presigned URL issued by the dataproxy carries the same controls:

- **TTL enforcement:** each URL expires after a default of 1 hour, configurable to shorter durations.
- **Single-object scope:** each URL grants access to exactly one object.
- **Operation specificity:** each URL is locked to a single operation (GET or PUT).
- **Transport encryption:** URLs are transmitted only over TLS.
- **No URL logging:** presigned URLs are not persisted in logs or databases on either plane.

Because presigned URLs are bearer tokens (possession alone grants access), Union.ai recommends treating them with the same care as short-lived credentials and configuring the shortest practical TTL for your use case.

## Workflow lifecycle

The Direct-to-DataPlane pattern applies at every stage of the workflow lifecycle. The sections below trace how data moves at each stage.

### Run launch: the ping-pong upload flow

Launching a run is the one behavior that changes visibly under Zero Trust. Prior to Zero Trust, the SDK sent inputs to the control plane, which then uploaded them to the customer's object store using a signed URL it issued to itself. Under Zero Trust, the upload happens client-to-data-plane first, and `CreateRun` is called by reference -- a two-step "ping-pong" pattern. The control plane never sees the input bytes.

```
SDK / CLI / UI                            Data-plane dataproxy        Customer object store     Control plane
     │                                            │                            │                       │
     │ ─── 1. SelectCluster(project/domain) ──────┼────────────────────────────┼──────────────────────▶ │
     │ ◀───── per-cluster tunnel domain ──────────┼────────────────────────────┼─────────────────────── │
     │                                            │                            │                       │
     │ ─── 2. CreateUploadLocation ──────────────▶│                            │                       │
     │ ◀───── signed PUT URL ─────────────────────│                            │                       │
     │                                            │                            │                       │
     │ ─── 3. PUT inputs (direct upload) ─────────┼───────────────────────────▶│                       │
     │ ◀───── 200 OK ─────────────────────────────┼────────────────────────────│                       │
     │                                            │                            │                       │
     │ ─── 4. CreateRun(inputs_uri = ...) ────────┼────────────────────────────┼──────────────────────▶ │
     │ ◀───── run ID ─────────────────────────────┼────────────────────────────┼─────────────────────── │
```

1. **SelectCluster.** The SDK calls `SelectCluster` on the control plane with the run's project/domain (or queue/org). The control plane returns the per-cluster tunnel domain (under the default tier) or the per-cluster internal LB hostname (under Sovereign Data Plane) for the cluster that will handle this request class. The SDK caches this for subsequent calls in the same submission.

2. **CreateUploadLocation.** The SDK calls `CreateUploadLocation` on the data-plane dataproxy through the resolved tunnel/LB. The Envoy router authenticates the request against Union identity and enforces RBAC. The dataproxy returns a short-lived signed PUT URL into the customer's object store, plus the URI the URL writes to.

3. **Direct upload.** The SDK uploads the serialized inputs (and any binary input artifacts) directly to the customer's object store using the signed URL. The data flows client-to-object-store; no Union service is on the path. If the signed URL expires before the upload completes, the SDK transparently re-requests a fresh URL and retries once.

4. **CreateRun by reference.** The SDK calls `CreateRun` on the control plane with the URI from step 2 (not the bytes). The control plane validates the URI shape, stores it alongside the run metadata, and enqueues the action to the data plane. The control plane never sees the input bytes.

`CreateRun` and `UploadInputs` are separate APIs under Zero Trust. Prior architectures fused them into a single call that carried the bytes; the split is what makes the no-CP-transit guarantee possible.

The code bundle follows the same pattern: it is uploaded directly to the customer's object store via a presigned PUT URL issued by the dataproxy, and `CreateRun` references the resulting URI. Code never touches the control plane.

### Task execution

Once the action is enqueued, the Executor on the data plane creates a pod that reads inputs from and writes outputs back to the customer's object store. During workflow execution, inter-task I/O flows directly between task pods and the object store via IAM, with no control plane involvement. Secrets required by the task are injected into pods from the customer's secrets backend at runtime; secret values do not traverse the control plane during execution. The control plane receives phase transitions, status updates, and error messages from the Executor. Error messages may contain customer data from Python tracebacks.

The task specification (container image, resource requirements, typed interface, configuration) is stored in the control plane databases -- this is metadata, not customer data.

### Result retrieval

All four channels for accessing run results serve their data from the data plane through the Direct-to-DataPlane tunnel; none transit the control plane:

- **Binary outputs, reports, and code bundles** are accessed via presigned URLs issued by the data-plane dataproxy. The data flows directly from the customer's object store to the client.
- **Structured outputs** (protobuf literals) are retrieved through the data-plane dataproxy from the data-plane object store, served back to the client through the tunnel.
- **Logs** (live and persisted) are served from the data plane through the tunnel. The control plane is not a relay.
- **Metadata** (run status, phase transitions, timestamps, error messages) is served directly from the control plane database. Metadata is the only category the control plane ever serves; it contains no customer data payload.

## Data in the UI

The Union.ai web console displays information from multiple sources. The following table shows where each UI field originates and how the browser retrieves it:

| Field | Source | Access method |
|---|---|---|
| Task names (function/module names) | Control plane | CP API |
| User names | IDP (cached in CP memory) | IDP / CP |
| Inputs/outputs (structured) | Data plane dataproxy | Direct-to-DataPlane tunnel |
| Logs (live) | Data plane Kubernetes | Direct-to-DataPlane tunnel |
| Logs (persisted) | Data plane log aggregator (CloudWatch / Cloud Logging / Azure Monitor) | Direct-to-DataPlane tunnel |
| K8s events | Data plane Kubernetes | Direct-to-DataPlane tunnel |
| Reports (HTML) | Data plane object store | Signed URL, rendered in browser iframe |
| Code explorer | Data plane object store | Signed URL, JS downloads and unzips bundle |
| Timeline timestamps | Control plane | CP API |
| Errors | Control plane | CP API |

Fields sourced from the control plane include orchestration metadata and task definitions, which may contain potentially sensitive fields such as environment variables and default values (see [Data classification and residency](./classification-and-residency) for the full enumeration). Error messages served from the control plane database may contain customer data from Python tracebacks.

For details on the underlying network architecture, see [Network architecture](../architecture/network).

## Verification

### Direct-to-DataPlane request path

**Reviewer focus:** Confirm that customer-data requests resolve to the customer's data plane via the Direct-to-DataPlane tunnel, with no Union control plane involvement.

**How to verify (browser-based):**

1. Open the Union.ai UI and navigate to a completed run.
2. Open browser developer tools (Network tab) and observe the requests when viewing inputs, outputs, and logs.
3. Each customer-data request should resolve to a per-cluster tunnel domain (e.g. `<cluster-id>.<base-domain>`), not to the Union control plane endpoint.
4. Bulk-data requests (binary outputs, reports, code bundles) should resolve directly to the customer's object store domain (S3/GCS/Azure Blob), via a signed URL.

**How to verify (audit-log-based):**

The Direct-to-DataPlane request pattern is auditable independently from outside Union:

- **Cloudflare Access logs** record every authenticated request through the tunnel, including the resolved Union identity, the destination service, and the response status.
- **Object store audit logs** (CloudTrail / Cloud Audit / Azure Storage) record every read and write. The principal on every payload-bearing access is a customer-controlled identity, never Union.
- **Kubernetes audit logs** on the data plane record cluster-internal accesses by the dataproxy.
- **Cloud Audit logs** on the data-plane cluster confirm the outbound-only tunnel connection pattern.

Customers can ingest all of the above into their own SIEM and assert on it without Union's cooperation.

### Presigned URLs

**Reviewer focus:** Confirm that presigned URLs point to the customer's object store, expire as documented, and are scoped to a single object.

**How to verify:**

1. Open the Union.ai UI and navigate to a completed task's outputs.
2. Open browser developer tools (Network tab) and observe the request when viewing output data.
3. The presigned URL should resolve to the customer's S3/GCS/Azure Blob domain (not a Union.ai domain), contain an expiry parameter, and reference a single object key.
4. Copy the presigned URL and wait 1 hour. Paste it into the browser. It should return a 403 (TTL expired).
5. Modify the object key in the URL and retry immediately. It should return a 403 (signature invalid, confirming single-object scope).

### End-to-end workflow

**Reviewer focus:** Confirm the data separation model at every workflow stage: customer data stays in the customer's infrastructure throughout the lifecycle.

**How to verify:**

**Step 1: Deployment and code bundle**

Run a workflow and observe where the code bundle is stored:

```bash
union run --remote my_task.py main
```

Verify that the code bundle is in the customer's bucket:

```bash
aws s3 ls s3://<customer-bucket>/org/project/domain/code-bundles/
```

The code bundle `.tgz` file should appear in the customer's own object store.

**Step 2: Execution**

Inspect the task pod to confirm it reads from customer infrastructure:

```bash
kubectl describe pod <task-pod> -n <workspace-namespace>
```

The pod description should show volumes mounted from customer S3, secrets from the customer's backend, and a non-root security context.

**Step 3: Retrieval**

Open browser developer tools (Network tab) and view the task's outputs in the Union.ai UI. Customer-data requests should resolve to either the per-cluster tunnel domain (for structured outputs, logs, K8s events) or directly to the customer's S3/GCS/Azure Blob endpoint (for binary artifacts). Confirm that the control plane API returns metadata and URI references only:

```bash
uctl get execution <execution-id> -o json
```

The response should contain phase, timestamps, URIs, and task definition fields. Bulk data content should not appear inline.

**Step 4: Negative proof**

Search control plane audit logs for the recognizable data string used in the workflow. It should not appear. If VPC Flow Logs are enabled, customer-data transfers should flow either directly between task pods and the customer's object store, or between clients and the per-cluster tunnel endpoint -- never between the data plane and Union's control plane endpoints.
