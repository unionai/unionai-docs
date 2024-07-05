# Setting up container image handling

:::{admonition} Differences between BYOC and Serverless
This section applies to the BYOC version of Union. The Serverless version uses `ImageBuilder` to build and push images and does not require the setup described here.
:::

With Union, each task in a workflow typically runs within its own dedicated container, which has an associated container image. When you deploy your workflow, the images defined by the `ImageSpec` objects in your code are built on your local machine and pushed to a container registry, from which they are later pulled by Union when the workflow is executed.

We will explain how to define `ImageSpec` objects [later in this section](understanding-the-workflow-code).
For now, we will just cover setting up the necessary tools and access.

:::{admonition} Default image
If no image is specified for a task, Union will use a default image that is provided by the system.
For example, the code in the [Quick start guide](../quick-start) did not explicitly specify an image.
:::

## Prerequisites

You will need to have:

* A container engine, like Docker, installed locally.
* Access to a container registry, like GitHub Container Registry.

## Install Docker

Install [Docker](https://docs.docker.com/get-docker/) on your local machine and ensure that the associated client daemon is up and running.

:::{note}
Any [OCI-compatible](https://opencontainers.org/) container engine like [Podman](https://podman.io/),
[LXD](https://linuxcontainers.org/lxd/introduction/), or [Containerd](https://containerd.io/) should also work.
:::

## Get access to a container registry

In this example, we assume you will be using the GitHub Container Registry (GHCR) that comes as part of your GitHub account. For more information, see [Working with the Container registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry).

You may use another container registry if you prefer, such as [Docker Hub](https://hub.docker.com/), [Amazon Elastic Container Registry (ECR)](../integrations/enabling-aws-resources/enabling-aws-ecr), or [Google Artifact Registry (GAR)](../integrations/enabling-gcp-resources/enabling-google-artifact-registry).

:::{admonition} Specifying your registry in the `ImageSpec`
Later in the process, we will show you where to specify the name of your registry (in this case, the name of your GitHub organization) in the `ImageSpec` object in your Python code.
:::

## Authenticate to the registry

You will need to set up your local Docker client to authenticate with GHCR in order for `unionai` to be able to push the image built according to the `ImageSpec` to GHCR.

Follow the directions in [Working with the Container registry > Authenticating to the Container registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry.md#authenticating-to-the-container-registry).

:::{admonition} Making your image publicly accessible
In addition to making sure your registry is accessible from your local machine, you will need to ensure that the specific image, once pushed to the registry, is itself publicly accessible.

However, this step can ony be done once the image *has been* pushed, which comes later in the process.
We will call out the need to make the image publicly accessible at that time.
:::

## Next step

The next step is [Running the workflow](running-the-workflow).
