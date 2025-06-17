---
title: Machine learning
weight: 90
variants: +flyte +serverless +byoc +selfmanaged
---

# Machine learning

Flyte v2 is well-equipped to orchestrate parallelized multi-container operations such as hyperparameter optimization, recursive feature elimination, etc.

## Recursive feature elimination example

The below script performs a recursive feature elimination workflow. In each iteration, each feature is evaluated for importance and the least important feature is dropped.

{{< code file="/external/migrate-to-unionai-examples-flyte2/rfe.py" lang="python" >}}

Each group is shown together in the UI to facilitate easy inspection:

![RFE visualization](../_static/images/user-guide/rfe.png)


