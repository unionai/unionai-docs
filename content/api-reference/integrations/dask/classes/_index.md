---
title: Classes
version: 2.0.0b53
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Classes

| Class | Description |
|-|-|
| [`flyteplugins.dask.Dask`](../packages/flyteplugins.dask/dask) |Configuration for the dask task. |
| [`flyteplugins.dask.Scheduler`](../packages/flyteplugins.dask/scheduler) |Configuration for the scheduler pod. |
| [`flyteplugins.dask.WorkerGroup`](../packages/flyteplugins.dask/workergroup) |Configuration for a group of dask worker pods. |
| [`flyteplugins.dask.task.Dask`](../packages/flyteplugins.dask.task/dask) |Configuration for the dask task. |
| [`flyteplugins.dask.task.DaskTask`](../packages/flyteplugins.dask.task/dasktask) |Actual Plugin that transforms the local python code for execution within a spark context. |
| [`flyteplugins.dask.task.DownloadCodeBundleSchedulerPlugin`](../packages/flyteplugins.dask.task/downloadcodebundleschedulerplugin) |A Dask plugin to download and set up the code bundle on the scheduler. |
| [`flyteplugins.dask.task.DownloadCodeBundleWorkerPlugin`](../packages/flyteplugins.dask.task/downloadcodebundleworkerplugin) |A Dask plugin to download and set up the code bundle on each worker. |
| [`flyteplugins.dask.task.Scheduler`](../packages/flyteplugins.dask.task/scheduler) |Configuration for the scheduler pod. |
| [`flyteplugins.dask.task.WorkerGroup`](../packages/flyteplugins.dask.task/workergroup) |Configuration for a group of dask worker pods. |
