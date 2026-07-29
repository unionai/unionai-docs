---
title: Kubeflow MPI
version: 1.16.26
variants: +flyte +union
layout: py_api
---

# Kubeflow MPI



## Directory

### Classes

| Class | Description |
|-|-|
| [`flytekitplugins.kfmpi.task.CleanPodPolicy`](packages/flytekitplugins.kfmpi.task/cleanpodpolicy) | CleanPodPolicy describes how to deal with pods when the job is finished. |
| [`flytekitplugins.kfmpi.task.HorovodFunctionTask`](packages/flytekitplugins.kfmpi.task/horovodfunctiontask) | For more info, check out https://github. |
| [`flytekitplugins.kfmpi.task.HorovodJob`](packages/flytekitplugins.kfmpi.task/horovodjob) | Configuration for an executable [`Horovod Job using MPI operator`](https://github. |
| [`flytekitplugins.kfmpi.task.Launcher`](packages/flytekitplugins.kfmpi.task/launcher) | Launcher replica configuration. |
| [`flytekitplugins.kfmpi.task.MPIFunctionTask`](packages/flytekitplugins.kfmpi.task/mpifunctiontask) | Plugin that submits a MPIJob (see https://github. |
| [`flytekitplugins.kfmpi.task.MPIJob`](packages/flytekitplugins.kfmpi.task/mpijob) | Configuration for an executable [`MPI Job`](https://github. |
| [`flytekitplugins.kfmpi.task.RestartPolicy`](packages/flytekitplugins.kfmpi.task/restartpolicy) | RestartPolicy describes how the replicas should be restarted. |
| [`flytekitplugins.kfmpi.task.RunPolicy`](packages/flytekitplugins.kfmpi.task/runpolicy) | RunPolicy describes some policy to apply to the execution of a kubeflow job. |
| [`flytekitplugins.kfmpi.task.Worker`](packages/flytekitplugins.kfmpi.task/worker) | Worker replica configuration. |

### Packages

| Package | Description |
|-|-|
| [`flytekitplugins.kfmpi.task`](packages/flytekitplugins.kfmpi.task/_index) | This Plugin adds the capability of running distributed MPI training to Flyte using backend plugins, natively on. |

