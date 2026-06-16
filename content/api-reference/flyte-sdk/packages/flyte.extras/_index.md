---
title: flyte.extras
version: 2.4.4
variants: +flyte +union
layout: py_api
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

3. Sleep: Route a task to the backend `core-sleep` plugin, which executes in leaseworker with no
                   task pod.

4. Shell: Wrap a CLI tool packaged in a container image. Designed as the foundation for
                bio module libraries (bedtools, samtools, bcftools, GATK, etc.) and any other case
                where a user wants to call a pre-built binary in a published container with
                typed inputs and outputs.
## Directory

### Classes

| Class | Description |
|-|-|
| [`BatchStats`](../flyte.extras/batchstats) | Monitoring statistics exposed by `DynamicBatcher. |
| [`ContainerTask`](../flyte.extras/containertask) | This is an intermediate class that represents Flyte Tasks that run a container at execution time. |
| [`DynamicBatcher`](../flyte.extras/dynamicbatcher) | Batches records from many concurrent producers and runs them through. |
| [`Prompt`](../flyte.extras/prompt) | Simple prompt record with built-in token estimation. |
| [`Sleep`](../flyte.extras/sleep) | Route a task to the backend `core-sleep` plugin. |
| [`SleepTask`](../flyte.extras/sleeptask) |  |
| [`TokenBatcher`](../flyte.extras/tokenbatcher) | Token-aware batcher for LLM inference workloads. |

### Protocols

| Protocol | Description |
|-|-|
| [`CostEstimator`](../flyte.extras/costestimator) | Protocol for records that can estimate their own processing cost. |
| [`TokenEstimator`](../flyte.extras/tokenestimator) | Protocol for records that can estimate their own token count. |

