---
title: Compute and control plane components
weight: 4
variants: -flyte +union
mermaid: true
---

# Compute and control plane components

## Component architecture

All cross-plane traffic flows through the Cloudflare Tunnel -- an outbound-only, mTLS-encrypted connection initiated from the data plane. No inbound ports are opened on the customer's cluster.

```mermaid
graph TB
    subgraph CP["Control plane (Union.ai hosted — AWS)"]
        Admin["Admin<br/>(UI &amp; API gateway)"]
        QueueSvc["Queue Service<br/>(schedules TaskActions)"]
        StateSvc["State Service<br/>(receives state transitions)"]
        ClusterSvc["Cluster Service<br/>(cluster health &amp; DNS reconciliation)"]
        DataProxy["DataProxy<br/>(streaming relay for logs &amp; metrics)"]
    end

    subgraph Tunnel["Cloudflare Tunnel (outbound-only, mTLS)"]
        direction LR
        TunnelEdge(["Cloudflare edge"])
    end

    subgraph DP["Data plane (customer hosted — customer cloud account)"]
        TunnelSvc["Tunnel Service<br/>(maintains outbound tunnel connection)"]
        Executor["Executor<br/>(Kubernetes controller — runs task pods)"]
        ObjStore["Object Store Service<br/>(presigned URL generation)"]
        LogProvider["Log Provider<br/>(live K8s logs + cloud log aggregator)"]
        ImageBuilder["Image Builder<br/>(Buildkit — on-cluster image builds)"]

        subgraph Apps["Apps &amp; Serving"]
            Kourier["Kourier gateway<br/>(Envoy — auth + routing)"]
            Knative["Knative Services<br/>(app containers)"]
        end

        Executor -->|"submit and watch"| Pods["Task pods<br/>(customer workloads)"]
        Pods -->|"read/write via IAM"| ObjBucket[("Object store<br/>(metadata + fast-reg buckets)")]
        ObjStore -->|"signs URLs using admin IAM role"| ObjBucket
        LogProvider -->|"live: K8s API<br/>completed: CloudWatch / Cloud Logging / Azure Monitor"| Pods
        Kourier --> Knative
    end

    Admin -->|"ConnectRPC / HTTPS"| User(["Client<br/>(browser / CLI / SDK)"])
    User -->|"presigned URL — direct fetch"| ObjBucket

    CP <-->|"Cloudflare Tunnel"| TunnelEdge
    TunnelEdge <-->|"outbound-initiated from data plane"| TunnelSvc
    TunnelSvc --- Executor
    TunnelSvc --- ObjStore
    TunnelSvc --- LogProvider
    TunnelSvc --- Apps

    QueueSvc -->|"TaskAction"| Executor
    Executor -->|"state transitions (ConnectRPC)"| StateSvc
    LogProvider -->|"streamed relay — never persisted"| DataProxy
    ClusterSvc -->|"health checks &amp; DNS"| TunnelSvc
```

**Key relationships:**

| From | To | What flows |
| --- | --- | --- |
| Queue Service | Executor | TaskAction custom resources (orchestration instructions) |
| Executor | State Service | Phase transitions (Queued -> Running -> Succeeded/Failed) |
| Executor | Task pods | Pod lifecycle management |
| Task pods | Object store | Task inputs/outputs via IAM role (workload identity) |
| Object Store Service | Object store | Presigned URL generation using admin IAM role |
| Log Provider | DataProxy | Log streams relayed in memory -- optionally persisted on customer storage |
| Cluster Service | Tunnel Service | Health checks and DNS record reconciliation |
| Tunnel Service | Cloudflare edge | Single outbound-only mTLS connection covering all data-plane services |

## Executor

The Executor is a Kubernetes controller on the customer's data plane. It watches for `TaskAction` custom resources created by the Queue Service, reconciles each through its lifecycle (`Queued`, `Initializing`, `Running`, `Succeeded`/`Failed`), reports state transitions to the control plane's State Service via ConnectRPC through the tunnel, and creates Kubernetes pods for task execution.

The Executor accesses the customer's object store and secrets using IAM roles bound to its Kubernetes service account via workload identity federation. It communicates with external services only through the Cloudflare tunnel to the control plane.

## Apps and serving

Apps and Serving enables deployment of long-running web applications (Streamlit dashboards, FastAPI services, notebooks, inference endpoints) on the customer's data plane:

- Apps run as Knative Services within tenant-scoped Kubernetes namespaces, with the Union Operator managing lifecycle including autoscaling and scale-to-zero
- No application code, data, or serving traffic passes through the control plane
- Inbound traffic routes through Cloudflare for DDoS protection to a Kourier gateway (Union's Envoy fork) on the customer's cluster, which enforces authentication before forwarding to the app container
- Browser access uses SSO; programmatic access requires a Union API key. All endpoints require authentication by default, with optional per-app anonymous access.
- Union's RBAC controls which users can deploy and access apps per project, and resource quotas constrain consumption
- The load balancer, serving infrastructure, and app containers all run within the customer's cluster
- In BYOC, Union.ai manages the [serving infrastructure lifecycle](./deployment-models#infrastructure-management)

## Object store service

The Object Store Service runs on the data plane and provides presigned URL signing using the customer's IAM credentials (admin role):

- `CreateSignedURL` -- generates presigned URLs for object access
- `CreateUploadLocation` -- generates presigned `PUT` URLs for fast registration with `Content-MD5` integrity verification
- `Presign` -- generic presigning for arbitrary object store keys
- `Get`/`Put` -- direct object store read/write used internally by platform services

Two buckets are provisioned per cluster: a metadata bucket (task inputs, outputs, reports, intermediate data) and a fast-registration bucket (code bundles). Object layout follows `org/project/domain/run-name/action-name`, providing natural namespace isolation.

## Log provider

The Log Provider runs on the data plane and serves task logs from two sources: live logs streamed from the Kubernetes API (pod stdout/stderr) and completed task logs read from the cloud log aggregator (CloudWatch, Cloud Logging, or Azure Monitor). Union also supports persisting logs in object storage. Log lines include structured metadata (timestamp, message content, originator classification) enabling security teams to distinguish application-generated from platform-generated logs.

## Image builder

When enabled, the Image Builder runs on the data plane using Buildkit. It pulls base images from a customer-approved registry, accesses user code via a time-limited presigned URL, builds the container image with specified layers, and pushes to the customer's container registry. Source code and built images never leave the customer's infrastructure.

## Tunnel service

The Tunnel Service maintains the Cloudflare Tunnel connection. It initiates and maintains the outbound-only encrypted connection, performs periodic health checks and heartbeats, and reconnects automatically on network disruption. The Cluster Service on the control plane performs periodic reconciliation to ensure tunnel health and DNS records are current.
