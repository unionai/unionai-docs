---
title: Artifacts on AWS
weight: 1
variants: -flyte +union
---

# Artifacts on AWS

Concrete example of the [generalized Artifacts setup](./_index) on AWS: a dedicated S3 bucket, a lenient lifecycle policy, and an IAM role (via IRSA) that grants the Artifacts service access to just that bucket.

Replace the placeholders — `ARTIFACTS_BUCKET`, `ACCOUNT_ID`, `REGION`, `OIDC_PROVIDER`, `CP_NAMESPACE` — with your values.

## 1. Create the S3 bucket

```bash
aws s3api create-bucket \
  --bucket ARTIFACTS_BUCKET \
  --region REGION \
  --create-bucket-configuration LocationConstraint=REGION
```

Keep public access blocked (the default) — the Artifacts service reaches the bucket through IAM, never public URLs.

## 2. Apply a lenient lifecycle policy

Artifacts are long-lived; the only cleanup you want is aborting orphaned multipart uploads. **Do not** set object-expiration rules on this bucket.

```json
{
  "Rules": [
    {
      "ID": "abort-incomplete-multipart-uploads",
      "Status": "Enabled",
      "Filter": {},
      "AbortIncompleteMultipartUpload": { "DaysAfterInitiation": 7 }
    }
  ]
}
```

```bash
aws s3api put-bucket-lifecycle-configuration \
  --bucket ARTIFACTS_BUCKET \
  --lifecycle-configuration file://artifacts-lifecycle.json
```

> [!NOTE]
> Contrast this with the metadata / offloaded-data bucket, where an aggressive object-expiration rule is appropriate. The two buckets exist so their lifecycles can differ.

## 3. IAM policy for the Artifacts service

Grant object read/write scoped to the bucket:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ArtifactsBucketObjects",
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
      "Resource": "arn:aws:s3:::ARTIFACTS_BUCKET/*"
    },
    {
      "Sid": "ArtifactsBucketList",
      "Effect": "Allow",
      "Action": ["s3:ListBucket"],
      "Resource": "arn:aws:s3:::ARTIFACTS_BUCKET"
    }
  ]
}
```

Attach it to a role that the Artifacts pod's service account can assume via [IRSA](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html). The role's trust policy binds it to the control-plane namespace's `artifacts` service account:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "Federated": "arn:aws:iam::ACCOUNT_ID:oidc-provider/OIDC_PROVIDER" },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "OIDC_PROVIDER:sub": "system:serviceaccount:CP_NAMESPACE:artifacts",
          "OIDC_PROVIDER:aud": "sts.amazonaws.com"
        }
      }
    }
  ]
}
```

## 4. Values

The chart's `values.aws.yaml` overlay already annotates the `artifacts` service account with the role ARN and selects the S3 object-store backend. You only set the globals and the enable toggle in your environment overrides:

```yaml
global:
  ARTIFACTS_BUCKET_NAME: "ARTIFACTS_BUCKET"
  ARTIFACT_IAM_ROLE_ARN: "arn:aws:iam::ACCOUNT_ID:role/union-artifacts"

services:
  artifacts:
    disabled: false
```

Return to the [generalized guide](./_index) for verification steps.
