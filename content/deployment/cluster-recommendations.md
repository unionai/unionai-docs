---
title: Cluster Recommendations
weight: 2
variants: -flyte -byoc +selfmanaged
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

The sections below describe how to configure this service account for each cloud provider.

> [!NOTE] Common service account
> In previous versions, each component had its own service account. The consolidated `union-system` service account simplifies IAM configuration — you only need to bind cloud permissions to a single identity.

# Performance Recommendations

## Node Pools

It is recommended but not required to use separate node pools for the Union services and the Union worker pods.  This allows you to
guard against resource contention between Union services and other tasks running in your cluster.  You can find additional information
in the [Configuring Node Pools](./configuration/node-pools) section.

# AWS

## S3

Each data plane uses an object store (an AWS S3 bucket, GCS bucket or ABS container) that is used to store data used in the execution of workflows.
As a {{< key product_name >}} administrator, you can specify retention policies for this data when setting up your data plane 
(learn more [about the different types of data categories](./configuration/data-retention) stored by the data plane.)

Union recommends the use of two S3 buckets:

1. metadata bucket: contains workflow execution data such as Task inputs and outputs, etc
2. fast registration bucket: contain local code artifacts that will be copied into the Flyte task container at runtime when using `union register` or `union run --remote --copy-all`.

Note: You can choose to use a single bucket in your dataplane

### Data Retention

Union recommends using Lifecycle Policy on these buckets to manage the storage costs. See [Data retention policy](./configuration/data-retention) for more information.

## IAM

You will need to create an IAM role for the `union-system` service account and grant it access to your S3 buckets.

1. Create an [IAM OIDC provider for your EKS cluster](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html#_create_oidc_provider_eksctl).

2. Create a new IAM role named `union-system-role`. This role will be assumed by the `union-system` Kubernetes service account via [IAM Roles for Service Accounts (IRSA)](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html).

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
                   "StringEquals": {
                       "$oidc_provider:aud": "sts.amazonaws.com",
                       "$oidc_provider:sub": "system:serviceaccount:union:union-system"
                   }
               }
           }
       ]
   }
   ```
   where `$account_id` is your AWS account ID and `$oidc_provider` is the OIDC provider you created above.

   You can obtain the OIDC provider value using the AWS CLI:

   ```bash
   aws eks describe-cluster --region $cloud_region --name $cluster_name --query "cluster.identity.oidc.issuer" --output text
   ```

3. Create and attach an IAM policy to this role granting S3 access:

   ```json
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "S3BucketAccess",
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

4. If Image Builder is enabled, also attach ECR permissions to the same role:

   ```json
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "ECRAuth",
               "Effect": "Allow",
               "Action": [
                   "ecr:GetAuthorizationToken"
               ],
               "Resource": "*"
           },
           {
               "Sid": "ECRReadWrite",
               "Effect": "Allow",
               "Action": [
                   "ecr:BatchCheckLayerAvailability",
                   "ecr:BatchGetImage",
                   "ecr:GetDownloadUrlForLayer",
                   "ecr:DescribeImages",
                   "ecr:PutImage",
                   "ecr:InitiateLayerUpload",
                   "ecr:UploadLayerPart",
                   "ecr:CompleteLayerUpload"
               ],
               "Resource": "arn:aws:ecr:<AWS_REGION>:<AWS_ACCOUNT_ID>:repository/<REPOSITORY>"
           }
       ]
   }
   ```

5. Annotate the `union-system` service account with the role ARN in your Helm values:

   ```yaml
   commonServiceAccount:
     annotations:
       eks.amazonaws.com/role-arn: "arn:aws:iam::<account_id>:role/union-system-role"
   ```

## EKS configuration

Union recommends installing the following EKS add-ons:
  - CoreDNS
  - Amazon VPC CNI
  - Kube-proxy

Union supports Autoscaling and the use of spot (interruptible) instances.

# GKE

## Secure access

Union recommends using [GKE Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to securely access GCP resources.

Create a Google Service Account and bind it to the `union-system` Kubernetes service account:

```bash
gcloud iam service-accounts add-iam-policy-binding \
  <GSA_NAME>@<PROJECT_ID>.iam.gserviceaccount.com \
  --role roles/iam.workloadIdentityUser \
  --member "serviceAccount:<PROJECT_ID>.svc.id.goog[union/union-system]"
```

Grant the following roles to the Google Service Account:

- `roles/storage.objectAdmin` on the GCS bucket(s) used for workflow data
- `roles/artifactregistry.writer` on the Artifact Registry repository (if Image Builder is enabled)
- `iam.serviceAccounts.signBlob` at the project level (required for Image Builder authentication)

Annotate the `union-system` service account with the Google Service Account email in your Helm values:

```yaml
commonServiceAccount:
  annotations:
    iam.gke.io/gcp-service-account: "<GSA_NAME>@<PROJECT_ID>.iam.gserviceaccount.com"
```

## GCS

Each data plane uses a GCS bucket to store data used in the execution of workflows.
Union recommends the use of two buckets (metadata and fast registration), though a single bucket is also supported.

See [Data retention policy](./configuration/data-retention) for information on managing storage costs with lifecycle policies.

# AKS

## Secure access

Union recommends using [Microsoft Entra Workload ID](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview) to securely access Azure resources.

Ensure your AKS cluster is [enabled as OIDC Issuer](https://learn.microsoft.com/en-us/azure/aks/use-oidc-issuer).

Create a User Assigned Managed Identity with a Federated Credential that maps to the `union-system` Kubernetes service account:

**Subject Identifier**

- `system:serviceaccount:<NAMESPACE>:union-system`

Where `<NAMESPACE>` is where you plan to install the Union operator (`union` by default).

Assign the following roles to this Identity:

- `Storage Blob Data Owner` at the Storage Account level
- `AcrPush` on the Azure Container Registry (if Image Builder is enabled)

Annotate the `union-system` service account with the managed identity client ID in your Helm values:

```yaml
commonServiceAccount:
  annotations:
    azure.workload.identity/client-id: "<MANAGED_IDENTITY_CLIENT_ID>"
```

### Workers

This is the Identity that the Pods created for each execution will use to access Azure resources. Those Pods use the `default` K8s Service Account on each project-domain namespace, unless otherwise specified.

Create a User Assigned Managed Identity with Federated Credentials that map to the `default` K8s Service Account:

**Subject Identifier**

- `system:serviceaccount:development:default`
- `system:serviceaccount:staging:default`
- `system:serviceaccount:production:default`

Assign the `Storage Blob Data Owner` role to this Identity at the Storage Account level.

## Azure Key Vault
Union ships with an embedded secrets manager. Alternatively, you can enable Union to consume secrets from Azure Key Vault adding the following to your Helm values file:

```yaml
config:

  ## Optional integration with Azure Key Vault secrets manager
  core:
    webhook:
      embeddedSecretManagerConfig:
        enabled: true
        type: Azure
        azureConfig:
          vaultURI: ""https://kv-myorg-prod.vault.azure.net/" #full key vault URI
      secretManagerTypes:
        - Azure
        - Embedded

```
## Node pools

By default, the Union installation request the following resources:

|          | CPU (vCPUs)| Memory (GiB) |
|----------|------------|--------------|
| Requests |          14|          27.1|
| Limits   |          17|            32|

For GPU access, Union injects tolerations and label selectors to execution Pods.
