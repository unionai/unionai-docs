---
title: Prepare infrastructure
weight: 1
variants: -flyte +union
---

# Prepare infrastructure

This page walks you through creating the AWS resources needed for a Union data plane. If you already have these resources, skip to [Deploy the dataplane](../selfmanaged-aws/deploy-dataplane).

## EKS Cluster

You need an EKS cluster running one of the most recent three minor Kubernetes versions. See [Cluster Recommendations](../cluster-recommendations) for networking and node pool guidance.

If you don't already have a cluster, create one with `eksctl`:

```bash
eksctl create cluster \
  --name union-dataplane \
  --region us-east-2 \
  --version 1.31 \
  --node-type m5.xlarge \
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
aws eks list-addons --cluster-name union-dataplane --region ${AWS_REGION}
```

Union supports Autoscaling and the use of spot (interruptible) instances.

## S3

Each data plane uses S3 buckets to store data used in workflow execution.
Union recommends the use of two S3 buckets:

1. **Metadata bucket**: contains workflow execution data such as task inputs and outputs.
2. **Code bundle/Fast registration bucket**: contains local code artifacts copied into the Flyte task container at runtime when using `union register` or `union run --remote --copy-all`.

You can also choose to use a single bucket.

Create the buckets:

```bash
export BUCKET_PREFIX=union-dataplane   # choose a globally unique prefix
export AWS_REGION=us-east-2

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

### CORS Configuration

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

### Data Retention

Union recommends using Lifecycle Policy on these buckets to manage storage costs. See [Data retention policy](../configuration/data-retention) for more information.

## ECR

Create an [ECR private repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html) for Image Builder to push and pull container images:

```bash
aws ecr create-repository \
  --repository-name union-dataplane/imagebuilder \
  --region ${AWS_REGION} \
  --image-scanning-configuration scanOnPush=true
```

Note the repository URI from the output (e.g. `<AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/union-dataplane/imagebuilder`) — you will reference it when configuring IAM permissions below.

## IAM

Create an IAM role that both the Union platform services and workflow task pods will use to access S3 and ECR. This role is assumed via [IAM Roles for Service Accounts (IRSA)](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html).

### 1. Enable OIDC

If you created your cluster with `--with-oidc` above, this is already done. Otherwise, create an [IAM OIDC provider for your EKS cluster](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html#_create_oidc_provider_eksctl):

```bash
eksctl utils associate-iam-oidc-provider --cluster union-dataplane --region ${AWS_REGION} --approve
```

Get the OIDC provider URL (you'll need it for the trust policy):

```bash
export OIDC_PROVIDER=$(aws eks describe-cluster \
  --region ${AWS_REGION} \
  --name union-dataplane \
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
  --role-name union-system-role \
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
  --role-name union-system-role \
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
  --role-name union-system-role \
  --policy-name union-ecr-access \
  --policy-document file://ecr-policy.json
```

### 5. Configure the service account annotation

In your Helm values, annotate the `union-system` service account with the role ARN:

```yaml
commonServiceAccount:
  annotations:
    eks.amazonaws.com/role-arn: "arn:aws:iam::<AWS_ACCOUNT_ID>:role/union-system-role"
```
