---
title: flyteplugins.dask.task
version: 2.0.0b52
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flyteplugins.dask.task

## Directory

### Classes

| Class | Description |
|-|-|
| [`Dask`](../flyteplugins.dask.task/dask) | Configuration for the dask task. |
| [`DaskTask`](../flyteplugins.dask.task/dasktask) | Actual Plugin that transforms the local python code for execution within a spark context. |
| [`DownloadCodeBundleSchedulerPlugin`](../flyteplugins.dask.task/downloadcodebundleschedulerplugin) | A Dask plugin to download and set up the code bundle on the scheduler. |
| [`DownloadCodeBundleWorkerPlugin`](../flyteplugins.dask.task/downloadcodebundleworkerplugin) | A Dask plugin to download and set up the code bundle on each worker. |
| [`Scheduler`](../flyteplugins.dask.task/scheduler) | Configuration for the scheduler pod. |
| [`WorkerGroup`](../flyteplugins.dask.task/workergroup) | Configuration for a group of dask worker pods. |

