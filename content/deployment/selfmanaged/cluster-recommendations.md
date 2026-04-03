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
allocate IP addresses to Kubernetes Pods out of one or more or your VPC's subnets.
If you are using one of these CNI plugins, you should ensure that your VPC's subnets have enough available IP addresses to support the number of concurrent tasks you expect to run.

We recommend using at least a `/16` CIDR range (65,536 addresses), you may optionally subdivide this range into smaller subnets to
support multiple availability zones or other network segmentation requirements.

In short, you should aim to have at least 1 IP address available for each task you expect to run concurrently.

## Service accounts

The {{< key product_name >}} data plane uses a single Kubernetes service account, `union-system`, shared by all platform components (operator, executor, webhook, proxy, and FluentBit). This service account needs cloud provider credentials to access:

- **Object storage** (S3, GCS, or Azure Blob Storage) — read/write workflow execution data (task inputs/outputs, fast registration artifacts).
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
