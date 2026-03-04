---
title: Image Builder
variants: -flyte -serverless +byoc +selfmanaged
weight: 2
---

# Image Builder

Union Image Builder supports the ability to build container images within the dataplane. For details about this feature, please visit [Image Builder](../../../deployment/configuration/image-builder.md).

## Authentication

By default, Union is intended to be configured to use [IAM roles for service accounts (IRSA)](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) for authentication. Setting `authenticationType` to `aws` configures Union image builder related services to use AWS default credential chain. Additionally, Union image builder uses [`docker-credential-ecr-login`](https://github.com/awslabs/amazon-ecr-credential-helper) to authenticate to the ecr repository configured with `defaultRepository`.

`defaultRepository` should be the full qualified ecr repository named `<AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/<REPOSITORY_NAME>`.

Therefore, it is necessary to configure the user role with permissions the following permissions.

```json
{
  "Effect": "Allow",
  "Action": [
    "ecr:GetAuthorizationToken"
  ],
  "Resource": "*"
},
{
  "Effect": "Allow",
  "Action": [
    "ecr:BatchCheckLayerAvailability",
    "ecr:BatchGetImage",
    "ecr:GetDownloadUrlForLayer"
  ],
  "Resource": "*"
  // Or
  // "Resource": "arn:aws:ecr:<AWS_REGION>:<AWS_ACCOUNT_ID>:repository/<REPOSITORY>"
}
```

Simarly, the `operator-proxy` requires the following permissions

```json
{
  "Effect": "Allow",
  "Action": [
    "ecr:GetAuthorizationToken"
  ],
  "Resource": "*"
},
{
  "Effect": "Allow",
  "Action": [
    "ecr:DescribeImages"
  ],
  "Resource": "arn:aws:ecr:<AWS_REGION>:<AWS_ACCOUNT_ID>:repository/<REPOSITORY>"
}
```

### AWS Cross Account access

Access to repositories that do not exist in the same AWS account as the data plane requires additional ECR resource-based permissions. An ECR policy like the following is required if the configured `defaultRepository` or ImageSpec's `registry` exists in an AWS account different from the dataplane's.

```json
{
  "Statement": [
    {
      "Sid": "AllowPull",
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::<DATAPLANE_AWS_ACCOUNT>:role/<user-role>",
          "arn:aws:iam::<DATAPLANE_AWS_ACCOUNT>:role/<node-role>"
          // ... Additional roles that require image pulls
        ]
      },
      "Action": [
        "ecr:BatchCheckLayerAvailability",
        "ecr:BatchGetImage",
        "ecr:GetDownloadUrlForLayer"
      ]
    },
    {
      "Sid": "AllowDescribeImages",
      "Action": ["ecr:DescribeImages"],
      "Principal": {
        "AWS": [
          "arn:aws:iam::<DATAPLANE_AWS_ACCOUNT>:role/<operator-proxy-role>"
        ]
      },
      "Effect": "Allow"
    },
    {
      "Sid": "ManageRepositoryContents"
      // ...
    }
  ],
  "Version": "2012-10-17"
}
```

In order to support a private ImageSpec `base_image` the following permissions are required.

```json
{
  "Statement": [
    {
      "Sid": "AllowPull",
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::<DATAPLANE_AWS_ACCOUNT>:role/<user-role>",
          "arn:aws:iam::<DATAPLANE_AWS_ACCOUNT>:role/<node-role>"
          // ... Additional roles that require image pulls
        ]
      },
      "Action": [
        "ecr:BatchCheckLayerAvailability",
        "ecr:BatchGetImage",
        "ecr:GetDownloadUrlForLayer"
      ]
    }
  ]
}
```
