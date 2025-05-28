---
title: Enabling AWS S3
weight: 1
variants: -flyte -serverless +byoc -selfmanaged
---

# Enabling AWS S3

For {{< key product_name >}} customers whose data plane is in AWS, we walk through setting up access to your own AWS S3 bucket.

> [!NOTE] AWS S3 in the {{< key product_name >}} environment
> Your data plane is set up with a Kubernetes cluster and other resources.
> Among these are a number of S3 buckets used internally by the {{< key product_name >}} operator running in the cluster (see [Platform architecture](../platform-architecture)) to store things like workflow metadata.
>
> **These **_**are not**_** the S3 bucket we are talking about in this section.**
>
> **We are discussing the case where you have **_**your own S3 bucket**_** that you set up to store input and output data used by your workflows.**

## Add permissions to your custom policy

In order to enable access to an AWS resource (in this case S3) you need to create a custom policy in AWS IAM with the required permissions and attach it to either the existing _User Flyte Role_ associated with your data plane Kubernetes cluster or to a custom role which you have created and attached to the cluster.
The general procedure is covered in [Enabling AWS resources](.).

_In order to enable S3 access in particular, in the step_ [#add-permissions-to-your-custom-policy](./enabling-aws-s3#add-permissions-to-your-custom-policy) _you must specify the needed permissions. For example:_

- `s3:ListBucket` - This permission allows you to list the objects in the bucket.
- `s3:GetObject` - This permission allows you to retrieve objects from the bucket.
- `s3:PutObject` - This permission allows you to upload objects to the bucket.

Here is a sample JSON policy document that grants these permissions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowReadWriteBucket",
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket",
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": [
        "arn:aws:s3:::<BucketName>/*",
        "arn:aws:s3:::<BucketName>"
      ]
    }
  ]
}
```

In the `Resource` field, replace `<BucketName>` with the actual name of your S3 bucket.

## Accessing S3 from your task code

Once you have enabled access to your S3 bucket, you can use the standard [AWS SDK for Python (Boto3)](https://aws.amazon.com/sdk-for-python/) in your task code to read and write to it.
