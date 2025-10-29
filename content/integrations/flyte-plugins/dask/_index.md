---
title: Dask
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: false
---

# Dask

Flyte can execute Dask jobs natively on a Kubernetes Cluster,
which manages a cluster’s lifecycle, spin-up, and tear down. It leverages
the open-sourced Dask Kubernetes Operator and can be enabled without signing up for
any service. This is like running a transient Dask cluster — a type of cluster
spun up for a specific Dask job and torn down after completion.

To install the plugin, run the following command:

## Install the plugin

To install the Dask plugin, run the following command:

```shell
$ pip install --pre flyteplugins-dask
```

The following example shows how to configure Dask in a `TaskEnvironment`. Flyte automatically provisions a Dask cluster for each task using this configuration:

{{< code file="/external/unionai-examples/v2/integrations/flyte-plugins/dask/dask_example.py" lang="python" >}}