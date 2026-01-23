---
title: Pytorch
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: false
---
# Pytorch

Flyte can execute distributed PyTorch jobs (which is similar to Running a torchrun script) natively on a Kubernetes Cluster,
which manages a cluster’s lifecycle, spin-up, and tear down.
It leverages the open-sourced Kubeflow Operator.
This is like running a transient Pytorch cluster — a type of cluster
spun up for a specific Pytorch job and torn down after completion.


To install the plugin, run the following command:

```shell
$ pip install --pre flyteplugins-pytorch
```

The following example shows how to configure Pytorch in a `TaskEnvironment`. Flyte automatically provisions a Pytorch cluster for each task using this configuration:

{{< code file="/external/unionai-examples/v2/integrations/flyte-plugins/pytorch/pytorch_example.py" lang="python" >}}