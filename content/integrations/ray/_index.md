---
title: Ray
weight: 1
variants: +flyte +union
---

# Ray

The Ray plugin lets you run [Ray](https://www.ray.io/) jobs natively on Kubernetes. Flyte provisions a transient Ray cluster for each task execution using [KubeRay](https://github.com/ray-project/kuberay) and tears it down on completion.

## When to use this plugin

- Distributed Python workloads (parallel computation, data processing)
- ML training with Ray Train or hyperparameter tuning with Ray Tune
- Ray Serve inference workloads
- Any workload that benefits from Ray's actor model or task parallelism

## Installation

```bash
pip install flyteplugins-ray
```

Your task image must also include a compatible version of Ray:

```python
image = (
    flyte.Image.from_debian_base(name="ray")
    .with_pip_packages("ray[default]==2.46.0", "flyteplugins-ray")
)
```

## Configuration

Create a `RayJobConfig` and pass it as `plugin_config` to a `TaskEnvironment`:

```python
from flyteplugins.ray import HeadNodeConfig, RayJobConfig, WorkerNodeConfig

ray_config = RayJobConfig(
    head_node_config=HeadNodeConfig(ray_start_params={"log-color": "True"}),
    worker_node_config=[WorkerNodeConfig(group_name="ray-group", replicas=2)],
    runtime_env={"pip": ["numpy", "pandas"]},
    enable_autoscaling=False,
    shutdown_after_job_finishes=True,
    ttl_seconds_after_finished=300,
)

ray_env = flyte.TaskEnvironment(
    name="ray_env",
    plugin_config=ray_config,
    image=image,
)
```

### `RayJobConfig` parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `worker_node_config` | `List[WorkerNodeConfig]` | **Required.** List of worker group configurations |
| `head_node_config` | `HeadNodeConfig` | Head node configuration (optional) |
| `enable_autoscaling` | `bool` | Enable Ray autoscaler (default: `False`) |
| `runtime_env` | `dict` | Ray runtime environment (pip packages, env vars, etc.) |
| `address` | `str` | Connect to an existing Ray cluster instead of provisioning one |
| `shutdown_after_job_finishes` | `bool` | Shut down the cluster after the job completes (default: `False`) |
| `ttl_seconds_after_finished` | `int` | Seconds to keep the cluster after completion before cleanup |

### `WorkerNodeConfig` parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `group_name` | `str` | **Required.** Name of this worker group |
| `replicas` | `int` | **Required.** Number of worker replicas |
| `min_replicas` | `int` | Minimum replicas (for autoscaling) |
| `max_replicas` | `int` | Maximum replicas (for autoscaling) |
| `ray_start_params` | `Dict[str, str]` | Ray start parameters for workers |
| `requests` | `Resources` | Resource requests per worker |
| `limits` | `Resources` | Resource limits per worker |
| `pod_template` | `PodTemplate` | Full pod template (mutually exclusive with `requests`/`limits`) |

### `HeadNodeConfig` parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `ray_start_params` | `Dict[str, str]` | Ray start parameters for the head node |
| `requests` | `Resources` | Resource requests for the head node |
| `limits` | `Resources` | Resource limits for the head node |
| `pod_template` | `PodTemplate` | Full pod template (mutually exclusive with `requests`/`limits`) |

### Connecting to an existing cluster

To connect to an existing Ray cluster instead of provisioning a new one, set the `address` parameter:

```python
ray_config = RayJobConfig(
    worker_node_config=[WorkerNodeConfig(group_name="ray-group", replicas=2)],
    address="ray://existing-cluster:10001",
)
```

## Examples

The following example shows how to configure Ray in a `TaskEnvironment`. Flyte automatically provisions a Ray cluster for each task using this configuration:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/ray/ray_example.py" lang="python" >}}

The next example demonstrates how Flyte can create ephemeral Ray clusters and run a subtask that connects to an existing Ray cluster:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/ray/ray_existing_example.py" lang="python" >}}

## API reference

See the [Ray API reference](../../api-reference/integrations/ray/_index) for full details.
