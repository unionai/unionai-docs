---
title: MPI
weight: 1
variants: +flyte -serverless -byoc -selfmanaged
sidebar_expanded: false
---

# MPI

In this section, you'll find a demonstration of running Horovod code with the Kubeflow MPI API.

## Horovod

[Horovod](http://horovod.ai/) stands as a distributed deep learning training framework compatible with
TensorFlow, Keras, PyTorch and Apache MXNet. Its primary objective is to enhance the speed and usability
of distributed deep learning through the implementation of ring-allreduce. This technique necessitates
just a few minimal modifications to the user's code, thereby simplifying the process of distributed deep learning.

## MPI (Message Passing Interface)

The Flyte platform employs the [Kubeflow training operator](https://github.com/kubeflow/training-operator),
to facilitate streamlined execution of all-reduce-style distributed training on Kubernetes.
This integration offers a straightforward interface for conducting distributed training through the utilization of MPI.

The combined power of MPI and Horovod can be harnessed to streamline the complexities of distributed training.
The MPI API serves as a convenient encapsulation to execute Horovod scripts, thereby enhancing the overall efficiency of the process.

## Install the plugin

Install the MPI plugin by running the following command:

```shell
$ pip install flytekitplugins-kfmpi
```

## Build a Docker image

The Dockerfile should include installation commands for various components, including MPI and Horovod.

```dockerfile
FROM ubuntu:focal
LABEL org.opencontainers.image.source https://github.com/flyteorg/flytesnacks

WORKDIR /root
ENV VENV /opt/venv
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONPATH /root
ENV DEBIAN_FRONTEND=noninteractive

# Install Python3.10 and other libraries
RUN apt-get update \
    && apt-get install -y software-properties-common \
    && add-apt-repository ppa:ubuntu-toolchain-r/test \
    && add-apt-repository -y ppa:deadsnakes/ppa \
    && apt-get install -y \
    build-essential \
    cmake \
    g++-7 \
    curl \
    git \
    wget \
    python3.10 \
    python3.10-venv \
    python3.10-dev \
    make \
    libssl-dev \
    python3-pip \
    python3-wheel \
    libuv1

# Virtual environment
ENV VENV /opt/venv
RUN python3.10 -m venv ${VENV}
ENV PATH="${VENV}/bin:$PATH"

ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

# Install wheel after venv is activated
RUN pip3 install wheel

# Install Open MPI
RUN wget --progress=dot:mega -O /tmp/openmpi-4.1.4-bin.tar.gz https://download.open-mpi.org/release/open-mpi/v4.1/openmpi-4.1.4.tar.gz && \
    cd /tmp && tar -zxf /tmp/openmpi-4.1.4-bin.tar.gz && \
    mkdir openmpi-4.1.4/build && cd openmpi-4.1.4/build && ../configure --prefix=/usr/local && \
    make -j all && make install && ldconfig && \
    mpirun --version

# Allow OpenSSH to talk to containers without asking for confirmation
RUN mkdir -p /var/run/sshd
RUN cat /etc/ssh/ssh_config | grep -v StrictHostKeyChecking > /etc/ssh/ssh_config.new && \
    echo "    StrictHostKeyChecking no" >> /etc/ssh/ssh_config.new && \
    mv /etc/ssh/ssh_config.new /etc/ssh/ssh_config

# Install Python dependencies
COPY requirements.in /root
RUN pip install -r /root/requirements.in

# Install TensorFlow
# In case you encounter the "The TensorFlow library was compiled to use AVX instructions, which are not present on your machine" error,
# you can resolve it by installing TensorFlow using the following RUN instruction:
# RUN wget https://tf.novaal.de/westmere/tensorflow-2.8.0-cp310-cp310-linux_x86_64.whl && pip install tensorflow-2.8.0-cp310-cp310-linux_x86_64.whl
# Otherwise:
RUN pip install tensorflow==2.8.0

# Enable GPU
# ENV HOROVOD_GPU_OPERATIONS NCCL
RUN HOROVOD_WITH_MPI=1 pip install --no-cache-dir horovod==0.28.1

# Copy the actual code
COPY . /root/

# This tag is supplied by the build script and will be used to determine the version
# when registering tasks, workflows, and launch plans
ARG tag
ENV FLYTE_INTERNAL_IMAGE $tag
```

## Run the example on the Flyte cluster

To run the provided example on the Flyte cluster, use the following command:

```shell
$ pyflyte run --remote \
  --image ghcr.io/flyteorg/flytecookbook:kfmpi_plugin-latest \
  https://raw.githubusercontent.com/flyteorg/flytesnacks/master/examples/kfmpi_plugin/kfmpi_plugin/mpi_mnist.py \
  horovod_training_wf
```

## MPI Plugin Troubleshooting Guide

This section covers common issues encountered during the setup of the MPI operator for distributed training jobs on Flyte.

**Worker Pods Failing to Start (Insufficient Resources)**

MPI worker pods may fail to start or exhibit scheduling issues, leading to job timeouts or failures. This often occurs due to resource constraints (CPU, memory, or GPU) in the cluster.

1. Adjust Resource Requests:
Ensure that each worker pod has sufficient resources. You can adjust the resource requests in your task definition:

```python
requests=Resources(cpu="<your_cpu_request>", mem="<your_mem_request>")
```

Modify the CPU and memory values according to your cluster's available resources. This helps prevent pod scheduling failures caused by resource constraints.

2. Check Pod Logs for Errors:
If the worker pods still fail to start, check the logs for any related errors:

```shell
$ kubectl logs <pod-name> -n <namespace>
```

Look for resource allocation or worker communication errors.

**Workflow Registration Method Errors (Timeouts or Deadlocks)**

If your MPI workflow hangs or times out, it may be caused by an incorrect workflow registration method.

1. Verify Registration Method:
    When using a custom image, refer to the Flyte documentation on [Registering workflows](../../../user-guide/development-cycle/running-your-code) to ensure you're following the correct registration method.
