---
title: Cluster Recommendations
weight: 2
variants: -flyte +union
---

# Cluster recommendations

{{< key product_name >}} is capable of running on any Kubernetes cluster.
This includes managed Kubernetes services such as Google Kubernetes Engine (GKE), Azure Kubernetes Service (AKS), and Amazon Elastic Kubernetes Service (EKS), as well as self-managed Kubernetes clusters.

While many configurations are supported, we have some recommendations to ensure the best performance and reliability of your Union deployment.

## Kubernetes Versions

We recommend running Kubernetes versions that are [actively supported by the Kubernetes community](https://kubernetes.io/releases/).  This
typically means running one of the most recent three minor versions.  For example, if the most recent version is 1.32, we recommend
running 1.32, 1.31, or 1.30.

## Networking Requirements

Many Container Network Interface (CNI) plugins require planning for IP address allocation capacity.
For example, [Amazon's VPC CNI](https://docs.aws.amazon.com/eks/latest/userguide/managing-vpc-cni.html) and [GKE's Dataplane v2](https://cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2)
allocate IP addresses to Kubernetes Pods out of one or more of your VPC's subnets.
If you are using one of these CNI plugins, you should ensure that your VPC's subnets have enough available IP addresses to support the number of concurrent tasks you expect to run.

### VPC and subnet sizing

We recommend using at least a `/16` CIDR range (65,536 addresses) for the overall VPC. Within that range, size your subnets according to their role:

| Subnet type | Recommended size | Purpose |
|-------------|-----------------|---------|
| **Private subnets** (worker nodes) | `/18` per AZ (16,384 addresses) | Pods receive IPs from these subnets. Size for your peak concurrent task count — each running task pod consumes at least one IP. |
| **Public subnets** (load balancers) | `/24` per AZ (256 addresses) | Only needed for internet-facing load balancers and NAT Gateways. Minimal IP consumption. |

As a rule of thumb, you should have at least 1 available IP address for each task you expect to run concurrently.

### Public vs. private subnets

We recommend running worker nodes in **private subnets** (no direct internet ingress). This is the default for managed Kubernetes services like EKS, GKE, and AKS. Public subnets are only needed for internet-facing load balancers or bastion hosts.

A typical layout per availability zone:

```
VPC (/16)
├── Public subnet  (/24) — NAT Gateway, load balancers
└── Private subnet (/18) — Worker nodes, pods
```

### NAT Gateway requirements

Worker nodes in private subnets need outbound internet access to pull container images from public registries (e.g. Docker Hub, ECR Public, ghcr.io) and to communicate with the Union control plane. This requires a **NAT Gateway** (or equivalent) in each availability zone's public subnet.

| Cloud | Service | Notes |
|-------|---------|-------|
| AWS | [NAT Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) | One per AZ for high availability. `eksctl` creates these automatically with the `--managed` flag. |
| GCP | [Cloud NAT](https://cloud.google.com/nat/docs/overview) | Attach to the Cloud Router for your VPC. Private GKE clusters require this. |
| Azure | [NAT Gateway](https://learn.microsoft.com/en-us/azure/nat-gateway/nat-overview) | Associate with the AKS subnet. Alternatively, AKS `outboundType: loadBalancer` (default) provides outbound access via the LB. |

> [!NOTE] If you use a fully private cluster with no outbound internet access, you must configure private endpoints or mirrors for all container registries and the Union control plane.

## Service accounts

The {{< key product_name >}} data plane uses a single Kubernetes service account, `union-system`, shared by all platform components (operator, executor, webhook, proxy, and FluentBit). This service account needs cloud provider credentials to access:

- **Object storage** (S3, GCS, or Azure Blob Storage) — read/write workflow execution data (task inputs/outputs, bundled code -in fast registration bucket-).
- **Container registry** (ECR, Artifact Registry, or ACR) — pull task container images; push images when Image Builder is enabled.

See the cloud-specific setup pages for details on configuring this service account:
[AWS](./selfmanaged-aws/_index), [GCP](./selfmanaged-gcp/_index), [Azure](./selfmanaged-azure/_index).

> [!NOTE] Common service account
> In previous versions, each component had its own service account. The consolidated `union-system` service account simplifies IAM configuration — you only need to bind cloud permissions to a single identity.

# Performance Recommendations

## Node Pools

It is recommended but not required to use separate node pools for the Union services and the Union worker pods.  This allows you to
guard against resource contention between Union services and other tasks running in your cluster.  You can find additional information
in the [Configuring Node Pools](./configuration/node-pools) section.

By default, the Union installation request the following resources:

|          | CPU (vCPUs)| Memory (GiB) |
|----------|------------|--------------|
| Requests |          14|          27.1|
| Limits   |          17|            32|

For GPU access, Union injects tolerations and label selectors to execution Pods.
