---
title: AWS
weight: 1
variants: -flyte +union
---

# AWS infrastructure

This page walks you through creating the AWS resources needed for a Union data plane. If you already have these resources, skip to [Deploy the dataplane](../deploy/_index).

## Environment variables

Set these variables before running the commands below. Customize the names if you are deploying multiple data planes in the same AWS account.

```bash
export AWS_REGION=us-east-2                          # AWS region for all resources
export CLUSTER_NAME=union-dataplane                  # EKS cluster name
export BUCKET_PREFIX=union-dataplane                 # prefix for S3 buckets (must be globally unique)
export ECR_REPO_NAME=${ECR_REPO_NAME}    # ECR repository name
export IAM_ROLE_NAME=union-system-role               # IAM role name
```

## EKS cluster

You need an EKS cluster running one of the most recent three minor Kubernetes versions. See [Infrastructure recommendations](../infrastructure-recommendations/_index) for networking and node pool guidance.

If you don't already have a cluster, create one with `eksctl`:

```bash
eksctl create cluster \
  --name ${CLUSTER_NAME} \
  --region us-east-2 \
  --version 1.31 \
  --node-type m5.2xlarge \
  --nodes 3 \
  --with-oidc \
  --managed
```

> [!NOTE] The `--with-oidc` flag creates an IAM OIDC provider for the cluster, which is required for [IRSA](#iam) below.

The following EKS add-ons are required and come pre-installed on managed clusters created with `eksctl`:

- CoreDNS
- Amazon VPC CNI
- Kube-proxy

If you created your cluster through other means, verify they are installed:

```bash
aws eks list-addons --cluster-name ${CLUSTER_NAME} --region ${AWS_REGION}
```

Union supports Autoscaling and the use of spot (interruptible) instances.

## Networking and IP capacity

The AWS VPC CNI assigns one VPC IP per pod from the **node's subnet**, so pod-IP exhaustion is
the most common scale blocker. Completed/terminating pods hold their IPs until garbage-collected,
so high-churn workloads compound subnet pressure. Size the VPC greedily up front — adding VPC
CIDR blocks later works, but resizing existing subnets does not.

Suggested defaults for a production-scale data plane:

| Component | Setting |
| --- | --- |
| VPC CIDR | `10.0.0.0/16` |
| Private subnets | 3× `/18` (`10.0.64.0/18`, `10.0.128.0/18`, `10.0.192.0/18`) — ~16,376 IPs per AZ |
| Public subnets | 3× `/24` — only NAT gateways and internet-facing load balancers live here |
| NAT gateways | 1 (cost-optimized) or per-AZ (production resilience) |

This sizing supports up to ~40,000 pods and ~9,000 nodes per VPC. When a single cluster scales
past ~40,000 concurrent pods, add `10.1.0.0/16`, `10.2.0.0/16`, etc. as additional VPC CIDR
blocks and provision new private subnets from them — the VPC CNI does not require contiguous
CIDRs.

**Relieving pod-IP pressure**:

- Add CIDR blocks to the VPC (typically `/16` per block). New private subnets become available
  immediately.
- Enable VPC CNI **prefix delegation** — allocates `/28` prefixes (16 IPs) per ENI attachment
  instead of individual IPs.
- Reduce the pod-GC timer for completed pods (default 24 h → 1 h) so IPs return to the pool
  faster.

For the full set of per-cluster scaling ceilings (vCPU quotas, image pull rate, conntrack,
etcd), see [Scaling constraints](../infrastructure-recommendations/scaling-constraints).

## S3

Each data plane uses S3 buckets to store data used in workflow execution.
Union recommends the use of two S3 buckets:

1. **Metadata bucket**: contains workflow execution data such as task inputs and outputs.
2. **Code bundle/Fast registration bucket**: contains local code artifacts copied into the Flyte task container at runtime when using `flyte deploy` or `flyte run --copy-style all`.

You can also choose to use a single bucket.

Create the buckets:

```bash
aws s3api create-bucket \
  --bucket ${BUCKET_PREFIX}-metadata \
  --region ${AWS_REGION} \
  --create-bucket-configuration LocationConstraint=${AWS_REGION}

aws s3api create-bucket \
  --bucket ${BUCKET_PREFIX}-fast-reg \
  --region ${AWS_REGION} \
  --create-bucket-configuration LocationConstraint=${AWS_REGION}
```

> [!NOTE] If your region is `us-east-1`, omit the `--create-bucket-configuration` flag.

### CORS configuration

To enable the [Code Viewer](../configuration/code-viewer) in the Union UI, configure a CORS policy on your buckets. This allows the UI to securely fetch code bundles directly from S3.

Save the following as `cors.json`:

```json
{
  "CORSRules": [
    {
      "AllowedHeaders": ["*"],
      "AllowedMethods": ["GET", "HEAD"],
      "AllowedOrigins": ["https://*.unionai.cloud"],
      "ExposeHeaders": ["ETag"],
      "MaxAgeSeconds": 3600
    }
  ]
}
```

Apply it to both buckets:

```bash
aws s3api put-bucket-cors --bucket ${BUCKET_PREFIX}-metadata --cors-configuration file://cors.json
aws s3api put-bucket-cors --bucket ${BUCKET_PREFIX}-fast-reg --cors-configuration file://cors.json
```

### Data retention

Union recommends using Lifecycle Policy on these buckets to manage storage costs. See [Data retention policy](../configuration/data-retention) for more information.

## ECR

Create an [ECR private repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html) for Image Builder to push and pull container images:

```bash
aws ecr create-repository \
  --repository-name ${ECR_REPO_NAME} \
  --region ${AWS_REGION} \
  --image-scanning-configuration scanOnPush=true
```

Note the repository URI from the output (e.g. `<AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/${ECR_REPO_NAME}`). You will reference it when configuring IAM permissions below.

> [!NOTE] Image pulls use the node role; watch pull rate at scale
> Kubelet pulls task images using the node's instance-profile IAM role, not the pod's IRSA
> binding. `eksctl`-managed node groups attach `AmazonEC2ContainerRegistryReadOnly` by
> default, so pulls work out of the box; if you use a custom node role, grant it ECR read on
> this repository. During rapid node scale-up, public system-image pulls funnel through the
> NAT gateway and can hit per-IP rate limits — configure an ECR pull-through cache or VPC
> interface endpoints for `ecr.api`/`ecr.dkr`. See
> [Image registry pull rate](../infrastructure-recommendations/scaling-constraints#image-registry-pull-rate).

## IAM

Create an IAM role that both the Union platform services and workflow task pods will use to access S3 and ECR. This role is assumed via [IAM Roles for Service Accounts (IRSA)](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html).

### 1. Enable OIDC

If you created your cluster with `--with-oidc` above, this is already done. Otherwise, create an [IAM OIDC provider for your EKS cluster](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html#_create_oidc_provider_eksctl):

```bash
eksctl utils associate-iam-oidc-provider --cluster ${CLUSTER_NAME} --region ${AWS_REGION} --approve
```

Get the OIDC provider URL (you'll need it for the trust policy):

```bash
export OIDC_PROVIDER=$(aws eks describe-cluster \
  --region ${AWS_REGION} \
  --name ${CLUSTER_NAME} \
  --query "cluster.identity.oidc.issuer" \
  --output text | sed 's|https://||')

export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
```

### 2. Create the IAM role

Save the following trust policy as `trust-policy.json`:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::$AWS_ACCOUNT_ID:oidc-provider/$OIDC_PROVIDER"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringEquals": {
                    "$OIDC_PROVIDER:aud": "sts.amazonaws.com"
                },
                "StringLike": {
                    "$OIDC_PROVIDER:sub": "system:serviceaccount:*"
                }
            }
        }
    ]
}
```

> [!NOTE] Why `system:serviceaccount:*`?
> Union platform services run in the data plane namespace (e.g. `union`), but workflow task pods run in per-project namespaces (e.g. `union-health-monitoring-development`). Both need to assume this role to access S3 and ECR.

Substitute your values and create the role:

```bash
envsubst < trust-policy.json > /tmp/trust-policy.json

aws iam create-role \
  --role-name ${IAM_ROLE_NAME} \
  --assume-role-policy-document file:///tmp/trust-policy.json
```

### 3. Attach the S3 policy

Save as `s3-policy.json` (replace `<BUCKET_PREFIX>` with your actual prefix):

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
                "arn:aws:s3:::<BUCKET_PREFIX>-metadata",
                "arn:aws:s3:::<BUCKET_PREFIX>-metadata/*",
                "arn:aws:s3:::<BUCKET_PREFIX>-fast-reg",
                "arn:aws:s3:::<BUCKET_PREFIX>-fast-reg/*"
            ]
        }
    ]
}
```

```bash
aws iam put-role-policy \
  --role-name ${IAM_ROLE_NAME} \
  --policy-name union-s3-access \
  --policy-document file://s3-policy.json
```

### 4. Attach the ECR policy

Save as `ecr-policy.json` (replace `<AWS_REGION>`, `<AWS_ACCOUNT_ID>`, and `<REPOSITORY>`):

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

```bash
aws iam put-role-policy \
  --role-name ${IAM_ROLE_NAME} \
  --policy-name union-ecr-access \
  --policy-document file://ecr-policy.json
```

### 5. Configure the service account annotation

In your Helm values, annotate the `union-system` service account with the role ARN:

```yaml
commonServiceAccount:
  annotations:
    eks.amazonaws.com/role-arn: "arn:aws:iam::<AWS_ACCOUNT_ID>:role/${IAM_ROLE_NAME}"
```

## Deploy configuration

When you [deploy the data plane](../deploy/_index), download the AWS values file and set the AWS-specific keys below. The shared `global` keys (`UNION_CONTROL_PLANE_HOST`, `CLUSTER_NAME`, `ORG_NAME`) are covered in the deploy walkthrough.

```bash
curl -O https://raw.githubusercontent.com/unionai/helm-charts/main/charts/dataplane/values.aws.yaml
```

Using the [environment variables](#environment-variables) from above, set the following keys under `global`. The rest of the file (storage, service account annotations, IRSA) is templated from these values, so you do not need to edit it:

- Set `global.AWS_ACCOUNT_ID` to your AWS account ID. You can retrieve it with `aws sts get-caller-identity --query Account --output text`.
- Set `global.AWS_REGION` to `${AWS_REGION}`.
- Set `global.METADATA_BUCKET` to `${BUCKET_PREFIX}-metadata`.
- Set `global.FAST_REGISTRATION_BUCKET` to `${BUCKET_PREFIX}-fast-reg`.
- Set `global.BACKEND_IAM_ROLE_ARN` to `arn:aws:iam::${AWS_ACCOUNT_ID}:role/${IAM_ROLE_NAME}` (where `AWS_ACCOUNT_ID` is your 12-digit account ID).
- Set `global.WORKER_IAM_ROLE_ARN` to the same value (or a separate role if you use distinct worker permissions).
- Optionally set `imageBuilder.registryName` to `${ECR_REPO_NAME}` (defaults to `union-dataplane`; the chart auto-generates the full ECR URL from the account ID and region).
