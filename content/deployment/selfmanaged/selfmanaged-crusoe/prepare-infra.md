---
title: Prepare infrastructure
weight: 1
variants: -flyte +union
---

# Prepare infrastructure

This page walks you through creating the resources needed for a Union data plane on [Crusoe Managed Kubernetes (CMK)](https://docs.crusoecloud.com/kubernetes/overview/) with [Crusoe Cloud Storage](https://docs.crusoecloud.com/storage/object-storage/overview). If you already have these resources, skip to [Deploy the dataplane](../selfmanaged-crusoe/deploy-dataplane).

## CMK cluster

You need a [CMK cluster](https://docs.crusoecloud.com/kubernetes/overview/) running one of the most recent three minor Kubernetes versions, with `kubectl` access configured. See [Cluster Recommendations](../cluster-recommendations) for networking and node pool guidance.

For instructions on creating a cluster, see [Create a CMK cluster](https://docs.crusoecloud.com/kubernetes/cluster-creation) <!-- [VERIFY link] -->.

> [!NOTE] Tip
> Crusoe's GPU node pools (H100, H200, A100, L40S) map directly to Union task resource requests via standard Kubernetes node selectors and tolerations. We recommend a separate CPU node pool for the Union operator and system pods.

## Crusoe Cloud Storage

Union uses S3-compatible object storage to store workflow data and artifacts. Crusoe Cloud Storage is supported and is S3-compatible.

<!-- [VERIFY: confirm whether Crusoe requires virtual-hosted or path-style URLs — adjust the disable_force_path_style flag accordingly.] -->

### Create a bucket

Create a bucket in the [Crusoe Cloud Console](https://console.crusoecloud.com/). Navigate to **Storage > Object Storage** and create a bucket in your desired region (e.g., `us-northcentral1-a`) <!-- [VERIFY region naming] -->.

For detailed instructions, see [Create a bucket](https://docs.crusoecloud.com/storage/object-storage/create-bucket) <!-- [VERIFY link] -->.

### Generate access credentials

In the Crusoe Cloud Console, navigate to **Identity & Access > Access Keys** <!-- [VERIFY path] --> and create an access key pair. Record the **Access Key ID** and **Secret Access Key** for use during deployment.

You need this key pair so the Helm values and workload environment variables can authenticate to your bucket.

### Create an IAM / access policy

Create a policy that grants your access key permissions on the bucket. Replace `<BUCKET_NAME>` with the name of your bucket.

<!-- [VERIFY: confirm Crusoe's policy syntax — the snippet below assumes standard S3-style IAM JSON. Crusoe may use a different policy schema.] -->

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowUnionS3Access",
      "Effect": "Allow",
      "Action": ["s3:*"],
      "Resource": [
        "arn:aws:s3:::<BUCKET_NAME>",
        "arn:aws:s3:::<BUCKET_NAME>/*"
      ]
    }
  ]
}
```

> [!WARNING]
> Without an access policy, API operations return `403 Forbidden` errors even with valid access keys.
