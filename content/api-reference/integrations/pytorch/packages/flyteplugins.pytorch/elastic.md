---
title: Elastic
version: 2.0.0b59
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Elastic

**Package:** `flyteplugins.pytorch`

Elastic defines the configuration for running a PyTorch elastic job using torch.distributed.



```python
class Elastic(
    nnodes: typing.Union[int, str],
    nproc_per_node: int,
    rdzv_backend: typing.Literal['c10d', 'etcd', 'etcd-v2'],
    run_policy: typing.Optional[flyteplugins.pytorch.task.RunPolicy],
    monitor_interval: int,
    max_restarts: int,
    rdzv_configs: typing.Dict[str, typing.Any],
)
```
| Parameter | Type | Description |
|-|-|-|
| `nnodes` | `typing.Union[int, str]` | Number of nodes to use. Can be a fixed int or a range string (e.g., "2:4" for elastic training). |
| `nproc_per_node` | `int` | Number of processes to launch per node. |
| `rdzv_backend` | `typing.Literal['c10d', 'etcd', 'etcd-v2']` | Rendezvous backend to use. Typically "c10d". Defaults to "c10d". |
| `run_policy` | `typing.Optional[flyteplugins.pytorch.task.RunPolicy]` | Run policy applied to the job execution. Defaults to None. |
| `monitor_interval` | `int` | Interval (in seconds) to monitor the job's state. Defaults to 3. |
| `max_restarts` | `int` | Maximum number of worker group restarts before failing the job. Defaults to 3. |
| `rdzv_configs` | `typing.Dict[str, typing.Any]` | Rendezvous configuration key-value pairs. Defaults to {"timeout": 900, "join_timeout": 900}. |

