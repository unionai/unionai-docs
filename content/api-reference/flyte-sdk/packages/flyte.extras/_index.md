---
title: flyte.extras
version: 2.0.7
variants: +flyte +byoc +selfmanaged
layout: py_api
sidebar_expanded: true
---

# flyte.extras


Flyte extras package.
This package provides various utilities that make it possible to build highly customized workflows.

1. ContainerTask: Execute arbitrary pre-containerized applications, without needing the `flyte-sdk`
                  to be installed. This extra uses `flyte copilot` system to inject inputs and slurp
                  outputs from the container run.

2. DynamicBatcher / TokenBatcher: Maximize resource utilization by batching work from many concurrent
                   producers through a single async processing function.  DynamicBatcher is the
                   general-purpose base; TokenBatcher is a convenience subclass for token-budgeted
                   LLM inference with reusable containers.

## Directory

### Classes

| Class | Description |
|-|-|
| [`BatchStats`](../flyte.extras/batchstats) | Monitoring statistics exposed by :attr:`DynamicBatcher. |
| [`ContainerTask`](../flyte.extras/containertask) | This is an intermediate class that represents Flyte Tasks that run a container at execution time. |
| [`DynamicBatcher`](../flyte.extras/dynamicbatcher) | Batches records from many concurrent producers and runs them through. |
| [`Prompt`](../flyte.extras/prompt) | Simple prompt record with built-in token estimation. |
| [`TokenBatcher`](../flyte.extras/tokenbatcher) | Token-aware batcher for LLM inference workloads. |

### Protocols

| Protocol | Description |
|-|-|
| [`CostEstimator`](../flyte.extras/costestimator) | Protocol for records that can estimate their own processing cost. |
| [`TokenEstimator`](../flyte.extras/tokenestimator) | Protocol for records that can estimate their own token count. |

