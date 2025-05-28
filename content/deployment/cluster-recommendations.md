---
title: Cluster Recommendations
weight: 2
variants: -flyte -serverless -byoc +selfmanaged
---

# Cluster recommendations

{{< key product_name >}} is capable of running on any Kubernetes cluster.  This includes managed Kubernetes services such as Google Kubernetes Engine (GKE), Azure Kubernetes Service (AKS), and Amazon Elastic Kubernetes Service (EKS), as well as self-managed Kubernetes clusters.

While many configurations are supported, we have some recommendations to ensure the best performance and reliability of your Union deployment.

## Kubernetes Versions

We recommend running Kubernetes versions that are [actively supported by the Kubernetes community](https://kubernetes.io/releases/).  This
typically means running one of the most recent three minor versions.  For example, if the most recent version is 1.32, we recommend
running 1.32, 1.31, or 1.30.

## Networking Requirements

Many Container Network Interface (CNI) plugins require planning for IP address allocation capacity.  For example, [Amazon's VPC CNI](https://docs.aws.amazon.com/eks/latest/userguide/managing-vpc-cni.html) and [GKE's Dataplane v2](https://cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2)
allocate IP addresses to Kubernetes Pods out of one or more or your VPC's subnets.  If you are using one of these CNI plugins, you should
ensure that your VPC's subnets have enough available IP addresses to support the number of concurrent tasks you expect to run.

We recommend using at least a `/16` CIDR range (65,536 addresses), you may optionally sub-divide this range into smaller subnets to
support multiple availability zones or other network segmentation requirements.

In short, you should aim to have at least 1 IP address available for each task you expect to run concurrently.

# Performance Recommendations

## Node Pools

It is recommended but not required to use separate node pools for the Union services and the Union worker pods.  This allows you to
guard against resource contention between Union services and other tasks running in your cluster.  You can find additional information
in the [Configuring Node Pools](./configuration/node-pools.md) section.

# AWS

## S3
Each data plane uses an object store (an AWS S3 bucket, GCS bucket or ABS container) that is used to store data used in the execution of workflows.
As a {{< key product_name >}} administrator, you can specify retention policies for this data when setting up your data plane (learn more [about the different types of data categories](./data-retention-policy.md#data-categories) stored by the data plane.)

Union recommends the use of two S3 buckets
1. metadata bucket: contains workflow execution data such as Task inputs and outputs, etc
2. fast registration bucket: contain local code artifacts that will be copied into the Flyte task container at runtime when using `union register` or `union run --remote --copy-all`.

Note: You can choose to use a single bucket in your dataplane

### Data Retention
Union recommends using Lifecycle Policy on these buckets to manage the storage costs. See [Data retention policy](./data-retention-policy.md#data-retention-policy) for more information.


## IAM
You will need to enable access to your S3 buckets from the cluster.

1. Update the EKS Node IAM role for your cluster to allow the data plane nodes to use your S3 buckets. This can be done by creating and attaching a new IAM policy which enables access to your S3 buckets. Use `union-flyte-worker` as the name of the new policy. The permissions for the policy will be:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Action": [
                "s3:DeleteObject*",
                "s3:GetObject*",
                "s3:ListBucket",
                "s3:PutObject*"
            ],
            "Resource": [
                "arn:aws:s3:::<bucket-name>",
                "arn:aws:s3:::<bucket-name>/*"
            ]
        }
    ]
}
```

2. Attach this policy to your node group IAM role
3. Create an [IAM OIDC provider for your EKS cluster](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html#_create_oidc_provider_eksctl).
4. Create a new role named `union-flyte-role` to enable applications in a Pod’s containers to make API requests to AWS services using AWS Identity and Access Management (IAM) permissions.

The Trust Policy for this role will be:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::$account_id:oidc-provider/$oidc_provider"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringLike": {
                    "$oidc_provider:aud": "sts.amazonaws.com",
                    "$oidc_provider:sub": "system:serviceaccount:*:*"
                }
            }
        }
    ]
}
```
where `$account_id` is your AWS account ID and `$oidc_provider` is the OIDC provider you created above.

NOTE: You can obtain these values using the AWS CLI:
```bash
aws eks describe-cluster --region $cloud_region --name $cluster_name --query "cluster.identity.oidc.issuer" --output text
```
5. Attach the `union-flyte-worker` policy created above to this new role.


## EKS configuration
Union recommends installing the following EKS add-ons:
  - CoreDNS
  - Amazon VPC CNI
  - Kube-proxy

Union supports Autoscaling and the use of spot (interruptible) instances.

# AKS

## Secure access

Union recommends using [Microsoft Entra Workload ID](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview) to securely access Azure resources.

> Ensure your AKS cluster is [enabled as OIDC Issuer](https://learn.microsoft.com/en-us/azure/aks/use-oidc-issuer)
### Backend services

- Create a User Assigned Managed Identity with Federated Credentials that map to the following Kubernetes Service Accounts:

**Subject Identifier**
- `system:serviceaccount:<NAMESPACE>:flytepropeller-system`
- `system:serviceaccount:<NAMESPACE>:flytepropeller-webhook-system`
- `system:serviceaccount:<NAMESPACE>:operator-system`
- `system:serviceaccount:<NAMESPACE>:proxy-system`

Where `<NAMESPACE>` is where you plan to install the Union operator (`union` by default)

- Assign the `Storage Blob Data Owner` role to this Identity at the Storage Account level.

### Workers

This is the Identity that the Pods created for each execution will use to access Azure resources. Those Pods use the `default` K8s Service Account on each project-domain namespace, unless otherwise specified.

- Create a User Assigned Managed Identity with Federated Credentials that map to the `default` K8s Service Account:

**Subject Identifier**

- `system:serviceaccount:development:default`
- `system:serviceaccount:staging:default`
- `system:serviceaccount:production:default`

- Assign the `Storage Blob Data Owner` role to this Identity at the Storage Account level.

## Node pools

By default, the Union installation request the following resources:

|   |  CPU (vCPUs)| Memory (GiB) |
|---|---|---|
| Requests  |  14 | 27.1  |
| Limits  | 17  |  32 |

For GPU access, Union injects tolerations and label selectors to execution Pods. [Learn](https://www.union.ai/docs/flyte/deployment/flyte-configuration/configuring-access-to-gpus/) more and validate your AKS nodes have matching labels and/or taints.
