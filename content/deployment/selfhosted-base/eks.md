---
title: Deploy on Amazon EKS
description: Install Self-Hosted Base on Amazon EKS with an RDS for PostgreSQL database and an S3 bucket, using IAM roles for service accounts.
icon: amazon
weight: 2
variants: -flyte +union
---

# Deploy on Amazon EKS

This guide installs Self-Hosted Base on an existing Amazon EKS cluster, with an RDS for PostgreSQL database and an S3 bucket. Self-Hosted Base and its task pods reach the bucket through an IAM role for service accounts (IRSA), so no AWS keys are stored in the cluster.

## Prerequisites

- An EKS cluster, and `kubectl` configured for it.
- The AWS CLI, `eksctl`, and [Helm](https://helm.sh) 3.

Set these for the commands below:

```shell
export CLUSTER_NAME=<your EKS cluster>
export AWS_REGION=<region>
export BUCKET=<globally unique bucket name>
export NAMESPACE=union
export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
```

## Create the database

Create an RDS for PostgreSQL instance in the cluster's VPC, and allow inbound connections on port `5432` from the cluster nodes' security group. Then create a database and a user that owns it, for example from a `psql` session as the master user:

```sql
CREATE USER union WITH PASSWORD '<password>';
CREATE DATABASE union OWNER union;
```

Self-Hosted Base connects with TLS (`database.sslMode: require`), which RDS supports by default.

For thousands of tasks at once, give the instance a `max_connections` of at least 300. RDS sets `max_connections` from the instance's memory, so a small instance can allow fewer; raise it in the instance's parameter group. See [Sizing](./_index#sizing).

## Create the bucket

```shell
aws s3api create-bucket --bucket ${BUCKET} --region ${AWS_REGION} \
  --create-bucket-configuration LocationConstraint=${AWS_REGION}
```

In `us-east-1`, leave out `--create-bucket-configuration`.

Let the UI read objects from it (see [Bucket CORS](./_index#bucket-cors)), with the address your users open:

```shell
cat > cors.json <<EOF
{"CORSRules": [{"AllowedOrigins": ["https://<host>"], "AllowedMethods": ["GET", "HEAD"],
                "AllowedHeaders": ["*"], "MaxAgeSeconds": 3600}]}
EOF
aws s3api put-bucket-cors --bucket ${BUCKET} --cors-configuration file://cors.json
```

## Create the IAM role

Self-Hosted Base and the task pods both need the bucket. Self-Hosted Base runs as the `selfhosted-base` service account; task pods run as the namespace's `default` service account unless a task asks for another one. Create one role that both can assume.

Enable the cluster's OIDC provider, if it isn't already:

```shell
eksctl utils associate-iam-oidc-provider --cluster ${CLUSTER_NAME} --region ${AWS_REGION} --approve
export OIDC_PROVIDER=$(aws eks describe-cluster --name ${CLUSTER_NAME} --region ${AWS_REGION} \
  --query "cluster.identity.oidc.issuer" --output text | sed 's|https://||')
```

Create the role, trusted by the two service accounts:

```shell
cat > trust-policy.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"Federated": "arn:aws:iam::${AWS_ACCOUNT_ID}:oidc-provider/${OIDC_PROVIDER}"},
    "Action": "sts:AssumeRoleWithWebIdentity",
    "Condition": {
      "StringEquals": {"${OIDC_PROVIDER}:aud": "sts.amazonaws.com"},
      "ForAnyValue:StringEquals": {"${OIDC_PROVIDER}:sub": [
        "system:serviceaccount:${NAMESPACE}:selfhosted-base",
        "system:serviceaccount:${NAMESPACE}:default"
      ]}
    }
  }]
}
EOF
aws iam create-role --role-name selfhosted-base --assume-role-policy-document file://trust-policy.json
```

Give it the bucket:

```shell
cat > s3-policy.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["s3:GetObject*", "s3:PutObject*", "s3:DeleteObject*", "s3:ListBucket", "s3:GetBucketLocation"],
    "Resource": ["arn:aws:s3:::${BUCKET}", "arn:aws:s3:::${BUCKET}/*"]
  }]
}
EOF
aws iam put-role-policy --role-name selfhosted-base --policy-name selfhosted-base-s3 --policy-document file://s3-policy.json
```

## Install Self-Hosted Base

Create the namespace and the database password Secret, and let task pods assume the role:

```shell
kubectl create namespace ${NAMESPACE}
kubectl -n ${NAMESPACE} create secret generic selfhosted-base-db --from-literal=password='<password>'
kubectl -n ${NAMESPACE} annotate serviceaccount default \
  eks.amazonaws.com/role-arn=arn:aws:iam::${AWS_ACCOUNT_ID}:role/selfhosted-base
```

Save this as `values.yaml`, with your RDS endpoint:

```yaml
database:
  host: <rds-endpoint>.rds.amazonaws.com
  name: union
  user: union
  existingSecret: selfhosted-base-db
storage:
  type: s3
  bucket: <bucket>
  region: <region>
serviceAccount:
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::<account-id>:role/selfhosted-base
```

Install the chart:

```shell
helm repo add unionai https://unionai.github.io/helm-charts
helm repo update
helm install selfhosted-base unionai/selfhosted-base -n ${NAMESPACE} -f values.yaml --wait --timeout 10m
```

Install Self-Hosted Base in a namespace of its own: task pods, their secrets, and the other Kubernetes objects created for tasks all live in it.

## Check it

```shell
kubectl -n ${NAMESPACE} port-forward svc/selfhosted-base 8080:80
```

Open [http://localhost:8080/v2](http://localhost:8080/v2), and run a workflow as in [Install the chart on k3d](./local-k3d#run-a-workflow).

Anyone who can reach port `80` can use Self-Hosted Base until you put an authenticating proxy in front of it. To expose Self-Hosted Base to your users behind an ALB with single sign-on, see [Authentication](./authentication#aws-alb).

## Troubleshooting

| Symptom | Cause and fix |
|---|---|
| The Self-Hosted Base pod restarts with `connection refused` or a timeout to the database | The RDS security group doesn't allow the nodes. Allow port `5432` from the nodes' security group. |
| `AccessDenied` from S3 in Self-Hosted Base's logs | The `selfhosted-base` service account can't assume the role. Check the annotation, and that the trust policy names `system:serviceaccount:<namespace>:selfhosted-base`. |
| Tasks fail reading their inputs with `AccessDenied` | The namespace's `default` service account isn't annotated, or the trust policy doesn't name it. |
| The Self-Hosted Base pod restarts with `OOMKilled` | Its memory limit is too small for the actions in flight; 2 GiB holds about 13,000. Raise `resources`; see [Sizing](./_index#sizing). Self-Hosted Base before 2026.11.14 needs about 1 GiB plus 1 MiB for each action queued or running. |
| Tasks stay queued while the cluster has room for them | Self-Hosted Base runs at most 500 tasks at once. Raise `extraConfig.leaseworker.capacity`; see [Sizing](./_index#sizing). |
