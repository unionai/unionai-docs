---
title: Self-hosted deployment
weight: 6
variants: -flyte +union
sidebar_expanded: true
mermaid: true
---

# Self-hosted deployment

In a self-hosted deployment, you host both the **control plane** and the **data plane**. You choose the topology that fits your operational and regulatory requirements — both planes in a single Kubernetes cluster, in separate clusters, in different regions, or any combination. {{< key product_name >}} gives you complete control over the installation with full data sovereignty.

> [!NOTE]
> Self-hosted deployment is distinct from [self-managed deployment](../selfmanaged/_index), where {{< key product_name >}} hosts the control plane and you manage only the data plane.

## When to use self-hosted deployment

Choose self-hosted deployment when:

- You need full control over both control plane and data plane
- You have strict data locality or sovereignty requirements
- You want to minimize network egress costs
- You are running in an air-gapped or restricted network environment
- You need to colocate the control plane with the data plane for latency, isolation, or regulatory reasons

Choose [self-managed deployment](../selfmanaged/_index) when:

- You want {{< key product_name >}} to manage the control plane
- You need {{< key product_name >}}'s managed services and support

## Topologies

Self-hosted deployments support two topologies, distinguished by how the control plane and data plane are placed relative to each other:

- **Separate-cluster (default and recommended)** — control plane in one Kubernetes cluster, one or more data planes in separate clusters (often per environment, region, or business unit). Communication is via the control plane's external ingress; each data plane authenticates to the CP as a workload identity. Data planes may run on different cloud providers than the CP. This is the topology [Infrastructure requirements](./infrastructure-requirements) is written around.
- **Intra-cluster (special case)** — both planes in the same Kubernetes cluster, communicating over internal DNS. The simplest topology; used by the [Getting started](./getting-started) walkthrough and for footprint-constrained or evaluation deployments. The chart ships `values.{aws,gcp}.selfhosted-intracluster.yaml` for this case. See [Infrastructure requirements → Intra-cluster topology](./infrastructure-requirements#intra-cluster-topology) for the differences from separate-cluster.

The architecture diagram below shows the intra-cluster topology — the simplest layout to visualize. Separate-cluster uses the same chart components in different cluster boundaries.

## Architecture

In an intra-cluster deployment, the control plane and data plane communicate using Kubernetes internal networking rather than external endpoints.

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

## Deployment guides

Start with [Getting started](./getting-started) for an end-to-end walkthrough. Review [Infrastructure requirements](./infrastructure-requirements) before provisioning your cloud substrate. The remaining pages cover individual deployment components in depth.

{{< grid >}}

{{< link-card target="./getting-started" icon="play" title="Getting started" >}}
End-to-end walkthrough: provision, install, configure, smoke test
{{< /link-card >}}

{{< link-card target="./infrastructure-requirements" icon="layers" title="Infrastructure requirements" >}}
What to provision — substrate, CP and DP sizing, scaling constraints, topology choice
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

{{< link-card target="./operations" icon="settings" title="Operations" >}}
Operational guides: CI/CD integration, key rotation, and more
{{< /link-card >}}

{{< /grid >}}
