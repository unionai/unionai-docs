---
title: Prepare infrastructure
weight: 1
variants: -flyte +union
---

# Prepare infrastructure

This page walks you through creating the resources needed for a Union data plane on Nebius Managed Kubernetes with Nebius Object Storage. If you already have these resources, skip to [Deploy the dataplane](../selfmanaged-nebius/deploy-dataplane).

## Nebius Managed Kubernetes cluster

You need a [Nebius Managed Kubernetes cluster](https://docs.nebius.com/kubernetes) running one of the most recent three minor Kubernetes versions, with `kubectl` access configured. See [Cluster Recommendations](../cluster-recommendations) for networking and node pool guidance.

GPU node groups should be provisioned ahead of time if you plan to run training or inference workloads. Nebius supports H100, H200, and B200 SKUs — confirm your tenant has quota in the [desired region](https://docs.nebius.com/overview/regions#public-regions).

For instructions on creating a node group, see [How to create node groups](https://docs.nebius.com/kubernetes/node-groups/manage#how-to-create-node-groups).

## Nebius Object Storage

Union uses S3-compatible object storage to store workflow data and artifacts. Nebius Object Storage is supported and exposes an S3-compatible API.

### Create a bucket

Create a bucket in the [Nebius Console](https://console.nebius.com/). Navigate to **Storage > Object Storage** and create a bucket in the same region as your MK8s cluster (to avoid egress costs and latency).

For detailed instructions, see [Create a bucket](https://docs.nebius.com/object-storage/buckets/manage#how-to-create-buckets).

### Generate access credentials

Nebius Object Storage uses a **service account + access key** pattern (similar to AWS IAM). Both the Union backend and the Pods created at execution time will need these credentials. Follow the steps in [How to get started with Nebius Object Storage](https://docs.nebius.com/object-storage/quickstart#configure-access-credentials-and-aws-cli-settings) to obtain access credentials.
