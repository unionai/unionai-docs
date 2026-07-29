---
title: Kubeflow TensorFlow
version: 1.16.26
variants: +flyte +union
layout: py_api
---

# Kubeflow TensorFlow



## Directory

### Classes

| Class | Description |
|-|-|
| [`flytekitplugins.kftensorflow.task.Chief`](packages/flytekitplugins.kftensorflow.task/chief) |  |
| [`flytekitplugins.kftensorflow.task.CleanPodPolicy`](packages/flytekitplugins.kftensorflow.task/cleanpodpolicy) | CleanPodPolicy describes how to deal with pods when the job is finished. |
| [`flytekitplugins.kftensorflow.task.Evaluator`](packages/flytekitplugins.kftensorflow.task/evaluator) |  |
| [`flytekitplugins.kftensorflow.task.PS`](packages/flytekitplugins.kftensorflow.task/ps) |  |
| [`flytekitplugins.kftensorflow.task.RestartPolicy`](packages/flytekitplugins.kftensorflow.task/restartpolicy) | RestartPolicy describes how the replicas should be restarted. |
| [`flytekitplugins.kftensorflow.task.RunPolicy`](packages/flytekitplugins.kftensorflow.task/runpolicy) | RunPolicy describes a set of policies to apply to the execution of a Kubeflow job. |
| [`flytekitplugins.kftensorflow.task.TensorflowFunctionTask`](packages/flytekitplugins.kftensorflow.task/tensorflowfunctiontask) | Plugin that submits a TFJob (see https://github. |
| [`flytekitplugins.kftensorflow.task.TfJob`](packages/flytekitplugins.kftensorflow.task/tfjob) | Configuration for an executable [`TensorFlow Job`](https://github. |
| [`flytekitplugins.kftensorflow.task.Worker`](packages/flytekitplugins.kftensorflow.task/worker) |  |

### Packages

| Package | Description |
|-|-|
| [`flytekitplugins.kftensorflow.task`](packages/flytekitplugins.kftensorflow.task/_index) | This Plugin adds the capability of running distributed tensorflow training to Flyte using backend plugins, natively on. |

