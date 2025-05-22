---
title: PyTorch Distributed
weight: 1
variants: +flyte -serverless -byoc -selfmanaged
sidebar_expanded: false
---

# PyTorch Distributed

The Kubeflow PyTorch plugin leverages the [Kubeflow training operator](https://github.com/kubeflow/training-operator)
to offer a highly streamlined interface for conducting distributed training using different PyTorch backends.

## Install the plugin

To use the PyTorch plugin, run the following command:

```shell
$ pip install flytekitplugins-kfpytorch
```

To enable the plugin in the backend, follow instructions outlined in the {ref}`deployment-plugin-setup-k8s` guide.

## Run the example on the Flyte cluster

To run the provided examples, use the following commands:

Distributed pytorch training:

```shell
$ pyflyte run --remote pytorch_mnist.py pytorch_training_wf
```

Pytorch lightning training:

```shell
$ pyflyte run --remote pytorch_lightning_mnist_autoencoder.py train_workflow
```


