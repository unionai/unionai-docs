---
title: Component architecture
weight: 12
variants: -flyte +byoc +selfmanaged
mermaid: true
---

# Compute and control plane components reference

This section provides a detailed reference for each security-relevant component running on the compute plane and/or control plane.
Understanding these components is essential for enterprise security teams conducting architecture reviews.

## Component architecture

The diagram below shows the major components in both planes and how they communicate.
All cross-plane traffic flows through the Cloudflare Tunnel—an outbound-only, mTLS-encrypted connection initiated from the compute plane.
No inbound ports are opened on the customer’s cluster.

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

    subgraph DP["Compute plane (customer hosted — customer cloud account)"]
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
    TunnelEdge <-->|"outbound-initiated from compute plane"| TunnelSvc
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
| Executor | State Service | Phase transitions (Queued → Running → Succeeded/Failed) |
| Executor | Task pods | Pod lifecycle management |
| Task pods | Object store | Task inputs/outputs via IAM role (workload identity) |
| Object Store Service | Object store | Presigned URL generation using admin IAM role |
| Log Provider | DataProxy | Log streams relayed in memory — optionally persisted on customer storage |
| Cluster Service | Tunnel Service | Health checks and DNS record reconciliation |
| Tunnel Service | Cloudflare edge | Single outbound-only mTLS connection covering all compute-plane services |

## Executor

The Executor is a Kubernetes controller that runs on the customer’s compute plane.
It is the core component responsible for translating orchestration instructions into actual workload execution.
The Executor watches for `TaskAction` custom resources created by the Queue Service, reconciles each `TaskAction` through its lifecycle (`Queued`, `Initializing`, `Running`, `Succeeded`/`Failed`), reports state transitions back to the control plane’s State Service via `ConnectRPC` through the Cloudflare tunnel, and creates and manages Kubernetes pods for task execution.

The Executor runs entirely within the customer’s cluster.
It accesses the customer’s object store and secrets using IAM roles bound to its Kubernetes service account via workload identity federation.
At no point does the Executor communicate directly with external services outside the customer’s cloud account (except through the Cloudflare tunnel to the control plane).

## Apps and serving

- Apps and Serving enables customers to deploy long-running web applications — Streamlit dashboards, FastAPI services, notebooks, and inference endpoints — directly on the customer's compute plane.
- Apps run as Knative Services within tenant-scoped Kubernetes namespaces, with the Union Operator managing the full lifecycle including autoscaling and scale-to-zero.
- No application code, data, or serving traffic passes through the Union control plane.
- Inbound traffic routes through Cloudflare for DDoS protection to a Kourier gateway (Union's Envoy fork) running on the customer's cluster, which enforces authentication against the control plane before forwarding to the app container.
- Browser access uses SSO; programmatic access requires a Union API key.
- All endpoints require authentication by default, with optional per-app anonymous access.
- Union's RBAC controls which users can deploy and access apps per project, and resource quotas constrain consumption.
- The load balancer, serving infrastructure, and app containers all run within the customer's cluster, maintaining the same data residency guarantees as workflow execution.

## Object store service

The Object Store Service runs on the compute plane and provides the signing capabilities that enable the presigned URL security model.
Its key operations include:  
- `CreateSignedURL` (generates presigned URLs using the customer’s IAM credentials via the admin role). 
- `CreateUploadLocation` (generates presigned `PUT` URLs for fast registration with `Content-MD5` integrity verification)  
- `Presign` (generic presigning for arbitrary object store keys)  
- `Get`/`Put` (direct object store read/write used internally by platform services).

Two object store buckets are provisioned per compute plane cluster: a metadata bucket for task inputs, outputs, reports, and intermediate data, and a "fast-registration" bucket for code bundles uploaded during task registration.
Object layout follows a hierarchical pattern: org/project/domain/run-name/action-name, providing natural namespace isolation.

## Log provider

The Log Provider runs on the compute plane and serves task logs from two sources.
For live tasks, logs are streamed directly from the Kubernetes API (pod stdout/stderr) in real time.
For completed tasks, logs are read from the cloud log aggregator (CloudWatch, Cloud Logging, or Azure Monitor) after pod termination.
Union also supports persisting logs in object storage.
Log lines include structured metadata: timestamp, message content, and originator classification (user vs. system).
This structured approach enables security teams to distinguish between application-generated logs and platform-generated logs for audit purposes.

## Image builder

When enabled, the Image Builder runs on the compute plane and uses Buildkit to construct container images without exposing source code or built artifacts outside the customer’s infrastructure.
The build process pulls the base image from a customer-approved registry (public or private), accesses user code via a presigned URL with a limited time-to-live, builds the container image with specified layers (pip packages, apt packages, custom commands, UV/Poetry projects), and pushes the built image to the customer’s container registry (ECR, GCR, ACR, or others).
Source code and built images never leave the customer’s infrastructure during the build process.

## Tunnel service

The Tunnel Service maintains the Cloudflare Tunnel connection between the compute plane and control plane.
It is responsible for initiating and maintaining the outbound-only encrypted connection, performing periodic health checks and heartbeats, and reconnecting automatically in case of network disruption.
The Cluster Service on the control plane performs periodic reconciliation to ensure tunnel health and DNS records are current.
