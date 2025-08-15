---
title: Spark
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: false
---

# Spark

Flyte can execute Spark jobs natively on a Kubernetes Cluster,
which manages a virtual cluster’s lifecycle, spin-up, and tear down. It leverages
the open-sourced Spark On K8s Operator and can be enabled without signing up for
any service. This is like running a transient Spark cluster — a type of cluster
spun up for a specific Spark job and torn down after completion.

To install the plugin, run the following command:

```bash
pip install --pre flyteplugins-spark
```
