---
title: Deploy on Amazon EKS
description: Install onebox on Amazon EKS with an RDS for PostgreSQL database and an S3 bucket, using IAM roles for service accounts.
icon: amazon
weight: 2
variants: -flyte +union
---

# Deploy on Amazon EKS

This guide installs onebox on an existing Amazon EKS cluster, with an RDS for PostgreSQL database and an S3 bucket. Onebox and its task pods reach the bucket through an IAM role for service accounts (IRSA), so no AWS keys are stored in the cluster.

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

Onebox connects with TLS (`database.sslMode: require`), which RDS supports by default.

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

Onebox and the task pods both need the bucket. Onebox runs as the `onebox` service account; task pods run as the namespace's `default` service account unless a task asks for another one. Create one role that both can assume.

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
        "system:serviceaccount:${NAMESPACE}:onebox",
        "system:serviceaccount:${NAMESPACE}:default"
      ]}
    }
  }]
}
EOF
aws iam create-role --role-name onebox --assume-role-policy-document file://trust-policy.json
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
aws iam put-role-policy --role-name onebox --policy-name onebox-s3 --policy-document file://s3-policy.json
```

## Install onebox

Create the namespace and the database password Secret, and let task pods assume the role:

```shell
kubectl create namespace ${NAMESPACE}
kubectl -n ${NAMESPACE} create secret generic onebox-db --from-literal=password='<password>'
kubectl -n ${NAMESPACE} annotate serviceaccount default \
  eks.amazonaws.com/role-arn=arn:aws:iam::${AWS_ACCOUNT_ID}:role/onebox
```

Save this as `values.yaml`, with your RDS endpoint:

```yaml
database:
  host: <rds-endpoint>.rds.amazonaws.com
  name: union
  user: union
  existingSecret: onebox-db
storage:
  type: s3
  bucket: <bucket>
  region: <region>
serviceAccount:
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::<account-id>:role/onebox
```

Install the chart:

```shell
helm repo add unionai https://unionai.github.io/helm-charts
helm repo update
helm install onebox unionai/onebox -n ${NAMESPACE} -f values.yaml --wait --timeout 10m
```

Install onebox in a namespace of its own: task pods, their secrets, and the objects plugins create all live in it.

## Check it

```shell
kubectl -n ${NAMESPACE} port-forward svc/onebox 8080:80
```

Open [http://localhost:8080/v2](http://localhost:8080/v2), and run a workflow as in [Install the chart on k3d](./local-k3d#run-a-workflow).

Anyone who can reach port `80` can use onebox until you put an authenticating proxy in front of it. To expose onebox to your users behind an ALB with single sign-on, see [Authentication](./authentication#aws-alb).

## Troubleshooting

| Symptom | Cause and fix |
|---|---|
| The onebox pod restarts with `connection refused` or a timeout to the database | The RDS security group doesn't allow the nodes. Allow port `5432` from the nodes' security group. |
| `AccessDenied` from S3 in onebox's logs | The `onebox` service account can't assume the role. Check the annotation, and that the trust policy names `system:serviceaccount:<namespace>:onebox`. |
| Tasks fail reading their inputs with `AccessDenied` | The namespace's `default` service account isn't annotated, or the trust policy doesn't name it. |
