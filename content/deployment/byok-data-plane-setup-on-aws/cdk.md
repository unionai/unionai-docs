---
title: Setup with AWS CDK
weight: 1
variants: -flyte -serverless -byoc +selfmanaged
---

# Setup with AWS CDK

You can automate the provisioning of your {{< key product_name >}} data plane on AWS using [AWS Cloud Development Kit (CDK)](https://aws.amazon.com/cdk/) and [EKS Blueprints](https://aws-quickstart.github.io/cdk-eks-blueprints/).

The [`@unionai/union-eks-blueprints-addon`](https://www.npmjs.com/package/@unionai/union-eks-blueprints-addon) package provides CDK constructs that deploy the {{< key product_name >}} data plane onto an EKS cluster, including all required IAM roles, Helm charts, and Kubernetes resources.

## Prerequisites

- [Node.js](https://nodejs.org/) >= 18
- [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) v2 installed and bootstrapped in your target account/region
- [npm](https://www.npmjs.com/) or another Node.js package manager
- A {{< key product_name >}} organization with the following information (provided by the {{< key product_name >}} team):
  - **Control plane host** (e.g. `your-org.hosted.unionai.cloud`)
  - **Organization name**
  - **Cluster name** registered with {{< key product_name >}}
  - **Client ID** and **Client Secret** for authentication

## Installation

Install the addon package in your CDK project:

```bash
npm install @unionai/union-eks-blueprints-addon
```

## Store your credentials in AWS Secrets Manager

The addon retrieves {{< key product_name >}} credentials from AWS Secrets Manager. Create a secret containing both the client ID and client secret as a JSON object:

```bash
aws secretsmanager create-secret \
  --name "union/credentials" \
  --secret-string '{"clientId": "<YOUR_CLIENT_ID>", "clientSecret": "<YOUR_CLIENT_SECRET>"}'
```

## Create your CDK stack

The following example creates an EKS cluster with [EKS Auto Mode](https://docs.aws.amazon.com/eks/latest/userguide/automode.html) enabled and deploys the {{< key product_name >}} data plane onto it:

```typescript
import * as cdk from 'aws-cdk-lib';
import * as blueprints from "@aws-quickstart/eks-blueprints"
import * as union from "@unionai/union-eks-blueprints-addon"

const app = new cdk.App();

const account = process.env.CDK_DEFAULT_ACCOUNT;
const region = process.env.CDK_DEFAULT_REGION;
let props = { env: { account, region } };

const unionBlueprint = blueprints.AutomodeBuilder.builder({})
  .resourceProvider(
    'union-bucket',
    new blueprints.CreateS3BucketProvider({
      id: 'my-union-bucket-123',
      s3BucketProps: { bucketName: 'union-bucket' }
    })
  )
  .addOns(
    new blueprints.addons.MetricsServerAddOn(),
    new union.UnionDataplaneCRDsAddOn(),
    new union.UnionDataplaneAddOn({
      s3BucketProviderName: 'union-bucket',
      clusterName: "<YOUR_UNION_CLUSTER_NAME>",
      unionSecretName: "<YOUR_UNION_SECRET_NAME>",
      host: "<YOUR_UNION_CONTROL_PLANE_HOST>",
      orgName: "<YOUR_ORG_NAME>"
    })
  )
  .build(app, "union-blueprint", props);
```

Replace the placeholder values:

| Parameter | Description |
| --- | --- |
| `s3BucketProviderName` | Name of the S3 bucket resource provider registered with the blueprint. Must match the name passed to `resourceProvider()`. |
| `clusterName` | Name of the cluster registered with {{< key product_name >}}. Provided by the {{< key product_name >}} team. |
| `unionSecretName` | Name of the AWS Secrets Manager secret containing your {{< key product_name >}} credentials. |
| `host` | Your {{< key product_name >}} control plane URL (without `https://`). |
| `orgName` | Your {{< key product_name >}} organization name. |

## Deploy

Once your CDK stack is defined, deploy it:

```bash
cdk deploy union-blueprint
```

## What gets provisioned

The addon deploys the following resources:

- **UnionDataplaneCRDsAddOn**: Installs the {{< key product_name >}} Custom Resource Definitions (CRDs) required by the data plane operator.
- **UnionDataplaneAddOn**: Deploys the {{< key product_name >}} data plane Helm chart, which includes:
  - An IAM policy granting read/write access to the configured S3 bucket.
  - An IAM role with OIDC federation for Kubernetes service accounts.
  - The data plane operator and supporting services.

## Using an existing S3 bucket

If you already have an S3 bucket, use `ImportS3BucketProvider` instead of `CreateS3BucketProvider`:

```typescript
.resourceProvider(
  'union-bucket',
  new blueprints.ImportS3BucketProvider('my-existing-bucket-name')
)
```

## Additional configuration

The `UnionDataplaneAddOn` accepts additional Helm values through the `values` property, which are merged with the defaults. Refer to the {{< key product_name >}} Helm chart documentation for available options.
