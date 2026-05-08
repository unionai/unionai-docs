---
title: Prepare infrastructure
weight: 1
variants: -flyte +union
---

# Prepare infrastructure

This page walks you through creating the resources needed for a Union data plane on CoreWeave Kubernetes Service (CKS) with [CoreWeave AI Object Storage](https://docs.coreweave.com/products/storage/object-storage). If you already have these resources, skip to [Deploy the dataplane](../selfmanaged-coreweave/deploy-dataplane).

## CKS cluster

You need a [CKS cluster](https://docs.coreweave.com/products/cks/clusters/introduction) running one of the most recent three minor Kubernetes versions, with `kubectl` access configured. See [Cluster Recommendations](../cluster-recommendations) for networking and node pool guidance.

For instructions on creating a cluster, see [Create a CKS cluster](https://docs.coreweave.com/products/cks/clusters/create).

## CoreWeave AI Object Storage

Union uses S3-compatible object storage to store workflow data and artifacts. CoreWeave AI Object Storage is supported, but requires virtual-hosted style S3 URLs (the default Union configuration uses path-style URLs, which CoreWeave doesn't support — you'll set the relevant overrides during deployment).

### Create a bucket

Create a bucket in the [CoreWeave Cloud Console](https://console.coreweave.com/). Navigate to **Storage > Object Storage** and create a bucket in your desired Availability Zone.

For detailed instructions, see [Create a bucket](https://docs.coreweave.com/products/storage/object-storage/buckets/create-bucket).

### Generate access credentials

Navigate to **Administration > Object Storage Access Keys** in the Cloud Console and create an access key pair. Record the **Access Key ID** and **Secret Key** for use during deployment.

You need this key pair so the Helm values and workload environment variables can authenticate to your bucket.

For detailed instructions, see [Create access keys](https://docs.coreweave.com/products/storage/object-storage/auth-access/manage-access-keys/create-keys).

### Create an access policy

Create an organization access policy that grants your access key permissions on the bucket. Navigate to **Administration > Policies > Object Storage Access** in the Cloud Console and create a policy with the following JSON. Replace `<BUCKET_NAME>` with the name of your bucket.

```json
{
  "policy": {
    "version": "v1alpha1",
    "name": "union-ai-bucket-access",
    "statements": [
      {
        "name": "allow-union-s3-access",
        "effect": "Allow",
        "actions": ["s3:*"],
        "resources": [
          "<BUCKET_NAME>",
          "<BUCKET_NAME>/*"
        ],
        "principals": ["*"]
      }
    ]
  }
}
```

For detailed instructions on creating and managing policies, see [Organization access policies](https://docs.coreweave.com/products/storage/object-storage/auth-access/organization-policies/about).

> [!WARNING]
> Without an access policy, API operations return `403 Forbidden` errors even with valid access keys.
