---
title: Elastic
version: 2.0.3
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# Elastic

**Package:** `flyteplugins.pytorch`

Elastic defines the configuration for running a PyTorch elastic job using torch.distributed.

When a worker fails (e.g. CUDA OOM), the elastic agent detects the failure and
restarts all workers as a group. Each restart cycle has a cost determined by the
NCCL timeout settings below. The total worst-case time before the job fails is::

    (max_restarts + 1) * (nccl_collective_timeout_sec + nccl_heartbeat_timeout_sec)

For example, with defaults (max_restarts=3, collective=600s, heartbeat=300s):
4 * 900s = 60 min. With aggressive settings (max_restarts=0, collective=60s,
heartbeat=60s): 1 * 120s = 2 min.



```python
class Elastic(
    nnodes: typing.Union[int, str],
    nproc_per_node: int,
    rdzv_backend: typing.Literal['c10d', 'etcd', 'etcd-v2'],
    run_policy: typing.Optional[flyteplugins.pytorch.task.RunPolicy],
    monitor_interval: int,
    max_restarts: int,
    rdzv_configs: typing.Dict[str, typing.Any],
    nccl_heartbeat_timeout_sec: typing.Optional[int],
    nccl_async_error_handling: bool,
    nccl_collective_timeout_sec: typing.Optional[int],
    nccl_enable_monitoring: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `nnodes` | `typing.Union[int, str]` | Number of nodes to use. Can be a fixed int or a range string (e.g., "2:4" for elastic training). |
| `nproc_per_node` | `int` | Number of processes to launch per node. |
| `rdzv_backend` | `typing.Literal['c10d', 'etcd', 'etcd-v2']` | Rendezvous backend to use. Typically "c10d". Defaults to "c10d". |
| `run_policy` | `typing.Optional[flyteplugins.pytorch.task.RunPolicy]` | Run policy applied to the job execution. Defaults to None. |
| `monitor_interval` | `int` | Interval (in seconds) the elastic agent polls worker process health. Once a worker process exits, detection takes at most this long. Defaults to 3. |
| `max_restarts` | `int` | Maximum number of worker group restarts before the elastic agent gives up and raises ``ChildFailedError``. Each restart kills all workers and relaunches the entire group. If the failure is deterministic (e.g. model too large for GPU memory), restarts just repeat the same failure — set to 0 to fail immediately. Use higher values for transient failures (e.g. spot instance preemption, occasional OOM from variable batch sizes). Defaults to 3. |
| `rdzv_configs` | `typing.Dict[str, typing.Any]` | Rendezvous configuration key-value pairs. Defaults to {"timeout": 900, "join_timeout": 900}. |
| `nccl_heartbeat_timeout_sec` | `typing.Optional[int]` | Timeout in seconds for the NCCL heartbeat monitor thread. After the collective timeout fires and the NCCL watchdog aborts the communicator, the heartbeat monitor waits this long before sending SIGABRT to kill the worker process. This is the second phase of failure detection — it converts a stuck NCCL abort into a hard process kill. Defaults to 300 (5 min) instead of PyTorch's 1800s (30 min). Set to None to use PyTorch default. |
| `nccl_async_error_handling` | `bool` | When True, sets TORCH_NCCL_ASYNC_ERROR_HANDLING=1 so that NCCL aborts stuck collectives asynchronously instead of blocking indefinitely. This causes the worker process to crash-exit on a stuck collective, which the elastic agent detects within ``monitor_interval`` seconds (~3s by default) — much faster than waiting for the heartbeat timeout. Defaults to False (PyTorch default behavior). |
| `nccl_collective_timeout_sec` | `typing.Optional[int]` | Timeout in seconds for individual NCCL collective operations (e.g. all-reduce inside loss.backward()). This is the timeout passed to ``torch.distributed.init_process_group``. When a worker desyncs (e.g. skips a collective after OOM), surviving workers block in the collective for this long before the NCCL watchdog fires. This is the first phase of failure detection. PyTorch default is 600s (10 min). Set to None to use PyTorch default. |
| `nccl_enable_monitoring` | `bool` | When True, sets TORCH_NCCL_ENABLE_MONITORING=1 to activate NCCL's built-in monitoring thread. The monitoring thread checks each worker's heartbeat counter and sends SIGABRT when it stalls, which is what drives ``nccl_heartbeat_timeout_sec``. Defaults to True. |

