---
title: Enabling AWS ECR
description: Give the data plane access to the ECR registry holding your task images.
icon: archive
weight: 2
variants: -flyte +union
---

# Enabling AWS ECR

## Access to ECR in the same account is enabled by default

When registering tasks and workflows, the Union.ai infrastructure in your data plane must have access to the container registry that holds the task container images you will be using.
If your data plane is on AWS then you may want to use AWS Elastic Container Registry (ECR) to store these images.

For details on how to use ECR when building and deploying your workflows, see the ImageSpec with ECR documentation.

**In most cases, you will be using an ECR instance in the same AWS account as your data plane.**
**If this is the case, then you do not need to configure anything.**
**Access to ECR in the same account is enabled by default.**

## Enabling cross-account access to ECR

If you want to store your task container images in an ECR instance in an AWS account _other than the one that holds your data plane_, then you will have to configure that ECR instance to permit access from your data plane.
Here are the details:

* Your Union.ai data plane comes pre-configured with a specific role, which we will refer to here as `<FlyteWorkerNodeGroupRole>`.
* The actual name of this role is of the form `unionai-<ClusterName>-eks-flyteworker-node-group`, where `<ClusterName>` is your EKS cluster's name without the `opta-` prefix. To find it, search **IAM > Roles** for `flyteworker-node-group`.

To enable access to the ECR instance in the other account, do the following:

* In your data plane AWS account, Go to **IAM > Roles**.
Find the role `<FlyteWorkerNodeGroupRole>` and copy the ARN of that role.
We will call this `<FlyteWorkerNodeGroupRoleARN>`.
* In the other AWS account (the one that contains the ECR instance), go to **Amazon ECR > Repositories**,
* Find the ECR repository you want to enable and under **Permissions**, select **Edit,** then **Add Statement**.
* Specify the `<FlyteWorkerNodeGroupRoleARN>` as a **Principal** and add (at least) the following permissions:
  * `ecr:BatchCheckLayerAvailability`: This permission allows your data plane to check the availability of image layers in the registry.
  * `ecr:GetDownloadUrlForLayer`: This permission allows your data plane to retrieve a pre-signed URL that is required to download the image layers.
  * `ecr:BatchGetImage`: This permission allows your data plane to retrieve image manifests and image layer information from the registry.
* To specify the above parameters via JSON, select **Edit policy JSON** and use the following policy document:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowPull",
      "Effect": "Allow",
      "Principal": {
        "AWS": "<FlyteWorkerNodeGroupRoleARN>"
      },
      "Action": [
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchGetImage",
        "ecr:BatchCheckLayerAvailability"
      ]
    }
  ]
}
```

* Select **Save**.

Your Union.ai data plane infrastructure should now be able to pull images from the ECR instance. For more information see [How can I allow a secondary account to push or pull images in my Amazon ECR image repository?](https://repost.aws/knowledge-center/secondary-account-access-ecr)

## Building on a base image from another account

The policy above lets tasks _run_ on images stored in the other account.
If you instead use one of those images as a base and build on top of it with the remote `ImageBuilder` (for example, `flyte.Image.from_base(...)` followed by `with_*` layers), the policy is not enough on its own: the build fails with `401 Unauthorized` because `ImageBuilder` doesn't send credentials to that registry by default.
To fix this, create an `image_pull` secret that configures the `ecr-login` credential helper for the registry and pass it as `registry_secret`.
See [Pulling a base image from ECR in another AWS account](../../../user-guide/tasks/task-configuration/container-images#pulling-a-base-image-from-ecr-in-another-aws-account).
