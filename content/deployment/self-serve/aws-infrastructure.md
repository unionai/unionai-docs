---
title: Provision your AWS resources
description: Create the EKS cluster, S3 bucket, ECR repository and IAM roles that a self-serve cluster pool on AWS needs.
icon: amazon
weight: 4
variants: -flyte +union
---

# Provision your AWS resources

The self-serve setup installs the data plane into your cluster for you, but the AWS resources it runs on must exist first. This page creates them with the AWS CLI and `eksctl`:

- an EKS cluster in Auto Mode
- one S3 bucket
- a private ECR repository
- separate backend and worker IAM roles for service accounts (IRSA)

At the end you have the six values the AWS cluster-pool form asks for in [Connect your cluster](./connect-a-cluster).

> [!NOTE] Not the manual self-managed setup
> These resources differ from the ones in the manual [AWS infrastructure](../selfmanaged/infrastructure-recommendations/aws) guide: a single bucket, AWS Secrets Manager for runtime secrets, and IAM trust that follows the namespace the agent chooses. Use this page for self-serve setup only.

## Prerequisites

- AWS CLI authenticated to the target account.
- `eksctl` 0.195.0 or later, `kubectl`, and `envsubst` installed locally.
- Permissions to create EKS, EC2/VPC, IAM, S3, ECR, and CloudWatch resources.
- A Union.ai organization. See [Sign up and create your Union.ai organization](./sign-up).

The commands create billable resources, including an EKS control plane and
networking. Choose a dedicated test account when possible.

## 1. Set names and verify your AWS identity

Choose names that are unique in the AWS account. `BUCKET_PREFIX` must also be
globally unique because S3 bucket names are global. Do not use the sample values
unchanged.

```shell
export NAME_PREFIX=<name_prefix>
export AWS_REGION=us-east-2
export CLUSTER_NAME=${NAME_PREFIX}-union-selfserve
export KUBERNETES_VERSION=1.35
export BUCKET_PREFIX=${NAME_PREFIX}-union-selfserve
export DATA_BUCKET=${BUCKET_PREFIX}-data
export ECR_REPO_NAME=${CLUSTER_NAME}
export BACKEND_ROLE_NAME=${CLUSTER_NAME}-backend
export WORKER_ROLE_NAME=${CLUSTER_NAME}-worker

# "*" supports the agent-selected release namespace. Replace it with a known
# namespace only after the cluster is connected and the chart release namespace
# is stable.
export DATAPLANE_NAMESPACE='*'

export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
aws sts get-caller-identity
```

Use a currently supported EKS Kubernetes version. The Terraform root defaults
to `1.35`; update `KUBERNETES_VERSION` if AWS no longer offers that version in
your region.

## 2. Create an EKS Auto Mode cluster

Create the cluster and let `eksctl` create its VPC, subnets, control-plane
role, Auto Mode node role, and default node pools:

These commands use [Amazon EKS Auto Mode with eksctl](https://docs.aws.amazon.com/eks/latest/userguide/automode-get-started-eksctl.html).

```shell
eksctl create cluster \
  --name "${CLUSTER_NAME}" \
  --region "${AWS_REGION}" \
  --version "${KUBERNETES_VERSION}" \
  --enable-auto-mode
```

Associate an IAM OIDC provider. It is required for both IRSA roles. The command
is safe to run when the provider already exists.

```shell
eksctl utils associate-iam-oidc-provider \
  --cluster "${CLUSTER_NAME}" \
  --region "${AWS_REGION}" \
  --approve

export OIDC_PROVIDER=$(aws eks describe-cluster \
  --region "${AWS_REGION}" \
  --name "${CLUSTER_NAME}" \
  --query 'cluster.identity.oidc.issuer' \
  --output text | sed 's|https://||')

export NODE_ROLE_ARN=$(aws eks describe-cluster \
  --region "${AWS_REGION}" \
  --name "${CLUSTER_NAME}" \
  --query 'cluster.computeConfig.nodeRoleArn' \
  --output text)
```

Configure access and check that the cluster is usable. If the creator identity
is not an EKS administrator, grant its IAM role the EKS cluster-admin access
policy before running `update-kubeconfig`.

```shell
aws eks update-kubeconfig --region "${AWS_REGION}" --name "${CLUSTER_NAME}"
kubectl get nodes
```

## 3. Create the S3 bucket

The data bucket stores workflow metadata, task inputs and outputs, artifacts,
and fast-registration code bundles. It is the object store entered in the
cluster-pool form. For `us-east-1`, omit `--create-bucket-configuration`.

```shell
aws s3api create-bucket \
  --bucket "${DATA_BUCKET}" \
  --region "${AWS_REGION}" \
  --create-bucket-configuration "LocationConstraint=${AWS_REGION}"

aws s3api put-public-access-block --bucket "${DATA_BUCKET}" \
  --public-access-block-configuration \
  'BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true'
```

To let the Union.ai console download code and artifacts through presigned URLs,
save the following as `cors.json`. Add your console hostname if it is not served
from a Union domain.

```json
{
  "CORSRules": [
    {
      "AllowedHeaders": ["*"],
      "AllowedMethods": ["GET", "PUT", "POST", "DELETE", "HEAD"],
      "AllowedOrigins": ["https://*.unionai.cloud", "https://*.union.ai"],
      "ExposeHeaders": ["ETag"],
      "MaxAgeSeconds": 3600
    }
  ]
}
```

Apply the CORS policy to the bucket:

```shell
aws s3api put-bucket-cors \
  --bucket "${DATA_BUCKET}" \
  --cors-configuration file://cors.json
```

For production, add an S3 lifecycle policy, explicit encryption/KMS controls as
required by your organization, and recovery retention appropriate for workflow
data.

## 4. Create the private ECR repository

```shell
aws ecr create-repository \
  --repository-name "${ECR_REPO_NAME}" \
  --region "${AWS_REGION}" \
  --image-scanning-configuration scanOnPush=true

export IMAGE_REGISTRY=$(aws ecr describe-repositories \
  --repository-names "${ECR_REPO_NAME}" \
  --region "${AWS_REGION}" \
  --query 'repositories[0].repositoryUri' \
  --output text)
```

## 5. Create the backend and worker IRSA roles

The backend role is assumed by `union-system` and the legacy
`flytepropeller-system` service accounts in the dataplane namespace. The worker
role is assumed by task-pod service accounts (`default` or `union`) in dynamic
project namespaces.

Save this backend trust policy as `backend-trust-policy.json`:

```json
{
  "Version": "2012-10-17",
  "Statement": [{
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
        "$OIDC_PROVIDER:sub": [
          "system:serviceaccount:$DATAPLANE_NAMESPACE:union-system",
          "system:serviceaccount:$DATAPLANE_NAMESPACE:flytepropeller-system"
        ]
      }
    }
  }]
}
```

Save this worker trust policy as `worker-trust-policy.json`:

```json
{
  "Version": "2012-10-17",
  "Statement": [{
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
        "$OIDC_PROVIDER:sub": [
          "system:serviceaccount:*:default",
          "system:serviceaccount:*:union"
        ]
      }
    }
  }]
}
```

Substitute the shell variables, create the roles, and record their ARNs:

```shell
envsubst < backend-trust-policy.json > /tmp/backend-trust-policy.json
envsubst < worker-trust-policy.json > /tmp/worker-trust-policy.json

aws iam create-role \
  --role-name "${BACKEND_ROLE_NAME}" \
  --assume-role-policy-document file:///tmp/backend-trust-policy.json

aws iam create-role \
  --role-name "${WORKER_ROLE_NAME}" \
  --assume-role-policy-document file:///tmp/worker-trust-policy.json

export BACKEND_IAM_ROLE_ARN=$(aws iam get-role --role-name "${BACKEND_ROLE_NAME}" --query 'Role.Arn' --output text)
export WORKER_IAM_ROLE_ARN=$(aws iam get-role --role-name "${WORKER_ROLE_NAME}" --query 'Role.Arn' --output text)
```

## 6. Grant S3 and Secrets Manager access

Save this policy as `backend-policy.json`. It grants the dataplane services
access to the data bucket and permits the runtime secret-store operations used by
the operator proxy.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "UnionDataBuckets",
      "Effect": "Allow",
      "Action": ["s3:DeleteObject*", "s3:GetObject*", "s3:ListBucket", "s3:PutObject*"],
      "Resource": [
        "arn:aws:s3:::$DATA_BUCKET",
        "arn:aws:s3:::$DATA_BUCKET/*"
      ]
    },
    {
      "Sid": "SecretsManagerReadWrite",
      "Effect": "Allow",
      "Action": [
        "secretsmanager:CreateSecret", "secretsmanager:DescribeSecret",
        "secretsmanager:GetSecretValue", "secretsmanager:PutSecretValue",
        "secretsmanager:UpdateSecret", "secretsmanager:TagResource"
      ],
      "Resource": "arn:aws:secretsmanager:$AWS_REGION:$AWS_ACCOUNT_ID:secret:*"
    }
  ]
}
```

Save this policy as `worker-policy.json`. It lets task pods use storage, read
runtime secrets, and obtain an ECR authorization token.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "UnionDataBuckets",
      "Effect": "Allow",
      "Action": ["s3:DeleteObject*", "s3:GetObject*", "s3:ListBucket", "s3:PutObject*"],
      "Resource": [
        "arn:aws:s3:::$DATA_BUCKET",
        "arn:aws:s3:::$DATA_BUCKET/*"
      ]
    },
    {
      "Sid": "SecretsManagerRead",
      "Effect": "Allow",
      "Action": ["secretsmanager:DescribeSecret", "secretsmanager:GetSecretValue"],
      "Resource": "arn:aws:secretsmanager:$AWS_REGION:$AWS_ACCOUNT_ID:secret:*"
    },
    {
      "Sid": "ECRTokenPermission",
      "Effect": "Allow",
      "Action": "ecr:GetAuthorizationToken",
      "Resource": "*"
    }
  ]
}
```

Expand the variables and attach the inline policies:

```shell
envsubst < backend-policy.json > /tmp/backend-policy.json
envsubst < worker-policy.json > /tmp/worker-policy.json

aws iam put-role-policy \
  --role-name "${BACKEND_ROLE_NAME}" \
  --policy-name union-backend-access \
  --policy-document file:///tmp/backend-policy.json

aws iam put-role-policy \
  --role-name "${WORKER_ROLE_NAME}" \
  --policy-name union-worker-access \
  --policy-document file:///tmp/worker-policy.json
```

## 7. Grant repository access

Save this ECR repository policy as `ecr-policy.json`. It gives the worker role
push/pull access and the backend and EKS node roles pull access.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "WorkerPushPull",
      "Effect": "Allow",
      "Principal": {"AWS": "$WORKER_IAM_ROLE_ARN"},
      "Action": [
        "ecr:BatchCheckLayerAvailability", "ecr:BatchGetImage",
        "ecr:CompleteLayerUpload", "ecr:DescribeImages",
        "ecr:DescribeRepositories", "ecr:GetDownloadUrlForLayer",
        "ecr:InitiateLayerUpload", "ecr:ListImages", "ecr:PutImage",
        "ecr:UploadLayerPart"
      ]
    },
    {
      "Sid": "BackendAndNodePull",
      "Effect": "Allow",
      "Principal": {"AWS": ["$BACKEND_IAM_ROLE_ARN", "$NODE_ROLE_ARN"]},
      "Action": [
        "ecr:BatchCheckLayerAvailability", "ecr:BatchGetImage",
        "ecr:DescribeImages", "ecr:DescribeRepositories",
        "ecr:GetDownloadUrlForLayer", "ecr:ListImages"
      ]
    }
  ]
}
```

```shell
envsubst < ecr-policy.json > /tmp/ecr-policy.json
aws ecr set-repository-policy \
  --repository-name "${ECR_REPO_NAME}" \
  --region "${AWS_REGION}" \
  --policy-text file:///tmp/ecr-policy.json
```

## 8. Collect the values for the cluster pool

Print the values you will enter in the AWS cluster-pool form:

```shell
printf '%s\n' \
  "object_store_uri = s3://${DATA_BUCKET}" \
  "secret_store_account_id = ${AWS_ACCOUNT_ID}" \
  "secret_store_region = ${AWS_REGION}" \
  "image_registry = ${IMAGE_REGISTRY}" \
  "backend_iam_role_arn = ${BACKEND_IAM_ROLE_ARN}" \
  "worker_iam_role_arn = ${WORKER_IAM_ROLE_ARN}" \
  "kubeconfig_command = aws eks update-kubeconfig --region ${AWS_REGION} --name ${CLUSTER_NAME}"
```

Keep this output, and keep the shell where `kubectl get nodes` succeeds: you run the agent install from it.

## Important behavior and cleanup

- The wide service-account trust is deliberate for the agent-selected release
  namespace and dynamic task namespaces. Restrict `DATAPLANE_NAMESPACE` only
  when the actual release namespace is known and fixed.
- The pool uses one object-store bucket for metadata and fast registration; do
  not create or configure a separate fast-registration bucket.
- This guide does not configure automatic expiry. Add S3/ECR lifecycle rules
  before production use.
- To remove the environment, delete the cluster with `eksctl delete cluster`,
  then empty/delete the S3 bucket, delete the ECR repository, and delete the
  two IAM roles and their inline policies. Review every target before deletion.

## Next steps

**[Connect your cluster](./connect-a-cluster).** Create an AWS cluster pool with the values above, register the cluster, and install the agent.
