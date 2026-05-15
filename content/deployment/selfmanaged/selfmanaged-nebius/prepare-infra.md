---
title: Prepare infrastructure
weight: 1
variants: -flyte +union
---

# Prepare infrastructure

This page walks you through creating the resources needed for a Union data plane on Nebius Managed Kubernetes with Nebius Object Storage. If you already have these resources, skip to [Deploy the dataplane](../selfmanaged-nebius/deploy-dataplane).

## Nebius Managed Kubernetes cluster

You need a [Nebius Managed Kubernetes cluster](https://docs.nebius.com/kubernetes) running one of the most recent three minor Kubernetes versions, with `kubectl` access configured. See [Cluster Recommendations](../cluster-recommendations) for networking and node pool guidance.

GPU node groups should be provisioned ahead of time if you plan to run training or inference workloads. Nebius supports H100, H200, and B200 SKUs — confirm your tenant has quota in the desired region (`eu-north1`, `eu-west1`, or `us-central1`). <!-- [VERIFY regions] -->

For instructions on creating a cluster, see [Create a Managed Kubernetes cluster](https://docs.nebius.com/kubernetes/clusters/create).

## Nebius Object Storage

Union uses S3-compatible object storage to store workflow data and artifacts. Nebius Object Storage is supported and exposes an S3-compatible API.

### Create a bucket

Create a bucket in the [Nebius Console](https://console.nebius.com/). Navigate to **Storage > Object Storage** and create a bucket in the same region as your MK8s cluster (to avoid egress costs and latency).

For detailed instructions, see [Create a bucket](https://docs.nebius.com/object-storage/operations/buckets/create).

### Generate access credentials

Nebius Object Storage uses a **service account + access key** pattern (similar to AWS IAM):

1. Navigate to **IAM > Service Accounts** and create a service account (e.g., `union-dataplane-sa`).
2. Assign the service account the `storage.editor` role (or a custom role scoped to the bucket). <!-- [VERIFY role name] -->
3. Navigate to the service account's **Access Keys** tab and create a static access key. Record the **Access Key ID** and **Secret Key** for use during deployment.

You need this key pair so the Helm values and workload environment variables can authenticate to your bucket.

For detailed instructions, see [Manage access keys](https://docs.nebius.com/iam/service-accounts/access-keys). <!-- [VERIFY link] -->

### Confirm bucket permissions

Verify the service account can read and write to the bucket using the AWS CLI with the Nebius endpoint:

```bash
aws --endpoint-url=https://storage.eu-north1.nebius.cloud \
  s3 ls s3://<BUCKET_NAME>/
```

> [!WARNING]
> Without the proper role binding, API operations return `403 Forbidden` errors even with valid access keys.
