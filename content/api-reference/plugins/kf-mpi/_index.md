---
title: Kubeflow MPI
version: 1.16.28
variants: +flyte +union
layout: py_api
---

# Kubeflow MPI



## Directory

### Classes

| Class | Description |
|-|-|
| [`flytekitplugins.kfmpi.task.CleanPodPolicy`](flytekitplugins.kfmpi.task#flytekitpluginskfmpitaskcleanpodpolicy) | CleanPodPolicy describes how to deal with pods when the job is finished. |
| [`flytekitplugins.kfmpi.task.HorovodFunctionTask`](flytekitplugins.kfmpi.task#flytekitpluginskfmpitaskhorovodfunctiontask) | For more info, check out https://github. |
| [`flytekitplugins.kfmpi.task.HorovodJob`](flytekitplugins.kfmpi.task#flytekitpluginskfmpitaskhorovodjob) | Configuration for an executable [`Horovod Job using MPI operator`](https://github. |
| [`flytekitplugins.kfmpi.task.Launcher`](flytekitplugins.kfmpi.task#flytekitpluginskfmpitasklauncher) | Launcher replica configuration. |
| [`flytekitplugins.kfmpi.task.MPIFunctionTask`](flytekitplugins.kfmpi.task#flytekitpluginskfmpitaskmpifunctiontask) | Plugin that submits a MPIJob (see https://github. |
| [`flytekitplugins.kfmpi.task.MPIJob`](flytekitplugins.kfmpi.task#flytekitpluginskfmpitaskmpijob) | Configuration for an executable [`MPI Job`](https://github. |
| [`flytekitplugins.kfmpi.task.RestartPolicy`](flytekitplugins.kfmpi.task#flytekitpluginskfmpitaskrestartpolicy) | RestartPolicy describes how the replicas should be restarted. |
| [`flytekitplugins.kfmpi.task.RunPolicy`](flytekitplugins.kfmpi.task#flytekitpluginskfmpitaskrunpolicy) | RunPolicy describes some policy to apply to the execution of a kubeflow job. |
| [`flytekitplugins.kfmpi.task.Worker`](flytekitplugins.kfmpi.task#flytekitpluginskfmpitaskworker) | Worker replica configuration. |

### Packages

| Package | Description |
|-|-|
| [`flytekitplugins.kfmpi.task`](flytekitplugins.kfmpi.task) | This Plugin adds the capability of running distributed MPI training to Flyte using backend plugins, natively on. |

