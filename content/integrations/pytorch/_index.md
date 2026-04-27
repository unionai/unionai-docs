---
title: PyTorch
weight: 1
variants: +flyte +union
---

# PyTorch

The PyTorch plugin lets you run distributed [PyTorch](https://pytorch.org/) training jobs natively on Kubernetes. It uses the [Kubeflow Training Operator](https://github.com/kubeflow/training-operator) to manage multi-node training with PyTorch's elastic launch (`torchrun`).

## When to use this plugin

- Single-node or multi-node distributed training with `DistributedDataParallel` (DDP)
- Elastic training that can scale up and down during execution
- Any workload that uses `torch.distributed` for data-parallel or model-parallel training

## Installation

```bash
pip install flyteplugins-pytorch
```

## Configuration

Create an `Elastic` configuration and pass it as `plugin_config` to a `TaskEnvironment`:

```python
from flyteplugins.pytorch import Elastic

torch_env = flyte.TaskEnvironment(
    name="torch_env",
    resources=flyte.Resources(cpu=(1, 2), memory=("1Gi", "2Gi")),
    plugin_config=Elastic(
        nnodes=2,
        nproc_per_node=1,
    ),
    image=image,
)
```

### `Elastic` parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `nnodes` | `int` or `str` | **Required.** Number of nodes. Use an int for a fixed count or a range string (e.g., `"2:4"`) for elastic training |
| `nproc_per_node` | `int` | **Required.** Number of processes (workers) per node |
| `rdzv_backend` | `str` | Rendezvous backend: `"c10d"` (default), `"etcd"`, or `"etcd-v2"` |
| `max_restarts` | `int` | Maximum worker group restarts (default: `3`) |
| `monitor_interval` | `int` | Agent health check interval in seconds (default: `3`) |
| `run_policy` | `RunPolicy` | Job run policy (cleanup, TTL, deadlines, retries) |

### `RunPolicy` parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `clean_pod_policy` | `str` | Pod cleanup policy: `"None"`, `"all"`, or `"Running"` |
| `ttl_seconds_after_finished` | `int` | Seconds to keep pods after job completion |
| `active_deadline_seconds` | `int` | Maximum time the job can run (seconds) |
| `backoff_limit` | `int` | Number of retries before marking the job as failed |

### NCCL tuning parameters

The plugin includes built-in NCCL timeout tuning to reduce failure-detection latency (PyTorch defaults to 1800 seconds):

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `nccl_heartbeat_timeout_sec` | `int` | `300` | NCCL heartbeat timeout (seconds) |
| `nccl_async_error_handling` | `bool` | `False` | Enable async NCCL error handling |
| `nccl_collective_timeout_sec` | `int` | `None` | Timeout for NCCL collective operations |
| `nccl_enable_monitoring` | `bool` | `True` | Enable NCCL monitoring |

### Writing a distributed training task

Tasks using this plugin do not need to be `async`. Initialize the process group and use `DistributedDataParallel` as you normally would with `torchrun`:

```python
import torch
import torch.distributed
from torch.nn.parallel import DistributedDataParallel as DDP

@torch_env.task
def train(epochs: int) -> float:
    torch.distributed.init_process_group("gloo")
    model = DDP(MyModel())
    # ... training loop ...
    return final_loss
```

> [!NOTE]
> When `nnodes=1`, the task runs as a regular Python task (no Kubernetes training job is created). Set `nnodes >= 2` for multi-node distributed training.

## Example

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/pytorch/pytorch_example.py" lang="python" >}}

## API reference

See the [PyTorch API reference](../../api-reference/integrations/pytorch/_index) for full details.
