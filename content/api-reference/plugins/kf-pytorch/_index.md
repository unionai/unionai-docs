---
title: Kubeflow PyTorch
version: 1.16.28
variants: +flyte +union
layout: py_api
---

# Kubeflow PyTorch



## Directory

### Classes

| Class | Description |
|-|-|
| [`flytekitplugins.kfpytorch.task.CleanPodPolicy`](flytekitplugins.kfpytorch.task#flytekitpluginskfpytorchtaskcleanpodpolicy) | CleanPodPolicy describes how to deal with pods when the job is finished. |
| [`flytekitplugins.kfpytorch.task.Elastic`](flytekitplugins.kfpytorch.task#flytekitpluginskfpytorchtaskelastic) | Configuration for [`torch elastic training`](https://pytorch. |
| [`flytekitplugins.kfpytorch.task.ElasticWorkerResult`](flytekitplugins.kfpytorch.task#flytekitpluginskfpytorchtaskelasticworkerresult) | A named tuple representing the result of a torch elastic worker process. |
| [`flytekitplugins.kfpytorch.task.Master`](flytekitplugins.kfpytorch.task#flytekitpluginskfpytorchtaskmaster) | Configuration for master replica group. |
| [`flytekitplugins.kfpytorch.task.PyTorch`](flytekitplugins.kfpytorch.task#flytekitpluginskfpytorchtaskpytorch) | Configuration for an executable [`PyTorch Job`](https://github. |
| [`flytekitplugins.kfpytorch.task.PyTorchFunctionTask`](flytekitplugins.kfpytorch.task#flytekitpluginskfpytorchtaskpytorchfunctiontask) | Plugin that submits a PyTorchJob (see https://github. |
| [`flytekitplugins.kfpytorch.task.PytorchElasticFunctionTask`](flytekitplugins.kfpytorch.task#flytekitpluginskfpytorchtaskpytorchelasticfunctiontask) | Plugin for distributed training with torch elastic/torchrun (see. |
| [`flytekitplugins.kfpytorch.task.RestartPolicy`](flytekitplugins.kfpytorch.task#flytekitpluginskfpytorchtaskrestartpolicy) | RestartPolicy describes how the replicas should be restarted. |
| [`flytekitplugins.kfpytorch.task.RunPolicy`](flytekitplugins.kfpytorch.task#flytekitpluginskfpytorchtaskrunpolicy) | RunPolicy describes some policy to apply to the execution of a kubeflow job. |
| [`flytekitplugins.kfpytorch.task.Worker`](flytekitplugins.kfpytorch.task#flytekitpluginskfpytorchtaskworker) |  |

### Functions

| Function | Description |
|-|-|
| [`flytekitplugins.kfpytorch.error_handling.create_recoverable_error_file()`](flytekitplugins.kfpytorch.error_handling#create_recoverable_error_file) | Create a file to signal to the agent process that an exception in the worker process is recoverable. |
| [`flytekitplugins.kfpytorch.error_handling.is_recoverable_worker_error()`](flytekitplugins.kfpytorch.error_handling#is_recoverable_worker_error) | Check if the error in the worker process is recoverable. |
| [`flytekitplugins.kfpytorch.pod_template.add_shared_mem_volume_to_pod_template()`](flytekitplugins.kfpytorch.pod_template#add_shared_mem_volume_to_pod_template) | Add shared memory volume and volume mount to the pod template. |
| [`flytekitplugins.kfpytorch.task.spawn_helper()`](flytekitplugins.kfpytorch.task#spawn_helper) | Help to spawn worker processes. |

### Packages

| Package | Description |
|-|-|
| [`flytekitplugins.kfpytorch.error_handling`](flytekitplugins.kfpytorch.error_handling) | Handle errors in elastic training jobs. |
| [`flytekitplugins.kfpytorch.pod_template`](flytekitplugins.kfpytorch.pod_template) |  |
| [`flytekitplugins.kfpytorch.task`](flytekitplugins.kfpytorch.task) | This Plugin adds the capability of running distributed pytorch training to Flyte using backend plugins, natively on. |

