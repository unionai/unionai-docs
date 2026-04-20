---
title: Security architecture
weight: 1
variants: -flyte +union
---

# Security architecture

Union.ai’s security architecture is founded on the principle of strict separation between orchestration (control plane) and execution (data plane).
This architectural decision ensures that customer data remains within the customer’s own cloud infrastructure at all times.

## Control plane / data plane separation

The control plane and data plane serve fundamentally different purposes and handle different types of data:

### Control plane (Union.ai hosted)

The control plane is responsible for workflow orchestration, user management, and providing the web interface.
It runs within Union.ai’s AWS account and stores only orchestration metadata in a managed PostgreSQL database.
This metadata includes task definitions (image references, resource requirements, typed interfaces), run and action metadata (identifiers, phase, timestamps, error information), user identity and RBAC records, cluster configuration and health records, and trigger/schedule definitions.
The control plane never stores customer data payloads.
It stores only references (URIs) to data in the customer’s object store, no data.
When data must be surfaced to a client, the control plane either proxies a signing request to generate a presigned URL or relays a data stream from the data plane without persisting it.

**See comprehensive list of control plane roles and permissions in [Kubernetes RBAC: control plane](./kubernetes-rbac-control-plane).**

### Data plane (customer hosted)

The data plane runs inside the customer’s own cloud account on their own Kubernetes cluster.
All customer data resides here, including:

| Data Type | Storage Technology | Access Pattern |
| --- | --- | --- |
| Task inputs/outputs | Object Store | Read/write by task pods via IAM roles |
| Code bundles (TGZ) | Object Store (fast-registration bucket) | Write via presigned URL; read by task pods and presigned URL by the browser |
| Container images | Container Registry | Built on-cluster; pulled by K8s |
| Task logs | Cloud Log Aggregator + live K8s API | Streamed via tunnel (never stored in CP) |
| Secrets | K8s Secrets, Vault, or Cloud Secrets Manager | Injected into pods at runtime |
| Observability metrics | Prometheus (in-cluster / customer managed) | Proxied queries via DataProxy |
| Reports (HTML) | Object Store (S3/GCS/Azure Blob) | Accessed by the browser via presigned URL |
| Cluster events | K8s API (ephemeral) | Live from K8s API |

**See comprehensive list of data plane roles and permissions in [Kubernetes RBAC: data plane](./kubernetes-rbac-data-plane).**

## Network architecture

Network security is enforced through multiple layers:

![Network security](../_static/images/security/network-security.png)

> [!NOTE]
> In BYOC deployments, Union.ai additionally maintains a private management connection to the customer's K8s cluster. See [BYOC deployment differences: Network architecture](./byoc-differences#network-architecture) for details.

### Cloudflare tunnel (outbound-only)

The data plane connects to the control plane via a Cloudflare Tunnel—an outbound-only encrypted connection initiated from the customer’s cluster.
This architecture provides several critical security benefits:

* No inbound firewall rules are required on the customer’s network
* All traffic through the tunnel uses mutual TLS (mTLS) encryption
* The Tunnel Service performs periodic health checks and state reconciliation
* Connection is initiated outward to Cloudflare’s edge network, from the data plane, which then connects to the control plane

### Control plane tunnel (outbound only)

The data plane reaches out to the control plane to establish a bidirectional, encrypted and authenticated, outbound-only tunnel.
Union.ai operates regional control plane endpoints:

| Area | Region | Endpoint |
| --- | --- | --- |
| US | us-east-2 | hosted.unionai.cloud |
| US | us-west-2 | us-west-2.unionai.cloud |
| Europe | eu-west-1 | eu-west-1.unionai.cloud |
| Europe | eu-west-2 | eu-west-2.unionai.cloud |
| Europe | eu-central-1 | eu-central-1.unionai.cloud |

In locked-down environments, networking teams can limit egress access to published Cloudflare CIDR blocks, and further restrict to specific regions in coordination with the Union networking team.

### Communication paths

| Communication Path | Protocol | Encryption |
| --- | --- | --- |
| Client → Control Plane | ConnectRPC (gRPC-Web) over HTTPS | TLS 1.2+ |
| Control Plane ↔ Data Plane | Cloudflare Tunnel (outbound-initiated) | mTLS |
| Client → Object Store (presigned URL) | HTTPS | TLS 1.2+ (cloud provider enforced) |
| Fluent Bit → Log Aggregator | Cloud provider SDK | TLS (cloud-native) |
| Task Pods → Object Store | Cloud provider SDK | TLS (cloud-native) |

> [!NOTE]
> BYOC deployments add a PrivateLink/PSC management path between Union.ai and the customer's K8s API. See [BYOC deployment differences: Network architecture](./byoc-differences#network-architecture).

## Data flow architecture

Union.ai implements two primary data access patterns, both designed to keep customer data out of the control plane:

### Presigned URL pattern

For task inputs, outputs, code bundles, and reports, the control plane proxies signing requests to the data plane, which generates time-limited presigned URLs using customer-managed credentials.
The client fetches data directly from the customer’s object store—the data never transits the control plane.
Presigned URLs generated on the data plane are single-object scope, operation-specific (GET or PUT), time-limited (default 1 hour maximum), and transport-encrypted at every hop.

Union.ai applies several controls:

* **TTL enforcement** — URLs expire after a configurable window (default 1 hour, configurable shorter)
* **Single-object scope** — each URL grants access to exactly one object, not a bucket or prefix
* **Operation specificity** — each URL is locked to a single operation (GET or PUT)
* **Transport encryption** — URLs are transmitted only over TLS-encrypted channels
* **No URL logging** — presigned URLs are not persisted in control plane logs or databases

Organizations with stricter requirements can configure shorter TTLs. The presigned URL model was chosen because it eliminates the need for the control plane to hold persistent cloud IAM credentials, which would represent a larger and more persistent attack surface than time-limited bearer URLs.

### Streaming relay pattern

For logs and observability metrics, the control plane acts as a stateless relay—streaming data from the data plane through the Cloudflare tunnel to the client in real time.
The data passes through the control plane’s memory as a TLS encrypted stream with a termination point in the cloud.
It is never written to disk, cached, or stored.

### Execution flow diagram

![Execution flow](../_static/images/security/execution-flow.png)

### Data in the UI

| Field | What is it? | Where is it stored? | How is it retrieved? |
| --- | --- | --- | --- |
| Task names | Python function and module names | Control Plane | CP API |
| Users’ names | First and last names of users on the platform | IDP | Cached in memory in CP, otherwise retrieved directly from IDP |
| Inputs/Outputs | Primitive inputs/outputs returned by tasks (e.g. return 5) | Dataplane’s S3 bucket | Cloudflare Tunnel |
| Logs | Runtime logs written by the task code/SDK | Dataplane K8s for live logs, dataplane S3/Cloudwatch/Stackdriver for persistent logs | Cloudflare Tunnel |
| K8s Events | Pod autoscaling events explaining whether a node is found or the cluster needs to scale up… etc. | Dataplane K8s | Cloudflare Tunnel |
| Report | Reports produced by the task code in HTML | Dataplane’s S3 bucket | A signed URL is generated through the tunnel, then the browser renders it in iframe |
| Code explorer | Code bundled when the task was kicked off, that contains the task code and surrounding dependencies/functions it calls| Dataplane’s S3 bucket | A signed URL is generated through the tunnel, then JS in the browser downloads and unzips the bundle to render |
| Timeline timestamps | Showing when did a task start, when it moved from queued to running to completed | Control Plane | CP API |
| Errors | Showing the failure message written into stderr or raised exceptions for a task attempt | Control Plane | CP API |
