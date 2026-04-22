---
title: Self-hosted deployment
weight: 6
variants: -flyte +union
sidebar_expanded: true
mermaid: true
---

# Self-hosted deployment

In a self-hosted deployment, you host both the **control plane** and the **data plane** in the same Kubernetes cluster. This gives you complete control over your {{< key product_name >}} installation with full data sovereignty.

> [!NOTE]
> Self-hosted deployment is distinct from [self-managed deployment](../selfmanaged/_index), where {{< key product_name >}} hosts the control plane and you manage only the data plane.

## When to use self-hosted deployment

Choose self-hosted deployment when:

- You need full control over both control plane and data plane
- You have strict data locality or sovereignty requirements
- You want to minimize network egress costs
- You are running in an air-gapped or restricted network environment

Choose [self-managed deployment](../selfmanaged/_index) when:

- You want {{< key product_name >}} to manage the control plane
- You need {{< key product_name >}}'s managed services and support
- Control plane and data plane are in separate clusters

## Architecture

In a self-hosted intra-cluster deployment, the control plane and data plane communicate using Kubernetes internal networking rather than external endpoints.

```mermaid
graph TB
    subgraph cluster["Kubernetes Cluster"]
        subgraph cp["Controlplane Namespace"]
            cpingress["NGINX Ingress\n(TLS/HTTP2)\nClusterIP"]
            admin["Admin"]
            identity["Identity"]
            services["Services"]

            cpingress --> admin
            cpingress --> identity
            cpingress --> services
        end

        subgraph dp["Dataplane Namespace"]
            dpingress["NGINX Ingress\nClusterIP"]
            operator["Operator"]
            propeller["Propeller"]
            clusterresource["Cluster Resource\nSync"]

            dpingress --> operator
            dpingress --> propeller
            dpingress --> clusterresource
        end

        subgraph external["External Resources"]
            db["PostgreSQL"]
            storage["Object Storage\n(S3 / GCS)"]
        end

        dpingress -.->|"Internal DNS"| cpingress
        cpingress -.->|"Internal DNS"| dpingress

        admin --> db
        identity --> db
        services --> db
        admin --> storage
        operator --> storage
    end
```

**Key characteristics:**

- **Simplified networking**: All communication stays within the cluster via Kubernetes DNS
- **No external dependencies**: No internet connectivity required for control plane to data plane communication
- **Cost-effective**: No network egress costs between control plane and data plane
- **Self-signed certificates**: Can use self-signed certificates for intra-cluster TLS
- **Single-tenant mode**: Simplified security model with explicit organization configuration

## Prerequisites

### Infrastructure

- **Kubernetes cluster** (>= 1.28.0) with sufficient resources for both control plane and data plane. Recommended: at least 6 nodes with 8 CPU / 16GB RAM each.
- **PostgreSQL database** (12+), either cloud-managed (RDS, Cloud SQL) or self-hosted.
- **Object storage** (S3 or GCS) for metadata and artifacts.
- **IAM roles** or **service accounts** configured for cloud resource access.

### Tools

- [Helm](https://helm.sh/docs/intro/install/) 3.18+
- `kubectl` configured to access your cluster
- `openssl` or `cert-manager` for TLS certificate generation

### Registry access

{{< key product_name >}} control plane images are hosted in a private registry. You will receive registry credentials from the {{< key product_name >}} team for your organization.

## Deployment guides

Deploy the control plane first, then the data plane.

{{< grid >}}

{{< link-card target="./control-plane-aws" icon="server" title="Control plane on AWS" >}}
Deploy the control plane with Amazon RDS and S3
{{< /link-card >}}

{{< link-card target="./control-plane-gcp" icon="server" title="Control plane on GCP (Preview)" >}}
Deploy the control plane with Cloud SQL and GCS
{{< /link-card >}}

{{< link-card target="./data-plane-aws" icon="cpu" title="Data plane on AWS" >}}
Deploy the data plane with S3 and IRSA
{{< /link-card >}}

{{< link-card target="./data-plane-gcp" icon="cpu" title="Data plane on GCP (Preview)" >}}
Deploy the data plane with GCS and Workload Identity
{{< /link-card >}}

{{< link-card target="./authentication" icon="lock" title="Authentication" >}}
Configure OIDC/OAuth2 authentication for your deployment
{{< /link-card >}}

{{< link-card target="./authorization" icon="shield" title="Authorization" >}}
Configure authorization mode (Noop, External, or Union built-in RBAC)
{{< /link-card >}}

{{< link-card target="./image-builder" icon="package" title="Image builder" >}}
Register the image builder for automatic container image builds
{{< /link-card >}}

{{< /grid >}}
