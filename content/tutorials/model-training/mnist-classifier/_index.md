---
title: MNIST classification with PyTorch and W & B
weight: 1
variants: +flyte -serverless -byoc -selfmanaged
sidebar_expanded: false
---

# MNIST Classification With PyTorch and W&B

## PyTorch

[Pytorch](https://pytorch.org) is a machine learning framework that accelerates the path from research prototyping
to production deployment. You can build *Tensors* and *Dynamic neural networks* in Python with strong GPU acceleration
using PyTorch.

In a nutshell, it is a Python package that provides two high-level features:

- Tensor computation (like NumPy) with strong GPU acceleration
- Deep neural networks built on a tape-based autograd system

Flyte directly has no unique understanding of PyTorch. As per Flyte, PyTorch is just a Python library.
However, when merged with Flyte, the combo helps utilize and bootstrap the infrastructure for PyTorch and ensures that things work well!
Additionally, it also offers other benefits of using tasks and workflows -- checkpointing, separation of concerns, and auto-memoization.

## Model Development

Some basics of model development are outlined in the following video, in addition to:

- Bias Variance trade-off
- Model families
- Data parallelism
- Model parallelism, and
- PyTorch parallelism

{{< youtube FuMtJOMh5uQ >}}

## Specify GPU Requirement

One of the necessary directives applicable when working on deep learning models is explicitly requesting one or more GPUs.
This can be done by giving a simple directive to the task declaration as follows:

```python
from flytekit import Resources, task

@task(requests=Resources(gpu="1"), limits=Resources(gpu="1"))
def my_deep_learning_task():
    ...
```

It is recommended to use the same `requests` and `limits` for a GPU as automatic GPU scaling is not supported.

Moreover, to utilize the power of a GPU, ensure that your Flyte backend has GPU nodes provisioned.

## Distributed Data-Parallel Training

Flyte also supports distributed training for PyTorch models using the [PyTorch plugin](../../../integrations/native-backend-plugins/kfpytorch-plugin).

## Weights & Biases Integration

[Weights & Biases](https://wandb.ai/site), or simply, `wandb` helps build better models faster with experiment tracking, dataset versioning, and model management.

We'll use `wandb` alongside PyTorch to track our ML experiment and its concerned model parameters.

> [!NOTE]
> Before running the example, create a `wandb` account and log in to access the API.
> If you're running the code locally, run the command `wandb login`.
> If it's a remote cluster, you have to include the API key in the Dockerfile.

## PyTorch Dockerfile for Deployment

It is essential to build the Dockerfile with GPU support to use a GPU within PyTorch.
The example in this section uses a simple `nvidia-supplied GPU Docker image` as the base, and the rest of the construction is similar to the other Dockerfiles.

```dockerfile
FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-runtime
LABEL org.opencontainers.image.source https://github.com/flyteorg/flytesnacks

WORKDIR /root
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONPATH /root

# Set your wandb API key and user name. Get the API key from https://wandb.ai/authorize.
# ENV WANDB_API_KEY <api_key>
# ENV WANDB_USERNAME <user_name>

# Install the AWS cli for AWS support
RUN pip install awscli

# Install gcloud for GCP
RUN apt-get update && apt-get install -y make build-essential libssl-dev curl

# Virtual environment
ENV VENV /opt/venv
RUN python3 -m venv ${VENV}
ENV PATH="${VENV}/bin:$PATH"

# Install Python dependencies
COPY requirements.in /root
RUN pip install -r /root/requirements.in

# Copy the actual code
COPY . /root/

# This tag is supplied by the build script and will be used to determine the version
# when registering tasks, workflows, and launch plans
ARG tag
ENV FLYTE_INTERNAL_IMAGE $tag
```

> [!NOTE]
> Run your code in the `ml_training` directory, both locally and within the sandbox.
