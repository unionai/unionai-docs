# ImageSpec with ECR

In this section we explain how to set up and use AWS Elastic Container Registry (ECR) to build and deploy task container images using `ImageSpec`.

## Prerequisites

If you are using ECR in the same AWS account as your Union data plane, then you do not need to configure anything. Access to ECR in the same account is enabled by default.

If you want to store your task container images in an ECR instance in an AWS account _other than the one that holds your data plane_, then you will have to configure that ECR instance to permit access from your data plane. See [Enable AWS ECR](../../../integrations/enabling-aws-resources/enabling-aws-ecr) for details.

## Set up the image repository

Unlike GitHub Container Registry, ECR does not allow you to simply push an arbitrarily named image to the registry. Instead, you must first create a repository in the ECR instance and then push the image to that repository.

:::{admonition} Registry, repository, and image

In ECR terminology the **registry** is the top-level storage service. The registry holds a collection of **repositories**. Each repository corresponds to a named image and holds all versions of that image.

When you push an image to a registry, you are actually pushing it to a repository within that registry. Strictly speaking, the term *image* refers to a specific *image version* within that repository.

:::


This means that you have to decide on the name of your image and create a repository by that name first, before registering your workflow.

Adapting the example from the [previous section](./index.md), we will assume the following

* The ECR instance you will be using has the base URL `123456789012.dkr.ecr.us-eas-1.amazonaws.com`.

* Your image will be called `simple-example-image`.

In the AWS console, go to **Amazon ECR > Repositories**. If you are in the same account as your Union data plane you should go directly to the ECR registry that was set up for you by Union. If there are multiple ECR registries present, consult with your Union administrator to find out which one to use.

Once you are in the correct ECR registry, under **Create a Repository**, click **Get Started**:

![]/_static/images/create-repository-1.png)

On the **Create repository** page:

* Select **Private** for the repository visibility, assuming you want to make it private. You can, alternatively, select **Public**, but in most cases, the main reason for using ECR is to keep your images private.

* Enter the name of the repository:

![]/_static/images/create-repository-2.png)

and then scroll down to click **Create repository**:

![]/_static/images/create-repository-3.png)

Your repository is now created.

## Authenticate to the registry

You will need to set up your local Docker client to authenticate with ECR. This is needed for `union` to be able to push the image built according to the `ImageSpec` to ECR.

To do this, you will need to [install the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html), use it to run the `aws ecr get-login-password` command to get the appropriate password, then perform a `docker login` with that password.

See [Private registry authentication](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html) for details.

## Register your workflow to Union

You can register tasks with `ImageSpec` declarations that reference this repository.

For example, to use the example repository shown here, we would alter the Python code in the [previous section](./index.md), to have the following `ImageSpec` declaration:

```{code-block} python
image_spec = ImageSpec(
    registry="123456789012.dkr.ecr.us-eas-1.amazonaws.com",
    name="simple-example-image",
    base_image="ghcr.io/flyteorg/flytekit:py3.11-latest",
    requirements="image-requirements.txt"
)
```

