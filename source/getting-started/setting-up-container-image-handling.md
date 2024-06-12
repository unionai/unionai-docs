# Setting up container image handling

With Union, each task in a workflow typically runs within its own dedicated container.
Since a container requires a container image to run, every task in Union must have a container image associated with it.
When you deploy your workflow, the images defined in your code are built on your local machine and pushed to a container registry,
from which they are later pulled by Union when the workflow is executed.

The standard way to define the container image for a task is though an `ImageSpec` object referenced in your task definition.
We will explain how to do this [later in this section](looking-at-the-workflow-code).
For now, we will just cover setting up the necessary tools and access.

:::{admonition} Default image
If no image is specified for a task, Union will use a default image that is provided by the system.
For example, this is how the code in [Getting started](index) was able to run without specifying an image.
:::

## Prerequisites

You will need to have:

* A container engine, like Docker, installed locally.
* Have access to an image registry.

:::{admonition} Differences between BYOC and Serverless
This section applies to the BYOC version of Union.
If you are using the Serverless version, the system for building and pushing images
differs. It uses the built-in `ImageBuilder` feature.
:::

## Install Docker

We assume here that you have already installed Python and the `unionai` SDK and CLI.
If not, go back to [Getting started](index) and complete that process first.

Next, you need to install [Docker](https://docs.docker.com/get-docker/) on your local machine.
Any [OCI-compatible](https://opencontainers.org/) container engine like [Podman](https://podman.io/), [LXD](https://linuxcontainers.org/lxd/introduction/), or [Containerd](https://containerd.io/) should also work.

Ensure that the associated client daemon is up and running.

## Get access to a container registry

In this example, we assume you will be using the GitHub Container Registry (GHCR) that comes as part of your GitHub account.
For more information, see [Working with the Container registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry).

You may use another container registry if you prefer, such as [Docker Hub](https://hub.docker.com/), [Amazon Elastic Container Registry (ECR)](../integrations/enabling-aws-resources/enabling-aws-ecr), or [Google Artifact Registry (GAR)](../integrations/enabling-gcp-resources/enabling-google-artifact-registry).

:::{admonition} Specifying your registry in the `ImageSpec`
Later in the process, you will need to specify the name of your registry (in this case, the name of your GitHub organization) in the `ImageSpec` object in your Python code.
We will call out the need to do this at that time.
:::

## Authenticate to the registry

You will need to set up your local Docker client to authenticate with GHCR in order for `unionai` to be able to push the image built according to the `ImageSpec` to GHCR.

Follow the directions in [Working with the Container registry > Authenticating to the Container registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry.md#authenticating-to-the-container-registry).

:::{admonition} Making your image publicly accessible
In addition to making sure your registry is accessible from your local machine, you will need to ensure that the specific image, once pushed to the registry, is itself publicly accessible.

However, this step can ony be done once the image *has been* pushed, which comes later in the process.
We will call out the need to make the image publicly accessible at that time.
:::

:::{admonition} Making your image publicly accessible
In addition to making sure your registry is accessible from your local machine, you will need to ensure that the specific image, once pushed to the registry, is itself publicly accessible.

However, this step can ony be done once the image *has been* pushed, which comes later in the process.
We will call out the need to make the image publicly accessible at that time.
:::
