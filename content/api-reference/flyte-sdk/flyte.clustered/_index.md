---
title: flyte.clustered
icon: box-seam
version: 2.8.1
variants: +flyte +union
layout: py_api
---

# flyte.clustered

## Directory

### Classes

| Class | Description |
|-|-|
| [`ClusterFailurePolicy`](../flyte.clustered/clusterfailurepolicy) | Failure and restart policy for the JobSet as a whole. |
| [`ClusteredTaskEnvironment`](../flyte.clustered/clusteredtaskenvironment) | A TaskEnvironment that emits a Kubernetes JobSet for distributed multi-node training. |
| [`ClusteredTaskTemplate`](../flyte.clustered/clusteredtasktemplate) | Task template for `ClusteredTaskEnvironment`. |
| [`JaxRun`](../flyte.clustered/jaxrun) | JAX multi-process runtime for a ClusteredTaskEnvironment. |
| [`TorchRun`](../flyte.clustered/torchrun) | TorchRun launcher configuration for a ClusteredTaskEnvironment. |

### Methods

| Method | Description |
|-|-|
| [`jax_initialize()`](#jax_initialize) | Initialize `jax.distributed` for this clustered task's process topology. |


## Methods

#### jax_initialize()

```python
def jax_initialize(
    **overrides: Any,
)
```
Initialize `jax.distributed` for this clustered task's process topology.

Wraps `jax.distributed.initialize` with the coordinator address, process count and process id
that the `clustered` launcher exported for a `JaxRun` environment, and disables JAX's cluster
auto-detection: its Kubernetes detector otherwise activates in every pod and either fails to
import the `kubernetes` client or queries the API without RBAC. Any keyword argument is forwarded
to `jax.distributed.initialize` and wins over the defaults, e.g. `local_device_ids=[0]`.

Safe to call more than once: subsequent calls are no-ops once JAX reports it is initialized.



| Parameter | Type | Description |
|-|-|-|
| `**overrides` | `Any` | |

**Raises**

| Exception | Description |
|-|-|
| `RuntimeError` | when called outside a `JaxRun` clustered task (no process topology in the environment). |

