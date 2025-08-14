---
title: Ray
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: false
---

# Ray

Flyte can execute Ray jobs natively on a Kubernetes Cluster,
which manages a virtual cluster’s lifecycle, spin-up, and tear down.
It leverages the open-sourced https://github.com/ray-project/kuberay and can be
enabled without signing up for any service. This is like running a transient Ray
cluster — a type of cluster spun up for a specific Ray job and torn down after
completion.

To install the plugin, run the following command:

## Install the plugin

To install the Ray plugin, run the following command:

```shell
$ pip install --pre flyteplugins-ray
```
