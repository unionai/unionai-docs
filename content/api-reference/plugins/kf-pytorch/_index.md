---
title: Kubeflow PyTorch
version: 1.16.26
variants: +flyte +union
layout: py_api
---

# Kubeflow PyTorch



## Directory

### Classes

| Class | Description |
|-|-|
| [`flytekitplugins.kfpytorch.task.CleanPodPolicy`](packages/flytekitplugins.kfpytorch.task/cleanpodpolicy) | CleanPodPolicy describes how to deal with pods when the job is finished. |
| [`flytekitplugins.kfpytorch.task.Elastic`](packages/flytekitplugins.kfpytorch.task/elastic) | Configuration for [`torch elastic training`](https://pytorch. |
| [`flytekitplugins.kfpytorch.task.ElasticWorkerResult`](packages/flytekitplugins.kfpytorch.task/elasticworkerresult) | A named tuple representing the result of a torch elastic worker process. |
| [`flytekitplugins.kfpytorch.task.Master`](packages/flytekitplugins.kfpytorch.task/master) | Configuration for master replica group. |
| [`flytekitplugins.kfpytorch.task.PyTorch`](packages/flytekitplugins.kfpytorch.task/pytorch) | Configuration for an executable [`PyTorch Job`](https://github. |
| [`flytekitplugins.kfpytorch.task.PyTorchFunctionTask`](packages/flytekitplugins.kfpytorch.task/pytorchfunctiontask) | Plugin that submits a PyTorchJob (see https://github. |
| [`flytekitplugins.kfpytorch.task.PytorchElasticFunctionTask`](packages/flytekitplugins.kfpytorch.task/pytorchelasticfunctiontask) | Plugin for distributed training with torch elastic/torchrun (see. |
| [`flytekitplugins.kfpytorch.task.RestartPolicy`](packages/flytekitplugins.kfpytorch.task/restartpolicy) | RestartPolicy describes how the replicas should be restarted. |
| [`flytekitplugins.kfpytorch.task.RunPolicy`](packages/flytekitplugins.kfpytorch.task/runpolicy) | RunPolicy describes some policy to apply to the execution of a kubeflow job. |
| [`flytekitplugins.kfpytorch.task.Worker`](packages/flytekitplugins.kfpytorch.task/worker) |  |

### Packages

| Package | Description |
|-|-|
| [`flytekitplugins.kfpytorch.error_handling`](packages/flytekitplugins.kfpytorch.error_handling/_index) | Handle errors in elastic training jobs. |
| [`flytekitplugins.kfpytorch.pod_template`](packages/flytekitplugins.kfpytorch.pod_template/_index) |  |
| [`flytekitplugins.kfpytorch.task`](packages/flytekitplugins.kfpytorch.task/_index) | This Plugin adds the capability of running distributed pytorch training to Flyte using backend plugins, natively on. |

