---
title: Security architecture
weight: 2
variants: -flyte +byoc +selfmanaged
---

# Security architecture

Union.ai’s security architecture is founded on the principle of strict separation between orchestration (control plane) and execution (data plane).
This architectural decision ensures that customer data remains within the customer’s own cloud infrastructure at all times.

## Control plane / data plane separation

The control plane and data plane serve fundamentally different purposes and handle different types of data:

### Control plane (Union.ai-hosted)

The control plane is responsible for workflow orchestration, user management, and providing the web interface.
It runs within Union.ai’s AWS account and stores only orchestration metadata in a managed PostgreSQL database.
This metadata includes task definitions (image references, resource requirements, typed interfaces), run and action metadata (identifiers, phase, timestamps, error information), user identity and RBAC records, cluster configuration and health records, and trigger/schedule definitions.
The control plane never stores customer data payloads.
It stores only references (URIs) to data in the customer’s object store, no data.
When data must be surfaced to a client, the control plane either proxies a signing request to generate a presigned URL or relays a data stream from the data plane without persisting it.

**See comprehensive list of control plane roles and permissions in [Appendix C](./appendix#c-kubernetes-rbac---control-plane).**

### Data plane (customer-hosted)

The data plane runs inside the customer’s own cloud account on their own Kubernetes cluster.
All customer data resides here, including:

| Data Type | Storage Technology | Access Pattern |
| --- | --- | --- |
| Task inputs/outputs | Object Store (S3/GCS/Azure Blob) | Read/write by task pods via IAM roles |
| Code bundles (TGZ) | Object Store (fast-registration bucket) | Write via presigned URL; read by task pods |
| Container images | Container Registry (ECR/GCR/ACR) | Built on-cluster; pulled by K8s |
| Task logs | Cloud Log Aggregator + live K8s API | Streamed via tunnel (never stored in CP) |
| Secrets | K8s Secrets or Cloud Secrets Manager | Injected into pods at runtime |
| Observability metrics | ClickHouse (per-cluster) | Proxied queries via DataProxy |
| Reports (HTML) | Object Store | Accessed via presigned URL |
| Cluster events | K8s API (ephemeral) | Live from K8s API |

**See comprehensive list of data plane roles and permissions in [Appendix D](./appendix#d-kubernetes-rbac---data-plane)**

<!-- TODO: Add architecture diagram -->

## Network architecture

Network security is enforced through multiple layers:

### Cloudflare tunnel (outbound-only)

The data plane connects to the control plane via a Cloudflare Tunnel—an outbound-only encrypted connection initiated from the customer’s cluster.
This architecture provides several critical security benefits:

* No inbound firewall rules are required on the customer’s network
* The control plane cannot independently initiate connections to the data plane
* All traffic through the tunnel uses mutual TLS (mTLS) encryption
* The Tunnel Service performs periodic health checks and state reconciliation
* Connection is initiated outward to Cloudflare’s edge network, which then connects to the control plane

### Control plane tunnel (outbound-only)

The data plane reaches out to the control plane to establish a bi-directional, encrypted and authenticated, outbound-only tunnel.
Union.ai operates regional control plane endpoints:

| Area | Region | Endpoint |
| --- | --- | --- |
| US | us-east-2 | hosted.unionai.cloud |
| US | us-west-2 | us-west-2.unionai.cloud |
| Europe | eu-west-1 | eu-west-1.unionai.cloud |
| Europe | eu-west-2 | eu-west-2.unionai.cloud |
| Europe | eu-central-1 | eu-central-1.unionai.cloud |

In locked-down environments, networking teams can limit egress access to [published Cloudflare CIDR blocks](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/configure-tunnels/tunnel-with-firewall), and further restrict to specific regions in coordination with the Union networking team.

### Communication paths

| Communication Path | Protocol | Encryption |
| --- | --- | --- |
| Client → control plane | ConnectRPC (gRPC-Web) over HTTPS | TLS 1.2+ |
| Control plane ↔ data plane | Cloudflare Tunnel (outbound-initiated) | mTLS |
| Union → Customer EKS/GKE | AWS PrivateLink / GCP Private Service Connect | Private network (no Internet) |
| Client → Object Store (presigned URL) | HTTPS | TLS 1.2+ (cloud provider enforced) |
| Fluentbit → Log Aggregator | Cloud provider SDK | TLS (cloud-native) |
| Task Pods → Object Store | Cloud provider SDK | TLS (cloud-native) |

## Data flow architecture

Union.ai implements two primary data access patterns, both designed to keep customer data out of the control plane:

### Presigned URL pattern

For task inputs, outputs, code bundles, and reports, the control plane generates time-limited presigned URLs.
The client fetches data directly from the customer’s object store—the data never transits the control plane.
Presigned URLs are single-object scope, operation-specific (GET or PUT), time-limited (default 1 hour maximum), and transport-encrypted at every hop.

### Streaming relay pattern

For logs and observability metrics, the control plane acts as a stateless relay—streaming data from the data plane through the Cloudflare tunnel to the client in real time.
The data passes through the control plane’s memory as an encrypted stream but is never written to disk, cached, or stored.

<!-- TODO: Add data flow diagram (see /user-guide/run-scaling/life-of-a-run/#execution-flow-diagram) -->

The code bundle is directly uploaded to object store using signed URLs.

<!-- TODO: Add code bundle upload diagram -->
