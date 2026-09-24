---
title: Provision your AWS resources
description: Create the EKS cluster, S3 buckets, ECR repository and IAM roles that a self-serve cluster pool on AWS needs.
icon: amazon
weight: 4
variants: -flyte +union
---

# Provision your AWS resources

The self-serve setup installs the data plane into your cluster for you, but the AWS resources it runs on must exist first. This page creates them with the AWS CLI and `eksctl`:

- an EKS cluster with a managed node group of three `m6i.large` nodes
- two S3 buckets, one for metadata and one for fast registration
- a private ECR repository
- separate backend and worker IAM roles for service accounts (IRSA)

At the end you have the values you enter when you [connect your cluster](./connect-a-cluster): four for the cluster pool, and two IAM role ARNs for registering the cluster.

> [!NOTE] Not the manual self-managed setup
> These resources differ from the ones in the manual [AWS infrastructure](../selfmanaged/infrastructure-recommendations/aws) guide: AWS Secrets Manager holds runtime secrets, IAM trust follows the namespace the agent chooses, and the data plane chart installs Metrics Server itself. Use this page for self-serve setup only.

## Prerequisites

- AWS CLI authenticated to the target account.
- `eksctl` 0.195.0 or later, `kubectl`, `jq`, and `envsubst` installed locally.
- Permissions to create EKS, EC2/VPC, IAM, S3, ECR, and CloudWatch resources.
- A Union.ai organization. See [Sign up and create your Union.ai organization](./sign-up).

The commands create billable resources, including an EKS control plane, three EC2 nodes, and networking. Choose a dedicated test account when possible.

Run every step in the same shell session. Later steps use the variables that earlier steps export.

## 1. Set names and verify your AWS identity

Choose names that are unique in the AWS account. `BUCKET_PREFIX` must also be globally unique, because S3 bucket names are global. Do not use the sample values unchanged.

```shell
export AWS_REGION=us-east-2
export NAME_PREFIX=<my-team>
export CLUSTER_NAME=${NAME_PREFIX}-union-selfserve
export NODEGROUP_NAME=${CLUSTER_NAME}-workers
export KUBERNETES_VERSION=1.35
export BUCKET_PREFIX=${NAME_PREFIX}-union-selfserve
export METADATA_BUCKET=${BUCKET_PREFIX}-metadata
export FAST_REGISTRATION_BUCKET=${BUCKET_PREFIX}-fast-reg
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

Use a Kubernetes version that EKS currently supports in your region. If AWS no longer offers `1.35`, update `KUBERNETES_VERSION`.

## 2. Create the EKS cluster

Create the cluster with a managed node group. The configuration leaves out the EKS Metrics Server add-on, because the data plane chart installs Metrics Server itself, and keeps the networking add-ons the cluster needs:

```shell
eksctl create cluster --config-file <(
  jq -n \
    --arg clusterName "${CLUSTER_NAME}" \
    --arg region "${AWS_REGION}" \
    --arg version "${KUBERNETES_VERSION}" \
    --arg nodegroupName "${NODEGROUP_NAME}" \
    '{
      apiVersion: "eksctl.io/v1alpha5",
      kind: "ClusterConfig",
      metadata: {
        name: $clusterName,
        region: $region,
        version: $version
      },
      addonsConfig: {
        disableDefaultAddons: true
      },
      addons: [
        {name: "vpc-cni"},
        {name: "coredns"},
        {name: "kube-proxy"}
      ],
      managedNodeGroups: [
        {
          name: $nodegroupName,
          instanceType: "m6i.large",
          desiredCapacity: 3,
          minSize: 3,
          maxSize: 6
        }
      ]
    }'
)
```

`eksctl` also creates the VPC and subnets the cluster uses. The three `m6i.large` nodes provide the data plane's initial capacity, and the node group can scale to six.

Associate an IAM OIDC provider, which both IRSA roles need, and look up the OIDC issuer and the node group's IAM role. The first command is safe to run when the provider already exists.

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

if [[ -z "${OIDC_PROVIDER}" || "${OIDC_PROVIDER}" == "None" ]]; then
  echo "Unable to resolve the cluster OIDC provider" >&2
fi

export NODE_ROLE_ARN=$(aws eks describe-nodegroup \
  --region "${AWS_REGION}" \
  --cluster-name "${CLUSTER_NAME}" \
  --nodegroup-name "${NODEGROUP_NAME}" \
  --query 'nodegroup.nodeRole' \
  --output text)

if [[ -z "${NODE_ROLE_ARN}" || "${NODE_ROLE_ARN}" == "None" ]]; then
  echo "Unable to resolve the managed node-group IAM role" >&2
fi
```

If either check prints an error, stop and fix it before you continue. Later steps put these values into IAM policies.

Configure access and check that the cluster is usable. If the identity that created the cluster is not an EKS administrator, grant its IAM role the EKS cluster-admin access policy before you run `update-kubeconfig`.

```shell
aws eks update-kubeconfig --region "${AWS_REGION}" --name "${CLUSTER_NAME}"
kubectl get nodes
```

Confirm that three nodes report `Ready`. Then check that the cluster has no Metrics Server of its own, which would conflict with the one the data plane chart installs:

```shell
if kubectl get clusterrole system:metrics-server-aggregated-reader >/dev/null 2>&1; then
  echo "ERROR: An existing Metrics Server will conflict with the dataplane chart." >&2
else
  echo "No Metrics Server ownership collision detected."
fi
```

Do not install the EKS Metrics Server add-on on this cluster later. The data plane chart owns Metrics Server.

## 3. Create the S3 buckets

The metadata bucket stores workflow metadata, task inputs and outputs, and artifacts. It is the object store you enter in the cluster-pool form. The fast-registration bucket holds code bundles, and both IAM roles get the same access to it.

For `us-east-1`, omit `--create-bucket-configuration`.

```shell
aws s3api create-bucket \
  --bucket "${METADATA_BUCKET}" \
  --region "${AWS_REGION}" \
  --create-bucket-configuration "LocationConstraint=${AWS_REGION}"

aws s3api create-bucket \
  --bucket "${FAST_REGISTRATION_BUCKET}" \
  --region "${AWS_REGION}" \
  --create-bucket-configuration "LocationConstraint=${AWS_REGION}"

for bucket in "${METADATA_BUCKET}" "${FAST_REGISTRATION_BUCKET}"; do
  aws s3api put-public-access-block --bucket "${bucket}" \
    --public-access-block-configuration \
    'BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true'
done
```

Add a CORS policy to both buckets, so the Union.ai UI can download code and artifacts through presigned URLs. If your UI is not served from a Union.ai domain, add its hostname to `AllowedOrigins`.

```shell
for bucket in "${METADATA_BUCKET}" "${FAST_REGISTRATION_BUCKET}"; do
  aws s3api put-bucket-cors \
    --bucket "${bucket}" \
    --cors-configuration '{
      "CORSRules": [
        {
          "AllowedHeaders": ["*"],
          "AllowedMethods": ["GET", "PUT", "POST", "DELETE", "HEAD"],
          "AllowedOrigins": ["https://*.unionai.cloud", "https://*.union.ai"],
          "ExposeHeaders": ["ETag"],
          "MaxAgeSeconds": 3600
        }
      ]
    }'
done
```

For production, add an S3 lifecycle policy, the encryption and KMS controls your organization requires, and recovery retention appropriate for workflow data.

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

The backend role is assumed by the `union-system` and legacy `flytepropeller-system` service accounts in the data plane namespace. The worker role is assumed by task-pod service accounts (`default` or `union`) in dynamic project namespaces.

Each command fills the shell variables into the trust policy with `envsubst`, creates the role, and records its ARN:

```shell
export BACKEND_IAM_ROLE_ARN=$(aws iam create-role \
  --role-name "${BACKEND_ROLE_NAME}" \
  --assume-role-policy-document "$(envsubst <<< '{
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
  }')" \
  --query 'Role.Arn' \
  --output text)

export WORKER_IAM_ROLE_ARN=$(aws iam create-role \
  --role-name "${WORKER_ROLE_NAME}" \
  --assume-role-policy-document "$(envsubst <<< '{
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
  }')" \
  --query 'Role.Arn' \
  --output text)
```

## 6. Grant S3 and Secrets Manager access

Attach an inline policy to each role:

- The backend policy gives the data plane services access to both buckets, and permits the runtime secret-store operations the operator proxy uses.
- The worker policy lets task pods use both buckets, read runtime secrets, and obtain an ECR authorization token.

```shell
aws iam put-role-policy \
  --role-name "${BACKEND_ROLE_NAME}" \
  --policy-name union-backend-access \
  --policy-document "$(envsubst <<< '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "UnionDataBuckets",
        "Effect": "Allow",
        "Action": [
          "s3:DeleteObject*",
          "s3:GetObject*",
          "s3:ListBucket",
          "s3:PutObject*"
        ],
        "Resource": [
          "arn:aws:s3:::$METADATA_BUCKET",
          "arn:aws:s3:::$METADATA_BUCKET/*",
          "arn:aws:s3:::$FAST_REGISTRATION_BUCKET",
          "arn:aws:s3:::$FAST_REGISTRATION_BUCKET/*"
        ]
      },
      {
        "Sid": "SecretsManagerReadWrite",
        "Effect": "Allow",
        "Action": [
          "secretsmanager:CreateSecret",
          "secretsmanager:DescribeSecret",
          "secretsmanager:GetSecretValue",
          "secretsmanager:PutSecretValue",
          "secretsmanager:UpdateSecret",
          "secretsmanager:TagResource"
        ],
        "Resource": "arn:aws:secretsmanager:$AWS_REGION:$AWS_ACCOUNT_ID:secret:*"
      }
    ]
  }')"

aws iam put-role-policy \
  --role-name "${WORKER_ROLE_NAME}" \
  --policy-name union-worker-access \
  --policy-document "$(envsubst <<< '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "UnionDataBuckets",
        "Effect": "Allow",
        "Action": [
          "s3:DeleteObject*",
          "s3:GetObject*",
          "s3:ListBucket",
          "s3:PutObject*"
        ],
        "Resource": [
          "arn:aws:s3:::$METADATA_BUCKET",
          "arn:aws:s3:::$METADATA_BUCKET/*",
          "arn:aws:s3:::$FAST_REGISTRATION_BUCKET",
          "arn:aws:s3:::$FAST_REGISTRATION_BUCKET/*"
        ]
      },
      {
        "Sid": "SecretsManagerRead",
        "Effect": "Allow",
        "Action": [
          "secretsmanager:DescribeSecret",
          "secretsmanager:GetSecretValue"
        ],
        "Resource": "arn:aws:secretsmanager:$AWS_REGION:$AWS_ACCOUNT_ID:secret:*"
      },
      {
        "Sid": "ECRTokenPermission",
        "Effect": "Allow",
        "Action": "ecr:GetAuthorizationToken",
        "Resource": "*"
      }
    ]
  }')"
```

## 7. Grant repository access

Set a repository policy on the ECR repository. It gives the worker role push and pull access, and gives the backend role and the EKS node role pull access.

```shell
aws ecr set-repository-policy \
  --repository-name "${ECR_REPO_NAME}" \
  --region "${AWS_REGION}" \
  --policy-text "$(envsubst <<< '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "WorkerPushPull",
        "Effect": "Allow",
        "Principal": {
          "AWS": "$WORKER_IAM_ROLE_ARN"
        },
        "Action": [
          "ecr:BatchCheckLayerAvailability",
          "ecr:BatchGetImage",
          "ecr:CompleteLayerUpload",
          "ecr:DescribeImages",
          "ecr:DescribeRepositories",
          "ecr:GetDownloadUrlForLayer",
          "ecr:InitiateLayerUpload",
          "ecr:ListImages",
          "ecr:PutImage",
          "ecr:UploadLayerPart"
        ]
      },
      {
        "Sid": "BackendAndNodePull",
        "Effect": "Allow",
        "Principal": {
          "AWS": [
            "$BACKEND_IAM_ROLE_ARN",
            "$NODE_ROLE_ARN"
          ]
        },
        "Action": [
          "ecr:BatchCheckLayerAvailability",
          "ecr:BatchGetImage",
          "ecr:DescribeImages",
          "ecr:DescribeRepositories",
          "ecr:GetDownloadUrlForLayer",
          "ecr:ListImages"
        ]
      }
    ]
  }')"
```

## 8. Collect the values for connecting your cluster

Print the values you will enter in the Union.ai UI, labelled with the fields they go in:

```shell
printf '%s\n' \
  "Cluster pool form:" \
  "  S3 Bucket          = s3://${METADATA_BUCKET}" \
  "  Account ID         = ${AWS_ACCOUNT_ID}" \
  "  Region             = ${AWS_REGION}" \
  "  Image registry     = ${IMAGE_REGISTRY}" \
  "Connect cluster dialog:" \
  "  System IAM Role ARN = ${BACKEND_IAM_ROLE_ARN}" \
  "  Task IAM Role ARN   = ${WORKER_IAM_ROLE_ARN}" \
  "kubeconfig command: aws eks update-kubeconfig --region ${AWS_REGION} --name ${CLUSTER_NAME}"
```

Keep this output, and keep the shell where `kubectl get nodes` succeeds: you run the agent install from it.

## Important behavior and cleanup

- The wide service-account trust is deliberate, for the agent-selected release namespace and dynamic task namespaces. Restrict `DATAPLANE_NAMESPACE` only when the actual release namespace is known and fixed.
- The data plane chart owns Metrics Server. Do not add the EKS Metrics Server add-on to this cluster.
- This guide does not configure automatic expiry. Add S3 and ECR lifecycle rules before production use.
- To remove the environment, delete the cluster and its node group with `eksctl delete cluster`, then empty and delete both S3 buckets, delete the ECR repository, and delete the two IAM roles and their inline policies. Review every target before deletion.

## Next steps

**[Connect your cluster](./connect-a-cluster).** Create an AWS cluster pool with the values above, register the cluster, and install the agent.
