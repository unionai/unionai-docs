---
title: Data flow architecture
weight: 3
variants: -flyte +union
---

# Data flow architecture

Union.ai implements two primary data access patterns, both designed to keep customer data out of the control plane.

## Presigned URL pattern

For task inputs, outputs, code bundles, and reports, the control plane proxies signing requests to the data plane, which generates time-limited presigned URLs using customer-managed credentials.
The client fetches data directly from the customer's object store -- the data never transits the control plane.
Presigned URLs generated on the data plane are single-object scope, operation-specific (GET or PUT), time-limited (default 1 hour maximum), and transport-encrypted at every hop.

Union.ai applies several controls:

* **TTL enforcement** -- URLs expire after a configurable window (default 1 hour, configurable shorter)
* **Single-object scope** -- each URL grants access to exactly one object, not a bucket or prefix
* **Operation specificity** -- each URL is locked to a single operation (GET or PUT)
* **Transport encryption** -- URLs are transmitted only over TLS-encrypted channels
* **No URL logging** -- presigned URLs are not persisted in control plane logs or databases

Organizations with stricter requirements can configure shorter TTLs. The presigned URL model was chosen because it eliminates the need for the control plane to hold persistent cloud IAM credentials, which would represent a larger and more persistent attack surface than time-limited bearer URLs.

### Presigned URL data types

| Data Type | Access Method | Direction |
| --- | --- | --- |
| Task inputs/outputs | Presign via ObjectStore service | Download (GET) |
| Code bundles (TGZ) | CreateDownloadLinkV2 | Download (GET) |
| Reports (HTML) | CreateDownloadLinkV2 | Download (GET) |
| Fast registration uploads | CreateUploadLocation | Upload (PUT) |

## Streaming relay pattern

For logs and observability metrics, the control plane acts as a stateless relay -- streaming data from the data plane through the Cloudflare tunnel to the client in real time.
The data passes through the control plane's memory as a TLS encrypted stream with a termination point in the cloud.
It is never written to disk, cached, or stored.

## Execution flow diagram

![Execution flow](../../_static/images/security/execution-flow.png)

## Data in the UI

| Field | What is it? | Where is it stored? | How is it retrieved? |
| --- | --- | --- | --- |
| Task names | Python function and module names | Control Plane | CP API |
| Users' names | First and last names of users on the platform | IDP | Cached in memory in CP, otherwise retrieved directly from IDP |
| Inputs/Outputs | Primitive inputs/outputs returned by tasks (e.g. return 5) | Dataplane's S3 bucket | Cloudflare Tunnel |
| Logs | Runtime logs written by the task code/SDK | Dataplane K8s for live logs, dataplane S3/Cloudwatch/Stackdriver for persistent logs | Cloudflare Tunnel |
| K8s Events | Pod autoscaling events explaining whether a node is found or the cluster needs to scale up... etc. | Dataplane K8s | Cloudflare Tunnel |
| Report | Reports produced by the task code in HTML | Dataplane's S3 bucket | A signed URL is generated through the tunnel, then the browser renders it in iframe |
| Code explorer | Code bundled when the task was kicked off, that contains the task code and surrounding dependencies/functions it calls| Dataplane's S3 bucket | A signed URL is generated through the tunnel, then JS in the browser downloads and unzips the bundle to render |
| Timeline timestamps | Showing when did a task start, when it moved from queued to running to completed | Control Plane | CP API |
| Errors | Showing the failure message written into stderr or raised exceptions for a task attempt | Control Plane | CP API |

## Data residency summary

| Data | Stored In | Accessed Via | Transits Control Plane? |
| --- | --- | --- | --- |
| Task definitions (spec metadata) | Control plane DB | ConnectRPC | Yes -- metadata only |
| Run metadata (phase, timestamps) | Control plane DB | ConnectRPC | Yes |
| Action metadata (phase, attempts) | Control plane DB | ConnectRPC | Yes |
| Task inputs/outputs | Customer object store | Presigned URL | No -- direct client <-> object store |
| Code bundles | Customer object store | Presigned URL | No -- direct client <-> object store |
| Reports (HTML) | Customer object store | Presigned URL | No -- direct client <-> object store |
| Container images | Customer container registry | Pulled by K8s | No -- stays in customer infra |
| Task logs | Customer log aggregator | Streamed via tunnel | Relayed in-memory (not stored) |
| Secrets | Customer secrets backend | Injected at runtime | Relayed during create (not stored) |
| Observability metrics | Customer ClickHouse | Proxied via DataProxy | Relayed in-memory (not stored) |
| User identity / RBAC | Control plane DB | ConnectRPC | Yes |
| Cluster state | Control plane DB | Internal | Yes |
